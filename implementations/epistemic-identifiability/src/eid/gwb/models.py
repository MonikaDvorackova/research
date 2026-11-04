"""Learned latent world models (CPU/MPS): RSSM-style, deterministic-GRU comparator, ICI discovery variant.

All models consume only (a_t, y_t).  Convention: y_t is the observation AFTER action a_t is applied.
"""
from __future__ import annotations
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

LOG2PI = math.log(2 * math.pi)


def gauss_nll(y, mu, logstd):
    return 0.5 * ((y - mu) / logstd.exp()) ** 2 + logstd + 0.5 * LOG2PI


class RSSM(nn.Module):
    """h_t = GRU(h_{t-1}, [z_{t-1}, a_t]); prior p(z_t|h_t); posterior q(z_t|h_t,y_t); decoder p(y_t|h_t,z_t)."""

    def __init__(self, H=128, Z=8, E=64, proj=64):
        super().__init__()
        self.H, self.Z = H, Z
        self.inp = nn.Sequential(nn.Linear(Z + 1, E), nn.ELU())
        self.cell = nn.GRUCell(E, H)
        self.prior = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, 2 * Z))
        self.post = nn.Sequential(nn.Linear(H + 1, E), nn.ELU(), nn.Linear(E, 2 * Z))
        self.dec = nn.Sequential(nn.Linear(H + Z, E), nn.ELU(), nn.Linear(E, 2))
        self.proj = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, proj))  # ICI head (unused if lambda=0)

    @staticmethod
    def _split(p):
        m, s = p.chunk(2, -1)
        return m, F.softplus(s) + 0.1

    def forward(self, a, y, free_bits=0.1, sample=True):
        B, T = a.shape
        h = a.new_zeros(B, self.H); z = a.new_zeros(B, self.Z)
        nll, kl, nllp = [], [], []
        mus = []
        for t in range(T):
            h = self.cell(self.inp(torch.cat([z, a[:, t:t + 1]], -1)), h)
            pm, ps = self._split(self.prior(h))
            # prior-predictive loss (deviation from Dreamer): decode y_t from a PRIOR sample, so the dynamics
            # (not the posterior leak of y_t) must carry the prediction.  Added after dev eval showed the
            # reconstruction decoder otherwise autoencodes observation noise (excess prior-NLL ~390).
            outp = self.dec(torch.cat([h, pm + ps * torch.randn_like(ps)], -1))
            nllp.append(gauss_nll(y[:, t:t + 1], outp[:, :1], outp[:, 1:].clamp(-5, 2)).squeeze(-1))
            qm, qs = self._split(self.post(torch.cat([h, y[:, t:t + 1]], -1)))
            z = qm + qs * torch.randn_like(qs) if sample else qm
            out = self.dec(torch.cat([h, z], -1))
            mu, ls = out[:, :1], out[:, 1:].clamp(-5, 2)
            nll.append(gauss_nll(y[:, t:t + 1], mu, ls).squeeze(-1)); mus.append(mu.squeeze(-1))
            # KL balancing (0.8 train prior / 0.2 posterior), free bits
            kl_p = _kl(qm.detach(), qs.detach(), pm, ps).sum(-1).clamp_min(free_bits)
            kl_q = _kl(qm, qs, pm.detach(), ps.detach()).sum(-1).clamp_min(free_bits)
            kl.append(0.8 * kl_p + 0.2 * kl_q)
        h = self.cell(self.inp(torch.cat([z, torch.zeros_like(a[:, :1])], -1)), h)  # summary state (dummy zero action)
        return dict(nll=torch.stack(nll, 1), kl=torch.stack(kl, 1), nll_prior=torch.stack(nllp, 1), mu=torch.stack(mus, 1), feat=h)

    @torch.no_grad()
    def filter(self, a, y):
        """Posterior-mean filtering; returns final (h, z) and per-step one-step PRIOR predictive (mean, logstd)."""
        B, T = a.shape
        h = a.new_zeros(B, self.H); z = a.new_zeros(B, self.Z)
        mus, lss = [], []
        for t in range(T):
            h = self.cell(self.inp(torch.cat([z, a[:, t:t + 1]], -1)), h)
            pm, ps = self._split(self.prior(h))
            out = self.dec(torch.cat([h, pm], -1))     # prior-mean prediction (no access to y_t)
            mus.append(out[:, 0]); lss.append(out[:, 1].clamp(-5, 2))
            qm, _ = self._split(self.post(torch.cat([h, y[:, t:t + 1]], -1)))
            z = qm
        return h, z, torch.stack(mus, 1), torch.stack(lss, 1)

    @torch.no_grad()
    def step_state(self, h, z, a_t):
        return self.cell(self.inp(torch.cat([z, a_t[:, None]], -1)), h)

    @torch.no_grad()
    def rollout(self, h, z, acts):
        """Open-loop imagination: prior-mean latents; returns predicted y means [B,K]."""
        mus = []
        for t in range(acts.shape[1]):
            h = self.cell(self.inp(torch.cat([z, acts[:, t:t + 1]], -1)), h)
            pm, _ = self._split(self.prior(h))
            z = pm
            mus.append(self.dec(torch.cat([h, z], -1))[:, 0])
        return torch.stack(mus, 1)

    def summary(self, h):
        return h

    def init_state(self, B, dev="cpu"):
        return torch.zeros(B, self.H, device=dev), torch.zeros(B, self.Z, device=dev)


def _kl(qm, qs, pm, ps):
    return torch.log(ps / qs) + (qs ** 2 + (qm - pm) ** 2) / (2 * ps ** 2) - 0.5


class DetGRU(nn.Module):
    """Deterministic recurrent latent dynamics (no stochastic latent): h_t=GRU(h_{t-1},[y_{t-1},a_t])."""

    def __init__(self, H=128, E=64, proj=64):
        super().__init__()
        self.H = H
        self.inp = nn.Sequential(nn.Linear(2, E), nn.ELU())
        self.cell = nn.GRUCell(E, H)
        self.head = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, 2))
        self.proj = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, proj))

    def forward(self, a, y, free_bits=0.0, sample=True):
        B, T = a.shape
        h = a.new_zeros(B, self.H); yp = a.new_zeros(B, 1)
        nll, mus = [], []
        for t in range(T):
            h = self.cell(self.inp(torch.cat([yp, a[:, t:t + 1]], -1)), h)
            out = self.head(h)
            mu, ls = out[:, :1], out[:, 1:].clamp(-5, 2)
            nll.append(gauss_nll(y[:, t:t + 1], mu, ls).squeeze(-1)); mus.append(mu.squeeze(-1))
            yp = y[:, t:t + 1]
        h = self.cell(self.inp(torch.cat([yp, torch.zeros_like(yp)], -1)), h)
        return dict(nll=torch.stack(nll, 1), kl=torch.zeros_like(torch.stack(nll, 1)), mu=torch.stack(mus, 1), feat=h)

    @torch.no_grad()
    def filter(self, a, y):
        B, T = a.shape
        h = a.new_zeros(B, self.H); yp = a.new_zeros(B, 1)
        mus, lss = [], []
        for t in range(T):
            h = self.cell(self.inp(torch.cat([yp, a[:, t:t + 1]], -1)), h)
            out = self.head(h); mus.append(out[:, 0]); lss.append(out[:, 1].clamp(-5, 2))
            yp = y[:, t:t + 1]
        return h, yp, torch.stack(mus, 1), torch.stack(lss, 1)

    @torch.no_grad()
    def rollout(self, h, yp, acts):
        mus = []
        for t in range(acts.shape[1]):
            h = self.cell(self.inp(torch.cat([yp, acts[:, t:t + 1]], -1)), h)
            mu = self.head(h)[:, :1]; mus.append(mu[:, 0]); yp = mu
        return torch.stack(mus, 1)

    @torch.no_grad()
    def step_state(self, h, yp, a_t):
        return self.cell(self.inp(torch.cat([yp, a_t[:, None]], -1)), h)

    def init_state(self, B, dev="cpu"):
        return torch.zeros(B, self.H, device=dev), torch.zeros(B, 1, device=dev)


class ClassifierGRU(nn.Module):
    """Supervised end-to-end mechanism classifier (control: label-supervised upper reference)."""

    def __init__(self, H=128, E=64, ncls=6):
        super().__init__()
        self.inp = nn.Sequential(nn.Linear(2, E), nn.ELU()); self.cell = nn.GRUCell(E, H)
        self.out = nn.Linear(H, ncls); self.H = H

    def forward(self, a, y):
        h = a.new_zeros(a.shape[0], self.H)
        for t in range(a.shape[1]):
            h = self.cell(self.inp(torch.cat([y[:, t:t + 1], a[:, t:t + 1]], -1)), h)
        return self.out(h)


def info_nce(e1, e2, tau=0.2):
    e1, e2 = F.normalize(e1, dim=-1), F.normalize(e2, dim=-1)
    logits = e1 @ e2.t() / tau
    tgt = torch.arange(e1.shape[0], device=e1.device)
    return 0.5 * (F.cross_entropy(logits, tgt) + F.cross_entropy(logits.t(), tgt))


class CondGRU(nn.Module):
    """Class-conditional deterministic latent dynamics: p(y_t | y_<t, a_<=t, class c). One network, one-hot class input.
    Used as a bank of learned per-class simulators (generative classifier + imagined interventional responses)."""

    def __init__(self, H=128, E=64, ncls=6):
        super().__init__()
        self.H, self.ncls = H, ncls
        self.inp = nn.Sequential(nn.Linear(2 + ncls, E), nn.ELU())
        self.cell = nn.GRUCell(E, H)
        self.head = nn.Sequential(nn.Linear(H, E), nn.ELU(), nn.Linear(E, 2))

    def _oh(self, c, dev=None):
        return F.one_hot(c.long(), self.ncls).float()

    def forward(self, a, y, c, **kw):
        B, T = a.shape
        oh = self._oh(c); h = a.new_zeros(B, self.H); yp = a.new_zeros(B, 1)
        nll, mus, lss = [], [], []
        for t in range(T):
            h = self.cell(self.inp(torch.cat([yp, a[:, t:t + 1], oh], -1)), h)
            out = self.head(h); mu, ls = out[:, :1], out[:, 1:].clamp(-5, 2)
            nll.append(gauss_nll(y[:, t:t + 1], mu, ls).squeeze(-1)); mus.append(mu.squeeze(-1)); lss.append(ls.squeeze(-1))
            yp = y[:, t:t + 1]
        return dict(nll=torch.stack(nll, 1), kl=torch.zeros(B, T), mu=torch.stack(mus, 1), ls=torch.stack(lss, 1), feat=h)

    @torch.no_grad()
    def filter(self, a, y, c):
        o = self.forward(a, y, c)
        B, T = a.shape
        oh = self._oh(c); h = a.new_zeros(B, self.H); yp = a.new_zeros(B, 1)
        for t in range(T):
            h = self.cell(self.inp(torch.cat([yp, a[:, t:t + 1], oh], -1)), h); yp = y[:, t:t + 1]
        return h, yp, o["mu"], o["ls"], o["nll"]

    @torch.no_grad()
    def rollout(self, h, yp, acts, c):
        oh = self._oh(c); mus = []
        for t in range(acts.shape[1]):
            h = self.cell(self.inp(torch.cat([yp, acts[:, t:t + 1], oh], -1)), h)
            mu = self.head(h)[:, :1]; mus.append(mu[:, 0]); yp = mu
        return torch.stack(mus, 1)
