"""Finite POMDP benchmark (second environment): hidden states, noisy observations, exact likelihoods and exact law enumeration.

Hidden states 0..3. Observations 0..2. Actions 0..2.
 - States 0 and 1 emit the same symbol distribution: the observer cannot tell them apart from a single observation.
 - Action 2 sends state 0 to state 2 and state 1 to state 3 (with high probability), so the *next observation* reveals which of the
   two indistinguishable states the system was in. Actions 0 and 1 do not depend on that distinction in an observable way.
 - The training policy uses action 2 rarely, so a learned world model sees little evidence about it (an intervention-coverage gap).
Controls (all exact):
 - E0 : the reference POMDP.
 - Eeq: E0 with hidden state 0 split into two copies with identical outgoing rows and emissions and equally split incoming mass:
        a bisimilar, hence observationally equivalent, POMDP with a different hidden structure (verified exactly).
 - Et : mechanism-distinct but observationally similar: action-2 transitions of states 0 and 1 are partly swapped.
 - En : emission-noise variant: each emitted symbol is replaced by a uniform symbol with probability eta.
"""
from __future__ import annotations

import itertools

import numpy as np

S, A, O = 4, 3, 3
START = O   # start token for the previous observation


def _norm(M):
    return M / M.sum(-1, keepdims=True)


def make_e0(seed: int, jitter: float = 0.08):
    """Reference POMDP with the structure above; per-seed jitter varies the numbers without changing the structure."""
    r = np.random.default_rng(seed)
    T = np.zeros((A, S, S))
    T[0] = 0.8 * np.eye(S) + 0.2 / (S - 1) * (1 - np.eye(S))                      # wait: mostly stay
    for s in range(S):
        T[1, s, (s + 1) % S] += 0.7
        T[1, s, s] += 0.2
        T[1, s, (s + 2) % S] += 0.1                                               # rotate
    T[2] = np.array([[0.02, 0.02, 0.92, 0.04], [0.02, 0.02, 0.04, 0.92],
                     [0.45, 0.45, 0.05, 0.05], [0.45, 0.45, 0.05, 0.05]])        # informative action
    T = _norm((1 - jitter) * T + jitter * r.dirichlet(np.ones(S), size=(A, S)))
    Z = _norm(0.9 * np.array([[0.8, 0.1, 0.1], [0.8, 0.1, 0.1], [0.1, 0.8, 0.1], [0.1, 0.1, 0.8]]) + 0.1 * r.dirichlet(np.ones(O), size=S))
    b0 = np.array([0.5, 0.5, 0.0, 0.0])
    return POMDP(T, Z, b0)


class POMDP:
    def __init__(self, T, Z, b0):
        self.T, self.Z, self.b0 = np.asarray(T), np.asarray(Z), np.asarray(b0)
        self.S = self.T.shape[1]

    # ---- simulation (hidden state is internal; only observations leave)
    def reset(self, R, rng):
        return rng.choice(self.S, size=R, p=self.b0)

    def step(self, s, a, rng):
        cum = np.cumsum(self.T[a, s], axis=1)
        s2 = np.minimum((rng.random(len(s))[:, None] > cum).sum(1), self.S - 1)
        cum = np.cumsum(self.Z[s2], axis=1)
        o = np.minimum((rng.random(len(s))[:, None] > cum).sum(1), O - 1)
        return s2, o

    # ---- exact filtering (used by hypotheses, never by the environment's own sampler)
    def belief0(self, R):
        return np.tile(self.b0, (R, 1))

    def predict(self, b):
        """p(o | a, belief) for every action: (R, A, O)."""
        bp = np.einsum("rs,ast->rat", b, self.T)                 # (R, A, S) next-state distribution
        return np.einsum("rat,to->rao", bp, self.Z)

    def update(self, b, a, o):
        bp = np.einsum("rs,rst->rt", b, self.T[a])
        post = bp * self.Z[:, o].T
        return post / post.sum(1, keepdims=True)


def with_emission_noise(p: POMDP, eta: float) -> POMDP:
    return POMDP(p.T, (1 - eta) * p.Z + eta / O, p.b0)


def split_state0(p: POMDP) -> POMDP:
    """Bisimilar POMDP with a duplicated copy of hidden state 0 (new index S). Incoming mass to 0 is split equally."""
    n = p.S + 1
    T = np.zeros((A, n, n))
    for a in range(A):
        for s in range(p.S):
            row = p.T[a, s]
            for t in range(p.S):
                if t == 0:
                    T[a, s, 0] += row[0] / 2
                    T[a, s, p.S] += row[0] / 2
                else:
                    T[a, s, t] += row[t]
        T[a, p.S] = T[a, 0]                                       # the copy has identical outgoing behaviour
    Z = np.vstack([p.Z, p.Z[0]])
    b0 = np.append(p.b0.copy(), 0.0)
    b0[p.S] = b0[0] / 2
    b0[0] = b0[0] / 2
    return POMDP(T, Z, b0)


def perturb_action2(p: POMDP, eps: float) -> POMDP:
    """Mechanism-distinct control: with probability eps the action-2 transitions of states 0 and 1 are swapped."""
    T = p.T.copy()
    r0, r1 = T[2, 0].copy(), T[2, 1].copy()
    T[2, 0] = (1 - eps) * r0 + eps * r1
    T[2, 1] = (1 - eps) * r1 + eps * r0
    return POMDP(T, p.Z, p.b0)


# ------------------------------------------------------------------------------------------------ exact enumeration
def exact_obs_law(p: POMDP, actions):
    """Exact probabilities of all observation sequences (shape (O,)*T flattened to O**T) under a fixed action sequence."""
    alpha = p.b0[None, :]                                          # (1, S): unnormalised forward vectors indexed by observation prefix
    for a in actions:
        nxt = (alpha @ p.T[a])[:, None, :] * p.Z.T[None, :, :]     # (prefixes, O, S)
        alpha = nxt.reshape(-1, p.S)
    return alpha.sum(1)


def brute_force_obs_law(p: POMDP, actions):
    """Independent computation by summing over all hidden paths (for validating the forward algorithm)."""
    T_len = len(actions)
    law = np.zeros(O ** T_len)
    for obs in itertools.product(range(O), repeat=T_len):
        tot = 0.0
        for path in itertools.product(range(p.S), repeat=T_len):
            pr, prev = 1.0, None
            for t, (a, s2, o) in enumerate(zip(actions, path, obs)):
                trans = (p.b0 @ p.T[a])[s2] if t == 0 else p.T[a, prev, s2]
                pr *= trans * p.Z[s2, o]
                prev = s2
            tot += pr
        law[np.ravel_multi_index(obs, (O,) * T_len)] = tot
    return law
