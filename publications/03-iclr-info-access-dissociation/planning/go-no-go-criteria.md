---
id: pub-03-c1-go-no-go-stopped
title: "Go / no-go — C1 (novelty stop)"
type: research-notes
status: stopped
created: 2026-07-31
updated: 2026-07-31
---

# Go / no-go — C1

## Pre-implementation gate (executed)

| Gate | Result |
|---|---|
| Novelty duplicate test | **FAIL — OCCUPIED** (Laban et al., ICLR 2026 Best Paper) |
| Cosmetic rename check | Fail (tool wrap / agent wrap) |
| C2 fallback under same bar | **OCCUPIED** (APB; execution-vs-planning literature) |

## Decision

**NO-GO.** Do not implement the C1 pilot. Do not draft a C1 manuscript.

## Hypothetical empirical thresholds (void — not authorized)

If C1 had been OPEN, continue/stop thresholds would have been:

**Continue only if:** sequential ≤ simultaneous −15 pp after length matching; gap across ≥2 families; RECAP does not close to within 5 pp; effect scales with required fact integration; failures not mostly parse/format.

**Stop if:** gap <5 pp; disappears under padding; RECAP closes to within 5 pp; weak-model-only; format/parse dominates; near-duplicate paper found.

The last stop condition triggered **before** any experiment.

## Next programme action

Return to blank-slate ICLR topic search with explicit exclusions:

- Lost-in-Conversation renames / shard-vs-concat variants
- Plan-vs-execute / APB-style planning diagnostics as sole claim
- Closed CR-Gap / memory / revision-aware topics
