"""POST HOC equivalence tests on the frozen Phase 1-4 results (not pre-specified at the time).
Margins fixed here before running: |difference in AUROC (W vs controls)| < 0.10 for architecture / sample claims (the practical threshold used in Phase 4);
|AUROC(E0 vs E0split) - 0.5| < 0.05 for the negative control. Seed-paired TOST, Holm-adjusted within each family. Quality 3, wide, T = 10 and T = 50, active T = 10.
Usage: PYTHONPATH=src python scripts/phase4_equivalence_posthoc.py > results/phase4_equivalence_posthoc.md"""
import numpy as np

from eid.analyze_bayes1 import holm, tost_paired
from eid.metrics import bootstrap_ci
from eid.report import read

REF = "poc_v2"
CONDS = {"abl_qindep": "independent training sample", "abl_relu128": "ReLU theory", "abl_wrelu_qtanh": "W = ReLU, theory tanh", "abl_wrelu_qrelu": "W = ReLU, theory ReLU"}
CELLS = [("wide", 10), ("wide", 50), ("active", 10)]


def vec(rows, q, p, T, key):
    d = {int(r["seed"]): r[key] for r in rows if int(r["quality"]) == q and r["policy"] == p and int(r["T"]) == T}
    return np.array([d[s] for s in sorted(d)])


ref = read(f"results/{REF}/metrics.csv")
print("# Post hoc equivalence tests on frozen Phase 4 results\n")
print("Margins fixed before running: 0.10 (AUROC, architecture/sample claims); 0.05 (negative control around 0.5). Seed-paired TOST (n = 10), Holm-adjusted within each family. 'not established' does not mean 'different'.\n")
print("## Family A: AUROC (W vs controls) of each condition minus the baseline, quality 3\n")
print("| condition | cell | difference [95% CI] | TOST p | Holm p | equivalent within ±0.10 |\n|---|---|---|---|---|---|")
rowsA, ps = [], []
for c, desc in CONDS.items():
    rows = read(f"results/{c}/metrics.csv")
    for p, T in CELLS:
        d = vec(rows, 3, p, T, "auroc_W_vs_null") - vec(ref, 3, p, T, "auroc_W_vs_null")
        rowsA.append((desc, f"{p} T={T}", d)); ps.append(tost_paired(d, 0.10))
adj = holm(ps)
for (desc, cell, d), pa, p in zip(rowsA, adj, ps):
    m, lo, hi = bootstrap_ci(d)
    print(f"| {desc} | {cell} | {m:+.3f} [{lo:+.3f}, {hi:+.3f}] | {p:.4f} | {pa:.4f} | {'yes' if pa < 0.05 else 'not established'} |")
print("\n## Family B: negative control, AUROC(E0 vs E0split) - 0.5, all nine conditions, quality 3\n")
print("| condition | cell | deviation from 0.5 [95% CI] | TOST p | Holm p | equivalent within ±0.05 |\n|---|---|---|---|---|---|")
rowsB, ps = [], []
for c in [REF] + list(CONDS) + ["abl_poly3", "abl_qwide", "abl_analytic", "adaptive_tanh"]:
    rows = read(f"results/{c}/metrics.csv")
    for p, T in CELLS:
        d = vec(rows, 3, p, T, "auroc_null_vs_null") - 0.5
        rowsB.append((c, f"{p} T={T}", d)); ps.append(tost_paired(d, 0.05))
adj = holm(ps)
for (c, cell, d), pa, p in zip(rowsB, adj, ps):
    m, lo, hi = bootstrap_ci(d)
    print(f"| {c} | {cell} | {m:+.3f} [{lo:+.3f}, {hi:+.3f}] | {p:.4f} | {pa:.4f} | {'yes' if pa < 0.05 else 'not established'} |")
