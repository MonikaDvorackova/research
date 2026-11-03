"""Exact finite-state analysis of Bayesian experimental design under a misspecified hypothesis class (Proposition 10).

Two actions {0, 1}, binary outcomes. Hypotheses (classes) for the observer:
  E0 : P(o=1 | a) = (0.5, 0.5)            reference
  Ea : P(o=1 | a) = (0.9, 0.5)            differs from E0 only at action 0
  C  : catch-all: P(o=1 | a) = p_a with p_a ~ Beta(1,1) independently per action (optional)
Truth: E1 with P(o=1 | a) = (0.5, 0.95): differs from E0 only at action 1, i.e. outside the region where E0 and Ea disagree.

The posterior depends on the data only through the counts (n_a, k_a); the distribution of the counts under a policy is computed exactly
by dynamic programming over all outcome sequences.
"""
from __future__ import annotations

import math
from collections import defaultdict

TRUTH = (0.5, 0.95)
E0 = (0.5, 0.5)
EA = (0.9, 0.5)


def _lbeta(a, b):
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def log_marginals(counts, with_catch_all):
    """Log sequence-marginal likelihood of the counts under each class."""
    (n0, k0), (n1, k1) = counts
    lm = {"E0": (k0 * math.log(E0[0]) + (n0 - k0) * math.log(1 - E0[0])) + (k1 * math.log(E0[1]) + (n1 - k1) * math.log(1 - E0[1])),
          "Ea": (k0 * math.log(EA[0]) + (n0 - k0) * math.log(1 - EA[0])) + (k1 * math.log(EA[1]) + (n1 - k1) * math.log(1 - EA[1]))}
    if with_catch_all:
        lm["C"] = _lbeta(k0 + 1, n0 - k0 + 1) + _lbeta(k1 + 1, n1 - k1 + 1)
    return lm


def posterior(counts, prior, with_catch_all):
    lm = log_marginals(counts, with_catch_all)
    lw = {h: math.log(prior[h]) + lm[h] for h in lm}
    m = max(lw.values())
    z = sum(math.exp(v - m) for v in lw.values())
    return {h: math.exp(v - m) / z for h, v in lw.items()}


def predictive(counts, cls, a):
    """P(o=1 | a, data, class)."""
    (n0, k0), (n1, k1) = counts
    if cls == "E0":
        return E0[a]
    if cls == "Ea":
        return EA[a]
    n, k = (n0, k0) if a == 0 else (n1, k1)
    return (k + 1) / (n + 2)


def _h(p):
    return 0.0 if p <= 0 or p >= 1 else -(p * math.log(p) + (1 - p) * math.log(1 - p))


def eig(counts, prior, with_catch_all, a):
    """Mutual information between the class index and the next outcome at action a (exact, nats)."""
    post = posterior(counts, prior, with_catch_all)
    mix = sum(post[h] * predictive(counts, h, a) for h in post)
    return _h(mix) - sum(post[h] * _h(predictive(counts, h, a)) for h in post)


def _seq_prob(counts, cls, a, outcomes):
    """P(next outcomes (all at action a) | data, class), outcomes a tuple of 0/1; the catch-all updates inside the sequence."""
    (n0, k0), (n1, k1) = counts
    n, k = (n0, k0) if a == 0 else (n1, k1)
    p = 1.0
    for o in outcomes:
        q = predictive(((n, k), (0, 0)) if a == 0 else ((0, 0), (n, k)), cls, a)
        p *= q if o else 1 - q
        if cls == "C":
            n, k = n + 1, k + o
    return p


def eig_plan(counts, prior, with_catch_all, a, horizon=2):
    """Non-myopic EIG about the class from repeating action a for ``horizon`` steps (exact)."""
    import itertools
    post = posterior(counts, prior, with_catch_all)
    seqs = list(itertools.product((0, 1), repeat=horizon))
    pm = {h: [_seq_prob(counts, h, a, sq) for sq in seqs] for h in post}
    mix = [sum(post[h] * pm[h][i] for h in post) for i in range(len(seqs))]
    ent = lambda v: -sum(x * math.log(x) for x in v if x > 0)  # noqa: E731
    return ent(mix) - sum(post[h] * ent(pm[h]) for h in post)


def policy_action(name, counts, prior, with_catch_all, t):
    if name == "passive":          # always action 0 (the training-like intervention)
        return {0: 1.0}
    if name == "random":
        return {0: 0.5, 1: 0.5}
    if name == "sweep":            # fixed exploratory alternation
        return {t % 2: 1.0}
    if name == "eig":              # myopic expected information gain about the class, ties broken towards action 0
        e0, e1 = eig(counts, prior, with_catch_all, 0), eig(counts, prior, with_catch_all, 1)
        return {0: 1.0} if e0 >= e1 - 1e-12 else {1: 1.0}
    if name == "eig2":             # non-myopic: best of the plans "repeat a for 2 steps", first action executed
        e0, e1 = eig_plan(counts, prior, with_catch_all, 0), eig_plan(counts, prior, with_catch_all, 1)
        return {0: 1.0} if e0 >= e1 - 1e-12 else {1: 1.0}
    raise ValueError(name)


def run_exact(name, T, prior, with_catch_all, truth=TRUTH):
    """Exact distribution over counts after T steps; returns summary statistics of the posterior."""
    dist = {((0, 0), (0, 0)): 1.0}
    prob_play_1 = 0.0
    for t in range(T):
        new = defaultdict(float)
        for counts, w in dist.items():
            for a, pa in policy_action(name, counts, prior, with_catch_all, t).items():
                if a == 1:
                    prob_play_1 += w * pa
                for o, po in ((1, truth[a]), (0, 1 - truth[a])):
                    (n0, k0), (n1, k1) = counts
                    c = ((n0 + 1, k0 + o), (n1, k1)) if a == 0 else ((n0, k0), (n1 + 1, k1 + o))
                    new[c] += w * pa * po
        dist = new
    out = {"p_E0_mean": 0.0, "p_Ea_mean": 0.0, "p_C_mean": 0.0, "P(E0>=0.95)": 0.0, "P(C>0.5)": 0.0, "entropy_mean": 0.0, "expected_plays_of_action1": prob_play_1}
    for counts, w in dist.items():
        post = posterior(counts, prior, with_catch_all)
        out["p_E0_mean"] += w * post["E0"]
        out["p_Ea_mean"] += w * post["Ea"]
        out["p_C_mean"] += w * post.get("C", 0.0)
        out["P(E0>=0.95)"] += w * (post["E0"] >= 0.95)
        out["P(C>0.5)"] += w * (post.get("C", 0.0) > 0.5)
        out["entropy_mean"] += w * -sum(p * math.log(p) for p in post.values() if p > 0)
    return out
