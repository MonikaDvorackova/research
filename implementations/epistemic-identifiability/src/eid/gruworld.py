"""GRU world model for the POMDP benchmark: an autoregressive latent-state model p(o_t | a_{1:t}, o_{<t}) trained on reference trajectories."""
from __future__ import annotations

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

from .pomdp import A, O, POMDP, START

TRAIN_P2 = 0.02   # probability of the informative action 2 under the training policy


class GRUWorld(nn.Module):
    def __init__(self, hidden: int = 32):
        super().__init__()
        self.hidden = hidden
        self.cell = nn.GRUCell(A + O + 1, hidden)
        self.head = nn.Linear(hidden, O)

    def step(self, h, a, prev):
        x = torch.cat([F.one_hot(a, A).float(), F.one_hot(prev, O + 1).float()], dim=1)
        h2 = self.cell(x, h)
        return h2, self.head(h2)

    def seq_logprob(self, acts, obs):
        """Exact log-probability of each observation sequence given the actions (B,T) -> (B,)."""
        B, T = acts.shape
        h = torch.zeros(B, self.hidden)
        prev = torch.full((B,), START, dtype=torch.long)
        lp = torch.zeros(B)
        for t in range(T):
            h, logits = self.step(h, acts[:, t], prev)
            lp = lp + F.log_softmax(logits, dim=1).gather(1, obs[:, t:t + 1]).squeeze(1)
            prev = obs[:, t]
        return lp


def sample_dataset(pomdp: POMDP, n_episodes: int, horizon: int, rng, p2: float = TRAIN_P2):
    probs = np.array([(1 - p2) / 2, (1 - p2) / 2, p2])
    acts = rng.choice(A, size=(n_episodes, horizon), p=probs)
    s = pomdp.reset(n_episodes, rng)
    obs = np.zeros_like(acts)
    for t in range(horizon):
        s, obs[:, t] = pomdp.step(s, acts[:, t], rng)
    return acts, obs


def train_gru(acts, obs, seed: int, steps: int = 700, lr: float = 5e-3, batch: int = 128, hidden: int = 32) -> GRUWorld:
    torch.manual_seed(seed)
    m = GRUWorld(hidden)
    opt = torch.optim.Adam(m.parameters(), lr=lr)
    a, o = torch.as_tensor(acts, dtype=torch.long), torch.as_tensor(obs, dtype=torch.long)
    g = torch.Generator().manual_seed(seed)
    n, T = a.shape
    for _ in range(steps):
        idx = torch.randint(0, n, (min(batch, n),), generator=g)
        loss = -m.seq_logprob(a[idx], o[idx]).mean() / T
        opt.zero_grad()
        loss.backward()
        opt.step()
    return m


def gru_obs_law(m: GRUWorld, actions):
    """Exact probabilities of all O**T observation sequences under a fixed action sequence."""
    import itertools
    T = len(actions)
    seqs = torch.as_tensor(list(itertools.product(range(O), repeat=T)), dtype=torch.long)
    acts = torch.as_tensor(actions, dtype=torch.long)[None, :].expand(len(seqs), T)
    with torch.no_grad():
        return m.seq_logprob(acts, seqs).exp().numpy().astype(np.float64)


# --------------------------------------------------------------------------------------------- environments (observation-only interface)
class POMDPEnv:
    def __init__(self, pomdp: POMDP):
        self.p = pomdp

    def reset(self, R, rng):
        self.s = self.p.reset(R, rng)

    def step(self, a, rng):
        self.s, o = self.p.step(self.s, a, rng)
        return o


class GRUEnv:
    """The learned world model used as the environment: samples o_t from its own predictive distribution."""

    def __init__(self, m: GRUWorld):
        self.m = m

    def reset(self, R, rng):
        self.h = torch.zeros(R, self.m.hidden)
        self.prev = torch.full((R,), START, dtype=torch.long)

    def step(self, a, rng):
        with torch.no_grad():
            self.h, logits = self.m.step(self.h, torch.as_tensor(a, dtype=torch.long), self.prev)
            p = F.softmax(logits, dim=1).numpy().astype(np.float64)
        p = p / p.sum(1, keepdims=True)
        o = np.minimum((rng.random(len(a))[:, None] > np.cumsum(p, axis=1)).sum(1), O - 1)
        self.prev = torch.as_tensor(o, dtype=torch.long)
        return o
