"""Exact reduction of the 2-state case.  Memory x = P(state 1).  Per-step affine maps: uninformative B(x)=b0+sigma x ; informative under h: A_h(x)=a_h0+s_h x with
a_h0=b0+c_h r0, s_h=sigma+c_h (r1-r0), c_1=-c_0=c=p_1-1/2, sigma=b1-b0, r_i=q_i*delta_i in [-2min(b_i,1-b_i), 2min(b_i,1-b_i)].
Period-K stationary point (phase 0 = informative), time-average of the memory marginal over phases, TV = |xbar_1 - xbar_0|, error = (1-TV)/2.
Global search: dense grid + local polish.  Conjecture C-M2: sup TV = ((lam-1)/(lam+1))/K.   usage: embedded_m2_exact.py out.json"""
import sys, json, itertools, numpy as np
from scipy.optimize import minimize


def xbar(b0, b1, r0, r1, c, K):
    sig = b1 - b0; xB = b0 / (1 - sig + 1e-300); g = sig ** (K - 1)
    a0 = b0 + c * r0; s = sig + c * (r1 - r0)
    den = 1 - g * s; u = (xB * (1 - g) + g * a0) / den
    Au = a0 + s * u
    geo = (1 - g) / (1 - sig + 1e-300) if abs(1 - sig) > 1e-12 else K - 1
    return (u + (K - 1) * xB + (Au - xB) * geo) / K


def tv(params, c, K):
    b0, b1, t0, t1 = params                          # r_i = t_i * 2*min(b_i,1-b_i), t_i in [-1,1]
    r0 = t0 * 2 * min(b0, 1 - b0); r1 = t1 * 2 * min(b1, 1 - b1)
    return abs(xbar(b0, b1, r0, r1, c, K) - xbar(b0, b1, r0, r1, -c, K))


def sup_tv(c, K, rng):
    best = 0.0
    g = np.linspace(0.02, 0.98, 25); tg = np.linspace(-1, 1, 11)
    cand = []
    for b0, b1 in itertools.product(g, g):
        for t0, t1 in itertools.product(tg, tg):
            try: cand.append((tv((b0, b1, t0, t1), c, K), (b0, b1, t0, t1)))
            except Exception: pass
    cand.sort(key=lambda z: -z[0] if np.isfinite(z[0]) else 0)
    for v, x0 in cand[:30]:
        r = minimize(lambda x: -tv(x, c, K) if np.all(np.abs(x[2:]) <= 1) and np.all((x[:2] > 0) & (x[:2] < 1)) else 1.0, x0, method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-14, maxiter=4000))
        best = max(best, -r.fun, v if np.isfinite(v) else 0)
    return best


if __name__ == "__main__":
    out = {}
    for p1 in (0.6, 2 / 3, 0.75, 0.9):
        c = p1 - 0.5; lam = p1 / (1 - p1)
        for K in (1, 2, 3, 4, 6, 10):
            s = sup_tv(c, K, None); conj = ((lam - 1) / (lam + 1)) / K
            out[f"p{p1:.3f}_K{K}"] = dict(sup_tv=s, conjecture=conj, diff=s - conj)
            print(f"p1={p1:.3f} lam={lam:.3f} K={K:2d}: sup TV {s:.8f}  conj {conj:.8f}  diff {s-conj:+.2e}", flush=True)
    json.dump(out, open(sys.argv[1], "w"), indent=1)
