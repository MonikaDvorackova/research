"""The ten-case perturbation matrix (experiment-design/perturbation-matrix.md)
with concrete parameters (experiment-design/implementation-spec.md Section 3).

Design license used here: implementation-spec.md Section 3 explicitly states
its numeric values are "illustrative placeholders" and that "the implementer
may substitute any concrete values that preserve each case's structural
property... without needing to revisit this design." The placeholder scores
in that table are not internally consistent with its own placeholder weights
(e.g. Case 1's evidence/weights as literally given do not produce its listed
score of 0.41). This module picks self-consistent concrete numbers that
preserve every structural property named in perturbation-matrix.md and
implementation-spec.md Section 3, and documents each deliberate choice below.

Ground truth is always anchored to the *original, t0* state -- exactly as
experimental-system.md requires ("ground truth ... is computable directly
from the case's t0 specification, independent of and prior to constructing
any regime's preserved artifacts"). A later "retroactive correction" changes
what the *queryable history* claims, never what ground truth records actually
happened.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional

from .domain import (
    AuthorityAssignment,
    DecisionBindingRecord,
    DecisionEventTrace,
    DecisionOutcomeLog,
    GroundTruth,
    ModelVersion,
    PolicyVersion,
    WatchlistEntry,
    compute_score,
    decide,
)

# Shared baseline (Cases 1,2,3,4,6,7,8,10; Case 5/9 note their own evidence).
# w1=w2=0.5, account_age_norm=0.42, prior_incidents_norm=0.40 -> score=0.41.
# Chosen so 0.41 sits strictly between the two threshold values used anywhere
# in the matrix (0.30 in Case 2's new policy, 0.45 in Case 3's "corrected"
# policy, 0.50 in the baseline policy) wherever the case requires the wrong
# policy to actually change something observable.
BASE_WEIGHTS = {"w1": 0.5, "w2": 0.5}
BASE_EVIDENCE = {"account_age_norm": 0.42, "prior_incidents_norm": 0.40}
BASE_T0 = datetime(2026, 3, 1)
BASE_T1 = datetime(2026, 4, 1)  # generic "later" transaction time for forward drift
RETRO_RECORDED_AT = datetime(2026, 5, 1)  # transaction time of retroactive corrections


@dataclass
class World:
    """Everything derivable about one decision: the full append-only
    histories (Regime B/C's queryable stores), the event trace, the
    binding record (Regime C only), Regime A's live-only snapshot, and
    ground truth (scoring-only, never exposed to a reconstruction view).
    """

    case_id: str
    category: str  # control | forward-drift | retroactive-drift | combined-drift | concurrency
    description: str
    decision_id: str
    t0: datetime
    query_time: datetime  # t1: when the investigator runs, i.e. "now"
    requester_id: str

    policy_history: List[PolicyVersion]
    authority_history: List[AuthorityAssignment]
    model_history: List[ModelVersion]
    watchlist_history: List[WatchlistEntry]

    event_trace: DecisionEventTrace
    outcome_log: DecisionOutcomeLog
    binding_record: DecisionBindingRecord

    live_policy: PolicyVersion
    live_authority: AuthorityAssignment
    live_model: ModelVersion
    live_watchlist: WatchlistEntry

    ground_truth: GroundTruth


def _policy(version_id, threshold, valid_from, valid_to, recorded_at):
    return PolicyVersion(version_id, threshold, valid_from, valid_to, recorded_at)


def _authority(agent_id, valid_from, valid_to, recorded_at, role="Approver"):
    return AuthorityAssignment(agent_id, role, valid_from, valid_to, recorded_at)


def _model(version_id, weights, valid_from, valid_to):
    return ModelVersion(version_id, weights, valid_from, valid_to)


def _watchlist(requester_id, on_watchlist, valid_from, valid_to):
    return WatchlistEntry(requester_id, on_watchlist, valid_from, valid_to)


def _build_ground_truth(
    decision_id,
    t0,
    policy: PolicyVersion,
    authority: AuthorityAssignment,
    evidence: Dict[str, float],
    model: ModelVersion,
    on_watchlist: bool,
):
    score = compute_score(evidence, model.weights)
    result = decide(score, policy.threshold, approver_present=True, on_watchlist=on_watchlist)
    justification = (
        f"score {score:.2f} {'<' if score < policy.threshold else '>='} "
        f"threshold {policy.threshold} (policy {policy.version_id}, valid from "
        f"{policy.valid_from.date()}), Approver was {authority.agent_id} "
        f"(valid from {authority.valid_from.date()}), "
        f"{'on' if on_watchlist else 'not on'} watchlist"
    )
    return GroundTruth(
        decision_id=decision_id,
        t0=t0,
        true_policy_version_id=policy.version_id,
        true_policy_valid_interval=(policy.valid_from, policy.valid_to),
        true_authority_agent_id=authority.agent_id,
        true_authority_valid_interval=(authority.valid_from, authority.valid_to),
        true_evidence_values=dict(evidence),
        true_model_version_id=model.version_id,
        true_watchlist_status_at_t0=on_watchlist,
        true_computed_score=score,
        true_result=result,
        true_justification=justification,
    ), score, result


def _build_binding(decision_id, gt: GroundTruth, policy, authority, model, watchlist_snapshot_id):
    return DecisionBindingRecord(
        decision_id=decision_id,
        policy_ref={
            "version_id": policy.version_id,
            "valid_from": policy.valid_from,
            "valid_to": policy.valid_to,
        },
        authority_ref={
            "agent_id": authority.agent_id,
            "valid_from": authority.valid_from,
            "valid_to": authority.valid_to,
        },
        model_ref={"version_id": model.version_id},
        evidence_ref={"snapshot_id": f"{decision_id}-evidence", "values": dict(gt.true_evidence_values)},
        context_ref={"snapshot_id": watchlist_snapshot_id},
    )


def _base_world(
    case_id: str,
    category: str,
    description: str,
    decision_id: str,
    requester_id: str = "R1",
    evidence: Optional[Dict[str, float]] = None,
    t0: datetime = BASE_T0,
    query_time: datetime = BASE_T1,
    on_watchlist_t0: bool = False,
) -> World:
    evidence = dict(evidence or BASE_EVIDENCE)

    policy_v1 = _policy("v1", 0.50, datetime(2026, 1, 1), None, datetime(2026, 1, 1))
    authority_a1 = _authority("Agent-1", datetime(2025, 11, 1), None, datetime(2025, 11, 1))
    model_m1 = _model("m1", dict(BASE_WEIGHTS), datetime(2025, 1, 1), None)
    watchlist_r1 = _watchlist(requester_id, on_watchlist_t0, datetime(2025, 1, 1), None)

    gt, score, result = _build_ground_truth(
        decision_id, t0, policy_v1, authority_a1, evidence, model_m1, on_watchlist_t0
    )

    trace = DecisionEventTrace(
        decision_id=decision_id,
        t0=t0,
        evidence_attributes_read=dict(evidence),
        score_computed=score,
        threshold_value_read=policy_v1.threshold,
        approver_check_result=True,
        watchlist_check_result=on_watchlist_t0,
    )
    outcome = DecisionOutcomeLog(decision_id, t0, requester_id, score, result)
    binding = _build_binding(
        decision_id, gt, policy_v1, authority_a1, model_m1, f"{decision_id}-watchlist"
    )

    return World(
        case_id=case_id,
        category=category,
        description=description,
        decision_id=decision_id,
        t0=t0,
        query_time=query_time,
        requester_id=requester_id,
        policy_history=[policy_v1],
        authority_history=[authority_a1],
        model_history=[model_m1],
        watchlist_history=[watchlist_r1],
        event_trace=trace,
        outcome_log=outcome,
        binding_record=binding,
        live_policy=policy_v1,
        live_authority=authority_a1,
        live_model=model_m1,
        live_watchlist=watchlist_r1,
        ground_truth=gt,
    )


def _close_and_append(history, index, new_row, closed_valid_to, closed_recorded_at):
    """Close out history[index]'s validity (a new row with the same
    identity but valid_to set) and append new_row in its place.

    For PolicyVersion/AuthorityAssignment (which carry recorded_at),
    reconstruction always resolves an identity via the *latest* recorded_at
    per identity (see reconstruction.py's _as_of_valid_time_latest_transaction),
    so whether or not a stale pre-close row is also kept around never
    changes any query result -- only the latest transaction-time row per
    identity is ever selected. Not retaining the stale row here keeps
    every history list unambiguous under a plain valid-time containment
    filter too, which matters for ModelVersion/WatchlistEntry: those types
    carry no recorded_at at all (per domain.py's schema -- no retroactive-
    correction case targets them), so a leftover, never-closed duplicate
    of the original row would create a genuine, unintended query ambiguity
    that has nothing to do with the mechanism under test.
    """
    old = history[index]
    if isinstance(old, PolicyVersion):
        closed = PolicyVersion(old.version_id, old.threshold, old.valid_from, closed_valid_to, closed_recorded_at)
    elif isinstance(old, AuthorityAssignment):
        closed = AuthorityAssignment(old.agent_id, old.role, old.valid_from, closed_valid_to, closed_recorded_at)
    elif isinstance(old, ModelVersion):
        closed = ModelVersion(old.version_id, old.weights, old.valid_from, closed_valid_to)
    elif isinstance(old, WatchlistEntry):
        closed = WatchlistEntry(old.requester_id, old.on_watchlist, old.valid_from, closed_valid_to)
    else:  # pragma: no cover - defensive
        raise TypeError(type(old))
    return history[:index] + history[index + 1:] + [closed, new_row]


_UNSET = object()


def _with_final_interval(gt: GroundTruth, policy_valid_to=_UNSET, authority_valid_to=_UNSET) -> GroundTruth:
    """A non-retroactive forward close (Cases 2, 4, 6/7 by omission, 9's
    authority dimension) is a legitimate resolution of ground truth: the
    version genuinely did stop applying at the moment its successor began,
    and this was never in dispute. Ground truth is updated to reflect that
    true, final interval.

    A *retroactive* correction (Cases 3, 8, 9's policy dimension) is a
    disputed, backdated claim about the past -- ground truth must NOT be
    updated to reflect it, precisely because the retroactive claim is the
    thing whose (in)correctness the experiment is testing. Case builders
    for retroactive drift never call this helper for the affected
    dimension, so ground truth stays anchored to the original, open
    interval as it stood before any correction was recorded.
    """
    policy_interval = gt.true_policy_valid_interval
    authority_interval = gt.true_authority_valid_interval
    if policy_valid_to is not _UNSET:
        policy_interval = (policy_interval[0], policy_valid_to)
    if authority_valid_to is not _UNSET:
        authority_interval = (authority_interval[0], authority_valid_to)
    return dataclasses.replace(
        gt,
        true_policy_valid_interval=policy_interval,
        true_authority_valid_interval=authority_interval,
    )


# ---------------------------------------------------------------------------
# Case 1 -- no-drift control
# ---------------------------------------------------------------------------
def case_1() -> List[World]:
    w = _base_world(
        "1", "control", "No-drift control: sanity check only.",
        "D1", query_time=BASE_T0,
    )
    return [w]


# ---------------------------------------------------------------------------
# Case 2 -- isolated policy drift (forward, non-retroactive)
# ---------------------------------------------------------------------------
def case_2() -> List[World]:
    w = _base_world("2", "forward-drift", "Isolated policy drift (forward, non-retroactive).", "D2")
    policy_v2 = _policy("v2", 0.30, BASE_T1, None, BASE_T1)
    w.policy_history = _close_and_append(w.policy_history, 0, policy_v2, BASE_T1, BASE_T1)
    w.live_policy = policy_v2
    w.ground_truth = _with_final_interval(w.ground_truth, policy_valid_to=BASE_T1)
    return [w]


# ---------------------------------------------------------------------------
# Case 3 -- isolated policy drift (RETROACTIVE) -- theoretically central case
# ---------------------------------------------------------------------------
def case_3() -> List[World]:
    w = _base_world("3", "retroactive-drift", "Isolated policy drift (retroactive correction).", "D3")
    backdated_from = datetime(2026, 2, 1)  # before t0
    policy_v1bis = _policy("v1bis", 0.45, backdated_from, None, RETRO_RECORDED_AT)
    w.policy_history = _close_and_append(w.policy_history, 0, policy_v1bis, backdated_from, RETRO_RECORDED_AT)
    w.live_policy = policy_v1bis
    w.query_time = RETRO_RECORDED_AT
    return [w]


# ---------------------------------------------------------------------------
# Case 4 -- isolated authority drift (forward, non-retroactive)
# ---------------------------------------------------------------------------
def case_4() -> List[World]:
    w = _base_world("4", "forward-drift", "Isolated authority drift (forward, non-retroactive).", "D4")
    authority_a2 = _authority("Agent-2", BASE_T1, None, BASE_T1)
    w.authority_history = _close_and_append(w.authority_history, 0, authority_a2, BASE_T1, BASE_T1)
    w.live_authority = authority_a2
    w.ground_truth = _with_final_interval(w.ground_truth, authority_valid_to=BASE_T1)
    return [w]


# ---------------------------------------------------------------------------
# Case 5 -- isolated evidence supersession
# ---------------------------------------------------------------------------
def case_5() -> List[World]:
    """An upstream incident record is later "expunged" (corrected) at t1, so
    a live query of R's profile at t1 would show incidents=0.0. Per
    reconstruction-task.md / implementation-spec.md Section 5, Regime A
    never has any per-decision evidence source (evidence is UNDETERMINED
    unconditionally in Regime A -- there is nothing to "correct" there
    because there was never anything captured). Regime B and C both read
    evidence from the immutable per-decision event trace, not from any live
    upstream profile, so both retain the true t0 value (incidents=0.40)
    regardless of the later upstream correction. This case therefore tests
    whether B's event-trace design already handles supersession correctly
    (expected: yes, for both B and C identically) -- perturbation-matrix.md's
    predicted non-difference."""
    w = _base_world("5", "forward-drift", "Isolated evidence supersession (upstream correction).", "D5")
    return [w]


# ---------------------------------------------------------------------------
# Case 6 -- isolated context drift (watchlist, forward, non-retroactive)
# ---------------------------------------------------------------------------
def case_6() -> List[World]:
    w = _base_world("6", "forward-drift", "Isolated context drift (watchlist, forward).", "D6")
    watchlist_new = _watchlist(w.requester_id, True, BASE_T1, None)
    w.watchlist_history = _close_and_append(w.watchlist_history, 0, watchlist_new, BASE_T1, BASE_T1)
    w.live_watchlist = watchlist_new
    return [w]


# ---------------------------------------------------------------------------
# Case 7 -- isolated model/config drift (forward, non-retroactive)
# ---------------------------------------------------------------------------
def case_7() -> List[World]:
    w = _base_world("7", "forward-drift", "Isolated model/config drift (forward, non-retroactive).", "D7")
    model_m2 = _model("m2", {"w1": 0.2, "w2": 0.8}, BASE_T1, None)
    w.model_history = _close_and_append(w.model_history, 0, model_m2, BASE_T1, BASE_T1)
    w.live_model = model_m2
    return [w]


# ---------------------------------------------------------------------------
# Case 8 -- combined drift (policy + authority, both retroactive)
# ---------------------------------------------------------------------------
def case_8() -> List[World]:
    w = _base_world("8", "combined-drift", "Combined retroactive drift (policy AND authority).", "D8")
    backdated_policy_from = datetime(2026, 2, 1)
    policy_v1bis = _policy("v1bis", 0.45, backdated_policy_from, None, RETRO_RECORDED_AT)
    w.policy_history = _close_and_append(w.policy_history, 0, policy_v1bis, backdated_policy_from, RETRO_RECORDED_AT)
    w.live_policy = policy_v1bis

    backdated_auth_from = datetime(2026, 2, 15)  # before t0
    authority_a3 = _authority("Agent-3", backdated_auth_from, None, RETRO_RECORDED_AT)
    w.authority_history = _close_and_append(w.authority_history, 0, authority_a3, backdated_auth_from, RETRO_RECORDED_AT)
    w.live_authority = authority_a3

    w.query_time = RETRO_RECORDED_AT
    return [w]


# ---------------------------------------------------------------------------
# Case 9 -- combined drift, all five dimensions, mixed forward/retroactive
# ---------------------------------------------------------------------------
def case_9() -> List[World]:
    w = _base_world("9", "combined-drift", "Combined drift, all five dimensions, mixed forward/retroactive.", "D9")

    # Retroactive policy correction (as Case 3).
    backdated_policy_from = datetime(2026, 2, 1)
    policy_v1bis = _policy("v1bis", 0.45, backdated_policy_from, None, RETRO_RECORDED_AT)
    w.policy_history = _close_and_append(w.policy_history, 0, policy_v1bis, backdated_policy_from, RETRO_RECORDED_AT)
    w.live_policy = policy_v1bis

    # Forward authority reassignment (as Case 4).
    authority_a2 = _authority("Agent-2", BASE_T1, None, BASE_T1)
    w.authority_history = _close_and_append(w.authority_history, 0, authority_a2, BASE_T1, BASE_T1)
    w.live_authority = authority_a2
    w.ground_truth = _with_final_interval(w.ground_truth, authority_valid_to=BASE_T1)

    # Evidence supersession (as Case 5): handled by live_* vs. event-trace
    # distinction, no history table change needed (evidence has no history
    # table in this design -- only the per-decision trace and any live
    # upstream profile).

    # Forward watchlist addition (as Case 6).
    watchlist_new = _watchlist(w.requester_id, True, BASE_T1, None)
    w.watchlist_history = _close_and_append(w.watchlist_history, 0, watchlist_new, BASE_T1, BASE_T1)
    w.live_watchlist = watchlist_new

    # Forward model drift (as Case 7).
    model_m2 = _model("m2", {"w1": 0.2, "w2": 0.8}, BASE_T1, None)
    w.model_history = _close_and_append(w.model_history, 0, model_m2, BASE_T1, BASE_T1)
    w.live_model = model_m2

    w.query_time = RETRO_RECORDED_AT
    return [w]


# ---------------------------------------------------------------------------
# Case 10 -- concurrency / attribution ambiguity
# ---------------------------------------------------------------------------
def case_10() -> List[World]:
    """Two decisions, D_x and D_y, straddling a policy validity boundary.
    No retroactive drift: the boundary was always where it is; the only
    question is whether an as-of-timestamp query attributes each decision
    to the correct side of the boundary.

    Per implementation-spec.md Section 5's note, whether Regime B's
    algorithm resolves this unambiguously or detects a genuine ambiguity is
    itself part of what the experiment measures. This implementation models
    the boundary precisely (v1 valid_to == the boundary instant, v2
    valid_from == the same instant) and lets the standard half-open
    valid-time interval semantics used everywhere else in this codebase
    (valid_from <= t < valid_to) determine the outcome, rather than
    injecting an artificial ambiguity not implied by the design's own
    query semantics. This is the "documented limitation" branch flagged as
    open in implementation-spec.md Section 7, not a fault-injection case.
    """
    boundary = datetime(2026, 3, 1, 12, 0, 0)
    t0_x = datetime(2026, 3, 1, 11, 59, 0)
    t0_y = datetime(2026, 3, 1, 12, 1, 0)

    policy_v1 = _policy("v1", 0.50, datetime(2026, 1, 1), boundary, datetime(2026, 1, 1))
    policy_v2 = _policy("v2", 0.30, boundary, None, boundary)
    authority_a1 = _authority("Agent-1", datetime(2025, 11, 1), None, datetime(2025, 11, 1))
    model_m1 = _model("m1", dict(BASE_WEIGHTS), datetime(2025, 1, 1), None)

    worlds = []
    for decision_id, requester_id, t0, policy in (
        ("D10x", "Rx", t0_x, policy_v1),
        ("D10y", "Ry", t0_y, policy_v2),
    ):
        evidence = dict(BASE_EVIDENCE)
        watchlist = _watchlist(requester_id, False, datetime(2025, 1, 1), None)
        gt, score, result = _build_ground_truth(
            decision_id, t0, policy, authority_a1, evidence, model_m1, False
        )
        trace = DecisionEventTrace(
            decision_id=decision_id, t0=t0, evidence_attributes_read=dict(evidence),
            score_computed=score, threshold_value_read=policy.threshold,
            approver_check_result=True, watchlist_check_result=False,
        )
        outcome = DecisionOutcomeLog(decision_id, t0, requester_id, score, result)
        binding = _build_binding(decision_id, gt, policy, authority_a1, model_m1, f"{decision_id}-watchlist")
        worlds.append(World(
            case_id="10", category="concurrency",
            description="Concurrency/attribution ambiguity across a policy validity boundary.",
            decision_id=decision_id, t0=t0, query_time=boundary + timedelta(days=31),
            requester_id=requester_id,
            policy_history=[policy_v1, policy_v2],
            authority_history=[authority_a1],
            model_history=[model_m1],
            watchlist_history=[watchlist],
            event_trace=trace, outcome_log=outcome, binding_record=binding,
            live_policy=policy_v2, live_authority=authority_a1,
            live_model=model_m1, live_watchlist=watchlist,
            ground_truth=gt,
        ))
    return worlds


CASE_BUILDERS = {
    "1": case_1, "2": case_2, "3": case_3, "4": case_4, "5": case_5,
    "6": case_6, "7": case_7, "8": case_8, "9": case_9, "10": case_10,
}

# Case ids expected to fail on Regime A per the manipulation check
# (validity-and-confounders.md): all forward-drift cases where "current
# live" != "what applied at t0".
MANIPULATION_CHECK_CASE_IDS = ["2", "4", "6", "7"]

CASE_CATEGORY_ORDER = [
    "control", "forward-drift", "retroactive-drift", "combined-drift", "concurrency",
]


def all_worlds() -> List[World]:
    worlds = []
    for case_id in sorted(CASE_BUILDERS, key=lambda c: int(c)):
        worlds.extend(CASE_BUILDERS[case_id]())
    return worlds
