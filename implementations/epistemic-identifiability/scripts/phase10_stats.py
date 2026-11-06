"""Phase 10 statistical design audit (development data + simulation).  python scripts/phase10_stats.py results/phase10_dev"""
import sys, json, collections
import numpy as np
from scipy.stats import beta as betad, t as tdist
from eid.phase9_audit import cp_upper, betabin_sample
out = sys.argv[1]; L = []
def w(s=""): print(s); L.append(s)
rows = [json.loads(l) for l in open(out + "/certified_runs.jsonl")]

def anova_icc(groups):
    k = len(groups); n = np.array([len(g) for g in groups]); N = n.sum(); m = N / k
    means = np.array([np.mean(g) for g in groups]); grand = np.concatenate(groups).mean()
    msb = (n * (means - grand) ** 2).sum() / (k - 1); msw = sum(((np.array(g) - np.mean(g)) ** 2).sum() for g in groups) / (N - k)
    n0 = (N - (n ** 2).sum() / N) / (k - 1)
    return (msb - msw) / (msb + (n0 - 1) * msw) if msb + (n0 - 1) * msw > 0 else float("nan")

w("## S1. Intra-structure dependence measured on the development runs (60 independent Markov structures)\n")
w("| outcome | runs per structure | mean | ICC (ANOVA) | design effect 1+(R-1)ICC |\n|---|---|---|---|---|")
nl = [r for r in rows if r["kind"] == "null"]
for tp, ntr in (("narrow", 1000), ("narrow", 10000), ("uniform", 1000)):
    for key, lab in (("frozen", "frozen-null rejection (simple null; semantic false alarm)"), ("cert", "certified rejection (type-I)")):
        g = collections.defaultdict(list)
        for r in nl:
            if r["train"] == tp and r["ntr"] == ntr: g[r["idx"]].append(float(r[key] is not None))
        gs = [v for v in g.values()]; mean = np.mean(np.concatenate(gs))
        if mean in (0.0, 1.0): w(f"| {lab}, {tp}/{ntr} | 30 | {mean:.4f} | undefined (no variation) | – |")
        else:
            icc = anova_icc(gs); w(f"| {lab}, {tp}/{ntr} | 30 | {mean:.4f} | {icc:.3f} | {1+29*icc:.1f} |")
pw = [r for r in rows if r["kind"] == "power"]
for tp, ntr in (("uniform", 10000), ("uniform", 1000), ("narrow", 10000)):
    g = collections.defaultdict(list)
    for r in pw:
        if r["train"] == tp and r["ntr"] == ntr: g[r["idx"]].append(np.log((r["cert"] or 3001) / (r["oracle"] or 3001)))
    gs = list(g.values()); icc = anova_icc(gs)
    w(f"| log(certified delay / oracle delay), {tp}/{ntr} | 8 | {np.mean(np.concatenate(gs)):.3f} | {icc:.3f} | {1+7*icc:.1f} |")

w("\n## S2. Coverage of one-sided 95 % upper bounds for a rate, m = 60 structures x R = 60 runs, 300 simulated datasets\n")
def cov(mean, icc, m, R, reps, rng, boot=200):
    r = {"pooled CP": 0, "cluster t": 0, "cluster bootstrap": 0, "design-effect-adjusted CP": 0}
    for _ in range(reps):
        ks = betabin_sample(rng, m, R, mean, icc); rates = ks / R
        r["pooled CP"] += cp_upper(int(ks.sum()), m * R) >= mean
        se = rates.std(ddof=1) / np.sqrt(m); r["cluster t"] += rates.mean() + tdist.ppf(0.95, m - 1) * se >= mean
        bs = np.array([rates[rng.integers(0, m, m)].mean() for _ in range(boot)]); r["cluster bootstrap"] += np.percentile(bs, 95) >= mean
        g = [np.r_[np.ones(k), np.zeros(R - k)] for k in ks]
        icc_hat = max(0.0, anova_icc(g)) if 0 < ks.sum() < m * R else 0.0
        neff = m * R / (1 + (R - 1) * icc_hat); kk = int(round(rates.mean() * neff)); r["design-effect-adjusted CP"] += cp_upper(kk, int(round(neff))) >= mean
    return {k: v / reps for k, v in r.items()}
rng = np.random.default_rng(2026)
w("| true mean rate | ICC | pooled CP | cluster t | cluster bootstrap | design-effect-adjusted CP |\n|---|---|---|---|---|---|")
for mean in (0.05, 0.02):
    for icc in (0.0, 0.05, 0.2, 0.5):
        c = cov(mean, icc, 60, 60, 300, rng)
        w(f"| {mean} | {icc} | {c['pooled CP']:.3f} | {c['cluster t']:.3f} | {c['cluster bootstrap']:.3f} | {c['design-effect-adjusted CP']:.3f} |")

w("\n## S3. Sample sizes from measured variability (exact exponents; development runs)\n")
w("Retained fraction of the oracle exponent, rho_s = Lambda_cert / Lambda_oracle per structure (from the exact information projection onto the LR confidence set):\n")
w("| training policy | training episodes | mean rho | between-structure SD of rho | structures for a 95 % interval half-width 0.05 on mean rho | structures for half-width 0.02 |\n|---|---|---|---|---|---|")
for tp in ("narrow", "uniform"):
    for ntr in (1000, 10000):
        g = collections.defaultdict(list)
        for r in pw:
            if r["train"] == tp and r["ntr"] == ntr: g[r["idx"]].append(r["lam_c"] / r["lam_o"])
        per = np.array([np.mean(v) for v in g.values()]); mu, tau = per.mean(), per.std(ddof=1)
        w(f"| {tp} | {ntr} | {mu:.3f} | {tau:.3f} | {int(np.ceil((1.96*tau/0.05)**2))} | {int(np.ceil((1.96*tau/0.02)**2))} |")
w("\nLog delay ratio (certified / oracle), variance components from the 8 runs per structure:\n")
w("| condition | between-structure SD | within-structure SD | structures m for a 95 % interval of +-10 % on the geometric-mean ratio with R = 8 | with R = 30 |\n|---|---|---|---|---|")
for tp, ntr in (("uniform", 10000), ("uniform", 1000), ("narrow", 10000)):
    g = collections.defaultdict(list)
    for r in pw:
        if r["train"] == tp and r["ntr"] == ntr: g[r["idx"]].append(np.log((r["cert"] or 3001) / (r["oracle"] or 3001)))
    gs = list(g.values()); means = np.array([np.mean(v) for v in gs]); within = np.sqrt(np.mean([np.var(v, ddof=1) for v in gs]))
    between2 = max(means.var(ddof=1) - within ** 2 / 8, 0.0)
    need = lambda R: int(np.ceil((1.96 ** 2) * (between2 + within ** 2 / R) / np.log(1.1) ** 2))
    w(f"| {tp}/{ntr} | {np.sqrt(between2):.3f} | {within:.3f} | {need(8)} | {need(30)} |")
open(out + "/stats_audit.md", "w").write("\n".join(L) + "\n")
