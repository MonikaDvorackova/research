---
id: note-contribution-02-experiment-research-question
title: "Contribution 2 Experiment — Locked Research Question and Hypotheses"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, research-question, hypotheses]
refs: [../novelty-verdict.md, ../temporal-semantics.md, ../collision-tests.md]
---

## Locked Primary Empirical Question

> Given a historical AI-mediated decision D made at t0, for which all
> relevant dependencies (model/scoring version, evidence, policy, authority)
> are independently, fully versioned with complete history — does that
> independent versioning suffice for an investigator at t1 to reconstruct
> the policy-, evidence-, and authority-correct justification of D, or does
> temporally correct reconstruction additionally require an explicit,
> decision-time binding of D to the specific versions that applied at t0?

This is a refinement, not a replacement, of the brief's suggested wording.
The refinement makes explicit what "sufficient" means operationally
(defined in `metrics-and-scoring.md`) and names the comparison the brief
itself identifies as the scientific center: **Regime B (versioned,
unbound) against Regime C (versioned, bound)**. Regime A (bare) is retained
only as a floor/sanity-check condition, not as part of the primary
comparison — a design choice justified below.

**This experiment does not test whether preserving more information helps
reconstruction.** That proposition is already conceded as true and
uninteresting by the prior-art audit (`../collision-tests.md`, Objection 9)
and is not what distinguishes Verdict B (narrowed survival) from Verdict C
(framing only) in `../novelty-verdict.md`. The only proposition genuinely at
stake is narrower and sharper: **whether independent artifact versioning,
without an explicit per-decision binding, already suffices for temporally
correct reconstruction** — which, if true, would mean Contribution 2's
"binding" concept adds nothing beyond well-established versioning practice
and the thesis would collapse toward Verdict C.

---

## Why Regime A is not part of the primary comparison

Regime A (bare) answers a different, already-settled question: "does
retaining any version history help at all compared to retaining none."
`../prior-art-audit.md` and `../collision-tests.md` already establish this
affirmatively and uncontroversially (Objections 2, 4, 6 all confirm that
version history of some kind is necessary). Including A in the primary
statistical comparison would risk the experiment appearing to "prove" a
proposition nobody disputes, diluting the actual test. A is retained as a
**floor condition**: if B and C do not both clearly outperform A, something
is wrong with the case design itself (see `preregistered-interpretation.md`,
the manipulation-check row), not with the binding hypothesis.

---

## Hypotheses, made operational

### H0 — Null hypothesis

Explicit decision-time binding (Regime C) provides no meaningful
improvement over independently versioned but unbound artifacts (Regime B)
in **Temporal Correctness** (the primary metric, defined in
`metrics-and-scoring.md`) or **False Historical Confidence** (the primary
diagnostic metric), across the perturbation matrix defined in
`perturbation-matrix.md`.

**Operational rejection criterion:** H0 is treated as *not* falsified if, on
the pre-registered case matrix, Regime C's Temporal Correctness rate and
Regime B's Temporal Correctness rate differ by less than the pre-specified
practical-significance threshold (see below), **or** if any observed
advantage for C is confined to case types that do not include a retroactive
or concurrency-ambiguity perturbation (i.e., the advantage does not track
the specific mechanism the thesis predicts — see `temporal-semantics.md`).

### H1 — Primary hypothesis

Explicit decision-time binding materially improves Temporal Correctness
and reduces False Historical Confidence compared with independently
versioned but unbound artifacts, and this advantage is **concentrated in**
(not merely present alongside) perturbation cases involving retroactive
policy/authority correction or decision-attribution ambiguity — the specific
failure mechanism identified in `../temporal-semantics.md` (the
transaction-time/valid-time confound) and `../collision-tests.md`
(Objection 8).

**Operational support criterion:** H1 is supported if Regime C achieves a
materially higher Temporal Correctness rate than Regime B specifically on
the retroactive-correction and concurrency-ambiguity cases (Cases 3 and 10
in `perturbation-matrix.md`), while both regimes achieve comparable,
reasonably high scores on the no-drift and simple-forward-drift cases —
i.e., the gap has the *shape* the theory predicts, not merely a raw average
gap that could be produced by an unrelated design asymmetry.

---

## Why this is not a significance-testing (p-value) design, and what replaces it

A frequentist hypothesis test requires either random sampling from a
population or a large enough case count for asymptotic guarantees to be
meaningful. Neither holds here: the case matrix (`perturbation-matrix.md`)
is a **deliberately constructed, non-random set of ~10 cases**, designed to
isolate specific failure mechanisms, not sampled to represent a population
of real-world decisions. Computing a p-value over 10 hand-designed cases
would manufacture false statistical authority the design cannot support,
which the brief explicitly warns against.

**Replacement method: a pre-registered, pattern-based diagnostic
evaluation**, structurally closer to a set of unit/regression tests with a
graded rubric than to a statistical trial:

1. Each case is scored independently against ground truth on each metric
   (`metrics-and-scoring.md`), producing a per-case, per-regime, per-metric
   result (not a single aggregate score).
2. Results are organized into the case-type categories the perturbation
   matrix defines (no-drift, isolated-forward-drift, isolated-retroactive-
   drift, concurrency-ambiguity, combined-drift).
3. The **pattern** of where B and C diverge — not a single averaged
   difference — is what confirms or disconfirms H1, per the interpretation
   table pre-registered in `preregistered-interpretation.md` *before* any
   case is run.
4. "Material improvement" is defined qualitatively but concretely in
   advance: a difference is material if it changes the categorical outcome
   of Temporal Correctness (correct → incorrect, or correct → honestly
   flagged as undetermined) on a majority of cases within a perturbation
   category, not merely a difference in a continuous score. This avoids
   needing an arbitrary numeric threshold while still being falsifiable —
   the criterion is stated precisely enough that a future disagreement
   about "was H1 supported" can be resolved by re-inspecting the same
   fixed rubric, not renegotiated after seeing results.

This is a deliberate, disclosed methodological choice: the experiment is
designed to be **diagnostic and falsifiable**, not to produce a p-value that
would misrepresent the nature of a ten-case, purpose-built synthetic study.
