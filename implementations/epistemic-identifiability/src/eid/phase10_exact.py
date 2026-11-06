"""Phase 10: exact finite computation of the rejection probability of a sequential e-process (Bernoulli stream) with different denominators.
Dynamic programming over the number of ones k at each n; rejected mass is absorbed.  Numerator: prequential Beta(1/2,1/2) mixture (predictable).
Denominators: the exact supremum over the null interval [a, b], or the supremum over a finite grid of null points (an approximate maximiser)."""
from __future__ import annotations

import numpy as np
from scipy.special import gammaln
from scipy.stats import binom


def _log_q(k, n):
    return gammaln(1.0) - gammaln(1.0 + n) + gammaln(0.5 + k) + gammaln(0.5 + n - k) - 2 * gammaln(0.5)


def _log_p(k, n, p):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(k > 0, k * np.log(p), 0.0) + np.where(n - k > 0, (n - k) * np.log(1 - p), 0.0)


def sup_interval(k, n, a, b):
    ph = np.clip(k / n, a, b)
    return _log_p(k, n, ph)


def sup_grid(k, n, grid):
    return np.max(np.stack([_log_p(k, n, g) for g in grid]), axis=0)


def rejection_probability(p_true, N, alpha, denom):
    """P(exists n <= N: log E_n >= ln(1/alpha)) when the stream is iid Bernoulli(p_true); denom(k, n) returns the log-denominator."""
    thr = np.log(1 / alpha)
    alive = np.array([1.0])                                   # distribution over k for n = 0 (no rejection yet)
    rejected = 0.0
    for n in range(1, N + 1):
        new = np.zeros(n + 1)
        new[:n] += alive * (1 - p_true); new[1:] += alive * p_true
        k = np.arange(n + 1)
        logE = _log_q(k, n) - denom(k, n)
        hit = logE >= thr
        rejected += new[hit].sum(); new[hit] = 0.0
        alive = new
    return float(rejected)


# ---------------------------------------------------------------- exact expected e-value of the certified test (2 contexts, binary outcomes, adaptive context rule c_{t+1} = o_t)
def expected_evalue_certified(nu1, train_counts, delta, n_test):
    """E_{nu*}[ E_N ] for the certified e-value E_N = exp(L_q(m_N) - sup_{nu in C} sum m log nu) after n_test test observations, exactly, by dynamic programming over
    count states (m00, m01, m10, m11) and the current context (rule: next context = last outcome, start 0).  nu1 = (P(o=1|c=0), P(o=1|c=1)); train_counts: 2x2 array."""
    from eid.certified_null import lr_gamma, sup_over_set
    from eid.e6proc import dir_logml
    gamma = lr_gamma(np.asarray(train_counts, float), delta)
    states = {(0, 0, 0, 0, 0): 1.0}
    for _ in range(n_test):
        new = {}
        for (a, b, c, d, ctx), pr in states.items():
            p1 = nu1[ctx]
            for o, po in ((0, 1 - p1), (1, p1)):
                m = [a, b, c, d]; m[2 * ctx + o] += 1
                key = (*m, o)
                new[key] = new.get(key, 0.0) + pr * po
        states = new
    tot = 0.0
    for (a, b, c, d, ctx), pr in states.items():
        m = np.array([[a, b], [c, d]], float)
        tot += pr * np.exp(dir_logml(m) - sup_over_set(m, np.asarray(train_counts, float), gamma))
    return float(tot)
