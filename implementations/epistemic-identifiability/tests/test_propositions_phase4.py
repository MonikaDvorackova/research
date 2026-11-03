"""Exact finite-process checks for Propositions 7-9 and the Bostrom corollary."""
import itertools
import math

import numpy as np
import pytest

from eid.finite import (auc_exact, deterministic_policy_sup_tv, history_law, kl, max_auc_over_orders, posterior_after, tv)

NA, NO = 2, 2


def _law(seed, k=6):
    r = np.random.default_rng(seed)
    return {i: float(v) for i, v in enumerate(r.dirichlet(np.ones(k)))}


@pytest.mark.parametrize("seed", range(15))
def test_auc_ceiling_by_total_variation(seed):
    """P7(a): every score has AUROC <= 1/2 + TV; the maximum over rankings is attained by likelihood-ratio order."""
    p0, p1 = _law(seed), _law(100 + seed)
    t = tv(p0, p1)
    best = max_auc_over_orders(p0, p1)
    assert best <= 0.5 + t + 1e-12
    lr_order = {k: p1[k] / p0[k] for k in p0}
    assert auc_exact(p0, p1, lr_order) == pytest.approx(best, abs=1e-12)


def test_auc_ceiling_is_not_tightened_to_half_tv():
    """The bound 1/2 + TV/2 is false: the ceiling cannot be improved to that form (counterexample on 3 outcomes)."""
    p0, p1 = {0: .5, 1: .5, 2: 1e-12}, {0: 1e-12, 1: .5, 2: .5}
    p0 = {k: v / sum(p0.values()) for k, v in p0.items()}
    p1 = {k: v / sum(p1.values()) for k, v in p1.items()}
    assert max_auc_over_orders(p0, p1) > 0.5 + tv(p0, p1) / 2 + 0.05


@pytest.mark.parametrize("seed", range(10))
def test_cross_entropy_identity(seed):
    """P7(b): E_P[-log Q] = H(P) + KL(P||Q); so the mean anomaly score under Q separates two environments by
    [H(P1) - H(P0)] + [KL(P1||Q) - KL(P0||Q)]."""
    p0, p1, q = _law(seed), _law(50 + seed), _law(200 + seed)
    ent = lambda p: -sum(v * math.log(v) for v in p.values())  # noqa: E731
    mean = lambda p: sum(p[k] * -math.log(q[k]) for k in p)  # noqa: E731
    lhs = mean(p1) - mean(p0)
    rhs = (ent(p1) - ent(p0)) + (kl(p1, q) - kl(p0, q))
    assert lhs == pytest.approx(rhs, abs=1e-12)


def test_theory_equal_to_the_environment_inverts_the_anomaly_score():
    """P7(c): with E0 and E1 of disjoint support (TV = 1) and the observer's theory Q = E1, the anomaly score
    -log Q has AUROC exactly 0 for E1 as positive class, although separation is perfect for the likelihood ratio."""
    eps = 1e-9
    p0 = {0: 1 - eps, 1: eps}
    p1 = {0: eps, 1: 1 - eps}
    q = p1
    s = {k: -math.log(q[k]) for k in q}
    assert tv(p0, p1) > 0.999
    assert auc_exact(p0, p1, s) < 1e-6
    assert max_auc_over_orders(p0, p1) > 0.999


def _env_pair(delta):
    def e0(h, a):
        return np.array([0.5, 0.5])

    def e1(h, a):
        if len(h) == 2 and a == h[1]:        # difference exists only when the action matches the previous observation
            return np.array([0.5 - delta, 0.5 + delta])
        return np.array([0.5, 0.5])
    return e0, e1


@pytest.mark.parametrize("delta", [0.05, 0.1, 0.2])
def test_adaptivity_strictly_helps_in_a_state_dependent_process(delta):
    """P9(b): sup TV over history-dependent policies is strictly larger than over open-loop policies (here twice as large)."""
    e0, e1 = _env_pair(delta)
    open_loop = deterministic_policy_sup_tv(e0, e1, NA, NO, adaptive=False)
    adaptive = deterministic_policy_sup_tv(e0, e1, NA, NO, adaptive=True)
    assert open_loop == pytest.approx(delta / 2, abs=1e-12)
    assert adaptive == pytest.approx(delta, abs=1e-12)


@pytest.mark.parametrize("seed", range(5))
def test_memoryless_kernels_gain_nothing_from_adaptivity_for_kl(seed):
    """P9(a): if kernels depend on the history only through the current action, sup KL over policies equals
    T * max_a KL_a and a constant policy attains it (checked over all deterministic 2-step policies)."""
    r = np.random.default_rng(seed)
    k0 = {a: r.dirichlet(np.ones(NO)) for a in range(NA)}
    k1 = {a: r.dirichlet(np.ones(NO)) for a in range(NA)}
    e0, e1 = (lambda h, a: k0[a]), (lambda h, a: k1[a])  # noqa: E731
    kla = [sum(k0[a][o] * math.log(k0[a][o] / k1[a][o]) for o in range(NO)) for a in range(NA)]
    best = 0.0
    for a1, m0, m1 in itertools.product(range(NA), range(NA), range(NA)):
        def pol(h, a1=a1, m=(m0, m1)):
            a = a1 if len(h) == 0 else m[h[1]]
            v = np.zeros(NA); v[a] = 1.0
            return v
        best = max(best, kl(history_law(e0, pol, NA, NO, 2), history_law(e1, pol, NA, NO, 2)))
    assert best == pytest.approx(2 * max(kla), abs=1e-12)


def test_misspecified_finite_class_concentrates_on_kl_minimiser():
    """P8(b): with the truth outside a finite class, the posterior concentrates on the KL(truth || model) minimiser."""
    truth = {0: .5, 1: .3, 2: .2}
    models = [{0: .6, 1: .2, 2: .2}, {0: .48, 1: .32, 2: .2}, {0: .2, 1: .3, 2: .5}]  # KL gaps >= 0.02 nats per episode
    kls = [kl(truth, m) for m in models]
    sampler = lambda rng: int(rng.choice(3, p=[truth[0], truth[1], truth[2]]))  # noqa: E731
    post = posterior_after(models, sampler, 4000, np.random.default_rng(0))
    assert sorted(kls)[1] - sorted(kls)[0] > 0.02  # the minimiser is separated by a decisive margin
    assert int(np.argmax(post)) == int(np.argmin(kls)) and post.max() > 0.99


def test_correct_finite_class_identifies_the_truth_at_rate_kl():
    """P8(a): E[log posterior-odds(E1 vs E0)] under E0 changes by -KL(P0||P1) per episode (exact identity)."""
    p0, p1 = _law(3, 5), _law(4, 5)
    exp_log_lr = sum(p0[k] * math.log(p1[k] / p0[k]) for k in p0)
    assert exp_log_lr == pytest.approx(-kl(p0, p1), abs=1e-12)
    # Bostrom corollary: episodes needed in expectation to move prior odds omega below 1 is ln(omega)/KL(P0||P1)
    omega = 1e6
    n = math.log(omega) / kl(p0, p1)
    assert math.log(omega) + n * exp_log_lr == pytest.approx(0, abs=1e-9)
