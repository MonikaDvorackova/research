"""Meta-trained context world model for MDW (GRU).  Context = concatenated episodes; per-step input = [prev obs(2), action(2), start flag].
Imagination = autoregressive roll-out of a probe programme after the context.  DescGRU = supervised descriptor regressor (same encoder)."""
from __future__ import annotations
import math
import torch
import torch.nn as nn

LOG2PI = math.log(2 * math.pi)


class CtxGRU(nn.Module):
    def __init__(self, H=128, E=64, n_desc=0):
        super().__init__()
        self.H = H
        self.inp = nn.Sequential(nn.Linear(5, E), nn.ELU())
        self.cell = nn.GRUCell(E, H)
        self.head = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, 4))
        self.dhead = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, n_desc)) if n_desc else None

    def step(self, h, prev, a, start):
        h = self.cell(self.inp(torch.cat([prev, a, start], -1)), h)
        out = self.head(h)
        return h, out[:, :2], out[:, 2:].clamp(-6, 2)

    def run(self, U, Y, T, ss_prob=0.0, free_last=False):
        """U,Y [B,E*T,2]; returns total NLL [B,E*T] (teacher forced / scheduled sampling; last episode free-running if free_last)."""
        B, L, _ = U.shape
        h = U.new_zeros(B, self.H); prev = U.new_zeros(B, 2); nll = []
        for t in range(L):
            start = U.new_full((B, 1), 1.0 if t % T == 0 else 0.0)
            if t % T == 0: prev = torch.zeros_like(prev)
            h, mu, ls = self.step(h, prev, U[:, t], start)
            nll.append((0.5 * ((Y[:, t] - mu) / ls.exp()) ** 2 + ls + 0.5 * LOG2PI).sum(-1))
            own = (free_last and t >= L - T) or (ss_prob > 0 and float(torch.rand(1)) < ss_prob)
            prev = mu.detach() if own else Y[:, t]
        return torch.stack(nll, 1), h

    @torch.no_grad()
    def encode(self, U, Y, T):
        """final hidden state after a context of episodes (U,Y [B,E*T,2]); zeros if no context."""
        B = U.shape[0]
        if U.shape[1] == 0: return U.new_zeros(B, self.H)
        return self.run(U, Y, T)[1]

    @torch.no_grad()
    def imagine(self, h, progs, T):
        """h [B,H]; progs [B,T,2] -> predicted obs means [B,T,2] (autoregressive from the post-context state)."""
        B = h.shape[0]; prev = progs.new_zeros(B, 2); outs = []
        for t in range(T):
            h, mu, _ = self.step(h, prev, progs[:, t], progs.new_full((B, 1), 1.0 if t == 0 else 0.0))
            outs.append(mu); prev = mu
        return torch.stack(outs, 1)

    def predict_desc(self, h):
        return self.dhead(h)
