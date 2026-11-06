"""Learned state estimator (Role B, representation): bidirectional GRU mapping (noisy x3, u2) -> hidden state x2n = d*x2.
Trained in simulation on the KNOWN families only (lin, sat, delay) with simulator x2 labels (privileged *training* signal, disclosed);
deployed on observations only.  Held-out structure (quad, gate, backlash, fb, osc, unreach) is never seen in training."""
from __future__ import annotations
import numpy as np, torch, torch.nn as nn
from . import env


class Est(nn.Module):
    def __init__(self, hid=48):
        super().__init__()
        self.rnn = nn.GRU(2, hid, num_layers=2, batch_first=True, bidirectional=True); self.out = nn.Linear(2 * hid, 1)

    def forward(self, y3, u2):
        h, _ = self.rnn(torch.stack([y3, u2], -1)); return self.out(h)[..., 0]


def make_data(n, seed):
    rng = np.random.default_rng(seed); X, U2, Z = [], [], []
    progs = env.random_programmes(n, rng)
    for i, u in enumerate(progs):
        inst = env.make_instance(env.KNOWN[i % 3], rng)
        if rng.random() < 0.3: u = u.copy(); u[:, 0] = 0; u[:, 1] = env._sq(rng.uniform(.3, 1), int(rng.integers(12, 30)))      # u2-only episode
        y, _, x2n = env.simulate(inst, u, rng); X.append(y[:, 1]); U2.append(u[:, 1]); Z.append(x2n)
    return [torch.tensor(np.array(a), dtype=torch.float32) for a in (X, U2, Z)]


def train(seed, steps=1500, n=6000, log=None):
    torch.manual_seed(seed); X, U2, Z = make_data(n, 24100 + seed)
    m = Est(); opt = torch.optim.Adam(m.parameters(), 3e-3); g = torch.Generator().manual_seed(seed)
    for s in range(steps):
        idx = torch.randint(0, n, (64,), generator=g)
        loss = ((m(X[idx], U2[idx]) - Z[idx]) ** 2).mean(); opt.zero_grad(); loss.backward(); opt.step()
        if log and s % 250 == 0: log(f"step {s} mse {loss.item():.5f}")
    return m


@torch.no_grad()
def infer(m, y3, u2):
    """y3,u2 [E,T] arrays -> x2n estimate [E,T]."""
    return m(torch.tensor(y3, dtype=torch.float32), torch.tensor(u2, dtype=torch.float32)).numpy().astype(float)
