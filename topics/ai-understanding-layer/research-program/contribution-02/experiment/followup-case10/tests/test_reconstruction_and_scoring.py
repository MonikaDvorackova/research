"""Step 12 required checks:
- no-drift/no-ambiguity control works in both B and C;
- false confidence scoring distinguishes WRONG from AMBIGUOUS;
plus determinism and hand-verified scoring, mirroring the primary
experiment's own pre-execution test discipline.
"""

from src.cases import all_worlds
from src.domain import AMBIGUOUS, DENY, GRANT, UNDETERMINED, UNIQUE
from src.reconstruction import reconstruct
from src.regimes import view_for
from src.scoring import CORRECT_UNIQUE, WRONG_UNIQUE, score_case


def _world(case_id):
    return next(w for w in all_worlds() if w.case_id == case_id)


def test_f10_1_control_both_regimes_fully_correct():
    world = _world("F10-1")
    for regime in ("B", "C"):
        answers = reconstruct(regime, view_for(world, regime))
        score = score_case(world, regime, answers)
        assert score.tc == 1
        assert score.urr == 1.0
        assert score.fhc_rate == 0.0
        assert score.adr is None  # no ambiguous dimension in this case


def test_reconstruction_is_deterministic():
    world = _world("F10-5")
    for regime in ("B", "C"):
        view = view_for(world, regime)
        a1 = reconstruct(regime, view)
        a2 = reconstruct(regime, view)
        assert a1 == a2


def test_f10_2_b_reports_ambiguous_not_wrong_and_c_resolves_correctly():
    world = _world("F10-2")
    b_answers = reconstruct("B", view_for(world, "B"))
    b_score = score_case(world, "B", b_answers)
    assert b_answers.policy.status == AMBIGUOUS
    assert b_score.policy_class == AMBIGUOUS  # not WRONG_UNIQUE
    assert b_score.fhc_rate == 0.0  # an honest AMBIGUOUS must never count as false confidence
    assert b_score.adr == 1.0  # correctly detected the one ambiguous dimension
    assert b_answers.authorized_at_t0 == UNDETERMINED  # never guesses through an ambiguous policy

    c_answers = reconstruct("C", view_for(world, "C"))
    c_score = score_case(world, "C", c_answers)
    assert c_score.policy_class == CORRECT_UNIQUE
    assert c_score.tc == 1
    # v2's threshold (0.30) is below the fixed evidence score (0.41), so
    # the true, correctly-reconstructed result here is DENY, not GRANT --
    # see case-matrix.md's note on this.
    assert c_answers.authorized_at_t0 == DENY


def test_false_confidence_and_ambiguous_are_scored_differently_hand_verified():
    """Hand-verified: construct one WRONG_UNIQUE case and one AMBIGUOUS
    case with otherwise identical structure, and confirm only the former
    contributes to fhc_rate."""
    from src.domain import Resolution
    from src.reconstruction import FollowupAnswers
    from src.scoring import score_case

    world = _world("F10-2")
    gt = world.ground_truth  # true_policy_version_id == "v2"

    wrong_confident = FollowupAnswers(
        decision_id=world.decision_id, requester_id="R1", result=GRANT,
        evidence_values=dict(gt.true_evidence_values),
        policy=Resolution(status=UNIQUE, value={"version_id": "v1", "valid_from": None, "valid_to": None, "threshold": 0.50}),
        authority=Resolution(status=UNIQUE, value={"agent_id": gt.true_authority_agent_id}),
        model=Resolution(status=UNIQUE, value={"version_id": gt.true_model_version_id}),
        authorized_at_t0=GRANT,
    )
    honestly_ambiguous = FollowupAnswers(
        decision_id=world.decision_id, requester_id="R1", result=GRANT,
        evidence_values=dict(gt.true_evidence_values),
        policy=Resolution(status=AMBIGUOUS, candidates=(
            {"version_id": "v1"}, {"version_id": "v2"},
        )),
        authority=Resolution(status=UNIQUE, value={"agent_id": gt.true_authority_agent_id}),
        model=Resolution(status=UNIQUE, value={"version_id": gt.true_model_version_id}),
        authorized_at_t0=UNDETERMINED,
    )

    wrong_score = score_case(world, "B", wrong_confident)
    ambiguous_score = score_case(world, "B", honestly_ambiguous)

    assert wrong_score.policy_class == WRONG_UNIQUE
    assert wrong_score.fhc_rate > 0.0
    assert ambiguous_score.policy_class == AMBIGUOUS
    assert ambiguous_score.fhc_rate == 0.0
    assert wrong_score.tc == 0 and ambiguous_score.tc == 0  # both fail TC...
    assert wrong_score.fhc_rate != ambiguous_score.fhc_rate  # ...but are not the same kind of failure


def test_f10_6_negative_control_causal_event_lets_b_match_c():
    """This is a genuine result check, not just a construction check --
    it is included here (pre-execution) because case-matrix.md's own
    F10-6 design already fixes what causal_consumption_event contains
    (the true consumed version), so whether B *can* use it correctly is
    an implementation-correctness property to verify before freezing,
    not an experimental outcome to discover after."""
    world = _world("F10-6")
    b_answers = reconstruct("B", view_for(world, "B"))
    c_answers = reconstruct("C", view_for(world, "C"))
    b_score = score_case(world, "B", b_answers)
    c_score = score_case(world, "C", c_answers)
    assert b_score.policy_class == CORRECT_UNIQUE
    assert b_score.tc == c_score.tc == 1
    assert b_answers.policy.value["version_id"] == c_answers.policy.value["version_id"]
