"""Data schemas for the trajectory-composition experiment.

Fully isolated from Contribution 2's experiment code (no imports from
`contribution-02/experiment/`), per this experiment's explicit
instruction to prefer isolation. Only the *conceptual* pattern (regime
views, a deterministic never-guessing investigator, ground truth hidden
from reconstruction) is reused, not any code.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

UNIQUE = "UNIQUE"
AMBIGUOUS = "AMBIGUOUS"
NO_DEPENDENCY = "NO_DEPENDENCY"


@dataclass(frozen=True)
class Decision:
    """One decision in a trajectory. `context` and `result` are the
    decision's own local facts -- always fully retained, correct, and
    unambiguous in every case and regime of this experiment (verified in
    tests/test_local_reconstruction.py). `output_value` and
    `consumed_input_value` drive the value-collision mechanism;
    `depends_on_most_recent` drives the order/timing mechanism -- a
    decision uses at most one of the two mechanisms.
    """

    decision_id: str
    true_t0: datetime
    observed_t0: datetime  # precision-truncated, what every regime's investigator sees
    context: str  # placeholder for Contribution 2's own consumed-context object
    result: str
    output_value: Optional[object] = None
    consumed_input_value: Optional[object] = None
    depends_on_most_recent: bool = False


@dataclass(frozen=True)
class DecisionRecordT1:
    """Regime T1: locally complete, globally unlinked. No
    `consumed_from_decision_id` field exists on this type at all --
    structurally absent, not merely undisclosed."""

    decision_id: str
    observed_t0: datetime
    context: str
    result: str
    output_value: Optional[object]
    consumed_input_value: Optional[object]
    depends_on_most_recent: bool
    causal_trace_event: Optional[str] = None  # populated only in C3-6, naming the true predecessor


@dataclass(frozen=True)
class DecisionRecordT2:
    """Regime T2: locally complete + the one additional cross-decision
    relation. `consumed_from_decision_id` is authored at decision time
    from ground truth and never subsequently altered -- mirrors
    Contribution 2's DecisionBindingRecord discipline, reused here only
    as a design pattern, not as code."""

    decision_id: str
    observed_t0: datetime
    context: str
    result: str
    output_value: Optional[object]
    consumed_input_value: Optional[object]
    depends_on_most_recent: bool
    consumed_from_decision_id: Optional[str]


@dataclass(frozen=True)
class TrajectoryGroundTruth:
    """Scoring-only. Never exposed to any reconstruction procedure."""

    case_id: str
    decision_ids: tuple
    true_edges: dict  # {to_decision_id: from_decision_id or None}
    ambiguous_by_construction: tuple  # decision_ids expected to be genuinely ambiguous given the observable record
