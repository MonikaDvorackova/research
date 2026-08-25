---
id: note-contribution-03-article-editorial-notes
title: "Contribution 3 Article — Editorial Notes (draft-v1)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, editorial-notes]
refs: [draft-v1.md, draft-v1-audit.md, ../experiment/RESULT.md]
---

## Scope and framing decisions

- The article is scoped exactly to the authorized thesis: compositional
  reconstructability of AI-mediated decision trajectories. It does not
  reopen "Understanding Layer," does not use capability-vs-understanding
  framing, and does not attempt a broad AI-understanding essay.
- The four things the article was explicitly told to contribute
  (decision-vs-trajectory distinction; the compositional failure mode;
  a controlled demonstration; an engineering implication) are each given
  their own section. The five things it was told not to contribute (new
  provenance architecture, new graph-theory result, new observability
  theory, new diagnosability theory, evidence of production prevalence)
  are each explicitly disclaimed in "This Is Not a New Provenance
  System" and "What the Experiment Does Not Show."

## Title selection

Eight candidates were generated and ranked. Full ranking:

1. **"When Reconstructable Decisions Produce an Unreconstructable
   System"** (chosen) — states the paradox directly in the title itself,
   uses no "AI" claim of uniqueness, and matches the opening section's
   own framing exactly.
2. "Local Reconstruction Is Not Global Reconstruction" — precise and
   general, but reads more like a lemma statement than an article title;
   held in reserve if reviewers find the chosen title too narrative.
3. "Why Individually Auditable AI Decisions Can Still Form an Ambiguous
   Trajectory" — accurate, but foregrounds "AI" in a way the article's
   own AI-specificity section argues against foregrounding.
4. "Decision Provenance Does Not Compose Automatically" — accurate and
   tight, but "provenance" in the title risks readers assuming the
   article claims a provenance contribution, which Section 8 explicitly
   disclaims.
5. "From Decisions to Trajectories: The Missing Relations in AI
   Reconstruction" — descriptive but flatter than 1–4.
6. "Perfect Decisions, Ambiguous History" — punchy, but underspecifies
   what "perfect" and "ambiguous" refer to without the subtitle doing
   most of the work.
7. "The Trajectory Is Not the Sum of Its Decisions" — evocative, risks
   being read as a stronger/more universal claim than the article
   supports ("not necessarily," not "never").
8. "What Composition Doesn't Give You for Free" — accurate but generic
   enough it could title several different articles in this space.

Title 1 was selected over Title 2 (the strongest technical alternative)
because the authorizing task asked for a publication title chosen "after
the article structure is clear," and once the opening-paradox structure
was drafted, the title that names the paradox directly read as the
better fit for a practitioner audience than the more lemma-like Title 2.

## Sourcing notes

Five citations used, all independently verified before drafting (not
carried over from source-ledger.md's search-summary-level entries
without re-verification, per that ledger's own disclosed caveat):

- [1] W3C PROV-DM and [2] OpenTelemetry Traces and [3] Fowler's Event
  Sourcing are reused from Contribution 2's draft-v2.md references list
  — those three were already independently confirmed there.
- [4] Sampath et al., "Diagnosability of Discrete-Event Systems," IEEE
  TAC 1995 — the foundational paper `source-ledger.md`'s S30 named only
  generically ("IEEE Xplore primary record"). Verified by direct web
  search returning the exact citation (volume 40, issue 9, pages
  1555–1575, September 1995) with a primary PDF link
  (wpage.unina.it/detommas/sed/1995_Sampath_Diagnosability_Automata.pdf)
  confirming the title and page header. Cited directly rather than via
  S30's placeholder.
- [5] Bakirtzis, G., Topcu, U., "AlgebraicSystems: Compositional
  Verification for Autonomous System Design," arXiv:2203.16343, 2022 —
  `source-ledger.md`'s S37. Verified by direct web search returning the
  arXiv abstract page confirming authors, identifier, and submission
  date (3 Mar 2022).

No citation in the article is sourced from a search-result snippet
without this direct verification step; no bibliographic metadata was
invented.

## Relationship to Contribution 2

Contribution 2's premise is summarized in two sentences in "What Has to
Compose" — enough to state what is being extended, not enough to
re-argue it. Contribution 2's own article, experiments, and frozen
acceptance decision were read only as intellectual scaffolding and were
not modified, re-cited beyond that one summary, or reopened.

## O'Reilly note (recorded only, not drafted)

A future synthesis chapter could trace a three-step arc across this
programme's contributions: decision-level control (Contribution 1) →
per-decision reconstruction (Contribution 2) → trajectory reconstruction
(Contribution 3) — each step widening the unit of analysis by exactly
one level, without any of the three requiring the others to be true for
its own claim to hold. This is recorded here as a possible future
framing note only; no O'Reilly material was drafted, edited, or
otherwise touched in this pass.

## What was deliberately left out

- No production case study or prevalence claim — the source material
  (`FINAL-RESEARCH-VERDICT.md`, `composition-review.md`) explicitly does
  not support one, and the article's own Limitations section says so.
- No new formal theorem or diagram of a "trajectory-binding
  architecture" — ruled out directly by the negative control (an
  ordinary trace field resolves the ambiguity) and by this task's
  explicit boundary list.
- No case-by-case fixture narration — the six cases are grouped by
  mechanism (value collision; near-concurrent ordering; control;
  negative control) rather than walked through individually, per the
  authorizing task's "do not narrate every fixture line" instruction.
