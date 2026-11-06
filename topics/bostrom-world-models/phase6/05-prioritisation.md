---
id: topic-bostrom-world-models-phase6-priorities
title: "Prioritisation of experimental directions"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [prioritisation]
---

# Prioritisation

Qualitative scores (H/M/L). Higher is better except "risk of trivial or known" (lower is better). Justifications are my judgement from the scan in `03`; they are not probabilities.

| Cand. | Originality | Philosophical significance | Math tractability | Discriminates explanations | Feasibility | Reproducibility | Risk trivial/known | Unexpected-finding potential | Interdisciplinary value |
|---|---|---|---|---|---|---|---|---|---|
| X1 criticism & design | M | H (can an embedded agent know its model is inadequate) | H (exact) | H | H | H | M–H (Gelman–Shalizi, universal inference) | M–H | H |
| X2 prediction–identification frontier | L–M | H | H | M | H | H | H (data-processing) | L–M | M |
| X3 learner/env generalisation | L–M (replication/extension) | M | L | H (tests an alternative explanation) | H | M | M | M | M |
| X4 expansion/discovery | M | H | M | M | M | M | M | M | H |
| X5 observer-effect POMDP | L–M | M | H | L | H | H | H (likely reducible) | L | L |
| X6 computational | L | M | H | L | H | H | H | L | L |
| X7 nested | unknown | H | none | none | none | – | unknown | – | – |

## Selected three
1. **X1** — exact, mathematically tractable, has the best chance of a result that is more than a restatement, directly addresses "can the agent discover that its hypothesis space is inadequate". Prerequisite for X4.
2. **X3** — the required generalisation test: our central empirical claim currently rests on two environments and two learner families, and an alternative explanation (architecture artefact) is untested. A negative result (failure under full coverage) would be informative and would change the story.
3. **X2** — theory/exact work to settle Direction A honestly: either a tight frontier statement exists or the direction collapses into Prop. 3. Cheap, decisive about whether "prediction ≠ identification" is a result or a restatement.

## Deferred / rejected
- X4: valuable but depends on X1; defer until Gate G2.
- X5: likely reducible to a larger POMDP; do only as a short proof attempt inside X2/X1 writing.
- X6: standard cryptography; mention in the map, do not run.
- X7: no formal mechanism; reject until one exists. The brief requires a mechanism and a discriminating experiment first.
