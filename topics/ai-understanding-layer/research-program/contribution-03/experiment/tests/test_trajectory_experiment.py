"""Pre-execution tests. All of these must pass BEFORE the experiment is
frozen (PRE-EXECUTION-MANIFEST.md) and run. They check the design, not
the results -- no case may be altered after this file is green in order
to change an outcome.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cases import CASE_BUILDERS, NEGATIVE_CONTROL_CASES, all_worlds
from src.domain import AMBIGUOUS, NO_DEPENDENCY, UNIQUE
from src.reconstruction import reconstruct
from src.regimes import ALL_REGIMES, REGIME_T1, REGIME_T2, view_for, verify_t1_t2_local_equivalence
from src.scoring import CLASS_AMBIGUOUS, CORRECT_UNIQUE, WRONG_UNIQUE, score_case


def test_every_decision_individually_reconstructable_in_both_regimes():
    for world in all_worlds():
        for regime in ALL_REGIMES:
            records = view_for(world, regime)
            answers = reconstruct(regime, records)
            assert len(answers.local_context_correct) == len(world.decisions)
            assert all(answers.local_context_correct.values()), (
                f"{world.case_id}/{regime}: a local decision fact was not reconstructable"
            )


def test_t1_t2_local_records_are_identical():
    for world in all_worlds():
        verify_t1_t2_local_equivalence(world)  # raises on any divergence


def test_ground_truth_is_not_reachable_from_regime_records():
    for world in all_worlds():
        for regime in ALL_REGIMES:
            for record in view_for(world, regime):
                assert not hasattr(record, "ground_truth")
                assert not hasattr(record, "true_edges")
                assert not hasattr(record, "true_t0")


def test_ambiguous_cases_permit_multiple_global_trajectories_under_t1():
    for case_id in ("C3-2", "C3-3", "C3-4", "C3-5"):
        world = CASE_BUILDERS[case_id]()
        records = view_for(world, REGIME_T1)
        answers = reconstruct(REGIME_T1, records)
        ambiguous_ids = world.ground_truth.ambiguous_by_construction
        assert ambiguous_ids, f"{case_id}: must declare at least one ambiguous-by-construction decision"
        for did in ambiguous_ids:
            resolution = answers.edges[did]
            assert resolution.status == AMBIGUOUS, (
                f"{case_id}/{did}: expected AMBIGUOUS under T1, got {resolution.status}"
            )
            assert resolution.candidates is not None and len(resolution.candidates) >= 2


def test_control_case_c3_1_is_uniquely_inferable_under_t1():
    world = CASE_BUILDERS["C3-1"]()
    records = view_for(world, REGIME_T1)
    answers = reconstruct(REGIME_T1, records)
    resolution = answers.edges["D2"]
    assert resolution.status == UNIQUE
    assert resolution.predecessor == "D1"


def test_negative_control_c3_6_locally_equivalent_to_c3_2_except_one_relation():
    c2 = CASE_BUILDERS["C3-2"]()
    c6 = CASE_BUILDERS["C3-6"]()
    t1_c2 = view_for(c2, REGIME_T1)
    t1_c6 = view_for(c6, REGIME_T1)
    assert len(t1_c2) == len(t1_c6)
    for r2, r6 in zip(t1_c2, t1_c6):
        assert r2.output_value == r6.output_value
        assert r2.consumed_input_value == r6.consumed_input_value
        assert r2.depends_on_most_recent == r6.depends_on_most_recent
    assert all(r.causal_trace_event is None for r in t1_c2)
    assert t1_c6[-1].causal_trace_event == "D1"

    ans_c2 = reconstruct(REGIME_T1, t1_c2)
    ans_c6 = reconstruct(REGIME_T1, t1_c6)
    assert ans_c2.edges["D3"].status == AMBIGUOUS
    assert ans_c6.edges["D3"].status == UNIQUE
    assert ans_c6.edges["D3"].predecessor == "D1"


def test_negative_control_is_declared():
    assert NEGATIVE_CONTROL_CASES == ["C3-6"]
    world = CASE_BUILDERS["C3-6"]()
    assert world.ground_truth.ambiguous_by_construction == ()


def test_reconstruction_is_deterministic():
    for world in all_worlds():
        for regime in ALL_REGIMES:
            records = view_for(world, regime)
            a1 = reconstruct(regime, records)
            a2 = reconstruct(regime, records)
            assert a1.edges == a2.edges


def test_ambiguity_is_never_scored_as_false_confidence():
    for world in all_worlds():
        records = view_for(world, REGIME_T1)
        answers = reconstruct(REGIME_T1, records)
        score = score_case(world, REGIME_T1, answers)
        for ec in score.edge_classifications:
            if ec.reconstructed_status == AMBIGUOUS:
                assert ec.classification == CLASS_AMBIGUOUS
                assert ec.classification != WRONG_UNIQUE


def test_t2_resolves_every_dependent_edge_uniquely_and_correctly():
    for world in all_worlds():
        records = view_for(world, REGIME_T2)
        answers = reconstruct(REGIME_T2, records)
        score = score_case(world, REGIME_T2, answers)
        for ec in score.edge_classifications:
            assert ec.classification == CORRECT_UNIQUE, (
                f"{world.case_id}/T2/{ec.decision_id}: T2 must resolve every dependent edge "
                f"correctly by construction (it reads the true relation directly)"
            )
        assert score.trajectory_identifiable


def test_local_decision_reconstruction_is_perfect_in_every_case_and_regime():
    for world in all_worlds():
        for regime in ALL_REGIMES:
            records = view_for(world, regime)
            answers = reconstruct(regime, records)
            score = score_case(world, regime, answers)
            assert score.local_decision_reconstruction == 1.0, (
                f"{world.case_id}/{regime}: local reconstruction must be perfect for this "
                f"experiment to isolate the trajectory-composition question"
            )
