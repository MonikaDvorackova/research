"""Proposition 10 (design relative to the hypothesis class), by exact dynamic programming over all outcome sequences."""
import math

import pytest

from eid.finite_bayes import EA, E0, TRUTH, eig, posterior, run_exact

PRIOR2 = {"E0": 0.5, "Ea": 0.5}
PRIOR3 = {"E0": 0.45, "Ea": 0.45, "C": 0.10}
ZERO = ((0, 0), (0, 0))


def test_eig_is_zero_where_members_agree_and_posterior_is_blind_there():
    """P10(a): at action 1 all members of {E0, Ea} agree, so EIG = 0 there for every posterior, and any data from action 1 leave the
    posterior unchanged (the Bayes factor between members involves only steps where they differ)."""
    for counts in [ZERO, ((5, 2), (3, 1)), ((10, 3), (30, 29))]:
        assert eig(counts, PRIOR2, False, 1) == pytest.approx(0.0, abs=1e-15)
    a = posterior(((4, 1), (0, 0)), PRIOR2, False)
    b = posterior(((4, 1), (50, 49)), PRIOR2, False)     # 50 extreme observations at action 1 (truth deviates there)
    assert a["E0"] == pytest.approx(b["E0"], abs=1e-12)


def test_eig_greedy_policy_manufactures_observational_equivalence():
    """P10(b): with prior-order tie-breaking the EIG-greedy policy never plays action 1 on any path, hence under it the truth E1
    produces exactly the law of E0, although TV between E1 and E0 under uniformly random actions is large."""
    r = run_exact("eig", 40, PRIOR2, False)
    assert r["expected_plays_of_action1"] == 0.0           # exact: never plays the informative-about-the-truth action
    assert r["p_E0_mean"] > 0.99 and r["P(E0>=0.95)"] > 0.95
    # same laws under that policy: always-action-0 histories have identical law under E0 and under the truth (0.5 at action 0)
    assert TRUTH[0] == E0[0]
    # while a random policy sees the deviation in the data (the posterior over {E0, Ea} still cannot, by (a)):
    rr = run_exact("random", 40, PRIOR2, False)
    assert abs(rr["p_E0_mean"] - r["p_E0_mean"]) < 0.5      # no class-internal evidence of misfit even under random actions


def test_myopic_eig_with_catch_all_still_fails_refuted_conjecture():
    """Refuted conjecture (documented counterexample): that a catch-all class makes myopic EIG explore the untried action.
    At action 1 the catch-all's one-step predictive equals the reference's (both 1/2 under a uniform prior), so one-step EIG about the
    class is exactly zero there and myopic EIG never plays it, even with the catch-all present."""
    z = ((0, 0), (0, 0))
    assert eig(z, PRIOR3, True, 1) == pytest.approx(0.0, abs=1e-15) and eig(z, PRIOR3, True, 0) > 0.05
    r = run_exact("eig", 40, PRIOR3, True)
    assert r["expected_plays_of_action1"] == 0.0 and r["P(C>0.5)"] < 0.05


def test_non_myopic_eig_with_catch_all_restores_detection_but_not_without_it():
    """P10(c), corrected: with a catch-all, a two-step non-myopic EIG design finds the deviation (exact: P(catch-all > 0.5) = 0.93 at
    T = 40); without a catch-all, no class-based design can, myopic or not (the members agree at action 1, so EIG there is 0 at any horizon)."""
    r2 = run_exact("eig2", 40, PRIOR3, True)
    assert r2["P(C>0.5)"] > 0.9 and r2["expected_plays_of_action1"] > 10
    assert run_exact("passive", 40, PRIOR3, True)["P(C>0.5)"] < 0.05
    rn = run_exact("eig2", 40, PRIOR2, False)
    assert rn["expected_plays_of_action1"] == 0.0 and rn["P(E0>=0.95)"] > 0.95


def test_dp_probabilities_normalise_and_match_a_direct_enumeration():
    """Sanity: the DP distribution is a probability distribution; for a deterministic policy compare with brute-force enumeration."""
    import itertools
    from eid.finite_bayes import policy_action
    T = 6
    brute = 0.0
    for outcomes in itertools.product([0, 1], repeat=T):
        counts, w = ((0, 0), (0, 0)), 1.0
        for t, o in enumerate(outcomes):
            a = list(policy_action("sweep", counts, PRIOR2, False, t))[0]
            w *= TRUTH[a] if o else 1 - TRUTH[a]
            (n0, k0), (n1, k1) = counts
            counts = ((n0 + 1, k0 + o), (n1, k1)) if a == 0 else ((n0, k0), (n1 + 1, k1 + o))
        brute += w * posterior(counts, PRIOR2, False)["E0"]
    assert run_exact("sweep", T, PRIOR2, False)["p_E0_mean"] == pytest.approx(brute, abs=1e-12)
    assert math.isclose(sum(posterior(((3, 1), (2, 2)), PRIOR3, True).values()), 1.0)
