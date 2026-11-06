---
id: topic-bostrom-world-models-phase10-dev
title: "Phase 10 development results (exploratory; includes negative findings)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [development, results, negative]
---

# Development results (namespace 10000; all exploratory)
Artifacts: `results/phase10_dev/` (`certified_runs.jsonl`, `certified_summary.md`, `kscaling.md`, `comp_adaptive.md`, `em_runs.jsonl`, `em_summary.md`, `exact_checks.md`, `stats_audit.md`, `design_inputs.md`, `determinism_check.txt`, registries). Tests: 299 pass in total (`tests/test_{certified_null,e6proc,e6streams,e6gen,phase9_audit}.py` extended). Determinism: 7 certified jobs and 2 EM jobs re-executed identically (one apparent EM mismatch was a tuple-vs-list comparison artefact, documented in `determinism_check.txt`).

## 1. Certified learned null (60 independent Markov structures)
See `04-…` for coverage (0/300), optional-stopping contrast (CP 468/1000 vs LR 32/1000), type-I 0/7200, adversary 0/300. **Frozen point null** (a test of the simple null "kernel = estimate"): rejects the *unchanged* kernel in **1335/1800 (74 %)** runs with narrow training on 10³ episodes, 1/1800 narrow/10⁴, 0/1800 uniform — correct rejections of its own false null; mistaken for "change" they are false attributions of an epistemic gap (Phase 9 semantics).
**Power and price** (change in action-2 rows; post-change stream of 3000 episodes; checkpoints every 25 episodes; oracle delay is at the first checkpoint in most runs, so ratios involving the oracle are floored):
| training policy | training episodes | certified detected | median delay oracle / certified (episodes) | median observed ratio | median predicted exponent ratio | mean retained exponent ρ̄ |
|---|---|---|---|---|---|---|
| narrow | 10³ | 107/480 | 25 / >3000 (censored) | >60 | 1649 | 0.010 |
| narrow | 10⁴ | 462/480 | 25 / 225 | 5.50 | 4.09 | 0.240 |
| uniform | 10³ | 479/480 | 25 / 125 | 2.92 | 2.40 | 0.395 |
| uniform | 10⁴ | 480/480 | 25 / 50 | 1.42 | 1.38 | 0.691 |
The exact exponent ratio predicts the observed delay inflation to within the spread across structures (mean log(observed/predicted) −0.05 for uniform/10⁴, +0.13, +0.19); the run-level Spearman correlation across all 480 runs is only 0.16 (delays are quantised to checkpoints, oracle delays floored). **Coverage vs size:** narrow coverage at 10³ training episodes leaves action-2 contexts essentially unseen: price → ∞ (T3a).

## 2. Why did the robust procedures have zero detections at N = 3000?
| Candidate cause | Evidence | Verdict |
|---|---|---|
| Genuine information-theoretic barrier | the exponent of a saturated change-detection null equals the oracle exponent (Π_exp = 0); no lower bound forbids detection (Prop T1) | **no** (no impossibility proved) |
| Excessively broad null → regret | evidence needed ≈ **10.4 nats per null cell** (K = 8, 16, 32; K = 64, 128 undetected in 12 000 observations); the episode-level model has 2160 free cells: extrapolated ≈ 2×10⁴ nats ≈ **2×10⁶ episodes** at 0.01 nats/episode vs N = 3000 | **yes, for E_ep** (extrapolated beyond the measured range) |
| Poorly chosen statistic / numerical conservatism | the Phase 9 predictive-comparison test used a worst-case sub-Gaussian proxy (σ = 2, boundary ≈ 667 at 12 000 observations) while conditional ranges R_t ≈ 0.08–0.2; the **predictable-range** boundary (`04` of Phase 9 + `e6proc`) gives: M3 **30/30** (was 0/30), H3 **12/30** (was 0/30), R1 **16/30** (was 0/30), with **0/30** in every null-true cell (M1, M2, M4, H1, H4, H5) | **yes, for E_comp** |
| Insufficient intervention coverage | M4/H4 (changed action never played): unobservable by exact equivalence, 0/30 as required | not the cause for played changes |
| Implementation defect | cross-checks (generic vs Phase 8 implementation; Robbins boundary MC 0/300; adaptive-range MC 0/300) | none found |
| Insufficient horizon | N = 3000 vs ≈ 2×10⁶ needed for E_ep | **yes, for E_ep** |
**Conclusion.** The zero detections were **not** an impossibility. E_ep: regret-dominated (breadth). E_comp: a conservative boundary; a predictable-range boundary restores power while keeping 0/30 under null-true scenarios (30 runs per cell cannot certify a bound; the MC validity test with dependent noise and predictable ranges gave 0/300). On hidden-state change (H3) the assumption-free predictive test (12/30) detected more than the restricted-kernel test did in Phase 9 (5/30); on the persistent regime (R1) 16/30 vs 8/30. (Different seeds and namespaces; not a paired comparison.)
**Caveat.** The predictable-range boundary is my derivation (Hoeffding's lemma with a predictable range + Robbins mixture). It is not in the Choe–Ramdas text read; its proof is short and its validity is checked by Monte Carlo only.

## 3. K-scaling (iid categorical; KL = 0.1 nats/obs; pre-change law unknown; 12 runs per K)
| K | detected within 12 000 | median delay (obs) | evidence needed (nats) |
|---|---|---|---|
| 2 | 12/12 | 170 | 17 |
| 4 | 12/12 | 300 | 30 |
| 8 | 12/12 | 480 | 48 |
| 16 | 12/12 | 1220 | 122 |
| 32 | 12/12 | 2950 | 295 |
| 64 | 1/12 | >12 000 (censored) | >1200 |
| 128 | 0/12 | >12 000 | >1200 |
Linear in K with ≈ 10 nats per cell over the detected range.

## 4. Approximate EM, positive and negative controls, dependence
See `05-…`, `exact_checks.md`, `08-…`. Negative controls: bisimilar twin (TV = 0, Phase 9), changes at zero-reach contexts (T3a), correct nulls (type-I). Positive controls: engineered kernel changes with exact exponents; iid change with known KL (K-scaling).
## 5. Negative / inconclusive findings kept
(i) Phase 9's zero power (now explained) — E_comp still has no power under the order-2 comparator (0/30 everywhere). (ii) Type-I of the certified test is 0 everywhere, so calibration cannot be distinguished from conservatism; the e-process does not exploit its allowance (guarantee 0.10, observed 0). (iii) The EM e-process failure appears only with 1-start optimisers. (iv) K = 64, 128 not detected: the slope is measured on K ≤ 32; the extrapolation is indicative only. (v) The predicted-vs-observed exponent ratio correlates weakly at run level (0.16).
