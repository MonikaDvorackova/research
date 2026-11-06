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
    ("abl_qindep", "independently trained theory (fresh E0 sample), same architecture"),
    ("abl_wrelu_qtanh", "W = ReLU-128x3, theory = tanh-64 (architectures differ)"),
    ("abl_wrelu_qrelu", "W = ReLU-128x3, theory = ReLU-128x3 (architectures shared)"),
    ("adaptive_tanh", "adaptive observer: fine-tunes the tanh theory on its own interaction before testing"),
]
CELLS = [("passive", 50), ("wide", 10), ("wide", 50), ("active", 10), ("active", 50)]
METRICS = [("fpr_null", "FPR (alpha=0.05)"), ("fnr_W", "FNR on W (1 - TPR)"), ("tpr_W", "TPR on W"), ("bal_acc", "balanced accuracy (TPR on W and 1 - FPR)"),
           ("auroc_W_vs_null", "AUROC W vs controls"), ("ece", "ECE (Platt-scaled)"), ("brier", "Brier score (0.25 = uninformative)"), ("oracle_auroc", "oracle AUROC")]


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
            for r in rows:
                r["fnr_W"] = 1 - r["tpr_W"]
                r["bal_acc"] = 0.5 * (r["tpr_W"] + 1 - r["fpr_null"])
            lines.append(f"| {desc} | " + " | ".join(cell(rows, a.quality, p, T, key) for p, T in CELLS) + " |")
        lines.append("")
    open(a.out, "w").write("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
