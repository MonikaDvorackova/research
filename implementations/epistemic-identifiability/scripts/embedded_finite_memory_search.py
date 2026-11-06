"""Small exact search supporting a precise conjecture (embedded finite-memory active testing).  NOT a learning experiment: optimises an m-state stochastic automaton
controller by numerical optimisation of an exactly computed asymptotic error.  Model: two hypotheses h in {0,1}; hidden phase cycles deterministically with period K;
action a in {probe, idle} chosen by the automaton from its memory state; signal y in {0,1}: probe at phase 0 gives Bernoulli(p_h), anything else Bernoulli(1/2).
Time-homogeneous automaton: i' ~ T[i,y,.]; guess g(i).  Asymptotic error (equal priors) = 1/2 sum_i min(pi_0(i), pi_1(i)) with pi_h the time-averaged memory marginal.
usage: embedded_finite_memory_search.py out.json"""
import sys, json, numpy as np
from scipy.optimize import minimize

P = (1/3, 2/3)          # lambda = 2


def stationary_error(theta, m, K, p=P):
    nparam_act = m; nT = m * 2 * m
    act = 1 / (1 + np.exp(-theta[:nparam_act]))
    T = np.exp(theta[nparam_act:nparam_act + nT].reshape(m, 2, m)); T /= T.sum(2, keepdims=True)
    pis = []
    for h in (0, 1):
        n = K * m; M = np.zeros((n, n))                       # joint state (phase k, memory i)
        for k in range(K):
            for i in range(m):
                for a, pa in ((1, act[i]), (0, 1 - act[i])):
                    py1 = p[h] if (a == 1 and k == 0) else 0.5
                    for y, py in ((1, py1), (0, 1 - py1)):
                        M[k * m + i, ((k + 1) % K) * m: ((k + 1) % K) * m + m] += pa * py * T[i, y]
        # stationary distribution via power iteration on lazy chain (handles periodicity)
        L = 0.5 * (np.eye(n) + M); v = np.ones(n) / n
        for _ in range(4000): v = v @ L
        pis.append(v.reshape(K, m).sum(0))
    return 0.5 * np.minimum(pis[0], pis[1]).sum()


def search(m, K, restarts, rng):
    best = (1.0, None); npar = m + m * 2 * m
    for r in range(restarts):
        th0 = rng.normal(0, 2, npar)
        res = minimize(stationary_error, th0, args=(m, K), method="L-BFGS-B", options=dict(maxiter=80))
        if res.fun < best[0]: best = (res.fun, res.x)
    return best[0]


if __name__ == "__main__":
    rng = np.random.default_rng(0); out = {}
    hc = lambda m, lam=2.0: 1 / (1 + lam ** (m - 1))
    for K in (1, 2):
        for m in (2, 3, 4):
            e = search(m, K, restarts=25 if m < 4 else 40, rng=rng); out[f"K{K}_m{m}"] = dict(opt_error=e, hellman_cover_floor=hc(m), hc_half_memory=hc(max(m // 2, 1)))
            print(f"K={K} m={m}: best found error {e:.4f}   H-C floor 1/(1+2^(m-1))*0.5 = {0.5*hc(m)*2:.4f} (error=1/2*sum min => floor/2 conv.)", flush=True)
    json.dump(out, open(sys.argv[1], "w"), indent=1)
