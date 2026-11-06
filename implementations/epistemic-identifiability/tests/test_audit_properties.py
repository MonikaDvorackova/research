"""Adversarial audit of Propositions 1-9 and the Bostrom corollary: randomised and exhaustive checks designed to find counterexamples.

Every test states the exact claim it attacks. Edge cases: zero-probability kernel entries (infinite KL), unreachable histories,
ties in scores, all measurable regions on small supports, and the stopping-time statement of the corollary.
"""
import itertools
import math

import numpy as np
import pytest

from eid.finite import history_law, tv

NA, NO = 2, 2


# ---------------------------------------------------------------- helpers
def sparse_env(seed, zero_prob=0.0):
    """Random finite environment; each kernel entry is zeroed with probability zero_prob (rows renormalised, never all-zero)."""
    r = np.random.default_rng(seed)
    cache = {}

    def env(h, a):
        if (h, a) not in cache:
            p = r.dirichlet(np.ones(NO))
            if r.random() < zero_prob:
                p[r.integers(NO)] = 0.0
                p = p / p.sum()
            cache[(h, a)] = p
        return cache[(h, a)]
    return env


def rand_policy(seed):
    r = np.random.default_rng(seed)
    cache = {}

    def pol(h):
        if h not in cache:
            cache[h] = r.dirichlet(np.ones(NA))
        return cache[h]
    return pol


def kl_safe(k0, k1):
    return sum(a * (math.log(a / b) if b > 0 else math.inf) for a, b in zip(k0, k1) if a > 0)


def stepwise_kl_safe(e0, e1, pol, T):
    """E_{P0^pi} sum_t KL(p0(.|h,a) || p1(.|h,a)), with inf allowed."""
    total = 0.0
    for t in range(T):
        for pre in itertools.product(*[range(NA), range(NO)] * t):
            w, h = 1.0, ()
            for s in range(t):
                a, o = pre[2 * s], pre[2 * s + 1]
                w *= pol(h)[a] * e0(h, a)[o]
                h = h + (a, o)
            for a in range(NA):
                if w * pol(h)[a] > 0:
                    d = kl_safe(e0(h, a), e1(h, a))
                    if d == math.inf:
                        return math.inf
                    total += w * pol(h)[a] * d
    return total


def all_subsets(keys):
    for r in range(len(keys) + 1):
        for c in itertools.combinations(keys, r):
            yield set(c)


# ---------------------------------------------------------------- Proposition 1 (kernel characterisation)
@pytest.mark.parametrize("seed", range(12))
def test_p1_laws_equal_iff_kernels_equal_on_reachable(seed):
    """Attack: kernels may differ on unreachable histories without changing any law; they may not differ on reachable ones."""
    base = sparse_env(seed)

    def e(h, a):                              # reachable-structure: after action 0 the first observation is always 0
        if h == () and a == 0:
            return np.array([1.0, 0.0])
        return base(h, a)
    alt = sparse_env(1000 + seed)

    def e_unreach(h, a):                      # differs only on histories starting (a=0, o=1), which E never produces
        if len(h) >= 2 and h[0] == 0 and h[1] == 1:
            return alt(h, a)
        return e(h, a)

    def e_reach(h, a):                        # differs on a reachable history
        if h == () and a == 1:
            k = e(h, a)
            return np.array([k[1], k[0]]) if abs(k[0] - k[1]) > 1e-3 else np.array([0.9, 0.1])
        return e(h, a)
    for ps in range(3):
        pol = rand_policy(50 + ps)
        l, lu = history_law(e, pol, NA, NO, 3), history_law(e_unreach, pol, NA, NO, 3)
        assert max(abs(l[k] - lu[k]) for k in l) < 1e-14
    steer = lambda h: np.array([0.0, 1.0]) if len(h) == 0 else np.array([1.0, 0.0])  # noqa: E731
    assert tv(history_law(e, steer, NA, NO, 3), history_law(e_reach, steer, NA, NO, 3)) > 1e-3


# ---------------------------------------------------------------- Proposition 2 (Neyman-Pearson / Le Cam / Pinsker)
@pytest.mark.parametrize("seed", range(20))
def test_p2_exhaustive_min_total_error_equals_one_minus_tv(seed):
    """Attack: minimum of P0(reject)+P1(accept) over ALL 2^8 deterministic tests equals 1 - TV exactly; Pinsker in both directions."""
    r = np.random.default_rng(seed)
    p = r.dirichlet(np.ones(8) * 0.5)
    q = r.dirichlet(np.ones(8) * 0.5)
    keys = list(range(8))
    best = min(sum(q[k] for k in A) + sum(p[k] for k in keys if k not in A) for A in all_subsets(keys))  # A = accept H0
    t = 0.5 * np.abs(p - q).sum()
    assert best == pytest.approx(1 - t, abs=1e-12)
    for a, b in ((p, q), (q, p)):
        kl = float(np.sum(a * np.log(a / b)))
        assert t <= math.sqrt(kl / 2) + 1e-12


# ---------------------------------------------------------------- Proposition 3(a) (coverage), including infinite KL
@pytest.mark.parametrize("seed", range(12))
@pytest.mark.parametrize("zero_prob", [0.0, 0.5])
def test_p3a_coverage_bound_including_infinite_kl(seed, zero_prob):
    """Attack: KL_pi <= sum_t c^t eps_t for every c bounding pi/mu, also when E1 has zeros (then both sides may be infinite)."""
    e0, e1 = sparse_env(seed), sparse_env(500 + seed, zero_prob)
    mu = rand_policy(900 + seed)
    pi_r = np.random.default_rng(800 + seed)
    cache = {}

    def pi(h):                                # a policy with pi <= c mu for the c computed below
        if h not in cache:
            cache[h] = 0.5 * mu(h) + 0.5 * pi_r.dirichlet(np.ones(NA))
        return cache[h]
    T = 3
    histories = [h for t in range(T) for h in itertools.product(*[range(NA), range(NO)] * t)]
    c = max(pi(h)[a] / mu(h)[a] for h in histories for a in range(NA))
    lhs = stepwise_kl_safe(e0, e1, pi, T)
    eps = []
    for t in range(T):
        tot = 0.0
        for pre in itertools.product(*[range(NA), range(NO)] * t):
            w, h = 1.0, ()
            for s in range(t):
                a, o = pre[2 * s], pre[2 * s + 1]
                w *= mu(h)[a] * e0(h, a)[o]
                h = h + (a, o)
            for a in range(NA):
                if w * mu(h)[a] > 0:
                    d = kl_safe(e0(h, a), e1(h, a))
                    tot = math.inf if d == math.inf else tot + w * mu(h)[a] * d
        eps.append(tot)
    rhs = sum(c ** (t + 1) * eps[t] for t in range(T))
    assert lhs <= rhs + 1e-9 or rhs == math.inf


# ---------------------------------------------------------------- Propositions 5 and 6 (event bounds), all regions
@pytest.mark.parametrize("seed", range(15))
def test_p5_bounds_over_all_regions(seed):
    """Attack: for every event N, |P1(N)-P0(N)| <= TV, hence the BF and rejection-LR bounds, for all 2^8 regions."""
    r = np.random.default_rng(seed)
    p, q = r.dirichlet(np.ones(8) * 0.4), r.dirichlet(np.ones(8) * 0.4)
    t = 0.5 * np.abs(p - q).sum()
    for A in all_subsets(list(range(8))):
        pn, qn = sum(p[k] for k in A), sum(q[k] for k in A)
        assert abs(qn - pn) <= t + 1e-12
        if 0 < pn < 1:
            alpha = 1 - pn                    # N = non-rejection
            assert abs(qn / pn - 1) <= t / pn + 1e-12
            rej_p, rej_q = 1 - pn, 1 - qn
            assert rej_q / rej_p <= 1 + t / rej_p + 1e-12


@pytest.mark.parametrize("seed", range(15))
def test_p6_false_alarm_inflation_over_all_tests(seed):
    """Attack: every region R with Q(R) <= alpha has E0(R) <= alpha + TV(E0, Q)."""
    r = np.random.default_rng(seed)
    p0, q = r.dirichlet(np.ones(8) * 0.4), r.dirichlet(np.ones(8) * 0.4)
    t = 0.5 * np.abs(p0 - q).sum()
    for alpha in (0.01, 0.05, 0.2):
        worst = max(sum(p0[k] for k in A) for A in all_subsets(list(range(8))) if sum(q[k] for k in A) <= alpha)
        assert worst <= alpha + t + 1e-12


# ---------------------------------------------------------------- Proposition 7(a) with ties
@pytest.mark.parametrize("seed", range(40))
def test_p7a_auroc_ceiling_with_ties(seed):
    """Attack: AUROC (ties = 1/2) of an arbitrary integer-valued score with many ties never exceeds 1/2 + TV."""
    r = np.random.default_rng(seed)
    p, q = r.dirichlet(np.ones(8) * 0.5), r.dirichlet(np.ones(8) * 0.5)
    t = 0.5 * np.abs(p - q).sum()
    score = r.integers(0, 3, 8)
    auc = sum(q[i] * p[j] * (1.0 if score[i] > score[j] else 0.5 if score[i] == score[j] else 0.0) for i in range(8) for j in range(8))
    assert auc <= 0.5 + t + 1e-12


# ---------------------------------------------------------------- Corollary: stopping-time statement
@pytest.mark.parametrize("seed", range(3))
def test_corollary_expected_stopping_time_is_at_least_ln_omega_over_kl(seed):
    """Attack on the corollary as originally worded ('the expected number of episodes needed is ln(omega)/KL').
    Wald's identity gives only E[tau] >= ln(omega)/KL (overshoot makes the true value larger). Simulate to check the inequality
    and that equality can fail."""
    r = np.random.default_rng(seed)
    p0, p1 = r.dirichlet(np.ones(4)), r.dirichlet(np.ones(4))
    kl = float(np.sum(p0 * np.log(p0 / p1)))
    omega = 50.0
    llr = np.log(p1 / p0)
    taus = []
    for _ in range(4000):
        s, n = math.log(omega), 0
        while s > 0:
            s += llr[r.choice(4, p=p0)]
            n += 1
        taus.append(n)
    taus = np.array(taus)
    bound = math.log(omega) / kl
    se = taus.std() / math.sqrt(len(taus))
    assert taus.mean() >= bound - 3 * se
    assert taus.mean() > bound            # overshoot: the 'expected number of episodes = ln(omega)/KL' wording is false in general
