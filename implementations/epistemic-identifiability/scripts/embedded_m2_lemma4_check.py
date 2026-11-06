"""Numerical check of Lemma 4 of proof-note-two-state-hidden-phase.md:  R(xhat0) = R(x_B)/(1-theta).   usage: out.json"""
import sys, json, numpy as np
sys.path.insert(0, __import__("os").path.dirname(__file__))
from embedded_m2_identity_check import entry
rng = np.random.default_rng(1); worst = 0.0
for _ in range(200000):
    b0, b1 = rng.uniform(0.01, 0.99, 2); t0, t1 = rng.uniform(-1, 1, 2); c = rng.uniform(0.01, 0.49); K = int(rng.integers(2, 9))
    r0 = t0 * 2 * min(b0, 1 - b0); r1 = t1 * 2 * min(b1, 1 - b1); sig = b1 - b0; g = sig ** (K - 1)
    xh = 0.5 * (entry(b0, b1, r0, r1, c, K) + entry(b0, b1, r0, r1, -c, K)); R = r0 * (1 - xh) + r1 * xh
    RB = (r0 * (1 - b1) + r1 * b0) / (1 - sig); th = (g * c * (r1 - r0) / (1 - g * sig)) ** 2
    worst = max(worst, abs(R - RB / (1 - th)))
print(f"max |R(xhat) - R(x_B)/(1-theta)| = {worst:.2e}"); json.dump(dict(max_error=worst), open(sys.argv[1], "w"))
