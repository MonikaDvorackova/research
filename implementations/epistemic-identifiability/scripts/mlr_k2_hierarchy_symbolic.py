"""Symbolic proof of the K=2 even-memory hierarchy  TV_{4L} < TV_{4L+2} < TV_{4L+4}  with x = r^L, r>1, x>=r.  usage: out.json"""
import sys, json, sympy as sp
x, r = sp.symbols("x r", positive=True)
S = lambda n_expr: (n_expr - 1) / (r - 1)           # sum_{k<n} r^k = (r^n - 1)/(r-1)
p = r / (1 + r)
SL = (x - 1) / (r - 1); S2L1 = SL * (1 + x) + x ** 2                           # S_{2L+1} = S_L (1+r^L) + r^{2L}
lower = (4 * SL + x * (r + 3) / (r + 1)) / (4 * S2L1)                          # r^{L-1}(r+2p) = x (r+3)/(r+1)
tv_mid = sp.simplify(1 - 2 * lower)
tv_lo = (x - 1) / (x + 1); tv_hi = (r * x - 1) / (r * x + 1)
d1 = sp.factor(sp.simplify(tv_mid - tv_lo)); d2 = sp.factor(sp.simplify(tv_hi - tv_mid))
print("TV_{4L+2} - TV_{4L}   =", d1); print("TV_{4L+4} - TV_{4L+2} =", d2)
# sign analysis: substitute x = r*(1+u), u>=0 and r = 1+v, v>0 and inspect coefficients of numerators
u, v = sp.symbols("u v", nonnegative=True)
res = {}
for name, d in (("mid_minus_low", d1), ("high_minus_mid", d2)):
    num, den = sp.fraction(sp.together(d)); numpoly = sp.Poly(sp.expand(num.subs({x: (1 + v) * (1 + u), r: 1 + v})), u, v); denpoly = sp.Poly(sp.expand(den.subs({x: (1 + v) * (1 + u), r: 1 + v})), u, v)
    res[name] = dict(num_all_coeffs_nonneg=all(co >= 0 for co in numpoly.coeffs()), den_all_coeffs_nonneg=all(co >= 0 for co in denpoly.coeffs()), num_nonzero=numpoly.is_zero is False)
    print(name, res[name])
json.dump(dict(d1=str(d1), d2=str(d2), checks=res), open(sys.argv[1], "w"), indent=1)
