"""Phase 11 closure: independent verification of the type-class bound and the interval branch-and-bound prototype."""
import itertools
import math
from fractions import Fraction

import numpy as np

from eid.hmm_bounds import (box_upper, branch_and_bound, class_likelihood, class_log_sup, exact_U_C, fp_inflation, log_U_C, theta_from_hmm, type_classes)
from eid.hmm_small import best_em, exact_likelihood, forward_loglik, random_hmm, sample, sample_adaptive


def _brute_classes(acts, obs, S, O, A):
    out = {}
    n = len(obs)
    for path in itertools.product(range(S), repeat=n + 1):
        N = [0] * (A * S * S); M = [0] * (S * O)
        for t in range(n):
            N[acts[t] * S * S + path[t] * S + path[t + 1]] += 1
            M[path[t + 1] * O + obs[t]] += 1
        k = (path[0],) + tuple(N) + tuple(M)
        out[k] = out.get(k, 0) + 1
    return out


def test_type_classes_match_brute_force_enumeration_and_total_path_count():
    rng = np.random.default_rng(0)
    for (S, O, A, n) in ((2, 2, 1, 5), (2, 2, 2, 5), (3, 2, 1, 4), (2, 3, 2, 4)):
        acts = rng.integers(0, A, n); obs = rng.integers(0, O, n)
        cl, _ = type_classes(acts, obs, S, O, A)
        assert cl == _brute_classes(acts, obs, S, O, A)
        assert sum(cl.values()) == S ** (n + 1)


def test_decomposition_is_exact_including_boundary_parameters_and_zero_probabilities():
    rng = np.random.default_rng(1)
    S, O, A, n = 2, 2, 2, 7
    acts = rng.integers(0, A, n); obs = rng.integers(0, O, n)
    cl, _ = type_classes(acts, obs, S, O, A)
    for _ in range(20):
        T, Z, b0 = random_hmm(S, O, A, rng, 0.3, 0.3)
        assert abs(class_likelihood(cl, T, Z, b0, S, O, A) - math.exp(forward_loglik(T, Z, b0, acts, obs))) < 1e-12
    # boundary: deterministic transitions/emissions and point-mass initial law (zeros everywhere)
    T = np.zeros((A, S, S)); T[:, 0, 1] = 1; T[:, 1, 0] = 1
    Z = np.array([[1.0, 0.0], [0.0, 1.0]]); b0 = np.array([1.0, 0.0])
    lik = class_likelihood(cl, T, Z, b0, S, O, A)
    assert abs(lik - math.exp(forward_loglik(T, Z, b0, acts, obs))) < 1e-15 or (lik == 0.0 and forward_loglik(T, Z, b0, acts, obs) == -np.inf)


def _theta_c(key, S, O, A):
    nN = A * S * S; cnt = key[1:]
    T = np.zeros((A, S, S)); Z = np.zeros((S, O)); b0 = np.zeros(S); b0[key[0]] = 1.0
    for a in range(A):
        for s in range(S):
            row = np.array([cnt[a * S * S + s * S + s2] for s2 in range(S)], float)
            T[a, s] = row / row.sum() if row.sum() > 0 else 1.0 / S
    for s in range(S):
        row = np.array([cnt[nN + s * O + o] for o in range(O)], float)
        Z[s] = row / row.sum() if row.sum() > 0 else 1.0 / O
    return T, Z, b0


def test_sandwich_L_le_U_le_K_L_via_independent_forward_algorithm():
    """U_C = sum_c W_c sup f_c >= p_theta(D) for every theta (sup of a sum <= sum of sups); and L* >= p_{theta_c}(D) >= W_c f_c(theta_c) for every class, so U_C <= K L*.
    Checked with the forward algorithm (independent of the DP) at the class maximisers theta_c."""
    rng = np.random.default_rng(2)
    for (S, O, A, n) in ((2, 2, 1, 8), (2, 2, 2, 7), (3, 2, 1, 6)):
        acts = rng.integers(0, A, n); obs = rng.integers(0, O, n)
        cl, _ = type_classes(acts, obs, S, O, A)
        lu, mx, K = log_U_C(cl, S, O, A)
        best_fwd = -np.inf
        for key, w in cl.items():
            T, Z, b0 = _theta_c(key, S, O, A)
            fwd = forward_loglik(T, Z, b0, acts, obs)
            assert fwd >= math.log(w) + class_log_sup(key, S, O, A) - 1e-9          # one class's term cannot exceed the whole likelihood
            best_fwd = max(best_fwd, fwd)
        assert lu >= best_fwd - 1e-9 and lu <= best_fwd + math.log(K) + 1e-9          # L* >= best_fwd, so g <= log K
        for _ in range(200):                                                         # validity against random parameters
            T, Z, b0 = random_hmm(S, O, A, rng, 0.2, 0.2)
            assert forward_loglik(T, Z, b0, acts, obs) <= lu + 1e-12


def test_exact_rational_bound_dominates_exact_rational_likelihood_and_matches_float():
    rng = np.random.default_rng(3)
    S, O, A, n = 2, 2, 2, 6
    acts = rng.integers(0, A, n); obs = rng.integers(0, O, n)
    cl, _ = type_classes(acts, obs, S, O, A)
    U = exact_U_C(cl, S, O, A)
    assert abs(math.log(U) - log_U_C(cl, S, O, A)[0]) < 1e-12
    for _ in range(100):
        T = [[[Fraction(int(x), 10) for x in (r, 10 - r)] for r in rng.integers(0, 11, 2)] for _ in range(A)]
        Z = [[Fraction(int(x), 10) for x in (r, 10 - r)] for r in rng.integers(0, 11, 2)]
        b0 = [Fraction(int(r), 10) for r in (rng.integers(0, 11),)]; b0 = [b0[0], 1 - b0[0]]
        assert exact_likelihood(T, Z, b0, acts, obs) <= U


def test_adaptive_actions_are_handled_because_likelihood_is_conditional_on_realised_actions():
    rng = np.random.default_rng(4)
    S, O, A, n = 2, 2, 2, 8
    T, Z, b0 = random_hmm(S, O, A, rng)
    acts, obs = sample_adaptive(T, Z, b0, n, lambda h: (h[-1] if h else 0), rng)       # action depends on the previous observation
    cl, _ = type_classes(acts, obs, S, O, A)
    assert abs(class_likelihood(cl, T, Z, b0, S, O, A) - math.exp(forward_loglik(T, Z, b0, acts, obs))) < 1e-12
    assert log_U_C(cl, S, O, A)[0] >= forward_loglik(T, Z, b0, acts, obs) - 1e-12


def test_interval_bound_dominates_exact_likelihood_inside_the_box_and_is_consistent_with_type_class_bound():
    rng = np.random.default_rng(5)
    S, O, A, n = 2, 2, 1, 10
    T, Z, b0 = random_hmm(S, O, A, rng)
    acts = np.zeros(n, int); obs = sample(T, Z, b0, acts, rng)
    lo = rng.random((30, 5)) * 0.8; hi = np.minimum(lo + rng.random((30, 5)) * 0.2, 1.0)
    U = box_upper(lo, hi, acts, obs, A)
    for i in range(30):
        for _ in range(10):
            th = lo[i] + rng.random(5) * (hi[i] - lo[i])
            Tm = np.array([[[1 - th[0], th[0]], [1 - th[1], th[1]]]]); Zm = np.array([[1 - th[2], th[2]], [1 - th[3], th[3]]]); bb = np.array([1 - th[4], th[4]])
            ex = exact_likelihood(Tm.tolist(), Zm.tolist(), bb.tolist(), acts, obs)       # floats converted exactly to Fractions
            assert float(ex) <= U[i]
    cl, _ = type_classes(acts, obs, S, O, A)
    lu = log_U_C(cl, S, O, A)[0]
    em = best_em(acts, obs, S, O, A, np.random.default_rng(0), 10, 300)
    r = branch_and_bound(acts, obs, A, 0.2, max_boxes=300_000, warm=em[:3], time_limit=20)
    assert r["L_lo"] <= r["U"] and math.log(r["U"]) >= em[3] - 1e-9 and lu >= math.log(r["L_lo"]) - 1e-9
    assert fp_inflation(n) > 1.0


def test_dense_grid_never_exceeds_certified_bounds():
    rng = np.random.default_rng(6)
    T, Z, b0 = random_hmm(2, 2, 1, rng)
    acts = np.zeros(6, int); obs = sample(T, Z, b0, acts, rng)
    g = np.linspace(0, 1, 9); best = -np.inf
    for th in itertools.product(g, repeat=5):
        Tm = np.array([[[1 - th[0], th[0]], [1 - th[1], th[1]]]]); Zm = np.array([[1 - th[2], th[2]], [1 - th[3], th[3]]])
        best = max(best, forward_loglik(Tm, Zm, np.array([1 - th[4], th[4]]), acts, obs))
    cl, _ = type_classes(acts, obs, 2, 2, 1)
    r = branch_and_bound(acts, obs, 1, 0.2, max_boxes=300_000, time_limit=20)
    assert best <= math.log(r["U"]) and best <= log_U_C(cl, 2, 2, 1)[0] + 1e-12


def test_K_ratio_claim_fails_for_a_constrained_family_counterexample():
    """The sandwich U_C <= K L* needs the class maximisers theta_c to lie in Theta_0.  If emission probabilities of symbol 0 are constrained to <= 0.6 in every state,
    L* <= 0.6^n for all-zero data while U_C stays near 1: the ratio exceeds any fixed K as n grows."""
    n = 24; acts = np.zeros(n, int); obs = np.zeros(n, int)
    cl, _ = type_classes(acts, obs, 2, 2, 1)
    lu, _, K = log_U_C(cl, 2, 2, 1)
    assert lu > -1e-6 and lu - n * math.log(0.6) > math.log(K)


def test_determinism():
    rng = np.random.default_rng(7); acts = np.zeros(8, int); obs = rng.integers(0, 2, 8)
    a = log_U_C(type_classes(acts, obs, 2, 2, 1)[0], 2, 2, 1); b = log_U_C(type_classes(acts, obs, 2, 2, 1)[0], 2, 2, 1)
    assert a == b
    r1 = branch_and_bound(acts, obs, 1, 0.3, max_boxes=100_000, time_limit=20); r2 = branch_and_bound(acts, obs, 1, 0.3, max_boxes=100_000, time_limit=20)
    assert r1["U"] == r2["U"] and r1["boxes"] == r2["boxes"]
