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
