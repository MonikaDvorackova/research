"""Phase 9 development: (1) approximate-maximiser audit: how often does multi-start EM reach a likelihood >= the likelihood at the TRUE parameters (denominator dominance)?
(2) confidence-set denominator (T6d) feasibility: type-I, power and vacuity versus training coverage.  python scripts/phase9_dev_em_cs.py results/phase9_dev"""
import sys, time, json
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from eid.e6gen import gen_hmm, gen_markov
from eid.iohmm import em_fit, loglik
from eid.e6proc import cs_repair_etest
from eid.phase8 import simulate_stream, change_action2
from eid.pomdp import A, O

out = sys.argv[1]; L = []
def w(s=""): print(s); L.append(s)

def em_job(args):
    idx, ntr, iters = args; restarts = 10
    p, d = gen_hmm(idx)
    if p.S > 4: return None
    rng = np.random.default_rng(np.random.SeedSequence([9000, 88, idx, ntr]))
    acts = rng.integers(0, A, (ntr, 4))
    # simulate episodes with the uniform open-loop actions
    from eid.phase8 import simulate_stream
    ctx, obs = simulate_stream((p, p), None, lambda e: 1 / 3, ntr, 4, rng); acts = ctx % A
    ll_true = loglik(p.T, p.Z, p.b0, acts, obs)
    t0 = time.perf_counter(); lls = []
    for r in range(restarts):
        lls.append(em_fit(acts, obs, p.S, rng, iters=iters)[3])
    return dict(idx=idx, S=p.S, ntr=ntr, iters=iters, ll_true=ll_true, lls=lls, secs=time.perf_counter() - t0)

def cs_job(args):
    idx, ntr, train_pol, cond, rep = args
    mk, _ = gen_markov(idx); ch = change_action2(mk, idx)
    rng = np.random.default_rng(np.random.SeedSequence([9000, 89, idx, ntr, 0 if train_pol == "narrow" else 1, 0 if cond == "null" else 1, rep]))
    pol = (lambda e: 0.02) if train_pol == "narrow" else (lambda e: 1 / 3)
    tr = simulate_stream((mk, mk), None, pol, ntr, 4, rng)
    te = simulate_stream((mk, ch if cond == "change" else mk), 500 if cond == "change" else None, lambda e: 1 / 3, 1500, 4, rng)
    t0 = time.perf_counter(); r = cs_repair_etest(*tr, *te)
    return dict(idx=idx, ntr=ntr, train=train_pol, cond=cond, rej=r, secs=time.perf_counter() - t0)

if __name__ == "__main__":
    with ProcessPoolExecutor(11) as ex:
        em = [r for r in ex.map(em_job, [(i, n, it) for i in range(14) for n in (500, 5000) for it in (60, 300)]) if r]
        cs = list(ex.map(cs_job, [(i, n, tp, c, r) for i in range(10) for n in (100, 1000, 10000) for tp in ("narrow", "uniform") for c in ("null", "change") for r in range(2)], chunksize=2))
    w("## E. Approximate maximiser: multi-start EM (10 random starts) against the likelihood at the TRUE parameters (hidden-state instances with S <= 4, uniform actions, T = 4)\n")
    w("| instance | hidden states | training episodes | EM iterations | starts below the true-parameter log-likelihood by > 0.5 nats | worst shortfall (nats) | best start − true (nats) | seconds for 10 starts |\n|---|---|---|---|---|---|---|---|")
    for r in em:
        d = np.array(r["lls"]) - r["ll_true"]
        w(f"| {r['idx']} | {r['S']} | {r['ntr']} | {r['iters']} | {int((d < -0.5).sum())}/10 | {d.min():.1f} | {d.max():+.2f} | {r['secs']:.0f} |")
    for it in (60, 300):
        sub = [r for r in em if r["iters"] == it]
        tot = sum(int((np.array(r['lls']) - r['ll_true'] < -0.5).sum()) for r in sub); n = 10 * len(sub)
        w(f"\nEM budget {it} iterations: {tot}/{n} starts ended below the true-parameter likelihood by > 0.5 nats; a denominator built from any such start is NOT an upper bound on the true null likelihood.")
    w("\n## F. Confidence-set denominator (T6d): rejection rate within 1500 test episodes (wide policy); Markov instances (10), 2 reps; level alpha = 0.05, alpha1 = 0.05\n")
    w("| training policy | training episodes | unchanged kernel (type-I; guarantee <= 0.10) | kernel change in action-2 rows at episode 500 | median seconds per run |\n|---|---|---|---|---|")
    for tp in ("narrow", "uniform"):
        for ntr in (100, 1000, 10000):
            a = [r for r in cs if r["train"] == tp and r["ntr"] == ntr and r["cond"] == "null"]; b = [r for r in cs if r["train"] == tp and r["ntr"] == ntr and r["cond"] == "change"]
            w(f"| {tp} | {ntr} | {sum(r['rej'] is not None for r in a)}/{len(a)} | {sum(r['rej'] is not None for r in b)}/{len(b)} | {np.median([r['secs'] for r in a+b]):.1f} |")
    open(out + "/em_cs_dev.md", "w").write("\n".join(L) + "\n")
