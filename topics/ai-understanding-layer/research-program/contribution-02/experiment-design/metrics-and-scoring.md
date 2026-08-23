---
id: note-contribution-02-experiment-metrics
title: "Contribution 2 Experiment — Metrics, Scoring, and Success Criteria"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, metrics, falsifiability]
refs: [reconstruction-task.md, perturbation-matrix.md]
---

## Metrics, formally defined

All metrics are computed **per case, per regime**, then aggregated by
perturbation-case category (per `perturbation-matrix.md`), never as a
single pooled average across all ten cases — pooling would obscure exactly
the pattern (`research-question.md`) that distinguishes support for H1
from support for H0.

### 1. Artifact Identification Accuracy (AIA)

For each of the four version-bearing dependencies (policy, authority,
model, evidence), a binary score: `1` if the investigator's stated version
identifier (Q4, Q6, or the model/evidence equivalents) exactly matches
ground truth's true version identifier; `0` otherwise (including
`UNDETERMINED`, which is scored `0` here but tracked separately —
see Justification Completeness below). Reported as a proportion across
the four dependencies, per case.

### 2. Temporal Correctness (TC) — **PRIMARY METRIC**

Binary, per case: `1` if **both** Q4 and Q6 (policy version, authority
version) name the version whose valid-time interval actually contained t0
per ground truth; `0` if either names a version that was valid at some
*other* time (the "plausible but historically wrong" failure mode the
brief specifically requires the design to surface) or fails to determine
an answer at all. TC is stricter than AIA in that it is specifically
sensitive to *temporally wrong* answers, not just *any* wrong answer —
this is the metric most directly tied to the surviving thesis
(`../novelty-verdict.md`'s "versioned is not bound" formulation), because
the thesis is a claim about temporal correctness under drift specifically,
not about reconstruction accuracy in general.

**Why TC is primary:** the research question (`research-question.md`) is
not "can artifacts be found" (already conceded as solvable) but "are the
artifacts found the ones that were actually temporally valid at decision
time." TC operationalizes exactly that distinction and nothing broader.

### 3. Authorization Correctness (AC)

Binary, per case: `1` if the investigator's Q7 answer (GRANT/DENY/
UNDETERMINED) matches ground truth's true result; `0` otherwise. This is
the "bottom-line" outcome metric — of practical interest, but **not**
primary, because it is possible for AC to be correct "by accident" even
when TC is wrong (e.g., an incorrect policy version happens to produce the
same GRANT/DENY outcome as the correct one) or incorrect even when the
underlying reasoning was reasonable. AC alone would not distinguish the
mechanism the thesis targets from a coincidental match.

### 4. Justification Completeness (JC)

Proportion, per case: fraction of the four version-bearing answers (Q2
evidence, Q4 policy version, Q6 authority version, and the model version
where applicable) that are **not** `UNDETERMINED`, regardless of whether
they are correct. This measures whether the regime even supports
attempting an answer — a low-completeness, high-correctness result would
indicate a regime that is honestly silent rather than actively wrong,
which is a materially different (better) failure mode than the one below.

### 5. False Historical Confidence (FHC) — **PRIMARY DIAGNOSTIC METRIC**

Binary, per case, per version-bearing answer (Q4, Q6): `1` if the
investigator's answer is a **concrete, non-`UNDETERMINED` value** that is
**incorrect** per ground truth; `0` if the answer is correct, or if it is
honestly `UNDETERMINED`. FHC specifically isolates the failure mode the
brief calls out as "may be especially important": a reconstruction that
looks complete and confident but is silently wrong. This is scored
separately from — and is a stricter, more specific condition than — plain
incorrectness (an `UNDETERMINED` answer is wrong in the sense of being
incomplete, but is not a **false-confidence** failure, because it does not
mislead anyone into believing a wrong answer is correct).

**Why FHC is designated a primary metric alongside TC, not merely a
secondary one:** a thesis whose entire content is "reconstruction can be
wrong without anyone knowing it" is under-tested by TC alone, since TC
treats an honest `UNDETERMINED` and a confident-but-wrong answer as
equally "not temporally correct." FHC is the metric that specifically
distinguishes the two, and is therefore the sharpest available test of the
thesis's most distinctive claim.

---

## Scoring procedure

1. For each of the 10 cases × 3 regimes (30 total case-regime
   combinations), run the regime-appropriate deterministic procedure
   (`reconstruction-task.md`) to produce the 8 structured answers.
2. Score each answer set against that case's ground truth on AIA, TC, AC,
   JC, FHC as defined above.
3. Aggregate scores within each perturbation category defined in
   `perturbation-matrix.md` (control; forward-drift; retroactive-drift;
   combined-drift; concurrency-ambiguity) — five categories, not one pooled
   figure.
4. Compare Regime B's and Regime C's category-level scores directly,
   category by category. Regime A's scores are reported only to confirm
   the floor condition (`research-question.md`).

---

## Success and Failure Criteria

Stated in advance, precisely, and including the outcomes that would weaken
or kill the thesis — per the brief's explicit instruction not to hide
these.

### Strong support

Regime C achieves materially higher TC and lower FHC than Regime B
**specifically and only** on the retroactive-drift and concurrency-
ambiguity categories (Cases 3, 8, 9, 10), while both B and C achieve
comparably high TC on the control and forward-drift categories (Cases 1,
2, 4, 5, 6, 7). This is the pattern `../temporal-semantics.md` predicts
mechanistically, and its presence would be the cleanest possible
confirmation available from this design.

### Partial support

Regime C reduces FHC relative to Regime B (fewer silent wrong answers,
more honest `UNDETERMINED` responses) without a correspondingly large
improvement in raw AC (the bottom-line GRANT/DENY determination). This
would indicate binding improves **epistemic honesty and traceability**
more than it changes the final authorization outcome — a real, narrower,
and still-useful finding that would require reframing the thesis around
completeness/honesty rather than raw correctness.

### Null result

Regime B's TC and FHC scores are statistically/practically
indistinguishable from Regime C's across all perturbation categories,
including the retroactive and concurrency cases specifically. **This must
be reported as evidence that explicit decision-time binding is not
empirically justified by this experiment** — not reframed, not minimized.
Per `../novelty-verdict.md`'s own decision structure, this result would
push the surviving verdict from B (narrowed survival) toward C (framing
only): if bitemporal history alone, competently implemented, already
achieves what binding was hypothesized to add, the "binding" concept adds
rhetorical clarity but no measurable behavior.

### Evidence against the contribution

Regime B ≈ Regime C **and** both ≈ Regime A (i.e., even the basic,
uncontroversial versioning-helps claim shows no measurable advantage in
this design). This does not merely fail to support H1 — it calls the
experimental design itself into question (see the manipulation-check
discussion in `preregistered-interpretation.md`) and must be investigated
as a design defect before being read as evidence against the broader
research programme.

### What would specifically kill the thesis, stated directly

If, on Case 3 (the theoretically central retroactive-policy-drift case)
and Case 10 (concurrency ambiguity), Regime B's deterministic as-of-t0
query procedure achieves the same TC and FHC scores as Regime C's direct
binding lookup, the mechanism `../temporal-semantics.md` predicts does not
manifest even in the case designed specifically to surface it — this is
the single most damaging possible individual result and should be reported
as such without qualification if it occurs.
