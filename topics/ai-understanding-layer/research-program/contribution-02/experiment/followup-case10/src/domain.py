"""Follow-up Case 10 domain model.

Reuses the primary experiment's stable schema/logic (`PolicyVersion`,
`AuthorityAssignment`, `ModelVersion`, `WatchlistEntry`,
`DecisionOutcomeLog`, `DecisionBindingRecord`, `compute_score`, `decide`,
`GRANT`/`DENY`/`UNDETERMINED`) read-only, via direct file loading rather
than a package-relative import -- this follow-up's own top-level package
is also named `src` (matching the primary experiment's layout, per this
follow-up's directory structure), so a normal `import src.domain` would
be ambiguous about which `src` it means depending on working directory.
Loading the primary module by explicit path avoids that collision
entirely and guarantees zero risk of this follow-up accidentally mutating
or shadowing the primary package. Nothing in the primary `experiment/src/`
tree is imported in a way that could be affected by anything this follow-up
does -- this module only reads dataclass/function definitions from it.

Adds what the primary schema does not need: an observable-vs-true decision
time distinction, a resolution status for reconstruction under genuine
ambiguity, and one negative-control-only trace field.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional, Tuple

_PRIMARY_DOMAIN_PATH = Path(__file__).resolve().parent.parent.parent / "src" / "domain.py"
_spec = importlib.util.spec_from_file_location("primary_domain_for_followup_case10", _PRIMARY_DOMAIN_PATH)
_primary_domain = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = _primary_domain  # dataclasses' internal introspection requires this
_spec.loader.exec_module(_primary_domain)

PolicyVersion = _primary_domain.PolicyVersion
AuthorityAssignment = _primary_domain.AuthorityAssignment
ModelVersion = _primary_domain.ModelVersion
WatchlistEntry = _primary_domain.WatchlistEntry
DecisionOutcomeLog = _primary_domain.DecisionOutcomeLog
DecisionBindingRecord = _primary_domain.DecisionBindingRecord
GRANT = _primary_domain.GRANT
DENY = _primary_domain.DENY
UNDETERMINED = _primary_domain.UNDETERMINED
compute_score = _primary_domain.compute_score
decide = _primary_domain.decide

PRECISION = timedelta(seconds=1)

# Resolution statuses for a single dependency's reconstruction (Step 7):
# an investigator must never be forced to guess among equally compatible
# candidates.
UNIQUE = "UNIQUE"
AMBIGUOUS = "AMBIGUOUS"
NO_DATA = "NO_DATA"


def observed_t0(true_t0: datetime) -> datetime:
    """Truncate to whole-second precision -- the only decision timestamp
    Regime A/B ever receive. Regime C never receives this truncation
    either; its binding is authored using true_t0 directly, exactly as
    the primary experiment's Regime C binding is authored at decision
    time using ground truth, never a degraded observation of it."""
    return true_t0.replace(microsecond=0)


@dataclass(frozen=True)
class Resolution:
    """One dependency's reconstructed answer. Exactly one of `value`
    (if status == UNIQUE) or `candidates` (if status == AMBIGUOUS) is
    populated; both are absent if status == NO_DATA."""

    status: str  # UNIQUE | AMBIGUOUS | NO_DATA
    value: Optional[Dict] = None
    candidates: Optional[Tuple[Dict, ...]] = None


@dataclass(frozen=True)
class FollowupEventTrace:
    """Analogous to the primary experiment's DecisionEventTrace, but
    keyed on the *observable* decision timestamp only -- true_t0 is
    never part of this trace, by construction (see World.true_t0 in
    cases.py, which is kept separate and is ground-truth-only).

    `causal_consumption_event` is populated only in the F10-6 negative
    control case, on Regime B's view only -- see case-matrix.md."""

    decision_id: str
    observed_t0: datetime
    evidence_attributes_read: Dict[str, float]
    score_computed: float
    approver_check_result: bool
    watchlist_check_result: bool
    causal_consumption_event: Optional[Dict] = None


@dataclass(frozen=True)
class FollowupGroundTruth:
    decision_id: str
    true_t0: datetime
    observed_t0: datetime
    true_policy_version_id: str
    true_authority_agent_id: str
    true_model_version_id: str
    true_evidence_values: Dict[str, float]
    true_watchlist_status_at_t0: bool
    true_computed_score: float
    true_result: str
    ambiguous_dimensions: Tuple[str, ...]  # subset of ("policy","authority","model")
