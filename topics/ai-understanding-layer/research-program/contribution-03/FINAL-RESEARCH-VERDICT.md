---
id: note-contribution-03-final-research-verdict
title: "Contribution 3 — Final Research Verdict (Narrow Pass)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-25
tags: [contribution-03, final-verdict]
refs: [operationalization-review.md, diagnosability-review.md, assurance-integration-review.md, composition-review.md, generalization-from-c2.md, article-03-options.md]
---

## RQ1 — Can system-level understanding be operationalized?

**PARTIALLY.**

Exact definition: system-level "understanding" of an AI-mediated
decision system is best represented as a vector of already-named,
independently-formalized properties, each defined relative to an
observer and an information set, not as one new scalar or one new named
umbrella property:

```
U(S, observer, evidence) = [
  reconstructability   -- ≈ diagnosability (discrete-event systems theory)
  observability         -- control theory's own term, unmodified
  interpretability       -- XAI's own term, unmodified
  predictability          -- ≈ system identification
  verifiability            -- formal/runtime verification's own term
]
```

Only **one** dimension (reconstructability) has actually been
operationalized and tested by this programme — Contribution 2's own
result, formally reducible to diagnosability theory applied to a new
object (`operationalization-review.md`, `diagnosability-review.md`). No
source found in this pass jointly operationalizes the full vector for a
multi-component AI decision system.

## RQ3 — Does Contribution 2 generalize?

**PARTIALLY.**

Highest defensible generalization level: **G2 (execution-context
identifiability) — plausible extension, not confirmed.** G1 (decision-
context identifiability) is fully supported, being Contribution 2's own
earned result. G3 (trajectory reconstructability) is the first level
this review classifies as requiring genuinely new evidence rather than a
natural next step, because it requires per-decision guarantees to
*compose*, and composition effects are directly evidenced (for the
adjacent property of predictability) as a real, non-trivial risk, not a
safe default (`generalization-from-c2.md`, `composition-review.md`).

## Integration gap

**NARROWED.**

Exact surviving formulation: existing mechanisms for understanding
AI-mediated systems are not, in fact, missing a coordination mechanism —
dynamic and continuous assurance cases already exist, are actively
developed, and are explicitly being applied to AI systems (including
frontier AI) specifically (`assurance-integration-review.md`). What
survives is narrower: **no source found composes a dynamic-assurance-
case claim structure with a decision-context-reconstructability claim of
the specific kind Contribution 2 tested** — an adoption/composition gap
for this specific object class, not an absence of coordinating
infrastructure in general.

## Measurement gap

**CONFIRMED.**

Current transparency/legibility/interpretability-metric literature
itself states directly that "standardizing definitions and evaluation
metrics remains an ongoing challenge" (`operationalization-review.md`).
No source found in either research pass jointly measures the full
property vector above for a multi-component AI decision system. This
gap is real, current, and not resolved by anything found in this pass.

## Composition effect

**PLAUSIBLE** (not SUPPORTED, not UNSUPPORTED).

Directly SUPPORTED for the adjacent property of behavioral
predictability (compositional-verification/emergent-behavior research is
explicit and current: local component verifiability does not guarantee
global predictability). Only PLAUSIBLE, not yet tested, for
reconstructability specifically — the object this programme actually
cares about (`composition-review.md`).

## Understanding

**KEEP ONLY AS UMBRELLA.**

Useful as an informal label for the property vector above, for
communication with a non-specialist reader — not defensible as a single
technical term with its own independent metric, given every dimension
in the vector already has a more precise existing name.

## Understanding Layer

**DEMOTE TO METAPHOR** (unchanged from the first pass, and further
weakened by this pass — the existence of dynamic assurance cases as a
real, current coordination mechanism removes one of the strongest
remaining reasons a *new* architectural layer might have been needed).

## Capability-vs-understanding

**RETIRE FROM ARTICLE 3.**

Nothing in this pass rescues the claim. If anything, mechanistic
interpretability's own field-wide admission that "many interpretability
queries are intractable" (found in the first pass, unchanged here) and
this pass's own finding that "understanding" is a five-dimensional
vector with no joint metric make the claim harder to even state
precisely, let alone test.

## Article 3

**C — research agenda article.** See `article-03-options.md` for the
full ranking; the surviving candidate is the composition question (does
per-decision reconstructability compose to per-trajectory
reconstructability), not a new technical property (A, ruled out by RQ1)
and not a systems synthesis strong enough to stand alone given dynamic
assurance cases already exist (B, weakened but not eliminated, ranked
second).

## Independent publication

**UNCERTAIN.**

The Rank-1 candidate is a genuinely open, well-scoped, precisely-stated
question with real prior-art grounding — but it is conditional on
further empirical work (an experiment extending Contribution 2's own
methodology to multi-decision trajectories) that has not been done and
was explicitly not designed in this pass.

## Experiment

**DESIRABLE.**

Proposition, derived directly from this pass's own findings (not the
authorizing task's illustrative example verbatim): **systems with
equivalent per-decision reconstructability guarantees (i.e., Regime C at
every decision point, per Contribution 2's own construction) can still
differ in trajectory-level reconstructability once decisions have
dependencies on each other** — motivated directly by
`composition-review.md`'s finding that local verifiability famously does
not guarantee global predictability in adjacent literature, and untested
for reconstructability specifically. Not designed here.

## Ready to draft?

**NO.**

## Strongest final thesis

> System-level understanding of an AI-mediated decision system is best
> treated not as a new property to be named, but as an open, precisely-
> stated question — whether Contribution 2's earned, per-decision
> reconstructability guarantee composes across a trajectory of
> interdependent decisions — which current compositional-verification
> research gives good reason not to assume holds by default.

---

## POST-VERDICT EXPERIMENT UPDATE (2026-08-25)

This section is appended, not a rewrite of anything above. The
"desirable" experiment this verdict called for (see "Experiment" above)
has since been designed, pre-registered, executed, and reported in
`experiment/`. Nothing above is superseded by this update — the update
answers the open question the prior verdict deliberately left open.

**Result: H1 supported.** Per-decision reconstructability (Local
Decision Reconstruction = 1.00 in both tested regimes, all 6 cases) does
**not necessarily** compose into trajectory-level reconstructability
(Trajectory Identifiability = 0.33 under the locally-complete-but-
globally-unlinked regime, vs. 1.00 once the one missing cross-decision
relation is supplied). Critically, the failure mode observed was honest
ambiguity, not false confidence: Dependency Edge Accuracy = 1.00, False
Global Confidence Rate = 0.00 across all cases tested. Full detail:
`experiment/RESULT.md`, `experiment/analysis/experiment-report.md`,
`experiment/analysis/results-summary.md`, raw data in
`experiment/results/`.

**Consequence for this verdict's own conclusions:**

- "Independent publication: UNCERTAIN" (above) is now **narrower but
  answerable**: the empirical precondition that section named
  ("conditional on further empirical work... that has not been done")
  has been done. A technical article is now survivable under the
  framing given in `experiment/RESULT.md` — "trajectory
  reconstructability requires an explicit retained cross-decision
  relation, not merely more per-decision detail" — strictly as an
  extension of Contribution 2's existing thesis, not a new named
  property, per this verdict's own repeated caution against resurrecting
  "Understanding Layer" or "capability-vs-understanding" framing.
- "Ready to draft? NO" (above) is **not overturned by this update**.
  Drafting Article 3 was explicitly out of scope for the experiment pass
  that produced this result and remains a separate authorization.
- "Strongest final thesis" (above) stands as the open question; this
  update reports that, for the two specific mechanisms tested
  (identical-value/branch/state-write provenance collision, and
  concurrent/near-concurrent ordering ambiguity), the answer to that
  open question is no, composition does not hold by default — consistent
  with, not contradicting, this verdict's prediction that
  compositional-verification research "gives good reason not to assume
  holds by default."

**Contribution 3 empirical phase: CLOSED**, pending separate
authorization to draft Article 3. See `experiment/RESULT.md` for full
scientific limitations (synthetic testbed, two mechanisms only, no
prevalence claim, no claim about human understanding).
