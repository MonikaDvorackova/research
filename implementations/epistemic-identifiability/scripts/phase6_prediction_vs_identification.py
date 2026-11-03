"""Phase 6 lightweight diagnostic (Direction A): exact predictive vs interventional divergence in the finite POMDP.

For the reference POMDP E0 and the mechanism-distinct control Et(eps) we compute, exactly, the per-episode KL(E0 || Et) of the
observation law under action policies that play the informative action 2 with probability q (other actions uniform), horizon T.
Predictive gap under the training policy (small q) vs identification gap under a wide policy (q = 1/3):
a model whose predictive error on its own training distribution is below delta can still be far from E0 on the wide class.
This is a coverage amplification (cf. Proposition 3), not a new theorem; the script only quantifies it for the benchmark.
Exploratory; no random numbers are used (exact enumeration).
"""
import itertools
import json
import sys

import numpy as np

from eid.pomdp import make_e0, perturb_action2, exact_obs_law

T_H = 4
SEED = 0


def policy_kl(p, r, q, T=T_H):
    """E_{actions ~ policy_q} KL(law_p(.|actions) || law_r(.|actions)); policy is open loop, iid across steps."""
    probs = np.array([(1 - q) / 2, (1 - q) / 2, q])
    tot = 0.0
    for acts in itertools.product(range(3), repeat=T):
        w = np.prod(probs[list(acts)])
        if w == 0:
            continue
        P, R = exact_obs_law(p, acts), exact_obs_law(r, acts)
        m = P > 0
        tot += w * np.sum(P[m] * np.log(P[m] / R[m]))
    return tot


def main():
    e0 = make_e0(SEED)
    rows = []
    for eps in (0.05, 0.2, 0.5):
        et = perturb_action2(e0, eps)
        k_wide = policy_kl(e0, et, 1 / 3)
        for q in (0.0, 0.005, 0.02, 0.1, 1 / 3):
            k = policy_kl(e0, et, q)
            rows.append(dict(eps=eps, q=round(q, 4), kl_per_episode=k, kl_wide=k_wide,
                             amplification=(k_wide / k if k > 0 else float('inf')),
                             episodes_for_unit_log_odds=(1 / k if k > 0 else float('inf'))))
    json.dump(rows, open(sys.argv[1], 'w'), indent=1)
    print(f"{'eps':>5} {'q':>7} {'KL/ep':>10} {'KL wide':>9} {'amplif.':>10} {'eps-needed(1 nat)':>18}")
    for r in rows:
        print(f"{r['eps']:5.2f} {r['q']:7.4f} {r['kl_per_episode']:10.2e} {r['kl_wide']:9.2e} {r['amplification']:10.1f} {r['episodes_for_unit_log_odds']:18.1f}")


if __name__ == '__main__':
    main()
