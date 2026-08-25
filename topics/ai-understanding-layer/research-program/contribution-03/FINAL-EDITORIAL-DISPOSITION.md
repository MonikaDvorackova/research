---
id: note-contribution-03-final-editorial-disposition
title: "Contribution 3 — Final Editorial Disposition"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, editorial-decision, disposition]
refs: [article/review/VERDICT.md, FINAL-RESEARCH-VERDICT.md, ../PUBLICATION-ARCHITECTURE-FINAL.md]
---

Human editorial decision, following the completed adversarial review of
`article/draft-v1.md` (`article/review/VERDICT.md`). This is a
publication-architecture decision, not a research-validity finding —
every experiment, review, and document listed below remains part of the
permanent research record and is preserved unmodified.

## Status

- **RESEARCH COMPLETE.**
- **EMPIRICAL PHASE CLOSED.**
- **STANDALONE ARTICLE DEVELOPMENT CLOSED.**
- **RETAINED AS SUPPORTING RESEARCH NOTE** — "Trajectory Reconstruction
  and Honest Ambiguity." See `../PUBLICATION-ARCHITECTURE-FINAL.md` for
  its place in the programme's publication map.

## Article draft-v1

**FROZEN AS HISTORICAL RESEARCH-NOTE DRAFT.** `article/draft-v1.md` is
not modified by this decision. **No draft-v2 is authorized.**
`article/editorial-notes.md`, `article/draft-v1-audit.md`, and the full
`article/review/` package are preserved unmodified as part of the same
historical record.

## Reason for demotion (accurate, not a validity finding)

The research survives technically — the adversarial review found no
factual or numeric error anywhere in draft-v1
(`article/review/empirical-traceability.md`: zero discrepancies) — but
the standalone-publication case is too weak because:

1. **The central non-composition phenomenon has strong established
   prior art.** Compositional verification already establishes that
   local component correctness does not automatically imply global
   system correctness, for an adjacent property (predictability), before
   this experiment ran (`composition-review.md`; `article/review/
   reviewer-report.md` Objection 1).
2. **Workflow provenance already provides the relevant relation-
   preservation mechanism.** W3C PROV and, more precisely, the older
   Buneman why/where-provenance formalism already model exactly the
   cross-decision relation the experiment's Regime T2 adds
   (`article/review/prior-art-review.md`).
3. **The experiment's T1/T2 trajectory-identifiability direction is
   substantially structural.** `DecisionRecordT1`'s schema has no field
   capable of encoding a cross-decision relation at all; the four
   failing cases were, by design, constructed so no local fact resolves
   the ambiguity. The *direction* of the result is close to guaranteed
   by construction, not discovered (`article/review/reviewer-report.md`,
   Objection 6 — the review's most consequential single finding).
4. **Article 3's engineering consequence overlaps heavily with Article
   2.** "Preserve cross-decision relations, not just per-decision
   context" reads as a natural one-paragraph extension of Article 2's
   own "preserve the consumption relation" takeaway, not a qualitatively
   distinct engineering practice (`article/review/VERDICT.md`,
   Independence test: 2 of 5 criteria clearly passing).
5. **The strongest genuinely useful result is narrower than the original
   Article 3 thesis.** The one result the experiment's schema does not
   guarantee — that a well-built investigator's ambiguity is honest
   (Dependency Edge Accuracy = 1.00) rather than falsely confident (False
   Global Confidence = 0.00) — is real, non-trivial, and worth
   preserving, but it is a narrower claim than "trajectory
   reconstructability" as originally scoped for a standalone Article 3.

**The experiment is not invalid. Contribution 3 is not a failed
research effort.** Every number is traceable and correct; the honest-
ambiguity finding is genuine and retained (see below). What changed is
the publication-architecture judgment about whether this material
carries enough independent weight for a third, freestanding article
alongside Articles 1 and 2.

## Findings retained for synthesis

### A — Per-decision reconstructability does not necessarily imply unique trajectory reconstruction

**KEEP WITH QUALIFICATION.**

Qualification: cross-decision provenance is the established missing
relation — this is not a newly discovered failure mode, and the
direction of the T1/T2 gap is substantially built into the experimental
schema (see Reason 3 above). The finding is real as a controlled,
quantified demonstration for this specific object class (AI-mediated
decision trajectories), not as a novel discovery about composition in
general.

### B — Cross-decision dependency/provenance relations can resolve trajectory ambiguity

**KEEP.**

But: not a novel mechanism. Confirmed directly by the negative control
(C3-6): one ordinary trace field, of the kind workflow provenance and
distributed tracing already provide, resolves the ambiguity completely.
No new architecture is implied or required.

### C — AMBIGUOUS and WRONG are different reconstruction outcomes

**KEEP.**

This is the strongest surviving conceptual point from Contribution 3 —
see the "single strongest contribution" finding in `article/review/
VERDICT.md`. A reconstruction procedure that returns AMBIGUOUS when the
retained record genuinely underdetermines the answer is behaving
correctly, not failing; a procedure that confidently names a wrong
answer is a categorically worse failure. This distinction is worth
carrying into both Article 2's own framing and any future O'Reilly
synthesis.

### D — False Global Confidence = 0.00 in the controlled experiment

**KEEP as experiment-specific evidence only. Do not generalize beyond
the testbed.**

This is a real, non-guaranteed result about this specific investigator
design on these six cases — not a claim about false-confidence rates in
production AI-mediated systems generally. No prevalence claim was made
in draft-v1 and none should be introduced when this finding is reused
elsewhere.

### E — A new trajectory architecture/layer is required

**DROP.**

Explicitly ruled out by the negative control and by draft-v1's own
"This Is Not a New Provenance System" section. Never was a claim of this
programme; recorded here only to close off any future misreading of
Finding A as implying it.

### F — Understanding Layer

**DROP / RETIRED.** Unchanged from `novelty-verdict.md`'s prior
retirement (demoted to metaphor). This decision does not reopen it.

### G — Capability-vs-understanding

**DROP / RETIRED.** Unchanged from `FINAL-RESEARCH-VERDICT.md`'s prior
retirement. This decision does not reopen it.

## Preserved as permanent research record (unmodified)

Literature reviews (`historical-literature-review.md`, `program-
comprehension-review.md`, `observability-review.md`, `provenance-
review.md`, `ai-systems-review.md`), the operationalization,
diagnosability, and composition reviews, `prior-art-collision-matrix.md`,
`source-ledger.md`, `earned-premises.md`, `residual-gap-analysis.md`,
`novelty-verdict.md`, `research-questions.md`, `VERDICT.md`,
`FINAL-RESEARCH-VERDICT.md`; the full `experiment/` directory (design
docs, pre-registration, source code, tests, raw results, analysis,
`RESULT.md`); `article/draft-v1.md`, `article/editorial-notes.md`,
`article/draft-v1-audit.md`, and the full `article/review/` package.
None of these are rewritten by this decision. This document and
`../PUBLICATION-ARCHITECTURE-FINAL.md` are the new, additional records
that state the editorial disposition; they do not replace anything
listed here.
