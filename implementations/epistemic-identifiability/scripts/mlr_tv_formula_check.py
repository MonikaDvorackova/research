"""Check TV_m = 2 mu_+(M >= m/2) - 1 (even m) and mu_+(M > (m-1)/2) - mu_+(M < (m-1)/2) (odd m)  against (1/2)||mu_+ - mu_-||_1.   usage: out.json"""
import sys, json, numpy as np
sys.path.insert(0, __import__("os").path.dirname(__file__))
from mlr_model import laws
err = 0
for m in range(2, 25):
    for K in (2, 3, 4, 7, 12):
        for c in (0.02, 0.2, 0.4, 0.49):
            a = laws(m, K, c)['+'][1]; b = laws(m, K, c)['-'][1]; tv = 0.5 * np.abs(a - b).sum()
            f = 2 * a[m // 2:].sum() - 1 if m % 2 == 0 else a[(m + 1) // 2:].sum() - a[:(m - 1) // 2].sum()
            err = max(err, abs(tv - f))
print("max |TV - threshold formula| =", err); json.dump(dict(max_error=err), open(sys.argv[1], "w"))
