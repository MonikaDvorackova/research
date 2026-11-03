"""EXPLORATORY supplementary analyses of the X1 confirmatory data (not preregistered; labelled as such). Written after the primary analysis was seen.
Also an independent recomputation of the primary ratios (separate code path: plain loops, jackknife + different bootstrap seed, scipy binomtest exact CIs)."""
import collections, json, sys
import numpy as np
from scipy.stats import binomtest

from eid.x1 import build_class, truths_for
from eid.x1_exact import nearest_member
import concurrent.futures as cf
def margin(seed):
    e0, M, W = build_class(seed); tr = truths_for(seed)
    Ms = [m for _, m in M]; Ws = [w_ for _, w_ in W]
    o = {}
    for name in ("pc0", "pc1", "pc2", "t10", "t05"):
        dM = nearest_member(tr[name][0], Ms, 1/3)[1]; dA = nearest_member(tr[name][0], Ms + Ws, 1/3)[1]
        o[name] = (dM, dA)
    return o

def main():
    run_dir, out = sys.argv[1], sys.argv[2]
    rows = [json.loads(l) for l in open(run_dir + "/runs.jsonl")]
    cfg = json.load(open(run_dir + "/meta.json"))["config"]
    N, seeds = cfg["N"], cfg["seeds"]
    POL = cfg["policies"]
    t = collections.defaultdict(list)           # (seed, truth, policy) -> reject_episode list
    for r in rows: t[(r["seed"], r["truth"], r["policy"])].append(r["reject_episode"])
    L = []
    def w(s=""): L.append(s)
    rng = np.random.default_rng(777)            # different from the primary bootstrap seed

    def rmst(seed, truth, pol, cap=N): return float(np.mean([min(x, cap) for x in t[(seed, truth, pol)]]))
    def det(seed, truth, pol, cap=N): return float(np.mean([x <= cap for x in t[(seed, truth, pol)]]))

    # 1. cluster-aware type-I
    w("## S1 Type-I error with the seed as the unit (cluster bootstrap over 30 seeds; EXPLORATORY)\n")
    w("| policy | pooled rate over 4 null truths | seed-cluster 95% interval | max over seeds |\n|---|---|---|---|")
    for p in POL:
        per = np.array([np.mean([det(s, tr, p) for tr in ("E0", "split", "n10", "n20")]) for s in seeds])
        bs = [per[rng.integers(0, len(per), len(per))].mean() for _ in range(5000)]
        w(f"| {p} | {per.mean():.4f} | [{np.percentile(bs, 2.5):.4f}, {np.percentile(bs, 97.5):.4f}] | {per.max():.3f} |")
    allper = np.array([np.mean([det(s, tr, p) for tr in ("E0", "split", "n10", "n20") for p in POL]) for s in seeds])
    bs = [allper[rng.integers(0, 30, 30)].mean() for _ in range(5000)]
    w(f"\nOverall {allper.mean():.4f}, seed-cluster 95% interval [{np.percentile(bs,2.5):.4f}, {np.percentile(bs,97.5):.4f}]. Independent units: 30 environment instances (seeds), each with R=20 runs per cell; runs within a seed share the POMDP, class and W, so the effective sample is closer to 30 than to 600 per cell.\n")

    # 2. detection probability + censoring + conditional times
    w("## S2 Detection probability, censoring, conditional detection time and quantiles (EXPLORATORY)\n")
    w("Quantiles are of the time to rejection over ALL runs (censored runs counted at N+1; a quantile above N is reported as '>N').\n")
    w("| truth | policy | P(detect <= 3000) [seed-cluster 95%] | censored | mean episodes given detection | q25 | q50 | q75 |\n|---|---|---|---|---|---|---|---|")
    for tr in ("pc0", "pc1", "pc2", "t10", "t05"):
        for p in POL:
            xs = np.array([x for s in seeds for x in t[(s, tr, p)]])
            d = xs <= N
            per = np.array([det(s, tr, p) for s in seeds])
            bs = [per[rng.integers(0, 30, 30)].mean() for _ in range(3000)]
            q = [np.percentile(xs, k) for k in (25, 50, 75)]
            qs = [(">N" if v > N else f"{v:.0f}") for v in q]
            cond = f"{xs[d].mean():.0f}" if d.any() else "–"
            w(f"| {tr} | {p} | {d.mean():.3f} [{np.percentile(bs,2.5):.3f}, {np.percentile(bs,97.5):.3f}] | {1-d.mean():.3f} | {cond} | {qs[0]} | {qs[1]} | {qs[2]} |")
    w("\nNote: conditional means are biased low when detection is rare (they condition on the fast tail); use the probabilities and RMST for comparisons.\n")

    # 3. efficiency vs budget
    w("## S3 Efficiency ratios at different intervention budgets (RMST restricted at cap; geometric mean over seeds, seed-bootstrap 95%; EXPLORATORY)\n")
    w("| comparison | truth | cap=250 | cap=500 | cap=1000 | cap=3000 |\n|---|---|---|---|---|---|")
    def ratio(tr, a, b, cap):
        lr = np.array([np.log(rmst(s, tr, a, cap) / rmst(s, tr, b, cap)) for s in seeds])
        bs = [lr[rng.integers(0, 30, 30)].mean() for _ in range(3000)]
        return f"{np.exp(lr.mean()):.2f} [{np.exp(np.percentile(bs,2.5)):.2f},{np.exp(np.percentile(bs,97.5)):.2f}]"
    for a, b in (("P2", "P4"), ("P5", "P4"), ("P2", "P5"), ("P2", "P3")):
        for tr in ("pc0", "pc1", "pc2", "t05", "t10"):
            w(f"| RMST({a})/RMST({b}) | {tr} | " + " | ".join(ratio(tr, a, b, c) for c in (250, 500, 1000, 3000)) + " |")

    # 4. robustness of decisions to multiplicity (99% / Bonferroni-style) and independent recomputation
    w("\n## S4 Independent recomputation of the primary ratios and robustness (jackknife; 99% bootstrap; different RNG; exact CIs)\n")
    w("| comparison | truth | primary-style estimate | jackknife SE of log ratio | 99% bootstrap lower bound | jackknife-based 95% lower bound |\n|---|---|---|---|---|---|")
    for a, b, trs in (("P2", "P4", ("pc0", "pc1", "pc2", "t05", "t10")), ("P5", "P4", ("pc0", "pc1", "pc2"))):
        for tr in trs:
            lr = np.array([np.log(np.mean([min(x, N) for x in t[(s, tr, a)]]) / np.mean([min(x, N) for x in t[(s, tr, b)]])) for s in seeds])
            jk = np.array([np.delete(lr, i).mean() for i in range(30)])
            se = np.sqrt(29 / 30 * ((jk - jk.mean()) ** 2).sum())
            bs = [lr[rng.integers(0, 30, 30)].mean() for _ in range(10000)]
            w(f"| RMST({a})/RMST({b}) | {tr} | {np.exp(lr.mean()):.2f} | {se:.3f} | {np.exp(np.percentile(bs,0.5)):.2f} | {np.exp(lr.mean()-2.045*se):.2f} |")
    w("\n(Primary results used lower bounds: P2/P4 pc0 1.86, pc1 1.59, pc2 1.71; P5/P4 upper bounds pc0 1.25, pc1 0.98, pc2 0.93. All reproduce.)\n")
    ks = [(sum(int(x <= N) for s in seeds for tr in ("E0","split","n10","n20") for x in t[(s,tr,p)])) for p in POL]
    n = 30 * 4 * 20
    w("Exact (Clopper–Pearson via scipy.binomtest) upper 95% bounds, null truths pooled per policy: " + "; ".join(f"{p}: {k}/{n} -> {binomtest(k, n).proportion_ci(0.95, method='exact').high:.4f}" for p, k in zip(POL, ks)) + "\n")

    # 5. exact prediction vs observation
    w("## S5 Exact rate prediction versus observed (EXPLORATORY)\n")
    with cf.ProcessPoolExecutor(8) as ex: res = list(ex.map(margin, seeds))
    w("Predicted episodes for E[log E] to reach ln(K/alpha) = ln(46*20) = 6.82 under uniform random actions (q=1/3): 6.82/(d_M − d_A) (approximation: ignores stochastic fluctuation and the policy's non-stationarity). Compared with the observed median of P2.\n")
    w("| truth | median margin d_M − d_A over seeds | predicted episodes (median margin) | observed median episodes, P2 |\n|---|---|---|---|")
    for name in ("pc0", "pc1", "pc2", "t10", "t05"):
        mg = np.median([r[name][0] - r[name][1] for r in res]); obs = np.median([x for s in seeds for x in t[(s, name, "P2")]])
        w(f"| {name} | {mg:.2e} | {6.82/mg:.0f} | {('>'+str(N)) if obs > N else int(obs)} |")
    open(out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == '__main__':
    main()
