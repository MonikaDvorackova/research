---
id: note-contribution-02-article-editorial-notes-v2
title: "Article 2 — Editorial Notes (draft-v2)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, editorial-notes, v2]
refs: [draft-v2.md, ../review/VERDICT.md, ../review/BITEMPORAL-VERDICT.md]
---

## Editorial Notes — draft-v2

Draft-v1's own `editorial-notes.md` is not superseded wholesale — several
of its items (diagram production, venue questions) still apply
unchanged. This file records what's new or changed for v2 specifically.

## Word count

**2,519** (full file, including headings, code blocks, and the
References section) — tighter than draft-v1's 2,723, per the
authorizing brief's instruction that v2 should probably be slightly
tighter than v1. Within the 2,400–3,000 target range without padding.

## Remaining citation verification

- References [1] (W3C PROV-DM) and [4] (OpenTelemetry) reuse URLs
  already verified via live fetch in `../../prior-art-audit.md`'s
  original session (2026-08-22/23) — not re-fetched in this drafting
  pass, but not newly asserted either.
- References [2] and [3] (Microsoft SQL Server temporal tables; MariaDB
  system-versioned tables) were fetched live during the dedicated
  bitemporal-verification pass (`../review/bitemporal-verification.md`)
  and are the direct source of the corrected bitemporal claim in the
  "Experiment: When History Changes After the Decision" section.
- Reference [5] (Fowler, "Event Sourcing," 2005) is cited from
  `../review/citation-plan.md`'s existing REQUIRED list; not re-fetched
  in this pass — same status as [1]/[4], a previously-verified source
  reused, not newly asserted. **A dangling-reference issue was caught
  and fixed during this drafting pass itself**: [5] was initially listed
  in the References section but not cited inline; corrected to add the
  inline marker in the event-sourcing paragraph before this file was
  written.
- **No new external verification gap identified** beyond what
  `../review/citation-plan.md` already flagged and `../review/bitemporal-verification.md`
  already closed.

## Claims still requiring human judgment

- **Whether Case 8's specific FHC value should be quoted numerically.**
  Draft-v2 deliberately describes Case 8's false-confidence result
  qualitatively ("named a specific, wrong approver with full confidence")
  rather than citing its exact `fhc_rate` figure. Reason: Case 8's
  reported `fhc_rate` (1.00 in the raw data) reflects *both* its policy
  and authority dimensions being wrong-confident under the as-tested
  algorithm — but only the authority dimension is genuinely
  unrescuable (`../review/BITEMPORAL-VERDICT.md`); the policy portion of
  that same number shares the same algorithm-limitation caveat as Cases
  3/9. Citing "1.00" for Case 8 without that caveat would risk
  re-introducing a smaller version of the same overstatement this
  revision exists to fix. A human editor comfortable with a longer,
  more heavily caveated sentence could reinstate the exact number with
  the qualification attached; this draft chose the simpler, qualitative
  route instead. This is a judgment call, not a correctness requirement.
- **Whether to reinstate more of draft-v1's numeric density.** Draft-v1
  cited exact figures far more frequently. Draft-v2 is deliberately more
  qualitative in the two experiment sections that carry the corrected
  interpretation (to avoid re-introducing the exact kind of
  numeric-precision-without-interpretive-precision problem the
  verification pass found), while still citing exact figures wherever
  they are unambiguous (the follow-up's ADR=1.00/FHC=0.00 figures, which
  carry no such caveat). A human editor may prefer more numeric density
  throughout for consistency with Article 1's style; this is a legitimate
  stylistic alternative, not a correctness fix.
- **The closing bridge sentence** — same open question as draft-v1's
  editorial notes: keep or cut "Historical reconstructability is only one
  dimension of what it means to preserve understanding of a system over
  time." Unchanged from v1's own open question.
- **Whether the restructured order (follow-up experiment before the
  primary experiment) reads better than draft-v1's chronological order.**
  This was a deliberate structural choice (per the authorizing brief's
  suggested restructure) to put the cleaner, less-caveated experiment
  first. A human editor may have a different intuition about narrative
  flow; the current order is a recommendation, not a fixed requirement.

## Material deliberately cut from v1

- **The formal `R(D, x)` notation box** from v1's "What a Historical
  Decision Actually Depends On" section is not carried into v2's
  "Retained Is Not Consumed" section. Cut for length under the tighter
  target and because the prose alone (already present in both drafts)
  carries the same content; `../../drafting-readiness/formalization.md`
  already flagged this notation as optional, not load-bearing.
  Reinstating it would cost roughly 40–60 words if a future revision
  wants it back.
- **The extended "Property to Design For" callout box formatting** is
  condensed to a single blockquote in v2 rather than a separate
  standalone section with its own heading, to fit the tighter word
  budget — content is preserved, presentation is more compact.
- **Explicit enumeration of "not a new provenance architecture / not new
  temporal database theory / not a new event-sourcing mechanism"** (the
  authorizing brief's Section 8 framing) is present in spirit throughout
  "Prior Art, Revisited Honestly" but not restated as its own explicit
  bulleted disclaimer — the prior-art section's own conditional framing
  ("each can supply... whether a given deployment actually does is a
  separate question") already carries this without a redundant list. A
  human editor who wants the explicit bulleted form back can add it at
  low cost (~40 words).

## Unresolved venue issues (unchanged from v1)

- No venue is locked; v2 remains venue-agnostic, matching v1's own
  editorial notes.
- Whether this becomes an O'Reilly piece remains a separate, not-yet-made
  decision, per `../../../CHECKPOINT-2026-08-23.md`'s O'Reilly status and
  this task's explicit instruction not to adapt it for O'Reilly.
- Whether a published version should cross-link to Article 1 remains
  open, unchanged from v1.

## What changed structurally from v1 (for the record)

Restructured per the authorizing brief's suggested order: reconstruction
paradox → retained-vs-consumed → brief prior-art acknowledgment → the
timestamp-precision follow-up experiment (now presented first, as the
cleaner result) → the F10-6 negative control → the retroactive-correction
experiment (now presented second, with Case 8 as the lead illustration
and Cases 3/9 explicitly reframed) → full prior-art revisit with
citations → engineering property → implementation patterns → limitations
→ closing question. Draft-v1's chronological order (primary experiment
first, follow-up second) is fully preserved in `draft-v1.md`, untouched.
