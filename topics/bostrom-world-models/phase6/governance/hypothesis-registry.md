---
id: topic-bostrom-world-models-hypothesis-registry
title: "Hypothesis registry"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance, hypotheses]
---

# Hypothesis registry
Status values: supported (C), rejected, unresolved, proposed.
| ID | Hypothesis | Origin | Status | Evidence |
|---|---|---|---|---|
| H-P5-1…8 (env 1) | Eight directional claims on Bayesian observers (oracle vs learned, design, calibration) | `preregistration-phase5.md` | supported (8/8) | `results/bayes1_confirm` |
| H-P5-1…8 (env 2) | Same for POMDP | same | supported (8/8) | `results/bayes2_confirm` |
| E-1…3 (env 1) | Equivalence claims | same | 2 established, **E3b not established (run A)** | `results/compare_runs_bayes1.md` |
| E-1…3 (env 2) | Equivalence claims | same | 3/3 established | `results/bayes2_confirm` |
| H-conj-1 | Catch-all makes myopic EIG explore | Phase 5 conjecture | **rejected** (exact DP) | `test_proposition10_exact.py` |
| H-expl-1 | Information-gain ratio separates misspecified observers | exploratory | **not replicated** (env 2) | `results-phase5.md` |
| H-cov | Learned-observer failure is determined by training coverage, for all learner families | Phase 5 stress tests (X) | unresolved; to be tested in X3 | – |
| H-X1-1…6 | Criticism design / validity / barrier / P10 prediction | Phase 6 proposal | proposed (not frozen) | `phase6/08-next-experiment-prereg.md` |
| H-A | A tight frontier statement beyond Prop. 3 exists | Phase 6 | proposed (T1) | `results/phase6/prediction_vs_identification.txt` (seed only) |

## Phase 7 (X1, confirmatory, seeds 600–629; prereg commit 02bad01)
| ID | Hypothesis | Status | Evidence |
|---|---|---|---|
| H-X1-1 (H1) | Type-I ≤ α for all policies | **supported** (1.69 %) | `results/x1_confirm/analysis.md` |
| H-X1-2 (H2) | Barrier without action 2 | **supported** | same |
| H-X1-3 (H3) | Random wide power ≥ 0.8 within 1500 (anticipated) | **supported** (1.000) | same |
| H-X1-4a (H4a) | P4 ≥ 1.5× faster than random, anticipated | **supported** (2.01/1.74/1.85) | same |
| H-X1-4b (H4b) | same, unanticipated | **rejected** (1.24, 1.02) | same |
| H-X1-4c (H4c) | P4 ≥ 1.5× faster than P5 (equal information) | **rejected** (1.13/0.87/0.88) | same |
| H-X1-5 (H5) | P3 not faster than random | **inconclusive by rule** (pc0 +1.44×; pc1/pc2 −6–8×) | same |
| H-cov | learned-observer failure is coverage-determined for all learners | unresolved → X3 | – |
| H-X4 | A valid learned-null class-adequacy test retains useful power | proposed | `phase7/08-…` |
