---
id: note-oreilly-submission-diagram-spec
title: "O'Reilly Submission — Diagram Specification"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, submission, diagram]
refs: [../article/draft-v2.md, article-submission.md]
---

## Decision: include the diagram

**Yes.** The article's one conceptual diagram (currently a plain-text
block in "What to Actually Build") earns its place — it is the only
place the article shows, rather than describes in prose, how the
authorization and consumption relations both attach to one decision
record. It is not decorative; removing it would leave the checklist
section's two-part split (`article-submission.md`, "What to Actually
Build") without a visual anchor.

## What it must communicate

Exactly the flow already used in the article, nothing added:

```
model output → proposed decision → authorization gate → action
                        |
                  decision record
                        |
        +---------------+----------------+
        |                                |
authorization relation           consumption relation
        |                                |
"why was it allowed?"          "what did it actually use?"
```

Two structural facts the diagram must preserve, not simplify away:

1. **The gate sits between the proposed decision and the action** — it
   is what turns a proposed decision into an authorized one, not a
   separate, disconnected step.
2. **The decision record branches into exactly two relations**, not
   three or more — this matches the article's own claim precisely
   (authorization and consumption are the two properties; dependency
   relations, mentioned in the checklist text, are a cross-decision
   extension of the consumption side, not a third top-level branch, and
   should not be added to the diagram to avoid overstating its scope).

## Format recommendation

**Plain-text block, as currently used in `article-submission.md`, not
Mermaid.** Reasoning: no repository or O'Reilly-CMS convention for
rendering Mermaid was confirmed during this session (matching Article
2's own unresolved diagram question, `contribution-02/article/
FINAL-ACCEPTANCE.md`), and a plain-text diagram renders identically in
every Markdown preview, every plain-text pitch email, and any CMS that
doesn't support diagram rendering — the safer default until O'Reilly's
actual production format is confirmed.

If O'Reilly's editorial team requests a rendered figure (a real
possibility for a published piece, common for O'Reilly technical
articles), the same five-node structure above converts directly to a
simple box-and-arrow illustration: one horizontal chain of four boxes
(model output → proposed decision → authorization gate → action) with
one box (decision record) hanging below the "authorization gate → action"
join, branching to two boxes (authorization relation, consumption
relation) with the two questions as captions underneath. **TO CONFIRM
WITH EDITOR** whether a rendered figure is required or whether the
plain-text version is acceptable as submitted.

## Caption

*"A decision record splits into two relations that answer different
questions: what authorized the decision, and what it actually
consumed. Neither one substitutes for the other."*

## What not to do

- Do not add a third branch for "dependency relations" — this would
  visually imply a three-way split the article's own thesis doesn't
  claim (see structural fact 2 above).
- Do not add the "identified / ambiguous / unavailable" reconstruction
  outcomes to this diagram — they are outputs of a later process, not
  part of the decision-record structure this diagram depicts, and
  combining them here would reintroduce exactly the decision-time-vs-
  later-output conflation `oreilly/article/review/reviewer-report.md`
  §12 flagged and draft-v2 corrected. A second, small diagram for the
  reconstruction-outcome triad is not necessary — the prose in "When the
  Record Can't Decide" carries it without a visual aid.
