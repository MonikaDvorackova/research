"""Scoring for the trajectory-composition experiment. Conceptually mirrors
Contribution 2's followup-case10 scoring (CORRECT/WRONG/AMBIGUOUS
classification, a false-confidence metric), reimplemented here rather than
imported, per this experiment's isolation requirement.

Ground truth is consulted only here, never inside reconstruction.py.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .cases import TrajectoryWorld
from .domain import AMBIGUOUS, NO_DEPENDENCY, UNIQUE
from .reconstruction import TrajectoryAnswers

CORRECT_UNIQUE = "CORRECT_UNIQUE"
WRONG_UNIQUE = "WRONG_UNIQUE"
CLASS_AMBIGUOUS = "AMBIGUOUS"
CORRECT_NO_DEPENDENCY = "CORRECT_NO_DEPENDENCY"
WRONG_NO_DEPENDENCY = "WRONG_NO_DEPENDENCY"


@dataclass(frozen=True)
class EdgeClassification:
    decision_id: str
    true_predecessor: object  # str or None
    reconstructed_status: str
    reconstructed_predecessor: object
    classification: str
    is_ambiguous_by_construction: bool


@dataclass(frozen=True)
class CaseScore:
    case_id: str
    regime: str
    local_decision_reconstruction: float  # fraction of decisions with correct local facts
    trajectory_identifiable: bool  # every dependent edge is CORRECT_UNIQUE
    edge_classifications: List[EdgeClassification]


def _dependent_decision_ids(world: TrajectoryWorld):
    return [did for did, pred in world.ground_truth.true_edges.items() if pred is not None]


def score_case(world: TrajectoryWorld, regime: str, answers: TrajectoryAnswers) -> CaseScore:
    local_ok_count = sum(1 for v in answers.local_context_correct.values() if v)
    local_fraction = local_ok_count / len(answers.local_context_correct)

    dependent_ids = _dependent_decision_ids(world)
    classifications = []
    for did in dependent_ids:
        true_pred = world.ground_truth.true_edges[did]
        resolution = answers.edges[did]
        is_amb_by_construction = did in world.ground_truth.ambiguous_by_construction

        if resolution.status == UNIQUE:
            cls = CORRECT_UNIQUE if resolution.predecessor == true_pred else WRONG_UNIQUE
        elif resolution.status == AMBIGUOUS:
            cls = CLASS_AMBIGUOUS
        elif resolution.status == NO_DEPENDENCY:
            cls = WRONG_NO_DEPENDENCY  # every dependent id has a true predecessor by definition
        else:
            raise ValueError(f"unknown resolution status {resolution.status!r}")

        classifications.append(EdgeClassification(
            decision_id=did, true_predecessor=true_pred,
            reconstructed_status=resolution.status,
            reconstructed_predecessor=resolution.predecessor,
            classification=cls, is_ambiguous_by_construction=is_amb_by_construction,
        ))

    trajectory_identifiable = all(c.classification == CORRECT_UNIQUE for c in classifications)

    return CaseScore(
        case_id=world.case_id, regime=regime,
        local_decision_reconstruction=local_fraction,
        trajectory_identifiable=trajectory_identifiable,
        edge_classifications=classifications,
    )


@dataclass(frozen=True)
class AggregateMetrics:
    regime: str
    n_cases: int
    local_decision_reconstruction_rate: float  # mean across all decisions in all cases
    trajectory_identifiability_rate: float  # fraction of cases fully identifiable
    dependency_edge_accuracy: float  # among UNIQUE claims, fraction CORRECT_UNIQUE
    ambiguity_detection_rate: float  # among genuinely-ambiguous edges, fraction classified AMBIGUOUS
    false_global_confidence_rate: float  # WRONG_UNIQUE / all dependent edges


def aggregate(case_scores: List[CaseScore]) -> AggregateMetrics:
    assert case_scores, "no case scores to aggregate"
    regime = case_scores[0].regime
    assert all(cs.regime == regime for cs in case_scores)

    local_fractions = [cs.local_decision_reconstruction for cs in case_scores]
    local_rate = sum(local_fractions) / len(local_fractions)

    identifiable = [cs.trajectory_identifiable for cs in case_scores]
    identifiability_rate = sum(1 for x in identifiable if x) / len(identifiable)

    all_edges = [ec for cs in case_scores for ec in cs.edge_classifications]
    unique_claims = [ec for ec in all_edges if ec.reconstructed_status == UNIQUE]
    edge_accuracy = (
        sum(1 for ec in unique_claims if ec.classification == CORRECT_UNIQUE) / len(unique_claims)
        if unique_claims else float("nan")
    )

    genuinely_ambiguous = [ec for ec in all_edges if ec.is_ambiguous_by_construction]
    detection_rate = (
        sum(1 for ec in genuinely_ambiguous if ec.classification == CLASS_AMBIGUOUS)
        / len(genuinely_ambiguous)
        if genuinely_ambiguous else float("nan")
    )

    false_confidence_rate = (
        sum(1 for ec in all_edges if ec.classification == WRONG_UNIQUE) / len(all_edges)
        if all_edges else float("nan")
    )

    return AggregateMetrics(
        regime=regime, n_cases=len(case_scores),
        local_decision_reconstruction_rate=local_rate,
        trajectory_identifiability_rate=identifiability_rate,
        dependency_edge_accuracy=edge_accuracy,
        ambiguity_detection_rate=detection_rate,
        false_global_confidence_rate=false_confidence_rate,
    )
