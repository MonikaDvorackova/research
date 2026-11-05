"""Numerical/exact checks for mlr-and-single-crossing-theorem.md.
(1) cone invariance: random nondecreasing vectors v>=0 are mapped to nondecreasing vectors by v->vA_p (p>=1/2) and v->vB (float, 2e5 trials, m=2..12).
(2) exact: Fraction-valued periodic stationary laws (mlr_exact) are nondecreasing in i at every phase, and mirror-symmetric (nu_-=J nu_+): m<=8,K<=7, several rational c.
(3) float scan of phasewise and averaged monotonicity of mu_+ and of MLR (m<=14, K<=60).   usage: out.json"""
import sys, json, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, __import__("os").path.dirname(__file__))
from mlr_model import kernel, laws
from mlr_exact import phase_laws
rng = np.random.default_rng(0); worst = 1e9
for _ in range(200000):
    m = int(rng.integers(2, 13)); p = rng.uniform(0.5, 0.9999) if rng.random() < .8 else 0.5
    v = np.sort(rng.exponential(size=m) ** rng.uniform(.3, 3)); v /= v.sum()
    for M in (kernel(m, p), kernel(m, 0.5)):
        w = v @ M; worst = min(worst, np.diff(w).min())
res = dict(cone_min_increment=float(worst))
bad_exact = 0; bad_mirror = 0; n_exact = 0
for m in range(2, 9):
    for K in (1, 2, 3, 4, 5, 7):
        if K == 1: continue
        for c in (Fr(1, 100), Fr(1, 10), Fr(1, 4), Fr(2, 5), Fr(49, 100)):
            L = phase_laws(m, K, c); n_exact += 1
            for j in range(K):
                a, b = L["+"][j], L["-"][j]
                if any(a[i + 1] < a[i] for i in range(m - 1)): bad_exact += 1
                if any(b[i] != a[m - 1 - i] for i in range(m)): bad_mirror += 1
res.update(exact_cases=n_exact, exact_nonmonotone=bad_exact, exact_mirror_failures=bad_mirror)
mn = 1e9; mlr_min = 1e9
for m in range(2, 15):
    for K in list(range(2, 12)) + [30, 60]:
        for c in (1e-3, 0.05, 0.2, 0.4, 0.499):
            Lw = laws(m, K, c); a = Lw["+"][1]; mn = min(mn, np.diff(a).min() / a.max()); b = Lw["-"][1]
            mlr_min = min(mlr_min, ((a[1:] * b[:-1] - a[:-1] * b[1:]) / (a[1:] * b[:-1])).min())
res.update(avg_min_increment_over_max=float(mn), mlr_min_relative_cross=float(mlr_min))
print(json.dumps(res)); json.dump(res, open(sys.argv[1], "w"), indent=1)
