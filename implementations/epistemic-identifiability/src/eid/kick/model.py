"""Autoregressive world model for kick-world (GRU latent):  p(click_t | past) * p(o_t | past, click_t),
o_t=(p,v) Gaussian.  The click cross-entropy is a proper score for the shock channel: under true randomness (iid fair bits)
E[CE] >= ln 2 for ANY predictor computed from the past, so a frozen-predictor test on fresh streams is null-valid."""
from __future__ import annotations
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

LOG2PI = math.log(2 * math.pi)


class KickGRU(nn.Module):
    def __init__(self, H=128, E=64):
        super().__init__()
        self.H = H
        self.inp = nn.Sequential(nn.Linear(4, E), nn.ELU())          # prev (p,v), prev click, action
        self.cell = nn.GRUCell(E, H)
        self.click_head = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, 1))
        self.obs_head = nn.Sequential(nn.Linear(H + 1, E), nn.ELU(), nn.Linear(E, 4))

    def forward(self, obs, act, click):
        B, T, _ = obs.shape
        h = obs.new_zeros(B, self.H); prev = obs.new_zeros(B, 2); pc = obs.new_zeros(B, 1)
        bce, nll = [], []; plogit = []
        for t in range(T):
            h = self.cell(self.inp(torch.cat([prev, pc, act[:, t:t + 1]], -1)), h)
            lg = self.click_head(h).squeeze(-1)
            c = click[:, t]
            bce.append(F.binary_cross_entropy_with_logits(lg, c, reduction="none")); plogit.append(lg)
            out = self.obs_head(torch.cat([h, c[:, None]], -1)); mu, ls = out[:, :2], out[:, 2:].clamp(-6, 2)
            nll.append((0.5 * ((obs[:, t] - mu) / ls.exp()) ** 2 + ls + 0.5 * LOG2PI).sum(-1))
            prev = obs[:, t]; pc = c[:, None]
        return torch.stack(bce, 1), torch.stack(nll, 1), torch.stack(plogit, 1)
