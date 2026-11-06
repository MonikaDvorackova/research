---
id: topic-bostrom-world-models-phase10-stats
title: "Statistical power and dependence audit; proposed confirmatory design (not executed)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [statistics, ICC, power, design]
---

# Statistical audit (`scripts/phase10_stats.py`, `results/phase10_dev/stats_audit.md`, `design_inputs.md`)
Primary experimental units: **independently generated structures** (60 Markov structures, 40 small HMMs); runs are nested replicates.

## 1. Intra-structure dependence (measured)
| outcome | runs/structure | mean | ICC (ANOVA) | design effect |
|---|---|---|---|---|
| frozen-null rejection, narrow/10³ (74 %) | 30 | 0.742 | 0.007 | 1.2 |
| frozen-null rejection, narrow/10⁴ | 30 | 0.0006 | 0.000 | 1.0 |
| **certified rejection (type-I)** — all conditions | 30 | 0.000 | **undefined (no events)** | – |
| log(certified delay / oracle delay), uniform/10⁴ | 8 | 0.344 | **0.37** | 3.6 |
| log(certified/oracle), uniform/10³ | 8 | 1.108 | **0.65** | 5.6 |
| log(certified/oracle), narrow/10⁴ | 8 | 1.705 | **0.79** | 6.5 |
| detection by the predictable-range comparison test, H3 (hidden-state change) | 3 | 12/30 | **1.00** | – |
| same, R1 (persistent regime) | 3 | 16/30 | 0.75 | – |
Reading: (a) when an outcome is determined by structure (power, detection) the structure is the effective unit and repeated runs add little (m = 30 → 26 structures when R goes 8 → 30). (b) Type-I ICC cannot be estimated for a conservative procedure with no events; dependence for type-I claims must be handled by design (cluster-aware bounds) rather than by an estimated ICC.

## 2. Interval coverage (60 structures × 60 runs, 300 simulated datasets; one-sided 95 % upper bounds)
| true mean | ICC | pooled CP | cluster t | cluster bootstrap | design-effect-adjusted CP |
|---|---|---|---|---|---|
| 0.05 | 0 | 0.973 | 0.970 | 0.967 | 0.973 |
| 0.05 | 0.05 | 0.773 | 0.927 | 0.923 | 0.947 |
| 0.05 | 0.2 | 0.673 | 0.880 | 0.870 | 0.927 |
| 0.05 | 0.5 | 0.637 | 0.870 | 0.887 | 0.933 |
| 0.02 | 0 | 0.963 | 0.937 | 0.940 | 0.967 |
| 0.02 | 0.05 | 0.833 | 0.913 | 0.923 | 0.933 |
| 0.02 | 0.2 | 0.683 | 0.833 | 0.843 | 0.913 |
| 0.02 | 0.5 | 0.550 | 0.770 | 0.783 | 0.843 |
Pooled CP is badly anticonservative with any clustering; the design-effect-adjusted CP is best (0.84–0.97) but still below 0.95 when the ICC is large and the rate is low. **No interval method is nominal everywhere**; claims near the boundary need simulation-calibrated bounds or a margin. (300 replicates: s.e. ≈ 0.013.)

## 3. Sample sizes from measured variability
| claim | quantity | unit-level SD | structures needed |
|---|---|---|---|
| retained exponent ρ̄ (exact), ±0.05 | uniform/10⁴ | 0.116 | **21** (±0.02: 129) |
| | uniform/10³ | 0.103 | 17 (±0.02: 103) |
| | narrow/10⁴ | 0.094 | 14 (±0.02: 85) |
| agreement of observed delay inflation with the exact prediction, ±10 % | uniform/10⁴ | 0.381 | **62** |
| | uniform/10³ | 0.556 | 131 |
| | narrow/10⁴ | 0.607 | 156 |
| log delay ratio certified/oracle, ±10 % (R = 8) | uniform/10⁴ | between 0.24, within 0.32 | 30 (R = 30: 26) |
| | uniform/10³ | 0.53 / 0.39 | 128 |
| | narrow/10⁴ | 0.75 / 0.39 | 246 |
| proportion of hidden-state structures where the comparison test detects a change, half-width 0.1 at p ≈ 0.4 (ICC ≈ 1 → structures are the unit) | – | – | ≈ **93** (= 1.96²·0.24/0.01) |
| type-I of the certified test, "no violation, upper bound ≤ 0.05" | zero events | – | m = 60 structures × R = 60: pooled UB 0.0008; even with design effect 6.5 the effective n ≈ 550 gives UB 0.0054 |

## 4. Proposed confirmatory design (NOT executed; contingent on `11-…`)
- **Calibration checks** (type-I of certified/robust procedures): m ≥ 60 structures per family, R ≥ 60 runs; claim "no violation" if the cluster-level one-sided 95 % upper bound ≤ 0.05; a violation if the cluster lower bound > 0.05. No arbitrary relaxed threshold: the criterion is the nominal 0.05 (plus δ for the certified procedure, stated). Because the procedures are conservative, this is achievable; it checks the implementation, not the theorem.
- **Exploratory effect estimation** (retained exponent, delay ratios): unit = structure; report the between-structure SD and ICC; no hypothesis test.
- **Confirmatory hypotheses** (see `11-…`): H1 exact-price formula predicts delay inflation within ±30 % in the median (m ≥ 130 structures for ±10 % precision); H2 optimiser-asymmetry dose–response (monotone in shortfall/deficit; ≥ 60 structures × 3 data sets); H3 predictable-range comparison test detects more than the restricted-kernel test on hidden-state change by ≥ 1.5× in detection probability, paired by structure (≥ 93 structures).
- **Equivalence/non-inferiority.** Not claimed anywhere: a failure to reject is never read as equivalence; equivalence margins would have to be derived from theory, and none is needed.
- **Pseudo-replication guard.** All tests use the structure as unit; runs within a structure are averaged first.
