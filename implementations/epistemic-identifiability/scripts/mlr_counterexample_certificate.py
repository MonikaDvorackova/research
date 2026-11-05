"""Exact rational certificate that the reflecting-walk observer is NOT optimal among 3-state clockless observers.
Sticky decision automaton S(eps, ell): memory {0,1,2}, always probe.
 state 0: y=0 -> (eps, 1-2eps, eps) ; y=1 -> (eps, eps, 1-2eps)
 state 1: y=0 -> (eps, 1-2eps, eps) ; y=1 -> (ell, 1-ell-eps, eps)
 state 2: y=0 -> (ell, eps, 1-ell-eps) ; y=1 -> (eps, eps, 1-2eps)       (rows: next-state probabilities over 0,1,2)
Fractions only; the stationary periodic laws are obtained by exact Gauss-Jordan elimination; TV = (1/2) sum |mu_+ - mu_-| of phase-averaged laws, K=2, c=1/5.
usage: out.json"""
import sys, json
from fractions import Fraction as Fr
sys.path.insert(0, __import__("os").path.dirname(__file__))
import sympy as sp
from mlr_exact import phase_laws, vecmat, matmul, stationary

def automaton_tv(T, q, K, c):
    m = len(q); out = []
    for ch in (c, -c):
        py1 = [Fr(1, 2) + ch * qi for qi in q]
        Af = [[(T[i][0][j] + T[i][1][j]) / 2 for j in range(m)] for i in range(m)]
        Ai = [[(1 - py1[i]) * T[i][0][j] + py1[i] * T[i][1][j] for j in range(m)] for i in range(m)]
        Per = Ai
        for _ in range(K - 1): Per = matmul(Per, Af)
        v = stationary(Per); ph = [v]; x = vecmat(v, Ai); ph.append(x)
        for _ in range(K - 2): x = vecmat(x, Af); ph.append(x)
        ph = ph[:K]; out.append([sum(ph[j][i] for j in range(K)) / K for i in range(m)])
    return sum(abs(a - b) for a, b in zip(*out)) / 2, out

def sticky(eps, ell):
    e, l = eps, ell
    return [[[e, 1 - 2 * e, e], [e, e, 1 - 2 * e]], [[e, 1 - 2 * e, e], [l, 1 - l - e, e]], [[l, e, 1 - l - e], [e, e, 1 - 2 * e]]]

def walk_tv(m, K, c):
    L = phase_laws(m, K, c); mu = {h: [sum(L[h][j][i] for j in range(K)) / K for i in range(m)] for h in "+-"}
    return sum(abs(a - b) for a, b in zip(mu["+"], mu["-"])) / 2

res = {}
for (K, c) in ((2, Fr(1, 5)), (2, Fr(2, 5)), (3, Fr(3, 10)), (2, Fr(1, 20))):
    w = walk_tv(3, K, c)
    best = None
    for eps, ell in ((Fr(1, 10000), Fr(1, 30)), (Fr(1, 1000), Fr(1, 20)), (Fr(1, 100), Fr(1, 10))):
        tv, _ = automaton_tv(sticky(eps, ell), [Fr(1)] * 3, K, c)
        if best is None or tv > best[0]: best = (tv, eps, ell)
    res[f"K{K}_c{c}"] = dict(walk_TV=str(w), walk_TV_float=float(w), sticky_TV=str(best[0]), sticky_TV_float=float(best[0]), eps=str(best[1]), ell=str(best[2]), sticky_exceeds_walk=bool(best[0] > w), ratio=float(best[0] / w))
    print(f"K={K} c={c}: walk TV {float(w):.6f}; sticky(eps={best[1]}, ell={best[2]}) TV {float(best[0]):.6f}; exceeds: {best[0] > w}; ratio {float(best[0]/w):.3f}")
json.dump(res, open(sys.argv[1], "w"), indent=1)
