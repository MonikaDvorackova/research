"""Structural discovery world (SDW): hidden x2, observed x1 (actuator), x3 (readout), nuisance x4.  The unknown is the construction of the
coupling feeding the hidden variable x2.  See topics/.../19-structural-discovery-framework-and-protocol.md for the protocol."""
from __future__ import annotations
import numpy as np

DT, T, SUB = 0.1, 80, 4
B1, G = 1.6, 1.5
SIG, SIGP = 0.03, 0.02
REACH = G / B1                                    # sup |x1| for |u1| <= 1
KNOWN = ("lin", "sat", "delay")                   # families seen by the declared-class baseline and the learned estimator
UNFAMILIAR = ("quad", "gate", "backlash", "fb")   # in-language, outside the declared class
INLANG = KNOWN + UNFAMILIAR
OOL = "osc"                                       # outside the hypothesis language
EQUIV = "unreach"                                 # interventionally equivalent to no coupling (S1)
ALL_FAMS = INLANG + (OOL, EQUIV)


def make_instance(fam, rng):
    u = rng.uniform
    inst = dict(fam=fam, a=u(1.2, 1.8), b3=u(1.2, 1.8), e=u(0.4, 0.6), d=u(1.2, 1.8), c=u(1.5, 2.5), par=0.0, kappa=0.0, om=0.0, ze=0.0)
    if fam == "sat": inst["par"] = u(0.25, 0.8)
    elif fam == "delay": inst["par"] = float(rng.integers(3, 10))
    elif fam == "gate": inst["par"] = u(0.2, 0.7)
    elif fam == "backlash": inst["par"] = u(0.15, 0.5)
    elif fam == "fb": inst["kappa"] = u(0.15, 0.5)
    elif fam == "osc": inst["om"], inst["ze"] = u(2.5, 4.0), 0.15
    elif fam == "unreach": inst["par"] = u(1.1, 1.5)
    elif fam not in ("lin", "quad"): raise ValueError(fam)
    return inst


def simulate(inst, U, rng=None):
    """U [T,2]. Returns (y [T,3] observations (x1,x3,x4) [noisy iff rng], x3 [T], x2n = d*x2 [T] (privileged; used only by oracle/training/scoring)).  rng=None -> no process/obs noise."""
    Tn = len(U); h = DT / SUB; sq = np.sqrt(h)
    fam, a, b3, e, d, c, par = inst["fam"], inst["a"], inst["b3"], inst["e"], inst["d"], inst["c"], inst["par"]
    x1 = x2 = x3 = x4 = z = x5 = v = 0.0
    hist = np.zeros(Tn + 1); Y = np.zeros((Tn, 3)); x3c = np.zeros(Tn); x2c = np.zeros(Tn)
    kk = int(round(par)) if fam == "delay" else 0
    w2 = inst["om"] ** 2
    for t in range(Tn):
        for _ in range(SUB):
            x1 += h * (-B1 * x1 + G * U[t, 0])
            if fam == "backlash": z = min(max(z, x1 - par), x1 + par)
            if fam == "osc":
                v += h * (-w2 * x5 - 2 * inst["ze"] * inst["om"] * v + w2 * x1); x5 += h * v
            if fam in ("lin", "fb"): phi = x1
            elif fam == "sat": phi = par * np.tanh(x1 / par)
            elif fam == "quad": phi = x1 * x1
            elif fam == "delay": phi = hist[t + 1 - kk] if t + 1 - kk > 0 else 0.0
            elif fam in ("gate", "unreach"): phi = x1 if x1 > par else 0.0
            elif fam == "backlash": phi = z
            else: phi = x5                                                            # osc
            dx2 = -a * x2 + c * phi + e * U[t, 1]
            if fam == "fb": dx2 -= inst["kappa"] * x2 ** 3
            x2 += h * dx2 + (sq * SIGP * rng.standard_normal() if rng is not None else 0.0)
            x3 += h * (-b3 * x3 + d * x2)
            x4 += h * (-0.5 * x4) + (sq * 0.3 * rng.standard_normal() if rng is not None else 0.0)
        hist[t + 1] = x1; x3c[t] = x3; x2c[t] = d * x2
        Y[t] = (x1, x3, x4)
    if rng is not None: Y = Y + SIG * rng.standard_normal(Y.shape)
    return Y, x3c, x2c


# ---------------------------------------------------------------- programmes
def _u(u1, u2=None):
    out = np.zeros((T, 2)); out[:, 0] = u1
    if u2 is not None: out[:, 1] = u2
    return out


_t = np.arange(T)
_step = lambda lo, hi, t0=T // 2: np.where(_t < t0, lo, hi).astype(float)
_tri = lambda pk: np.concatenate([np.linspace(0, pk, T // 2), np.linspace(pk, 0, T - T // 2)])
_pulse = lambda amp, per, duty: amp * ((_t % per) < duty * per).astype(float)
_sine = lambda amp, per: amp * np.sin(2 * np.pi * _t / per)
_sq = lambda amp, per: amp * np.where((_t % per) < per // 2, 1.0, -1.0)

POOL_NAMES = ["u1 +1", "u1 -1", "u1 +0.4", "u1 -0.4", "u1 +0.15", "u1 step 1>-1", "u1 step -1>1", "u1 step 0.3>1", "u1 tri +", "u1 tri -",
              "u1 pulse p16", "u1 pulse -p30", "u1 sine 1/30", "u1 sine .6/14", "u1 ramp up", "u1 ramp down", "u2 +1", "u2 -1", "u2 square",
              "combo u1+1,u2+.7", "combo u1+1,u2-.7", "combo sine+sq", "combo u1-1,u2+.7", "combo step+pulse"]
POOL = [_u(np.ones(T)), _u(-np.ones(T)), _u(np.full(T, .4)), _u(np.full(T, -.4)), _u(np.full(T, .15)),
        _u(_step(1, -1)), _u(_step(-1, 1)), _u(_step(.3, 1)), _u(_tri(1)), _u(_tri(-1)),
        _u(_pulse(1, 16, .25)), _u(_pulse(-1, 30, .25)), _u(_sine(1, 30)), _u(_sine(.6, 14)),
        _u(np.linspace(0, 1, T)), _u(np.linspace(1, -1, T)), _u(0 * _t, np.ones(T)), _u(0 * _t, -np.ones(T)), _u(0 * _t, _sq(1, 20)),
        _u(np.ones(T), np.full(T, .7)), _u(np.ones(T), np.full(T, -.7)), _u(_sine(1, 30), _sq(.7, 20)), _u(-np.ones(T), np.full(T, .7)),
        _u(_step(.3, 1), _pulse(.8, 16, .25))]
IDX = {n: i for i, n in enumerate(POOL_NAMES)}
E0 = _u(0 * _t, _sq(.5, 20))                           # shared skeleton episode (u2 only, low amplitude)
E1 = POOL[IDX["u1 +1"]]                                # shared large u1 step
SWEEP_A = [IDX[n] for n in ["u1 -1", "u1 +0.4", "u1 step 1>-1", "u1 tri +", "u1 pulse p16", "u1 sine 1/30", "u2 +1", "u2 square", "combo u1+1,u2+.7"]]
SWEEP_B = [IDX[n] for n in ["u1 -1", "u2 +1", "u1 +0.4", "u2 square", "u1 step 1>-1", "combo u1+1,u2+.7", "u1 tri +", "u1 pulse p16", "u1 sine 1/30"]]


def random_programmes(n, rng):
    """Fresh admissible programmes (test sets, equivalence check): u1 of several shapes, u2 zero half of the time."""
    out = []
    for _ in range(n):
        amp = rng.uniform(.2, 1.0); k = rng.integers(0, 6)
        if k == 0: u1 = np.full(T, amp * rng.choice([-1, 1]))
        elif k == 1: u1 = _step(rng.uniform(-1, 1), rng.uniform(-1, 1), int(rng.integers(15, 60)))
        elif k == 2: u1 = _tri(amp * rng.choice([-1, 1]))
        elif k == 3: u1 = _sine(amp, rng.uniform(10, 40))
        elif k == 4: u1 = _pulse(amp * rng.choice([-1, 1]), int(rng.integers(10, 30)), rng.uniform(.2, .5))
        else: u1 = np.clip(np.convolve(rng.standard_normal(T + 10), np.ones(10) / 5, "valid")[:T] * amp, -1, 1)
        m = rng.integers(0, 4)
        u2 = np.zeros(T) if m < 2 else (np.full(T, rng.uniform(-1, 1)) if m == 2 else _sq(rng.uniform(.3, 1), int(rng.integers(12, 30))))
        out.append(_u(u1, u2))
    return out
