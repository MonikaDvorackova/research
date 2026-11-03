"""Exact demonstration of observational equivalence RELATIVE TO AN INTERVENTION CLASS in the POMDP benchmark.

Hypotheses: the reference POMDP E0 and the transition-perturbed POMDP Et (identical unless action 2 is used). An observer with exact
likelihoods for both, equal priors, interacts with truth Et. Under a policy that never uses action 2 the posterior odds E0 : Et stay at
the prior odds to numerical precision at every step; under a policy that uses action 2 they move. Usage: PYTHONPATH=src python scripts/equivalence_demo.py"""
import numpy as np

from eid.bayes2 import POMDPMember, Space2, run_observer2
from eid.gruworld import POMDPEnv
from eid.pomdp import make_e0, perturb_action2


def odds_after(policy, steps, seed, R=200):
    e0 = make_e0(seed)
    et = perturb_action2(e0, 0.9)
    sp = Space2([POMDPMember(e0), POMDPMember(et)], [0, 2], (0.5, 0, 0.5, 0))
    out = run_observer2(sp, POMDPEnv(et), policy, np.random.default_rng(seed), R=R, steps=steps, episode_len=10, checkpoints=(steps,))
    p = out["post"][:, 0]
    return p[:, 2] / p[:, 0]


if __name__ == "__main__":
    for seed in (0, 1, 2):
        no2 = odds_after("no2", 100, seed)
        rnd = odds_after("random", 100, seed)
        print(f"seed {seed}: posterior odds Et:E0 after 100 steps, truth Et. never action 2: max |odds - 1| = {np.abs(no2 - 1).max():.2e}; "
              f"random actions: median odds = {np.median(rnd):.2f} (fraction of runs with odds > 3: {(rnd > 3).mean():.2f})")
