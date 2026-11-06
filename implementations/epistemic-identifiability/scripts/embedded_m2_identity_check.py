"""Numerical check of the 2-state identity  TV_K = 2c |R(xhat)| / (K (1-sigma))  and of the K-independent inequality |R(xhat)| <= 1-sigma on random parameters.
xhat = mean of the two hypotheses' phase-0 entry laws; R(x) = r0 (1-x) + r1 x; sigma = b1-b0.   usage: embedded_m2_identity_check.py out.json"""
import sys, json, numpy as np
sys.path.insert(0, __import__("os").path.dirname(__file__))
from embedded_m2_exact import xbar

def entry(b0, b1, r0, r1, c, K):
    sig = b1 - b0; xB = b0 / (1 - sig); g = sig ** (K - 1); a0 = b0 + c * r0; s = sig + c * (r1 - r0)
    return (xB * (1 - g) + g * a0) / (1 - g * s)

rng = np.random.default_rng(0); n = 200000; worst_id = 0; worst_ineq = -1; viol = 0
for _ in range(n):
    b0, b1 = rng.uniform(0.01, 0.99, 2); t0, t1 = rng.uniform(-1, 1, 2); c = rng.uniform(0.01, 0.49); K = int(rng.integers(1, 8))
    r0 = t0 * 2 * min(b0, 1 - b0); r1 = t1 * 2 * min(b1, 1 - b1); sig = b1 - b0
    tvv = abs(xbar(b0, b1, r0, r1, c, K) - xbar(b0, b1, r0, r1, -c, K))
    xh = 0.5 * (entry(b0, b1, r0, r1, c, K) + entry(b0, b1, r0, r1, -c, K)); R = r0 * (1 - xh) + r1 * xh
    rhs = 2 * c * abs(R) / (K * (1 - sig)); worst_id = max(worst_id, abs(tvv - rhs))
    ratio = abs(R) / (1 - sig); worst_ineq = max(worst_ineq, ratio); viol += ratio > 1 + 1e-9
print(f"max |TV - identity| = {worst_id:.2e};  max |R(xhat)|/(1-sigma) = {worst_ineq:.6f};  violations of <=1: {viol}/{n}")
json.dump(dict(n=n, max_identity_error=worst_id, max_ratio=worst_ineq, violations=int(viol)), open(sys.argv[1], "w"))
