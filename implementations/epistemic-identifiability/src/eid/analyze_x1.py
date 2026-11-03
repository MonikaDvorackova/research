"""Pre-specified analysis of X1 (frozen with the preregistration).  python -m eid.analyze_x1 --runs results/x1_confirm --out results/x1_confirm/analysis.md
All thresholds are constants below and were fixed before any confirmatory outcome existed."""
from __future__ import annotations

import argparse
import collections
import json

import numpy as np
from scipy.stats import beta

THRESH = 1.5            # required efficiency ratio (lower CI bound) for H4 / contradiction bound for H5
TYPEI_UB = 0.07         # H1/H2: upper 95% Clopper-Pearson bound must not exceed alpha + 0.02
POOLED_MAX = 0.05
POWER = 0.8             # H3
POWER_BUDGET = 1500     # episodes
BUDGETS = (100, 200, 400, 800, 1500, 3000)
NULLS = ("E0", "split", "n10", "n20")
ANTICIPATED = ("pc0", "pc1", "pc2")
UNANTICIPATED = ("t05", "t10")
NBOOT, BOOT_SEED = 10000, 20261103


def cp_upper(k, n, a=0.05):
    return 1.0 if k >= n else float(beta.ppf(1 - a, k + 1, n - k))


def cp_lower(k, n, a=0.05):
    return 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))


def load(path):
    rows = [json.loads(l) for l in open(path + "/runs.jsonl")]
    cfg = json.load(open(path + "/meta.json"))["config"]
    return rows, cfg


def ratio_ci(per_seed_logratio, rng):
    x = np.asarray(per_seed_logratio)
    bs = np.array([x[rng.integers(0, len(x), len(x))].mean() for _ in range(NBOOT)])
    return float(np.exp(x.mean())), float(np.exp(np.percentile(bs, 2.5))), float(np.exp(np.percentile(bs, 97.5)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    rows, cfg = load(a.runs)
    N, seeds = cfg["N"], cfg["seeds"]
    rng = np.random.default_rng(BOOT_SEED)
    cell = collections.defaultdict(list)
    sec = collections.defaultdict(float)
    for r in rows:
        cell[(r["truth"], r["policy"])].append(min(r["reject_episode"], N + 1))
        sec[r["policy"]] += r["seconds"]
    per = collections.defaultdict(list)             # (seed, truth, policy) -> restricted times min(T, N)
    for r in rows:
        per[(r["seed"], r["truth"], r["policy"])].append(min(r["reject_episode"], N))
    pols = [p for p in cfg["policies"]]
    out = [f"# X1 analysis ({a.runs})\n", f"seeds {seeds[0]}..{seeds[-1]} (n={len(seeds)}), R={cfg['R']}, N={N}, T={cfg['T']}, alpha={cfg['alpha']}\n"]
    res = {}

    # H1 type-I (null truths, all policies) and H2 barrier (P0 on unanticipated/pc2)
    out.append("\n## H1 Type-I error (truth in M)\n\n| truth | " + " | ".join(pols) + " |\n|---|" + "---|" * len(pols))
    ok_cells, tot_k, tot_n = True, 0, 0
    for t in NULLS:
        line = f"| {t} |"
        for p in pols:
            x = np.array(cell[(t, p)]); k, n = int((x <= N).sum()), len(x)
            ub = cp_upper(k, n); ok_cells &= ub <= TYPEI_UB; tot_k += k; tot_n += n
            line += f" {k}/{n} (UB {ub:.3f}) |"
        out.append(line)
    pooled = tot_k / tot_n
    pooled_lo = cp_lower(tot_k, tot_n)
    res["H1"] = "supported" if (ok_cells and pooled <= POOLED_MAX) else ("contradicted" if pooled_lo > POOLED_MAX else "inconclusive")
    out.append(f"\nPooled {tot_k}/{tot_n} = {pooled:.4f} (CP lower {pooled_lo:.4f}); all cell UB <= {TYPEI_UB}: {ok_cells}. **H1: {res['H1']}**\n")
    ok2, lines = True, []
    for t in UNANTICIPATED + ("pc2",):
        x = np.array(cell[(t, "P0")]); k, n = int((x <= N).sum()), len(x); ub = cp_upper(k, n); ok2 &= ub <= TYPEI_UB
        lines.append(f"{t}: {k}/{n} (UB {ub:.3f})")
    res["H2"] = "supported" if ok2 else "contradicted"
    out.append("## H2 Barrier (policy P0 never uses action 2; these truths equal a member's law on that class)\n\n" + "; ".join(lines) + f". **H2: {res['H2']}**\n")

    # H3 power
    out.append("## H3 Power of random wide intervention (P2): rejection rate within budget\n\n| truth | " + " | ".join(str(b) for b in BUDGETS if b <= N) + " |\n|---|" + "---|" * len([b for b in BUDGETS if b <= N]))
    h3 = True
    for t in ANTICIPATED + UNANTICIPATED:
        x = np.array(cell[(t, "P2")]); line = f"| {t} |"
        for b in BUDGETS:
            if b <= N:
                line += f" {(x <= b).mean():.3f} |"
        if t in ANTICIPATED:
            h3 &= (x <= POWER_BUDGET).mean() >= POWER
        out.append(line)
    res["H3"] = "supported" if h3 else "not supported"
    out.append(f"\nCriterion: P2 rejection within {POWER_BUDGET} episodes >= {POWER} for pc0, pc1, pc2. **H3: {res['H3']}**\n")

    # H4 / H4b / H5 : restricted-mean-time ratios
    def ratios(t, pa, pb):
        lr = [np.log(np.mean(per[(s, t, pa)]) / np.mean(per[(s, t, pb)])) for s in seeds]
        return ratio_ci(lr, rng)

    def block(title, truths, pa, pb, label):
        out.append(f"\n### {title}: RMST({pa}) / RMST({pb}) (restricted at N={N}; >1 means {pb} is faster); bootstrap over seeds\n\n| truth | ratio | 95% CI |\n|---|---|---|")
        r = {}
        for t in truths:
            m, lo, hi = ratios(t, pa, pb); r[t] = (m, lo, hi)
            out.append(f"| {t} | {m:.2f} | [{lo:.2f}, {hi:.2f}] |")
        return r
    out.append("\n## H4 Efficiency of class-level design P4 (primary comparator: random P2)\n")
    r4a = block("H4a anticipated deviations", ANTICIPATED, "P2", "P4", "H4a")
    res["H4a"] = "supported" if all(v[1] >= THRESH for v in r4a.values()) else ("contradicted" if any(v[2] < THRESH for v in r4a.values()) else "inconclusive")
    out.append(f"\n**H4a (lower CI bound >= {THRESH} for all of pc0, pc1, pc2): {res['H4a']}**\n")
    r4b = block("H4b unanticipated deviations", UNANTICIPATED, "P2", "P4", "H4b")
    res["H4b"] = "supported" if all(v[1] >= THRESH for v in r4b.values()) else ("contradicted" if any(v[2] < THRESH for v in r4b.values()) else "inconclusive")
    out.append(f"\n**H4b (same criterion for t05, t10): {res['H4b']}**\n")
    out.append("\n## H4c Fair comparator: P5 (within-class EIG over M u W) vs P4 (same information, different target)\n")
    r4c = block("H4c", ANTICIPATED + UNANTICIPATED, "P5", "P4", "H4c")
    res["H4c"] = "supported" if all(r4c[t][1] >= THRESH for t in ANTICIPATED) else ("contradicted" if any(r4c[t][2] < THRESH for t in ANTICIPATED) else "inconclusive")
    out.append(f"\n**H4c (anticipated truths, lower CI bound >= {THRESH}): {res['H4c']}**\n")

    out.append("\n## H5 Within-class EIG over M only (P3) is not faster than random (P2)\n")
    r5 = block("H5", ANTICIPATED + UNANTICIPATED, "P2", "P3", "H5")
    anyfast = any(r5[t][1] >= THRESH for t in ANTICIPATED)
    allnot = all(r5[t][2] < THRESH for t in ANTICIPATED)
    res["H5"] = "contradicted" if anyfast else ("supported" if allnot else "inconclusive")
    out.append(f"\n**H5 (upper CI bound < {THRESH} for pc0, pc1, pc2 => supported; any lower bound >= {THRESH} => contradicted): {res['H5']}**\n")
    out.append("\nRate of rejection within the budget, all non-null truths:\n\n| truth | " + " | ".join(pols) + " |\n|---|" + "---|" * len(pols))
    for t in ANTICIPATED + UNANTICIPATED + ("shift",):
        out.append(f"| {t} | " + " | ".join(f"{(np.array(cell[(t, p)]) <= N).mean():.3f}" for p in pols) + " |")
    out.append("\nMedian episodes-to-reject (N+1 = censored):\n\n| truth | " + " | ".join(pols) + " |\n|---|" + "---|" * len(pols))
    for t in ANTICIPATED + UNANTICIPATED:
        out.append(f"| {t} | " + " | ".join(f"{np.median(cell[(t, p)]):.0f}" for p in pols) + " |")
    out.append("\n## Computational cost (run-seconds per policy, summed)\n\n" + ", ".join(f"{p}: {sec[p]:.0f}" for p in pols))
    out.append("\n\n## Summary of decisions\n\n```json\n" + json.dumps(res, indent=1) + "\n```\n")
    open(a.out, "w").write("\n".join(out))
    json.dump(res, open(a.out.replace(".md", ".json"), "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
