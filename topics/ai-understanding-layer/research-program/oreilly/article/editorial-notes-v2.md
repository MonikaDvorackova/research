---
id: note-oreilly-article-editorial-notes-v2
title: "O'Reilly Article draft-v2 — Editorial Notes"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, editorial-notes, v2]
refs: [draft-v2.md, draft-v2-audit.md, review/revision-plan-v2.md]
---

Implements `review/revision-plan-v2.md` in full. `draft-v1.md` and the
complete `review/` package are unmodified.

## What changed, mapped to the revision plan

- **P0 (item 1):** Section "Reconstructing a Decision Later" rewritten.
  The requirement is now stated as informational, not representational
  — a preserved consumption relation "may be captured directly... or
  reliably derivable afterward," explicitly not requiring decision-time
  recording. Matches Article 2's frozen position exactly.
- **P1 (items 2–3):** All three unsupported-prevalence instances
  removed ("most systems," "most ML pipelines," "in most production AI
  systems") and replaced with non-quantified, structural framings.
  A fourth, related instance ("more heterogeneous inputs than most of
  the systems...") was caught during this session's own pre-audit grep
  pass and fixed the same way — not present in the original revision
  plan's three flagged instances, but the same pattern, corrected on
  sight rather than left in.
- **P1 (item 4):** "Will, sooner or later" / "will eventually" replaced
  with a design-necessity framing ("creates pressure to collapse an
  underdetermined record into a specific answer") — no deterministic
  future-behavior claim remains.
- **P1 (item 5):** "Exactly three possible outcomes" changed to "let a
  useful gate expose three operational outcomes."
- **P1 (item 6):** Retitled to "Authorized Now, Reconstructable Later."
  Dek rewritten to state the two-properties claim directly, no
  prevalence language.
- **P1 (item 7):** "Explainable"/"explain" removed as the primary term
  throughout; retained only in the one disambiguation sentence (Section
  1), which now explicitly states "where 'explain' appears below, it's
  shorthand for this" — so any informal recurrence elsewhere is
  pre-covered, though in practice no other instance remained.
- **P1 (item 8):** Five citations added — Kubernetes admission
  controllers, XACML/PDP-PEP, in-toto, SLSA, and Buneman/Khanna/Tan's
  why/where-provenance (ICDT 2001, previously verified elsewhere in this
  programme's `contribution-03/source-ledger.md` but unused in the
  O'Reilly piece until now). Citation [9] (formerly [4], Carlan et al.)
  retained with "et al." — no author list was fabricated.
- **P2 (item 9):** Section 7's checklist split explicitly into "what to
  preserve around the decision" (four decision-time categories) and
  "what a reconstruction process should be able to return" (identified/
  ambiguous/unavailable), with the reason stated directly ("not
  persisted at decision time, because it isn't known at decision time").
- **P2 (item 10):** The XAI-disambiguation sentence was tightened and
  placed immediately after the section's punchline rather than one
  paragraph later, shortening the window where a skimming reader could
  form the wrong impression. Given "reconstructable" is now the primary
  term throughout (title, dek, every heading), this risk is
  substantially lower than in draft-v1 regardless.
- **P2 (item 12):** Section 8's paragraph order was not changed —
  on review, the existing order (disclaimers, then payoff) reads
  acceptably once the payoff paragraph was itself tightened; flagged
  here as a considered, not overlooked, decision. If a future reviewer
  disagrees, swapping the two paragraphs remains a trivial edit.
- **Not changed, deliberately (item 11, low priority):** the
  fraud-scoring aside in Section 2 (one sentence) was left as-is — the
  revision plan marked this optional/low-priority, and it remains
  self-contained and does not compete with the primary running example.

## New material beyond the revision plan's explicit items

- The synthesis pivot paragraph ("Authorization asks... Reconstruction
  asks... A system can satisfy either property while failing the other")
  was added at the start of the reconstruction section, per the
  drafting task's Section 15 instruction — sharpening a moment
  `review/reviewer-report.md` §13 had already identified as present but
  implicit in draft-v1.
- Section 6 gained one explicit sentence naming dynamic/continuous
  assurance cases as "the closest" prior art to this article's own
  combined concern and stating plainly it "wasn't invented here," per
  the drafting task's Section 12 instruction and `review/reviewer-
  report.md` §9's finding that this objection deserved a more direct
  answer.
- The retroactive-correction example was compressed from a full
  standalone paragraph (draft-v1) into one sentence folded into the main
  reconstruction-requirement paragraph, per the drafting task's explicit
  instruction to cut or radically simplify it rather than preserve it
  merely because it existed in v1.

## Unresolved / flagged for the acceptance gate

- The four newly added infrastructure citations (Kubernetes, XACML,
  in-toto, SLSA) use well-known, stable canonical URLs for major
  standards/projects, based on high confidence rather than a fresh
  same-session verification fetch (unlike the Carlan et al. citation,
  which was independently verified via search in the prior review
  round). This is disclosed here per this programme's citation-hygiene
  discipline; the acceptance gate should decide whether this level of
  confidence is sufficient for these four specific, extremely
  well-established URLs or whether a narrowly-necessary verification
  pass is still warranted before any external submission.
- Word count: 3,783 (body, excluding References) — within the
  3,500–4,300 target and tighter than draft-v1's 3,882, without cutting
  any required content; the reduction comes primarily from compressing
  the retroactive-correction example.
