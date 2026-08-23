"""Invariant checks required by PHASE 1G before execution:
(1) ground truth is hidden from investigators;
(7) reconstruction code produces deterministic results.

Also spot-checks the algorithm's known-correct behavior on a few cases,
to catch an implementation bug before it is mistaken for an experimental
result.
"""

import inspect

from src.cases import CASE_BUILDERS
from src.domain import GRANT, UNDETERMINED
from src.reconstruction import reconstruct
from src.regimes import ALL_REGIMES, view_for


def test_reconstruct_signature_never_takes_ground_truth_or_world():
    params = list(inspect.signature(reconstruct).parameters)
    assert params == ["regime", "view"]


def test_views_passed_to_reconstruct_never_carry_ground_truth():
    world = CASE_BUILDERS["1"]()[0]
    for regime in ALL_REGIMES:
        view = view_for(world, regime)
        assert not hasattr(view, "ground_truth")


def test_reconstruction_is_deterministic():
    world = CASE_BUILDERS["9"]()[0]
    for regime in ALL_REGIMES:
        view = view_for(world, regime)
        a1 = reconstruct(regime, view)
        a2 = reconstruct(regime, view)
        assert a1 == a2


def test_case_1_no_drift_all_regimes_identify_correct_policy_and_authority():
    world = CASE_BUILDERS["1"]()[0]
    gt = world.ground_truth
    for regime in ALL_REGIMES:
        answers = reconstruct(regime, view_for(world, regime))
        assert answers.policy_version != UNDETERMINED
        assert answers.policy_version["version_id"] == gt.true_policy_version_id
        assert answers.authority_version != UNDETERMINED
        assert answers.authority_version["agent_id"] == gt.true_authority_agent_id


def test_case_1_regime_a_cannot_recompute_authorization_by_construction():
    # Regime A never retains a per-decision evidence trace (preservation-
    # regimes.md), so Q7 is UNDETERMINED even with zero drift -- this is
    # the documented, intentional floor behavior, not a bug.
    world = CASE_BUILDERS["1"]()[0]
    answers = reconstruct("A", view_for(world, "A"))
    assert answers.evidence_values == UNDETERMINED
    assert answers.authorized_at_t0 == UNDETERMINED


def test_case_2_regime_a_uses_wrong_current_policy():
    world = CASE_BUILDERS["2"]()[0]
    gt = world.ground_truth
    answers = reconstruct("A", view_for(world, "A"))
    assert answers.policy_version["version_id"] != gt.true_policy_version_id


def test_case_2_regime_b_and_c_identify_correct_policy():
    world = CASE_BUILDERS["2"]()[0]
    gt = world.ground_truth
    for regime in ("B", "C"):
        answers = reconstruct(regime, view_for(world, regime))
        assert answers.policy_version["version_id"] == gt.true_policy_version_id
        valid_from, valid_to = answers.policy_version["valid_from"], answers.policy_version["valid_to"]
        assert valid_from <= gt.t0 and (valid_to is None or gt.t0 < valid_to)


def test_case_3_regime_c_still_finds_the_true_t0_policy_after_retroactive_correction():
    world = CASE_BUILDERS["3"]()[0]
    gt = world.ground_truth
    answers = reconstruct("C", view_for(world, "C"))
    assert answers.policy_version["version_id"] == gt.true_policy_version_id == "v1"
    assert answers.policy_version["valid_to"] == gt.true_policy_valid_interval[1] is None


def test_case_3_regime_b_is_misled_by_the_retroactive_correction():
    world = CASE_BUILDERS["3"]()[0]
    gt = world.ground_truth
    answers = reconstruct("B", view_for(world, "B"))
    assert answers.policy_version != UNDETERMINED
    assert answers.policy_version["version_id"] != gt.true_policy_version_id


def test_case_5_evidence_supersession_b_and_c_retain_true_t0_evidence():
    world = CASE_BUILDERS["5"]()[0]
    gt = world.ground_truth
    for regime in ("B", "C"):
        answers = reconstruct(regime, view_for(world, regime))
        assert answers.evidence_values == gt.true_evidence_values
