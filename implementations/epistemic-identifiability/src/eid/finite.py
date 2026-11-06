"""Exact computations on finite controlled processes, used to check the propositions numerically.

A finite environment is a dict mapping (history, action) -> probability vector over observations,
where history is a tuple (a_1, o_1, ..., a_{t-1}, o_{t-1}). A policy maps history -> probability
vector over actions. Histories of length T are enumerated exactly.
"""
from __future__ import annotations

import itertools
import math

import numpy as np


def history_law(env, policy, n_actions: int, n_obs: int, T: int):
    """Exact law of the T-step history (a_1,o_1,...,a_T,o_T) under ``policy`` in ``env``."""
    law = {}
    for hist in itertools.product(*[range(n_actions), range(n_obs)] * T):
        p, h = 1.0, ()
        for t in range(T):
            a, o = hist[2 * t], hist[2 * t + 1]
            p *= policy(h)[a] * env(h, a)[o]
            h = h + (a, o)
        law[hist] = p
    return law


def kl(p: dict, q: dict) -> float:
    return sum(v * math.log(v / q[k]) for k, v in p.items() if v > 0) if all(q[k] > 0 for k, v in p.items() if v > 0) else math.inf


def tv(p: dict, q: dict) -> float:
    return 0.5 * sum(abs(p[k] - q[k]) for k in p)


def stepwise_kl_sum(env0, env1, policy, n_actions, n_obs, T):
    """E_{P0^pi} sum_t KL(p0(.|h,a) || p1(.|h,a)) computed from the kernels (RHS of the chain rule)."""
    total = 0.0
    for t in range(T):
        # distribution over (h_{t-1}, a_t) under P0^pi, then expected kernel KL
        for pre in itertools.product(*[range(n_actions), range(n_obs)] * t):
            p_pre = 1.0
            h = ()
            for s in range(t):
                a, o = pre[2 * s], pre[2 * s + 1]
                p_pre *= policy(h)[a] * env0(h, a)[o]
                h = h + (a, o)
            for a in range(n_actions):
                w = p_pre * policy(h)[a]
                if w > 0:
                    k0, k1 = env0(h, a), env1(h, a)
                    total += w * sum(k0[o] * math.log(k0[o] / k1[o]) for o in range(n_obs) if k0[o] > 0)
    return total


# ---------------------------------------------------------------------------------------------------------------
# Additional exact computations (Propositions 7-9). Not used by the experiment runner.
# ---------------------------------------------------------------------------------------------------------------

def auc_exact(p0: dict, p1: dict, score: dict) -> float:
    """Exact AUROC of ``score`` (a dict outcome -> real) for positives ~ p1 against negatives ~ p0, ties counted 1/2."""
    gt = tie = 0.0
    for k1, w1 in p1.items():
        for k0, w0 in p0.items():
            if score[k1] > score[k0]:
                gt += w1 * w0
            elif score[k1] == score[k0]:
                tie += w1 * w0
    return gt + 0.5 * tie


def max_auc_over_orders(p0: dict, p1: dict) -> float:
    """Maximum AUROC over all rankings of the (small) outcome set, by exhaustive enumeration."""
    keys = list(p0)
    best = 0.0
    for perm in itertools.permutations(range(len(keys))):
        best = max(best, auc_exact(p0, p1, {k: perm[i] for i, k in enumerate(keys)}))
    return best


def deterministic_policy_sup_tv(env0, env1, n_actions: int, n_obs: int, adaptive: bool):
    """sup over deterministic 2-step policies of TV(P0^pi, P1^pi): open-loop (a2 independent of o1) or history-dependent."""
    best = 0.0
    for a1 in range(n_actions):
        if adaptive:
            a2_choices = itertools.product(range(n_actions), repeat=n_obs)   # a2 as a function of o1
        else:
            a2_choices = ((c,) * n_obs for c in range(n_actions))             # constant a2
        for a2_map in a2_choices:
            def pol(h, a1=a1, a2_map=a2_map):
                a = a1 if len(h) == 0 else a2_map[h[1]]
                v = np.zeros(n_actions)
                v[a] = 1.0
                return v
            best = max(best, tv(history_law(env0, pol, n_actions, n_obs, 2), history_law(env1, pol, n_actions, n_obs, 2)))
    return best


def posterior_after(models, truth_sampler, n_episodes: int, rng, prior=None):
    """Posterior over a finite model class after n i.i.d. episodes drawn from ``truth_sampler(rng)``.

    ``models`` is a list of dicts outcome -> probability (all with the same support)."""
    logp = np.log(np.array(prior if prior is not None else [1.0 / len(models)] * len(models)))
    for _ in range(n_episodes):
        o = truth_sampler(rng)
        logp = logp + np.array([math.log(m[o]) for m in models])
    logp -= logp.max()
    p = np.exp(logp)
    return p / p.sum()
