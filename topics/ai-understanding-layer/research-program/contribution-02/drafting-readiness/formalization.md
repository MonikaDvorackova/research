---
id: note-contribution-02-drafting-formalization
title: "Contribution 2 Drafting Readiness — Minimal Formalization Decision"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, formalization]
refs: [terminology.md, ../experiment/followup-case10/RESULT.md]
---

## Should the article include a minimal formalization?

**Decision: yes, in a lightly adjusted form, as an optional boxed
definition — not as the article's spine, and with no theorem or proof.**

## Checking the candidate formalization against the evidence

The candidate definition (decision d at time t, consumed context
C(d) = {m, p, e, a, c}, retained state H(t1), reconstruction identifiable
iff a preserved relation R exists such that R(d, x) uniquely identifies
each relevant x ∈ C(d) from H(t1)) is checked below rather than adopted
blindly, per the instruction.

- **Against the experiments:** holds up well. "R exists such that R(d,x)
  uniquely identifies x" is exactly what Regime C's reconstruction
  algorithm computes (a direct lookup via the binding record) and exactly
  what Regime B's algorithm fails to compute when, and only when, no such
  R is available (retroactive correction removes R's reliability;
  precision loss removes R's existence for the affected dimension). The
  formal statement "x ∈ H(t1) does not entail R(d,x)" is precisely the
  primary experiment's central finding, stated formally.
- **Against F10-6:** this is the important check, because F10-6 is what
  narrowed the thesis. The formalization already generalizes correctly —
  R is *any* sufficient preserved relation, not specifically a
  `DecisionBindingRecord`. F10-6's causal_consumption_event is simply a
  second instantiation of R. **No adjustment needed here** — the original
  formulation already avoided over-committing to one implementation,
  which is worth noting as a point in its favor.
- **Against prior art:** consistent with `prior-art-matrix.md` — every
  row that "survives" an objection is exactly a row where R can be made
  to exist (PROV with version-identified Entities; event sourcing
  capturing identifiers; bitemporal storage for D/E specifically, subject
  to the transaction-time caveat).
- **Against temporal-semantics.md:** requires one addition. The primary
  experiment's finding is not fully captured by "R exists or does not" —
  it is that **R can exist, be queried correctly, and still return the
  wrong value**, because the retained state H(t1) itself is *not fixed*:
  a retroactive correction changes what querying H(t1) returns for the
  same (d, x) pair before and after the correction. The formalization
  needs H to be indexed by transaction time (H(t1) is itself a snapshot
  of an evolving record, not a static object) for this to be represented
  faithfully.
- **Against the follow-up's AMBIGUOUS outcome:** requires a second
  addition. "Uniquely identifies" is binary in the original formulation;
  the follow-up's central design choice (Step 7 of the authorizing
  instructions) was to make "cannot uniquely identify, and says so" a
  distinct, better outcome than "identifies incorrectly." A formalization
  that only has a true/false "identifiable" predicate cannot represent
  this distinction, which is empirically the sharpest result in the
  follow-up (FHC = 0.00 there because ambiguity is reported honestly).

## Adjusted formalization (if included)

```
Let d be a decision made at true time t, with consumed context
C(d) = {m, p, e, a, c} (model, policy, evidence, authority, context).

Let H(τ) be the system's retained state as queried at transaction time τ
(τ ≥ t) -- H is a function of WHEN it is queried, not a fixed object,
because retained records can themselves be corrected after the fact.

For x ∈ C(d), a query R(d, x, τ) against H(τ) returns exactly one of:
  UNIQUE(v)     -- a single candidate value v
  AMBIGUOUS(S)  -- a set S of >=2 equally compatible candidates
  ABSENT        -- no candidate

Decision-context identifiability holds for (d, x, τ) iff
  R(d, x, τ) = UNIQUE(v)  and  v is the value d actually consumed.

x ∈ H(τ) (the value exists somewhere in retained state) does not entail
identifiability -- neither does R(d, x, τ) = UNIQUE(v) alone, since v may
be UNIQUE and wrong (the primary experiment's finding, arising from H's
dependence on τ) rather than merely absent (the follow-up's finding,
which instead produces AMBIGUOUS, not UNIQUE-and-wrong, when the query
procedure is required never to guess).
```

## Verdict on inclusion

**Keep, but scoped tightly.** This is a genuinely minimal formalization
(one function, one three-way-valued query, one identifiability
predicate) that adds real clarity — specifically, it is the only way to
state precisely *why* "x ∈ H(t1)" (artifact retention) and
"identifiability" (reconstruction) are different predicates, which is
the article's entire non-obvious result stated formally in four lines.
It does not manufacture false sophistication: no theorem is claimed, no
proof is offered, and the box should be captioned as a **definition that
makes the two experiments' shared structure explicit**, not as a
theoretical result the experiments then verify. If a draft's tone or
venue disfavors any formal notation, the same content survives fully in
prose (`non-obvious-result.md`'s selected formulation) and the box can be
dropped without losing any claim.
