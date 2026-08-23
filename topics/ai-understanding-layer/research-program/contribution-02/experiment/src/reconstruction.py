"""The deterministic reconstruction procedure (experiment-design/
reconstruction-task.md, implementation-spec.md Section 5).

One algorithm shape, `reconstruct(regime, view)`, applied identically in
structure across all three regimes -- it differs only in which artifacts
each regime's view (regimes.py) actually exposes, never in reasoning
sophistication. This is the internal-validity control validity-and-
confounders.md requires: Regime B's as-of-t0 query is the objectively
correct use of bitemporal valid-time semantics (a genuine interval match
against the *latest known transaction state*, per dependency identity),
not a weakened heuristic.

Two questions (reconstruction-task.md's numbered list) are answered by
direct log/trace read in every regime and are not separately graded
(Q1, Q3, Q5's free-text label, Q8's structure -- Q8's *content* is graded
indirectly through Q2/Q4/Q6). The four version-bearing dependencies scored
by AIA/JC (metrics-and-scoring.md) are: evidence, policy version, authority
version, model version.

One documented completion of the design, not a redesign: implementation-
spec.md's Section 5 pseudocode is silent on how model-version and
watchlist-status are resolved (it only shows explicit query logic for
policy and authority). This module resolves them by the same principle
applied everywhere else: Regime A reads whatever is "live" (per
preservation-regimes.md, live policy/authority/watchlist values ARE
queryable in Regime A); Regime B/C read watchlist status directly from the
immutable per-decision event trace (already true for evidence, and
watchlist_check_result is a raw captured value of the same kind, not a
version-dependent lookup); and Regime B resolves model version via the
same as-of-t0 valid-time interval match used for policy (model has a
valid_from/valid_to history table but, per domain.py's schema, no
recorded_at/correction dimension, so no retroactive-correction case
targets it). Regime C reads model version directly from the binding
record. Neither Temporal Correctness nor False Historical Confidence
(the two primary/diagnostic metrics) score model or watchlist at all
(metrics-and-scoring.md scopes TC/FHC to Q4/Q6 -- policy and authority --
only), so this completion cannot affect the primary comparison.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from .domain import UNDETERMINED, compute_score, decide
from .regimes import REGIME_A, REGIME_B, REGIME_C, RegimeAView, RegimeBView, RegimeCView

Undetermined = str  # the literal token "UNDETERMINED"


@dataclass(frozen=True)
class Answers:
    decision_id: str
    requester_id: str
    result: str  # Q1 (component): the actual historical outcome-log result
    evidence_values: Union[Dict[str, float], Undetermined]  # Q2
    policy_label: str  # Q3
    policy_version: Union[Dict, Undetermined]  # Q4
    authority_identity: Union[Dict, Undetermined]  # Q5
    authority_version: Union[Dict, Undetermined]  # Q6
    model_version: Union[str, Undetermined]  # AIA/JC dependency, not part of Q1-8's numbering
    authorized_at_t0: Union[str, Undetermined]  # Q7: "GRANT" | "DENY" | "UNDETERMINED"
    justification: Union[Dict, Undetermined]  # Q8


def _as_of_valid_time_latest_transaction(rows, t0, key_fn, role_filter=None):
    """Standard bitemporal query: 'as of valid-time t0, using the latest
    known transaction-time state.' For each distinct identity, keep only
    the row with the greatest recorded_at (the most recent correction,
    if any), then filter for valid_from <= t0 < valid_to-or-open."""
    latest = {}
    for row in rows:
        if role_filter is not None and getattr(row, "role", None) != role_filter:
            continue
        key = key_fn(row)
        current = latest.get(key)
        if current is None or row.recorded_at > current.recorded_at:
            latest[key] = row
    return [
        row for row in latest.values()
        if row.valid_from <= t0 and (row.valid_to is None or t0 < row.valid_to)
    ]


def _as_of_valid_time(rows, t0):
    return [
        row for row in rows
        if row.valid_from <= t0 and (row.valid_to is None or t0 < row.valid_to)
    ]


def _policy_dict(p) -> Dict:
    return {"version_id": p.version_id, "valid_from": p.valid_from, "valid_to": p.valid_to}


def _authority_dict(a) -> Dict:
    return {"agent_id": a.agent_id, "valid_from": a.valid_from, "valid_to": a.valid_to}


def _authorize(evidence, weights, threshold, approver_present, on_watchlist) -> str:
    if (
        evidence is UNDETERMINED
        or weights is None
        or threshold is None
        or approver_present is None
        or on_watchlist is None
    ):
        return UNDETERMINED
    score = compute_score(evidence, weights)
    return decide(score, threshold, approver_present, on_watchlist)


def _justification(evidence, policy_answer, authority_answer, q7) -> Union[Dict, str]:
    if UNDETERMINED in (evidence, policy_answer, authority_answer, q7):
        return UNDETERMINED
    return {"evidence_ref": evidence, "policy_ref": policy_answer, "authority_ref": authority_answer}


def _reconstruct_a(view: RegimeAView) -> Answers:
    outcome = view.outcome
    policy_answer = _policy_dict(view.live_policy)
    authority_answer = _authority_dict(view.live_authority)
    authority_identity = {"agent_id": view.live_authority.agent_id, "role": view.live_authority.role}
    model_version = view.live_model.version_id
    evidence = UNDETERMINED  # no per-decision trace exists in Regime A, ever
    q7 = _authorize(
        evidence=evidence,
        weights=view.live_model.weights,
        threshold=view.live_policy.threshold,
        approver_present=True,
        on_watchlist=view.live_watchlist.on_watchlist,
    )
    return Answers(
        decision_id=outcome.decision_id,
        requester_id=outcome.requester_id,
        result=outcome.result,
        evidence_values=evidence,
        policy_label="threshold rule",
        policy_version=policy_answer,
        authority_identity=authority_identity,
        authority_version=authority_answer,
        model_version=model_version,
        authorized_at_t0=q7,
        justification=_justification(evidence, policy_answer, authority_answer, q7),
    )


def _reconstruct_b(view: RegimeBView) -> Answers:
    outcome = view.outcome
    trace = view.event_trace
    evidence = dict(trace.evidence_attributes_read)

    policy_matches = _as_of_valid_time_latest_transaction(
        view.policy_history, view.t0, key_fn=lambda p: p.version_id
    )
    policy_answer = _policy_dict(policy_matches[0]) if len(policy_matches) == 1 else UNDETERMINED
    threshold = policy_matches[0].threshold if len(policy_matches) == 1 else None

    auth_matches = _as_of_valid_time_latest_transaction(
        view.authority_history, view.t0, key_fn=lambda a: a.agent_id, role_filter="Approver"
    )
    authority_answer = _authority_dict(auth_matches[0]) if len(auth_matches) == 1 else UNDETERMINED
    authority_identity = (
        {"agent_id": auth_matches[0].agent_id, "role": auth_matches[0].role}
        if len(auth_matches) == 1 else UNDETERMINED
    )
    approver_present = True if len(auth_matches) == 1 else None

    model_matches = _as_of_valid_time(view.model_history, view.t0)
    model_version = model_matches[0].version_id if len(model_matches) == 1 else UNDETERMINED
    weights = model_matches[0].weights if len(model_matches) == 1 else None

    on_watchlist = trace.watchlist_check_result

    q7 = _authorize(evidence, weights, threshold, approver_present, on_watchlist)
    return Answers(
        decision_id=outcome.decision_id,
        requester_id=outcome.requester_id,
        result=outcome.result,
        evidence_values=evidence,
        policy_label="threshold rule",
        policy_version=policy_answer,
        authority_identity=authority_identity,
        authority_version=authority_answer,
        model_version=model_version,
        authorized_at_t0=q7,
        justification=_justification(evidence, policy_answer, authority_answer, q7),
    )


def _reconstruct_c(view: RegimeCView) -> Answers:
    outcome = view.outcome
    binding = view.binding
    evidence = dict(binding.evidence_ref["values"])

    policy_answer = dict(binding.policy_ref)
    threshold = next(
        p.threshold for p in view.policy_history if p.version_id == binding.policy_ref["version_id"]
    )

    authority_answer = dict(binding.authority_ref)
    authority_identity = {"agent_id": binding.authority_ref["agent_id"], "role": "Approver"}

    model_version = binding.model_ref["version_id"]
    weights = next(
        m.weights for m in view.model_history if m.version_id == model_version
    )

    on_watchlist = view.event_trace.watchlist_check_result

    q7 = _authorize(evidence, weights, threshold, approver_present=True, on_watchlist=on_watchlist)
    return Answers(
        decision_id=outcome.decision_id,
        requester_id=outcome.requester_id,
        result=outcome.result,
        evidence_values=evidence,
        policy_label="threshold rule",
        policy_version=policy_answer,
        authority_identity=authority_identity,
        authority_version=authority_answer,
        model_version=model_version,
        authorized_at_t0=q7,
        justification=_justification(evidence, policy_answer, authority_answer, q7),
    )


def reconstruct(regime: str, view) -> Answers:
    if regime == REGIME_A:
        return _reconstruct_a(view)
    if regime == REGIME_B:
        return _reconstruct_b(view)
    if regime == REGIME_C:
        return _reconstruct_c(view)
    raise ValueError(f"unknown regime {regime!r}")
