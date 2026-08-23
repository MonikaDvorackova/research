"""Metrics, formally defined (experiment-design/metrics-and-scoring.md).

All five metrics are computed per case, per regime, then aggregated by
perturbation-case category -- never pooled into one figure, per the design's
explicit instruction that pooling would obscure the pattern that
distinguishes H1 support from H0 support.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from .cases import CASE_CATEGORY_ORDER, World
from .domain import UNDETERMINED, GroundTruth
from .reconstruction import Answers


def _policy_id_correct(policy_answer, gt: GroundTruth) -> bool:
    if policy_answer == UNDETERMINED:
        return False
    return policy_answer["version_id"] == gt.true_policy_version_id


def _policy_temporally_correct(policy_answer, gt: GroundTruth) -> bool:
    """Correct iff the answer names ground truth's true version AND that
    answer's own stated interval is self-consistent with t0 (genuinely
    contains it). Deliberately does not require the answer's valid_to to
    equal a value only knowable in the future (e.g. a still-open interval
    correctly reported as valid_to=None at decision time is not penalized
    just because the version was later, legitimately, superseded) --
    metrics-and-scoring.md defines Temporal Correctness as naming "the
    version whose valid-time interval actually contained t0," which is a
    statement about version identity and containment, not about
    reproducing a specific future-dependent close timestamp."""
    if policy_answer == UNDETERMINED:
        return False
    if policy_answer["version_id"] != gt.true_policy_version_id:
        return False
    valid_from, valid_to = policy_answer["valid_from"], policy_answer["valid_to"]
    return valid_from <= gt.t0 and (valid_to is None or gt.t0 < valid_to)


def _authority_id_correct(authority_answer, gt: GroundTruth) -> bool:
    if authority_answer == UNDETERMINED:
        return False
    return authority_answer["agent_id"] == gt.true_authority_agent_id


def _authority_temporally_correct(authority_answer, gt: GroundTruth) -> bool:
    """See _policy_temporally_correct's docstring for the rationale behind
    checking self-consistent containment rather than exact interval
    equality."""
    if authority_answer == UNDETERMINED:
        return False
    if authority_answer["agent_id"] != gt.true_authority_agent_id:
        return False
    valid_from, valid_to = authority_answer["valid_from"], authority_answer["valid_to"]
    return valid_from <= gt.t0 and (valid_to is None or gt.t0 < valid_to)


def _model_correct(model_answer, gt: GroundTruth) -> bool:
    if model_answer == UNDETERMINED:
        return False
    return model_answer == gt.true_model_version_id


def _evidence_correct(evidence_answer, gt: GroundTruth) -> bool:
    if evidence_answer == UNDETERMINED:
        return False
    return dict(evidence_answer) == dict(gt.true_evidence_values)


@dataclass(frozen=True)
class CaseScore:
    case_id: str
    category: str
    decision_id: str
    regime: str

    aia: float
    aia_detail: Dict[str, bool]

    tc: int
    tc_detail: Dict[str, bool]

    ac: int

    jc: float
    jc_detail: Dict[str, bool]

    fhc_policy: int
    fhc_authority: int
    fhc_rate: float


def score_case(world: World, regime: str, answers: Answers) -> CaseScore:
    gt = world.ground_truth

    policy_id_ok = _policy_id_correct(answers.policy_version, gt)
    authority_id_ok = _authority_id_correct(answers.authority_version, gt)
    model_ok = _model_correct(answers.model_version, gt)
    evidence_ok = _evidence_correct(answers.evidence_values, gt)
    aia_detail = {
        "policy": policy_id_ok,
        "authority": authority_id_ok,
        "model": model_ok,
        "evidence": evidence_ok,
    }
    aia = sum(aia_detail.values()) / 4

    policy_tc_ok = _policy_temporally_correct(answers.policy_version, gt)
    authority_tc_ok = _authority_temporally_correct(answers.authority_version, gt)
    tc_detail = {"policy": policy_tc_ok, "authority": authority_tc_ok}
    tc = 1 if (policy_tc_ok and authority_tc_ok) else 0

    ac = 1 if answers.authorized_at_t0 == gt.true_result else 0

    jc_detail = {
        "policy": answers.policy_version != UNDETERMINED,
        "authority": answers.authority_version != UNDETERMINED,
        "model": answers.model_version != UNDETERMINED,
        "evidence": answers.evidence_values != UNDETERMINED,
    }
    jc = sum(jc_detail.values()) / 4

    fhc_policy = 1 if (answers.policy_version != UNDETERMINED and not policy_tc_ok) else 0
    fhc_authority = 1 if (answers.authority_version != UNDETERMINED and not authority_tc_ok) else 0
    fhc_rate = (fhc_policy + fhc_authority) / 2

    return CaseScore(
        case_id=world.case_id,
        category=world.category,
        decision_id=world.decision_id,
        regime=regime,
        aia=aia,
        aia_detail=aia_detail,
        tc=tc,
        tc_detail=tc_detail,
        ac=ac,
        jc=jc,
        jc_detail=jc_detail,
        fhc_policy=fhc_policy,
        fhc_authority=fhc_authority,
        fhc_rate=fhc_rate,
    )


@dataclass(frozen=True)
class CategorySummary:
    category: str
    regime: str
    n: int
    mean_aia: float
    tc_rate: float
    mean_ac: float
    mean_jc: float
    mean_fhc_rate: float


def aggregate_by_category(scores: List[CaseScore]) -> List[CategorySummary]:
    summaries = []
    for category in CASE_CATEGORY_ORDER:
        for regime in ("A", "B", "C"):
            subset = [s for s in scores if s.category == category and s.regime == regime]
            if not subset:
                continue
            n = len(subset)
            summaries.append(CategorySummary(
                category=category,
                regime=regime,
                n=n,
                mean_aia=sum(s.aia for s in subset) / n,
                tc_rate=sum(s.tc for s in subset) / n,
                mean_ac=sum(s.ac for s in subset) / n,
                mean_jc=sum(s.jc for s in subset) / n,
                mean_fhc_rate=sum(s.fhc_rate for s in subset) / n,
            ))
    return summaries
