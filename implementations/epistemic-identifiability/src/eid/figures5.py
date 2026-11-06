"""Phase 5 figures from the confirmatory data (run A). Usage: python -m eid.figures5 --out results/figures"""
from __future__ import annotations

import argparse
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from . import analyze_bayes1 as a1  # noqa: E402
from . import analyze_bayes2 as a2  # noqa: E402
from .metrics import bootstrap_ci  # noqa: E402

COL = {"random": "#0072B2", "eig2": "#009E73", "eig": "#D55E00", "no2": "#000000", "passive": "#999999", "sweep": "#CC79A7"}
STY = {"random": "-", "eig2": "-", "eig": "--", "no2": ":", "passive": ":", "sweep": "--"}
LAB = {"random": "random actions", "eig2": "two-step information gain", "eig": "one-step information gain", "no2": "never uses action 2", "passive": "training-like", "sweep": "fixed sweep"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/figures")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    d2 = a2.load("results/bayes2_confirm")
    steps = [25, 50, 100, 200]
    fig, ax = plt.subplots(1, 3, figsize=(12, 3.8), sharey=True)
    for j, regime in enumerate(("oracle", "learned", "bma")):
        for pol in ("random", "eig2", "eig", "no2", "passive", "sweep"):
            c = np.array([bootstrap_ci(a2.across_seeds(d2, regime, pol, k)["acc3"], n_boot=500) for k in range(4)])
            ax[j].plot(steps, c[:, 0], color=COL[pol], ls=STY[pol], lw=1.7, label=LAB[pol])
            ax[j].fill_between(steps, c[:, 1], c[:, 2], color=COL[pol], alpha=0.10, lw=0)
        ax[j].axhline(1 / 3, color="k", lw=0.5, ls="-.")
        ax[j].set_title({"oracle": "oracle likelihoods", "learned": "learned likelihoods", "bma": "model averaging over learners"}[regime], fontsize=10)
        ax[j].set_xscale("log")
        ax[j].set_xticks(steps)
        ax[j].set_xticklabels([str(s) for s in steps])
        ax[j].minorticks_off()
        ax[j].set_xlabel("interaction steps")
        ax[j].set_ylim(0.25, 1.0)
        ax[j].grid(alpha=0.25)
    ax[0].set_ylabel("3-class identification accuracy")
    h, l = ax[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=6, fontsize=8, frameon=False)
    fig.suptitle("Partially observed benchmark: accuracy against budget (12 held-out seeds; band = 95% bootstrap CI; dash-dot = chance)", fontsize=10)
    fig.tight_layout(rect=(0, 0.09, 1, 0.93))
    fig.savefig(os.path.join(a.out, "phase5_env2_accuracy_vs_budget.png"), dpi=160)

    d1 = a1.load("results/bayes1_confirm")
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    pols = ["passive", "wide", "sweep", "eig"]
    plab = {"passive": "training-like", "wide": "random wide", "sweep": "fixed sweep", "eig": "information gain"}
    width = 0.2
    for k, (key, title) in enumerate((("acc3", "3-class identification accuracy (step 40)"), ("ece", "expected calibration error (step 40)"))):
        for i, pol in enumerate(pols):
            vals = [bootstrap_ci(a1.across_seeds(d1, r, pol, 2)[key], n_boot=500) for r in ("oracle", "learned", "bma")]
            x = np.arange(3) + (i - 1.5) * width
            ax[k].bar(x, [v[0] for v in vals], width, yerr=[[v[0] - v[1] for v in vals], [v[2] - v[0] for v in vals]], color=["#999999", "#0072B2", "#CC79A7", "#D55E00"][i], capsize=2, label=plab[pol])
        ax[k].set_xticks(range(3))
        ax[k].set_xticklabels(["oracle", "learned", "model averaging"])
        ax[k].set_title(title, fontsize=10)
        ax[k].grid(axis="y", alpha=0.25)
    ax[0].axhline(1 / 3, color="k", lw=0.5, ls="-.")
    h, l = ax[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=4, fontsize=8, frameon=False)
    fig.suptitle("Fully observed environment: Bayesian observers (12 held-out seeds; 95% bootstrap CI)", fontsize=10)
    fig.tight_layout(rect=(0, 0.09, 1, 0.93))
    fig.savefig(os.path.join(a.out, "phase5_env1_regimes.png"), dpi=160)
    print("wrote figures")


if __name__ == "__main__":
    main()
