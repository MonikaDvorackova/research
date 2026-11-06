"""Figures for the cross-condition comparison. Usage: python -m eid.figures --out results/figures"""
from __future__ import annotations

import argparse
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from .metrics import bootstrap_ci  # noqa: E402
from .report import read  # noqa: E402

# Okabe-Ito palette (colour-blind safe); direct labels at line ends instead of a legend
SERIES = [  # (directory, label, colour, linestyle)
    ("poc_v2", "baseline: fixed tanh theory, narrow training", "#000000", "-"),
    ("abl_qindep", "independent E0 sample (same architecture)", "#999999", "-"),
    ("abl_relu128", "ReLU theory", "#D55E00", "-"),
    ("abl_wrelu_qtanh", "W = ReLU, theory = tanh", "#56B4E9", "--"),
    ("abl_wrelu_qrelu", "W = ReLU, theory = ReLU", "#CC9900", "--"),
    ("abl_poly3", "polynomial theory", "#CC79A7", "-"),
    ("abl_qwide", "theory trained over probed range", "#0072B2", "-"),
    ("abl_analytic", "analytic true law", "#009E73", "-"),
    ("adaptive_tanh", "adaptive observer (fine-tunes on interaction)", "#E69F00", ":"),
]
METRICS = [("fpr_null", "false-positive rate (alpha = 0.05)", (0, 1)), ("tpr_W", "true-positive rate on W", (0, 1)),
           ("auroc_W_vs_null", "AUROC, W vs controls", (0, 1))]


def curve(rows, q, p, key):
    Ts = sorted({int(r["T"]) for r in rows})
    out = []
    for T in Ts:
        v = [r[key] for r in rows if int(r["quality"]) == q and r["policy"] == p and int(r["T"]) == T]
        out.append(bootstrap_ci(v, n_boot=500))
    return Ts, np.array(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/figures")
    ap.add_argument("--quality", type=int, default=3)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    data = {n: read(os.path.join("results", n, "metrics.csv")) for n, _, _, _ in SERIES if os.path.exists(os.path.join("results", n, "metrics.csv"))}
    policies = ("passive", "wide", "active")
    fig, ax = plt.subplots(len(METRICS), len(policies), figsize=(11, 8.2), sharex=True)
    for i, (key, title, ylim) in enumerate(METRICS):
        for j, p in enumerate(policies):
            for n, label, col, ls in SERIES:
                if n not in data:
                    continue
                Ts, c = curve(data[n], a.quality, p, key)
                ax[i, j].plot(Ts, c[:, 0], color=col, lw=1.6, ls=ls, label=label)
                ax[i, j].fill_between(Ts, c[:, 1], c[:, 2], color=col, alpha=0.10, lw=0)
            ax[i, j].set_ylim(*ylim)
            ax[i, j].set_xscale("log")
            ax[i, j].set_xticks([2, 5, 10, 20, 50])
            ax[i, j].set_xticklabels(["2", "5", "10", "20", "50"])
            ax[i, j].minorticks_off()
            ax[i, j].grid(alpha=0.25)
            if key == "fpr_null":
                ax[i, j].axhline(0.05, color="k", lw=0.6, ls=":")
            if key == "auroc_W_vs_null":
                ax[i, j].axhline(0.5, color="k", lw=0.6, ls=":")
            if i == 0:
                ax[i, j].set_title(f"{p} interventions")
            if j == 0:
                ax[i, j].set_ylabel(title, fontsize=9)
            if i == len(METRICS) - 1:
                ax[i, j].set_xlabel("interaction horizon T")
    fig.suptitle(f"Detection by observer type (world model trained on 12,500 transitions; mean over 10 seeds, 95% bootstrap CI)", fontsize=10)
    h, l = ax[0, 0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=3, fontsize=8, frameon=False)
    fig.tight_layout(rect=(0, 0.09, 1, 0.97))
    fig.savefig(os.path.join(a.out, "observer_comparison.png"), dpi=160)
    print("wrote", os.path.join(a.out, "observer_comparison.png"))


if __name__ == "__main__":
    main()
