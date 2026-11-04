"""Action policies for the generative-world benchmark (agent-side; never sees hidden state)."""
from __future__ import annotations
import torch

MENU = torch.tensor([-1, -.6, -.3, -.15, -.08, 0, .08, .15, .3, .6, 1.], dtype=torch.float64)
BLOCK = 8


def sample_actions(kind, n, L, g):
    f = dict(dtype=torch.float64)
    if kind == "uniform":
        return torch.rand(n, L, generator=g, **f) * 2 - 1
    if kind == "passive":      # weak exploratory behaviour ~ observational regime
        return (0.3 * torch.randn(n, L, generator=g, **f)).clamp(-1, 1)
    if kind == "smooth":       # AR(1) random walk
        u = torch.zeros(n, L, **f); e = torch.randn(n, L, generator=g, **f)
        cur = torch.zeros(n, **f)
        for t in range(L):
            cur = 0.9 * cur + 0.4 * e[:, t]; u[:, t] = cur
        return u.clamp(-1, 1)
    if kind == "block":        # random constants from menu, 8-step blocks
        return MENU[torch.randint(0, len(MENU), (n, L // BLOCK), generator=g)].repeat_interleave(BLOCK, 1)
    if kind == "pulse":        # sparse large pulses
        m = (torch.rand(n, L, generator=g, **f) < 0.15).double()
        return m * (torch.rand(n, L, generator=g, **f) * 2 - 1)
    if kind == "sweep":        # HELD-OUT intervention condition: amplitude ramp with alternating sign blocks
        amp = torch.linspace(0.05, 1.0, L // BLOCK, **f).repeat_interleave(BLOCK)
        sgn = torch.tensor([1.0, 1.0, -1.0, -1.0, 1.0, -1.0], **f)[: L // BLOCK].repeat_interleave(BLOCK)
        return (amp * sgn)[None].repeat(n, 1)
    raise ValueError(kind)


TRAIN_KINDS = ("uniform", "passive", "smooth", "block", "pulse")


def sample_train_actions(n, L, g):
    kinds = torch.randint(0, len(TRAIN_KINDS), (n,), generator=g)
    out = torch.zeros(n, L, dtype=torch.float64)
    for i, k in enumerate(TRAIN_KINDS):
        sel = kinds == i
        if sel.any():
            out[sel] = sample_actions(k, int(sel.sum()), L, g)
    return out
