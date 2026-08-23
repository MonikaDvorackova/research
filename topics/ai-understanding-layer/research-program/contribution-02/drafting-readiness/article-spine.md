---
id: note-contribution-02-drafting-article-spine
title: "Contribution 2 Drafting Readiness — Article Spine"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, article-spine]
refs: [non-obvious-result.md, evidence-review.md, claim-ledger.md, thesis-and-titles.md]
---

## Article Spine

Target: an independent technical article, not yet assumed to be an
O'Reilly piece. This is the minimum argument structure, not prose — each
section names its job, its allowed claims (cross-referenced to
`claim-ledger.md`), and its evidence source. Section numbers follow the
authorizing instructions' progression.

### 1. A historical reconstruction problem

**Job:** ground the reader in a concrete case before any abstraction.
Start with a decision D at t0; at t1, every artifact involved in D still
exists somewhere in the system. Ask: can we reconstruct what actually
authorized D?

**Allowed claims:** none yet — this section is a scenario, not an
assertion. May reuse Source A's own six-months-later framing
(`../../sources/source-a-missing-layer.md`) as narrative inspiration, not
as evidence.

### 2. Why version retention appears sufficient

**Job:** present the strongest form of the "just version everything"
intuition, honestly, before undermining it — per `novelty-review.md`
Objections 3/4, do not strawman bitemporal/event-sourced/versioned
storage. State plainly: if every dependency has a complete history, isn't
"what was valid at t0" a solved query?

**Allowed claims:** B-class (prior-art claims) only — bitemporal theory
is decades old and complete for what it models (`prior-art-matrix.md`).

### 3. The distinction

**Job:** introduce the article's actual pivot — artifact existence
(x ∈ H(t1)) is not the same predicate as a preserved relation identifying
which x a decision consumed (R(d,x)). This is `non-obvious-result.md`'s
selected formulation (A+C).

**Allowed claims:** C-class (synthesis) — this section states the thesis,
not yet the evidence for it.

### 4. Failure mechanism 1 — retroactive correction

**Job:** use the primary experiment. Show the categorical TC flip on
Cases 3/8/9, and the False Historical Confidence result — B does not go
silent, it confidently names the wrong version.

**Allowed claims:** A-class only (`claim-ledger.md` claims 3, 5), scoped
exactly to the cited cases. Must state the control/forward-drift result
(B ≈ C) in the same breath, per `evidence-review.md` — omitting it would
make Regime B look strawmanned.

### 5. Failure mechanism 2 — observational temporal ambiguity

**Job:** use the follow-up. Show the honest-`AMBIGUOUS` result on
F10-2/3/4/5 — a *different*, better failure profile than mechanism 1's
confident wrongness, and worth naming as a distinct finding, not folded
into mechanism 1's framing.

**Allowed claims:** A-class only (claim 4), with the FHC=0.00 contrast to
mechanism 1 stated explicitly.

### 6. Negative control

**Job:** F10-6. This is structurally required, not optional — its
omission would leave the article implicitly defending "binding is
necessary," which claim 7 (`claim-ledger.md`) is class E, contradicted.
Show that an ordinary, non-binding causal event fully resolves the same
ambiguity Regime C resolves.

**Allowed claims:** A-class (claim 6). This section's entire purpose is
to prevent the article from reading as a sales pitch for one named
schema.

### 7. The engineering property

**Job:** name the general property both mechanisms' results converge on
— a preserved causal relation from decision to consumed context
(`terminology.md`'s "causal linkage/relation" entry). Optionally include
the boxed definition from `formalization.md` here.

**Allowed claims:** C-class only — this is interpretation of Sections 4–6
combined, not a new data point.

### 8. Existing mechanisms revisited

**Job:** show how provenance, event sourcing, and tracing *can* implement
the property from Section 7, when they retain the right causal relation
— using `prior-art-matrix.md`'s "ambiguity behavior" column and
`novelty-review.md`'s Objections 1/2/4 conclusions (conditional, not
unconditional, solutions).

**Allowed claims:** B-class, with the conditional framing from
`claim-ledger.md` claims 10/11 strictly enforced (no "always").

### 9. Architectural implication

**Job:** the practical recommendation — systems requiring historical
reconstructability should make the decision→consumed-version relation
explicit and durable, by whatever mechanism (binding record, causal
event, extended PROV graph) fits their existing architecture.

**Allowed claims:** C-class (recommendation follows from 4–8, is not
itself separately measured). Must not imply one specific schema is
mandated (claim 7 is class E).

### 10. Limits

**Job:** state plainly, in the reader's own words, not hedged into
invisibility: both experiments are synthetic; no prevalence claim is
made about real systems; no universal-mechanism claim is made (claims 12,
13, 14 in `claim-ledger.md` are class D and must not appear as findings
here or anywhere else in the article).

**Allowed claims:** explicitly negative — this section's job is to state
what is *not* claimed.

### 11. Conclusion

**Job:** land on the reframed question, per the authorizing instructions:
not "did we keep every version," but "did we preserve enough causal
structure to know which versions this decision actually used." Close with
`non-obvious-result.md`'s selected formulation, restated once more in its
shortest form.

**Allowed claims:** restatement only — no new claims introduced in the
conclusion that were not already licensed in an earlier section.

---

## What this spine deliberately excludes

No section argues capability-vs-understanding divergence, an
"understanding layer," fragmentation of explainability/observability/
governance, or any general claim about software-engineering history
beyond the specific mechanisms named in Sections 2 and 8 (bitemporal
databases, event sourcing, PROV — cited as prior art for *this*
contribution's problem, not as instances of a general historical
pattern). See `contribution-boundary-check.md` for the explicit scan
confirming this.
