"""(a) scan: is TV_m(K,c) strictly increasing in m for the reflecting-walk observer? (m<=40, many K, c)
(b) counterexample search: can any 3-state (or 4-state) clockless observer with free transition and action probabilities beat the reflecting walk at K=2?
    TV between time-averaged periodic stationary memory laws, exact linear solves; many random restarts of L-BFGS on a softmax parameterisation.   usage: out.json"""
import sys, json, numpy as np
from scipy.optimize import minimize
sys.path.insert(0, __import__("os").path.dirname(__file__))
from mlr_model import laws
def tv(m, K, c): L = laws(m, K, c); return 0.5 * np.abs(L['+'][1] - L['-'][1]).sum()
viol = []; worst = 1e9
for K in (2, 3, 4, 5, 7, 10, 20, 50):
    for c in (0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.49):
        t = [tv(m, K, c) for m in range(2, 41)]; d = np.diff(t); worst = min(worst, (d / np.array(t[1:])).min())
        if (d < -1e-12).any(): viol.append((K, c, int(np.argmin(d)) + 2))
out = dict(monotone_in_m_violations=viol, min_relative_increment=float(worst))
def auto_tv(theta, m, K, c):
    n = m * 2 * m; T = np.exp(theta[:n].reshape(m, 2, m)); T /= T.sum(2, keepdims=True); q = 1 / (1 + np.exp(-theta[n:n + m]))
    res = []
    for h, ch in ((1, c), (0, -c)):
        # state transition per signal; signal law: informative phase P(y=1|i)=1/2+ch*q_i (idle=fair); fair phases 1/2
        Af = 0.5 * (T[:, 0, :] + T[:, 1, :]); py1 = 0.5 + ch * q
        Ai = (1 - py1)[:, None] * T[:, 0, :] + py1[:, None] * T[:, 1, :]
        Per = Ai.copy()
        for _ in range(K - 1): Per = Per @ Af
        w, V = np.linalg.eig(Per.T); v = np.real(V[:, np.argmin(abs(w - 1))]); v = np.abs(v) / np.abs(v).sum()
        ph = [v]; x = v @ Ai; ph.append(x)
        for _ in range(K - 2): x = x @ Af; ph.append(x)
        res.append(np.mean(ph[:K], axis=0))
    return 0.5 * np.abs(res[0] - res[1]).sum()
rng = np.random.default_rng(0); opt = {}
for m, K, c in ((3, 2, 0.2), (3, 2, 0.4), (3, 3, 0.3), (4, 2, 0.2)):
    best = 0
    for r in range(150):
        th0 = rng.normal(0, 2, m * 2 * m + m)
        try: res = minimize(lambda t: -auto_tv(t, m, K, c), th0, method="L-BFGS-B", options=dict(maxiter=200)); best = max(best, -res.fun)
        except Exception: pass
    opt[f"m{m}_K{K}_c{c}"] = dict(best_found=float(best), reflecting_walk=float(tv(m, K, c)))
    print(m, K, c, "best random-restart TV", round(best, 6), " reflecting walk TV", round(tv(m, K, c), 6), flush=True)
out["optimality_search"] = opt; print(json.dumps({k: out[k] for k in ("monotone_in_m_violations", "min_relative_increment")})); json.dump(out, open(sys.argv[1], "w"), indent=1)
