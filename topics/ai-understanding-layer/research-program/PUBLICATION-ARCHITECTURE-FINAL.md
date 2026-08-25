---
id: note-research-program-publication-architecture-final
title: "Final Publication Architecture"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [research-program, publication-architecture, editorial-decision]
refs: [contribution-03/FINAL-EDITORIAL-DISPOSITION.md, contribution-03/article/review/VERDICT.md, publication-architectures.md, recommended-program.md]
---

Authoritative current publication map for the `ai-understanding-layer`
research programme, superseding the three-standalone-article
architecture recommended in `publication-architectures.md` and
`recommended-program.md`. This is a human editorial decision on
**publication architecture**, not a finding of factual invalidity — see
`contribution-03/FINAL-EDITORIAL-DISPOSITION.md` for the full reasoning.
Decided 2026-08-25.

## Core Article 1

- **Working title:** "Model Outputs Are Not Decisions: Building
  Evidence-Gated AI Systems" (`article-01-decision-level-control/
  draft-v2.md`; practitioner-register companion:
  `oreilly-submission-disruptive.md`).
- **Thesis:** Production AI needs an explicit decision layer — output →
  proposed decision → evidence → requirements/authority → gate →
  ALLOW/BLOCK/ESCALATE → transition — attached to the decision, not the
  model, because a single model participates in many decisions with
  different requirements.
- **Contribution:** A specific, coherent four-concept decomposition
  (evidence / requirements / authority / gate) with a concrete,
  implementable outcome model, generalized across artifact and decision
  types. Novelty classification: **Position B — new synthesis** of
  existing access-control, admission-control, and supply-chain-security
  mechanisms applied specifically to the model-vs-decision boundary
  (`article-01-decision-level-control/novelty-audit.md`).
- **Evidence basis:** Architecture/design argument, complete;
  adversarially self-reviewed; no experiment required to stand.
- **Status:** Independent core article, complete. Unchanged by this
  decision.
- **What it does NOT claim:** A newly invented mechanism (access
  control, admission control, and supply-chain attestation are all
  explicitly credited as prior art); that evaluation constitutes
  authorization; that documentation constitutes enforcement.

## Core Article 2

- **Title:** "Retained Is Not Consumed: Why Version History Doesn't
  Guarantee Decision Reconstruction" (`contribution-02/article/
  draft-v2.md`, frozen).
- **Thesis:** Retaining every version of a decision's dependencies does
  not by itself guarantee the decision can be uniquely reconstructed;
  the property that closes the gap is a preserved consumption relation,
  not more retained history.
- **Contribution:** A controlled empirical demonstration (two
  experiments: primary Regime A/B/C comparison, plus a timestamp-
  precision follow-up with a negative control) that the gap manifests in
  at least two distinguishable ways — honest ambiguity, and, in one
  clean case (Case 8), a genuine information-architecture gap.
- **Empirical basis:** Full experiment suite, raw results, adversarial
  review, rigorous fixture-level verification of the review's own
  headline finding, and an independent final-acceptance re-verification.
  See `contribution-02/article/FINAL-ACCEPTANCE.md`.
- **Status:** **COMPLETE and FROZEN.** Not modified by this decision or
  by any Contribution 3 finding.
- **What it does NOT claim:** That version history is generally
  insufficient; that bitemporal databases cannot solve reconstruction;
  that explicit decision-time binding is uniquely necessary; that a new
  architecture has been invented; that this problem is unique to AI.

## Supporting Research Note

- **Working title:** "Trajectory Reconstruction and Honest Ambiguity"
  (research materials: `contribution-03/`; draft-v1 and its adversarial
  review preserved as historical research-note artifacts, see
  `contribution-03/FINAL-EDITORIAL-DISPOSITION.md`).
- **Research question:** If individual decisions are reconstructable,
  what happens when reconstructing the relations across multiple
  decisions in a trajectory?
- **Experiment:** T1 (locally complete, globally unlinked) vs. T2
  (locally complete + one cross-decision relation), six controlled
  cases, negative control. Local Decision Reconstruction = 1.00 in both
  regimes; Trajectory Identifiability = 0.33 (T1) vs. 1.00 (T2);
  Dependency Edge Accuracy = 1.00; False Global Confidence = 0.00.
  (`contribution-03/experiment/RESULT.md`.)
- **Strongest earned finding:** Insufficient information and false
  confident reconstruction are empirically distinct failure modes — a
  well-built investigator, confronted with a genuinely ambiguous record,
  reported the ambiguity honestly rather than inventing a unique
  history, in every tested case.
- **Strongest prior-art collision:** Workflow provenance (W3C PROV, and
  the older Buneman why/where-provenance formalism) already models
  exactly the cross-decision relation the experiment's T2 regime adds —
  identified as the strongest single collision in the adversarial review
  (`contribution-03/article/review/prior-art-review.md`).
- **Why it is not being continued as standalone Article 3:** The
  adversarial review classified independent-publication status as
  **BORDERLINE** and publication register as **D — research note / short
  paper**, not a full technical practitioner article — see
  `contribution-03/article/review/VERDICT.md` for the complete reasoning
  (independence scored 2/5 criteria clearly passing; the T1/T2 gap
  direction is substantially structural, not a discovery; the
  engineering consequence overlaps heavily with Article 2's own
  takeaway).
- **What remains valuable:** The honest-ambiguity-vs-false-confidence
  finding, the negative-control demonstration, the diagnosability and
  compositional-verification framing, and the full experimental
  apparatus — all preserved and citable as supporting research, and as
  candidate O'Reilly synthesis material (see `OREILLY-SYNTHESIS-MAP.md`).

## O'Reilly synthesis

- **Status: NOT YET DRAFTED.**
- **Role of synthesis:** A future practitioner-facing piece connecting
  Core Article 1 (control), Core Article 2 (reconstruction), and the
  supporting research note (trajectory/honest-ambiguity) into one
  narrative arc, at the register of a synthesis rather than a systems
  paper.
- **Which earned concepts may feed it:** See `OREILLY-SYNTHESIS-MAP.md`
  for the full dependency map — at minimum, the decision-boundary
  pattern (Article 1), the retained-vs-consumed distinction (Article 2),
  and the honest-ambiguity principle (research note).
- **Which retired concepts may NOT return:** "Understanding Layer" as an
  architectural claim; "capability vs. understanding" as a scaling
  thesis. Both remain retired — see `contribution-03/FINAL-RESEARCH-
  VERDICT.md` and `contribution-03/novelty-verdict.md` for the original
  retirement findings, reaffirmed here.

## Superseded architecture

The three-standalone-article architecture recommended in
`publication-architectures.md` (Architecture C) and `recommended-
program.md`, and the corresponding three-part book arc in
`book-implications.md`, are **superseded by this document** for
publication-architecture purposes only. Those documents' underlying
research analysis (novelty audits, claim graphs, falsification tests)
remains historically accurate and is not rewritten — see the superseded-
architecture notices added at the top of each for the pointer back to
this decision.
