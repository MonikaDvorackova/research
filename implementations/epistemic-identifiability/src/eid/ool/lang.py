"""Hypothesis language with explicit, staged expansion for out-of-language discovery (OOL).

A hypothesis is an executable simulator  x2' = -a x2 - kap x2^3 + gam*x1*x2 + k u2 + sum_j w_j * term_j(x1_pred),  x3' = -b3 x3 + x2.
term = outer(inner):  inner in {id, sq, delay(k), lp(tau), rate}; outer in {id, sq, cube, abs, sqrtabs, sin(q), bump(p), tanh(p), relu(th), gate(th), dz(th), play(w)}.
Stage 0 (L0, the initial language, identical to the SDW grammar of docs 19/20): outer in {id,sq,cube,tanh,gate,dz} on inner id, play(id), id(delay), fb.
Stage 1 (new static operators): abs, sqrtabs, sin, bump, relu on inner id.
Stage 2 (new state variables): id(lp(tau)) - an extra leaky-integral state; id(rate) - the actuator rate.
Stage 3 (new compositions): inner in {sq, delay, lp} with any nonlinear outer.
Stage 4 (new state-state interaction): gam*x1*x2 (hidden-state-dependent gain).
Every term outside stage 0 counts as 'new vocabulary' and is charged EXP_PEN parameter-equivalents in BIC (protocol doc 23)."""
from __future__ import annotations
import numpy as np
from scipy.optimize import least_squares
from ..sdw import hyp as H0
from .bench import DT, T, SUB

EXP_PEN = 1.0
GRID_TH = tuple(round(0.05 * i, 2) for i in range(1, 15))
GATE0 = tuple(round(0.15 + 0.05 * i, 2) for i in range(12))
DELAYS = tuple(range(3, 10))
LPS = (0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0)
GAMMAS = (-0.5, -0.25, -0.1, 0.1, 0.25, 0.4, 0.6)
FB_KAPPA = H0.FB_KAPPA


def K(outer, op=None, inner="id", ip=None): return (outer, op, inner, ip)


def keys_stage(s):
    if s == 0:
        return ([K("id"), K("sq"), K("cube")] + [K("tanh", p) for p in (0.25, 0.4, 0.6, 0.8)] + [K("gate", p) for p in GATE0]
                + [K("dz", p) for p in (0.15, 0.3, 0.45, 0.6)] + [K("play", p) for p in (0.15, 0.25, 0.35, 0.5)] + [K("id", None, "delay", k) for k in DELAYS])
    if s == 1: return [K("abs"), K("sqrtabs")] + [K("sin", q) for q in (2, 3, 4, 5, 6)] + [K("bump", p) for p in (0.25, 0.3, 0.4, 0.5, 0.7)] + [K("relu", p) for p in GRID_TH]
    if s == 2: return [K("id", None, "lp", t) for t in LPS] + [K("id", None, "rate")]
    if s == 3:
        outs = ([("sq", None), ("cube", None), ("abs", None), ("sqrtabs", None), ("sin", 3), ("sin", 5), ("bump", 0.3), ("bump", 0.5), ("tanh", 0.4), ("tanh", 0.8),
                 ("dz", 0.2), ("dz", 0.4)] + [("relu", p) for p in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5)] + [("gate", p) for p in (0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5)])
        inn = [("sq", None)] + [("delay", k) for k in DELAYS] + [("lp", t) for t in (0.75, 1.5, 2.0, 3.0, 4.0)]
        return [K(o, op, i, ip) for (i, ip) in inn for (o, op) in outs]
    return []


def keys_upto(s): return [k for j in range(s + 1) for k in keys_stage(j)]


L0_SET = set(keys_stage(0))
def tname(t): return f"{t[0]}({t[2]})"
def is_new(t): return t not in L0_SET and not (t[0] in ("tanh", "gate", "dz", "play") and t[2] == "id")   # grid refinement of an L0 operator is not new vocabulary


# ------------------------------------------------------------------ signals
def _lp(m, tau):
    rho = np.exp(-DT / tau); z = np.zeros(m.shape[0]); out = np.empty_like(m)
    for t in range(m.shape[1]): z = rho * z + (1 - rho) * m[:, t]; out[:, t] = z
    return out


def inner_sig(name, p, e, m):
    if name == "id": return m
    if name == "sq": return m * m
    if name == "delay": k = int(p); o = np.zeros_like(e); o[:, k:] = e[:, :-k]; return o
    if name == "lp": return _lp(m, p)
    if name == "rate": o = np.zeros_like(e); o[:, 1:] = (e[:, 1:] - e[:, :-1]) / DT; o[:, 0] = e[:, 0] / DT; return o
    raise ValueError(name)


def outer_f(name, p, v):
    if name == "id": return v
    if name == "sq": return v * v
    if name == "cube": return v ** 3
    if name == "abs": return np.abs(v)
    if name == "sqrtabs": return np.sign(v) * np.sqrt(np.abs(v))
    if name == "sin": return np.sin(p * v)
    if name == "bump": return v * np.exp(-(v / p) ** 2)
    if name == "tanh": return p * np.tanh(v / p)
    if name == "relu": return np.maximum(v - p, 0.0)
    if name == "gate": return v * (v > p)
    if name == "dz": return v - np.clip(v, -p, p)
    if name == "play": return H0.prim_signal("play", p, v)
    raise ValueError(name)


def term_sig(t, e, m): return outer_f(t[0], t[1], inner_sig(t[2], t[3], e, m))


def chain_g(S, a, b3, kap=0.0, gam=0.0, M=None):
    """x2' = -a x2 - kap x2^3 + gam M x2 + S ; x3' = -b3 x3 + x2 ; ZOH input, SUB Euler substeps.  kap, gam scalar or one per row."""
    E = S.shape[0]; h = DT / SUB; x2 = np.zeros(E); x3 = np.zeros(E); out = np.empty_like(S)
    kap = np.broadcast_to(np.asarray(kap, float), (E,)); gam = np.broadcast_to(np.asarray(gam, float), (E,)); gm = bool(np.any(gam != 0))
    for t in range(S.shape[1]):
        mt = M[:, t] if gm else 0.0
        for _ in range(SUB):
            x2 = x2 + h * (-a * x2 - kap * x2 ** 3 + (gam * mt * x2 if gm else 0.0) + S[:, t]); x3 = x3 + h * (-b3 * x3 + x2)
        out[:, t] = x3
    return out


# --------------------------------------------------------------- hypotheses
def mk(terms, w, kap, gam, sk, sse, n, stage=0):
    terms = list(terms); nnew = sum(is_new(t) for t in terms) + (gam != 0)
    npar = sum(1 + (t[1] is not None) + (t[3] is not None) for t in terms) + (kap > 0) + (gam != 0)
    return dict(terms=terms, w=np.array(w, float), kappa=float(kap), gamma=float(gam), a=sk[0], b3=sk[1], k=sk[2], sse=float(sse), n=n, npar=npar, nnew=int(nnew),
                bic=n * np.log(max(sse, 1e-9) / n) + (npar + EXP_PEN * nnew) * np.log(n))


def desc(h): return tuple(sorted({tname(t) for t in h["terms"]} | ({"FB"} if h["kappa"] > 0 else set()) | ({"XINT"} if h["gamma"] != 0 else set())))
def label(h): return "+".join(desc(h)) or "null"


def predict(h, al, be, U):
    single = U.ndim == 2
    if single: U = U[None]
    xe, xm = H0.x1_ends_mid(U[..., 0], al, be); S = h["k"] * U[..., 1]
    for t, w in zip(h["terms"], h["w"]): S = S + w * term_sig(t, xe, xm)
    out = chain_g(S, h["a"], h["b3"], h["kappa"], h["gamma"], xm)
    return out[0] if single else out


def search(U, Y, st, keys, use_fb=True, use_xint=False, polish=3, pairs=True):
    """Forward structure search over `keys` (+ hidden feedback, + state interaction).  st = dict(al, be, a, b3, k).  Two passes (skeleton re-estimated).
    Returns (top distinct-structure hypotheses after polishing, all hypotheses, number of candidate columns evaluated)."""
    top, _, nc = _once(U, Y, st, keys, use_fb, use_xint, polish, pairs)
    best = min(top, key=lambda h: h["bic"]); st2 = dict(st, a=best["a"], b3=best["b3"], k=best["k"])
    top, allh, nc2 = _once(U, Y, st2, keys, use_fb, use_xint, polish, pairs)
    return top, allh, nc + nc2, st2


def _once(U, Y, st, keys, use_fb, use_xint, polish, pairs):
    XE, X1 = H0.x1_ends_mid(U[..., 0], st["al"], st["be"]); U2 = U[..., 1]; Y3 = Y[..., 1]; sk = (st["a"], st["b3"], st["k"])
    r = (Y3 - chain_g(sk[2] * U2, sk[0], sk[1])).ravel(); n = r.size; E = X1.shape[0]
    S_all = np.concatenate([term_sig(k, XE, X1) for k in keys], 0) if keys else np.zeros((0, X1.shape[1]))
    C_all = chain_g(S_all, sk[0], sk[1]).reshape(len(keys), E * X1.shape[1]) if keys else np.zeros((0, n))
    hyps = [mk([], [], 0, 0, sk, r @ r, n)]; sing = {}
    for i, kk in enumerate(keys):
        c = C_all[i]; w = (c @ r) / (c @ c + 1e-9); sse = r @ r - 2 * w * (c @ r) + w * w * (c @ c)
        sing[kk] = (sse, w); hyps.append(mk([kk], [w], 0, 0, sk, sse, n))
    WG = np.linspace(0.5, 7.0, 14)
    if use_fb:
        kaps = np.repeat(np.array(FB_KAPPA), len(WG)); ws = np.tile(WG, len(FB_KAPPA)); R = len(kaps)
        P = chain_g(np.concatenate([sk[2] * U2 + w * X1 for w in ws], 0), sk[0], sk[1], np.repeat(kaps, E)).reshape(R, E, -1)
        sse_g = ((Y3[None] - P) ** 2).sum((1, 2))
        for j in range(len(FB_KAPPA)):
            sl = slice(j * len(WG), (j + 1) * len(WG)); i = int(np.argmin(sse_g[sl])) + j * len(WG)
            hyps.append(mk([K("id")], [ws[i]], kaps[i], 0, sk, sse_g[i], n))
    if use_xint:
        gs = np.repeat(np.array(GAMMAS), len(WG)); ws = np.tile(WG, len(GAMMAS)); R = len(gs)
        Mrep = np.concatenate([X1] * R, 0)
        P = chain_g(np.concatenate([sk[2] * U2 + w * X1 for w in ws], 0), sk[0], sk[1], 0.0, np.repeat(gs, E), Mrep).reshape(R, E, -1)
        sse_g = ((Y3[None] - P) ** 2).sum((1, 2)); sse_g = np.where(np.isfinite(sse_g), sse_g, 1e9)
        for j in range(len(GAMMAS)):
            sl = slice(j * len(WG), (j + 1) * len(WG)); i = int(np.argmin(sse_g[sl])) + j * len(WG)
            hyps.append(mk([K("id")], [ws[i]], 0, gs[i], sk, sse_g[i], n))
    if pairs and sing:
        k1 = min(sing, key=lambda q: sing[q][0]); cols = {kk: C_all[i] for i, kk in enumerate(keys)}
        for k2, c2 in cols.items():
            if tname(k2) == tname(k1): continue
            A = np.stack([cols[k1], c2], 1); w, *_ = np.linalg.lstsq(A, r, rcond=None); hyps.append(mk([k1, k2], w, 0, 0, sk, ((r - A @ w) ** 2).sum(), n))
    hyps.sort(key=lambda h: h["bic"]); seen, top = set(), []
    for h in hyps:
        key = desc(h)
        if key in seen: continue
        seen.add(key); top.append(h)
        if len(top) >= polish + 1: break
    best1 = min((h for h in hyps if len(h["terms"]) <= 1 and h["kappa"] == 0 and h["gamma"] == 0), key=lambda h: h["bic"])      # a simpler rival is always polished too
    if all(desc(h) != desc(best1) for h in top): top.append(best1)
    pol = sorted((_polish(h, XE, X1, U2, Y3) for h in top), key=lambda h: h["bic"])                                            # rank AFTER polishing
    return pol, hyps, len(keys) + (len(FB_KAPPA) * len(WG) if use_fb else 0) + (len(GAMMAS) * len(WG) if use_xint else 0)


BOUNDS = dict(tanh=(.05, 1.5), gate=(.05, 1.5), relu=(.05, 1.5), dz=(.05, 1.5), play=(.05, 1.5), bump=(.1, 1.5), sin=(.5, 10.0))
LPB = (0.2, 10.0)


def _polish(h, XE, X1, U2, Y3):
    tm = h["terms"]; m = len(tm); fb = h["kappa"] > 0; gm = h["gamma"] != 0
    cidx = []                                                                  # (term index, 'op'|'ip') continuous parameters
    for i, t in enumerate(tm):
        if t[0] in BOUNDS and t[1] is not None and t[0] != "gate": cidx.append((i, "op"))
        if t[2] == "lp": cidx.append((i, "ip"))
    nb = 3 + m + fb + gm

    def terms_of(th):
        ts = [list(t) for t in tm]
        for j, (i, w) in enumerate(cidx): ts[i][1 if w == "op" else 3] = float(th[nb + j])
        return [tuple(t) for t in ts]

    def res(th):
        S = th[2] * U2
        for tt, wj in zip(terms_of(th), th[3:3 + m]): S = S + wj * term_sig(tt, XE, X1)
        kap = th[3 + m] if fb else 0.0; gam = th[3 + m + fb] if gm else 0.0
        return (Y3 - chain_g(S, th[0], th[1], kap, gam, X1)).ravel()
    lo = np.concatenate([[.3, .3, -20], -50 * np.ones(m), [0.0] if fb else [], [-2.0] if gm else [], [(BOUNDS[tm[i][0]] if w == "op" else LPB)[0] for i, w in cidx]])
    hi = np.concatenate([[5, 5, 20], 50 * np.ones(m), [5.0] if fb else [], [2.0] if gm else [], [(BOUNDS[tm[i][0]] if w == "op" else LPB)[1] for i, w in cidx]])
    x0 = np.concatenate([[h["a"], h["b3"], h["k"]], h["w"], [h["kappa"]] if fb else [], [h["gamma"]] if gm else [], [tm[i][1] if w == "op" else tm[i][3] for i, w in cidx]])
    try: r = least_squares(res, np.clip(x0, lo + 1e-9, hi - 1e-9), bounds=(lo, hi), max_nfev=40)
    except Exception: return h
    th = r.x; g = mk(terms_of(th), th[3:3 + m], th[3 + m] if fb else 0.0, th[3 + m + fb] if gm else 0.0, (th[0], th[1], th[2]), 2 * r.cost, h["n"])
    return g if g["sse"] <= h["sse"] else h


# ----------------------------------------------------------------- criticism
from scipy import stats


def episode_pvalues(h, al, be, U, Y, sig):
    res = Y[..., 1] - predict(h, al, be, U); return stats.chi2.sf((res ** 2).sum(1) / sig ** 2, df=res.shape[1])


def oos_p(h, al, be, u, y, sig): return float(stats.chi2.sf(((y[:, 1] - predict(h, al, be, u)) ** 2).sum() / sig ** 2, df=len(y)))


def nlp(p): return float(-np.log10(max(p, 1e-300)))
