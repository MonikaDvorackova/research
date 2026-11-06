"""Seed-paired statistical comparison of observer conditions, separating statistical from practical significance.

Usage: python -m eid.stats --out results/stats.md
Practical-significance thresholds were fixed before looking at the new conditions: |difference| >= 0.10 for AUROC and
>= 0.05 (absolute) for rates, accuracies and calibration error. Tests are Wilcoxon signed-rank on seed-paired values
(n = number of seeds); p-values are Holm-adjusted within each (metric) family. "Paired by seed index": for conditions that
change W's architecture the world models differ, so pairing is by seed index only.
"""
from __future__ import annotations

import argparse
import os

import numpy as np
from scipy.stats import wilcoxon

from .metrics import bootstrap_ci
from .report import read

REFERENCE = "poc_v2"
CONDITIONS = [
    ("abl_qindep", "independently trained theory (fresh E0 sample)"),
    ("abl_relu128", "ReLU theory"),
    ("abl_poly3", "polynomial theory"),
    ("abl_qwide", "theory trained over probed range"),
    ("abl_analytic", "analytic true-law theory"),
    ("abl_wrelu_qtanh", "W=ReLU, theory=tanh (architectures differ)"),
    ("abl_wrelu_qrelu", "W=ReLU, theory=ReLU (architectures shared)"),
    ("adaptive_tanh", "adaptive observer (fine-tunes on interaction)"),
]
CELLS = [("passive", 50), ("wide", 10), ("active", 10)]
THRESH = {"auroc_W_vs_null": 0.10, "fpr_null": 0.05, "tpr_W": 0.05, "bal_acc": 0.05}
LABEL = {"auroc_W_vs_null": "AUROC W vs controls", "fpr_null": "FPR (alpha=0.05)", "tpr_W": "TPR on W", "bal_acc": "balanced accuracy"}


def load(name):
    path = os.path.join("results", name, "metrics.csv")
    if not os.path.exists(path):
        return None
    rows = read(path)
    for r in rows:
        r["bal_acc"] = 0.5 * (r["tpr_W"] + 1 - r["fpr_null"])
    return rows


def vec(rows, q, p, T, key):
    d = {int(r["seed"]): r[key] for r in rows if int(r["quality"]) == q and r["policy"] == p and int(r["T"]) == T}
    return np.array([d[s] for s in sorted(d)])


def holm(pvals):
    order = np.argsort(pvals)
    m = len(pvals)
    adj = np.empty(m)
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, (m - rank) * pvals[i])
        adj[i] = min(1.0, run)
    return adj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/stats.md")
    ap.add_argument("--quality", type=int, default=3)
    a = ap.parse_args()
    ref = load(REFERENCE)
    lines = [f"# Seed-paired comparison against the baseline fixed observer (quality {a.quality})", "",
             "Difference = condition minus baseline, mean over seeds [bootstrap 95% CI]. Practical threshold: 0.10 for AUROC, 0.05 for rates.",
             "Holm-adjusted Wilcoxon p-values within each metric family (all conditions x cells). With 10 seeds the smallest attainable two-sided p is 0.002.", ""]
    for key in ("fpr_null", "tpr_W", "auroc_W_vs_null", "bal_acc"):
        entries = []
        for name, desc in CONDITIONS:
            rows = load(name)
            if rows is None:
                continue
            for p, T in CELLS:
                x, y = vec(rows, a.quality, p, T, key), vec(ref, a.quality, p, T, key)
                d = x - y
                try:
                    pv = float(wilcoxon(d).pvalue) if np.any(d != 0) else 1.0
                except ValueError:
                    pv = 1.0
                m, lo, hi = bootstrap_ci(d)
                entries.append((desc, f"{p} T={T}", m, lo, hi, pv))
        if not entries:
            continue
        adj = holm(np.array([e[5] for e in entries]))
        lines += [f"## {LABEL[key]}", "", "| condition | cell | difference | Holm p | statistically significant (p<0.05) | practically significant | reading |", "|---|---|---|---|---|---|---|"]
        for (desc, cell, m, lo, hi, pv), pa in zip(entries, adj):
            sig, prac = pa < 0.05, abs(m) >= THRESH[key]
            reading = ("both" if sig and prac else "statistical only (small effect)" if sig else "practical only (not established by 10 seeds)" if prac else "neither")
            lines.append(f"| {desc} | {cell} | {m:+.3f} [{lo:+.3f}, {hi:+.3f}] | {pa:.3f} | {'yes' if sig else 'no'} | {'yes' if prac else 'no'} | {reading} |")
        lines.append("")
    open(a.out, "w").write("\n".join(lines))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
