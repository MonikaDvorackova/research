"""Compare conditions (baseline and ablations) on key metrics. Usage: python -m eid.compare --out results/comparison.md"""
from __future__ import annotations

import argparse
import os

from .metrics import bootstrap_ci
from .report import read

CONDITIONS = [
    ("poc_v2", "baseline: tanh-64 ensemble theory, trained on a in [-1,1]"),
    ("abl_relu128", "A1: ReLU-128x3 ensemble theory"),
    ("abl_poly3", "A2: cubic-polynomial theory (different model class)"),
    ("abl_qwide", "C: tanh-64 theory trained on a in [-3,3] (coverage)"),
    ("abl_analytic", "B: analytic true-law theory; actions chosen by learned-ensemble disagreement"),
]
CELLS = [("passive", 50), ("wide", 10), ("wide", 50), ("active", 10), ("active", 50)]
METRICS = [("fpr_null", "FPR (alpha=0.05)"), ("tpr_W", "TPR on W"), ("auroc_W_vs_null", "AUROC W vs controls"),
           ("oracle_auroc", "oracle AUROC")]


def cell(rows, quality, policy, T, key):
    v = [r[key] for r in rows if int(r["quality"]) == quality and r["policy"] == policy and int(r["T"]) == T]
    m, lo, hi = bootstrap_ci(v)
    return f"{m:.3f} [{lo:.3f}, {hi:.3f}]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="results")
    ap.add_argument("--out", default="results/comparison.md")
    ap.add_argument("--quality", type=int, default=3)
    a = ap.parse_args()
    lines = [f"# Cross-condition comparison (quality {a.quality}, 12,500 training transitions for W; mean over seeds with bootstrap 95% CI)", ""]
    for key, title in METRICS:
        lines += [f"## {title}", "", "| condition | " + " | ".join(f"{p} T={T}" for p, T in CELLS) + " |", "|---|" + "---|" * len(CELLS)]
        for d, desc in CONDITIONS:
            path = os.path.join(a.root, d, "metrics.csv")
            if not os.path.exists(path):
                continue
            rows = read(path)
            lines.append(f"| {desc} | " + " | ".join(cell(rows, a.quality, p, T, key) for p, T in CELLS) + " |")
        lines.append("")
    open(a.out, "w").write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
