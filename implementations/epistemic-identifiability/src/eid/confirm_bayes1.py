"""Pre-specified confirmatory analysis for the Bayesian observer on environment 1 (see notes/preregistration-phase5.md).
Usage: python -m eid.confirm_bayes1 --dir results/bayes1_confirm --out results/bayes1_confirm/confirmatory.md [--dry-run]
The decision rules are fixed in this file before confirmatory data exist; --dry-run labels output as not confirmatory."""
from __future__ import annotations

import argparse

import numpy as np
from scipy import stats

from .analyze_bayes1 import across_seeds, holm, load, tost_paired
from .metrics import bootstrap_ci

CK = 2   # step 40


def pairs_from_seeds(data):
    return {s: a for s, a in data.items()}


def seed_values(data, regime, policy, key):
    return across_seeds(data, regime, policy, CK)[key]


def negctl(data, regime, policy="wide"):
    a = np.array([s[f"{regime}|full|uniform|E0|{policy}|post"][:, CK, 0].mean() for s in data.values()])
    b = np.array([s[f"{regime}|full|uniform|E0split|{policy}|post"][:, CK, 0].mean() for s in data.values()])
    return a - b


def lower_ci(v):
    return bootstrap_ci(v, n_boot=5000)[1]


def upper_ci(v):
    return bootstrap_ci(v, n_boot=5000)[2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    data = load(a.dir)
    n = len(data)
    V = lambda r, p, k: seed_values(data, r, p, k)  # noqa: E731
    # directional claims: (id, description, per-seed values of the statistic, threshold, kind)
    directional = [
        ("D1", "acc3(oracle, wide) - acc3(learned, wide) >= 0.10", V("oracle", "wide", "acc3") - V("learned", "wide", "acc3"), 0.10),
        ("D2", "acc3(oracle, wide) - acc3(bma, wide) >= 0.10", V("oracle", "wide", "acc3") - V("bma", "wide", "acc3"), 0.10),
        ("D3", "ECE(learned, wide) - ECE(oracle, wide) >= 0.10", V("learned", "wide", "ece") - V("oracle", "wide", "ece"), 0.10),
        ("D4", "ECE(bma, wide) - ECE(oracle, wide) >= 0.10", V("bma", "wide", "ece") - V("oracle", "wide", "ece"), 0.10),
        ("D5", "acc3(learned, wide) - acc3(learned, passive) >= 0.10", V("learned", "wide", "acc3") - V("learned", "passive", "acc3"), 0.10),
        ("D6", "H1-vs-H2 balanced accuracy (learned, wide) >= 0.80", V("learned", "wide", "h1v2_bal_acc") - 0.80, 0.0),
        ("D7", "false-identification rate (learned, wide) >= 0.20", V("learned", "wide", "false_id") - 0.20, 0.0),
        ("S1", "acc3(oracle, wide) >= 0.95 (sanity gate)", V("oracle", "wide", "acc3") - 0.95, 0.0),
    ]
    rows, pw = [], []
    for cid, desc, v, thr in directional:
        m, lo, hi = bootstrap_ci(v, n_boot=5000)
        # one-sided exact Wilcoxon signed-rank against the threshold
        d = v - thr
        p = float(stats.wilcoxon(d, alternative="greater").pvalue) if np.any(d != 0) else 1.0
        rows.append([cid, desc, m, lo, hi, p])
        pw.append(p)
    adj = holm(pw)
    equiv = [
        ("E1", "|acc3(eig) - acc3(wide)| < 0.05, learned regime", V("learned", "eig", "acc3") - V("learned", "wide", "acc3"), 0.05),
        ("E2", "|acc3(eig) - acc3(wide)| < 0.05, bma regime", V("bma", "eig", "acc3") - V("bma", "wide", "acc3"), 0.05),
        ("E3a", "negative control E0 vs E0split, mass on H0, oracle, wide", negctl(data, "oracle"), 0.05),
        ("E3b", "negative control E0 vs E0split, mass on H0, learned, wide", negctl(data, "learned"), 0.05),
        ("E3c", "negative control E0 vs E0split, mass on H0, bma, wide", negctl(data, "bma"), 0.05),
    ]
    erows, ep = [], []
    for cid, desc, d, margin in equiv:
        m, lo, hi = bootstrap_ci(d, n_boot=5000)
        p = tost_paired(d, margin)
        erows.append([cid, desc, m, lo, hi, margin, p])
        ep.append(p)
    eadj = holm(ep)
    L = [f"# Confirmatory analysis, Bayesian observer, environment 1 ({'DRY RUN ON DEVELOPMENT DATA - NOT CONFIRMATORY' if a.dry_run else 'confirmatory'})", "",
         f"Directory: {a.dir}; seeds: {sorted(data)} (n = {n}); checkpoint: step 40; unit of analysis: seed. Rules fixed in notes/preregistration-phase5.md.", "",
         "## Directional claims (supported iff the bootstrap 95% CI lower bound of the seed-level statistic exceeds the threshold AND the Holm-adjusted one-sided Wilcoxon p < 0.05)", "",
         "| id | claim | mean [95% CI] | raw p | Holm p | supported |", "|---|---|---|---|---|---|"]
    for (cid, desc, m, lo, hi, p), pa, (_, _, v, thr) in zip(rows, adj, directional):
        sup = (lo > thr) and pa < 0.05
        thr_text = f" (threshold {thr:.2f})" if thr else " (threshold 0 on the shifted statistic)"
        L.append(f"| {cid} | {desc} | {m:.3f} [{lo:.3f}, {hi:.3f}]{thr_text} | {p:.4f} | {pa:.4f} | **{'yes' if sup else 'not established'}** |")
    L += ["", "## Equivalence claims (supported iff Holm-adjusted TOST p < 0.05 at the stated margin; otherwise 'not established', never 'no effect')", "",
          "| id | claim | mean difference [95% CI] | margin | TOST p | Holm p | supported |", "|---|---|---|---|---|---|---|"]
    for (cid, desc, m, lo, hi, margin, p), pa in zip(erows, eadj):
        L.append(f"| {cid} | {desc} | {m:+.3f} [{lo:+.3f}, {hi:+.3f}] | ±{margin} | {p:.4f} | {pa:.4f} | **{'yes' if pa < 0.05 else 'not established'}** |")
    L.append("")
    open(a.out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
