"""Invariant checks required by PHASE 1G before execution:
(5) temporal interval logic is correct;
(6) transaction-time / valid-time distinctions work;
(8) scoring matches hand-verified examples.
"""

from datetime import datetime, timedelta

from src.cases import CASE_BUILDERS
from src.domain import GRANT, UNDETERMINED, AuthorityAssignment, GroundTruth, PolicyVersion
from src.reconstruction import Answers, _as_of_valid_time, _as_of_valid_time_latest_transaction
from src.scoring import score_case


def test_as_of_valid_time_containment():
    t0 = datetime(2026, 3, 1)
    before = PolicyVersion("v0", 0.6, datetime(2025, 1, 1), datetime(2026, 1, 1), datetime(2025, 1, 1))
    during = PolicyVersion("v1", 0.5, datetime(2026, 1, 1), datetime(2026, 6, 1), datetime(2026, 1, 1))
    after = PolicyVersion("v2", 0.4, datetime(2026, 6, 1), None, datetime(2026, 6, 1))
    matches = _as_of_valid_time([before, during, after], t0)
    assert matches == [during]


def test_as_of_valid_time_boundary_is_half_open():
    boundary = datetime(2026, 3, 1, 12, 0, 0)
    before = PolicyVersion("v1", 0.5, datetime(2026, 1, 1), boundary, datetime(2026, 1, 1))
    after = PolicyVersion("v2", 0.3, boundary, None, boundary)
    assert _as_of_valid_time([before, after], boundary - timedelta(minutes=1)) == [before]
    assert _as_of_valid_time([before, after], boundary) == [after]


def test_transaction_time_correction_changes_the_as_of_t0_answer():
    """The same as-of-t0 valid-time question, asked against two different
    transaction-time states of the same table, must return different
    answers when a retroactive correction has been recorded in between --
    this is the transaction-time/valid-time confound the design predicts
    (preservation-regimes.md's bitemporal section)."""
    t0 = datetime(2026, 3, 1)
    original = PolicyVersion("v1", 0.50, datetime(2026, 1, 1), None, datetime(2026, 1, 1))

    # Before the correction is recorded, only the original row exists.
    pre_correction_matches = _as_of_valid_time_latest_transaction(
        [original], t0, key_fn=lambda p: p.version_id
    )
    assert len(pre_correction_matches) == 1
    assert pre_correction_matches[0].version_id == "v1"

    # After a retroactive correction is recorded (a closed copy of v1 plus
    # a backdated v1bis, both with a later recorded_at), the same as-of-t0
    # query -- run against the now-current transaction state -- returns a
    # different version.
    retro_recorded_at = datetime(2026, 5, 1)
    backdated_from = datetime(2026, 2, 1)
    closed_v1 = PolicyVersion("v1", 0.50, datetime(2026, 1, 1), backdated_from, retro_recorded_at)
    v1bis = PolicyVersion("v1bis", 0.45, backdated_from, None, retro_recorded_at)
    post_correction_matches = _as_of_valid_time_latest_transaction(
        [original, closed_v1, v1bis], t0, key_fn=lambda p: p.version_id
    )
    assert len(post_correction_matches) == 1
    assert post_correction_matches[0].version_id == "v1bis"
    assert post_correction_matches[0].version_id != pre_correction_matches[0].version_id


def _make_gt():
    return GroundTruth(
        decision_id="D-test", t0=datetime(2026, 3, 1),
        true_policy_version_id="v1",
        true_policy_valid_interval=(datetime(2026, 1, 1), None),
        true_authority_agent_id="Agent-1",
        true_authority_valid_interval=(datetime(2025, 11, 1), None),
        true_evidence_values={"account_age_norm": 0.42, "prior_incidents_norm": 0.40},
        true_model_version_id="m1",
        true_watchlist_status_at_t0=False,
        true_computed_score=0.41,
        true_result=GRANT,
        true_justification="hand-verified fixture",
    )


def _make_world_stub(gt):
    class Stub:
        pass
    stub = Stub()
    stub.case_id = "hand-verified"
    stub.category = "control"
    stub.decision_id = gt.decision_id
    stub.ground_truth = gt
    return stub


def test_score_case_hand_verified_all_correct():
    gt = _make_gt()
    world = _make_world_stub(gt)
    answers = Answers(
        decision_id="D-test", requester_id="R1", result=GRANT,
        evidence_values={"account_age_norm": 0.42, "prior_incidents_norm": 0.40},
        policy_label="threshold rule",
        policy_version={"version_id": "v1", "valid_from": datetime(2026, 1, 1), "valid_to": None},
        authority_identity={"agent_id": "Agent-1", "role": "Approver"},
        authority_version={"agent_id": "Agent-1", "valid_from": datetime(2025, 11, 1), "valid_to": None},
        model_version="m1",
        authorized_at_t0=GRANT,
        justification={"evidence_ref": {}, "policy_ref": {}, "authority_ref": {}},
    )
    score = score_case(world, "C", answers)
    assert score.aia == 1.0
    assert score.tc == 1
    assert score.ac == 1
    assert score.jc == 1.0
    assert score.fhc_policy == 0
    assert score.fhc_authority == 0
    assert score.fhc_rate == 0.0


def test_score_case_hand_verified_confidently_wrong_policy_is_false_historical_confidence():
    gt = _make_gt()
    world = _make_world_stub(gt)
    answers = Answers(
        decision_id="D-test", requester_id="R1", result=GRANT,
        evidence_values={"account_age_norm": 0.42, "prior_incidents_norm": 0.40},
        policy_label="threshold rule",
        # Confident, concrete, but WRONG policy version (different id).
        policy_version={"version_id": "v1bis", "valid_from": datetime(2026, 2, 1), "valid_to": None},
        authority_identity={"agent_id": "Agent-1", "role": "Approver"},
        authority_version={"agent_id": "Agent-1", "valid_from": datetime(2025, 11, 1), "valid_to": None},
        model_version="m1",
        authorized_at_t0=GRANT,
        justification={"evidence_ref": {}, "policy_ref": {}, "authority_ref": {}},
    )
    score = score_case(world, "B", answers)
    assert score.tc == 0  # temporally wrong on policy
    assert score.fhc_policy == 1  # concrete AND wrong -> false historical confidence
    assert score.fhc_authority == 0  # authority was correct
    assert score.aia_detail["policy"] is False


def test_score_case_hand_verified_honest_undetermined_is_not_false_confidence():
    gt = _make_gt()
    world = _make_world_stub(gt)
    answers = Answers(
        decision_id="D-test", requester_id="R1", result=GRANT,
        evidence_values=UNDETERMINED,
        policy_label="threshold rule",
        policy_version=UNDETERMINED,
        authority_identity=UNDETERMINED,
        authority_version=UNDETERMINED,
        model_version=UNDETERMINED,
        authorized_at_t0=UNDETERMINED,
        justification=UNDETERMINED,
    )
    score = score_case(world, "A", answers)
    assert score.tc == 0  # not temporally correct...
    assert score.fhc_policy == 0  # ...but honestly so, not a false-confidence failure
    assert score.fhc_authority == 0
    assert score.jc == 0.0
    assert score.ac == 0


def test_case_10_boundary_partition_matches_documented_clean_semantics():
    worlds = CASE_BUILDERS["10"]()
    assert len(worlds) == 2
    dx, dy = worlds
    assert dx.ground_truth.true_policy_version_id == "v1"
    assert dy.ground_truth.true_policy_version_id == "v2"
