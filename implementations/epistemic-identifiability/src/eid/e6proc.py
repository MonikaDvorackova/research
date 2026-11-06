"""Phase 9: sequential procedures with explicitly stated formal nulls (development).
 N_ctx  : o_t | (previous observation, action) has one time-invariant law -- Markov in the context.        [E_ctx : changepoint e-process]
 N_ep   : episodes are i.i.d. given the action sequence (perfect environment-state and regime reset).        [E_ep  : episode-level saturated changepoint e-process]
 N_comp : the running sum of conditional expected Brier differences (class forecaster minus comparator) is <= 0.   [E_comp: Robbins-mixture confidence sequence]
Each is valid (type-I <= alpha) exactly when its formal null holds; a rejection when the null is false is not a type-I error."""
from __future__ import annotations

import numpy as np
from scipy.special import gammaln

from eid.pomdp import A, O
from eid.phase8 import NCTX, _contexts

ALPHA = 0.05


def dir_logml(counts):
    """Dirichlet(1/2) marginal log-likelihood of count rows (..., ncontext, noutcome), summed over contexts."""
    k = counts.shape[-1]
    n = counts.sum(-1)
    return (gammaln(0.5 * k) - gammaln(0.5 * k + n) + (gammaln(0.5 + counts) - gammaln(0.5)).sum(-1)).sum(-1)


def cp_etest(c, y, nc, ny, per_cell, alpha=ALPHA):
    """Generic categorical changepoint e-process.  c, y: flat int arrays (context, outcome) in time order; one grid cell = `per_cell` consecutive items.
    E_k = [G^-1 sum_j ML(items before cell j) ML(items after)] / sup_nu prod nu(y|c), evaluated at the end of every cell.  Returns (max log E, first rejecting cell or None)."""
    G = len(c) // per_cell
    cum = np.zeros((G + 1, nc, ny))
    for g in range(G):
        cum[g + 1] = cum[g]
        np.add.at(cum[g + 1], (c[g * per_cell:(g + 1) * per_cell], y[g * per_cell:(g + 1) * per_cell]), 1)
    best, rej = -np.inf, None
    idx = np.arange(G)
    for k in range(1, G + 1):
        tot = cum[k]
        n_c = tot.sum(1, keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            ll0 = np.nansum(np.where(tot > 0, tot * np.log(tot / n_c), 0.0))
        pre = np.where((idx <= k)[:, None, None], cum[:G], tot[None])
        lnum = dir_logml(pre) + dir_logml(tot[None] - pre)
        logE = (np.logaddexp.reduce(lnum) - np.log(G)) - ll0
        best = max(best, logE)
        if rej is None and logE >= np.log(1 / alpha):
            rej = k
    return float(best), rej


def ctx_etest(ctx, obs, alpha=ALPHA, step=25):
    """E_ctx on a (N, T) stream: context = (previous observation, action)."""
    T = ctx.shape[1]
    best, rej = cp_etest(ctx.ravel(), obs.ravel(), NCTX, O, step * T, alpha)
    return best, (rej * step if rej else None)


def ep_etest(ctx, obs, alpha=ALPHA, step=25):
    """E_ep: episode-level.  context = whole action sequence (A^T values); outcome = whole observation sequence (O^T values)."""
    N, T = ctx.shape
    acts = ctx % A
    c = (acts * (A ** np.arange(T))).sum(1)
    y = (obs * (O ** np.arange(T))).sum(1)
    best, rej = cp_etest(c, y, A ** T, O ** T, step, alpha)
    return best, (rej * step if rej else None)


def prequential_probs(c, y, nc, ny, gamma=1.0):
    """Predictive probabilities (n, ny) of a Dirichlet(1/2) count forecaster issued BEFORE each outcome; gamma < 1 = exponential forgetting per context."""
    cnt = np.zeros((nc, ny)); out = np.empty((len(c), ny))
    for i in range(len(c)):
        row = cnt[c[i]]
        out[i] = (row + 0.5) / (row.sum() + 0.5 * ny)
        if gamma < 1.0:
            row *= gamma
        row[y[i]] += 1
    return out


def brier(p, y):
    oh = np.zeros_like(p); oh[np.arange(len(y)), y] = 1
    return ((p - oh) ** 2).sum(1)


def comp_cs_test(p_class, p_comp, y, alpha=ALPHA, rho=2000.0, check_every=100):
    """Sequential test of N_comp.  Delta_t = Brier(class) - Brier(comparator) in [-2, 2].  Under N_comp, S_t = sum Delta <= (martingale with conditional range 4)
    so P(exists t: S_t >= sigma sqrt((t+rho) log((t+rho)/(rho alpha^2)))) <= alpha with sigma^2 = 4 (Robbins normal-mixture boundary; Hoeffding's lemma).
    Returns first rejection time (observation index) or None."""
    d = brier(p_class, y) - brier(p_comp, y)
    S = np.cumsum(d); t = np.arange(1, len(d) + 1)
    u = 2.0 * np.sqrt((t + rho) * np.log((t + rho) / (rho * alpha ** 2)))
    hit = np.flatnonzero(S >= u)
    return (int(hit[0]) + 1) if len(hit) else None


# ---------------------------------------------------------------- confidence-set denominator (T6d) for categorical contexts
def _cp_box(counts, a1):
    """Per-coordinate two-sided Clopper-Pearson intervals at level a1/(#coordinates) for each (context, outcome); unvisited contexts get [0, 1]."""
    from scipy.stats import beta
    nc, ny = counts.shape
    n = counts.sum(1)
    al = a1 / (nc * ny)
    lo = np.zeros((nc, ny)); hi = np.ones((nc, ny))
    for i in range(nc):
        if n[i] == 0:
            continue
        for j in range(ny):
            k = counts[i, j]
            lo[i, j] = 0.0 if k == 0 else beta.ppf(al / 2, k, n[i] - k + 1)
            hi[i, j] = 1.0 if k == n[i] else beta.ppf(1 - al / 2, k + 1, n[i] - k)
    return lo, hi


def _row_sup(n_row, lo, hi):
    """max sum n_o log nu_o  s.t. lo <= nu <= hi, sum nu = 1 (water-filling; returns -inf if infeasible)."""
    if lo.sum() > 1 + 1e-12 or hi.sum() < 1 - 1e-12:
        return -np.inf
    if n_row.sum() == 0:
        return 0.0
    f = lambda mu: np.clip(n_row / mu, lo, hi).sum()
    a, b = 1e-12, 1e12
    for _ in range(200):
        m = np.sqrt(a * b)
        (a, b) = (m, b) if f(m) > 1 else (a, m)
    nu = np.clip(n_row / np.sqrt(a * b), lo, hi)
    pos = n_row > 0
    if (nu[pos] <= 0).any():
        return -np.inf
    return float((n_row[pos] * np.log(nu[pos])).sum())


def cs_repair_etest(ctx_tr, obs_tr, ctx, obs, alpha=ALPHA, a1=0.05, step=25):
    """E'_k = q(D_k) / sup_{nu in C} prod nu(o|x), C = coordinatewise Clopper-Pearson box from INDEPENDENT training data (level a1 over all coordinates);
    q = prequential Dirichlet(1/2) on the test stream.  Evaluated at checkpoints.  Infeasible box (truth outside C) = reject.  Returns first rejection episode or None."""
    cnt_tr = np.zeros((NCTX, O)); np.add.at(cnt_tr, (ctx_tr.ravel(), obs_tr.ravel()), 1)
    lo, hi = _cp_box(cnt_tr, a1)
    N, T = ctx.shape
    c, y = ctx.ravel(), obs.ravel()
    run = np.zeros((NCTX, O)); lq = np.empty(len(c))
    for i in range(len(c)):
        row = run[c[i]]
        lq[i] = np.log((row[y[i]] + 0.5) / (row.sum() + 0.5 * O))
        row[y[i]] += 1
    cq = np.cumsum(lq)
    cnt = np.zeros((NCTX, O))
    for k in range(1, N // step + 1):
        seg = slice((k - 1) * step * T, k * step * T)
        np.add.at(cnt, (c[seg], y[seg]), 1)
        den = sum(_row_sup(cnt[i], lo[i], hi[i]) for i in range(NCTX))
        logE = cq[k * step * T - 1] - den
        if logE >= np.log(1 / alpha):
            return k * step
    return None


def conditional_range(p_class, p_comp):
    """Predictable conditional range R_t of Delta_t = Brier(class) - Brier(comparator) given the two forecasts p (class), q (comparator): whatever the outcome law,
    Delta takes one of the values d_o = (||p||^2 - ||q||^2) - 2 (p_o - q_o), o = 1..k, so R_t = 2 (max_o (p_o - q_o) - min_o (p_o - q_o))."""
    diff = p_class - p_comp
    return 2.0 * (diff.max(1) - diff.min(1))


def comp_cs_test_adaptive(p_class, p_comp, y, alpha=ALPHA, rho=1.0):
    """Variance-adaptive version of comp_cs_test using the PREDICTABLE conditional range R_t (known once the forecasts are issued).
    Conditionally on the past, Z_t = Delta_t - E[Delta_t | F_{t-1}] lies in an interval of length R_t, hence is (R_t/2)^2-sub-Gaussian (Hoeffding's lemma);
    V_t = sum_{s<=t} R_s^2/4 is predictable and exp(lam S^Z_t - lam^2 V_t/2) is a nonnegative supermartingale for every lam.  Mixing lam ~ N(0, 1/rho) gives
    sqrt(rho/(rho+V_t)) exp(S_t^2 / (2 (rho + V_t))); Ville => P(exists t: S^Z_t >= sqrt((V_t+rho) ln((V_t+rho)/(rho alpha^2)))) <= alpha.
    Under the weak null (sum E[Delta_s | F_{s-1}] <= 0 for all t) the rejection event is S_t = sum Delta_s >= that boundary.  Returns the first rejection time or None."""
    d = brier(p_class, y) - brier(p_comp, y)
    V = np.cumsum(conditional_range(p_class, p_comp) ** 2 / 4.0)
    S = np.cumsum(d)
    u = np.sqrt((V + rho) * np.log((V + rho) / (rho * alpha ** 2)))
    hit = np.flatnonzero(S >= u)
    return (int(hit[0]) + 1) if len(hit) else None
