import json, sys, numpy as np
r = json.load(open(sys.argv[1])); rng = np.random.default_rng(0)
ci = lambda v: np.percentile([np.mean(np.asarray(v)[rng.integers(0, len(v), len(v))]) for _ in range(600)], [2.5, 97.5])
methods = list(r["sets"]["known"].keys())
for B in ("2", "4", "8"):
    print(f"\n=== budget B={B} episodes: mean normalised descriptor error (95% bootstrap CI over instances); 0 = exact")
    print(f"{'method':18s} {'known F1-F3':>22s} {'H1 gate':>22s} {'H2 backlash':>22s}")
    for m in methods:
        cells = []
        for s in ("known", "gate", "backlash"):
            v = r["sets"][s][m][B]["err_all"]; lo, hi = ci(v); cells.append(f"{np.mean(v):6.2f} [{lo:5.2f},{hi:5.2f}]")
        print(f"{m:18s} " + " ".join(f"{c:>22s}" for c in cells))
print("\nper-descriptor mean error at B=4 (nl, asym, lat, hyst):")
for m in methods:
    print(f"{m:18s} " + " | ".join(s[:4] + ":" + " ".join(f"{x:5.2f}" for x in r['sets'][s][m]['4']['err_desc']) for s in ("known", "gate", "backlash")))
print("\nepistemic flags (AUROC: held-out vs known):")
for k, v in r["epistemic_flags"].items(): print(f"  {k:22s} gate {v['auroc_gate_vs_known']:.2f}  backlash {v['auroc_backlash_vs_known']:.2f}")
