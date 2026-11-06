"""Exact power-feasibility table for X1 (no random numbers, no outcome data).
For each truth: KL rate (nats/episode) to the nearest member of M and to the nearest member of M u W, under policies with
P(action 2) = q; N*_M = ln(20)/KL_M is the episodes an *oracle* likelihood-ratio test against its nearest class member needs on average
(Wald lower bound), and the e-process with the mixture alternative needs at least ln(20)/KL(truth || M u W) (best case: truth in W)."""
import sys, json
import numpy as np
from eid.x1 import build_class, truths_for
from eid.x1_exact import nearest_member

seed = int(sys.argv[1]); out = sys.argv[2]
e0, M, W = build_class(seed)
Ms = [m for _, m in M]; names = [n for n, _ in M]
rows = []
for tn, (t, role) in truths_for(seed).items():
    for q in (0.0, 0.02, 1 / 3):
        iM, kM = nearest_member(t, Ms, q)
        iA, kA = nearest_member(t, Ms + [w for _, w in W], q)
        rows.append(dict(truth=tn, role=role, q=round(q, 3), nearest_M=names[iM], KL_M=kM, KL_MW=kA,
                         Nstar_M=(np.log(20) / kM if kM > 1e-12 else None)))
json.dump(rows, open(out + ".json", "w"), indent=1)
with open(out + ".txt", "w") as f:
    f.write(f"seed {seed}\n{'truth':6s} {'role':10s} {'q':>5s} {'near':>5s} {'KL_M':>10s} {'KL_MW':>10s} {'N*_M(oracle)':>13s}\n")
    for r in rows:
        f.write(f"{r['truth']:6s} {r['role']:10s} {r['q']:5.2f} {r['nearest_M']:>5s} {r['KL_M']:10.2e} {r['KL_MW']:10.2e} "
                f"{('%.0f' % r['Nstar_M']) if r['Nstar_M'] else 'inf':>13s}\n")
print(open(out + ".txt").read())
