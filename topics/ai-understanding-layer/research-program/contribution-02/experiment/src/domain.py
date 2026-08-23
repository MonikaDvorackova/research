"""Data schemas and the fixed decision rule for the Tier-2 Access Advisor
reconstruction experiment.

Schemas follow experiment-design/implementation-spec.md Section 1 exactly.
No field is added or removed relative to that spec.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, Tuple

GRANT = "GRANT"
DENY = "DENY"
UNDETERMINED = "UNDETERMINED"


@dataclass(frozen=True)
class PolicyVersion:
    version_id: str
    threshold: float
    valid_from: datetime
    valid_to: Optional[datetime]
    recorded_at: datetime


@dataclass(frozen=True)
class AuthorityAssignment:
    agent_id: str
    role: str
    valid_from: datetime
    valid_to: Optional[datetime]
    recorded_at: datetime


@dataclass(frozen=True)
class ModelVersion:
    version_id: str
    weights: Dict[str, float]
    valid_from: datetime
    valid_to: Optional[datetime]


@dataclass(frozen=True)
class WatchlistEntry:
    requester_id: str
    on_watchlist: bool
    valid_from: datetime
    valid_to: Optional[datetime]


@dataclass(frozen=True)
class DecisionEventTrace:
    decision_id: str
    t0: datetime
    evidence_attributes_read: Dict[str, float]
    score_computed: float
    threshold_value_read: float
    approver_check_result: bool
    watchlist_check_result: bool


@dataclass(frozen=True)
class DecisionBindingRecord:
    """Regime C only. References version identifiers already present in
    Regime B's histories; asserts no new fact about the world."""

    decision_id: str
    policy_ref: Dict
    authority_ref: Dict
    model_ref: Dict
    evidence_ref: Dict
    context_ref: Dict


@dataclass(frozen=True)
class DecisionOutcomeLog:
    decision_id: str
    t0: datetime
    requester_id: str
    computed_score: float
    result: str


@dataclass(frozen=True)
class GroundTruth:
    decision_id: str
    t0: datetime
    true_policy_version_id: str
    true_policy_valid_interval: Tuple[datetime, Optional[datetime]]
    true_authority_agent_id: str
    true_authority_valid_interval: Tuple[datetime, Optional[datetime]]
    true_evidence_values: Dict[str, float]
    true_model_version_id: str
    true_watchlist_status_at_t0: bool
    true_computed_score: float
    true_result: str
    true_justification: str


def compute_score(evidence: Dict[str, float], weights: Dict[str, float]) -> float:
    """score = w1*account_age_norm + w2*prior_incidents_norm
    (implementation-spec.md Section 2)."""
    return (
        weights["w1"] * evidence["account_age_norm"]
        + weights["w2"] * evidence["prior_incidents_norm"]
    )


def decide(
    score: float,
    threshold: float,
    approver_present: bool,
    on_watchlist: bool,
) -> str:
    """GRANT iff score < threshold AND an Approver held role at t0 AND
    requester not on watchlist at t0 (implementation-spec.md Section 2)."""
    if score < threshold and approver_present and not on_watchlist:
        return GRANT
    return DENY
