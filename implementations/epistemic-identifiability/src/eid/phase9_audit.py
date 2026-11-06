"""Phase 9 audit computations: (1) corrected Bayesian-Occam dissociation (non-generic truth), (2) power / coverage audit of binomial and clustered claims,
(3) Chernoff design exponents for the X1 benchmark, (4) exact reset-semantics check.  Exact or deterministic unless stated."""
from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import linprog
from scipy.special import gammaln, logsumexp
from scipy.stats import beta, binom

from eid.pomdp import A


# ---------------------------------------------------------------- (1) Occam dissociation, truth at psi0
def occam_offset(ns, psi0):
    """E_{k ~ Bin(n, psi0)} P(m2 | k) with m1 = Bernoulli(1/2) (no free parameter), m2 = Bernoulli(psi), psi ~ U(0,1), equal prior; truth = m2 at psi0.
    Also the expected predictive KL(Ber(psi0) || posterior-mean predictive).  Exact (sum over k)."""
    out = []
    for n in ns:
        k = np.arange(n + 1)
        w = binom.pmf(k, n, psi0)
        lm1 = -n * np.log(2.0)
        lm2 = gammaln(k + 1) + gammaln(n - k + 1) - gammaln(n + 2)
        post2 = 1.0 / (1.0 + np.exp(np.clip(lm1 - lm2, -700, 700)))
        pred = (1 - post2) * 0.5 + post2 * (k + 1) / (n + 2)
        kl = psi0 * np.log(psi0 / pred) + (1 - psi0) * np.log((1 - psi0) / (1 - pred))
        out.append((n, float((w * post2).sum()), float((w * kl).sum())))
    return out


# ---------------------------------------------------------------- (2) statistical audit
def cp_upper(k, n, a=0.05):
    return 1.0 if k >= n else float(beta.ppf(1 - a, k + 1, n - k))


def cp_lower(k, n, a=0.05):
    return 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))


def max_k_for_upper(n, thr, a):
    """Largest k with CP upper bound (one-sided level a) <= thr."""
    ks = [k for k in range(n + 1) if cp_upper(k, n, a) <= thr]
    return max(ks) if ks else -1


def prob_demonstrate_bound(n, true_rate, thr, a=0.05):
    """P(CP upper bound <= thr) when the n runs are i.i.d. Bernoulli(true_rate): the power of a 'rate <= thr' claim."""
    k = max_k_for_upper(n, thr, a)
    return float(binom.cdf(k, n, true_rate)) if k >= 0 else 0.0


def prob_refute(n, true_rate, null_rate=0.05, a=0.05):
    """P(CP lower bound > null_rate): power of a one-sided test that a rate exceeds the nominal level."""
    ks = np.arange(n + 1)
    lo = np.array([cp_lower(int(k), n, a) for k in ks])
    return float(binom.pmf(ks, n, true_rate)[lo > null_rate].sum())


def runs_needed_zero(thr, a=0.05):
    """Smallest n such that zero rejections in n runs give a CP upper bound <= thr."""
    n = 1
    while cp_upper(0, n, a) > thr:
        n += 1
    return n


def betabin_sample(rng, m, R, mean, icc):
    """m clusters of R Bernoulli runs with cluster-specific rate ~ Beta with the given mean and intra-class correlation."""
    if icc <= 0:
        return rng.binomial(R, mean, size=m)
    s = (1 - icc) / icc
    return rng.binomial(R, rng.beta(mean * s, (1 - mean) * s, size=m))


def coverage_of_upper_bounds(mean, icc, m, R, reps, rng, boot=400):
    """Coverage (fraction of datasets with bound >= true mean) of the pooled Clopper-Pearson one-sided 95% upper bound and of a cluster-bootstrap (percentile) one-sided 95% bound."""
    from scipy.stats import t as tdist
    cov_cp = cov_bs = cov_t = 0
    for _ in range(reps):
        ks = betabin_sample(rng, m, R, mean, icc)
        cov_cp += cp_upper(int(ks.sum()), m * R) >= mean
        rates = ks / R
        bs = np.array([rates[rng.integers(0, m, m)].mean() for _ in range(boot)])
        cov_bs += np.percentile(bs, 95) >= mean
        se = rates.std(ddof=1) / np.sqrt(m)
        cov_t += rates.mean() + tdist.ppf(0.95, m - 1) * se >= mean
    return cov_cp / reps, cov_bs / reps, cov_t / reps


# ---------------------------------------------------------------- (3) Chernoff design exponent (episodes as actions)
def chernoff_exponent(K):
    """K[h', a] = KL(truth || h' under action-sequence a) for each competing hypothesis h' (rows) and action-sequence a (columns).
    Returns (max over mixing weights lambda of min_h' sum_a lambda_a K[h', a], lambda*).  LP."""
    H, Acts = K.shape
    c = np.zeros(Acts + 1); c[-1] = -1
    A_ub = np.hstack([-K, np.ones((H, 1))]); b_ub = np.zeros(H)
    A_eq = np.zeros((1, Acts + 1)); A_eq[0, :Acts] = 1
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1], bounds=[(0, None)] * Acts + [(None, None)])
    return float(res.x[-1]), res.x[:Acts]


# ---------------------------------------------------------------- (4) reset semantics: absorbing regime chain over episodes vs mixture over change time
def regime_hmm_law(q0, q1, eps, n_ep):
    """Law over sequences of n_ep episode outcomes (each outcome index i with probabilities q_r[i]) when the regime r starts at 0 and moves 0->1
    (absorbing) with probability eps between episodes: forward algorithm over the regime."""
    laws = {}
    for seq in itertools.product(range(len(q0)), repeat=n_ep):
        a0, a1 = 1.0, 0.0
        for e, i in enumerate(seq):
            if e > 0:
                a0, a1 = a0 * (1 - eps), a1 + a0 * eps
            a0, a1 = a0 * q0[i], a1 * q1[i]
        laws[seq] = a0 + a1
    return laws


def change_time_mixture_law(q0, q1, eps, n_ep):
    """Same law as a mixture over the change episode tau (first episode in regime 1): P(tau = e) = (1-eps)^(e-1) eps for e = 1..n_ep-1, and
    P(no change within the horizon) = (1-eps)^(n_ep-1); episode 0 is always in regime 0."""
    laws = {}
    for seq in itertools.product(range(len(q0)), repeat=n_ep):
        tot = 0.0
        for tau in range(1, n_ep + 1):
            pr = (1 - eps) ** (tau - 1) * eps if tau < n_ep else (1 - eps) ** (n_ep - 1)
            lik = np.prod([q0[i] for i in seq[:tau]]) * np.prod([q1[i] for i in seq[tau:]])
            tot += pr * lik
        laws[seq] = tot
    return laws


# ---------------------------------------------------------------- policy-induced kernel discrepancy for a misspecified (order-1) class
def pooled_kernel(p, probs, T=4):
    """Pooled order-1 conditional kernel k(o | prev obs, action) and context visitation weights under an open-loop iid policy `probs` (exact enumeration)."""
    from eid.pomdp import O as O_, exact_obs_law as law
    N = np.zeros(((O_ + 1) * A, O_))
    for acts in itertools.product(range(A), repeat=T):
        w = float(np.prod([probs[a] for a in acts]))
        if w == 0:
            continue
        P = law(p, acts)
        for i, obs in enumerate(itertools.product(range(O_), repeat=T)):
            prev = O_
            for t in range(T):
                N[prev * A + acts[t], obs[t]] += w * P[i]
                prev = obs[t]
    vis = N.sum(1)
    return N / np.maximum(vis[:, None], 1e-300), vis / vis.sum()


def policy_kernel_discrepancy(p, probs1, probs2, T=4):
    """E_{ctx ~ policy 2} KL( k_1(.|ctx) || k_2(.|ctx) ): how far the pooled order-1 kernel moves when only the POLICY changes (the mechanism is fixed)."""
    k1, _ = pooled_kernel(p, probs1, T); k2, v2 = pooled_kernel(p, probs2, T)
    d = 0.0
    for c in range(len(v2)):
        if v2[c] > 0:
            m = k1[c] > 0
            d += v2[c] * float(np.sum(k1[c][m] * np.log(k1[c][m] / np.maximum(k2[c][m], 1e-300))))
    return d
