"""Phase 9 DEVELOPMENT experiment (exploratory): formal-null semantics of three sequential procedures across independently generated environments.
python scripts/phase9_dev_semantics.py results/phase9_dev --workers 11
Namespace SeedSequence([9000, 77, scenario, instance, rep]) -- disjoint from all earlier and reserved confirmatory seeds.
Flags (experimenter side, exact or stated): phys = the physical generating mechanism changed during the run; N_ctx/N_ep/N_comp = whether each procedure's FORMAL null holds."""
import json, os, sys, time
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from eid.e6gen import *
from eid.e6gen import simulate_stream_probs
from eid.e6proc import comp_cs_test, ctx_etest, ep_etest, prequential_probs
from eid.phase8 import NCTX, _contexts
from eid.pomdp import A, O

N, T = 3000, 4
UNI = [1 / 3] * 3; NARROW = [.49, .49, .02]; EXTREME = [.05, .05, .9]
HALF = 1500
def const(p): return lambda e: p
def sched(p1, p2, at=HALF): return lambda e: p1 if e < at else p2

SC = []

def mk_change(idx):
    mk, _ = gen_markov(idx); r = np.random.default_rng([9000, 5, idx]); a = int(r.integers(0, 3))
    T2 = mk.T.copy(); T2[a] = r.dirichlet(np.full(3, 0.5), size=3)
    from eid.pomdp import POMDP
    return (mk, POMDP(T2, mk.Z, mk.b0)), a
def hm_change(idx):
    (p, p2), d = gen_changing(idx); return (p, p2), d["changed_action"]
def not_a(a): v = np.array([.5, .5, .5]); v[a] = 0; return list(v / v.sum())

def run_one(args):
    si, idx, rep = args
    name, build, flags = SC[si]
    rng = np.random.default_rng(np.random.SeedSequence([9000, 77, si, idx, rep]))
    envs, change_at, probs, regime = build(idx)
    if regime is not None:
        pair, eps = regime
        from eid.e6gen import simulate_regime_stream
        ctx, obs, _ = simulate_regime_stream(pair, eps, N, T, 1 / 3, rng)
    else:
        ctx, obs = simulate_stream_probs(envs, change_at, probs, N, T, rng)
    out = dict(scenario=name, inst=idx, rep=rep, **{k: v for k, v in flags.items()})
    t0 = time.perf_counter(); out["E_ctx"] = ctx_etest(ctx, obs)[1]; out["t_ctx"] = time.perf_counter() - t0
    t0 = time.perf_counter(); out["E_ep"] = ep_etest(ctx, obs)[1]; out["t_ep"] = time.perf_counter() - t0
    t0 = time.perf_counter()
    c, y = ctx.ravel(), obs.ravel()
    p1 = prequential_probs(c, y, NCTX, O); pf = prequential_probs(c, y, NCTX, O, gamma=0.99)
    acts = (ctx % A); c2 = _contexts(acts, obs, 2).ravel(); p2 = prequential_probs(c2, y, (O + 1) ** 2 * A, O)
    out["E_comp_forget"] = comp_cs_test(p1, pf, y); out["E_comp_ord2"] = comp_cs_test(p1, p2, y)
    out["t_comp"] = time.perf_counter() - t0
    return out

def mk_build(kind):
    def f(idx):
        if kind == "markov_stat": return (gen_markov(idx)[0],) * 2, None, const(UNI), None
        if kind == "markov_shift": return (gen_markov(idx)[0],) * 2, None, sched(NARROW, UNI), None
        if kind == "markov_change": (e, a) = mk_change(idx); return e, HALF, const(UNI), None
        if kind == "markov_change_unplayed": (e, a) = mk_change(idx); return e, HALF, const(not_a(a)), None
        if kind == "hmm_stat": return (gen_hmm(idx)[0],) * 2, None, const(UNI), None
        if kind == "hmm_shift": return (gen_hmm(idx)[0],) * 2, None, sched(UNI, EXTREME), None
        if kind == "hmm_change": (e, a) = hm_change(idx); return e, HALF, const(UNI), None
        if kind == "hmm_change_unplayed": (e, a) = hm_change(idx); return e, HALF, const(not_a(a)), None
        if kind == "hmm_equiv_switch": e, _ = gen_equivalent_pair(idx); return e, HALF, const(UNI), None
        if kind == "regime": pair, d = gen_regime_pair(idx); return None, None, None, (pair, d["eps_per_episode"])
    return f
def add2(name, kind, phys, nctx, nep, cf, c2):
    SC.append((name, mk_build(kind), dict(phys=phys, N_ctx=nctx, N_ep=nep, N_comp_forget=cf, N_comp_ord2=c2)))
# flags: N_ctx and N_ep are exact consequences of the generator; N_comp_* are APPROXIMATE (expected asymptotic sign of the conditional Brier difference)
add2("M1 Markov, stationary", "markov_stat", False, True, True, True, True)
add2("M2 Markov, pure policy shift (C)", "markov_shift", False, True, True, True, True)
add2("M3 Markov, mechanism change, changed action played (D)", "markov_change", True, False, False, False, True)
add2("M4 Markov, mechanism change, changed action never played", "markov_change_unplayed", True, True, True, True, True)
add2("H1 hidden-state, stationary, resets", "hmm_stat", False, False, True, True, False)
add2("H2 hidden-state, extreme policy shift (B+C)", "hmm_shift", False, False, True, False, False)
add2("H3 hidden-state, mechanism change, played (B+D)", "hmm_change", True, False, False, False, False)
add2("H4 hidden-state, change in an action never played", "hmm_change_unplayed", True, False, True, True, False)
add2("H5 hidden-state, switch to bisimilar split-state twin", "hmm_equiv_switch", False, False, True, True, False)
add2("R1 persistent latent regime, stationary", "regime", False, False, False, False, False)

if __name__ == "__main__":
    out_dir = sys.argv[1]; os.makedirs(out_dir, exist_ok=True)
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 8
    jobs = [(si, idx, rep) for si in range(len(SC)) for idx in range(10) for rep in range(3)]
    t0 = time.time()
    with ProcessPoolExecutor(workers) as ex: res = list(ex.map(run_one, jobs, chunksize=3))
    with open(os.path.join(out_dir, "runs.jsonl"), "w") as f:
        for r in res: f.write(json.dumps(r) + "\n")
    json.dump(dict(N=N, T=T, instances=10, reps=3, wall=time.time() - t0, namespace=9000), open(os.path.join(out_dir, "meta.json"), "w"))
    print("done", round(time.time() - t0))
