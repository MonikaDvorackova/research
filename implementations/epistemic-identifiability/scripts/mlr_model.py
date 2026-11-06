"""Reflecting-walk observer with hidden informative phase (independent reconstruction from transition matrices).
Memory {0..m-1}; y=1: i->min(i+1,m-1); y=0: i->max(i-1,0).  Phase 0 informative: P(y=1)=1/2+c_h, c_+=+c, c_-=-c; other K-1 phases fair.
Phase convention: nu_{h,j} = law of memory at the START of phase j (j=0 informative step is about to occur); mu_h = (1/K) sum_j nu_{h,j}."""
import numpy as np

def kernel(m, p):
    P = np.zeros((m, m))
    for i in range(m):
        P[i, min(i + 1, m - 1)] += p; P[i, max(i - 1, 0)] += 1 - p
    return P

def stationary(M):
    n = len(M); A = np.vstack([M.T - np.eye(n), np.ones(n)]); b = np.zeros(n + 1); b[-1] = 1
    return np.linalg.lstsq(A, b, rcond=None)[0]

def laws(m, K, c):
    out = {}
    Bf = kernel(m, 0.5)
    for h, ch in (("+", c), ("-", -c)):
        Ai = kernel(m, 0.5 + ch); Per = Ai.copy()
        for _ in range(K - 1): Per = Per @ Bf
        v = stationary(Per); phases = [v]; x = v @ Ai; phases.append(x)
        for _ in range(K - 2): x = x @ Bf; phases.append(x)
        out[h] = (np.array(phases[:K]), np.mean(phases[:K], axis=0))
    return out
