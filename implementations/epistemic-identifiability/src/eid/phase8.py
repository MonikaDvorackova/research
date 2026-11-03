"""Phase 8: exact and lightweight diagnostics for the identifiability analysis (topics/bostrom-world-models/phase8).
Everything here is a diagnostic or an exact verification of an elementary statement; no result is claimed as a new theorem.
Conventions follow eid.pomdp: s0 ~ b0; each step: s' ~ T[a, s], o ~ Z[s'].  Context of a step = (previous observation or START=3, action)."""
from __future__ import annotations

import itertools
from math import comb, log

import numpy as np
from scipy.special import gammaln

from eid.pomdp import A, O, POMDP, exact_obs_law, make_e0, perturb_action2

NCTX = (O + 1) * A
GRID_STEP = 25
ALPHA = 0.05


# ---------------------------------------------------------------- T5: Bayesian-Occam dissociation (exact)
def occam_dissociation(ns):
    """m1: law on the probed class is Bernoulli(1/2) (no free parameter).  m2: Bernoulli(psi), psi ~ Uniform(0,1); truth = m2 at psi = 1/2,
    so both mechanisms imply the *same* law on the probed class, but only m2 is the true mechanism (m1 and m2 differ on an unprobed intervention).
    Returns, for each n, exact expectations under the truth of P(m2 | data) with equal prior, and of the predictive KL of the posterior-mean predictive."""
    rows = []
    for n in ns:
        pm2, kl, pbin = 0.0, 0.0, []
        for k in range(n + 1):
            lp = (gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)) - n * log(2)      # log Binom(n,1/2) pmf at k
            pbin.append(lp)
        pbin = np.exp(pbin)
        for k in range(n + 1):
            m1 = -n * log(2)                                      # log p(sequence | m1): any particular sequence has probability 2^-n
            m2 = -np.log(n + 1) - comb_log(n, k)                  # log p(data | m2) = Beta(k+1, n-k+1) = 1/((n+1) C(n,k))
            post2 = 1.0 / (1.0 + np.exp(np.clip(m1 - m2, -700, 700)))
            pred = (1 - post2) * 0.5 + post2 * (k + 1) / (n + 2)
            pm2 += pbin[k] * post2
            kl += pbin[k] * (0.5 * np.log(0.5 / pred) + 0.5 * np.log(0.5 / (1 - pred)))
        rows.append((n, pm2, kl))
    return rows


def comb_log(n, k):
    return float(gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1))


# ---------------------------------------------------------------- T1/T4: absorption of non-stationarity into a larger stationary model (exact)
def time_varying_law(p: POMDP, acts, emission_by_step):
    """Law of observations under a *time-inhomogeneous* kernel: same transitions, emission matrix Z_t at step t. Independent forward recursion."""
    alpha = p.b0[None, :]
    for t, a in enumerate(acts):
        nxt = (alpha @ p.T[a])[:, None, :] * emission_by_step[t].T[None, :, :]
        alpha = nxt.reshape(-1, p.S)
    return alpha.sum(1)


def counter_augmented(p: POMDP, emission_by_step):
    """Stationary POMDP with latent counter c = 0..T-1 (state (s, c)); emission of state (s, c) is Z_c.  Reproduces the time-varying process exactly."""
    Tn = len(emission_by_step)
    S = p.S
    Taug = np.zeros((A, S * Tn, S * Tn))
    Z = np.zeros((S * Tn, O))
    for c in range(Tn):
        Z[c * S:(c + 1) * S] = emission_by_step[c]
    for a in range(A):
        for c in range(Tn):
            for s in range(S):
                Taug[a, c * S + s, ((c + 1) % Tn) * S:((c + 1) % Tn) * S + S] = p.T[a, s]     # counter advances, state moves by p.T
    b0 = np.zeros(S * Tn)
    b0[:S] = p.b0                                         # counter starts at 0; first emission is from the NEXT state (counter 1) -> shift below
    # The first emission must use Z_0, but our convention emits from the post-transition state: store emissions shifted by one.
    Zs = np.zeros_like(Z)
    for c in range(Tn):
        Zs[((c + 1) % Tn) * S:((c + 1) % Tn) * S + S] = emission_by_step[c]
    return POMDP(Taug, Zs, b0)


# ---------------------------------------------------------------- streams for the count-based learner
def markov_env(seed):
    """Observed-state Markov environment (S=O=3, identity emission): first-order Markov in the observations."""
    r = np.random.default_rng([seed, 31])
    T = r.dirichlet(np.ones(3) * 0.6, size=(A, 3))
    return POMDP(T, np.eye(3), np.ones(3) / 3)


def change_action2(p: POMDP, seed):
    r = np.random.default_rng([seed, 32])
    T = p.T.copy()
    T[2] = r.dirichlet(np.ones(p.S) * 0.6, size=p.S)
    return POMDP(T, p.Z, p.b0)


def simulate_stream(envs, change_at, p2_sched, N, T, rng):
    """N episodes of T steps. envs = (E_before, E_after); the kernel switches at episode `change_at` (None = never).
    p2_sched(ep) -> probability of action 2 at that episode (other actions uniform).  Open-loop actions: vectorised over episodes.
    Returns ctx (N, T) and obs (N, T)."""
    e1, e2 = envs
    ep = np.arange(N)
    after = np.zeros(N, bool) if change_at is None else ep >= change_at
    p2 = np.array([p2_sched(e) for e in ep])
    u = rng.random((N, T))
    acts = np.where(u < p2[:, None], 2, (rng.random((N, T)) < 0.5).astype(int))
    S = e1.S
    s = (rng.random(N)[:, None] > np.cumsum(e1.b0)).sum(1).clip(max=S - 1)
    prev = np.full(N, O)
    ctx = np.zeros((N, T), int)
    obs = np.zeros((N, T), int)
    for t in range(T):
        a = acts[:, t]
        P = np.where(after[:, None], e2.T[a, s], e1.T[a, s])
        s = (rng.random(N)[:, None] > np.cumsum(P, 1)).sum(1).clip(max=S - 1)
        Zrow = np.where(after[:, None], e2.Z[s], e1.Z[s])
        o = (rng.random(N)[:, None] > np.cumsum(Zrow, 1)).sum(1).clip(max=O - 1)
        ctx[:, t] = prev * A + a
        obs[:, t] = o
        prev = o
    return ctx, obs


def frozen_null_etest(ctx_tr, obs_tr, ctx, obs, alpha=ALPHA):
    """E_t = q(D_t)/p_hat(D_t): p_hat = posterior-mean count model trained once on (ctx_tr, obs_tr), q = prequential Dirichlet(1/2) from scratch
    on the test stream.  Returns (max log E, first rejection episode or None)."""
    cnt = np.zeros((NCTX, O))
    np.add.at(cnt, (ctx_tr.ravel(), obs_tr.ravel()), 1)
    khat = (cnt + 0.5) / (cnt.sum(1, keepdims=True) + 0.5 * O)
    c, o = ctx.ravel(), obs.ravel()
    run = np.zeros((NCTX, O))
    lq = np.empty(len(c))
    for i in range(len(c)):
        row = run[c[i]]
        lq[i] = np.log((row[o[i]] + 0.5) / (row.sum() + 0.5 * O))
        row[o[i]] += 1
    logE = np.cumsum(lq - np.log(khat[c, o]))
    hit = np.flatnonzero(logE >= np.log(1 / alpha))
    return float(logE.max()), (int(hit[0] // ctx.shape[1]) + 1 if len(hit) else None)


def _dir_logml(counts):
    """Dirichlet(1/2) marginal log-likelihood of count rows (..., NCTX, O), summed over contexts."""
    n = counts.sum(-1)
    return (gammaln(0.5 * O) - gammaln(0.5 * O + n) + (gammaln(0.5 + counts) - gammaln(0.5)).sum(-1)).sum(-1)


def stationarity_etest(ctx, obs, alpha=ALPHA, step=GRID_STEP):
    """Anytime-valid sequential test of H0: 'one stationary categorical kernel p(o | context) generated the stream'.
    E_k = [ (1/G) sum_j ML(counts before tau_j) * ML(counts after tau_j) ] / prod_c prod_o (n_co / n_c)^n_co  evaluated at checkpoints k.
    Numerator: a mixture of predictable laws (change at tau_j, Dirichlet(1/2) prequential before and after).  Denominator: the MLE under H0.
    Returns (max log E over checkpoints, first rejection episode or None)."""
    N, T = ctx.shape
    G = N // step
    cum = np.zeros((G + 1, NCTX, O))
    for g in range(G):
        seg_c, seg_o = ctx[g * step:(g + 1) * step].ravel(), obs[g * step:(g + 1) * step].ravel()
        cum[g + 1] = cum[g]
        np.add.at(cum[g + 1], (seg_c, seg_o), 1)
    best, rej = -np.inf, None
    for k in range(1, G + 1):
        tot = cum[k]
        n_c = tot.sum(1, keepdims=True)
        with np.errstate(divide="ignore", invalid="ignore"):
            ll0 = np.nansum(np.where(tot > 0, tot * np.log(tot / n_c), 0.0))
        pre = cum[:G]                                           # tau_j = j*step, j = 0..G-1  (before-counts)
        pre = np.minimum(pre, tot[None]) if False else pre
        pre_k = np.where((np.arange(G) <= k)[:, None, None], cum[:G], tot[None])      # tau beyond the current time = no change yet
        post_k = tot[None] - pre_k
        lnum = _dir_logml(pre_k) + _dir_logml(post_k)
        logE = (np.logaddexp.reduce(lnum) - np.log(G)) - ll0
        best = max(best, logE)
        if rej is None and logE >= np.log(1 / alpha):
            rej = k * step
    return float(best), rej


# ---------------------------------------------------------------- T3: learning curves, plateau and comparator (exact limits, MC over training sets)
def _policy_law(p: POMDP, T):
    """All (acts, obs) pairs with the exact truth probability under uniform actions: arrays acts (M,T), obs (M,T), prob (M,)."""
    A_ = list(itertools.product(range(A), repeat=T))
    out_a, out_o, out_p = [], [], []
    for acts in A_:
        law = exact_obs_law(p, acts)
        for i, o in enumerate(itertools.product(range(O), repeat=T)):
            out_a.append(acts); out_o.append(o); out_p.append(law[i] / len(A_))
    return np.array(out_a), np.array(out_o), np.array(out_p)


def _contexts(acts, obs, order):
    M_, T = acts.shape
    ctx = np.zeros((M_, T), int)
    prev1 = np.full(M_, O); prev2 = np.full(M_, O)
    for t in range(T):
        if order == 1:
            ctx[:, t] = prev1 * A + acts[:, t]
        else:
            ctx[:, t] = (prev2 * (O + 1) + prev1) * A + acts[:, t]
        prev2, prev1 = prev1, obs[:, t]
    return ctx


def learner_limit_and_entropy(p: POMDP, order, T=4):
    """Exact entropy H of the truth under the uniform-action policy and the exact KL (misspecification plateau) of the best order-`order` Markov kernel."""
    acts, obs, pr = _policy_law(p, T)
    ctx = _contexts(acts, obs, order)
    nctx = (O + 1) ** order * A
    N = np.zeros((nctx, O))
    for t in range(T):
        np.add.at(N, (ctx[:, t], obs[:, t]), pr)
    k = N / np.maximum(N.sum(1, keepdims=True), 1e-300)
    ll = np.log(np.maximum(k[ctx, obs], 1e-300)).sum(1)
    H = float(-(pr * np.log(pr / 1.0 * np.ones_like(pr) * 1.0)).sum())       # placeholder replaced below
    # entropy of sequence law per action sequence: sum_p log p  (pr already includes the 1/27 action weight)
    nA = A ** T
    H = float(-(pr * np.log(pr * nA)).sum())
    return H, float(-(pr * ll).sum()) - H, k


def learning_curve(p: POMDP, order, ns, R, rng, T=4):
    """Expected excess held-out log-loss (nats per T-step episode, uniform actions) of the Dirichlet(1/2) order-`order` count learner trained on n episodes."""
    acts, obs, pr = _policy_law(p, T)
    ctxs = _contexts(acts, obs, order)
    nctx = (O + 1) ** order * A
    nA = A ** T
    H = float(-(pr * np.log(pr * nA)).sum())
    out = {}
    for n in ns:
        vals = []
        for _ in range(R):
            ctx_tr, obs_tr = simulate_stream((p, p), None, lambda e: 1 / 3, n, T, rng)
            # re-compute contexts for the requested order from observations and actions
            # (simulate_stream returns order-1 contexts; derive actions and rebuild)
            a_tr = ctx_tr % A
            c_tr = _contexts(a_tr, obs_tr, order)
            cnt = np.zeros((nctx, O))
            np.add.at(cnt, (c_tr.ravel(), obs_tr.ravel()), 1)
            k = (cnt + 0.5) / (cnt.sum(1, keepdims=True) + 0.5 * O)
            ll = np.log(k[ctxs, obs]).sum(1)
            vals.append(float(-(pr * ll).sum()) - H)
        out[n] = (float(np.mean(vals)), float(np.std(vals, ddof=1) / np.sqrt(R)))
    return out
