"""Generative-world benchmark (gwb): batched partially observed generators.

Hidden state is simulated here but never exposed to learned agents; agents see only
(action a_t, noisy observation y_t).  Process is deterministic given actions; the
only randomness is observation noise (so the Bayesian oracle likelihood is exact).

Classes (6): family A (precision) 0 cont, 1 quant(q), 2 stiff(delta);
             family B (memory)    3 delay(d), 4 lag(tau), 5 reset(P).
Equivalence families (E): eqA = quant/stiff with threshold beyond actuator reach;
             eqB = delay(d>=horizon) vs reset(P=1): both give y == noise.
"""
from __future__ import annotations
import math
import torch

DT = 0.1
NCLS = 6
CLASS_NAMES = ["cont", "quant", "stiff", "delay", "lag", "reset"]
FAMILY_OF = [0, 0, 0, 1, 1, 1]
L_DEFAULT = 48


def simulate(cls, K, b, p, u):
    """cls[N] long, K,b,p[N], u[N,T] -> noiseless state trajectory x[N,T] (float64)."""
    N, T = u.shape
    cls = cls.long()
    x = torch.zeros(N, dtype=torch.float64)
    z = torch.zeros(N, dtype=torch.float64)
    out = torch.empty(N, T, dtype=torch.float64)
    pq = p.clamp_min(1e-6)
    alpha = (DT / pq).clamp(max=1.0)
    d = p.round().long().clamp_min(0)
    P = p.round().long().clamp_min(1)
    idx = torch.arange(N)
    for t in range(T):
        ut = u[:, t]
        ud = torch.where(t - d >= 0, u[idx, (t - d).clamp_min(0)], torch.zeros_like(ut))
        z = torch.where(cls == 4, z + alpha * (ut - z), z)
        ueff = torch.where(cls == 3, ud, torch.where(cls == 4, z, ut))
        v = x + DT * (-K * x + b * ueff)
        xq = pq * torch.round(v / pq)
        xs = torch.where((v - x).abs() >= pq, v, x)
        xn = torch.where(cls == 1, xq, torch.where(cls == 2, xs, v))
        xn = torch.where((cls == 5) & ((t + 1) % P == 0), torch.zeros_like(xn), xn)
        x = xn
        out[:, t] = x
    return out


def _lu(g, lo, hi, n):
    return torch.exp(torch.empty(n, dtype=torch.float64).uniform_(math.log(lo), math.log(hi), generator=g))


def _u(g, lo, hi, n):
    return torch.empty(n, dtype=torch.float64).uniform_(lo, hi, generator=g)


# parameter ranges per regime: (A threshold range, B delay set, B tau range, B reset range)
REGIMES = {
    "train": dict(q=(0.03, 0.09), d=(2, 3, 4, 5), tau=(0.25, 0.7), P=(12, 24)),
    "hoparam": dict(q=(0.09, 0.2), d=(6, 7), tau=(0.8, 1.2), P=(26, 36)),
}


def sample_instances(n, regime="train", family="both", sigma=(0.08, 0.2), seed=0, L=L_DEFAULT):
    """Return dict of instance tensors. regime: train|hoparam|eqA|eqB. 'label' -1 for equivalent worlds."""
    g = torch.Generator().manual_seed(seed)
    if regime == "eqA":
        fam = torch.zeros(n, dtype=torch.long)
    elif regime == "eqB":
        fam = torch.ones(n, dtype=torch.long)
    elif family == "A":
        fam = torch.zeros(n, dtype=torch.long)
    elif family == "B":
        fam = torch.ones(n, dtype=torch.long)
    else:
        fam = (torch.rand(n, generator=g) < 0.5).long()
    sub = torch.randint(0, 3, (n,), generator=g)
    cls = fam * 3 + sub
    K = _u(g, 0.3, 0.7, n)
    b = torch.where(fam == 0, _u(g, 0.8, 1.2, n), _u(g, 2.0, 3.0, n))
    p = torch.zeros(n, dtype=torch.float64)
    R = REGIMES["hoparam" if regime == "hoparam" else "train"]
    thr = _lu(g, *R["q"], n)
    ds = torch.tensor(R["d"], dtype=torch.float64)[torch.randint(0, len(R["d"]), (n,), generator=g)]
    tau = _u(g, *R["tau"], n)
    Pp = torch.randint(R["P"][0], R["P"][1] + 1, (n,), generator=g).double()
    p = torch.where((cls == 1) | (cls == 2), thr, p)
    p = torch.where(cls == 3, ds, p)
    p = torch.where(cls == 4, tau, p)
    p = torch.where(cls == 5, Pp, p)
    label = cls.clone()
    if regime == "eqA":
        # restrict to quant/stiff with thresholds beyond actuator reach DT*b*umax (<=0.12*... =0.12)
        cls = 1 + (torch.rand(n, generator=g) < 0.5).long()
        p = _lu(g, 0.35, 0.6, n)
        label = torch.full((n,), -1)
        b = _u(g, 0.8, 1.2, n)
    if regime == "eqB":
        cls = 3 + 2 * (torch.rand(n, generator=g) < 0.5).long()  # 3 delay or 5 reset
        p = torch.where(cls == 3, torch.full((n,), float(L + 10), dtype=torch.float64), torch.ones(n, dtype=torch.float64))
        label = torch.full((n,), -1)
    sig = _u(g, *sigma, n) if isinstance(sigma, tuple) else torch.full((n,), float(sigma), dtype=torch.float64)
    sig = sig * torch.where(fam == 1, 2.5, 1.0)  # family B has larger signal gain; noise scaled accordingly
    return dict(cls=cls, fam=fam, K=K, b=b, p=p, sigma=sig, label=label, regime=regime)


def take(inst, idx):
    return {k: (v[idx] if torch.is_tensor(v) else v) for k, v in inst.items()}


def observe(inst, u, g):
    """Noisy observation y[N,T] given actions u and generator g (noise stream)."""
    x = simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u)
    return x + inst["sigma"][:, None] * torch.randn(x.shape, generator=g, dtype=torch.float64), x


# ---------------- oracle hypothesis grid -------------------
THR_GRID = [0.03, 0.045, 0.07, 0.1, 0.15, 0.25, 0.4, 0.6]
HGRID = {
    0: [(0, 0.0)] + [(1, q) for q in THR_GRID] + [(2, q) for q in THR_GRID],
    1: [(3, float(d)) for d in (1, 2, 3, 4, 5, 6, 7, 8, 58)] + [(4, t) for t in (0.2, 0.35, 0.5, 0.7, 1.0, 1.3)]
       + [(5, float(P)) for P in (1, 8, 12, 16, 20, 24, 30, 36)],
}


def oracle_means(inst_fam_subset, u, fam):
    """Mean trajectories for every hypothesis in the family grid: [N, H, T], and class of each hyp."""
    hy = HGRID[fam]
    N = u.shape[0]
    outs = []
    for c, pv in hy:
        outs.append(simulate(torch.full((N,), c), inst_fam_subset["K"], inst_fam_subset["b"],
                             torch.full((N,), pv, dtype=torch.float64), u))
    return torch.stack(outs, 1), torch.tensor([c for c, _ in hy])


def oracle_class_posterior(inst, u, y, fam):
    """Exact Bayesian posterior over classes (uniform class prior, uniform within-class grid prior).
    Knows family, K, b, sigma.  inst/u/y restricted to one family."""
    m, hc = oracle_means(inst, u, fam)
    ll = -((y[:, None, :] - m) ** 2).sum(-1) / (2 * inst["sigma"][:, None] ** 2)
    prior = torch.zeros(len(hc), dtype=torch.float64)
    for c in hc.unique():
        sel = hc == c
        prior[sel] = 1.0 / (3 * sel.sum())
    lp = ll + prior.log()[None]
    post = torch.softmax(lp, 1)
    cp = torch.zeros(inst["K"].shape[0], NCLS, dtype=torch.float64)
    for c in hc.unique():
        cp[:, int(c)] = post[:, hc == c].sum(1)
    return cp


# Prior-matched oracle grid: hypotheses restricted to the TRAINING generator ranges (cannot explain eq worlds)
HGRID_MATCHED = {
    0: [(0, 0.0)] + [(1, q) for q in (0.03, 0.045, 0.06, 0.09)] + [(2, q) for q in (0.03, 0.045, 0.06, 0.09)],
    1: [(3, float(d)) for d in (2, 3, 4, 5)] + [(4, t) for t in (0.25, 0.4, 0.55, 0.7)] + [(5, float(P)) for P in (12, 15, 18, 21, 24)],
}


def oracle_class_posterior_matched(inst, u, y, fam):
    saved = dict(HGRID)
    try:
        HGRID.update(HGRID_MATCHED)
        return oracle_class_posterior(inst, u, y, fam)
    finally:
        HGRID.clear(); HGRID.update(saved)
