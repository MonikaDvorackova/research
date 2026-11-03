"""Phase 10 DEVELOPMENT: approximate EM maximisers and sequential validity.  python scripts/phase10_em.py results/phase10_dev
Part 1: optimiser gap against the true-parameter likelihood and a many-restart reference, by restarts / iteration budget / tolerance (40 independent small HMMs).
Part 2: type-I of an e-process whose denominator is an EM fit, with a predictable plug-in numerator, under a CORRECTLY SPECIFIED null (truth in the class, S known),
        symmetric versus asymmetric optimiser budgets; decomposition  log E = (ll_num - ll_true) + (ll_true - ll_den).
Truth is used only to evaluate (never given to the observer's fits)."""
import sys, os, json, time
from concurrent.futures import ProcessPoolExecutor
import numpy as np
import eid.e6gen as e6gen
e6gen.NS_DEV = 10000
from eid.e6gen import gen_hmm_small
from eid.e6streams import streams, registry_row, dump_registry
from eid.iohmm import em_fit, loglik
from eid.phase8 import simulate_stream
from eid.pomdp import A, O

M_STRUCT, NTR = 40, 800
CFG_GAP = [(r, it, 1e-6) for r in (1, 5, 20) for it in (20, 60, 300, 1000)] + [(5, 1000, 1e-3), (5, 300, 1e-3)]
DEN = {"sym(R5,B300)": (5, 300), "asym(R1,B60)": (1, 60), "asym(R1,B20)": (1, 20), "best(R10,B600)": (10, 600)}
BLOCKS = [100, 100, 200, 400]

def data(idx, rep, n):
    p, d = gen_hmm_small(idx); st = streams("hmm_small", idx, rep)
    ctx, obs = simulate_stream((p, p), None, lambda e: 1 / 3, n, 4, st["eval"])
    return p, d, ctx % A, obs, st

def fit_best(acts, obs, S, rng, R, B, tol=1e-6):
    best = None
    for _ in range(R):
        Tm, Zm, b0, ll, _ = em_fit(acts, obs, S, rng, iters=B, tol=tol)
        if best is None or ll > best[3]: best = (Tm, Zm, b0, ll)
    return best

def job_gap(idx):
    p, d, acts, obs, st = data(idx, 0, NTR); S = p.S
    ll_true = loglik(p.T, p.Z, p.b0, acts, obs)
    ref = fit_best(acts, obs, S, st["train"], 20, 1000)[3]; ref = max(ref, ll_true)
    rows = []
    for (R, B, tol) in CFG_GAP:
        rng = np.random.default_rng(np.random.SeedSequence([10000, 7, idx, R, B, int(tol * 1e6)])); t0 = time.perf_counter()
        ll = fit_best(acts, obs, S, rng, R, B, tol)[3]
        rows.append(dict(kind="gap", idx=idx, S=S, R=R, B=B, tol=tol, short_true=ll_true - ll, short_ref=ref - ll, secs=time.perf_counter() - t0))
    return rows

def block_ll(Tm, Zm, b0, acts, obs):
    return loglik(Tm, Zm, b0, acts, obs)

def job_eproc(args):
    idx, rep = args
    p, d, acts, obs, st = data(idx, 100 + rep, sum(BLOCKS)); S = p.S
    rng = st["train"]
    edges = np.cumsum([0] + BLOCKS)
    # predictable numerator: block 1 under an uninformative fixed model, block k under EM fit (R5,B300) on blocks < k
    Tm0 = np.full((A, S, S), 1 / S); Z0 = np.full((S, O), 1 / O); b00 = np.full(S, 1 / S)
    logq = []; cum = 0.0
    for k in range(len(BLOCKS)):
        sl = slice(edges[k], edges[k + 1])
        if k == 0: th = (Tm0, Z0, b00)
        else: th = fit_best(acts[:edges[k]], obs[:edges[k]], S, rng, 5, 300)[:3]
        cum += loglik(*th, acts[sl], obs[sl]); logq.append(cum)
    # a good FIXED alternative: the true parameters mixed 10 % with random rows (the experimenter builds it; the observer's test only needs a fixed law)
    ra = np.random.default_rng(np.random.SeedSequence([10000, 9, idx, rep]))
    alt = (0.9 * p.T + 0.1 * ra.dirichlet(np.ones(S), size=(A, S)), 0.9 * p.Z + 0.1 * ra.dirichlet(np.ones(O), size=S), 0.9 * p.b0 + 0.1 * ra.dirichlet(np.ones(S)))
    ll_alt = [loglik(*alt, acts[:edges[k + 1]], obs[:edges[k + 1]]) for k in range(len(BLOCKS))]
    out = dict(kind="eproc", idx=idx, rep=rep, S=S, rej={}, rej_alt={}, final={}, final_alt={})
    for name in ["true"] + list(DEN):
        rej = False; rej_alt = False; short = None; short_alt = None
        for k in range(len(BLOCKS)):
            a_, o_ = acts[:edges[k + 1]], obs[:edges[k + 1]]
            ll_true = loglik(p.T, p.Z, p.b0, a_, o_)
            if name == "true": ll_den = ll_true
            else:
                R, B = DEN[name]; ll_den = fit_best(a_, o_, S, np.random.default_rng(np.random.SeedSequence([10000, 8, idx, rep, k, R, B])), R, B)[3]
            logE = logq[k] - ll_den
            if logE >= np.log(20): rej = True
            if ll_alt[k] - ll_den >= np.log(20): rej_alt = True
            short = (ll_true - ll_den, logq[k] - ll_true); short_alt = (ll_true - ll_den, ll_alt[k] - ll_true)
        out["rej"][name] = rej; out["final"][name] = short; out["rej_alt"][name] = rej_alt; out["final_alt"][name] = short_alt
    return out

if __name__ == "__main__":
    out = sys.argv[1]; t0 = time.time()
    with ProcessPoolExecutor(11) as ex:
        gap = [r for rows in ex.map(job_gap, range(M_STRUCT)) for r in rows]
        ep = list(ex.map(job_eproc, [(i, r) for i in range(M_STRUCT) for r in range(3)], chunksize=2))
    with open(os.path.join(out, "em_runs.jsonl"), "w") as f:
        for r in gap + ep: f.write(json.dumps(r) + "\n")
    dump_registry([registry_row("hmm_small", i, gen_hmm_small(i)[1], train_coverage="uniform actions", reset="state (episodic)", model_class="IO-HMM(S known)") for i in range(M_STRUCT)], os.path.join(out, "registry_hmm_small.jsonl"))
    print("done", round(time.time() - t0))
