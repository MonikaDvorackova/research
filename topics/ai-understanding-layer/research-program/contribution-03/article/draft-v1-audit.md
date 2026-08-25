---
id: note-contribution-03-article-draft-v1-audit
title: "Contribution 3 Article draft-v1 — Self-Audit"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, audit]
refs: [draft-v1.md, editorial-notes.md, ../experiment/RESULT.md]
---

## Word count

**3,257 words** (full file, `wc -w draft-v1.md`, including headings,
code/inline-formula text, and references). Within the authorized
2,500–3,300 range.

## Composition claim

**PASS.** The closing section states the finding as "not *necessarily*
reconstructable as a trajectory" (draft-v1.md line 107), matching the
authorized thesis exactly. The provenance section states "does not
entail" (line 87), not "never entails" or "cannot." No sentence in the
article claims universal, unconditional non-composition. Grepped
directly for "does not compose" (unqualified) and "always" / "never" in
a composition context — none found unqualified.

## Local validity

**PASS.** "Perfect Local Records, Ambiguous Global History" states Local
Decision Reconstruction = 1.00 in both regimes across all six cases
*before* stating the Trajectory Identifiability numbers, and explicitly
frames this as the experiment's own precondition, checked rather than
assumed. This matches `experiment/results/aggregate_by_regime.json`
exactly (`local_decision_reconstruction_rate: 1.0` for both T1 and T2).

## Negative control

**PASS.** Given its own section ("The Relation That Resolves the
Ambiguity"), not a footnote. States directly that the negative control
"rules out a stronger, more dramatic claim" and that the result supports
only "preserving an ordinary cross-decision dependency relation is
sufficient," not a new architecture requirement.

## Prior art

**PASS.** "This Is Not a New Provenance System" concedes workflow
provenance (W3C PROV [1]), distributed tracing [2], and event sourcing
[3] each already model the relevant relation, and states plainly "this
piece is not a new provenance mechanism, and does not claim to be one."
The strongest objection ("isn't this just workflow provenance?") is
posed as the section's own opening question and answered honestly
("largely, yes"), matching the authorizing task's explicit instruction
to address this objection directly rather than deflect it.

## Novelty

**PASS.** No claim of a new mechanism, new theorem, new architecture, or
new named property anywhere in the article. The provenance section
explicitly attributes the relevant formal vocabulary to existing fields
(diagnosability [4], compositional verification [5]) and states the
article's own contribution as "a controlled demonstration... not a new
theoretical result" in substance, matching `composition-review.md`'s own
verdict language ("not a new theoretical result").

## AI specificity

**PASS.** "The Composition Question" states directly: "the same
composition question applies to any system built from dependent,
individually-auditable steps" and "every mechanism that closes it
already exists." The provenance section attributes the general
composition caution to compositional-verification literature "well
outside any AI context." AI-mediated systems are presented as the
domain of application (multi-step decisions, model calls, tool
invocations), never as the origin of the underlying principle.

## Experiment traceability

**PASS.** All four headline numbers quoted in the article (LDR=1.00,
T1 Trajectory Identifiability=0.33, T2=1.00, Dependency Edge
Accuracy=1.00, False Global Confidence=0.00) match
`experiment/results/aggregate_by_regime.json` exactly:
`trajectory_identifiability_rate` T1 = 0.3333... (article rounds to
0.33, consistent with `RESULT.md`'s own rounding), T2 = 1.0;
`dependency_edge_accuracy` = 1.0 for T1; `false_global_confidence_rate`
= 0.0 for T1. The "two of six" and "four of six" case counts match
`experiment/results/case_level_results.csv` (`trajectory_identifiable`
True for exactly C3-1 and C3-6, False for C3-2/3/4/5).

## Sample-size discipline

**PASS.** "What the Experiment Does Not Show" states directly that six
designed cases "are not a statistical sample and no inference about a
broader population is appropriate from them." No p-value, confidence
interval, or prevalence estimate appears anywhere in the article.

## Article 2 boundary

**PASS.** Contribution 2's result is summarized in two sentences in
"What Has to Compose," stated as an established premise being extended,
not re-argued, re-tested, or contradicted. No claim in this article
revises or reopens any conclusion in Contribution 2's frozen
`draft-v2.md` or `FINAL-ACCEPTANCE.md`; both were read only as
scaffolding and remain untouched (confirmed via `git status`, see
`RESULT.md`-equivalent validation step below).

## Understanding Layer non-resurrection

**PASS.** Grepped `draft-v1.md` case-insensitively for "understanding
layer," "capability-vs-understanding" (and the hyphenation variants),
"epistemic debt," "global intelligence," "system knowledge
preservation," and "understanding architecture" — zero matches.

## Citation sanity

**PASS.** Grepped for inline `[n]` markers: `[1]`, `[2]`, `[3]`, `[4]`,
`[5]` each appear exactly once in the body (all five within "This Is Not
a New Provenance System," the section they support) and each has a
corresponding entry in the References list — no dangling references, no
unused reference entries. [4] and [5] were independently re-verified by
direct web search before drafting (see `editorial-notes.md`, Sourcing
notes) rather than carried over from `source-ledger.md`'s
search-summary-level entries unverified.

## Overall

**PASS on all nine required checks.** No violation required a fix before
finalizing this draft.
