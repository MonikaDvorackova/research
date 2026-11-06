"""Phase 8 adversarial diagnostic (EXPLORATORY): can a STATIONARY mechanism with a hidden-state transient trigger the stationarity e-process (a false 'mechanism change')?
One long continuing run (no episode resets) of 12 000 steps cut into 3000 blocks of 4 for the checkpoint grid. python scripts/phase8_transient.py results/phase8"""
import sys, os
import numpy as np
from eid.phase8 import *
from eid.pomdp import POMDP

out = sys.argv[1]; os.makedirs(out, exist_ok=True)
def rng(*k): return np.random.default_rng(np.random.SeedSequence(list(k)))

def slow_env(eps, start):
    S = 4
    T = np.zeros((A, S, S))
    for a in range(A):
        for s in range(S):
            T[a, s, s] = 1 - eps
            T[a, s, (s + 1 + a) % S] += eps                      # drift to other states; every action keeps the same slow chain structure
    Z = np.array([[.8, .1, .1], [.1, .8, .1], [.1, .1, .8], [.4, .3, .3]])
    b0 = np.zeros(S); b0[start] = 1
    return POMDP(T, Z, b0)

L = ["## D2b Stationary mechanism, hidden-state transient (continuing run, 12 000 steps, order-1 count class, uniform actions)\n",
     "| hidden-chain switching rate eps per step | initial state | stationarity e-process rejection (R=40) | median rejection checkpoint (episode-blocks) |", "|---|---|---|---|"]
for eps in (0.0005, 0.002, 0.01):
    for start in (0,):
        rej = []
        for r in range(40):
            env = slow_env(eps, start)
            ctx, obs = simulate_stream((env, env), None, lambda e: 1 / 3, 1, 12000, rng(12, int(eps * 1e4), r))
            ctx, obs = ctx.reshape(3000, 4), obs.reshape(3000, 4)
            rej.append(stationarity_etest(ctx, obs)[1])
        rr = [e for e in rej if e]
        L.append(f"| {eps} | {start} | {len(rr)}/40 | {np.median(rr) if rr else '–'} |")
# control: same chain started from its stationary distribution (uniform): no transient
rej = []
for r in range(40):
    env = slow_env(0.002, 0); env.b0 = np.ones(4) / 4
    ctx, obs = simulate_stream((env, env), None, lambda e: 1 / 3, 1, 12000, rng(13, r))
    rej.append(stationarity_etest(ctx.reshape(3000, 4), obs.reshape(3000, 4))[1])
L.append(f"| 0.002 | stationary start (control) | {sum(1 for e in rej if e)}/40 | – |")
open(os.path.join(out, "transient.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
