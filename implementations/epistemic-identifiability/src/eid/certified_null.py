"""Phase 10: certified learned-null sequential test for categorical context kernels (development).

Null class: the conditional law of o_t given the ENTIRE past equals nu(.|x_t), nu time-invariant, x_t = (previous observation, action) predictable.
Training: any predictable (adaptive) context sequence.  The LR confidence SET after n training observations is
    C_n = { nu : sum_{c,o} n_co log nu_co  >=  log q(D_train) - log(1/delta) },    q = prequential Dirichlet(1/2) (predictable, normalised),
which satisfies  P_{nu*}( exists n : nu* not in C_n ) <= delta  (Ville applied to R_n(nu*) = q(D_n)/p_{nu*}(D_n), a nonnegative supermartingale; this is
Theorem 1 of Emmenegger-Mutny-Krause 2023 in categorical form).  Test statistic on a fresh stream (counts m, prequential log-marginal L_q(m)):
    E_k = exp( L_q(m_k) - sup_{nu in C} sum m_co log nu_co ).
Given nu* in C, E_k <= q(D_test)/p_{nu*}(D_test), a nonnegative supermartingale, so P(reject) <= alpha + delta overall.
The supremum over C is a concave program with one concave constraint; the Lagrangian solution is nu_co(lam) = (m_co + lam n_co)/(M_c + lam N_c), lam >= 0 chosen by
bisection so that the constraint binds.  All values are exact (up to bisection tolerance, which is conservative: the returned supremum is an UPPER bound)."""
from __future__ import annotations

import numpy as np

from eid.e6proc import dir_logml


def _row_terms(m, n, lam):
    M = m.sum(1, keepdims=True); N = n.sum(1, keepdims=True)
    den = M + lam * N
    with np.errstate(divide="ignore", invalid="ignore"):
        nu = np.where(den > 0, (m + lam * n) / np.where(den > 0, den, 1.0), 1.0 / m.shape[1])
    return nu


def _xlogy(x, y):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(x > 0, x * np.log(np.where(y > 0, y, 1.0)), 0.0)


def lr_gamma(n_train, delta):
    """Right-hand side gamma of the LR confidence set: C = {nu: sum n log nu >= gamma}."""
    return float(dir_logml(n_train) - np.log(1.0 / delta))


def in_set(nu, n_train, delta):
    """Is the kernel nu (rows sum to 1) in the LR confidence set built from training counts n_train?"""
    ll = _xlogy(n_train, nu).sum()
    return bool(ll >= lr_gamma(n_train, delta) - 1e-12)


def sup_over_set(m, n, gamma, iters=200):
    """sup_{nu in C} sum m log nu with C = {nu: sum n log nu >= gamma}.  Returns a value that is >= the true supremum (bisection tolerance is resolved upward)."""
    m = np.asarray(m, float); n = np.asarray(n, float)
    mle = _xlogy(m, m / np.maximum(m.sum(1, keepdims=True), 1e-300)).sum()
    nu0 = _row_terms(m, n, 0.0)
    g0 = _xlogy(n, nu0).sum() - gamma if np.all(nu0[n > 0] > 0) else -np.inf
    if g0 >= 0:
        return float(mle)                                             # the unconstrained test-data MLE already lies in C
    lo, hi = 0.0, 1.0
    while _xlogy(n, _row_terms(m, n, hi)).sum() - gamma < 0:
        hi *= 4.0
        if hi > 1e15:
            return float(mle)                                         # numerically infeasible: fall back to the (larger) MLE = conservative
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if _xlogy(n, _row_terms(m, n, mid)).sum() - gamma >= 0:
            hi = mid
        else:
            lo = mid
    nu = _row_terms(m, n, lo)                                         # lo: constraint slightly violated => value >= true sup (conservative)
    return float(_xlogy(m, nu).sum())


def certified_etest(n_train, ctx, obs, alpha=0.05, delta=0.05, step=25, nctx=None, ny=None):
    """Sequential certified test on a (N, T) test stream; checkpoints every `step` episodes.  Returns (max log E, first rejecting episode or None)."""
    from eid.phase8 import NCTX
    from eid.pomdp import O
    nctx = nctx or NCTX; ny = ny or O
    gamma = lr_gamma(n_train, delta)
    N, T = ctx.shape
    m = np.zeros((nctx, ny)); best, rej = -np.inf, None
    for k in range(1, N // step + 1):
        seg = slice((k - 1) * step, k * step)
        np.add.at(m, (ctx[seg].ravel(), obs[seg].ravel()), 1)
        logE = float(dir_logml(m)) - sup_over_set(m, n_train, gamma)
        best = max(best, logE)
        if rej is None and logE >= np.log(1 / alpha):
            rej = k * step
    return float(best), rej


def oracle_etest(nu_true, ctx, obs, alpha=0.05, step=25):
    """Diagnostic upper bound: simple null with the TRUE kernel known."""
    from eid.phase8 import NCTX
    from eid.pomdp import O
    N, T = ctx.shape
    m = np.zeros((NCTX, O)); best, rej = -np.inf, None
    for k in range(1, N // step + 1):
        seg = slice((k - 1) * step, k * step)
        np.add.at(m, (ctx[seg].ravel(), obs[seg].ravel()), 1)
        logE = float(dir_logml(m)) - float(_xlogy(m, nu_true).sum())
        best = max(best, logE)
        if rej is None and logE >= np.log(1 / alpha):
            rej = k * step
    return float(best), rej


def frozen_point_etest(n_train, ctx, obs, alpha=0.05, step=25):
    """Test of the SIMPLE null 'kernel = training posterior mean'.  Not a test of the intended composite null (kernel unchanged since training)."""
    from eid.phase8 import NCTX
    from eid.pomdp import O
    khat = (n_train + 0.5) / (n_train.sum(1, keepdims=True) + 0.5 * O)
    return oracle_etest(khat, ctx, obs, alpha, step)


def exponent_under_set(w, nu1, n, gamma):
    """Information-projection exponent min_{nu in C} sum_c w_c KL(nu1_c || nu_c) for per-observation context weights w and a post-change kernel nu1."""
    m = w[:, None] * nu1
    return float(_xlogy(m, nu1).sum() - sup_over_set(m, n, gamma))


def exponent_oracle(w, nu1, nu0):
    m = w[:, None] * nu1
    return float(_xlogy(m, nu1).sum() - _xlogy(m, nu0).sum())
