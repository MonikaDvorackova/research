---
id: topic-bostrom-world-models-phase10-em
title: "Approximate EM and numerical validity: systematic study"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [EM, optimiser, validity]
---

# Approximate EM maximisers (`scripts/phase10_em.py`, `results/phase10_dev/em_summary.md`)

Design. 40 independent small hidden-state POMDPs (S ∈ {2, 3}, A = O = 3, T = 4; generator `gen_hmm_small`, namespace 10000, separate streams for environment/training/evaluation), 800 uniform-action episodes. Reference: best of 20 restarts × 1000 iterations (and the true parameters). **Exact finite-state optimisation is not available for latent-variable nulls; "reference" is a many-restart proxy, not a certificate.** A fit is an **invalid denominator** if its log-likelihood is below that at the true parameters by > 0.5 nats.

## 1. Optimiser gap (fraction of the 40 structures with an invalid denominator; median shortfall vs true parameters)
| restarts | iteration budget | tolerance | invalid fraction | median shortfall (nats) | seconds |
|---|---|---|---|---|---|
| 1 | 20 | 10⁻⁶ | 0.82 | 13.9 | 0.01 |
| 1 | 60 | 10⁻⁶ | 0.35 | −1.4 | 0.04 |
| 1 | 300 | 10⁻⁶ | 0.07 | −6.1 | 0.20 |
| 1 | 1000 | 10⁻⁶ | 0.03 | −7.6 | 0.37 |
| 5 | 20 | 10⁻⁶ | 0.62 | 2.3 | 0.07 |
| 5 | 60 | 10⁻⁶ | 0.07 | −4.1 | 0.20 |
| 5 | 300 | 10⁻⁶ | 0.00 | −7.4 | 0.98 |
| 5 | 300 | **10⁻³** | **0.62** | 1.8 | 0.05 |
| 5 | 1000 | 10⁻⁶ | 0.00 | −8.0 | 1.78 |
| 5 | 1000 | **10⁻³** | **0.55** | 0.9 | 0.05 |
| 20 | 20 | 10⁻⁶ | 0.30 | −1.4 | 0.28 |
| 20 | 60 | 10⁻⁶ | 0.03 | −5.2 | 0.80 |
| 20 | 300 / 1000 | 10⁻⁶ | 0.00 | −7.6 / −8.1 | 3.7 / 7.5 |
A negative shortfall means the fit exceeds the true-parameter likelihood (the maximum-likelihood fit over-fits by ≈ 8 nats, as expected). **A loose convergence tolerance (10⁻³ per episode) leaves 55–62 % invalid denominators even with 1000 iterations** — early stopping, not the iteration cap, is the dominant failure; this is a property of the optimiser's stopping rule, not of the statistical framework.

## 2. Effect on the sequential statistic (truth in the class, S known; 40 structures × 3 data sets; blocks of 100, 100, 200, 400 episodes, checkpoints after each block)
Numerator: predictable plug-in (first block under a uniform model; block k under an EM fit (5 × 300) on blocks < k). Denominator: EM fit at each checkpoint.
| denominator | type-I with the plug-in numerator (median deficit −115 nats) | with a **good fixed alternative** (true parameters mixed 10 % with random rows; median deficit −17 nats) |
|---|---|---|
| true parameters (oracle, valid) | 0/120 | 0/120 |
| 5 restarts × 300 it. | 0/120 | 0/120 |
| 10 restarts × 600 it. | 0/120 | 0/120 |
| 1 restart × 60 it. | 0/120 | **18/120 (15 %; lower 95 % bound 0.099 > 0.05)**; 10/40 structures |
| 1 restart × 20 it. | 5/120 (4/40 structures) | **53/120 (44 %; LB 0.365)**; 27/40 structures |
**Mechanism (exact decomposition).** log E = (ll_num − ll_true) + (ll_true − ll_den) = (numerator deficit ≤ 0 on average, the price of learning the alternative) + (optimisation shortfall). A rejection requires the shortfall to exceed the deficit by ln 20 = 3.0 nats. A weak alternative provides a cushion (−115 nats) that hides the invalidity; a **good** alternative (deficit −17 nats) removes the cushion. So **the type-I inflation is largest precisely for the procedures that would have the most power**, and only the symmetric/strong optimisers (≥ 5 starts, ≥ 300 iterations, tolerance 10⁻⁶) kept 0/120 here — an empirical observation, not a guarantee (no certificate, 120 runs).
## 3. Verdict
- *Optimiser failure vs framework failure.* The e-process framework is valid for any denominator ≥ the true null likelihood; EM fails that condition when under-converged. The failure is the optimiser's, and it is invisible in the algorithm's output (no certificate).
- The correct-null calibration of the symmetric configurations does **not** establish validity: 0/120 has upper bound 0.025 pooled, no clustering-aware bound is available because there were no events (ICC undefined).
- Cost: 0.01–7.5 s per fit (800 episodes); the safe configurations cost 100–1000× the unsafe ones.
- A non-certified likelihood supremum must not be used as a denominator without an independent safeguard; certification for latent nulls is an open obligation (T5).
