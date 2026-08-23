"""The six-case follow-up matrix (case-matrix.md), built exactly to the
locked parameters there. No case uses a backdated valid_from or a
corrected recorded_at -- this follow-up tests observational precision
loss only, never retroactive correction (already tested by the primary
experiment).

Scope note: this follow-up implements Regime B and Regime C only. Regime
A (bare) was already established as a floor/manipulation-check condition
by the primary experiment and is not part of this follow-up's research
question (research-question.md) or the authorizing instructions' Step 14
("the primary comparison remains B vs C") -- it is out of scope here by
deliberate, disclosed choice, not omission.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

from .domain import (
    GRANT,
    AuthorityAssignment,
    DecisionBindingRecord,
    DecisionOutcomeLog,
    FollowupEventTrace,
    FollowupGroundTruth,
    ModelVersion,
    PolicyVersion,
    WatchlistEntry,
    compute_score,
    decide,
    observed_t0,
)

BASE_EVIDENCE = {"account_age_norm": 0.42, "prior_incidents_norm": 0.40}
WEIGHTS_M1 = {"w1": 0.5, "w2": 0.5}
WEIGHTS_M2 = {"w1": 0.2, "w2": 0.8}

BOUNDARY = datetime(2026, 3, 1, 12, 0, 0, 500000)  # inside the observable bucket
TRUE_T0_AMBIGUOUS = datetime(2026, 3, 1, 12, 0, 0, 750000)  # strictly after BOUNDARY
TRUE_T0_CONTROL = datetime(2026, 3, 1, 12, 0, 0, 200000)  # no boundary nearby


@dataclass
class World:
    case_id: str
    description: str
    decision_id: str
    true_t0: datetime  # ground-truth only, never exposed to any regime view
    requester_id: str

    policy_history: List[PolicyVersion]
    authority_history: List[AuthorityAssignment]
    model_history: List[ModelVersion]
    watchlist_history: List[WatchlistEntry]

    event_trace: FollowupEventTrace
    outcome_log: DecisionOutcomeLog
    binding_record: DecisionBindingRecord

    ground_truth: FollowupGroundTruth


def _wide_open_policy(valid_to: Optional[datetime] = None) -> PolicyVersion:
    return PolicyVersion("v1", 0.50, datetime(2026, 1, 1), valid_to, datetime(2026, 1, 1))


def _wide_open_authority(valid_to: Optional[datetime] = None) -> AuthorityAssignment:
    return AuthorityAssignment("Agent-1", "Approver", datetime(2025, 11, 1), valid_to, datetime(2025, 11, 1))


def _wide_open_model(valid_to: Optional[datetime] = None) -> ModelVersion:
    return ModelVersion("m1", dict(WEIGHTS_M1), datetime(2025, 1, 1), valid_to)


def _wide_open_watchlist(requester_id: str) -> WatchlistEntry:
    return WatchlistEntry(requester_id, False, datetime(2025, 1, 1), None)


def _build(
    case_id: str,
    description: str,
    decision_id: str,
    true_t0: datetime,
    policy_history: List[PolicyVersion],
    authority_history: List[AuthorityAssignment],
    model_history: List[ModelVersion],
    true_policy_version_id: str,
    true_authority_agent_id: str,
    true_model_version_id: str,
    ambiguous_dimensions: Tuple[str, ...],
    causal_consumption_event: Optional[Dict] = None,
    requester_id: str = "R1",
) -> World:
    evidence = dict(BASE_EVIDENCE)
    true_policy = next(p for p in policy_history if p.version_id == true_policy_version_id)
    true_authority = next(a for a in authority_history if a.agent_id == true_authority_agent_id)
    true_model = next(m for m in model_history if m.version_id == true_model_version_id)
    watchlist = _wide_open_watchlist(requester_id)

    score = compute_score(evidence, true_model.weights)
    result = decide(score, true_policy.threshold, approver_present=True, on_watchlist=False)

    obs_t0 = observed_t0(true_t0)
    trace = FollowupEventTrace(
        decision_id=decision_id,
        observed_t0=obs_t0,
        evidence_attributes_read=dict(evidence),
        score_computed=score,
        approver_check_result=True,
        watchlist_check_result=False,
        causal_consumption_event=causal_consumption_event,
    )
    outcome = DecisionOutcomeLog(decision_id, obs_t0, requester_id, score, result)
    binding = DecisionBindingRecord(
        decision_id=decision_id,
        policy_ref={"version_id": true_policy.version_id, "valid_from": true_policy.valid_from, "valid_to": true_policy.valid_to},
        authority_ref={"agent_id": true_authority.agent_id, "valid_from": true_authority.valid_from, "valid_to": true_authority.valid_to},
        model_ref={"version_id": true_model.version_id},
        evidence_ref={"snapshot_id": f"{decision_id}-evidence", "values": dict(evidence)},
        context_ref={"snapshot_id": f"{decision_id}-watchlist"},
    )
    gt = FollowupGroundTruth(
        decision_id=decision_id,
        true_t0=true_t0,
        observed_t0=obs_t0,
        true_policy_version_id=true_policy.version_id,
        true_authority_agent_id=true_authority.agent_id,
        true_model_version_id=true_model.version_id,
        true_evidence_values=dict(evidence),
        true_watchlist_status_at_t0=False,
        true_computed_score=score,
        true_result=result,
        ambiguous_dimensions=ambiguous_dimensions,
    )
    return World(
        case_id=case_id, description=description, decision_id=decision_id, true_t0=true_t0,
        requester_id=requester_id,
        policy_history=policy_history, authority_history=authority_history, model_history=model_history,
        watchlist_history=[watchlist],
        event_trace=trace, outcome_log=outcome, binding_record=binding, ground_truth=gt,
    )


def case_f10_1() -> World:
    return _build(
        case_id="F10-1", description="No-ambiguity control: no version boundary near the observable bucket.",
        decision_id="DF1", true_t0=TRUE_T0_CONTROL,
        policy_history=[_wide_open_policy()],
        authority_history=[_wide_open_authority()],
        model_history=[_wide_open_model()],
        true_policy_version_id="v1", true_authority_agent_id="Agent-1", true_model_version_id="m1",
        ambiguous_dimensions=(),
    )


def case_f10_2() -> World:
    v1 = _wide_open_policy(valid_to=BOUNDARY)
    v2 = PolicyVersion("v2", 0.30, BOUNDARY, None, BOUNDARY)
    return _build(
        case_id="F10-2", description="Policy-only ambiguity: v1/v2 boundary falls inside the observable bucket.",
        decision_id="DF2", true_t0=TRUE_T0_AMBIGUOUS,
        policy_history=[v1, v2],
        authority_history=[_wide_open_authority()],
        model_history=[_wide_open_model()],
        true_policy_version_id="v2", true_authority_agent_id="Agent-1", true_model_version_id="m1",
        ambiguous_dimensions=("policy",),
    )


def case_f10_3() -> World:
    a1 = _wide_open_authority(valid_to=BOUNDARY)
    a2 = AuthorityAssignment("Agent-2", "Approver", BOUNDARY, None, BOUNDARY)
    return _build(
        case_id="F10-3", description="Authority-only ambiguity: Agent-1/Agent-2 boundary inside the observable bucket.",
        decision_id="DF3", true_t0=TRUE_T0_AMBIGUOUS,
        policy_history=[_wide_open_policy()],
        authority_history=[a1, a2],
        model_history=[_wide_open_model()],
        true_policy_version_id="v1", true_authority_agent_id="Agent-2", true_model_version_id="m1",
        ambiguous_dimensions=("authority",),
    )


def case_f10_4() -> World:
    m1 = _wide_open_model(valid_to=BOUNDARY)
    m2 = ModelVersion("m2", dict(WEIGHTS_M2), BOUNDARY, None)
    return _build(
        case_id="F10-4", description="Model/config-only ambiguity: m1/m2 boundary inside the observable bucket.",
        decision_id="DF4", true_t0=TRUE_T0_AMBIGUOUS,
        policy_history=[_wide_open_policy()],
        authority_history=[_wide_open_authority()],
        model_history=[m1, m2],
        true_policy_version_id="v1", true_authority_agent_id="Agent-1", true_model_version_id="m2",
        ambiguous_dimensions=("model",),
    )


def case_f10_5() -> World:
    v1 = _wide_open_policy(valid_to=BOUNDARY)
    v2 = PolicyVersion("v2", 0.30, BOUNDARY, None, BOUNDARY)
    a1 = _wide_open_authority(valid_to=BOUNDARY)
    a2 = AuthorityAssignment("Agent-2", "Approver", BOUNDARY, None, BOUNDARY)
    return _build(
        case_id="F10-5", description="Combined ambiguity: policy AND authority boundaries both inside the observable bucket.",
        decision_id="DF5", true_t0=TRUE_T0_AMBIGUOUS,
        policy_history=[v1, v2],
        authority_history=[a1, a2],
        model_history=[_wide_open_model()],
        true_policy_version_id="v2", true_authority_agent_id="Agent-2", true_model_version_id="m1",
        ambiguous_dimensions=("policy", "authority"),
    )


def case_f10_6() -> World:
    """Negative control: identical to F10-2, except Regime B additionally
    receives a causal_consumption_event (case-matrix.md), never called a
    'binding'. Regime C is unchanged from every other case."""
    v1 = _wide_open_policy(valid_to=BOUNDARY)
    v2 = PolicyVersion("v2", 0.30, BOUNDARY, None, BOUNDARY)
    return _build(
        case_id="F10-6", description="Negative control: policy ambiguity as F10-2, plus a causal consumption event on B only.",
        decision_id="DF6", true_t0=TRUE_T0_AMBIGUOUS,
        policy_history=[v1, v2],
        authority_history=[_wide_open_authority()],
        model_history=[_wide_open_model()],
        true_policy_version_id="v2", true_authority_agent_id="Agent-1", true_model_version_id="m1",
        ambiguous_dimensions=("policy",),
        causal_consumption_event={"policy_version_id": "v2"},
    )


CASE_BUILDERS = {
    "F10-1": case_f10_1, "F10-2": case_f10_2, "F10-3": case_f10_3,
    "F10-4": case_f10_4, "F10-5": case_f10_5, "F10-6": case_f10_6,
}

AMBIGUOUS_CASE_IDS = ["F10-2", "F10-3", "F10-4", "F10-5", "F10-6"]
CONTROL_CASE_IDS = ["F10-1"]
NEGATIVE_CONTROL_CASE_IDS = ["F10-6"]


def all_worlds() -> List[World]:
    return [CASE_BUILDERS[k]() for k in sorted(CASE_BUILDERS)]
