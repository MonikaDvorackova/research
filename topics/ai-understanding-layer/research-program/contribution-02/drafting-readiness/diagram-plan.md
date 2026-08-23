---
id: note-contribution-02-drafting-diagram-plan
title: "Contribution 2 Drafting Readiness — Diagram Plan"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, diagrams]
refs: [article-spine.md, ../experiment/experiment-design/preservation-regimes.md]
---

## Diagram Plan

Three diagrams, each tied to a specific article section
(`article-spine.md`) and a specific experimental fact — none decorative.

### Diagram 1 — Versioned but Unbound (Regime B)

**Article placement:** Section 2/3 (why version retention appears
sufficient; the distinction).

**Content:** Decision D as a distinct node, drawn separate from four
parallel history tracks: policy history, authority history, evidence/
event trace, model history — each shown as a sequence of versioned
boxes along its own timeline. No arrow connects D to any specific box in
any track. A dashed, question-marked line from D toward the policy
track's t0-region signals "which one?" without resolving it.

**What it must get technically right:** every history track must show
*more than one* version (so the diagram itself demonstrates that
versioning exists and is not the missing piece), and D's timestamp must
sit visibly between two policy-track boxes, mirroring the primary
experiment's Case 2/3 structure (a policy boundary near t0) — this is
what makes the "which one?" question genuine rather than decorative.

**Caption anchor:** "Every dependency has a complete history. Nothing
says which slice of each history this decision used."

### Diagram 2 — Preserved Causal Context (Regime C / F10-6)

**Article placement:** Section 6/7 (negative control; the engineering
property).

**Content:** Identical to Diagram 1 — same D, same four history tracks,
same boxes, same versions. The only difference: solid arrows now run
from D to exactly one box in each track. A small annotation on the
arrows themselves (not on the boxes) states "reference only — no new
facts added," directly illustrating the B/C information-equivalence
property both experiments' regime-equivalence checks enforced
mechanically.

**What it must get technically right:** the diagram must visibly reuse
the *same* boxes as Diagram 1 (ideally as a paired figure, side by side
or as a before/after), so a reader can see nothing was added except the
arrows — this is the single most important visual argument against the
"sales pitch for binding" reading (Section 6's whole purpose), so the
diagram should be captioned to note that these arrows are *one way* to
achieve this (F10-6's causal event would draw the same arrow shape,
labeled differently), not tied exclusively to a "binding record" box.

**Caption anchor:** "Same artifacts. Same versions. The only addition is
a relation — and any relation of this shape works, not only a
schema named 'binding' (see the negative control)."

### Diagram 3 — Temporal Failure (retroactive correction)

**Article placement:** Section 4 (failure mechanism 1).

**Content:** A timeline with three marked instants: t0 (decision made,
policy v1 consulted), t1 (a correction is recorded: "policy v1bis,
backdated to before t0"), t2 (an investigator queries "what was valid at
t0"). Show two query arrows from t2 back to t0 on the policy track: one
arrow labeled "query run before t1" landing on v1; a second arrow labeled
"the same query, run after t1" landing on v1bis. Both arrows are drawn as
equally "valid-time correct" — neither is styled as obviously wrong —
to make the point that the query's own logic did not change, only the
answer did.

**What it must get technically right:** must not show v1bis as if it
were simply an error to be corrected by better engineering — the diagram
should present it as a legitimate, ordinary correction (matching the
primary experiment's own framing: "on the theory that v1 was itself an
error," a real and common pattern in policy administration), so the
diagram argues the mechanism, not a strawman bug.

**Caption anchor:** "The query never changed. The record did. A
temporally correct query is not the same thing as a temporally accurate
one."

## What is deliberately not diagrammed

No diagram of an "understanding layer," no diagram generalizing beyond
decisions to system behavior broadly, and no diagram of
explainability/observability/governance as parallel or fragmented fields
— all Contribution 3 material, excluded per
`contribution-boundary-check.md`.
