"""Regime T1 (locally complete, globally unlinked) and T2 (locally
complete + trajectory relations) views, plus the machine-checkable
local-facts equivalence test.
"""

from __future__ import annotations

from typing import List

from .cases import TrajectoryWorld
from .domain import DecisionRecordT1, DecisionRecordT2

REGIME_T1 = "T1"
REGIME_T2 = "T2"
ALL_REGIMES = (REGIME_T1, REGIME_T2)

_LOCAL_FIELDS = ("decision_id", "observed_t0", "context", "result", "output_value",
                  "consumed_input_value", "depends_on_most_recent")


def t1_view(world: TrajectoryWorld) -> List[DecisionRecordT1]:
    true_predecessor_of_d3 = world.ground_truth.true_edges.get("D3")
    records = []
    for d in world.decisions:
        causal_trace_event = None
        if world.case_id == "C3-6" and d.decision_id == "D3":
            causal_trace_event = true_predecessor_of_d3
        records.append(DecisionRecordT1(
            decision_id=d.decision_id, observed_t0=d.observed_t0, context=d.context,
            result=d.result, output_value=d.output_value,
            consumed_input_value=d.consumed_input_value,
            depends_on_most_recent=d.depends_on_most_recent,
            causal_trace_event=causal_trace_event,
        ))
    return records


def t2_view(world: TrajectoryWorld) -> List[DecisionRecordT2]:
    records = []
    for d in world.decisions:
        consumed_from = world.ground_truth.true_edges.get(d.decision_id)
        records.append(DecisionRecordT2(
            decision_id=d.decision_id, observed_t0=d.observed_t0, context=d.context,
            result=d.result, output_value=d.output_value,
            consumed_input_value=d.consumed_input_value,
            depends_on_most_recent=d.depends_on_most_recent,
            consumed_from_decision_id=consumed_from,
        ))
    return records


def view_for(world: TrajectoryWorld, regime: str):
    if regime == REGIME_T1:
        return t1_view(world)
    if regime == REGIME_T2:
        return t2_view(world)
    raise ValueError(f"unknown regime {regime!r}")


def verify_t1_t2_local_equivalence(world: TrajectoryWorld) -> None:
    """Local facts(T1) == Local facts(T2) for every decision, per
    research-question.md. Only trajectory-link information may differ:
    T2's consumed_from_decision_id (structurally absent from T1's type
    entirely) and, for C3-6 only, T1's disclosed causal_trace_event
    (structurally absent from T2's type entirely). Raises AssertionError
    on any other divergence -- must halt, not be silently repaired."""
    t1 = t1_view(world)
    t2 = t2_view(world)
    assert len(t1) == len(t2)
    for r1, r2 in zip(t1, t2):
        for field in _LOCAL_FIELDS:
            assert getattr(r1, field) == getattr(r2, field), (
                f"{world.case_id}/{r1.decision_id}: local field {field!r} diverged "
                f"between T1 ({getattr(r1, field)!r}) and T2 ({getattr(r2, field)!r})"
            )
    if world.case_id != "C3-6":
        for r1 in t1:
            assert r1.causal_trace_event is None, (
                f"{world.case_id}: only C3-6 may give T1 a causal_trace_event"
            )
