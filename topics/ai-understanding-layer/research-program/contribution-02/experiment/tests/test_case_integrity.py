"""Invariant checks required by PHASE 1G before execution:
(9) no-drift control is solvable;
(10) deliberately ambiguous cases are genuinely ambiguous in B before
     execution.

Also checks basic case-matrix integrity: all ten structural cases build,
categories match perturbation-matrix.md, and ground truth is computed
independently of (prior to) any regime's derived artifacts.
"""

from src.cases import CASE_BUILDERS, MANIPULATION_CHECK_CASE_IDS, all_worlds
from src.domain import UNDETERMINED
from src.reconstruction import reconstruct
from src.regimes import view_for


def test_all_ten_structural_cases_are_defined():
    assert set(CASE_BUILDERS) == {str(i) for i in range(1, 11)}


def test_case_10_yields_two_decisions_all_others_yield_one():
    for case_id, builder in CASE_BUILDERS.items():
        worlds = builder()
        if case_id == "10":
            assert len(worlds) == 2
        else:
            assert len(worlds) == 1


def test_manipulation_check_cases_are_the_four_forward_drift_cases():
    assert MANIPULATION_CHECK_CASE_IDS == ["2", "4", "6", "7"]
    for case_id in MANIPULATION_CHECK_CASE_IDS:
        worlds = CASE_BUILDERS[case_id]()
        for w in worlds:
            assert w.category == "forward-drift"


def test_ground_truth_result_is_computed_from_t0_state_not_from_any_regime_artifact():
    # Ground truth must be identical regardless of which regime's view is
    # later derived from the same world -- it is authored once, upstream
    # of all three regimes (experimental-system.md).
    for world in all_worlds():
        gt = world.ground_truth
        assert gt.decision_id == world.decision_id
        assert gt.t0 == world.t0
        # Ground truth's true policy/authority version must be among the
        # rows actually present in this world's history (never a fact
        # invented independently of it), and its recorded valid-time
        # interval must genuinely contain t0.
        policy_ids = {p.version_id for p in world.policy_history}
        authority_ids = {a.agent_id for a in world.authority_history}
        assert gt.true_policy_version_id in policy_ids
        assert gt.true_authority_agent_id in authority_ids
        p_from, p_to = gt.true_policy_valid_interval
        assert p_from <= gt.t0 and (p_to is None or gt.t0 < p_to)
        a_from, a_to = gt.true_authority_valid_interval
        assert a_from <= gt.t0 and (a_to is None or gt.t0 < a_to)


def test_case_1_no_drift_is_solvable_on_temporal_correctness_for_all_regimes():
    world = CASE_BUILDERS["1"]()[0]
    for regime in ("A", "B", "C"):
        answers = reconstruct(regime, view_for(world, regime))
        assert answers.policy_version != UNDETERMINED
        assert answers.authority_version != UNDETERMINED
        assert answers.policy_version["version_id"] == world.ground_truth.true_policy_version_id
        assert answers.authority_version["agent_id"] == world.ground_truth.true_authority_agent_id


def test_retroactive_cases_are_genuinely_hard_for_regime_b():
    """Cases 3, 8, 9 are constructed specifically so that Regime B's
    as-of-t0 query is misled by a retroactive correction. This test
    verifies the case construction actually produces that property
    before the experiment is run -- if it did not, Cases 3/8/9 would be
    trivially solvable by B and the design's central manipulation would
    not be present in the implementation."""
    for case_id in ("3", "8", "9"):
        world = CASE_BUILDERS[case_id]()[0]
        gt = world.ground_truth
        answers = reconstruct("B", view_for(world, "B"))
        misled = (
            answers.policy_version != UNDETERMINED
            and answers.policy_version["version_id"] != gt.true_policy_version_id
        )
        assert misled, f"case {case_id}: Regime B was not misled by the retroactive correction"


def test_case_10_boundary_is_implemented_as_documented_clean_semantics_not_fault_injection():
    """Per implementation-spec.md Section 5/7, whether Case 10 is a genuine
    fault-injection ambiguity or a documented limitation is an open
    implementer decision. This codebase takes the documented-limitation
    branch (exact half-open interval semantics, no injected clock
    imprecision). This test pins that choice so a future change is
    visible as a deliberate decision, not a silent regression."""
    worlds = CASE_BUILDERS["10"]()
    dx, dy = worlds
    answers_x = reconstruct("B", view_for(dx, "B"))
    answers_y = reconstruct("B", view_for(dy, "B"))
    assert answers_x.policy_version["version_id"] == dx.ground_truth.true_policy_version_id
    assert answers_y.policy_version["version_id"] == dy.ground_truth.true_policy_version_id
