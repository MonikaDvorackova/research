"""Data-collection policies, descriptor estimators (direct probing, ridge NARX SysID, declared-class Bayes grid, meta-trained world
model ensemble, supervised regressor) for MDW."""
from __future__ import annotations
import itertools
import numpy as np
import torch
from . import env

T = env.T
DM, DS = env.DESC_MEAN, env.DESC_SD


# ---------------- trajectories ----------------
def run_programmes(inst, progs, eps):
    """progs [N,T,2], eps [N,T,2] -> noisy obs [N,T,2]"""
    return env.simulate(inst, progs, eps)


def sweep_programmes(N, B):
    return torch.stack([env.PROBES[env.PROBE_ORDER[i % 4]][None].expand(N, -1, -1) for i in range(B)], 1)    # [N,B,T,2]


def collect_fixed(inst, progs_all, eps_all, B):
    Y = torch.stack([run_programmes(inst, progs_all[:, i], eps_all[:, i]) for i in range(B)], 1)
    return progs_all[:, :B], Y


# ---------------- descriptor helpers ----------------
def partial_descriptors(x3_by_probe):
    """x3_by_probe: dict probe -> [N,T] or None (missing).  Returns est [N,4] with prior mean for descriptors lacking probes."""
    N = next(v.shape[0] for v in x3_by_probe.values() if v is not None)
    est = DM[None].repeat(N, 1).clone()
    L = x3_by_probe["large"]
    if L is None: return est
    full = {k: (v if v is not None else torch.zeros_like(L)) for k, v in x3_by_probe.items()}
    d = env.descriptors_from_x3(full)
    est[:, 2] = d[:, 2]                                                      # lat needs only 'large'
    if x3_by_probe["small"] is not None: est[:, 0] = d[:, 0]
    if x3_by_probe["neg"] is not None: est[:, 1] = d[:, 1]
    if x3_by_probe["tri"] is not None: est[:, 3] = d[:, 3]
    return est


def est_direct(U, Y):
    """Direct probing from sweep data: average observed x3 over replicates of each probe."""
    N, B = U.shape[:2]; acc = {k: [] for k in env.PROBE_ORDER}
    for i in range(B): acc[env.PROBE_ORDER[i % 4]].append(Y[:, i, :, 1])
    return partial_descriptors({k: (torch.stack(v).mean(0) if v else None) for k, v in acc.items()})


# ---------------- generic SysID (ridge NARX) ----------------
NL, UL = 3, 10


def _base(prev_obs, uhist):
    """prev_obs: [N,NL,2] most-recent-first; uhist [N,UL,2]; -> [N,18]"""
    return torch.cat([prev_obs[:, :, 0], prev_obs[:, :, 1], uhist[:, :, 0], uhist[:, :2, 1]], 1)


def _poly(b):
    iu = torch.triu_indices(b.shape[1], b.shape[1])
    return torch.cat([torch.ones(b.shape[0], 1, dtype=b.dtype), b, (b[:, :, None] * b[:, None, :])[:, iu[0], iu[1]]], 1)


def est_sysid(U, Y, lam=1.0):
    N, B = U.shape[:2]
    Xs, Ys = [], []
    for i in range(B):
        u, y = U[:, i], Y[:, i]
        up = torch.cat([torch.zeros(N, UL, 2, dtype=u.dtype), u], 1); yp = torch.cat([torch.zeros(N, NL, 2, dtype=y.dtype), y], 1)
        for t in range(T):
            prev = yp[:, t:t + NL].flip(1); uh = up[:, t + 1:t + UL + 1].flip(1)
            Xs.append(_poly(_base(prev, uh))); Ys.append(y[:, t])
    X = torch.stack(Xs, 1); Yt = torch.stack(Ys, 1)                           # [N,M,F], [N,M,2]
    F = X.shape[2]; A = X.transpose(1, 2) @ X + lam * torch.eye(F, dtype=X.dtype)
    W = torch.linalg.solve(A, X.transpose(1, 2) @ Yt)                          # [N,F,2]
    x3 = {}
    for k, p in env.PROBES.items():
        up = torch.cat([torch.zeros(N, UL, 2, dtype=torch.float64), p[None].expand(N, -1, -1)], 1)
        prev = torch.zeros(N, NL, 2, dtype=torch.float64); out = []
        for t in range(T):
            uh = up[:, t + 1:t + UL + 1].flip(1)
            pred = (_poly(_base(prev, uh))[:, None] @ W).squeeze(1).clamp(-6, 6)
            out.append(pred[:, 1]); prev = torch.cat([pred[:, None], prev[:, :-1]], 1)
        x3[k] = torch.stack(out, 1)
    return env.descriptors_from_x3(x3)


# ---------------- declared-class Bayes grid ----------------
def _grid():
    hyp = [("lin", 0.0, c) for c in (1.5, 2.0, 2.5)] + [("sat", s, c) for s in (0.3, 0.5, 0.8) for c in (1.5, 2.0, 2.5)] + \
          [("delay", float(k), c) for k in (3, 5, 7, 9) for c in (1.5, 2.0, 2.5)]
    return dict(fam=torch.tensor([env.FAM_ID[h[0]] for h in hyp]), par=torch.tensor([h[1] for h in hyp], dtype=torch.float64),
                c=torch.tensor([h[2] for h in hyp], dtype=torch.float64))


GRID = _grid(); HN = GRID["c"].shape[0]
GRID_DESC = env.true_descriptors(GRID)                                          # [HN,4]
GRID_CAND_X3 = torch.stack([env.simulate(GRID, env.CANDS[j][None].expand(HN, -1, -1))[..., 1] for j in range(env.CANDS.shape[0])], 1)   # [HN,8,T]


def bayes_post(U, Y):
    """log-lik of all grid hypotheses given episodes; returns posterior [N,HN], chi2 per obs of best hypothesis [N]."""
    N, B = U.shape[:2]; ll = torch.zeros(N, HN, dtype=torch.float64)
    inst_rep = {k: v.repeat_interleave(1, 0) for k, v in GRID.items()}
    for i in range(B):
        sims = torch.stack([env.simulate(GRID, U[n, i][None].expand(HN, -1, -1)) for n in range(N)])    # [N,HN,T,2]
        ll += -((Y[:, i][:, None] - sims) ** 2).sum((2, 3)) / (2 * env.SIG ** 2)
    post = torch.softmax(ll, 1)
    chi2 = (-2 * ll.max(1).values) / (B * T * 2)
    return post, chi2


def bayes_est(U, Y):
    post, chi2 = bayes_post(U, Y)
    return post @ GRID_DESC, chi2, post


def bayes_choose(post):
    """next experiment: max posterior-weighted predictive variance of x3 among candidates."""
    m = torch.einsum("nh,hct->nct", post, GRID_CAND_X3)
    var = torch.einsum("nh,nhct->nc", post, (GRID_CAND_X3[None] - m[:, None]) ** 2)
    return var.argmax(1)


# ---------------- meta-trained world model ensemble ----------------
@torch.no_grad()
def wm_desc(models, U, Y):
    """Descriptors by imagination, per ensemble member; returns [M,N,4] and also per-member contexts handled internally."""
    N, B = U.shape[:2]
    out = []
    for m in models:
        h = m.encode(U.reshape(N, B * T, 2).float(), Y.reshape(N, B * T, 2).float(), T) if B > 0 else torch.zeros(N, m.H)
        x3 = {k: m.imagine(h, p.float()[None].expand(N, -1, -1), T)[..., 1].double() for k, p in env.PROBES.items()}
        out.append(env.descriptors_from_x3(x3))
    return torch.stack(out)


@torch.no_grad()
def wm_choose(models, U, Y):
    """Plan2Explore-style criterion: candidate experiment with max ensemble disagreement of predicted x3 trajectories."""
    N, B = U.shape[:2]; C = env.CANDS.shape[0]; preds = []
    for m in models:
        h = m.encode(U.reshape(N, B * T, 2).float(), Y.reshape(N, B * T, 2).float(), T) if B > 0 else torch.zeros(N, m.H)
        hh = h[:, None].expand(N, C, -1).reshape(N * C, -1); pr = env.CANDS.float()[None].expand(N, -1, -1, -1).reshape(N * C, T, 2)
        preds.append(m.imagine(hh, pr, T)[..., 1].reshape(N, C, T))
    P = torch.stack(preds); return P.var(0, unbiased=False).mean(-1).argmax(1)


@torch.no_grad()
def reg_desc(regs, U, Y):
    N, B = U.shape[:2]
    out = [m.predict_desc(m.encode(U.reshape(N, B * T, 2).float(), Y.reshape(N, B * T, 2).float(), T)).double() * DS + DM for m in regs]
    return torch.stack(out).mean(0)


# ---------------- interventional prediction on UNSEEN programmes (what a world model is for) ----------------
def sysid_fit(U, Y, lam=0.1):
    N, B = U.shape[:2]; Xs, Ys = [], []
    for i in range(B):
        u, y = U[:, i], Y[:, i]
        up = torch.cat([torch.zeros(N, UL, 2, dtype=u.dtype), u], 1); yp = torch.cat([torch.zeros(N, NL, 2, dtype=y.dtype), y], 1)
        for t in range(T):
            Xs.append(_poly(_base(yp[:, t:t + NL].flip(1), up[:, t + 1:t + UL + 1].flip(1)))); Ys.append(y[:, t])
    X = torch.stack(Xs, 1); Yt = torch.stack(Ys, 1); F = X.shape[2]
    return torch.linalg.solve(X.transpose(1, 2) @ X + lam * torch.eye(F, dtype=X.dtype), X.transpose(1, 2) @ Yt)


def sysid_rollout(W, progs):
    """progs [P,T,2] shared by all instances -> predicted x3 [N,P,T]."""
    N, P = W.shape[0], progs.shape[0]; res = []
    for j in range(P):
        up = torch.cat([torch.zeros(N, UL, 2, dtype=torch.float64), progs[j][None].expand(N, -1, -1)], 1)
        prev = torch.zeros(N, NL, 2, dtype=torch.float64); out = []
        for t in range(T):
            pred = (_poly(_base(prev, up[:, t + 1:t + UL + 1].flip(1)))[:, None] @ W).squeeze(1).clamp(-6, 6)
            out.append(pred[:, 1]); prev = torch.cat([pred[:, None], prev[:, :-1]], 1)
        res.append(torch.stack(out, 1))
    return torch.stack(res, 1)


@torch.no_grad()
def wm_rollout(models, U, Y, progs):
    N, B = U.shape[:2]; P = progs.shape[0]; outs = []
    for m in models:
        h = m.encode(U.reshape(N, B * T, 2).float(), Y.reshape(N, B * T, 2).float(), T) if B > 0 else torch.zeros(N, m.H)
        hh = h[:, None].expand(N, P, -1).reshape(N * P, -1); pr = progs.float()[None].expand(N, -1, -1, -1).reshape(N * P, T, 2)
        outs.append(m.imagine(hh, pr, T)[..., 1].reshape(N, P, T).double())
    return torch.stack(outs).mean(0)
