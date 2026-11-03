"""Phase 10 DEVELOPMENT: certified learned-null procedure (LR confidence set).  python scripts/phase10_certified.py results/phase10_dev --workers 11
Namespace 10000 (independent streams per role).  All outcomes exploratory; no confirmatory data."""
import json, os, sys, time
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy.stats import beta as betad
import eid.e6gen as e6gen
e6gen.NS_DEV = 10000
from eid.e6gen import gen_markov
from eid.e6streams import streams, registry_row, dump_registry
from eid.e6proc import dir_logml
from eid.certified_null import (certified_etest, oracle_etest, frozen_point_etest, in_set, lr_gamma, exponent_under_set, exponent_oracle, sup_over_set, _xlogy)
from eid.phase8 import simulate_stream, NCTX, change_action2
from eid.pomdp import A, O

M_STRUCT = 60
CONDS = [("narrow", 1000), ("narrow", 10000), ("uniform", 1000), ("uniform", 10000)]
POL = {"narrow": (lambda e: 0.02), "uniform": (lambda e: 1 / 3)}

def true_kernel(mk):
    k = np.zeros((NCTX, O))
    for prev in range(O + 1):
        for a in range(A):
            k[prev * A + a] = mk.T[a, prev] if prev < O else mk.b0 @ mk.T[a]
    return k

def counts(ctx, obs):
    c = np.zeros((NCTX, O)); np.add.at(c, (ctx.ravel(), obs.ravel()), 1); return c

def job_null(args):
    idx, ti, rep = args
    tp, ntr = CONDS[ti]; st = streams("markov", idx, 1000 * ti + rep)
    mk, d = gen_markov(idx)
    ctx_tr, obs_tr = simulate_stream((mk, mk), None, POL[tp], ntr, 4, st["train"])
    ctx, obs = simulate_stream((mk, mk), None, lambda e: 1 / 3, 1500, 4, st["eval"])
    n = counts(ctx_tr, obs_tr)
    return dict(kind="null", idx=idx, train=tp, ntr=ntr, rep=rep,
                cert=certified_etest(n, ctx, obs)[1], oracle=oracle_etest(true_kernel(mk), ctx, obs)[1], frozen=frozen_point_etest(n, ctx, obs)[1])

def job_power(args):
    idx, ti, rep = args
    tp, ntr = CONDS[ti]; st = streams("markov", idx, 1000 * ti + rep + 500)
    mk, d = gen_markov(idx); ch = change_action2(mk, 7000 + idx)
    ctx_tr, obs_tr = simulate_stream((mk, mk), None, POL[tp], ntr, 4, st["train"])
    ctx, obs = simulate_stream((ch, ch), None, lambda e: 1 / 3, 3000, 4, st["eval"])     # post-change stream
    n = counts(ctx_tr, obs_tr); gam = lr_gamma(n, 0.05)
    k0 = true_kernel(mk); k1 = true_kernel(ch)
    w = counts(ctx, obs).sum(1); w = w / w.sum()
    lam_o = exponent_oracle(w, k1, k0); lam_c = exponent_under_set(w, k1, n, gam)
    return dict(kind="power", idx=idx, train=tp, ntr=ntr, rep=rep, cert=certified_etest(n, ctx, obs)[1], oracle=oracle_etest(k0, ctx, obs)[1],
                frozen=frozen_point_etest(n, ctx, obs)[1], lam_o=lam_o, lam_c=lam_c)

def job_cov(args):
    idx, rep = args
    st = streams("markov", idx, 50 + rep); mk, d = gen_markov(idx); k0 = true_kernel(mk)
    ctx, obs = simulate_stream((mk, mk), None, lambda e: 1 / 3, 5000, 4, st["train"])
    miss = False; c = np.zeros((NCTX, O))
    for k in range(1, 5000 // 25 + 1):
        seg = slice((k - 1) * 25, k * 25); np.add.at(c, (ctx[seg].ravel(), obs[seg].ravel()), 1)
        if not in_set(k0, c, 0.05): miss = True; break
    return dict(kind="cov", idx=idx, rep=rep, miss=miss)

def job_adv(args):
    idx, rep = args
    st = streams("markov", idx, 80 + rep); mk, d = gen_markov(idx); k0 = true_kernel(mk); rng = st["intervene"]; rngE = st["eval"]
    ctx_tr, obs_tr = simulate_stream((mk, mk), None, lambda e: 1 / 3, 1000, 4, st["train"]); n = counts(ctx_tr, obs_tr); gam = lr_gamma(n, 0.05)
    khat = (n + 0.5) / (n.sum(1, keepdims=True) + 0.5 * O)
    m = np.zeros((NCTX, O)); rej = None
    for ep in range(1500):
        prev = O
        for t in range(4):
            # ADVERSARY: choose the action whose context currently shows the largest gap between the test-stream prequential predictor and the training estimate
            best, besta = -1, 0
            for a in range(A):
                c = prev * A + a
                q = (m[c] + 0.5) / (m[c].sum() + 1.5)
                g = float((q * np.log(q / khat[c])).sum())
                if g > best: best, besta = g, a
            a = besta if rng.random() > 0.1 else int(rng.integers(0, A))
            c = prev * A + a
            o = int(rngE.choice(O, p=k0[c])); m[c, o] += 1; prev = o
        if (ep + 1) % 50 == 0 and rej is None:
            if dir_logml(m) - sup_over_set(m, n, gam) >= np.log(20): rej = ep + 1
    return dict(kind="adv", idx=idx, rep=rep, rej=rej)

def job_cpbox(rep):
    r = np.random.default_rng(np.random.SeedSequence([10000, 99, rep])); x = r.random(2000) < 0.5; k = np.cumsum(x); n = np.arange(1, 2001)
    lo = np.where(k == 0, 0.0, betad.ppf(0.025, np.maximum(k, 1), n - k + 1)); hi = np.where(k == n, 1.0, betad.ppf(0.975, k + 1, np.maximum(n - k, 1)))
    cp_miss = bool(((0.5 < lo) | (0.5 > hi)).any())
    # LR confidence sequence for a Bernoulli(1/2): log q(D)/p(D) <= log(1/delta)
    logq = gammaln_bern(k, n)
    lr_miss = bool((logq - n * np.log(0.5) >= np.log(1 / 0.05)).any())
    return dict(kind="cpbox", rep=rep, cp_miss=cp_miss, lr_miss=lr_miss)

def gammaln_bern(k, n):
    """log of the Dirichlet(1/2,1/2) marginal likelihood of a particular binary sequence with k ones among n."""
    from scipy.special import gammaln
    return gammaln(1.0) - gammaln(1.0 + n) + gammaln(0.5 + k) + gammaln(0.5 + n - k) - 2 * gammaln(0.5)

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 8
    t0 = time.time(); res = []
    with ProcessPoolExecutor(workers) as ex:
        res += list(ex.map(job_cov, [(i, r) for i in range(M_STRUCT) for r in range(5)], chunksize=4))
        res += list(ex.map(job_cpbox, range(1000), chunksize=20))
        res += list(ex.map(job_null, [(i, ti, r) for i in range(M_STRUCT) for ti in range(4) for r in range(30)], chunksize=10))
        res += list(ex.map(job_power, [(i, ti, r) for i in range(M_STRUCT) for ti in range(4) for r in range(8)], chunksize=8))
        res += list(ex.map(job_adv, [(i, r) for i in range(30) for r in range(10)], chunksize=5))
    with open(os.path.join(out, "certified_runs.jsonl"), "w") as f:
        for r in res: f.write(json.dumps(r) + "\n")
    rows = [registry_row("markov", i, gen_markov(i)[1], train_coverage="narrow|uniform", reset="state (observed-state Markov)", model_class="categorical Markov in (prev obs, action)") for i in range(M_STRUCT)]
    dump_registry(rows, os.path.join(out, "registry_markov.jsonl"))
    print("done", round(time.time() - t0))
