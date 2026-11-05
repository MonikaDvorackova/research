"""Out-of-language discovery loop: predict -> criticise (calibrated) -> diagnose -> generate (staged language expansion) -> discriminate -> test -> revise -> stop/abstain.
The agent touches the environment only through bench.World.run.  Protocol: topics/.../23-adaptive-hypothesis-language-framework.md"""
from __future__ import annotations
import time
import numpy as np
from ..sdw import env as E, hyp as H0, baselines as bl
from . import lang, bench

DBIC, EPS, ALPHA, TAU = 10.0, 0.5, 0.01, 0.05
POOL = E.POOL; POOL_U = np.stack(POOL); IDX = E.IDX
STAGE_ORDER = (1, 2, 3, 4)


class Data:
    def __init__(self, world):
        self.w = world; self.ids, self.U, self.Y = [], [], []
        self.add(-1, E.E0); self.add(IDX["u1 +1"], E.E1)

    def add(self, pid, u):
        self.ids.append(pid); self.U.append(u); self.Y.append(self.w.run(u, 999 if pid < 0 else pid))

    @property
    def arr(self): return np.stack(self.U), np.stack(self.Y)


def fit_state(U, Y):
    al, be, sg = H0.fit_x1(U, Y); a, b3, k = H0.fit_skeleton(Y[0, :, 1], U[0, :, 1])
    return al, be, sg, dict(al=al, be=be, a=a, b3=b3, k=k)


def thr(cal, kind, B):
    if cal is None: return np.inf
    d = {int(k): v for k, v in cal[kind].items()}
    return d[B] if B in d else d[min(d, key=lambda b: abs(b - B))]


def discover(U, Y, B, cal, mode, order=STAGE_ORDER):
    """One revision: returns the agent's current explanation with the full generation trace."""
    t0 = time.time(); al, be, sg, st = fit_state(U, Y); tr = []; nc = 0
    if callable(order): order = order(U, Y, st, sg)
    crit = lambda h: lang.nlp(lang.episode_pvalues(h, al, be, U, Y, sg).min())
    cin = thr(cal, "in", B)
    if mode == "static_all":
        keys = lang.keys_upto(3); top, allh, n, st2 = lang.search(U, Y, st, keys, True, True); nc += n
        h = top[0]; s = crit(h); tr.append(dict(stage="all", cols=n, best=lang.label(h), bic=h["bic"], s_in=s))
        return dict(h=h, top=top, al=al, be=be, sg=sg, st2=st2, s_in=s, accepted=s <= cin, stage_used="all", ncol=nc, nstage=1, trace=tr, time=time.time() - t0, h0=None)
    top0, _, n, st2 = lang.search(U, Y, st, lang.keys_stage(0), True, False); nc += n
    h0 = top0[0]; s0 = crit(h0); tr.append(dict(stage=0, cols=n, best=lang.label(h0), bic=h0["bic"], s_in=s0, rejected=s0 > cin))
    base = dict(h=h0, top=top0, al=al, be=be, sg=sg, st2=st2, s_in=s0, accepted=s0 <= cin, stage_used=0, ncol=nc, nstage=0, trace=tr, h0=h0)
    if mode == "L0" or s0 <= cin:
        base["time"] = time.time() - t0; return base
    seen = []
    for stg in order:                                                             # diagnose-by-extension: cheapest/most specific class first
        keys = lang.keys_stage(0) + (lang.keys_stage(stg) if stg < 4 else [])
        top, allh, n, st2s = lang.search(U, Y, st, keys, True, stg == 4); nc += n
        h = top[0]; s = crit(h); dbic = h0["bic"] - h["bic"]
        tr.append(dict(stage=stg, cols=n, best=lang.label(h), bic=h["bic"], dbic_vs_L0=dbic, s_in=s, accepted=bool(dbic > DBIC and s <= cin)))
        seen.append((h["bic"], h, top, st2s, s))
        if dbic > DBIC and s <= cin:
            return dict(h=h, top=top, al=al, be=be, sg=sg, st2=st2s, s_in=s, accepted=True, stage_used=stg, ncol=nc, nstage=len(tr) - 1, trace=tr, time=time.time() - t0, h0=h0)
    keys = lang.keys_upto(3); top, allh, n, st2s = lang.search(U, Y, st, keys, True, True); nc += n    # last resort: everything at once
    h = top[0]; s = crit(h); dbic = h0["bic"] - h["bic"]
    tr.append(dict(stage="combined", cols=n, best=lang.label(h), bic=h["bic"], dbic_vs_L0=dbic, s_in=s, accepted=bool(dbic > DBIC and s <= cin)))
    seen.append((h["bic"], h, top, st2s, s))
    if dbic > DBIC and s <= cin:
        return dict(h=h, top=top, al=al, be=be, sg=sg, st2=st2s, s_in=s, accepted=True, stage_used="combined", ncol=nc, nstage=len(tr) - 1, trace=tr, time=time.time() - t0, h0=h0)
    _, h, top, st2s, s = min(seen, key=lambda q: q[0])                            # nothing passes: report best-BIC explanation as a predictive surrogate and abstain
    return dict(h=h, top=top, al=al, be=be, sg=sg, st2=st2s, s_in=s, accepted=False, stage_used=None, ncol=nc, nstage=len(tr) - 1, trace=tr, time=time.time() - t0, h0=h0)


def choose(design, data, res, rng, cfg, mask):
    free = [i for i in range(len(POOL)) if i not in data.ids and mask[i]]
    if design == "random": return int(rng.choice(free))
    if design == "sweepB":
        for i in E.SWEEP_B:
            if i not in data.ids and mask[i]: return i
        return free[0]
    if design == "falsify":
        h = res["h"]; alts = [h] + [x for x in res["top"] if lang.desc(x) != lang.desc(h)][:3]
        if len(alts) < 2: alts = alts + [res["h0"] or lang.mk([], [], 0, 0, (h["a"], h["b3"], h["k"]), 1.0, 1)]
        P = np.stack([lang.predict(a, res["al"], res["be"], POOL_U) for a in alts]); sc = (((P[1:] - P[:1]) ** 2).sum(2) / res["sg"] ** 2).max(0)
    elif design == "ens":
        U, Y = data.arr; ens = bl.fit_narx_ensemble(U, Y, cfg["lam_narx"], 6, rng); sc = np.stack([f(POOL_U) for f in ens]).var(0).sum(1)
    else: raise ValueError(design)
    sc = np.asarray(sc, float); sc[[i for i in range(len(POOL)) if i not in free]] = -np.inf; return int(np.argmax(sc))


def rmse(p, t): return float(np.sqrt(np.mean((p - t) ** 2)))


def run_agent(inst, iseed, Bs, design, mode, cal, tests, cfg, noise=1.0, pool_mask=None, order=STAGE_ORDER):
    rng = np.random.default_rng([iseed, 4242]); world = bench.World(inst, iseed, noise); data = Data(world)
    mask = pool_mask if pool_mask is not None else np.ones(len(POOL), bool)
    Ut, truth = tests; eq_U = np.concatenate([POOL_U, np.stack(E.random_programmes(100, np.random.default_rng([iseed, 5151])))])
    out, oos, t0, cols, wall = {}, None, time.time(), 0, 0.0
    while True:
        B = len(data.U)
        if B in Bs or design in ("falsify", "ens"):
            U, Y = data.arr; res = discover(U, Y, B, cal, mode, order); cols += res["ncol"]; wall += res["time"]
        if B in Bs:
            h = res["h"]; al, be, sg = res["al"], res["be"], res["sg"]
            alts = [x for x in res["top"][1:] if x["bic"] - h["bic"] < DBIC]; amb = 0.0
            if alts:
                Pb = lang.predict(h, al, be, eq_U); amb = max(float(np.sqrt(((lang.predict(x, al, be, eq_U) - Pb) ** 2).mean(1)).max()) for x in alts)
            r = rmse(lang.predict(h, al, be, Ut), truth); s_oos = None if oos is None else lang.nlp(oos)
            out[B] = dict(B=B, rmse=r, ok=r <= TAU, s_in=res["s_in"], s_oos=s_oos, amb_ratio=amb / sg, sig=sg, label=lang.label(h), desc=list(lang.desc(h)),
                          terms=[tuple(t) for t in h["terms"]], w=h["w"].tolist(), kappa=h["kappa"], gamma=h["gamma"], npar=h["npar"], nnew=h["nnew"],
                          accepted=res["accepted"], stage_used=res["stage_used"], ncol=cols, wall=wall, nstage=res["nstage"], trace=res["trace"], ids=list(data.ids),
                          runs=world.n_runs, rmse_l0=None)
            if res.get("h0") is not None and res["h0"] is not h: out[B]["rmse_l0"] = rmse(lang.predict(res["h0"], al, be, Ut), truth)
            elif res.get("h0") is not None: out[B]["rmse_l0"] = r
        if B >= max(Bs): break
        pid = choose(design, data, res if design in ("falsify", "ens") else None, rng, cfg, mask)
        data.add(pid, POOL[pid])
        oos = lang.oos_p(res["h"], res["al"], res["be"], POOL[pid], data.Y[-1], res["sg"]) if design in ("falsify", "ens") else None
    return out


def decide(rec, cal, mode="full"):
    """Epistemic decision from stored statistics (calibrated thresholds)."""
    if mode == "nocrit": return "claim"
    B = rec["B"]; rej = not rec["accepted"] or rec["s_in"] > thr(cal, "in", B)
    if mode == "full" and rec["s_oos"] is not None and rec["s_oos"] > thr(cal, "oos", B): rej = True
    if rej: return "abstain_ool"
    if rec["amb_ratio"] > EPS: return "abstain_amb"
    return "claim"


def make_tests(inst, k):
    rng = np.random.default_rng(1_000_000 + k); Ut = np.stack(E.random_programmes(24, rng))
    return Ut, np.stack([bench.simulate(inst, u)[1] for u in Ut])


def sweep_ids(n_total):
    """Episode ids of the matched schedule used by sweepB agents and all baselines: E0, E1, SWEEP_B, then the lowest unused pool index."""
    ids = [-1, IDX["u1 +1"]]
    for i in E.SWEEP_B:
        if len(ids) >= n_total: break
        if i not in ids: ids.append(i)
    while len(ids) < n_total: ids.append(next(i for i in range(len(POOL)) if i not in ids))
    return ids


def propose_order(U, Y, st, x2h):
    """World-model role: order the expansion stages by equation-error evidence on a reconstructed hidden state.  For each stage the best single-column regression
    of the drive phi = d x2hat/dt + a x2hat - k u2 on the stage's candidate signals (BIC); stages are tried best-first."""
    from scipy.signal import savgol_filter
    xe, xm = H0.x1_ends_mid(U[..., 0], st["al"], st["be"]); D = (savgol_filter(x2h, 9, 3, deriv=1, delta=bench.DT, axis=-1) + st["a"] * x2h - st["k"] * U[..., 1]).ravel(); n = D.size
    def best(sigs):
        s = np.inf
        for v in sigs:
            A = np.stack([v.ravel()], 1); w = np.linalg.lstsq(A, D, rcond=None)[0]; sse = ((D - A @ w) ** 2).sum(); s = min(s, n * np.log(sse / n) + 2 * np.log(n))
        return s
    sc = {stg: best([lang.term_sig(k, xe, xm) for k in lang.keys_stage(stg)]) for stg in (1, 2, 3)}
    sc[4] = best([xm * x2h])
    return tuple(sorted(sc, key=sc.get))
