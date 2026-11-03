"""Embedded agent: sees only (action, observation) streams; holds its own theory Q.

The environment is passed as an opaque object and only ``env.step`` is ever called. The agent
receives no label, no parameters, and no reference samples at test time.
"""
from __future__ import annotations

import numpy as np

from .env import sample_x0

POLICIES = ("passive", "wide", "active")
A_IN, A_WIDE, N_CAND = 1.0, 3.0, 64


def choose_action(policy: str, x, ensemble, rng):
    b = x.shape[0]
    if policy == "passive":                       # training-like interventions
        return rng.uniform(-A_IN, A_IN, b)
    if policy == "wide":                          # random out-of-distribution interventions
        return rng.uniform(-A_WIDE, A_WIDE, b)
    if policy == "active":                        # information-seeking: maximise ensemble disagreement
        cand = rng.uniform(-A_WIDE, A_WIDE, (b, N_CAND))
        xr = np.repeat(x, N_CAND, axis=0)
        _, _, epi = ensemble.predictive(xr, cand.reshape(-1))
        return cand[np.arange(b), epi.reshape(b, N_CAND).argmax(1)]
    raise ValueError(policy)


def interact(env, policy: str, ensemble, batch: int, horizon: int, rng):
    """Run ``batch`` independent episodes. Returns observations, actions, and Q-standardised residuals."""
    x = sample_x0(rng, batch)
    X, A, Z = [x], [], []
    for _ in range(horizon):
        a = choose_action(policy, x, ensemble, rng)
        mean, var, _ = ensemble.predictive(x, a)
        y = env.step(x, a, rng)
        Z.append((y - mean) / np.sqrt(var))
        A.append(a)
        X.append(y)
        x = y
    return np.stack(X, 1), np.stack(A, 1), np.stack(Z, 1)  # (B,T+1,2), (B,T), (B,T,2)
