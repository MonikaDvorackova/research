"""Discovery agent (structure search + model criticism + falsification-driven design + abstention), design ablations, baseline runners,
equation-error proposal step.  Protocol: topics/.../19-structural-discovery-framework-and-protocol.md"""
from __future__ import annotations
import time
import numpy as np
from scipy.signal import savgol_filter
from . import env, hyp, baselines as bl
from .env import T, POOL, IDX

ALPHA, DBIC, EPS = 0.01, 10.0, 0.5            # fixed in protocol 19 (theory, not tuned)
TAU = 0.05
POOL_U = np.stack(POOL)
U2_IDS = {i for i, u in enumerate(POOL) if np.abs(u[:, 1]).max() > 0}
EXPECT = dict(lin={"lin"}, sat={"tanh"}, quad={"quad"}, delay={"delay"}, gate={"gate"}, backlash={"play"}, fb={"fb"})


def observe(inst, iseed, pid, u):
    y, _, x2 = env.simulate(inst, u, np.random.default_rng([iseed, pid]))
    return y, x2


class Data:
    def __init__(self, inst, iseed):
        self.inst, self.iseed = inst, iseed
        self.ids = []; self.U = []; self.Y = []; self.X2 = []
        self.add(-1, env.E0); self.add(IDX["u1 +1"], env.E1)

    def add(self, pid, u):
        y, x2 = observe(self.inst, self.iseed, 999 if pid < 0 else pid, u)
        self.ids.append(pid); self.U.append(u); self.Y.append(y); self.X2.append(x2)

    @property
    def arr(self): return np.stack(self.U), np.stack(self.Y)


def fit_state(U, Y):
    al, be, sg = hyp.fit_x1(U, Y); a, b3, k = hyp.fit_skeleton(Y[0, :, 1], U[0, :, 1])
    return al, be, sg, dict(al=al, be=be, a=a, b3=b3, k=k)


def test_set(inst, k):
    rng = np.random.default_rng(26000 + k); Ut = np.stack(env.random_programmes(24, rng))
    truth = np.stack([env.simulate(inst, u)[1] for u in Ut]); return Ut, truth


def rmse(pred, truth): return float(np.sqrt(np.mean((pred - truth) ** 2)))


# ------------------------------------------------------------------ the agent
def choose(design, data, top, allh, st2, al, be, sg, rng, cfg, pool_mask):
    free = [i for i in range(len(POOL)) if i not in data.ids and pool_mask[i]]
    if design == "random": return int(rng.choice(free))
    if design in ("sweepA", "sweepB"):
        order = env.SWEEP_A if design == "sweepA" else env.SWEEP_B
        for i in order:
            if i not in data.ids: return i
        return free[0]
    if design == "falsify":
        alts = top[:4]
        if len(alts) < 2: alts = alts + [h for h in sorted(allh, key=lambda q: q["bic"]) if h is not alts[0]][:1]
        sc = hyp.disagreement_scores(alts, al, be, POOL_U, sg)
    elif design == "eig":                                                       # declared-class posterior-weighted predictive variance
        H, w, st3 = bl.bayes_grid(*data.arr, dict(al=al, be=be, a=st2["a"], b3=st2["b3"], k=st2["k"]), sg)
        keep = [i for i in np.argsort(-w)[:12] if w[i] > 1e-4]; ww = w[keep] / w[keep].sum()
        P = np.stack([hyp.predict(H[i], al, be, POOL_U) for i in keep]); mu = (ww[:, None, None] * P).sum(0)
        sc = ((ww[:, None, None] * (P - mu) ** 2).sum(0)).sum(1) / sg ** 2
    elif design == "ens":                                                       # generic ensemble-variance (E-SINDy / Plan2Explore-style)
        ens = bl.fit_narx_ensemble(*data.arr, cfg["lam_narx"], 6, rng)
        P = np.stack([f(POOL_U) for f in ens]); sc = P.var(0).sum(1)
    else: raise ValueError(design)
    sc = np.asarray(sc, float); sc[[i for i in range(len(POOL)) if i not in free]] = -np.inf
    return int(np.argmax(sc))


def run_agent(inst, iseed, Bs, design, cfg, allowed=hyp.ALL, pool_mask=None, tests=None):
    """Returns {B: record}.  The agent runs adaptively to max(Bs) and a snapshot decision is taken at each B in Bs (designs are nested)."""
    rng = np.random.default_rng([iseed, 4242]); data = Data(inst, iseed)
    pool_mask = pool_mask if pool_mask is not None else np.ones(len(POOL), bool)
    Ut, truth = tests; eq_U = np.concatenate([POOL_U, np.stack(env.random_programmes(100, np.random.default_rng([iseed, 5151])))])
    out, oos_p, last_top = {}, None, None
    t0 = time.time()
    while True:
        B = len(data.U); U, Y = data.arr
        need_fit = (B in Bs) or design in ("falsify", "eig", "ens")
        if need_fit:
            al, be, sg, st = fit_state(U, Y)
            top, allh, st2 = hyp.search(U, Y, st, allowed=allowed, return_all=True)
        if B in Bs:
            best = top[0]; p_in = hyp.episode_pvalues(best, al, be, U, Y, sg)
            alts = [h for h in top[1:] if h["bic"] - best["bic"] < DBIC]
            amb = 0.0
            if alts:
                Pb = hyp.predict(best, al, be, eq_U); amb = max(float(np.sqrt(((hyp.predict(h, al, be, eq_U) - Pb) ** 2).mean(1)).max()) for h in alts)
            r = rmse(hyp.predict(best, al, be, Ut), truth)
            out[B] = dict(B=B, rmse=r, ok=r <= TAU, p_in=float(p_in.min()), p_oos=oos_p, amb=amb, amb_ratio=amb / sg, sig=sg,
                          names="+".join(hyp.names_of(best)) or "null", ids=list(data.ids), time=time.time() - t0)
        if B >= max(Bs): break
        if design in ("falsify", "eig", "ens"): pid = choose(design, data, top, allh, st2, al, be, sg, rng, cfg, pool_mask)
        else: pid = choose(design, data, None, None, None, None, None, None, rng, cfg, pool_mask)
        if design in ("falsify", "eig", "ens"):                                  # out-of-sample test of the current leading hypothesis on the new episode
            data.add(pid, POOL[pid]); oos_p = hyp.oos_pvalue(top[0], al, be, POOL[pid], data.Y[-1], sg)
        else: data.add(pid, POOL[pid]); oos_p = None
    return out


def outcome(rec, mode="full"):
    """Epistemic decision from stored statistics.  full: in-sample + out-of-sample misfit, then ambiguity; crit_in: in-sample only;
    nocrit: always claim."""
    if mode == "nocrit": return "claim"
    rej = rec["p_in"] < ALPHA / rec["B"]
    if mode == "full" and rec["p_oos"] is not None and rec["p_oos"] < ALPHA: rej = True
    if rej: return "abstain_ool"
    if rec["amb_ratio"] > EPS: return "abstain_amb"
    return "claim"


# -------------------------------------------------------------------- baselines
def run_baselines(inst, iseed, Bs, cfg, tests, est_models=None, sched="B"):
    """Baselines on the shared sweep schedule.  Returns {method: {B: rec}}."""
    order = env.SWEEP_B if sched == "B" else env.SWEEP_A
    Ut, truth = tests; res = {}
    data = Data(inst, iseed)
    for pid in order[: max(Bs) - 2]: data.add(pid, POOL[pid])
    for B in Bs:
        U, Y = np.stack(data.U[:B]), np.stack(data.Y[:B]); X2 = np.stack(data.X2[:B])
        al, be, sg, st = fit_state(U, Y)
        def put(name, pred, **kw):
            try: p = pred(Ut); r = rmse(p, truth)
            except Exception: r = float("inf")
            res.setdefault(name, {})[B] = dict(B=B, rmse=r, ok=r <= TAU, **kw)
        # declared-class Bayes
        H, w, st2 = bl.bayes_grid(U, Y, st, sg); pb, keep, ww = bl.bayes_predictor(H, w, al, be)
        best = H[int(np.argmax(w))]; res_in = hyp.episode_pvalues(best, al, be, U, Y, sg)
        put("bayes_declared", pb, p_in=float(res_in.min()))
        top = hyp.search(U, Y, st)                                              # grammar search without criticism or design
        put("grammar_sweep", lambda Uq, h=top[0]: hyp.predict(h, al, be, Uq), p_in=float(hyp.episode_pvalues(top[0], al, be, U, Y, sg).min()))
        put("narx", bl.fit_narx(U, Y, cfg["lam_narx"]))
        put("hammerstein", bl.fit_hammerstein(U, Y, st))
        for mode in ("raw", "embed"):
            try: put("sindyc_" + mode, bl.fit_sindyc(U, Y, mode, cfg["sindy"][mode][1], degree=cfg["sindy"][mode][0])[0])
            except Exception: res.setdefault("sindyc_" + mode, {})[B] = dict(B=B, rmse=float("inf"), ok=False)
        if est_models:
            from . import rep
            x2hat = np.mean([rep.infer(m, Y[..., 1], U[..., 1]) for m in est_models], 0)
            try: put("sindyc_learned", bl.fit_sindyc(U, Y, "learned", cfg["sindy"]["learned"][1], x2hat=x2hat, degree=cfg["sindy"]["learned"][0])[0])
            except Exception: res.setdefault("sindyc_learned", {})[B] = dict(B=B, rmse=float("inf"), ok=False)
        for mode in ("raw", "learned", "oracle"):                                  # nonlinear per-variable dictionary library (no cross terms)
            if mode == "learned" and not est_models: continue
            try: put("sindyc_dict_" + mode, bl.fit_sindyc(U, Y, mode, cfg["sindy_dict"][mode], x2hat=x2hat if mode == "learned" else None, x2true=X2, lib="dict")[0])
            except Exception: res.setdefault("sindyc_dict_" + mode, {})[B] = dict(B=B, rmse=float("inf"), ok=False)
        try: put("sindyc_oracle", bl.fit_sindyc(U, Y, "oracle", cfg["sindy"]["oracle"][1], x2true=X2, degree=cfg["sindy"]["oracle"][0])[0])   # privileged hidden state
        except Exception: res.setdefault("sindyc_oracle", {})[B] = dict(B=B, rmse=float("inf"), ok=False)
    return res


# -------------------------------------------- proposal step (equation-error regression on reconstructed state)
def kalman_x2(y3, u2, a, b3, k, sig, q=4.0):
    """Model-based analytic reconstruction: RTS smoother for x2' = -a x2 + k u2 + (unknown coupling = process noise, variance q), x3' = -b3 x3 + x2,
    y3 = x3 + noise(sig).  Skeleton (a,b3,k) from the u2-only episode."""
    from scipy.linalg import expm
    Ac = np.array([[-a, 0.0], [1.0, -b3]]); Ad = expm(Ac * env.DT); Bd = np.linalg.solve(Ac, (Ad - np.eye(2))) @ np.array([k, 0.0])
    Q = np.diag([q * env.DT, 1e-8]); H = np.array([[0.0, 1.0]]); n = len(y3)
    xp = np.zeros((n, 2)); Pp = np.zeros((n, 2, 2)); xf = np.zeros((n, 2)); Pf = np.zeros((n, 2, 2)); x = np.zeros(2); P = np.diag([1.0, 1e-4])
    for t in range(n):
        x = Ad @ x + Bd * u2[t]; P = Ad @ P @ Ad.T + Q; xp[t], Pp[t] = x, P
        S = H @ P @ H.T + sig ** 2; K = P @ H.T / S; x = x + (K * (y3[t] - H @ x)).ravel(); P = (np.eye(2) - K @ H) @ P; xf[t], Pf[t] = x, P
    xs = xf.copy()
    for t in range(n - 2, -1, -1):
        C = Pf[t] @ Ad.T @ np.linalg.inv(Pp[t + 1]); xs[t] = xf[t] + C @ (xs[t + 1] - xp[t + 1])
    return xs[:, 0]


def proposal_rank(U, Y, X2, est_models, which):
    """Rank primitive names by equation-error regression  d/dt xhat2 = -alpha xhat2 + k u2 + w * prim(x1)  (free linear terms), on a
    reconstructed hidden state: oracle (privileged x2n) | analytic (derivative of x3 + b3 x3) | learned estimator."""
    al, be, sg, st = fit_state(U, Y); E = U.shape[0]
    d1 = lambda x: savgol_filter(x, 9, 3, deriv=1, delta=env.DT, axis=-1)
    if which == "oracle": x2 = X2
    elif which == "analytic": x2 = d1(Y[..., 1]) + st["b3"] * Y[..., 1]
    elif which == "kalman": x2 = np.stack([kalman_x2(Y[e, :, 1], U[e, :, 1], st["a"], st["b3"], st["k"], sg) for e in range(E)])
    else:
        from . import rep; x2 = np.mean([rep.infer(m, Y[..., 1], U[..., 1]) for m in est_models], 0)
    D = d1(x2).ravel(); x1 = savgol_filter(Y[..., 0], 9, 2, axis=-1); base = [x2.ravel(), U[..., 1].ravel()]
    best = {}; n = D.size; bic = lambda sse, p: n * np.log(sse / n) + p * np.log(n)
    for kk in hyp.KEYS:
        phi = hyp.prim_signal(kk[0], kk[1], x1).ravel()
        A = np.stack(base + [phi], 1); w, *_ = np.linalg.lstsq(A, D, rcond=None); s = bic(((D - A @ w) ** 2).sum(), 3 + (kk[1] is not None))
        best[kk[0]] = min(best.get(kk[0], np.inf), s)
    A = np.stack(base + [x1.ravel(), x2.ravel() ** 3], 1); w, *_ = np.linalg.lstsq(A, D, rcond=None); best["fb"] = bic(((D - A @ w) ** 2).sum(), 4)
    return [k for k, _ in sorted(best.items(), key=lambda q: q[1])]
