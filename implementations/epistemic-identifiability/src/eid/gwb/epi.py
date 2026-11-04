"""Epistemic benchmark extension: instances with controlled epistemic status.

Categories (agent never sees them): id, idnoisy (budget-limited), eqA/eqB/eqC/eqD (exact interventional equivalence from four
qualitatively different sources), approx (near-equivalent), ooc_sat/ooc_osc/ooc_qd (outside the six-class hypothesis class).
Inst dict extends gen's with 'cat' (str), 'eqmask' [N,6] (classes interventionally equivalent to the truth; zeros if out-of-class).
"""
from __future__ import annotations
import torch
from . import gen

DT = gen.DT
EQ_SOURCES = ("eqA", "eqB", "eqC", "eqD")
OOC = ("ooc_sat", "ooc_osc", "ooc_qd")
# oracle grids that include the degenerate members needed to represent the new equivalence sources
HGRID_EPI = {
    0: list(gen.HGRID[0]),
    1: list(gen.HGRID[1]) + [(3, 0.0), (4, 0.05)],
}


def _onehot(cls):
    return torch.nn.functional.one_hot(cls.long(), gen.NCLS).bool()


def simulate_ooc(kind, K, b, p, u):
    N, T = u.shape
    x = torch.zeros(N, dtype=torch.float64); v = torch.zeros(N, dtype=torch.float64)
    out = torch.empty(N, T, dtype=torch.float64)
    for t in range(T):
        ut = u[:, t]
        if kind == "ooc_sat":          # saturating actuator on continuous dynamics
            x = x + DT * (-K * x + b * 0.3 * torch.tanh(ut / 0.3))
        elif kind == "ooc_osc":        # underdamped second-order response (hidden velocity)
            v = v + DT * (-0.4 * v - 4.0 * x + 4.0 * b * ut)
            x = x + DT * v
        elif kind == "ooc_qd":         # composite: delay 3 AND quantisation 0.06 (two mechanisms at once)
            ud = u[:, t - 3] if t >= 3 else torch.zeros_like(ut)
            vv = x + DT * (-K * x + b * ud)
            x = 0.06 * torch.round(vv / 0.06)
        else:
            raise ValueError(kind)
        out[:, t] = x
    return out


def sample_epi(n, kind, seed, L=gen.L_DEFAULT):
    g = torch.Generator().manual_seed(seed)
    if kind in ("id", "idnoisy"):
        inst = gen.sample_instances(n, "train", seed=seed)
        if kind == "idnoisy":
            inst["sigma"] = inst["sigma"] * 3.0
        inst["eqmask"] = _onehot(inst["cls"])
    elif kind in ("eqA", "eqB"):
        inst = gen.sample_instances(n, kind, seed=seed)
        inst["eqmask"] = torch.zeros(n, gen.NCLS, dtype=torch.bool)
        inst["eqmask"][:, [1, 2] if kind == "eqA" else [3, 5]] = True
    elif kind == "eqC":                 # lag with tau < dt  (alpha clipped to 1)  ==  delay 0
        base = gen.sample_instances(n, "train", family="B", seed=seed)
        pick = torch.rand(n, generator=g) < 0.5
        base["cls"] = torch.where(pick, torch.full((n,), 3), torch.full((n,), 4))
        base["p"] = torch.where(pick, torch.zeros(n, dtype=torch.float64), torch.full((n,), 0.05, dtype=torch.float64))
        base["label"] = torch.full((n,), -1)
        base["eqmask"] = torch.zeros(n, gen.NCLS, dtype=torch.bool); base["eqmask"][:, [3, 4]] = True
        inst = base
    elif kind == "eqD":                 # null actuation b = 0: every class of the family is identical
        base = gen.sample_instances(n, "train", seed=seed)
        base["b"] = torch.zeros(n, dtype=torch.float64)
        base["label"] = torch.full((n,), -1)
        m = torch.zeros(n, gen.NCLS, dtype=torch.bool)
        for i in range(n):
            m[i, :3] = base["fam"][i] == 0
            m[i, 3:] = base["fam"][i] == 1
        base["eqmask"] = m; inst = base
    elif kind == "approx":              # threshold at 60-95 % of actuator reach: distinguishable only near saturation
        base = gen.sample_instances(n, "train", family="A", seed=seed)
        sub = 1 + (torch.rand(n, generator=g) < 0.5).long()
        r = 0.6 + 0.35 * torch.rand(n, generator=g, dtype=torch.float64)
        reach = DT * base["b"] * 1.0
        base["cls"] = sub
        base["p"] = torch.where(sub == 1, 2 * reach * r, reach * r)
        base["label"] = sub.clone(); base["eqmask"] = _onehot(sub); inst = base
    elif kind in OOC:
        base = gen.sample_instances(n, "train", seed=seed)
        base["label"] = torch.full((n,), -2)
        base["eqmask"] = torch.zeros(n, gen.NCLS, dtype=torch.bool); inst = base
    else:
        raise ValueError(kind)
    inst["cat"] = kind
    return inst


def x_of(inst, u):
    if inst["cat"] in OOC:
        return simulate_ooc(inst["cat"], inst["K"], inst["b"], inst["p"], u)
    return gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u)


def observe_epi(inst, u, eps):
    return u, x_of(inst, u) + inst["sigma"][:, None] * eps


class EpiGrid:
    """Context manager: temporarily swap the oracle hypothesis grid to the epistemic grid."""
    def __enter__(self):
        self.saved = {k: list(v) for k, v in gen.HGRID.items()}
        gen.HGRID.update({k: list(v) for k, v in HGRID_EPI.items()}); return self

    def __exit__(self, *a):
        gen.HGRID.clear(); gen.HGRID.update(self.saved)


def max_divergence(inst, hyp_cls, hyp_p, u_progs):
    """Privileged distinguishability: max over programs of ||x_true - x_hyp||^2 / sigma^2 (noise-normalised, whole episode)."""
    N = inst["K"].shape[0]; best = torch.zeros(N, dtype=torch.float64)
    for u in u_progs:
        xt = x_of(inst, u.expand(N, -1) if u.shape[0] == 1 else u)
        xh = gen.simulate(torch.full((N,), hyp_cls), inst["K"], inst["b"], torch.full((N,), hyp_p, dtype=torch.float64),
                          u.expand(N, -1) if u.shape[0] == 1 else u)
        best = torch.maximum(best, ((xt - xh) ** 2).sum(-1) / inst["sigma"] ** 2)
    return best
