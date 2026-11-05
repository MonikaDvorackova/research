"""Symbolic check of the endpoint inequalities used in the K>=2 proof.  For 0<=b0<=b1<=1, m_i=min(b_i,1-b_i):
 (E0) 2 m0 (1-b0) + 2 m1 b0  <=  1 - b1 + b0 ;   (E1) 2 m0 (1-b1) + 2 m1 b1  <=  1 - b1 + b0.
Each region (b0<=1/2 or >=1/2, b1<=1/2 or >=1/2) gives a polynomial of degree <=2; we minimise g-F over the polygon exactly (vertices, edges, interior critical point).  usage: out.json"""
import sys, json, itertools, sympy as sp
b0, b1 = sp.symbols("b0 b1", real=True)
regions = {"b0<=1/2,b1<=1/2": (b0, b1, [(0, 0), (sp.Rational(1, 2), sp.Rational(1, 2)), (0, sp.Rational(1, 2))]),
           "b0<=1/2,b1>=1/2": (b0, 1 - b1, [(0, sp.Rational(1, 2)), (sp.Rational(1, 2), sp.Rational(1, 2)), (sp.Rational(1, 2), 1), (0, 1)]),
           "b0>=1/2,b1>=1/2": (1 - b0, 1 - b1, [(sp.Rational(1, 2), sp.Rational(1, 2)), (sp.Rational(1, 2), 1), (1, 1)])}
res = {}
for name, (m0, m1, verts) in regions.items():
    for lab, F in (("E0", 2 * m0 * (1 - b0) + 2 * m1 * b0), ("E1", 2 * m0 * (1 - b1) + 2 * m1 * b1)):
        G = sp.expand(1 - b1 + b0 - F); cand = []
        pts = [tuple(map(sp.nsimplify, v)) for v in verts]; n = len(pts)
        for k in range(n):                                   # vertices and edge minima
            p, q = pts[k], pts[(k + 1) % n]; t = sp.symbols("t")
            e = sp.expand(G.subs({b0: p[0] + t * (q[0] - p[0]), b1: p[1] + t * (q[1] - p[1])}, simultaneous=True))
            cand += [e.subs(t, 0), e.subs(t, 1)]
            for r in sp.solve(sp.diff(e, t), t):
                if r.is_real and 0 < r < 1: cand.append(e.subs(t, r))
        sol = sp.solve([sp.diff(G, b0), sp.diff(G, b1)], [b0, b1], dict=True)      # interior critical point
        for s in sol:
            x, y = s[b0], s[b1]
            if x.is_real and y.is_real: cand.append(G.subs(s))
        # keep only interior critical points that lie in the polygon (conservative: include all; a smaller value would only strengthen the check if it is still >=0)
        res[f"{name}:{lab}"] = float(min(cand)); 
        print(f"{name:18s} {lab}: min over polygon candidates of (g - F) = {min(cand)}")
json.dump(res, open(sys.argv[1], "w"), indent=1)
