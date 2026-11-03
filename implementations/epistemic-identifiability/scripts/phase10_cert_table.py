"""Tabulate the certified-procedure development run (cluster-aware where relevant)."""
import json, sys, collections
import numpy as np
from eid.phase9_audit import cp_upper, cp_lower
rows = [json.loads(l) for l in open(sys.argv[1] + "/certified_runs.jsonl")]
L = []
def w(s=""): print(s); L.append(s)
# coverage
cov = [r for r in rows if r["kind"] == "cov"]
w("## A. Confidence-set coverage\n")
k = sum(r["miss"] for r in cov)
w(f"LR confidence set (delta = 0.05), time-uniform over 200 training checkpoints, 60 independent Markov structures x 5 training streams (5000 episodes, uniform policy): true kernel excluded at some checkpoint in **{k}/{len(cov)}** streams (guarantee: <= 5 %; one-sided CP upper bound {cp_upper(k, len(cov)):.3f}).\n")
cp = [r for r in rows if r["kind"] == "cpbox"]
w(f"Adversarial optional stopping (Bernoulli(1/2), 2000 observations, check every n): fixed-n Clopper-Pearson interval (95 %) excludes the truth at SOME n in **{sum(r['cp_miss'] for r in cp)}/{len(cp)}** runs; the LR confidence sequence (delta = 0.05) in **{sum(r['lr_miss'] for r in cp)}/{len(cp)}**.\n")
# type-I
nl = [r for r in rows if r["kind"] == "null"]
w("## B. Type-I under the intended null (kernel unchanged), 60 independent structures x 30 runs per condition (1500 test episodes)\n")
w("| training policy | training episodes | certified: rejections/runs | structures with >= 1 | oracle (true kernel known) | frozen point null (simple null 'kernel = estimate') |\n|---|---|---|---|---|---|")
for tp in ("narrow", "uniform"):
    for ntr in (1000, 10000):
        R = [r for r in nl if r["train"] == tp and r["ntr"] == ntr]
        f = lambda key: sum(r[key] is not None for r in R)
        s = collections.defaultdict(list)
        for r in R: s[r["idx"]].append(r["cert"] is not None)
        w(f"| {tp} | {ntr} | {f('cert')}/{len(R)} (UB {cp_upper(f('cert'), len(R)):.4f}) | {sum(any(v) for v in s.values())}/{len(s)} | {f('oracle')}/{len(R)} | {f('frozen')}/{len(R)} |")
# power and price
pw = [r for r in rows if r["kind"] == "power"]
w("\n## C. Detection after a change in action-2 rows (post-change stream of 3000 episodes), delay in episodes (censored at 3000), median over structures; price = exponent ratio\n")
w("| training policy | training episodes | oracle detected | certified detected | frozen detected | median delay oracle | median delay certified | median certified/oracle delay | median predicted exponent ratio (oracle/certified) |\n|---|---|---|---|---|---|---|---|---|")
for tp in ("narrow", "uniform"):
    for ntr in (1000, 10000):
        R = [r for r in pw if r["train"] == tp and r["ntr"] == ntr]
        dl = lambda key: np.array([r[key] if r[key] is not None else 3001 for r in R], float)
        det = lambda key: sum(r[key] is not None for r in R)
        per = collections.defaultdict(list)
        for r in R: per[r["idx"]].append((dl("oracle")[R.index(r)], dl("cert")[R.index(r)], r["lam_o"] / max(r["lam_c"], 1e-12)))
        med_ratio = np.median([np.median([c / o for o, c, _ in v]) for v in per.values()])
        pred = np.median([np.median([x for _, _, x in v]) for v in per.values()])
        w(f"| {tp} | {ntr} | {det('oracle')}/{len(R)} | {det('cert')}/{len(R)} | {det('frozen')}/{len(R)} | {np.median(dl('oracle')):.0f} | {np.median(dl('cert')):.0f} | {med_ratio:.2f} | {pred:.2f} |")
# correlation of prediction with observation across structures (uniform, 10000)
R = [r for r in pw if r["train"] == "uniform" and r["ntr"] == 10000]
obs = np.array([ (r["cert"] or 3001) / (r["oracle"] or 3001) for r in R]); pr = np.array([r["lam_o"] / max(r["lam_c"], 1e-12) for r in R])
if len(R) > 3: w(f"\nSpearman correlation between predicted exponent ratio and observed delay ratio (uniform training, 10000 episodes; {len(R)} runs): {__import__('scipy.stats', fromlist=['spearmanr']).spearmanr(pr, obs)[0]:.2f}")
# adversarial
ad = [r for r in rows if r["kind"] == "adv"]
w(f"\n## D. Adversarial adaptive test policy (chooses contexts to maximise the numerator's advantage), 30 structures x 10 runs, alpha = delta = 0.05: rejections **{sum(r['rej'] is not None for r in ad)}/{len(ad)}** (guarantee <= 0.10)")
open(sys.argv[1] + "/certified_summary.md", "w").write("\n".join(L) + "\n")
