"""The deterministic follow-up investigator.

One principle, reused from the primary experiment's discipline
(`../reconstruction-task.md`): never force a confident choice among
candidates the observable record cannot distinguish. Where the primary
experiment's bitemporal query returns `UNDETERMINED` on a non-unique
match, this follow-up returns the more specific `AMBIGUOUS` (carrying the
actual candidate set) precisely because Step 7 requires distinguishing
"inability to reconstruct uniquely" from "confidently reconstructing the
wrong history" -- both cases could otherwise collapse into the same
`UNDETERMINED` token.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple

from .domain import (
    AMBIGUOUS,
    NO_DATA,
    PRECISION,
    UNDETERMINED,
    UNIQUE,
    Resolution,
    compute_score,
    decide,
)
from .regimes import REGIME_B, REGIME_C, RegimeBView, RegimeCView


@dataclass(frozen=True)
class FollowupAnswers:
    decision_id: str
    requester_id: str
    result: str  # the logged outcome (from DecisionOutcomeLog, available identically in B/C)
    evidence_values: Dict[str, float]
    policy: Resolution
    authority: Resolution
    model: Resolution
    authorized_at_t0: str  # GRANT | DENY | UNDETERMINED


def _bucket_overlap_candidates(history, bucket_start: datetime, bucket_end: datetime):
    matches = []
    for row in history:
        row_end = row.valid_to if row.valid_to is not None else datetime.max
        if row.valid_from < bucket_end and row_end > bucket_start:
            matches.append(row)
    return matches


def _resolve(history, observed_t0: datetime, to_dict) -> Resolution:
    bucket_start = observed_t0
    bucket_end = observed_t0 + PRECISION
    matches = _bucket_overlap_candidates(history, bucket_start, bucket_end)
    if len(matches) == 0:
        return Resolution(status=NO_DATA)
    if len(matches) == 1:
        return Resolution(status=UNIQUE, value=to_dict(matches[0]))
    return Resolution(status=AMBIGUOUS, candidates=tuple(to_dict(m) for m in matches))


def _policy_dict(p) -> Dict:
    return {"version_id": p.version_id, "valid_from": p.valid_from, "valid_to": p.valid_to, "threshold": p.threshold}


def _authority_dict(a) -> Dict:
    return {"agent_id": a.agent_id, "valid_from": a.valid_from, "valid_to": a.valid_to}


def _model_dict(m) -> Dict:
    return {"version_id": m.version_id, "valid_from": m.valid_from, "valid_to": m.valid_to, "weights": m.weights}


def _apply_causal_disambiguation(resolution: Resolution, causal_event: Optional[Dict], key: str, id_field: str) -> Resolution:
    """A causal consumption event (F10-6 only) narrows an AMBIGUOUS
    resolution to UNIQUE if -- and only if -- it names one of the
    resolution's own candidates. It is never used to override a
    resolution that was already UNIQUE or to invent a candidate not
    already present in the observable history."""
    if resolution.status != AMBIGUOUS or not causal_event:
        return resolution
    target_id = causal_event.get(key)
    if target_id is None:
        return resolution
    for candidate in resolution.candidates:
        if candidate[id_field] == target_id:
            return Resolution(status=UNIQUE, value=candidate)
    return resolution


def _authorize(evidence, weights, threshold, approver_present, on_watchlist) -> str:
    if evidence is None or weights is None or threshold is None or approver_present is None or on_watchlist is None:
        return UNDETERMINED
    score = compute_score(evidence, weights)
    return decide(score, threshold, approver_present, on_watchlist)


def _reconstruct_b(view: RegimeBView) -> FollowupAnswers:
    trace = view.event_trace
    evidence = dict(trace.evidence_attributes_read)

    policy = _resolve(view.policy_history, view.observed_t0, _policy_dict)
    policy = _apply_causal_disambiguation(policy, trace.causal_consumption_event, "policy_version_id", "version_id")

    authority = _resolve(view.authority_history, view.observed_t0, _authority_dict)
    model = _resolve(view.model_history, view.observed_t0, _model_dict)

    threshold = policy.value["threshold"] if policy.status == UNIQUE else None
    weights = model.value["weights"] if model.status == UNIQUE else None
    approver_present = True if authority.status == UNIQUE else None

    q7 = _authorize(evidence, weights, threshold, approver_present, trace.watchlist_check_result)

    return FollowupAnswers(
        decision_id=view.outcome.decision_id,
        requester_id=view.outcome.requester_id,
        result=view.outcome.result,
        evidence_values=evidence,
        policy=policy,
        authority=authority,
        model=model,
        authorized_at_t0=q7,
    )


def _reconstruct_c(view: RegimeCView) -> FollowupAnswers:
    binding = view.binding
    evidence = dict(binding.evidence_ref["values"])

    policy_threshold = next(
        p.threshold for p in view.policy_history if p.version_id == binding.policy_ref["version_id"]
    )
    policy = Resolution(status=UNIQUE, value={**dict(binding.policy_ref), "threshold": policy_threshold})

    authority = Resolution(status=UNIQUE, value=dict(binding.authority_ref))

    model_version_id = binding.model_ref["version_id"]
    model_weights = next(m.weights for m in view.model_history if m.version_id == model_version_id)
    model = Resolution(status=UNIQUE, value={"version_id": model_version_id, "weights": model_weights})

    q7 = _authorize(evidence, model_weights, policy_threshold, approver_present=True,
                     on_watchlist=view.event_trace.watchlist_check_result)

    return FollowupAnswers(
        decision_id=view.outcome.decision_id,
        requester_id=view.outcome.requester_id,
        result=view.outcome.result,
        evidence_values=evidence,
        policy=policy,
        authority=authority,
        model=model,
        authorized_at_t0=q7,
    )


def reconstruct(regime: str, view) -> FollowupAnswers:
    if regime == REGIME_B:
        return _reconstruct_b(view)
    if regime == REGIME_C:
        return _reconstruct_c(view)
    raise ValueError(f"unknown regime {regime!r}")
