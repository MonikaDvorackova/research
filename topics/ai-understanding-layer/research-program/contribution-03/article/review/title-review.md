---
id: note-contribution-03-article-title-review
title: "Contribution 3 Article draft-v1 — Title Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, title]
refs: [../draft-v1.md, claim-review.md]
---

## Current title

**"When Reconstructable Decisions Produce an Unreconstructable System"**

## Attack

- **"System" is too broad.** The experiment measures trajectory-level
  dependency-edge identifiability across a small, bounded sequence of
  decisions — not any broader notion of "system" (deployed state,
  configuration, full operational history). `../../generalization-from-
  c2.md` explicitly places "deployed-system-state reconstructability"
  (G4) out of scope and "requiring new evidence" beyond what this
  experiment tested. The title claims a unit of analysis one level
  larger than what was tested. Classified **OVERSTATED** in
  `claim-review.md`.
- **"Unreconstructable" is too absolute.** Even in the four failing
  cases, the record is not uninformative — the investigator narrows to
  the exact tied candidates (e.g., "D1 or D2") and names them; it never
  collapses to "nothing is known." "Unreconstructable" reads as a
  stronger, more total failure than AMBIGUOUS-with-named-candidates
  actually is, and sits in tension with the article's own careful
  "ambiguous, not wrong" framing in its second-strongest section.
- **Does the title imply T1 always fails?** Yes, on a natural reading —
  "produce an unreconstructable system" reads as a general causal claim
  about what reconstructable decisions do, when the actual result is
  4/6 *deliberately constructed* cases, by design (see Objection 6 in
  `reviewer-report.md`). A reader has no way to recover "4 of 6, by
  construction" from the title alone.
- **Does "reconstructable decisions" read naturally?** Mostly yes, but
  it is shorthand for "individually/locally reconstructable decisions"
  — acceptable compression for a title, not a major issue on its own.

**Verdict: the title overclaims on both scope ("system") and severity
("unreconstructable"), independently of each other.** Both should be
fixed in v2; fixing only one would leave the other overclaim in place.

## Alternatives (6–8, ranked by category)

1. **Precise technical:** "Decision-Level Reconstructability Does Not
   Imply Trajectory-Level Reconstructability" — accurate, but reads as a
   lemma statement rather than an article title; best suited if the
   article compresses toward a research-note register (see
   `revision-plan-v2.md`).
2. **Practitioner:** "Your Decisions Are Auditable. Is the Path Between
   Them?" — punchy, correctly scoped to "path" rather than "system,"
   avoids "unreconstructable"'s absolutism; strongest practitioner
   candidate.
3. **Conservative research:** "On the Non-Composition of Decision
   Reconstructability Across a Trajectory" — precise and appropriately
   modest; reads as a research note title, which matches this review's
   publication-classification finding (see `VERDICT.md`).
4. **O'Reilly-style:** "The Missing Link Between Auditable Decisions and
   an Auditable Workflow" — accessible, correctly uses "workflow" rather
   than "system," softer than "unreconstructable."
5. **Local/global contrast (runner-up from editorial-notes.md):** "Local
   Reconstruction Is Not Trajectory Reconstruction" — precise, general,
   avoids both flagged overclaims; the strongest single replacement if
   only one axis of the title can change.
6. **Fixed-scope variant of the original:** "Reconstructable Decisions,
   Unreconstructable Trajectory" — preserves the original's rhetorical
   structure and paradox framing while swapping "System" for
   "Trajectory," directly fixing the scope overclaim; still carries the
   severity overclaim from "Unreconstructable" unless further softened.
7. **Softened original:** "When Reconstructable Decisions Produce an
   Ambiguous Trajectory" — fixes both flagged issues at once (system→
   trajectory, unreconstructable→ambiguous) while keeping the original's
   paradox structure and most of its name recognition within this
   review.
8. **Question-form practitioner:** "Every Decision Checks Out. Can You
   Still Reconstruct What Happened Between Them?" — leans on the
   article's own strongest opening device (the D1→D4 walkthrough);
   riskier tonally for a technical audience.

## Recommendation

**Do not rename draft-v1** (out of scope for this review). If v2 is
authorized: **Option 7 ("When Reconstructable Decisions Produce an
Ambiguous Trajectory")** is the recommended primary — it fixes both
flagged overclaims with the minimum structural change, preserving the
title's proven rhetorical hook. **Option 5 ("Local Reconstruction Is Not
Trajectory Reconstruction")** is the recommended runner-up, especially
if v2 compresses toward the research-note register this review's
publication classification suggests (see `VERDICT.md`).
