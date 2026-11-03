"""Gaussian MLP dynamics models (world model W and the agent's theory ensemble Q)."""
from __future__ import annotations

import numpy as np
import torch
import torch.nn as nn

LOGSTD_MIN, LOGSTD_MAX = -5.0, 1.0


class GaussMLP(nn.Module):
    def __init__(self, hidden: int = 64):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(3, hidden), nn.Tanh(), nn.Linear(hidden, hidden), nn.Tanh(), nn.Linear(hidden, 4))

    def forward(self, x, a):
        out = self.net(torch.cat([x, a[:, None]], dim=1))
        mu = x + out[:, :2]  # residual parameterisation
        logstd = out[:, 2:].clamp(LOGSTD_MIN, LOGSTD_MAX)
        return mu, logstd

    @torch.no_grad()
    def predict(self, x: np.ndarray, a: np.ndarray):
        mu, logstd = self(torch.as_tensor(x, dtype=torch.float32), torch.as_tensor(a, dtype=torch.float32))
        return mu.numpy().astype(np.float64), logstd.exp().numpy().astype(np.float64)


def train_gauss(X, A, Y, seed: int, steps: int = 1500, lr: float = 3e-3, batch: int = 256, hidden: int = 64) -> GaussMLP:
    torch.manual_seed(seed)
    model = GaussMLP(hidden)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    x, a, y = (torch.as_tensor(v, dtype=torch.float32) for v in (X, A, Y))
    g = torch.Generator().manual_seed(seed)
    n = x.shape[0]
    for _ in range(steps):
        idx = torch.randint(0, n, (min(batch, n),), generator=g)
        mu, logstd = model(x[idx], a[idx])
        nll = (0.5 * ((y[idx] - mu) / logstd.exp()) ** 2 + logstd).mean()
        opt.zero_grad()
        nll.backward()
        opt.step()
    return model


class Ensemble:
    """Agent-side theory Q: moment-matched mixture of K Gaussian models."""

    def __init__(self, members):
        self.members = members

    def predict_all(self, x, a):
        mus, stds = zip(*(m.predict(x, a) for m in self.members))
        return np.stack(mus), np.stack(stds)  # (K, B, 2)

    def predictive(self, x, a):
        mus, stds = self.predict_all(x, a)
        mean = mus.mean(0)
        epi = mus.var(0)                      # epistemic variance per dimension
        var = (stds**2).mean(0) + epi         # total predictive variance
        return mean, np.maximum(var, 1e-8), epi.sum(-1)
