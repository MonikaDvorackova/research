---
id: note-contribution-03-operationalization-review
title: "Contribution 3 — Operationalization Review (RQ1)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, operationalization, RQ1]
refs: [VERDICT.md, residual-gap-analysis.md, diagnosability-review.md]
---

## RQ1

> Can system-level understanding of an AI-mediated system be
> operationalized as a technically meaningful property without merely
> renaming observability, provenance, interpretability, or assurance?

## Rejecting the scalar assumption

Testing whether "understanding" is one scalar U, a vector, or an
umbrella term (Section 13 of the original review's own decision list;
Section 2 of this pass). Seven provisional dimensions were tested
against literature, not assumed:

| Symbol | Candidate dimension | Independent, or reducible to an existing named field? |
|---|---|---|
| R | Reconstructability | **Reducible** — formally, near-identical to **diagnosability** (discrete-event systems theory: "the occurrence of [an event] can be determined after a finite number of subsequent events... by observing the generated output sequence" [S30][S31]), applied to a different observable (which version was consumed, not which fault occurred). See `diagnosability-review.md`. |
| O | Observability | **Reducible** — this is literally control theory's own term, unmodified [S14]. |
| P | Provenance/lineage completeness | **Not clearly a capability at all** — it is a precondition (evidence availability) that R and O consume, not a distinct inference-capability dimension in its own right. |
| I | Interpretability | **Reducible** — XAI's own established term [S22][S24]; operates almost entirely at Level 1 (model). |
| B | Behavioral predictability | **Reducible** — this is **system identification**'s own object: "building mathematical models of dynamic systems from observed input-output data... allows predictions of future system responses" [S32]. |
| V | Verifiability | **Reducible** — formal/runtime verification's own object: "does the system's behaviour conform to requirements" [S25]. |
| C | Controllability/intervention | **Reducible, and doubly so** — control theory already has a distinct, formal meaning for "controllability" (can the system be driven to any desired state), and Contribution 1 already claims this territory under "decision-level enforcement." Using the word again for a third meaning would be a genuine terminology collision, not a new contribution. |

**Finding: every single candidate dimension reduces to an already-named,
already-formalized property in an existing field.** None survives as an
independent, novel technical property. This directly answers the "are
these independent, or redundant" question the authorizing task poses:
they are not novel; several (R vs. O vs. V) are genuinely distinguishable
from each other (see `diagnosability-review.md` for the R-vs-O
distinction specifically), but distinguishable-from-each-other is not
the same as new.

## Are some properties of the system, others of an observer?

Yes, and this distinction survives scrutiny. Observability, diagnosability,
and interpretability are all defined **relative to an observer's
available information set** (control theory's own definition: "how well
[state] can be determined **from its outputs**" — outputs available to
whom, is a load-bearing free variable). Verifiability is defined relative
to a **specification**, not an observer. Behavioral predictability
(system identification) is defined relative to a **model class** the
identifier is willing to entertain. This means a single "system-level
understanding" scalar was never well-posed to begin with — the
dimensions differ not only in what they measure but in what they are
measured *relative to*, confirming the vector framing over the scalar
framing on independent grounds.

## The operationalization test, applied to the one candidate that survives

Per the required six-part test, applied to the only dimension this
review's `earned-premises.md` and `generalization-from-c2.md` actually
earn evidence for — **decision-context reconstructability (R)**:

1. **Object:** a specific historical decision (or, per
   `generalization-from-c2.md`, tentatively an execution/trajectory).
2. **Observer:** an investigator at a later time, possessing only
   retained system records (not privileged access to ground truth).
3. **Information set:** whatever history, traces, and consumption
   relations the system's preservation regime retains — exactly
   Contribution 2's own Regime A/B/C framing.
4. **Task:** determine, uniquely and correctly, which version of each
   relevant dependency the decision consumed.
5. **Metric:** Temporal Correctness / False Historical Confidence /
   Ambiguity Detection Rate — Contribution 2's own metrics, already
   built and validated.
6. **Counterexample:** yes, directly demonstrated — Contribution 2's own
   Regime B vs. Regime C, and the follow-up's honest-ambiguity cases,
   are systems with identical task performance (both regimes reach the
   same GRANT/DENY outcome in several cases) that differ sharply on this
   property.

**This one dimension passes the operationalization test completely** —
but it already exists, fully specified, in Contribution 2. It is not a
new result of this pass; it is confirmation that Contribution 2's own
object is the *only* dimension in the candidate vector this programme
has actually operationalized and tested. No other dimension in the
table above has been operationalized by this programme, and this review
found no other source that operationalizes them *jointly*, across a
multi-component AI decision system, either.

## Verdict on RQ1

**PARTIALLY.**

System-level "understanding" can be operationalized — but only as a
**vector/taxonomy of already-named properties** (diagnosability-shaped
reconstructability, observability, interpretability, system-
identification-shaped predictability, verifiability), each already
formalized in its own field, **not as one new scalar and not as one new
named umbrella property**. The one dimension this programme has actually
operationalized and tested (decision-context reconstructability) is
Contribution 2's own already-earned result, reduced formally here to
diagnosability theory — a genuine, if modest, synthesis-level connection
(see `diagnosability-review.md`), not a new discovery.

**Consequence for Article 3 classification:** this rules out option A
(a new operationalizable technical property) — every dimension reduces
to existing terminology, satisfying exactly the condition this task's
Section 24 rules out. What remains open is whether the *specific joint
composition* of these dimensions, applied to multi-component AI decision
systems, is itself a defensible synthesis or research-agenda
contribution — addressed in `composition-review.md` and
`article-03-options.md`.
