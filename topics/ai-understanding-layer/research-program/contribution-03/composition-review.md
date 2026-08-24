---
id: note-contribution-03-composition-review
title: "Contribution 3 — Composition Effect Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, composition, emergent-behavior, bisimulation]
refs: [operationalization-review.md, generalization-from-c2.md]
---

## The question

> Even if every component has its own mature mechanism (model →
> interpretability, pipeline → observability, data → lineage, decision →
> provenance, policy → auditability, runtime → verification), does
> composition create a residual problem — can every component be locally
> inspectable while the composed decision system remains globally
> difficult to reconstruct, predict, or assure?

## Compositional verification confirms the effect — for predictability, not yet for reconstructability

"A crucial issue in autonomous systems design assurance is the notion of
emergent behavior; we cannot use their parts in isolation to examine
their overall behavior or performance" [S37]. Compositional verification
techniques exist specifically to combat this by structure-preserving
model transformation, but even so, "making emergent global behaviors
predictable remains a challenging open problem" for collective/adaptive
systems-of-systems [S37][S38]. This is a real, current, formally-
grounded confirmation that **local inspectability does not, in general,
guarantee global predictability** — a genuine composition effect,
directly evidenced.

**Scope limit, stated precisely:** every source found in this search
addresses **behavioral prediction/verification** (Level 5: what can the
system do), not **historical reconstruction** (Level 4: what did this
specific decision use). The composition effect is well-evidenced for
predictability; it is not directly tested, in any source found here, for
reconstructability specifically. This is an important distinction this
review does not blur.

## The projection model, formalized correctly via bisimulation

Section 16's candidate model (each mechanism preserves a projection
P_i(system history); ask when the original property is recoverable from
the P_i's jointly) has an exact, pre-existing formalization: **bisimulation
and observational equivalence**. Two system trajectories are
observationally equivalent (bisimilar under the observer's abstraction)
when no available sequence of observations can distinguish them —
"observation equivalence can be characterized in terms of abstraction
homomorphisms that preserve successors" [S39], and this machinery has
been extended explicitly to partially observable settings (POMDPs;
Castro's exact bisimulation; Dean and Givan's homogeneous partitions)
[S40].

**Direct, precise connection to Contribution 2:** the follow-up
experiment's AMBIGUOUS cases are, exactly, a demonstration that two
distinct ground-truth histories (policy version v1 vs. v2 applying) are
**observationally equivalent under the retained projection** (the
truncated timestamp) — the retained record cannot distinguish them, in
exactly bisimulation's own technical sense. This is a legitimate,
citable, precise formal connection this review recommends recording
directly, not a new theoretical result — Contribution 2's own
AMBIGUOUS/CORRECT_UNIQUE distinction is a specific instance of the
general "when do two projections collapse into observational
equivalence" question bisimulation theory already studies.

## Verdict on the composition effect

**SUPPORTED, for behavioral predictability specifically** (compositional-
verification/emergent-behavior literature is direct and current).
**PLAUSIBLE, not yet SUPPORTED, for reconstructability specifically** —
no source found in this review tests whether per-decision consumption-
relation guarantees (Contribution 2's object) compose into per-
trajectory or per-system reconstruction guarantees; the bisimulation
connection gives the right *formal vocabulary* to eventually test this,
but does not itself supply the answer. **This is exactly the open,
precise, well-scoped question `generalization-from-c2.md` isolates as
the highest defensible generalization frontier from Contribution 2 (G2),
and it is the single strongest candidate for a genuine, narrow Article 3
research-agenda contribution** — see `article-03-options.md`.
