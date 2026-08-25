"""The six-case trajectory matrix (case-matrix.md), built exactly to the
locked parameters there.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

from .domain import Decision, TrajectoryGroundTruth

PRECISION = timedelta(seconds=1)
BASE_T = datetime(2026, 6, 1, 12, 0, 0)


def _truncate(t: datetime) -> datetime:
    return t.replace(microsecond=0)


@dataclass
class TrajectoryWorld:
    case_id: str
    description: str
    decisions: List[Decision]
    ground_truth: TrajectoryGroundTruth


def _mk(decision_id, offset_seconds, context="ctx-1", result="OK", output_value=None,
        consumed_input_value=None, depends_on_most_recent=False) -> Decision:
    t = BASE_T + timedelta(seconds=offset_seconds)
    return Decision(
        decision_id=decision_id,
        true_t0=t,
        observed_t0=_truncate(t),
        context=context,
        result=result,
        output_value=output_value,
        consumed_input_value=consumed_input_value,
        depends_on_most_recent=depends_on_most_recent,
    )


def case_c3_1() -> TrajectoryWorld:
    """Fully identifiable control: exactly one value match exists."""
    d1 = _mk("D1", 0, output_value=10)
    d2 = _mk("D2", 60, consumed_input_value=10)
    return TrajectoryWorld(
        case_id="C3-1", description="Fully identifiable control.",
        decisions=[d1, d2],
        ground_truth=TrajectoryGroundTruth(
            case_id="C3-1", decision_ids=("D1", "D2"),
            true_edges={"D2": "D1"}, ambiguous_by_construction=(),
        ),
    )


def case_c3_2() -> TrajectoryWorld:
    """Identical-value provenance ambiguity."""
    d1 = _mk("D1", 0, output_value=7)
    d2 = _mk("D2", 60, output_value=7)
    d3 = _mk("D3", 120, consumed_input_value=7)
    return TrajectoryWorld(
        case_id="C3-2", description="Identical-value provenance ambiguity.",
        decisions=[d1, d2, d3],
        ground_truth=TrajectoryGroundTruth(
            case_id="C3-2", decision_ids=("D1", "D2", "D3"),
            true_edges={"D3": "D1"}, ambiguous_by_construction=("D3",),
        ),
    )


def case_c3_3() -> TrajectoryWorld:
    """Branch/abstraction ambiguity: two independent branches each
    satisfy the same boolean precondition D3 consumes."""
    d1 = _mk("D1", 0, output_value=True, context="branch-A")
    d2 = _mk("D2", 60, output_value=True, context="branch-B")
    d3 = _mk("D3", 120, consumed_input_value=True)
    return TrajectoryWorld(
        case_id="C3-3", description="Branch/abstraction ambiguity.",
        decisions=[d1, d2, d3],
        ground_truth=TrajectoryGroundTruth(
            case_id="C3-3", decision_ids=("D1", "D2", "D3"),
            true_edges={"D3": "D2"}, ambiguous_by_construction=("D3",),
        ),
    )


def case_c3_4() -> TrajectoryWorld:
    """State-write ambiguity: two independent writes set the same
    shared-state value; a later read cannot tell which write it observed."""
    d1 = _mk("D1", 0, output_value="state=active", context="writer")
    d2 = _mk("D2", 60, output_value="state=active", context="writer")
    d3 = _mk("D3", 120, consumed_input_value="state=active", context="reader")
    return TrajectoryWorld(
        case_id="C3-4", description="State-write ambiguity.",
        decisions=[d1, d2, d3],
        ground_truth=TrajectoryGroundTruth(
            case_id="C3-4", decision_ids=("D1", "D2", "D3"),
            true_edges={"D3": "D1"}, ambiguous_by_construction=("D3",),
        ),
    )


def case_c3_5() -> TrajectoryWorld:
    """Concurrent/near-concurrent dependency ambiguity: D1 and D2's true
    moments differ (0.2s vs 0.6s past the same second boundary) but both
    truncate to the identical observable second, so a "most recent"
    structural dependency cannot be resolved from observable timestamps
    alone."""
    d1 = Decision(
        decision_id="D1", true_t0=BASE_T + timedelta(seconds=0.2),
        observed_t0=_truncate(BASE_T), context="ctx-1", result="OK",
        output_value="A",
    )
    d2 = Decision(
        decision_id="D2", true_t0=BASE_T + timedelta(seconds=0.6),
        observed_t0=_truncate(BASE_T), context="ctx-1", result="OK",
        output_value="B",
    )
    d3 = _mk("D3", 60, depends_on_most_recent=True)
    return TrajectoryWorld(
        case_id="C3-5", description="Concurrent/near-concurrent dependency ambiguity.",
        decisions=[d1, d2, d3],
        ground_truth=TrajectoryGroundTruth(
            case_id="C3-5", decision_ids=("D1", "D2", "D3"),
            true_edges={"D3": "D2"}, ambiguous_by_construction=("D3",),
        ),
    )


def case_c3_6() -> TrajectoryWorld:
    """Negative control: identical structure to C3-2, plus one ordinary
    trace field on D3 (T1 only) naming the true predecessor."""
    d1 = _mk("D1", 0, output_value=7)
    d2 = _mk("D2", 60, output_value=7)
    d3 = _mk("D3", 120, consumed_input_value=7)
    return TrajectoryWorld(
        case_id="C3-6", description="Negative control: ordinary causal trace event resolves the ambiguity.",
        decisions=[d1, d2, d3],
        ground_truth=TrajectoryGroundTruth(
            case_id="C3-6", decision_ids=("D1", "D2", "D3"),
            true_edges={"D3": "D1"}, ambiguous_by_construction=(),
        ),
    )


CASE_BUILDERS = {
    "C3-1": case_c3_1, "C3-2": case_c3_2, "C3-3": case_c3_3,
    "C3-4": case_c3_4, "C3-5": case_c3_5, "C3-6": case_c3_6,
}

VALUE_COLLISION_CASES = ["C3-1", "C3-2", "C3-3", "C3-4", "C3-6"]
ORDER_TIMING_CASES = ["C3-5"]
NEGATIVE_CONTROL_CASES = ["C3-6"]


def all_worlds() -> List[TrajectoryWorld]:
    return [CASE_BUILDERS[k]() for k in sorted(CASE_BUILDERS)]
