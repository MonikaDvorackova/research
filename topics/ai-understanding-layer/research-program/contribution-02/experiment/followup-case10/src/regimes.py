"""Regime B and C views for the follow-up (Regime A is out of scope --
see cases.py's module docstring).

Regime C's view always strips `causal_consumption_event` from its copy of
the event trace, regardless of what the underlying World carries -- this
guarantees C never receives F10-6's negative-control signal, by
construction, not by convention.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from .cases import World
from .domain import (
    AuthorityAssignment,
    DecisionBindingRecord,
    DecisionOutcomeLog,
    FollowupEventTrace,
    ModelVersion,
    PolicyVersion,
    WatchlistEntry,
)

REGIME_B = "B"
REGIME_C = "C"
ALL_REGIMES = (REGIME_B, REGIME_C)


@dataclass(frozen=True)
class RegimeBView:
    decision_id: str
    observed_t0: datetime
    outcome: DecisionOutcomeLog
    event_trace: FollowupEventTrace  # may carry causal_consumption_event (F10-6 only)
    policy_history: List[PolicyVersion]
    authority_history: List[AuthorityAssignment]
    model_history: List[ModelVersion]
    watchlist_history: List[WatchlistEntry]


@dataclass(frozen=True)
class RegimeCView:
    decision_id: str
    observed_t0: datetime
    outcome: DecisionOutcomeLog
    event_trace: FollowupEventTrace  # causal_consumption_event always stripped to None
    policy_history: List[PolicyVersion]
    authority_history: List[AuthorityAssignment]
    model_history: List[ModelVersion]
    watchlist_history: List[WatchlistEntry]
    binding: DecisionBindingRecord


def regime_b_view(world: World) -> RegimeBView:
    return RegimeBView(
        decision_id=world.decision_id,
        observed_t0=world.event_trace.observed_t0,
        outcome=world.outcome_log,
        event_trace=world.event_trace,
        policy_history=list(world.policy_history),
        authority_history=list(world.authority_history),
        model_history=list(world.model_history),
        watchlist_history=list(world.watchlist_history),
    )


def regime_c_view(world: World) -> RegimeCView:
    sanitized_trace = dataclasses.replace(world.event_trace, causal_consumption_event=None)
    return RegimeCView(
        decision_id=world.decision_id,
        observed_t0=world.event_trace.observed_t0,
        outcome=world.outcome_log,
        event_trace=sanitized_trace,
        policy_history=list(world.policy_history),
        authority_history=list(world.authority_history),
        model_history=list(world.model_history),
        watchlist_history=list(world.watchlist_history),
        binding=world.binding_record,
    )


def view_for(world: World, regime: str):
    if regime == REGIME_B:
        return regime_b_view(world)
    if regime == REGIME_C:
        return regime_c_view(world)
    raise ValueError(f"unknown regime {regime!r}")


def verify_b_c_equivalence(world: World) -> None:
    """Machine-checkable B/C equivalence (Step 5), with F10-6's single,
    disclosed exemption: B there carries one extra field
    (causal_consumption_event) that C by construction never receives.
    Everything else -- histories, outcome, and the rest of the event
    trace -- must be identical, and C's binding must reference only
    identifiers already present in B's histories, exactly as the primary
    experiment's equivalence check requires."""
    b = regime_b_view(world)
    c = regime_c_view(world)

    assert b.decision_id == c.decision_id
    assert b.observed_t0 == c.observed_t0
    assert b.outcome == c.outcome
    assert b.policy_history == c.policy_history
    assert b.authority_history == c.authority_history
    assert b.model_history == c.model_history
    assert b.watchlist_history == c.watchlist_history

    b_trace_sans_causal = dataclasses.replace(b.event_trace, causal_consumption_event=None)
    assert b_trace_sans_causal == c.event_trace

    if world.case_id != "F10-6":
        assert b.event_trace.causal_consumption_event is None, (
            "only F10-6 may give Regime B a causal_consumption_event"
        )

    policy_ids_in_b = {p.version_id for p in b.policy_history}
    authority_ids_in_b = {a.agent_id for a in b.authority_history}
    model_ids_in_b = {m.version_id for m in b.model_history}
    binding = c.binding
    assert binding.policy_ref["version_id"] in policy_ids_in_b
    assert binding.authority_ref["agent_id"] in authority_ids_in_b
    assert binding.model_ref["version_id"] in model_ids_in_b
