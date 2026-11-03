"""Pre-specified confirmatory analysis for the partially observed benchmark (notes/preregistration-phase5.md, Part 2).
Usage: python -m eid.confirm_bayes2 --dir results/bayes2_confirm --out results/bayes2_confirm/confirmatory.md [--dry-run]
Checkpoint indices: 0 = step 25, 1 = step 50, 2 = step 100, 3 = step 200."""
from __future__ import annotations

import argparse

import numpy as np
from scipy import stats

from .analyze_bayes1 import holm, tost_paired
from .analyze_bayes2 import across_seeds, load
from .metrics import bootstrap_ci

CK100, CK200, CK25 = 2, 3, 0


def acc_scenario(data, regime, policy, scenario, cls, ck):
    return np.array([float(np.mean(a[f"{regime}|full|uniform|{scenario}|{policy}|post"][:, ck].argmax(1) == cls)) for a in data.values()])


def negctl(data, regime, policy="random", ck=CK100):
    a = np.array([s[f"{regime}|full|uniform|E0|{policy}|post"][:, ck, 0].mean() for s in data.values()])
    b = np.array([s[f"{regime}|full|uniform|E0split|{policy}|post"][:, ck, 0].mean() for s in data.values()])
    return a - b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    data = load(a.dir)
    M = lambda r, p, k, ck: across_seeds(data, r, p, ck)[k]  # noqa: E731
    # (id, description, per-seed statistic, threshold, direction) ; 'ge': claim stat >= thr ; 'lt': claim stat < thr (upper bound)
    claims = [
        ("G1", "oracle acc3, eig2: step 200 minus step 25 >= 0.10 (finite-sample, not fundamental)", M("oracle", "eig2", "acc3", CK200) - M("oracle", "eig2", "acc3", CK25), 0.10, "ge"),
        ("G2", "acc3(oracle, random) - acc3(learned, random) at step 100 >= 0.10 (misspecification-limited)", M("oracle", "random", "acc3", CK100) - M("learned", "random", "acc3", CK100), 0.10, "ge"),
        ("G3", "ECE(learned, random) - ECE(oracle, random) at step 100 >= 0.10", M("learned", "random", "ece", CK100) - M("oracle", "random", "ece", CK100), 0.10, "ge"),
        ("G4", "acc3(oracle, eig2) - acc3(oracle, random) at step 100 >= 0.05 (active design helps under correct specification)", M("oracle", "eig2", "acc3", CK100) - M("oracle", "random", "acc3", CK100), 0.05, "ge"),
        ("G5", "acc3(learned, eig2) - acc3(learned, random) at step 100 < 0.05 (no practically significant benefit under learned likelihoods)", M("learned", "eig2", "acc3", CK100) - M("learned", "random", "acc3", CK100), 0.05, "lt"),
        ("G6", "H1-vs-H2 AUROC (learned, random) at step 100 < 0.65 (learned observer cannot separate learned from non-learned mechanisms)", M("learned", "random", "h1v2_auroc", CK100), 0.65, "lt"),
        ("G7", "accuracy on the transition-perturbed truth: random minus no-action-2, oracle, step 200 >= 0.20 (equivalence relative to an intervention class)", acc_scenario(data, "oracle", "random", "AltOOD", 2, CK200) - acc_scenario(data, "oracle", "no2", "AltOOD", 2, CK200), 0.20, "ge"),
        ("S1", "ECE(oracle, random) at step 100 < 0.10 (oracle uncertainty is calibrated; sanity gate)", M("oracle", "random", "ece", CK100), 0.10, "lt"),
    ]
    rows, pw = [], []
    for cid, desc, v, thr, kind in claims:
        m, lo, hi = bootstrap_ci(v, n_boot=5000)
        d = v - thr
        p = float(stats.wilcoxon(d, alternative="greater" if kind == "ge" else "less").pvalue) if np.any(d != 0) else 1.0
        rows.append((cid, desc, m, lo, hi, thr, kind, p))
        pw.append(p)
    adj = holm(pw)
    equiv = [("E1a", "negative control, mass on H0 under reference vs bisimilar copy, oracle, random, step 100", negctl(data, "oracle"), 0.05),
             ("E1b", "same, learned", negctl(data, "learned"), 0.05), ("E1c", "same, bma", negctl(data, "bma"), 0.05)]
    erows, ep = [], []
    for cid, desc, d, mg in equiv:
        m, lo, hi = bootstrap_ci(d, n_boot=5000)
        p = tost_paired(d, mg)
        erows.append((cid, desc, m, lo, hi, mg, p))
        ep.append(p)
    eadj = holm(ep)
    L = [f"# Confirmatory analysis, Bayesian observer, partially observed benchmark ({'DRY RUN - NOT CONFIRMATORY' if a.dry_run else 'confirmatory'})", "",
         f"Directory: {a.dir}; seeds {sorted(data)} (n = {len(data)}); unit of analysis: seed. Rules fixed in notes/preregistration-phase5.md, Part 2.", "",
         "## Directional claims (supported iff the bootstrap 95% CI bound lies on the claimed side of the threshold AND the Holm-adjusted one-sided Wilcoxon p < 0.05)", "",
         "| id | claim | mean [95% CI] | threshold | raw p | Holm p | supported |", "|---|---|---|---|---|---|---|"]
    for (cid, desc, m, lo, hi, thr, kind, p), pa in zip(rows, adj):
        sup = ((lo > thr) if kind == "ge" else (hi < thr)) and pa < 0.05
        L.append(f"| {cid} | {desc} | {m:.3f} [{lo:.3f}, {hi:.3f}] | {'>=' if kind == 'ge' else '<'} {thr} | {p:.4f} | {pa:.4f} | **{'yes' if sup else 'not established'}** |")
    L += ["", "## Equivalence claims (supported iff Holm-adjusted TOST p < 0.05; otherwise 'not established', never 'no effect')", "", "| id | claim | mean difference [95% CI] | margin | TOST p | Holm p | supported |", "|---|---|---|---|---|---|---|"]
    for (cid, desc, m, lo, hi, mg, p), pa in zip(erows, eadj):
        L.append(f"| {cid} | {desc} | {m:+.3f} [{lo:+.3f}, {hi:+.3f}] | ±{mg} | {p:.4f} | {pa:.4f} | **{'yes' if pa < 0.05 else 'not established'}** |")
    open(a.out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
