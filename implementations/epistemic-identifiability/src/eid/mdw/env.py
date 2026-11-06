"""Mechanism-discovery world (MDW): hidden 3-D nonlinear system with two actuators; the unknown is the coupling phi(x1) feeding the
hidden variable x2.  Training families: lin, sat, delay.  Held-out constructions: gate (hybrid), backlash (memory)."""
from __future__ import annotations
import numpy as np
import torch

DT, T = 0.1, 60
B1, G, A, E, B3, D, SIG = 1.6, 1.5, 1.5, 0.5, 1.5, 1.5, 0.03
TRAIN_FAMS = ("lin", "sat", "delay")
HELD_FAMS = ("gate", "backlash")
FAM_ID = {"lin": 0, "sat": 1, "delay": 2, "gate": 3, "backlash": 4}


def sample_instances(fams, n, seed):
    """n instances per family: dict(fam [N] long, c, par [N]) where par = s | k | theta | w (0 for lin)."""
    g = torch.Generator().manual_seed(seed)
    F, C, P = [], [], []
    for f in fams:
        F += [FAM_ID[f]] * n
        C.append(1.5 + torch.rand(n, generator=g, dtype=torch.float64))
        lo, hi = dict(lin=(0, 0), sat=(0.25, 0.8), delay=(3, 9), gate=(0.2, 0.7), backlash=(0.15, 0.5))[f]
        p = lo + (hi - lo) * torch.rand(n, generator=g, dtype=torch.float64)
        P.append(torch.round(p) if f == "delay" else p)
    return dict(fam=torch.tensor(F), c=torch.cat(C), par=torch.cat(P))


def simulate(inst, U, eps=None):
    """U [N,T,2] actions in [-1,1]; returns noiseless (x1,x3) [N,T,2] and, if eps given, noisy obs. Optionally returns x2."""
    N, Tn, _ = U.shape
    fam, c, par = inst["fam"], inst["c"], inst["par"]
    x1 = torch.zeros(N, dtype=torch.float64); x2 = x1.clone(); x3 = x1.clone(); z = x1.clone()
    hist = torch.zeros(N, Tn + 1, dtype=torch.float64)
    out = torch.empty(N, Tn, 2, dtype=torch.float64); idx = torch.arange(N)
    k = par.round().long().clamp(0, Tn)
    for t in range(Tn):
        x1 = x1 + DT * (-B1 * x1 + G * U[:, t, 0]); hist[:, t + 1] = x1
        z = torch.minimum(torch.maximum(z, x1 - par), x1 + par)                     # play operator (backlash)
        delayed = hist[idx, (t + 1 - k).clamp(min=0)] * ((t + 1 - k) > 0)
        phi = torch.where(fam == 0, x1, torch.where(fam == 1, par * torch.tanh(x1 / par.clamp_min(1e-6)),
              torch.where(fam == 2, delayed, torch.where(fam == 3, x1 * (x1 > par), z))))
        x2 = x2 + DT * (-A * x2 + c * phi + E * U[:, t, 1])
        x3 = x3 + DT * (-B3 * x3 + D * x2)
        out[:, t, 0], out[:, t, 1] = x1, x3
    return out if eps is None else out + SIG * eps


# ---------------- probe programmes and descriptors ----------------
def probe_programmes():
    tri = torch.cat([torch.linspace(0, 1, T // 2), torch.linspace(1, 0, T - T // 2)]).double()
    P = {"small": torch.full((T,), 0.25, dtype=torch.float64), "large": torch.ones(T, dtype=torch.float64),
         "neg": -torch.ones(T, dtype=torch.float64), "tri": tri}
    return {k: torch.stack([v, torch.zeros(T, dtype=torch.float64)], -1) for k, v in P.items()}      # [T,2]


PROBES = probe_programmes()
PROBE_ORDER = ("large", "small", "neg", "tri")
DESC_NAMES = ("nl", "asym", "lat", "hyst")


def descriptors_from_x3(x3):
    """x3: dict probe-> [N,T] trajectories (true noiseless, noisy-observed or predicted). Smooths the last 3 samples for R."""
    R = {k: v[:, -3:].mean(1) for k, v in x3.items()}
    big = R["large"]; den = torch.where(big.abs() < 1e-3, torch.full_like(big, 1e-3), big)
    sm = lambda v: torch.nn.functional.avg_pool1d(v[:, None], 3, 1, padding=1, count_include_pad=False)[:, 0]
    xl = sm(x3["large"]); crossed = (xl > 0.1 * den[:, None]).float()
    lat = torch.where(crossed.sum(1) > 0, crossed.argmax(1).double(), torch.full_like(den, float(T)))
    return torch.stack([4 * R["small"] / den, -R["neg"] / den, lat, x3["tri"][:, -3:].mean(1) / den], 1)


def true_descriptors(inst):
    N = inst["c"].shape[0]
    x3 = {k: simulate(inst, p[None].expand(N, -1, -1))[..., 1] for k, p in PROBES.items()}
    return descriptors_from_x3(x3)


_ref = sample_instances(TRAIN_FAMS, 400, 20000)
_td = true_descriptors(_ref)
DESC_MEAN = _td.mean(0)
DESC_SD = torch.maximum(_td.std(0), torch.tensor([0.05, 0.25, 1.0, 0.05], dtype=torch.float64))   # fixed on TRAINING families; floor on asym (zero variance in-family)


def norm_err(est, true):
    return ((est - true).abs() / DESC_SD)


# ---------------- action programmes ----------------
def random_programmes(N, g, kinds=("const", "step", "tri", "smooth", "pulse")):
    out = torch.zeros(N, T, 2, dtype=torch.float64)
    which = torch.randint(0, len(kinds), (N,), generator=g)
    tt = torch.arange(T).double()
    for i in range(N):
        kd = kinds[int(which[i])]
        if kd == "const": u = torch.full((T,), float(torch.rand(1, generator=g) * 2 - 1), dtype=torch.float64)
        elif kd == "step":
            t0 = int(torch.randint(5, 40, (1,), generator=g)); a, b = (torch.rand(2, generator=g) * 2 - 1).tolist()
            u = torch.where(tt < t0, torch.tensor(a, dtype=torch.float64), torch.tensor(b, dtype=torch.float64))
        elif kd == "tri":
            pk = float(torch.rand(1, generator=g) * 2 - 1); h = int(torch.randint(15, 45, (1,), generator=g))
            u = torch.cat([torch.linspace(0, pk, h), torch.linspace(pk, 0, T - h)]).double()
        elif kd == "smooth":
            e = torch.randn(T, generator=g, dtype=torch.float64); u = torch.zeros(T, dtype=torch.float64); cur = 0.0
            for t in range(T): cur = 0.9 * cur + 0.35 * float(e[t]); u[t] = cur
            u = u.clamp(-1, 1)
        else:
            u = (torch.rand(T, generator=g, dtype=torch.float64) < 0.12).double() * (torch.rand(T, generator=g, dtype=torch.float64) * 2 - 1)
        out[i, :, 0] = u
    inj = (torch.rand(N, generator=g, dtype=torch.float64) < 0.3).double() * (torch.rand(N, generator=g, dtype=torch.float64) * 2 - 1) * 0.5
    out[:, :, 1] = inj[:, None]
    return out


def candidate_programmes():
    """Fixed candidate experiment set for planners (8): the 4 probes + 4 others (u2 injection included)."""
    tt = torch.arange(T).double()
    c = [PROBES[k] for k in PROBE_ORDER]
    c.append(torch.stack([torch.full((T,), 0.6, dtype=torch.float64), torch.zeros(T, dtype=torch.float64)], -1))
    c.append(torch.stack([torch.where(tt < 25, torch.tensor(1.0, dtype=torch.float64), torch.tensor(-1.0, dtype=torch.float64)), torch.zeros(T, dtype=torch.float64)], -1))
    c.append(torch.stack([(tt % 12 < 3).double() * 1.0, torch.zeros(T, dtype=torch.float64)], -1))
    c.append(torch.stack([torch.zeros(T, dtype=torch.float64), torch.full((T,), 1.0, dtype=torch.float64)], -1))
    return torch.stack(c)                                                        # [8,T,2]


CANDS = candidate_programmes()
