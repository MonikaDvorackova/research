"""K=2, even m: closed forms from the product-form phase law nu_{+,0}(i) = C r^{floor(i/2)}  (r = (1/2+c)/(1/2-c)).
 m = 4L  : TV = (r^L-1)/(r^L+1) = tanh(L artanh(2c))
 m = 4L+2: TV = 1 - 2*lower,  lower = [4 S_L + r^{L-1}(r+2p)] / (4 S_{2L+1}),  S_n = sum_{k<n} r^k,  p = r/(1+r)
Checks the formulas symbolically against sympy-simplified TV_6 of the repository's note and numerically against the independent model.  usage: out.json"""
import sys, json, numpy as np, sympy as sp
sys.path.insert(0, __import__("os").path.dirname(__file__))
from mlr_model import laws
def tv_num(m, K, c): L = laws(m, K, c); return 0.5 * np.abs(L['+'][1] - L['-'][1]).sum()
def tv_formula(m, c):
    r = (0.5 + c) / (0.5 - c); p = r / (1 + r); S = lambda n: sum(r ** k for k in range(n))
    if m % 4 == 0: L = m // 4; return (r ** L - 1) / (r ** L + 1)
    if m % 4 == 2: L = (m - 2) // 4; return 1 - 2 * (4 * S(L) + r ** (L - 1) * (r + 2 * p)) / (4 * S(2 * L + 1))
err = 0
for m in range(4, 41, 2):
    for c in (0.01, 0.1, 0.17, 0.3, 0.45, 0.499): err = max(err, abs(tv_num(m, 2, c) - tv_formula(m, c)))
out = dict(max_error_even_m_4_to_40=err)
c = sp.symbols("c", positive=True); r = (sp.Rational(1, 2) + c) / (sp.Rational(1, 2) - c); p = r / (1 + r); S = lambda n: sum(r ** k for k in range(n))
tv6 = sp.simplify(1 - 2 * (4 * S(1) + r ** 0 * (r + 2 * p)) / (4 * S(3)))
note6 = c * (9 - 4 * c ** 2) / (3 + 4 * c ** 2)
out["TV6_difference_symbolic"] = str(sp.simplify(tv6 - note6))
tv10 = sp.simplify(1 - 2 * (4 * S(2) + r * (r + 2 * p)) / (4 * S(5)))
out["TV10_closed_form"] = str(sp.factor(tv10))
print(json.dumps(out)); json.dump(out, open(sys.argv[1], "w"), indent=1)
