"""Equation-discovery and system-identification baselines for OOL, all fed the same information as the agent: the same episodes, the same actuator
model x1_pred (IV-AR), the same skeleton (a, b3, k) from the u2-only episode, and a hidden-state reconstruction (tuned RTS-Kalman | learned GRU | oracle).
Target: the coupling drive  phi(t) = d x2hat/dt + a x2hat - k u2.  Inputs: vars = [x1 midpoint, x1 lags 1,3..9, x2hat]  (tapped delay line, generic).
Predictions are made by simulating  x2' = -a x2 + k u2 + phi(vars)  (fixed-step, 4 substeps, ZOH) and x3' = -b3 x3 + x2."""
from __future__ import annotations
import warnings
import numpy as np
from scipy.signal import savgol_filter
from ..sdw import hyp as H0, agent as A
from .bench import DT, T, SUB

warnings.filterwarnings("ignore")
LAGS = (1, 3, 4, 5, 6, 7, 8, 9)
VNAMES = ["x"] + [f"l{k}" for k in LAGS] + ["x2h"]
CLIP = 20.0


def lagmat(e):
    out = [np.concatenate([np.zeros((e.shape[0], k)), e[:, :-k]], 1) for k in LAGS]
    return out


def kalman_x2(U, Y, st, sg, q):
    return np.stack([A.kalman_x2(Y[e, :, 1], U[e, :, 1], st["a"], st["b3"], st["k"], sg, q=q) for e in range(len(U))])


def x2_source(U, Y, st, sg, source, est_models=None, x2true=None, q=4.0):
    if source == "kalman": return kalman_x2(U, Y, st, sg, q)
    if source == "oracle": return x2true
    if source == "learned":
        from ..sdw import rep
        return np.mean([rep.infer(m, Y[..., 1], U[..., 1]) for m in est_models], 0)
    raise ValueError(source)


def eq_data(U, Y, x2h, st):
    """Training table for the coupling drive.  Returns V [N,10] (vars), D [N] (phi target)."""
    xe, xm = H0.x1_ends_mid(U[..., 0], st["al"], st["be"]); d1 = savgol_filter(x2h, 9, 3, deriv=1, delta=DT, axis=-1)
    D = d1 + st["a"] * x2h - st["k"] * U[..., 1]
    V = np.stack([xm] + lagmat(xe) + [x2h], -1)
    return V.reshape(-1, V.shape[-1]), D.ravel()


def simulate(f, st, Ut, full=False):
    """f(V [R,10], u2 [R]) -> drive (full=False: added to -a x2 + k u2) or the whole dx2/dt (full=True).  Fixed step, SUB substeps, ZOH per sample.
    Returns (x3 [R,T], diverged flag).  Output clipped at +-CLIP per derivative; divergence = |x2| > 1e3 at any substep."""
    xe, xm = H0.x1_ends_mid(Ut[..., 0], st["al"], st["be"]); L = lagmat(xe); R = Ut.shape[0]; h = DT / SUB
    x2 = np.zeros(R); x3 = np.zeros(R); out = np.empty((R, T)); div = False
    for t in range(T):
        V = np.stack([xm[:, t]] + [l[:, t] for l in L] + [x2], 1)
        d = np.clip(np.asarray(f(V, Ut[:, t, 1]), float).reshape(-1), -CLIP, CLIP)
        for _ in range(SUB):
            dx = d if full else (-st["a"] * x2 + st["k"] * Ut[:, t, 1] + d)
            x2 = x2 + h * dx; x3 = x3 + h * (-st["b3"] * x3 + x2)
            if np.any(np.abs(x2) > 1e3): div = True; x2 = np.clip(x2, -1e3, 1e3)
        out[:, t] = x3
    return out, div


# --------------------------------------------------------------------- SINDy family (pysindy 2.1.0)
def _libs(kind):
    import pysindy as ps
    if kind == "poly3": return ps.PolynomialLibrary(degree=3)
    if kind == "poly2": return ps.PolynomialLibrary(degree=2)
    if kind == "expanded":                                                     # poly2 + per-variable cubes + Fourier (sin/cos k=1..6)
        return ps.ConcatLibrary([ps.PolynomialLibrary(degree=2), ps.PolynomialLibrary(degree=3, include_interaction=False), ps.FourierLibrary(n_frequencies=6)])
    raise ValueError(kind)


def fit_sindy(U, Y, x2h, st, form, lib, thr, vsel="lags"):
    """SINDYc (explicit) or weak-form SINDy with control on the reconstructed hidden state: x = x2hat, controls = [x1 midpoint (+ x1 lags if vsel == 'lags'), u2];
    the whole x2' is learned.  Returns f(V, u2) for simulate(full=True)."""
    import pysindy as ps
    xe, xm = H0.x1_ends_mid(U[..., 0], st["al"], st["be"]); E = U.shape[0]; ci = [0] + (list(range(1, 9)) if vsel == "lags" else [])
    Vs = np.concatenate([np.stack([xm] + lagmat(xe), -1)[..., ci], U[..., 1:2]], -1)
    xs = [x2h[e][:, None] for e in range(E)]; us = [Vs[e] for e in range(E)]
    if form == "sindyc":
        D = savgol_filter(x2h, 9, 3, deriv=1, delta=DT, axis=-1)
        m = ps.SINDy(optimizer=ps.STLSQ(threshold=thr), feature_library=_libs(lib)); m.fit(xs, t=DT, x_dot=[D[e][:, None] for e in range(E)], u=us)
        pred = lambda inp: m.predict(inp[:, :1], u=inp[:, 1:])[:, 0]
    else:                                                                   # weak form needs a >=2-column state in pysindy 2.1.0: state = [x2hat, x1 midpoint], controls = [lags, u2]
        wl = ps.WeakPDELibrary(_libs(lib), spatiotemporal_grid=np.arange(T) * DT, is_uniform=True, K=200, include_interaction=False)
        xs2 = [np.stack([x2h[e], Vs[e][:, 0]], 1) for e in range(E)]; us2 = [Vs[e][:, 1:] for e in range(E)]
        m = ps.SINDy(optimizer=ps.STLSQ(threshold=thr), feature_library=wl); m.fit(xs2, t=DT, u=us2)
        fl = _libs(lib); fl.fit(np.concatenate([np.concatenate(xs2, 0), np.concatenate(us2, 0)], 1)); coef = m.coefficients()[0]
        pred = lambda inp: np.asarray(fl.transform(inp)) @ np.asarray(coef)
        return lambda V, u2: pred(np.concatenate([V[:, [-1]], V[:, [0]], V[:, ci[1:]], u2[:, None]], 1))
    return lambda V, u2: pred(np.concatenate([V[:, [-1]], V[:, ci], u2[:, None]], 1))


def fit_implicit(U, Y, x2h, st, thr):
    """Implicit-SINDy (SINDy-PI style, Kaheman et al. 2020): regress the target on a library that contains target-dependent (rational) terms.
    phi = (sum_i c_i p_i(v)) / (1 - sum_j d_j q_j(v)) is fitted by sparse regression of phi on [p_i(v), phi*q_j(v)] with STLSQ; prediction solves for phi."""
    V, D = eq_data(U, Y, x2h, st)
    P = _poly2(V); Qv = V[:, [0, -1]]; Q = np.concatenate([np.ones((len(V), 1)), Qv, np.sin(3 * V[:, [0]]), np.cos(3 * V[:, [0]])], 1)
    Th = np.concatenate([P, D[:, None] * Q[:, 1:3]], 1)
    sc = np.maximum(np.abs(Th).max(0), 1e-9); Z = Th / sc
    c = _stlsq(Z, D, thr) / sc; npoly = P.shape[1]

    def phi(Vq):
        Pq = _poly2(Vq); num = Pq @ c[:npoly]; den = 1.0 - Vq[:, [0, -1]] @ c[npoly:]
        den = np.where(np.abs(den) < 0.2, 0.2 * np.sign(den + 1e-12), den); return num / den
    return phi


def _poly2(V):
    n = V.shape[1]; iu = np.triu_indices(n)
    return np.concatenate([np.ones((len(V), 1)), V, (V[:, :, None] * V[:, None, :])[:, iu[0], iu[1]]], 1)


def _stlsq(Z, y, thr, it=10):
    w = np.linalg.lstsq(Z, y, rcond=1e-8)[0]
    for _ in range(it):
        small = np.abs(w) < thr; w[small] = 0
        if (~small).sum() == 0: break
        w[~small] = np.linalg.lstsq(Z[:, ~small], y, rcond=1e-8)[0]
    return w


# --------------------------------------------------------------------------- PySR
def pysr_fit(V, D, lib, seed, niter=40, timeout=60):
    from pysr import PySRRegressor
    fixed = dict(binary_operators=["+", "-", "*"], unary_operators=["square", "cube", "tanh"])
    expanded = dict(binary_operators=["+", "-", "*", "/", "max"], unary_operators=["square", "cube", "tanh", "abs", "sin", "exp", "sign", "sqrt_abs(x) = sqrt(abs(x))"],
                    extra_sympy_mappings={"sqrt_abs": lambda x: __import__("sympy").sqrt(__import__("sympy").Abs(x))})
    cfg = fixed if lib == "fixed" else expanded
    m = PySRRegressor(niterations=niter, populations=12, population_size=30, maxsize=22, parallelism="serial", deterministic=True, random_state=seed,
                      progress=False, verbosity=0, timeout_in_seconds=timeout, model_selection="best", **cfg)
    m.fit(V, D, variable_names=VNAMES)
    return m


# ------------------------------------------------- tuned classical state reconstruction (ML-fitted RTS smoother)
def _kf_mats(a, b3, k, q):
    from scipy.linalg import expm
    Ac = np.array([[-a, 0.0], [1.0, -b3]]); Ad = expm(Ac * DT); Bd = np.linalg.solve(Ac, Ad - np.eye(2)) @ np.array([k, 0.0])
    return Ad, Bd, np.diag([q * DT, 1e-8])


def _kf(y, u2, th, sig, smooth=False):
    """Batched (over episodes) Kalman filter for x2' = -a x2 + k u2 + w (var q), x3' = -b3 x3 + x2, y = x3 + e (sig).  Returns -loglik (and smoothed x2)."""
    a, b3, k, q = np.exp(th); Ad, Bd, Q = _kf_mats(a, b3, k, q); E, n = y.shape
    x = np.zeros((E, 2)); P = np.tile(np.diag([1.0, 1e-4]), (E, 1, 1)); ll = 0.0; xp, Pp, xf, Pf = [], [], [], []
    for t in range(n):
        x = x @ Ad.T + u2[:, t, None] * Bd[None]; P = Ad @ P @ Ad.T + Q
        xp.append(x.copy()); Pp.append(P.copy()); S = P[:, 1, 1] + sig ** 2; v = y[:, t] - x[:, 1]; K = P[:, :, 1] / S[:, None]
        ll += -0.5 * np.sum(np.log(S) + v ** 2 / S); x = x + K * v[:, None]; P = P - K[:, :, None] * P[:, None, 1, :]; xf.append(x.copy()); Pf.append(P.copy())
    if not smooth: return -ll
    xs = np.array(xf); out = xs.copy()
    for t in range(n - 2, -1, -1):
        C = Pf[t] @ Ad.T @ np.linalg.inv(Pp[t + 1]); out[t] = xf[t] + np.einsum("eij,ej->ei", C, out[t + 1] - xp[t + 1])
    return out[:, :, 0].T


QGRID = (0.1, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)


def kalman_prof(U, Y, st, sg):
    """Tuned classical reconstruction: skeleton (a, b3, k) from the u2-only episode, process-noise level q chosen by innovation likelihood over all collected
    episodes.  (Joint ML over (a,b3,k,q) was tried and rejected: it converges to a degenerate slow solution because the unknown coupling is not white noise.)"""
    y, u2 = Y[..., 1], U[..., 1]; th = lambda q: np.log([st["a"], st["b3"], max(st["k"], 0.05), q])
    q = min(QGRID, key=lambda q: _kf(y, u2, th(q), sg))
    return _kf(y, u2, th(q), sg, smooth=True), q


# ------------------------------------- role A: symbolic regression on raw observations (no latent state)
RAW_NAMES = ["x"] + [f"l{k}" for k in LAGS] + ["x3", "u2"]


def raw_data(U, Y, st):
    xe, xm = H0.x1_ends_mid(U[..., 0], st["al"], st["be"]); y3 = savgol_filter(Y[..., 1], 9, 3, axis=-1); d3 = savgol_filter(Y[..., 1], 9, 3, deriv=1, delta=DT, axis=-1)
    V = np.stack([xm] + lagmat(xe) + [y3, U[..., 1]], -1); return V.reshape(-1, V.shape[-1]), d3.ravel()


def simulate_raw(f, st, Ut):
    """x3' = f([x1 mid, x1 lags, x3, u2]) - a first-order observed-variable model (no latent state)."""
    xe, xm = H0.x1_ends_mid(Ut[..., 0], st["al"], st["be"]); L = lagmat(xe); R = Ut.shape[0]; h = DT / SUB; x3 = np.zeros(R); out = np.empty((R, T)); div = False
    for t in range(T):
        for _ in range(SUB):
            V = np.stack([xm[:, t]] + [l[:, t] for l in L] + [x3, Ut[:, t, 1]], 1)
            x3 = np.clip(x3 + h * np.clip(np.asarray(f(V), float).reshape(-1), -CLIP, CLIP), -CLIP, CLIP)
        out[:, t] = x3
    return out, div


def pysr_fit_raw(V, D, seed, niter=40, timeout=60):
    from pysr import PySRRegressor
    m = PySRRegressor(niterations=niter, populations=12, population_size=30, maxsize=22, parallelism="serial", deterministic=True, random_state=seed, progress=False, verbosity=0,
                      timeout_in_seconds=timeout, model_selection="best", binary_operators=["+", "-", "*", "/", "max"],
                      unary_operators=["square", "cube", "tanh", "abs", "sin", "exp", "sign", "sqrt_abs(x) = sqrt(abs(x))"],
                      extra_sympy_mappings={"sqrt_abs": lambda x: __import__("sympy").sqrt(__import__("sympy").Abs(x))})
    m.fit(V, D, variable_names=RAW_NAMES); return m
