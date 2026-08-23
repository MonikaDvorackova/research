"""The three preservation regimes (experiment-design/preservation-regimes.md),
implemented as distinct view objects derived from a World (cases.py).

Each view type structurally exposes only the fields that regime is allowed
to see. This is deliberate: a reconstruction procedure that only receives a
RegimeAView object *cannot* read history or a binding record, because those
attributes do not exist on that type -- there is no discipline-based
"promise" not to look, the information is architecturally absent. This is
what test_regimes.py's leakage tests check.

Regime C's view is built from exactly Regime B's underlying artifacts plus
one additional field (`binding`), never from independently-sourced data --
enforced by `verify_b_c_equivalence`, which PHASE 1B requires be run before
the experiment executes.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List

from .cases import World
from .domain import (
    AuthorityAssignment,
    DecisionBindingRecord,
    DecisionEventTrace,
    DecisionOutcomeLog,
    ModelVersion,
    PolicyVersion,
    WatchlistEntry,
)

REGIME_A = "A"
REGIME_B = "B"
REGIME_C = "C"
ALL_REGIMES = (REGIME_A, REGIME_B, REGIME_C)


@dataclass(frozen=True)
class RegimeAView:
    """Bare: a single outcome-log row plus whatever is currently live.
    No history of any dependency. No per-decision event trace."""

    decision_id: str
    t0: datetime
    query_time: datetime
    outcome: DecisionOutcomeLog
    live_policy: PolicyVersion
    live_authority: AuthorityAssignment
    live_model: ModelVersion
    live_watchlist: WatchlistEntry


@dataclass(frozen=True)
class RegimeBView:
    """Versioned but unbound: complete bitemporal/valid-time histories for
    every dependency, plus a per-decision event trace of raw values read.
    No explicit version-identifier reference from decision to version."""

    decision_id: str
    t0: datetime
    query_time: datetime
    outcome: DecisionOutcomeLog
    event_trace: DecisionEventTrace
    policy_history: List[PolicyVersion]
    authority_history: List[AuthorityAssignment]
    model_history: List[ModelVersion]
    watchlist_history: List[WatchlistEntry]


@dataclass(frozen=True)
class RegimeCView:
    """Versioned and bound: everything in RegimeBView, plus exactly one
    additional artifact -- the DecisionBindingRecord authored at t0."""

    decision_id: str
    t0: datetime
    query_time: datetime
    outcome: DecisionOutcomeLog
    event_trace: DecisionEventTrace
    policy_history: List[PolicyVersion]
    authority_history: List[AuthorityAssignment]
    model_history: List[ModelVersion]
    watchlist_history: List[WatchlistEntry]
    binding: DecisionBindingRecord


def regime_a_view(world: World) -> RegimeAView:
    return RegimeAView(
        decision_id=world.decision_id,
        t0=world.t0,
        query_time=world.query_time,
        outcome=world.outcome_log,
        live_policy=world.live_policy,
        live_authority=world.live_authority,
        live_model=world.live_model,
        live_watchlist=world.live_watchlist,
    )


def regime_b_view(world: World) -> RegimeBView:
    return RegimeBView(
        decision_id=world.decision_id,
        t0=world.t0,
        query_time=world.query_time,
        outcome=world.outcome_log,
        event_trace=world.event_trace,
        policy_history=list(world.policy_history),
        authority_history=list(world.authority_history),
        model_history=list(world.model_history),
        watchlist_history=list(world.watchlist_history),
    )


def regime_c_view(world: World) -> RegimeCView:
    b = regime_b_view(world)
    return RegimeCView(
        decision_id=b.decision_id,
        t0=b.t0,
        query_time=b.query_time,
        outcome=b.outcome,
        event_trace=b.event_trace,
        policy_history=b.policy_history,
        authority_history=b.authority_history,
        model_history=b.model_history,
        watchlist_history=b.watchlist_history,
        binding=world.binding_record,
    )


def view_for(world: World, regime: str):
    if regime == REGIME_A:
        return regime_a_view(world)
    if regime == REGIME_B:
        return regime_b_view(world)
    if regime == REGIME_C:
        return regime_c_view(world)
    raise ValueError(f"unknown regime {regime!r}")


def verify_b_c_equivalence(world: World) -> None:
    """Machine-checkable assertion (PHASE 1B): all underlying artifact
    content in C is also present in B, and C's only addition is the
    binding record. Raises AssertionError if this invariant fails --
    per the task's explicit instruction, this must halt execution, not
    be silently repaired.
    """
    b = regime_b_view(world)
    c = regime_c_view(world)

    assert b.decision_id == c.decision_id
    assert b.t0 == c.t0
    assert b.outcome == c.outcome
    assert b.event_trace == c.event_trace
    assert b.policy_history == c.policy_history
    assert b.authority_history == c.authority_history
    assert b.model_history == c.model_history
    assert b.watchlist_history == c.watchlist_history

    # C's binding must reference identifiers that already exist in B's
    # histories -- it must assert no new fact about the world.
    policy_ids_in_b = {p.version_id for p in b.policy_history}
    authority_ids_in_b = {a.agent_id for a in b.authority_history}
    model_ids_in_b = {m.version_id for m in b.model_history}

    binding = c.binding
    assert binding.decision_id == world.decision_id
    assert binding.policy_ref["version_id"] in policy_ids_in_b
    assert binding.authority_ref["agent_id"] in authority_ids_in_b
    assert binding.model_ref["version_id"] in model_ids_in_b
    assert set(binding.evidence_ref["values"].items()) <= set(
        b.event_trace.evidence_attributes_read.items()
    )
