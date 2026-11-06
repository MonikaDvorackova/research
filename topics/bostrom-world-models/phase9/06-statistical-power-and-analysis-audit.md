---
id: topic-bostrom-world-models-phase9-stats
title: "Statistical power and analysis audit of the E6 plan (with corrected calculations)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [statistics, power, audit]
---

# Statistical audit (executable: `src/eid/phase9_audit.py`, `scripts/phase9_dev_audit.py`, `tests/test_phase9_audit.py`)

## 1. Problems found in the Phase 8 plan and corrections
| Issue | Finding | Correction |
|---|---|---|
| 0.05 versus 0.07 | "CP upper bound ≤ 0.07" demonstrates *rate ≤ 0.07*, not *rate ≤ α = 0.05*. It is a non-inferiority margin of 0.02, not the nominal level. | State the claim as "type-I ≤ 0.07 demonstrated" or require ≤ 0.05; never call it "controlled at 0.05" from this criterion. Theory (Props A–D) gives ≤ 0.05; the experiment checks the implementation, not the theorem. |
| Certifying zero rejections | Zero rejections certify rate ≤ 0.07 at one-sided 95 % only with **n ≥ 42** runs, ≤ 0.05 with **n ≥ 59**. 20 runs per structure give a bound of **0.139**. | Per-structure claims need R ≥ 60 runs per structure; pooled claims over structures need clustering-aware bounds. |
| Power of the claim | n = 600 pooled runs, true rate 0.02: P(certify ≤ 0.07) > 0.999, P(certify ≤ 0.05) = 0.989 (unadjusted) / 0.847 (Bonferroni 0.05/24). True rate 0.05: P(certify ≤ 0.07) = 0.62 (0.15 Bonferroni); P(certify ≤ 0.05) = 0.03. | A conservative procedure with true rate ≈ 0.02 (as in X1) passes; a procedure at exactly 0.05 cannot be certified at ≤ 0.05 with realistic n. State that. |
| Multiplicity | X1 re-evaluated: 24 cells; max per-cell UB 0.0442; **max UB at Bonferroni level 0.05/24 = 0.0558**. So "simultaneously ≤ 0.07" holds with FWER 5 %; "simultaneously ≤ 0.05" is **not** demonstrated. | Report both; for E6 define families of claims and adjust within a family (Holm). |
| Demonstrating a violation vs failing to detect one | Power to refute: pooled n = 600, true rate 0.10: P(CP lower bound > 0.05) = **0.998**; true rate 0.07: **0.648**. | A violation of size ≥ 0.07 is detected with probability ≥ 0.65 at n = 600; "no violation found" must not be read as validity below that size. |
| Clustering | Coverage of 95 % upper bounds for a boundary mean 0.05, 30 structures × 20 runs: pooled CP **0.97 / 0.92 / 0.81 / 0.63** at ICC 0 / 0.05 / 0.2 / 0.5; cluster bootstrap 0.95 / 0.92 / 0.89 / 0.77; cluster t-bound 0.95 / 0.92 / 0.88 / 0.75. | Pooled CP is anticonservative under ICC > 0. Even cluster-level intervals undercover (≈ 0.85–0.93) for skewed binary outcomes with R = 20. |
| Number of structures | At ICC 0.2, boundary rate 0.05, R = 20: coverage (pooled / bootstrap / t) = 0.76/0.86/0.85 (m = 30), 0.80/0.93/0.91 (60), 0.73/0.90/0.88 (120), 0.79/0.92/0.92 (240) (300 replicates; s.e. ≈ 0.012–0.025). | **More structures alone do not repair coverage; more runs per structure and a margin do.** Use margin-based decisions (claim ≤ 0.07 only if the cluster bound ≤ 0.05) or beta-binomial/simulation-calibrated bounds. |
| Units | The primary independent units are **independently generated structures**; runs are nested replicates. The Phase 7 "30 seeds" were jitters of one structure (one structure in effect). | E6′ uses ≥ 60 structures per family (dev: 10), R ≥ 60 runs, family-level claims. |
| Sample-size claims in Phase 8 SAP ("±0.02") | Valid for pooled i.i.d. runs only. | Replaced by the table above. |

## 2. Corrected plan (applies to any confirmatory E6′)
1. **Units/replication.** m ≥ 60 independently generated structures per family; R ≥ 60 runs per (structure, procedure, scenario).
2. **Type-I claims (null-true cells only).** Decision: "no violation" if the cluster-level 95 % upper bound ≤ 0.05; "bounded by 0.07" if ≤ 0.07; "violation" if the cluster-level 95 % lower bound > 0.05. Report ICC and the design effect; if the design effect > 1.2, use a beta-binomial or simulation-calibrated bound.
3. **Multiplicity.** Families: (procedure × family) pairs. Holm within each family of claims; separate reporting across hypotheses; no composite success rule.
4. **Power claims.** Detection probability within budget (primary) and restricted mean time with censoring (secondary), each normalised to the Chernoff-optimal exponent (efficiency = observed exponent / optimal exponent).
5. **Formal-null flag.** Every cell carries the experimenter-side flags (null true; mechanism changed). Rejections in cells with null false are **not** counted as type-I errors; they enter H-C as false-attribution events if the mechanism is unchanged.
6. **Dev/confirmatory separation.** Dev structure indices ≥ 9000 namespace (this phase) and 700–719 (reserved dev); confirmatory 800–829 reserved and to be extended (≥ 60 per family) in the preregistration; no threshold changes after outcomes.
7. **Integrity.** Hash manifest of raw runs before analysis; preregistration commit before the run; run once; determinism test on a stored sample (done in dev: 30/30 stored runs reproduced exactly).

## 3. Dev-phase observation about the same issues
Dev null-true cells: 0/30 rejections in each; with 30 runs the upper bound is 0.095, so the dev run **cannot certify** any bound ≤ 0.07 (consistent with the table). It checks that no procedure fails grossly.
