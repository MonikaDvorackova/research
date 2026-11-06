"""Counterexample search for 'the reflecting walk is optimal among m-state clockless observers' (K, c fixed).  Irreducibility enforced by a probability floor eps=1e-4 on every
transition; stationary laws by linear solves (not eigenvectors, which are meaningless for reducible automata).  Many random restarts of L-BFGS.  Reports the best TV found and
the reflecting-walk TV.  A value above the walk's is a genuine counterexample only after exact re-verification (see mlr_counterexample_certificate.py).   usage: out.json"""
import sys, json, numpy as np
from scipy.optimize import minimize
sys.path.insert(0, __import__("os").path.dirname(__file__))
from mlr_model import laws
EPS = 1e-4
def tv_walk(m, K, c): L = laws(m, K, c); return 0.5 * np.abs(L['+'][1] - L['-'][1]).sum()
def build(theta, m):
    n = m * 2 * m; T = np.exp(theta[:n].reshape(m, 2, m)); T /= T.sum(2, keepdims=True); T = (1 - m * EPS) * T + EPS
    q = 1 / (1 + np.exp(-theta[n:n + m])); return T, q
def stat(M):
    n = len(M); A = np.vstack([M.T - np.eye(n), np.ones(n)]); b = np.zeros(n + 1); b[-1] = 1
    return np.linalg.lstsq(A, b, rcond=None)[0]
def avg_laws(T, q, m, K, c):
    out = []
    for ch in (c, -c):
        Af = 0.5 * (T[:, 0, :] + T[:, 1, :]); py1 = 0.5 + ch * q
        Ai = (1 - py1)[:, None] * T[:, 0, :] + py1[:, None] * T[:, 1, :]
        Per = Ai.copy()
        for _ in range(K - 1): Per = Per @ Af
        v = stat(Per); ph = [v]; x = v @ Ai; ph.append(x)
        for _ in range(K - 2): x = x @ Af; ph.append(x)
        out.append(np.mean(ph[:K], axis=0))
    return out
def obj(theta, m, K, c):
    T, q = build(theta, m); a, b = avg_laws(T, q, m, K, c); return -0.5 * np.abs(a - b).sum()
rng = np.random.default_rng(1); res = {}
for m, K, c, R in ((2, 2, 0.2, 60), (3, 2, 0.2, 200), (3, 2, 0.4, 150), (3, 3, 0.3, 150), (4, 2, 0.2, 200), (4, 3, 0.3, 120)):
    best = 0; arg = None
    for r in range(R):
        th0 = rng.normal(0, 2, m * 2 * m + m)
        try:
            o = minimize(obj, th0, args=(m, K, c), method="L-BFGS-B", options=dict(maxiter=300))
            if -o.fun > best: best = -o.fun; arg = o.x
        except Exception: pass
    res[f"m{m}_K{K}_c{c}"] = dict(best_found=float(best), reflecting_walk=float(tv_walk(m, K, c)), exceeds=bool(best > tv_walk(m, K, c) + 1e-6))
    print(m, K, c, "best", round(best, 6), "walk", round(tv_walk(m, K, c), 6), flush=True)
    if arg is not None and best > tv_walk(m, K, c) + 1e-6: np.save(f"results/mlr/best_theta_m{m}_K{K}_c{c}.npy", arg)
json.dump(res, open(sys.argv[1], "w"), indent=1)
