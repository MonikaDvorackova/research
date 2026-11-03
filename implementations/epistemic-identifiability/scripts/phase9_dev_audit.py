"""Phase 9 development audit computations (exact / deterministic or labelled). python scripts/phase9_dev_audit.py results/phase9_dev"""
import itertools, json, sys
import numpy as np
from eid.phase9_audit import *
from eid import x1
from eid.pomdp import exact_obs_law, A
out = sys.argv[1]; L = []
def w(s=""): print(s); L.append(s)

# ---- A. corrected Occam dissociation
w("## A. Bayesian-Occam dissociation: truth at psi0 (E[P(true mechanism m2 | data)]; E[predictive KL])\n")
w("| n | psi0 = 0.50 (non-generic) | 0.52 | 0.55 | 0.60 |\n|---|---|---|---|---|")
ns = [10, 30, 100, 300, 1000, 3000, 10000, 30000]
tabs = {p0: dict((n, (pp, kl)) for n, pp, kl in occam_offset(ns, p0)) for p0 in (0.5, 0.52, 0.55, 0.6)}
for n in ns: w(f"| {n} | " + " | ".join(f"{tabs[p0][n][0]:.3f} (KL {tabs[p0][n][1]:.1e})" for p0 in (0.5, 0.52, 0.55, 0.6)) + " |")

# ---- B. Chernoff reconciliation on the X1 benchmark (exact; dev seed 500 of Phase 7)
w("\n## B. Chernoff design exponent vs uniform and passive designs (X1 benchmark, seed 500, episodes as actions; truth vs the null class M)\n")
e0, M, W = x1.build_class(500); tr = x1.truths_for(500)
seqs = list(itertools.product(range(A), repeat=4))
def klv(truth, m):
    r = []
    for a in seqs:
        P, Q = exact_obs_law(truth, a), exact_obs_law(m, a); k = P > 0
        r.append(float(np.sum(P[k] * np.log(P[k] / Q[k]))))
    return np.array(r)
w("| truth | exponent, uniform actions | exponent, passive (P(a=2)=0.02) | Chernoff-optimal | optimal / uniform | observed X1 speed-up of P4 over P2 (confirmatory) |\n|---|---|---|---|---|---|")
obs_speed = {"pc0": 2.01, "pc1": 1.74, "pc2": 1.85}
def policy_w(q):
    pr = np.array([(1 - q) / 2, (1 - q) / 2, q]); return np.array([np.prod(pr[list(a)]) for a in seqs])
for name in ("pc0", "pc1", "pc2", "t10", "t05"):
    K = np.array([klv(tr[name][0], m) for _, m in M])
    opt, lam = chernoff_exponent(K)
    uni = (K @ policy_w(1 / 3)).min(); pas = (K @ policy_w(0.02)).min()
    w(f"| {name} | {uni:.2e} | {pas:.2e} | {opt:.2e} | {opt/uni:.2f} | {obs_speed.get(name, '–')} |")
w("\nFor pc0–pc2 (truth inside the alternative family) the oracle exponent is the relevant rate; for t05, t10 the e-process rate is the margin d_M − d_A, so the table gives only an upper bound.")

# ---- C. statistical audit
w("\n## C. Statistical audit of binomial and clustered claims\n")
w(f"- Zero rejections certify rate ≤ 0.07 at one-sided 95 % only with n ≥ {runs_needed_zero(0.07)} runs, rate ≤ 0.05 with n ≥ {runs_needed_zero(0.05)}; 20 runs per structure give a bound of {cp_upper(0, 20):.3f}.")
w("\nProbability that a pooled claim 'rate ≤ threshold' is demonstrated (one-sided CP, i.i.d. runs):\n")
w("| runs n | true rate | threshold | level | P(claim demonstrated) |\n|---|---|---|---|---|")
for n in (200, 600, 1800):
    for r in (0.02, 0.05):
        for thr in (0.05, 0.07):
            for a in (0.05, 0.05 / 24):
                w(f"| {n} | {r} | {thr} | {'0.05' if a == 0.05 else '0.05/24 (Bonferroni)'} | {prob_demonstrate_bound(n, r, thr, a):.3f} |")
# X1 actual cells
rows = [json.loads(l) for l in open("results/x1_confirm/runs.jsonl")]
cells = {}
for r in rows:
    if r["truth"] in ("E0", "split", "n10", "n20"): cells.setdefault((r["truth"], r["policy"]), []).append(r["reject_episode"] <= 3000)
ks = {c: (sum(v), len(v)) for c, v in cells.items()}
w(f"\nX1 re-evaluated: 24 cells, max rejections {max(k for k, n in ks.values())}/600; max 95 % UB = {max(cp_upper(k, n) for k, n in ks.values()):.4f}; "
  f"max UB at Bonferroni level 0.05/24 = {max(cp_upper(k, n, 0.05/24) for k, n in ks.values()):.4f} (threshold used in the preregistration: 0.07; nominal alpha: 0.05).")
w("\nCoverage of 95 % one-sided upper bounds for a boundary mean rate 0.05, m = 30 structures x R = 20 runs, 300 simulated datasets:\n")
w("| intra-structure correlation | pooled Clopper-Pearson coverage | cluster-bootstrap coverage | cluster-level t bound coverage |\n|---|---|---|---|")
rng = np.random.default_rng(31)
for icc in (0.0, 0.05, 0.2, 0.5):
    cp_, bs_, t_ = coverage_of_upper_bounds(0.05, icc, 30, 20, 300, rng)
    w(f"| {icc} | {cp_:.3f} | {bs_:.3f} | {t_:.3f} |")
w("\nNumber of structures m needed (R = 20 runs each, boundary mean 0.05, intra-structure correlation 0.2):\n")
w("| m structures | pooled CP | cluster bootstrap | cluster t |\n|---|---|---|---|")
for m in (30, 60, 120, 240):
    cp_, bs_, t_ = coverage_of_upper_bounds(0.05, 0.2, m, 20, 300, rng)
    w(f"| {m} | {cp_:.3f} | {bs_:.3f} | {t_:.3f} |")
w("\nPower to REFUTE validity: true rate 0.10, pooled n=600, P(CP lower bound at 95 % > 0.05) = " + f"{prob_refute(600, 0.10):.3f}; at true rate 0.07: {prob_refute(600, 0.07):.3f}.")

# ---- D. policy shift + misspecification: exact pooled-kernel discrepancy for the hidden-state instances (adversarial search for false 'mechanism change')
w("\n## D. Pure policy shift under a misspecified order-1 class: exact discrepancy E_ctx~pi2 KL(k1||k2) per hidden-state instance (mechanism fixed)\n")
from eid.e6gen import gen_hmm
w("| instance | S | order-1 plateau (misspecification) | discrepancy uniform -> extreme(0.9 on action 2) | discrepancy no-action-2 -> uniform |\n|---|---|---|---|---|")
from eid.e6gen import descriptors
for i in range(10):
    p, d = gen_hmm(i)
    w(f"| {i} | {d['S']} | {descriptors(p)['order1_plateau']:.2e} | {policy_kernel_discrepancy(p,[1/3]*3,[.05,.05,.9]):.2e} | {policy_kernel_discrepancy(p,[.5,.5,0.],[1/3]*3):.2e} |")
open(out + "/audit_dev.md", "w").write("\n".join(L) + "\n")
