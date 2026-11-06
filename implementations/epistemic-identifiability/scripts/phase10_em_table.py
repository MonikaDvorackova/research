import json, sys, collections
import numpy as np
from eid.phase9_audit import cp_upper
out = sys.argv[1]
rows = [json.loads(l) for l in open(out + "/em_runs.jsonl")]
gap = [r for r in rows if r["kind"] == "gap"]; ep = [r for r in rows if r["kind"] == "eproc"]
L = []
def w(s=""): print(s); L.append(s)
w("## E1. Optimiser gap: best-of-R EM against the likelihood at the TRUE parameters (40 independent small HMMs, S in {2,3}, 800 training episodes)\n")
w("| restarts R | iteration budget | tolerance | fraction with ll below the true-parameter ll by > 0.5 nats (invalid denominator) | median shortfall vs true (nats) | 90th pct shortfall | median shortfall vs 20x1000 reference | median seconds |\n|---|---|---|---|---|---|---|---|")
for key in sorted({(r["R"], r["B"], r["tol"]) for r in gap}):
    G = [r for r in gap if (r["R"], r["B"], r["tol"]) == key]
    st = np.array([r["short_true"] for r in G]); sr = np.array([r["short_ref"] for r in G])
    w(f"| {key[0]} | {key[1]} | {key[2]:g} | {np.mean(st > 0.5):.2f} ({int((st>0.5).sum())}/{len(G)}) | {np.median(st):.1f} | {np.percentile(st,90):.1f} | {np.median(sr):.1f} | {np.median([r['secs'] for r in G]):.2f} |")
w("\n## E2. Type-I of an e-process with an EM denominator, truth in the class, S known (40 structures x 3 data sets; blocks 100,100,200,400 episodes; checkpoints after every block; threshold 1/alpha = 20)\n")
w("| denominator | rejections / runs | structures with >= 1 | median optimisation shortfall at the last checkpoint (nats) | median numerator deficit  log q - log p_true (nats) | max (shortfall + numerator gap) |\n|---|---|---|---|---|---|")
for name in ["true", "sym(R5,B300)", "best(R10,B600)", "asym(R1,B60)", "asym(R1,B20)"]:
    k = sum(r["rej"][name] for r in ep); n = len(ep)
    byS = collections.defaultdict(list)
    for r in ep: byS[r["idx"]].append(r["rej"][name])
    sh = np.array([r["final"][name][0] for r in ep]); nd = np.array([r["final"][name][1] for r in ep])
    w(f"| {name} | {k}/{n} (UB {cp_upper(k, n):.3f}) | {sum(any(v) for v in byS.values())}/{len(byS)} | {np.median(sh):.1f} | {np.median(nd):.1f} | {np.max(sh + nd):.1f} |")
w("\nlog E = (log q - log p_true) + (log p_true - log p_den) = (numerator deficit, <= 0 on average: the price of learning) + (optimisation shortfall of the denominator). Rejection requires the shortfall to exceed the numerator deficit by ln 20 = 3.0 nats.")
w("\n## E3. Same denominators with a GOOD fixed alternative (true parameters mixed 10 % with random rows; deficit ll_alt - ll_true small): type-I under the correctly specified null\n")
w("| denominator | rejections / runs | structures with >= 1 | median optimisation shortfall (nats) | median alternative deficit (nats) | share of runs with shortfall > deficit + ln 20 |\n|---|---|---|---|---|---|")
for name in ["true", "sym(R5,B300)", "best(R10,B600)", "asym(R1,B60)", "asym(R1,B20)"]:
    k = sum(r["rej_alt"][name] for r in ep); n = len(ep)
    byS = collections.defaultdict(list)
    for r in ep: byS[r["idx"]].append(r["rej_alt"][name])
    sh = np.array([r["final_alt"][name][0] for r in ep]); nd = np.array([r["final_alt"][name][1] for r in ep])
    w(f"| {name} | {k}/{n} (LB {__import__('eid.phase9_audit', fromlist=['cp_lower']).cp_lower(k, n):.3f}) | {sum(any(v) for v in byS.values())}/{len(byS)} | {np.median(sh):.1f} | {np.median(nd):.1f} | {np.mean(sh > -nd + np.log(20)):.2f} |")
open(out + "/em_summary.md", "w").write("\n".join(L) + "\n")
