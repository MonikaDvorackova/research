"""Phase 11: small controlled HMM utilities (S hidden states, O symbols, A actions), single continuing trajectory.
Convention (as eid.pomdp): s_0 ~ b0; for t = 1..n: s_t ~ T[a_t, s_{t-1}, .], o_t ~ Z[s_t, .].  The likelihood of the observations GIVEN the realised actions is
    p_theta(o_{1:n} | a_{1:n}) = b0^T  prod_t ( T[a_t] diag(Z[:, o_t]) ) 1 ,
which is exactly the conditional form needed for adaptive policies (policy factors cancel in likelihood ratios)."""
from __future__ import annotations

from fractions import Fraction

import numpy as np


def forward_loglik(T, Z, b0, acts, obs):
    alpha = np.asarray(b0, float).copy(); ll = 0.0
    for a, o in zip(acts, obs):
        alpha = (alpha @ T[a]) * Z[:, o]
        c = alpha.sum()
        if c <= 0:
            return -np.inf
        ll += np.log(c); alpha /= c
    return float(ll)


def exact_likelihood(T, Z, b0, acts, obs):
    """Exact rational likelihood; T, Z, b0 given as nested lists of Fractions (or ints/floats convertible to Fraction)."""
    S = len(b0)
    alpha = [Fraction(x) for x in b0]
    for a, o in zip(acts, obs):
        alpha = [sum(alpha[s] * Fraction(T[a][s][t]) for s in range(S)) * Fraction(Z[t][o]) for t in range(S)]
    return sum(alpha)


def random_hmm(S, O, A, rng, conc_T=1.0, conc_Z=1.0):
    return rng.dirichlet(np.full(S, conc_T), size=(A, S)), rng.dirichlet(np.full(O, conc_Z), size=S), rng.dirichlet(np.ones(S))


def sample(T, Z, b0, acts, rng):
    S, O = Z.shape
    s = rng.choice(S, p=b0); obs = []
    for a in acts:
        s = rng.choice(S, p=T[a, s]); obs.append(int(rng.choice(O, p=Z[s])))
    return np.array(obs)


def sample_adaptive(T, Z, b0, n, policy, rng):
    """policy(history_of_obs) -> action; returns (acts, obs)."""
    S, O = Z.shape
    s = rng.choice(S, p=b0); acts, obs = [], []
    for _ in range(n):
        a = policy(obs); s = rng.choice(S, p=T[a, s]); o = int(rng.choice(O, p=Z[s])); acts.append(a); obs.append(o)
    return np.array(acts), np.array(obs)


def em_fit(acts, obs, S, O, A, rng, iters=100, tol=1e-9, init=None):
    """Baum-Welch for one trajectory (scaled forward-backward).  Returns (T, Z, b0, loglik, iterations).  Uncertified: a local maximiser."""
    n = len(obs)
    if init is None:
        T = rng.dirichlet(np.ones(S), size=(A, S)); Z = rng.dirichlet(np.ones(O), size=S); b0 = rng.dirichlet(np.ones(S))
    else:
        T, Z, b0 = (x.copy() for x in init)
    prev = -np.inf
    for it in range(iters):
        al = np.zeros((n, S)); c = np.zeros(n); a_ = b0.copy()
        for t in range(n):
            x = (a_ @ T[acts[t]]) * Z[:, obs[t]]; c[t] = x.sum()
            if c[t] <= 0:
                break
            a_ = x / c[t]; al[t] = a_
        else:
            be = np.ones((n, S))
            for t in range(n - 2, -1, -1):
                be[t] = T[acts[t + 1]] @ (Z[:, obs[t + 1]] * be[t + 1]) / c[t + 1]
            gam0 = None
            Tn = np.full((A, S, S), 1e-12); Zn = np.full((S, O), 1e-12); b0n = np.full(S, 1e-12)
            for t in range(n):
                prev_al = b0 if t == 0 else al[t - 1]
                xi = prev_al[:, None] * T[acts[t]] * (Z[:, obs[t]] * be[t])[None, :] / c[t]
                Tn[acts[t]] += xi
                Zn[:, obs[t]] += al[t] * be[t]
                if t == 0:
                    b0n += xi.sum(1)
            T = Tn / Tn.sum(2, keepdims=True); Z = Zn / Zn.sum(1, keepdims=True); b0 = b0n / b0n.sum()
            ll = float(np.log(c).sum())
            if abs(ll - prev) < tol:
                break
            prev = ll
            continue
        break
    return T, Z, b0, forward_loglik(T, Z, b0, acts, obs), it + 1


def best_em(acts, obs, S, O, A, rng, restarts, iters, tol=1e-9):
    best = None
    for _ in range(restarts):
        r = em_fit(acts, obs, S, O, A, rng, iters, tol)
        if best is None or r[3] > best[3]:
            best = r
    return best
