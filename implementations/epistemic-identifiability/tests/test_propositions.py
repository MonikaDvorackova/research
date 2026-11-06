"""Exact numerical checks of the formal propositions on finite controlled processes (T-step histories)."""
import itertools
import math

import numpy as np
import pytest

from eid.finite import history_law, kl, stepwise_kl_sum, tv

NA, NO, T = 2, 2, 3
RNG = np.random.default_rng(0)


def random_env(seed, null_prefix=False):
    r = np.random.default_rng(seed)
    cache = {}

    def env(h, a):
        key = (h, a)
        if key not in cache:
            p = r.dirichlet(np.ones(NO))
            cache[key] = p
        return cache[key]
    return env


def random_policy(seed):
    r = np.random.default_rng(seed)
    cache = {}

    def pol(h):
        if h not in cache:
            cache[h] = r.dirichlet(np.ones(NA))
        return cache[h]
    return pol


def perturbed(env, seed, eps):
    r = np.random.default_rng(seed)
    cache = {}

    def e1(h, a):
        if (h, a) not in cache:
            q = env(h, a) * (1 - eps) + eps * r.dirichlet(np.ones(NO))
            cache[(h, a)] = q
        return cache[(h, a)]
    return e1


@pytest.mark.parametrize("seed", range(5))
def test_chain_rule(seed):
    """P1: KL(P0^pi || P1^pi) equals the expected sum of kernel KLs under P0^pi."""
    e0, pol = random_env(seed), random_policy(100 + seed)
    e1 = perturbed(e0, 200 + seed, 0.4)
    lhs = kl(history_law(e0, pol, NA, NO, T), history_law(e1, pol, NA, NO, T))
    assert lhs == pytest.approx(stepwise_kl_sum(e0, e1, pol, NA, NO, T), rel=1e-10)


@pytest.mark.parametrize("seed", range(5))
def test_pinsker_and_le_cam(seed):
    """P2: TV <= sqrt(KL/2); the best test has total error 1 - TV (checked by enumerating all likelihood-ratio tests)."""
    e0, pol = random_env(seed), random_policy(100 + seed)
    e1 = perturbed(e0, 200 + seed, 0.4)
    p, q = history_law(e0, pol, NA, NO, T), history_law(e1, pol, NA, NO, T)
    assert tv(p, q) <= math.sqrt(kl(p, q) / 2) + 1e-12
    best = min(sum(p[k] for k in p if k not in acc) + sum(q[k] for k in acc) for acc in _likelihood_ratio_sets(p, q))
    assert best == pytest.approx(1 - tv(p, q), abs=1e-12)


def _likelihood_ratio_sets(p, q):
    """Acceptance regions of the form {k: p_k/q_k >= c}; here 'accept H0' sets, error = P1(accept) + P0(reject)."""
    ratios = sorted(set(p[k] / q[k] for k in p))
    for c in ratios + [math.inf]:
        yield {k for k in p if p[k] / q[k] >= c}


def test_equivalence_of_kernels_iff_equal_laws():
    """P5: equal kernels on reachable histories <=> equal law under every deterministic policy; a kernel difference
    on a reachable history is detected by the policy that steers to it."""
    e0 = random_env(1)
    same = lambda h, a: e0(h, a)  # noqa: E731
    pols = [random_policy(s) for s in range(4)]
    for pol in pols:
        assert kl(history_law(e0, pol, NA, NO, T), history_law(same, pol, NA, NO, T)) == pytest.approx(0, abs=1e-14)
    # differ at exactly one reachable history h*=(a=0,o=1), action 1 at step 2
    star = ((0, 1), 1)

    def diff(h, a):
        if (h, a) == star:
            return np.array([0.9, 0.1]) if abs(e0(h, a)[0] - 0.9) > 1e-6 else np.array([0.5, 0.5])
        return e0(h, a)
    # deterministic steering policy: play 0, then 1, then anything
    steer = lambda h: np.array([1.0, 0.0]) if len(h) == 0 else (np.array([0.0, 1.0]) if len(h) == 2 else np.array([1.0, 0.0]))  # noqa: E731
    assert tv(history_law(e0, steer, NA, NO, T), history_law(diff, steer, NA, NO, T)) > 1e-3


def test_screening_off():
    """P7: if two mechanisms share the observable kernel, data cannot move the within-fibre posterior."""
    prior = {"m_sim": 0.3, "m_base": 0.7}            # same kernel, different simulated status
    kernel = {"m_sim": "k", "m_base": "k"}
    likelihood = {"k": 0.02}                          # any data likelihood depends on the kernel only
    post = {m: prior[m] * likelihood[kernel[m]] for m in prior}
    z = sum(post.values())
    assert post["m_sim"] / z == pytest.approx(prior["m_sim"])


@pytest.mark.parametrize("tau_seed", range(20))
def test_bayes_factor_bound(tau_seed):
    """P8: for any event A, |P1(A) - P0(A)| <= TV, hence BF of a null result lies in 1 +- TV/(1-alpha)."""
    r = np.random.default_rng(tau_seed)
    p = r.dirichlet(np.ones(8))
    q = 0.3 * r.dirichlet(np.ones(8)) + 0.7 * r.dirichlet(np.ones(8))
    t = 0.5 * np.abs(p - q).sum()
    for mask in itertools.product([0, 1], repeat=8):  # every non-rejection region
        m = np.array(mask, dtype=bool)
        if p[m].sum() <= 0:
            continue
        bf = q[m].sum() / p[m].sum()
        assert abs(bf - 1) <= t / p[m].sum() + 1e-12


@pytest.mark.parametrize("M", [1.0, 10.0, 100.0])
def test_coverage_construction(M):
    """P6(b): training-distribution error <= eps while KL under an out-of-support intervention >= M."""
    eps = 1e-3
    q_ = 0.5 * math.exp(-2 * M) * 0.5            # observation prob of o=1 under a=1 in E1; KL(Ber(.5)||Ber(q)) >= M
    k = 0.5 * math.log(0.5 / q_) + 0.5 * math.log(0.5 / (1 - q_))
    assert k >= M
    w = eps / k                                  # training policy plays a=1 with probability w
    assert w * k <= eps + 1e-15


def test_coverage_upper_bound_ratio():
    """P6(a): if the policy ratio is bounded by c per step, occupancy ratio <= c^t, hence KL_pi <= sum_t c^t * eps_t."""
    e0 = random_env(3)
    e1 = perturbed(e0, 9, 0.5)
    mu = random_policy(11)

    def pi(h):  # mixture: bounded ratio pi/mu <= c
        u = np.array([0.5, 0.5])
        return 0.5 * mu(h) + 0.5 * u
    mins = min(mu(h)[a] for h in _all_histories(T) for a in range(NA))
    c = 0.5 + 0.25 / mins  # pi/mu = 0.5 + 0.25/mu(a|h) <= c for every history
    lhs = stepwise_kl_sum(e0, e1, pi, NA, NO, T)
    eps_t = _per_step_eps(e0, e1, mu, T)
    assert lhs <= sum(c ** (t + 1) * eps_t[t] for t in range(T)) + 1e-12


def _all_histories(Tn):
    for t in range(Tn):
        yield from itertools.product(*[range(NA), range(NO)] * t)


def _per_step_eps(e0, e1, mu, Tn):
    eps = []
    for t in range(Tn):
        tot = 0.0
        for pre in itertools.product(*[range(NA), range(NO)] * t):
            p_pre, h = 1.0, ()
            for s in range(t):
                a, o = pre[2 * s], pre[2 * s + 1]
                p_pre *= mu(h)[a] * e0(h, a)[o]
                h = h + (a, o)
            for a in range(NA):
                k0, k1 = e0(h, a), e1(h, a)
                tot += p_pre * mu(h)[a] * sum(k0[o] * math.log(k0[o] / k1[o]) for o in range(NO))
        eps.append(tot)
    return eps
