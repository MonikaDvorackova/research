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
