---
id: note-contribution-02-drafting-non-obvious-result
title: "Contribution 2 Drafting Readiness — The Article's Non-Obvious Result"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, thesis]
refs: [evidence-review.md, claim-ledger.md]
---

## Finding the Non-Obvious Result

The article cannot rest on "store more metadata" — that claim is both
obvious and, per `novelty-review.md` Objection 5, explicitly conceded as
mechanically trivial. This document evaluates the five candidate
formulations against the evidence and selects the strongest.

## Candidate formulations, evaluated

**A.** *Historical reconstructability depends not merely on preserving
the participating artifacts, but on preserving the relation that
identifies which artifacts actually participated in a decision.*
— **General, precise, fully supported.** This is the direct synthesis of
claim-ledger.md's class-A claims (3, 4, 5, 6). It is the article's actual
thesis-level statement, but on its own it is abstract — it needs a
concrete mechanism to land as non-obvious rather than as a truism.

**B.** *A system may retain every relevant version and still be unable to
uniquely reconstruct a historical decision.*
— **The accessible restatement of A.** This is the sentence a reader
remembers. It is a corollary of A, not independent content, but it is the
right *hook* sentence for an introduction — concrete, surprising on first
read, falsifiable.

**C.** *Temporal queries answer which state was valid according to the
retained history; they do not necessarily answer which state a historical
computation actually consumed.*
— **The precise mechanism.** This is what makes A non-obvious rather than
a truism: it names exactly *why* complete history can still fail — a
query against retained history answers a question about the record's
current best belief, not about what was actually relied upon at decision
time. This is the sentence a technically sophisticated reader needs to
be convinced, and it is exactly what `../temporal-semantics.md` argued
before either experiment ran and what the primary experiment then
measured.

**D.** *Under retroactive correction, a historically well-formed query
may produce a temporally coherent but factually incorrect reconstruction
of the original decision context.*
— **True, but scoped to one of the two tested mechanisms only** (the
primary experiment). Directly supported (class A), but stating it alone
would omit the follow-up's independent finding and understate the
article's evidence base.

**E.** *Under observational ambiguity, the correct result from an unbound
history may be "unknown" even when every candidate artifact still
exists.*
— **True, but scoped to the other mechanism only** (the follow-up), and
requires one correction for accuracy: in this implementation, B does not
merely risk returning "unknown" — it *correctly and reliably* returns
"unknown" (Ambiguity Detection Rate = 1.00 throughout). This is itself
worth stating as part of the finding: the failure under this specific
mechanism is honest, not silent, which is a materially different
(better) failure mode than D's.

## Selected formulation

**The article's non-obvious result combines A and C as the thesis-level
claim, uses B as the hook, and reports D and E as the two independently
demonstrated, differently-shaped concrete manifestations — not as two
separate claims to defend, but as evidence that the general claim (A+C)
is not a single coincidental result:**

> A system can preserve every version of every artifact a decision might
> have used, and still be unable to determine which ones it actually
> used — not because the data is gone, but because a query against
> retained history answers "what does the record now say was valid at
> t0," which is a different question from "what did this decision
> actually consume." That gap shows up in at least two independent ways:
> a record can be silently rewritten (retroactive correction), producing
> a confident, coherent, and wrong answer; or a record can be genuinely
> underdetermined (observational precision loss), producing an honest
> "unknown" rather than a wrong answer. Closing the gap requires
> preserving a relation between the decision and what it consumed — not
> preserving more history.

This is stronger than any single candidate alone: A+C is the general,
non-obvious claim; D and E are its two independently measured instances,
which is what makes A+C an empirical finding rather than an assertion;
and the honest-vs-confident distinction between D and E is itself a
result worth naming, not a footnote.
