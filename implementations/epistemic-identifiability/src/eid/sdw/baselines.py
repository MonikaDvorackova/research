"""Baselines with the same observation/intervention interface: SINDYc (pysindy 2.1.0, three or four state sets), ridge NARX,
Hammerstein static-map, declared-class Bayes.  Each fit_* returns a predictor fn(U [E,T,2]) -> x3 [E,T]."""
from __future__ import annotations
import numpy as np
from scipy.optimize import least_squares
from scipy.signal import savgol_filter
from . import hyp
from .env import DT, T

CLIP = 8.0


# ------------------------------------------------------------------- ridge NARX
def _poly2(z):
    n = z.shape[1]; iu = np.triu_indices(n)
    return np.concatenate([np.ones((len(z), 1)), z, (z[:, :, None] * z[:, None, :])[:, iu[0], iu[1]]], 1)


def _lagfeat(x1, x3, u1, u2, t, L):
    """features at time t from arrays [R,*] (lags of the observed/predicted x1,x3 and of the inputs)."""
    f = []
    for l in range(1, L + 1):
        f += [x1[:, t - l] if t - l >= 0 else 0 * x1[:, 0], x3[:, t - l] if t - l >= 0 else 0 * x3[:, 0]]
    for l in range(0, L):
        f += [u1[:, t - l] if t - l >= 0 else 0 * u1[:, 0], u2[:, t - l] if t - l >= 0 else 0 * u2[:, 0]]
    return np.stack(f, 1)


def fit_narx(U, Y, lam, L=3, rows=None):
    E = U.shape[0]; X, Z = [], []
    for t in range(T):
        X.append(_lagfeat(Y[..., 0], Y[..., 1], U[..., 0], U[..., 1], t, L)); Z.append(np.stack([Y[:, t, 0], Y[:, t, 1]], 1))
    X = np.concatenate(X); Z = np.concatenate(Z)
    if rows is not None: X, Z = X[rows], Z[rows]
    P = _poly2(X); W = np.linalg.solve(P.T @ P + lam * np.eye(P.shape[1]), P.T @ Z)

    def pred(Ut):
        R = Ut.shape[0]; x1 = np.zeros((R, T)); x3 = np.zeros((R, T))
        for t in range(T):
            o = np.clip(_poly2(_lagfeat(x1, x3, Ut[..., 0], Ut[..., 1], t, L)) @ W, -CLIP, CLIP); x1[:, t], x3[:, t] = o[:, 0], o[:, 1]
        return x3
    return pred


def fit_narx_ensemble(U, Y, lam, n_members, rng, L=3):
    nrow = U.shape[0] * T; return [fit_narx(U, Y, lam, L, rows=rng.integers(0, nrow, nrow)) for _ in range(n_members)]


# ----------------------------------------------------------------------- SINDYc
def fit_sindyc(U, Y, mode, thr, x2hat=None, x2true=None, degree=3, lib="poly"):
    """mode: raw [x1,x3,x4] | embed [x1,x3,dx3] | learned [x1,x3,x2hat] | oracle [x1,x3,x2n (privileged)]."""
    import pysindy as ps
    from sklearn.exceptions import ConvergenceWarning
    import warnings; warnings.filterwarnings("ignore")
    sm = ps.SmoothedFiniteDifference(smoother_kws={"window_length": 9})

    def states(Yv, x2):
        if mode == "raw": return [Yv[e][:, [0, 1, 2]] for e in range(len(Yv))]
        if mode == "embed": return [np.stack([Yv[e][:, 0], Yv[e][:, 1], savgol_filter(Yv[e][:, 1], 9, 3, deriv=1, delta=DT)], 1) for e in range(len(Yv))]
        return [np.stack([Yv[e][:, 0], Yv[e][:, 1], x2[e]], 1) for e in range(len(Yv))]
    xs = states(list(Y), x2hat if mode == "learned" else x2true); us = [U[e] for e in range(U.shape[0])]
    if lib == "poly": library = ps.PolynomialLibrary(degree=degree)
    else:                                                                       # per-variable dictionary, no cross terms (stable rollouts)
        fns = [lambda x: x ** 2, lambda x: x ** 3, lambda x: np.tanh(x / 0.5), lambda x: np.maximum(x, 0.0)]
        library = ps.ConcatLibrary([ps.PolynomialLibrary(degree=1), ps.CustomLibrary(library_functions=fns, function_names=[lambda x: f"{x}^2", lambda x: f"{x}^3", lambda x: f"tanh({x})", lambda x: f"relu({x})"])])
    model = ps.SINDy(optimizer=ps.STLSQ(threshold=thr, alpha=1e-3), feature_library=library, differentiation_method=sm)
    model.fit(xs, t=DT, u=us)
    n = xs[0].shape[1]

    def pred(Ut):
        R = Ut.shape[0]; x = np.zeros((R, n)); out = np.zeros((R, T))
        for t in range(T):
            try: d = model.predict(x, u=Ut[:, t, :])
            except Exception: d = np.full_like(x, np.nan)
            x = np.clip(x + DT * d, -CLIP, CLIP); x = np.where(np.isfinite(x), x, CLIP); out[:, t] = x[:, 1]
        return out
    return pred, model


# -------------------------------------------------------------------- Hammerstein
KNOTS = np.linspace(-1, 1, 9)


def _hats(x):
    h = KNOTS[1] - KNOTS[0]; return [np.clip(1 - np.abs(x - c) / h, 0, None) for c in KNOTS]


def fit_hammerstein(U, Y, st, lam=1e-3):
    """Static nonparametric coupling (piecewise-linear in x1) + fitted linear chain; variable projection over (a,b3)."""
    XE, X1 = hyp.x1_ends_mid(U[..., 0], st["al"], st["be"]); U2 = U[..., 1]; Y3 = Y[..., 1]

    def cols(a, b3):
        S = np.concatenate([U2] + _hats(X1), 0); C = hyp.chain(S, a, b3).reshape(len(KNOTS) + 1, -1); return C
    def solve(a, b3):
        C = cols(a, b3); w = np.linalg.solve(C @ C.T + lam * np.eye(len(C)), C @ Y3.ravel()); return w, Y3.ravel() - C.T @ w
    r = least_squares(lambda th: solve(*th)[1], [st["a"], st["b3"]], bounds=(.3, 5.), max_nfev=25); a, b3 = r.x; w, _ = solve(a, b3)

    def pred(Ut):
        xe, xm = hyp.x1_ends_mid(Ut[..., 0], st["al"], st["be"]); S = w[0] * Ut[..., 1] + sum(wj * h for wj, h in zip(w[1:], _hats(xm)))
        return hyp.chain(S, a, b3)
    return pred


# ------------------------------------------------------------- declared-class Bayes
def bayes_grid(U, Y, st, sig):
    """Grid posterior over the declared class {lin, tanh(s), delay(k)} x gain.  Returns (hyps, weights, st2)."""
    top, allh, st2 = hyp.search(U, Y, st, allowed=hyp.DECLARED, polish=0, pairs=False, return_all=True)
    H = [h for h in allh if h["prims"]]; sse = np.array([h["sse"] for h in H])
    w = np.exp(-(sse - sse.min()) / (2 * sig ** 2)); w /= w.sum(); return H, w, st2


def bayes_predictor(H, w, al, be):
    keep = [i for i in np.argsort(-w)[:12] if w[i] > 1e-4]; ww = w[keep] / w[keep].sum()
    def pred(Ut): return sum(wi * hyp.predict(H[i], al, be, Ut) for wi, i in zip(ww, keep))
    return pred, [H[i] for i in keep], ww
