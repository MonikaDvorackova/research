"""The deterministic trajectory investigator. Same discipline as
Contribution 2's own reconstruction procedures (reused as a pattern, not
as code): never force a confident choice among candidates the observable
record cannot distinguish.

Two independent inference mechanisms, applied in a fixed order per
decision (a decision uses at most one, per its own construction in
cases.py):

1. Causal trace event (T1's C3-6-only field) -- if present, resolves
   directly, no inference needed.
2. Value-collision -- match a decision's consumed_input_value against
   every strictly-earlier decision's output_value.
3. Order/timing -- for a "depends on most recent" decision, find the
   strictly-earlier decision(s) with the latest observable timestamp.

T2 never needs inference: its consumed_from_decision_id is read directly.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

from .domain import AMBIGUOUS, NO_DEPENDENCY, UNIQUE
from .regimes import REGIME_T1, REGIME_T2


@dataclass(frozen=True)
class EdgeResolution:
    status: str  # UNIQUE | AMBIGUOUS | NO_DEPENDENCY
    predecessor: Optional[str] = None
    candidates: Optional[Tuple[str, ...]] = None


@dataclass(frozen=True)
class TrajectoryAnswers:
    case_id_hint: str  # decision_id of the last decision, for logging only -- not scored
    local_context_correct: Dict[str, bool]  # always True in this experiment; verified, not just asserted
    edges: Dict[str, EdgeResolution]  # decision_id -> its inferred incoming edge


def _resolve_value_collision(records, target) -> Optional[EdgeResolution]:
    if target.consumed_input_value is None:
        return None
    candidates = [
        r for r in records
        if r.decision_id != target.decision_id
        and r.output_value == target.consumed_input_value
        and r.observed_t0 < target.observed_t0
    ]
    if len(candidates) == 0:
        return EdgeResolution(status=NO_DEPENDENCY)
    if len(candidates) == 1:
        return EdgeResolution(status=UNIQUE, predecessor=candidates[0].decision_id)
    return EdgeResolution(status=AMBIGUOUS, candidates=tuple(c.decision_id for c in candidates))


def _resolve_order(records, target) -> Optional[EdgeResolution]:
    if not target.depends_on_most_recent:
        return None
    candidates = [
        r for r in records
        if r.decision_id != target.decision_id and r.observed_t0 < target.observed_t0
    ]
    if not candidates:
        return EdgeResolution(status=NO_DEPENDENCY)
    max_t = max(c.observed_t0 for c in candidates)
    most_recent = [c for c in candidates if c.observed_t0 == max_t]
    if len(most_recent) == 1:
        return EdgeResolution(status=UNIQUE, predecessor=most_recent[0].decision_id)
    return EdgeResolution(status=AMBIGUOUS, candidates=tuple(c.decision_id for c in most_recent))


def _reconstruct_t1(records: List) -> TrajectoryAnswers:
    edges = {}
    for target in records:
        trace_event = getattr(target, "causal_trace_event", None)
        if trace_event is not None:
            edges[target.decision_id] = EdgeResolution(status=UNIQUE, predecessor=trace_event)
            continue
        resolution = _resolve_value_collision(records, target)
        if resolution is None:
            resolution = _resolve_order(records, target)
        if resolution is None:
            resolution = EdgeResolution(status=NO_DEPENDENCY)
        edges[target.decision_id] = resolution
    local_ok = {r.decision_id: (r.context is not None and r.result is not None) for r in records}
    return TrajectoryAnswers(
        case_id_hint=records[-1].decision_id, local_context_correct=local_ok, edges=edges,
    )


def _reconstruct_t2(records: List) -> TrajectoryAnswers:
    edges = {}
    for target in records:
        if target.consumed_from_decision_id is None:
            edges[target.decision_id] = EdgeResolution(status=NO_DEPENDENCY)
        else:
            edges[target.decision_id] = EdgeResolution(
                status=UNIQUE, predecessor=target.consumed_from_decision_id
            )
    local_ok = {r.decision_id: (r.context is not None and r.result is not None) for r in records}
    return TrajectoryAnswers(
        case_id_hint=records[-1].decision_id, local_context_correct=local_ok, edges=edges,
    )


def reconstruct(regime: str, records: List) -> TrajectoryAnswers:
    if regime == REGIME_T1:
        return _reconstruct_t1(records)
    if regime == REGIME_T2:
        return _reconstruct_t2(records)
    raise ValueError(f"unknown regime {regime!r}")
