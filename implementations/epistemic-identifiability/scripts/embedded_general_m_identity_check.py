"""Check of the m-state generalisation of Lemma 2:  time-averaged difference of memory laws  S/K = 2c * xhat0 D (I-B)^{-1} / K  (row vectors),
B = (T0+T1)/2 (uninformative kernel), D = Q (T1-T0) with Q=diag(q), xhat0 = mean entry law at the informative step, signals symmetric +-c.   usage: out.json"""
import sys, json, numpy as np
rng = np.random.default_rng(3); worst = 0.0
def run(m, K, c, T0, T1, q):
    B = 0.5 * (T0 + T1); D = np.diag(q) @ (T1 - T0); laws = []
    for h, ch in ((1, c), (0, -c)):
        A = B + ch * D; u = np.ones(m) / m
        for _ in range(4000):                                        # iterate the period map: informative step then K-1 uninformative steps
            x = u @ A
            for _ in range(K - 1): x = x @ B
            u = x
        entries = [u]; x = u
        xs = [u]; x = u @ A; xs.append(x)
        for _ in range(K - 2): x = x @ B; xs.append(x)
        laws.append((u, np.mean(xs[:K], axis=0)))                    # entry law and Cesaro average over the K step-starts
    (u1, a1), (u0, a0) = laws
    lhs = a1 - a0; xhat = 0.5 * (u1 + u0)
    w, V = np.linalg.eig(B.T); pi = np.real(V[:, np.argmin(abs(w - 1))]); pi = pi / pi.sum()    # stationary law of B
    Z = np.linalg.inv(np.eye(m) - B + np.outer(np.ones(m), pi))                             # fundamental matrix: k Z (I-B) = k for zero-sum k
    rhs = 2 * c * xhat @ D @ Z / K
    return np.abs(lhs - rhs).max()
for _ in range(300):
    m = int(rng.integers(2, 6)); K = int(rng.integers(1, 6)); c = rng.uniform(0.05, 0.45)
    T1 = rng.dirichlet(np.ones(m) * 2, size=m); T0 = rng.dirichlet(np.ones(m) * 2, size=m); q = rng.uniform(0.2, 1, m)
    worst = max(worst, run(m, K, c, T0, T1, q))
print(f"max |S/K - 2c xhat D Z / K| over 300 random automata (m=2..5, K=1..5): {worst:.2e}"); json.dump(dict(max_error=worst), open(sys.argv[1], "w"))
