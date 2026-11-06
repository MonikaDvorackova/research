"""EXPLORATORY summary of the stress tests for environment 1 (seeds 400-405; never combined with confirmatory seeds).
Usage: python -m eid.stress_summary --out results/stress_summary.md"""
from __future__ import annotations

import argparse
import os

import numpy as np

from .analyze_bayes1 import across_seeds, fmt, load

REF = ("bayes1_confirm", "baseline (confirmatory seeds; narrow-trained theories, W trained on 12,500, complete space, uniform prior)")


def row(data, regime, policy, ck, **kw):
    m = across_seeds(data, regime, policy, ck, **kw)
    return [fmt(m[k]) for k in ("acc3", "acc_h0", "acc_h1", "acc_h2", "h1v2_auroc", "ece")]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/stress_summary.md")
    ap.add_argument("--ck", type=int, default=2)
    ap.add_argument("--suffix", default="", help="directory suffix, e.g. _runB for the deterministic repeat")
    a = ap.parse_args()
    L = ["# Stress tests, environment 1 (EXPLORATORY)", "", f"Seeds 400-405 (n = 6) for stress runs; the baseline row uses the 12 confirmatory seeds and is shown for reference only. Step {[10, 20, 40, 80][a.ck]}. Mean over seeds [bootstrap 95% CI].", ""]
    heads = "| condition | regime | policy | acc (3-class) | acc H0 | acc H1 | acc H2 | H1 vs H2 AUROC | ECE |\n|---|---|---|---|---|---|---|---|---|"
    L += ["## Coverage and fidelity", "", heads]
    runs = [(REF[0], REF[1])] + [("bayes1_stress_cov", "observer theories trained over the probed range (a in [-3, 3])"),
                                 ("bayes1_stress_fid500", "low-fidelity world model (500 transitions)"), ("bayes1_stress_fid2500", "medium-fidelity world model (2,500 transitions)")]
    for d, desc in runs:
        path = os.path.join("results", d + a.suffix)
        if not os.path.exists(path):
            continue
        data = load(path)
        if not data:
            continue
        for regime in ("oracle", "learned", "bma"):
            for pol in ("passive", "wide", "eig"):
                if f"{regime}|full|uniform|E0|{pol}|post" in next(iter(data.values())):
                    L.append(f"| {desc} | {regime} | {pol} | " + " | ".join(row(data, regime, pol, a.ck)) + " |")
    path = os.path.join("results", "bayes1_stress_hyp" + a.suffix)
    data = load(path) if os.path.exists(path) else {}
    if data:
        L += ["", "## Incomplete hypothesis spaces and misleading priors (wide and eig policies)", "",
              "'no_h1': no learned-world-model class; 'no_h2': no alternative-mechanism class; 'only_ood' / 'only_alt': the alternative class contains one deviation shape only. Class priors: uniform; mislead_h0 = (0.98, 0.01, 0.01); mislead_h2 = (0.01, 0.01, 0.98). Accuracy for a class that is absent from the hypothesis space is 0 by construction (those truths cannot be classified correctly) and is included in the 3-class average, so compare the per-class columns, not acc (3-class), across rows.", "",
              "| complete | prior | regime | policy | acc (3-class) | acc H0 | acc H1 | acc H2 | H1 vs H2 AUROC | ECE |", "|---|---|---|---|---|---|---|---|---|---|"]
        for comp in ("no_h1", "no_h2", "only_ood", "only_alt"):
            for pn in ("uniform", "mislead_h0", "mislead_h2"):
                for regime in ("oracle", "learned", "bma"):
                    for pol in ("wide", "eig"):
                        try:
                            m = across_seeds(data, regime, pol, a.ck, complete=comp, pname=pn)
                        except KeyError:
                            continue
                        L.append(f"| {comp} | {pn} | {regime} | {pol} | " + " | ".join(fmt(m[k]) for k in ("acc3", "acc_h0", "acc_h1", "acc_h2", "h1v2_auroc", "ece")) + " |")
    open(a.out, "w").write("\n".join(L) + "\n")
    print("\n".join(L[:30]))


if __name__ == "__main__":
    main()
