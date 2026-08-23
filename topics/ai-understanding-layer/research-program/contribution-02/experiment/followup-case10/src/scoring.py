"""Metrics for the follow-up (locked in research-question.md / Step 8
before execution).

Every dependency (policy, authority, model) is classified into exactly
one of four mutually exclusive outcomes before any metric is computed:

- CORRECT_UNIQUE: resolved to one candidate, and it is the true one.
- WRONG_UNIQUE: resolved to one candidate, and it is NOT the true one --
  this is the only outcome that counts as False Historical Confidence.
- AMBIGUOUS: correctly reported multiple compatible candidates -- an
  honest non-answer, never scored as False Historical Confidence.
- NO_DATA: no candidate at all (not expected in this matrix; handled for
  completeness only).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from .cases import World
from .domain import AMBIGUOUS, NO_DATA, UNIQUE
from .reconstruction import FollowupAnswers

CORRECT_UNIQUE = "CORRECT_UNIQUE"
WRONG_UNIQUE = "WRONG_UNIQUE"


def _classify(resolution, true_value, id_field: str) -> str:
    if resolution.status == AMBIGUOUS:
        return AMBIGUOUS
    if resolution.status == NO_DATA:
        return NO_DATA
    # UNIQUE
    return CORRECT_UNIQUE if resolution.value[id_field] == true_value else WRONG_UNIQUE


@dataclass(frozen=True)
class CaseScore:
    case_id: str
    decision_id: str
    regime: str

    policy_class: str
    authority_class: str
    model_class: str

    tc: int  # policy AND authority both CORRECT_UNIQUE
    urr: float  # fraction of {policy,authority,model} CORRECT_UNIQUE
    adr: Optional[float]  # fraction of ground-truth-ambiguous dims correctly flagged AMBIGUOUS (None if no ambiguous dims)
    ac: int  # authorized_at_t0 == true_result
    fhc_rate: float  # fraction of {policy,authority,model} that are WRONG_UNIQUE


def score_case(world: World, regime: str, answers: FollowupAnswers) -> CaseScore:
    gt = world.ground_truth

    policy_class = _classify(answers.policy, gt.true_policy_version_id, "version_id")
    authority_class = _classify(answers.authority, gt.true_authority_agent_id, "agent_id")
    model_class = _classify(answers.model, gt.true_model_version_id, "version_id")
    classes = {"policy": policy_class, "authority": authority_class, "model": model_class}

    tc = 1 if (policy_class == CORRECT_UNIQUE and authority_class == CORRECT_UNIQUE) else 0

    urr = sum(1 for c in classes.values() if c == CORRECT_UNIQUE) / 3

    if gt.ambiguous_dimensions:
        adr = sum(1 for dim in gt.ambiguous_dimensions if classes[dim] == AMBIGUOUS) / len(gt.ambiguous_dimensions)
    else:
        adr = None

    ac = 1 if answers.authorized_at_t0 == gt.true_result else 0

    fhc_rate = sum(1 for c in classes.values() if c == WRONG_UNIQUE) / 3

    return CaseScore(
        case_id=world.case_id,
        decision_id=world.decision_id,
        regime=regime,
        policy_class=policy_class,
        authority_class=authority_class,
        model_class=model_class,
        tc=tc,
        urr=urr,
        adr=adr,
        ac=ac,
        fhc_rate=fhc_rate,
    )
