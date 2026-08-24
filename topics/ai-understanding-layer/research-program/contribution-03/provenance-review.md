---
id: note-contribution-03-provenance-review
title: "Contribution 3 — Provenance & Replay Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, provenance, replay, debugging]
refs: [pre-research-claim-ledger.md, source-ledger.md, ../contribution-02/prior-art-audit.md]
---

## Scope note

Contribution 2's own prior-art audit (`../contribution-02/prior-art-audit.md`)
already covers W3C PROV in depth for the decision-reconstruction object
specifically. This review does not repeat that work; it extends outward
to (1) provenance theory *predating* W3C PROV, to check whether PROV
itself reinvented something older, and (2) deterministic replay/
time-travel debugging, which Contribution 2's audit did not cover.

## Provenance theory predates W3C PROV by over a decade

Buneman, Khanna, and Tan's "Why and Where: A Characterization of Data
Provenance" (2001) [S16] established the foundational **why-provenance**
(which source data influenced a given output) / **where-provenance**
(which specific location in the source the output value came from)
distinction, later joined by **how-provenance** in subsequent database-
provenance literature [S16][S17]. This work is a full decade older than
W3C PROV (2013) and formalizes, in database-theoretic terms, essentially
the same lineage concept PROV later standardized for general use.

**Consequence.** W3C PROV is not the origin of "provenance" as a formal
concept — it is a later, general-purpose standardization of ideas already
mature in database theory. This does not change Contribution 2's own
finding (PROV lacks native valid-time semantics), but it does mean any
future Article 3 claiming provenance itself as a recently-emerged
concern would be historically wrong — provenance has been formally
studied in computer science since at least 2001, arguably earlier in
scientific-workflow contexts.

## Deterministic replay and time-travel debugging

Record/replay systems capture "the minimal information necessary so
that a later re-execution reproduces the same instruction-by-instruction
behavior" [S18] — syscalls, file snapshots, network I/O, timing, and
randomness sources [S18][S19]. Production tools (e.g., `rr`, Pernosco)
are mature and "battle-tested" for real-world debugging [S18].

**What replay gives, precisely:** a faithful reconstruction of
*execution* — literally "the world as it was" during the original run
[S19]. **What it does not give, by the same sources' own scope:** any
normative judgment about whether that execution was *authorized* or
*justified*. This is exactly Contribution 2's own replay-vs-reconstruction
distinction (`../contribution-02/collision-tests.md` Task 6), confirmed
here as applying identically one layer up — at the level of "can we
understand system behavior generally," not just "can we reconstruct one
decision's context." A perfectly replayed execution answers *what
happened, and how*, not *why it was allowed to happen* or *whether it
should have*.

## Distinguishing reconstruction, interpretation, explanation, prediction, control

Per the authorizing task's explicit instruction not to merge these, and
grounded in what the sources reviewed actually support:

- **Reconstruction** (record/replay, provenance, Contribution 2's object):
  recovering *what* state/values/versions were involved. Answerable, in
  principle, by faithful history retention plus (per Contribution 2) a
  consumption relation.
- **Interpretation**: assigning meaning to reconstructed facts — e.g.,
  mechanistic interpretability's attempt to say what a learned
  representation *means* [S20] — a different operation than recovering
  that the representation existed.
- **Explanation**: a justificatory account of *why* an outcome occurred,
  addressed to a specific audience — XAI's object (see
  `ai-systems-review.md`) — distinct from reconstruction because a fully
  reconstructed history can still lack any explanatory account (this is
  exactly Contribution 2's sub-problem G, "the normative-synthesis
  step," `../contribution-02/problem-formalization.md`).
- **Prediction**: forecasting future behavior — not addressed by any
  mechanism reviewed in this document; belongs to evaluation/testing
  literature, out of scope here.
- **Control**: the ability to intervene and change behavior — Contribution
  1's object (decision-level enforcement), not this review's.

## Verdict

**Provenance theory (database-theoretic and W3C PROV) and deterministic
replay together cover reconstruction (Level 3–4, see
`prior-art-collision-matrix.md`) about as completely as any mechanism
reviewed in this whole programme — this is not a residual gap.** What
they do not cover, confirmed directly by their own stated scope in every
source reviewed: interpretation, explanation, and prediction are
different operations on top of reconstructed facts, not included in
"reconstruction" by any of the mechanisms surveyed. If Contribution 3
has a residual claim in this territory, it is that these five operations
(reconstruction, interpretation, explanation, prediction, control) are
not yet related to each other by any single framework this review found
— a **taxonomy gap**, not a missing mechanism (see `residual-gap-analysis.md`,
option D/E distinction).
