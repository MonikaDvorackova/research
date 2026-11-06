"""Independent benchmark for out-of-language discovery (OOL).  The mechanisms are declared in manifest.json (frozen; sha256 recorded in the
results); this module is a generic evaluator that knows nothing about the agent's hypothesis language.  The agent sees only World.run(U)."""
from __future__ import annotations
import json, os, hashlib
import numpy as np

HERE = os.path.dirname(__file__)
DT, T, SUB = 0.1, 80, 4
B1, G = 1.6, 1.5
SIG, SIGP = 0.03, 0.02
MAN = json.load(open(os.path.join(HERE, "manifest.json")))
MAN_SHA = hashlib.sha256(open(os.path.join(HERE, "manifest.json"), "rb").read()).hexdigest()
FAM = MAN["families"]
SPLITS = {s: [f for f, v in FAM.items() if s in v["split"]] for s in ("calib", "dev", "holdout")}
_ENV = dict(sin=np.sin, exp=np.exp, tanh=np.tanh, sqrt=np.sqrt, abs=np.abs, sign=np.sign, floor=np.floor,
            relu=lambda v: max(v, 0.0), step=lambda v: 1.0 if v > 0 else 0.0)


def make_instance(fam, rng):
    spec = FAM[fam]; u = rng.uniform
    inst = dict(fam=fam, a=u(1.2, 1.8), b3=u(1.2, 1.8), e=u(0.4, 0.6), d=u(1.2, 1.8), c=u(1.5, 2.5), P={}, k=0, tau=0.0)
    for n, (lo, hi) in spec["params"].items(): inst["P"][n] = float(u(lo, hi))
    if "delay" in spec: inst["k"] = int(rng.integers(spec["delay"][0], spec["delay"][1] + 1))
    if "tau" in spec: inst["tau"] = float(u(*spec["tau"]))
    return inst


def _code(fam): return compile(FAM[fam]["expr"], f"<{fam}>", "eval")


def simulate(inst, U, rng=None, noise=1.0):
    """U [T,2] -> (Y [T,3] = (x1,x3,x4) noisy iff rng, x3_clean [T], x2n [T] privileged hidden-state readout d*x2)."""
    Tn = len(U); h = DT / SUB; sq = np.sqrt(h); code = _code(inst["fam"])
    a, b3, e, d, c, k, tau = inst["a"], inst["b3"], inst["e"], inst["d"], inst["c"], inst["k"], inst["tau"]
    ns = dict(_ENV, **inst["P"])
    x1 = x2 = x3 = x4 = z = 0.0; hist = np.zeros(Tn + 1); Y = np.zeros((Tn, 3)); x3c = np.zeros(Tn); x2c = np.zeros(Tn)
    for t in range(Tn):
        xd0 = -B1 * x1 + G * U[t, 0]
        for _ in range(SUB):
            xd = -B1 * x1 + G * U[t, 0]; x1 += h * xd
            if tau > 0: z += h * (x1 - z) / tau
            ns["x"], ns["xd"], ns["z"], ns["x2"] = x1, xd, z, x2
            ns["xdel"] = hist[t + 1 - k] if (k and t + 1 - k > 0) else 0.0
            phi = float(eval(code, {"__builtins__": {}}, ns))
            x2 += h * (-a * x2 + c * phi + e * U[t, 1]) + (sq * SIGP * noise * rng.standard_normal() if rng is not None else 0.0)
            x3 += h * (-b3 * x3 + d * x2)
            x4 += h * (-0.5 * x4) + (sq * 0.3 * rng.standard_normal() if rng is not None else 0.0)
        hist[t + 1] = x1; x3c[t] = x3; x2c[t] = d * x2; Y[t] = (x1, x3, x4)
    if rng is not None: Y = Y + SIG * noise * rng.standard_normal(Y.shape)
    return Y, x3c, x2c


class World:
    """What the agent may touch: run a programme, receive noisy observations.  Counts experiments."""
    def __init__(self, inst, iseed, noise=1.0):
        self._inst, self._seed, self._noise = inst, iseed, noise; self.n_runs = 0
    def run(self, U, tag):
        self.n_runs += 1
        return simulate(self._inst, U, np.random.default_rng([self._seed, tag]), self._noise)[0]


def reach(): return G / B1
