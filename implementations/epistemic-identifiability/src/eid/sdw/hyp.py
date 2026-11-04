"""Structural hypothesis language (grammar of executable coupling primitives), fitting, model criticism, falsification-driven design."""
from __future__ import annotations
import numpy as np
from scipy.optimize import least_squares, minimize_scalar
from scipy import stats
from .env import DT, T, SUB, POOL, POOL_NAMES

# ------------------------------------------------------------------ language
GRIDS = dict(tanh=(0.25, 0.4, 0.6, 0.8), gate=tuple(round(0.15 + 0.05 * i, 2) for i in range(12)), dz=(0.15, 0.3, 0.45, 0.6), delay=tuple(float(k) for k in range(3, 10)),
             play=(0.15, 0.25, 0.35, 0.5))
KEYS = [("lin", None), ("quad", None), ("cube", None)] + [(n, p) for n, g in GRIDS.items() for p in g]
FB_KAPPA = (0.05, 0.15, 0.4, 1.0)
DECLARED = ("lin", "tanh", "delay")
ALL = tuple(sorted({k[0] for k in KEYS} | {"fb"}))


def prim_signal(name, p, x):
    """x [E,T] (predicted actuator state) -> primitive of x [E,T]."""
    if name == "lin": return x
    if name == "quad": return x * x
    if name == "cube": return x ** 3
    if name == "tanh": return p * np.tanh(x / p)
    if name == "gate": return x * (x > p)
    if name == "dz": return x - np.clip(x, -p, p)
    if name == "delay":
        k = int(p); out = np.zeros_like(x); out[:, k:] = x[:, :-k]; return out
    if name == "play":
        z = np.zeros(x.shape[0]); out = np.empty_like(x)
        for t in range(x.shape[1]): z = np.minimum(np.maximum(z, x[:, t] - p), x[:, t] + p); out[:, t] = z
        return out
    raise ValueError(name)


def chain(S, a, b3):
    """Linear two-stage filter x2' = -a x2 + s, x3' = -b3 x3 + x2, zero-order-hold input, SUB Euler substeps per sample; S [E,T] -> x3 [E,T]."""
    h = DT / SUB; x2 = np.zeros(S.shape[0]); x3 = x2.copy(); out = np.empty_like(S)
    for t in range(S.shape[1]):
        for _ in range(SUB):
            x2 = x2 + h * (-a * x2 + S[:, t]); x3 = x3 + h * (-b3 * x3 + x2)
        out[:, t] = x3
    return out


def chain_fb(S, a, b3, kap):
    """Hidden self-cubic-damping variant; kap scalar or one value per row of S."""
    h = DT / SUB; x2 = np.zeros(S.shape[0]); x3 = x2.copy(); out = np.empty_like(S)
    for t in range(S.shape[1]):
        for _ in range(SUB):
            x2 = x2 + h * (-a * x2 - kap * x2 ** 3 + S[:, t]); x3 = x3 + h * (-b3 * x3 + x2)
        out[:, t] = x3
    return out


def fit_x1(U, Y):
    """AR model x1[t] = alpha x1[t-1] + beta u1[t].  Instrumental variables (y1[t-2], u1[t]) remove the attenuation bias that white
    measurement noise causes in the regressor y1[t-1]; sigma from the innovations (observation noise enters as (1+alpha^2))."""
    y1, u1 = Y[..., 0], U[..., 0]
    X = np.stack([y1[:, 1:-1].ravel(), u1[:, 2:].ravel()], 1); Z = np.stack([y1[:, :-2].ravel(), u1[:, 2:].ravel()], 1); b = y1[:, 2:].ravel()
    al, be = np.linalg.solve(Z.T @ X, Z.T @ b)
    res = b - X @ np.array([al, be])
    return float(al), float(be), float(np.sqrt(np.var(res) / (1 + al ** 2)))


def x1_ends_mid(u1, al, be):
    """Predicted actuator state at sample ends and at interval midpoints (the coupling acts continuously inside a sample)."""
    e = ar_sim(u1, al, be); prev = np.concatenate([np.zeros((e.shape[0], 1)), e[:, :-1]], 1)
    return e, 0.5 * (e + prev)


def psig(name, p, e, m):
    """Primitive signal; the delay primitive reads the end-of-sample value, every other primitive the midpoint."""
    return prim_signal(name, p, e if name == "delay" else m)


def ar_sim(u1, al, be):
    """u1 [E,T] -> predicted x1 [E,T]."""
    x = np.zeros(u1.shape[0]); out = np.empty_like(u1)
    for t in range(u1.shape[1]): x = al * x + be * u1[:, t]; out[:, t] = x
    return out


def fit_skeleton(y3, u2):
    """a, b3, k from a u2-only episode (u1 = 0 so every coupling primitive vanishes)."""
    best = None
    for a0, b0 in [(1., 1.), (1., 2.5), (2.5, 1.), (2., 2.)]:
        def res(th):
            R = chain(u2[None], *np.exp(th))[0]; k = (R @ y3) / (R @ R + 1e-12); return y3 - k * R
        r = least_squares(res, np.log([a0, b0]), bounds=(np.log(.3), np.log(5.)))
        if best is None or r.cost < best.cost: best = r
    a, b3 = np.exp(best.x); R = chain(u2[None], a, b3)[0]
    return float(a), float(b3), float((R @ y3) / (R @ R))


# --------------------------------------------------------------- hypotheses
def _hyp(prims, w, kappa, sk, sse, n):
    npar = sum(1 + (p is not None) for _, p in prims) + (kappa > 0)
    return dict(prims=list(prims), w=np.array(w, float), kappa=float(kappa), a=sk[0], b3=sk[1], k=sk[2], sse=float(sse), n=n,
                npar=npar, bic=n * np.log(max(sse, 1e-9) / n) + npar * np.log(n))


def names_of(h): return tuple(sorted({nm for nm, _ in h["prims"]} | ({"fb"} if h["kappa"] > 0 else set())))


def predict(h, al, be, U):
    """Executable hypothesis: x3 predicted for programmes U [E,T,2] (or [T,2] -> [T])."""
    single = U.ndim == 2
    if single: U = U[None]
    xe, xm = x1_ends_mid(U[..., 0], al, be)
    S = h["k"] * U[..., 1]
    for (nm, p), w in zip(h["prims"], h["w"]): S = S + w * psig(nm, p, xe, xm)
    out = chain_fb(S, h["a"], h["b3"], h["kappa"]) if h["kappa"] > 0 else chain(S, h["a"], h["b3"])
    return out[0] if single else out


def _search_once(U, Y, st, allowed=ALL, polish=3, pairs=True):
    """Two passes: structure search, then re-estimate the skeleton (a,b3,k) jointly with the best hypothesis and search again.
    Forward structure search. st = dict(al, be, a, b3, k).  Returns hypotheses sorted by BIC (null always included)."""
    XE, X1 = x1_ends_mid(U[..., 0], st["al"], st["be"]); U2 = U[..., 1]; Y3 = Y[..., 1]; sk = (st["a"], st["b3"], st["k"])
    r = (Y3 - chain(sk[2] * U2, sk[0], sk[1])).ravel(); n = r.size
    keys = [kk for kk in KEYS if kk[0] in allowed]
    E = X1.shape[0]
    if keys:
        S_all = np.concatenate([psig(kk[0], kk[1], XE, X1) for kk in keys], 0)           # [nkeys*E,T]
        C_all = chain(S_all, sk[0], sk[1]).reshape(len(keys), E * X1.shape[1])
    cols = {kk: C_all[i] for i, kk in enumerate(keys)}
    hyps = [_hyp([], [], 0, sk, r @ r, n)]
    sing = {}
    for kk, c in cols.items():
        w = (c @ r) / (c @ c + 1e-9); sse = r @ r - 2 * w * (c @ r) + w * w * (c @ c)
        sing[kk] = (sse, w); hyps.append(_hyp([kk], [w], 0, sk, sse, n))
    if "fb" in allowed:
        WG = np.linspace(0.5, 7.0, 14); kaps = np.repeat(np.array(FB_KAPPA), len(WG)); ws = np.tile(WG, len(FB_KAPPA)); R = len(kaps)
        S = np.concatenate([sk[2] * U2 + w * X1 for w in ws], 0)                     # [R*E,T]
        P = chain_fb(S, sk[0], sk[1], np.repeat(kaps, E)).reshape(R, E, -1)
        sse_g = ((Y3[None] - P) ** 2).sum((1, 2))
        for j in range(len(FB_KAPPA)):
            sl = slice(j * len(WG), (j + 1) * len(WG)); i = int(np.argmin(sse_g[sl])) + j * len(WG)
            hyps.append(_hyp([("lin", None)], [ws[i]], kaps[i], sk, sse_g[i], n))
    if pairs and sing:
        k1 = min(sing, key=lambda q: sing[q][0])
        for k2, c2 in cols.items():
            if k2[0] == k1[0]: continue
            A = np.stack([cols[k1], c2], 1); w, *_ = np.linalg.lstsq(A, r, rcond=None); sse = ((r - A @ w) ** 2).sum()
            hyps.append(_hyp([k1, k2], w, 0, sk, sse, n))
    hyps.sort(key=lambda h: h["bic"])
    seen, top = set(), []
    for h in hyps:                                                       # polish best hypothesis of each distinct structure
        key = names_of(h)
        if key in seen: continue
        seen.add(key); top.append(h)
        if len(top) >= polish + 1: break
    return [_polish(h, XE, X1, U2, Y3) for h in top], hyps


CONT = ("tanh", "gate", "dz", "play")


def _polish(h, XE, X1, U2, Y3):
    """Joint least-squares refinement of skeleton (a,b3,k), gains, hidden-feedback kappa and the continuous primitive parameters."""
    pr = h["prims"]; m = len(pr); ci = [i for i, (nm, _) in enumerate(pr) if nm in CONT]; fb = h["kappa"] > 0

    def build(th):
        ps = [p for _, p in pr]
        for j, i in enumerate(ci): ps[i] = th[3 + m + (1 if fb else 0) + j]
        return [psig(nm, p, XE, X1) for (nm, _), p in zip(pr, ps)], ps

    def res(th):
        sigs, _ = build(th); a, b3, k = th[:3]; w = th[3:3 + m]; kap = th[3 + m] if fb else 0.0
        S = k * U2 + sum(wj * s for wj, s in zip(w, sigs))
        return (Y3 - (chain_fb(S, a, b3, kap) if kap > 0 else chain(S, a, b3))).ravel()
    x0 = np.concatenate([[h["a"], h["b3"], h["k"]], h["w"], [h["kappa"]] if fb else [], [pr[i][1] for i in ci]])
    lo = np.concatenate([[.3, .3, -20], -50 * np.ones(m), [0.0] if fb else [], .05 * np.ones(len(ci))])
    hi = np.concatenate([[5, 5, 20], 50 * np.ones(m), [5.0] if fb else [], 1.5 * np.ones(len(ci))])
    try:
        r = least_squares(res, np.clip(x0, lo + 1e-9, hi - 1e-9), bounds=(lo, hi), max_nfev=40)
    except Exception:
        return h
    th = r.x; _, ps = build(th)
    g = _hyp([(nm, p) for (nm, _), p in zip(pr, ps)], th[3:3 + m], th[3 + m] if fb else 0.0, (th[0], th[1], th[2]), 2 * r.cost, h["n"])
    return g if g["sse"] <= h["sse"] else h


# ----------------------------------------------------------------- criticism
def episode_pvalues(h, al, be, U, Y, sig):
    """Per-episode chi-square p-values of the residuals of hypothesis h against measurement noise sigma (df = T)."""
    res = Y[..., 1] - predict(h, al, be, U)
    return stats.chi2.sf((res ** 2).sum(1) / sig ** 2, df=res.shape[1])


def oos_pvalue(h, al, be, u, y, sig):
    """Out-of-sample check: p-value of the prediction error of h on a programme it was not fitted to."""
    return float(stats.chi2.sf(((y[:, 1] - predict(h, al, be, u)) ** 2).sum() / sig ** 2, df=len(y)))


# -------------------------------------------------------------------- design
def disagreement_scores(alts, al, be, pool_U, sig):
    """alts: list of hypotheses (alts[0] = leading hypothesis).  Score of each pool programme = max_j ||F_0(u)-F_j(u)||^2 / sigma^2."""
    P = np.stack([predict(h, al, be, pool_U) for h in alts])               # [A,Np,T]
    return (((P[1:] - P[:1]) ** 2).sum(2) / sig ** 2).max(0)


def pool_array(): return np.stack(POOL)


def search(U, Y, st, allowed=ALL, polish=3, pairs=True, return_all=False):
    """Pass 1: structure search with the skeleton from the u2-only episode.  Pass 2: skeleton re-estimated jointly with the best polished
    hypothesis, then the search is repeated (the u2-only episode alone fixes the skeleton only to a few percent)."""
    top, _ = _search_once(U, Y, st, allowed, polish, pairs)
    best = min(top, key=lambda h: h["bic"])
    st2 = dict(st, a=best["a"], b3=best["b3"], k=best["k"])
    top, allh = _search_once(U, Y, st2, allowed, polish, pairs)
    return (top, allh, st2) if return_all else top
