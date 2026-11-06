"""Failure-boundary table from the stress runs (development families only).  usage: ool_stress_report.py out.md"""
import sys, os, pickle, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from eid.ool import evals, loop
cal = json.load(open("results/ool_dev/calibration_ns29000.json")); IO = {"sin", "rectsq", "leak", "bilin"}
lines = ["# Stress tests (development families sin, rectsq, leak, bilin, thresh; 6 instances each; namespace 32000)", "",
         "L1 = RMSE<=0.05, L2 = signature match; pooled over the four identifiable families (n=24 per cell, no CI: 24 instances); thresh = fraction claiming the null/null-equivalent explanation; L0 reject = fraction of identifiable instances on which calibrated criticism rejects L0.", "",
         "| condition | B | method | L1 | L2 | thresh null-claim | L0 reject |", "|---|---|---|---|---|---|---|"]
for cond in ("noise1", "noise2", "noise3", "nou2"):
    res = pickle.load(open(f"results/ool_dev/stress_{cond}_ns32000.pkl", "rb"))["res"]
    for B in (8, 12):
        for m in ("adapt_sweepB", "all_sweepB", "L0_sweepB", "oracle_struct"):
            l1, l2, nn, rj = [], [], [], []
            for r in res:
                rec = r["oracle"][B] if m == "oracle_struct" else r["agents"][m][B]
                ok = rec["rmse"] <= loop.TAU; desc = rec["desc"]
                if r["fam"] in IO: l1.append(ok); l2.append(evals.level2(r["fam"], desc))
                if r["fam"] == "thresh": nn.append(len(desc) == 0)
                if r["fam"] in IO and m == "L0_sweepB": rj.append(rec["s_in"] > cal["in"][str(B)])
            lines.append(f"| {cond} | {B} | {m} | {np.mean(l1):.2f} | {np.mean(l2):.2f} | {np.mean(nn):.2f} | {np.mean(rj):.2f} |" if rj else f"| {cond} | {B} | {m} | {np.mean(l1):.2f} | {np.mean(l2):.2f} | {np.mean(nn):.2f} | |")
open(sys.argv[1], "w").write("\n".join(lines)); print("\n".join(lines))
