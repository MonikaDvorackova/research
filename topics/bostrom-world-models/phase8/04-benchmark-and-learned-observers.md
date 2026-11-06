---
id: topic-bostrom-world-models-phase8-benchmark
title: "Minimal identifiability benchmark specification and learned-observer designs"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [benchmark, observers]
---

# ID-Bench-1: exact minimal benchmark (specification; the cases are already realised in `src/eid/phase8.py`)

## Principles
Ground truth is constructed explicitly, the observer sees only (actions, observations), and *the label set that is identifiable under the permitted information structure is computed by the experimenter from the exact law* (the "identifiability partition") and used only for scoring. An algorithm is never rewarded for guessing an unidentifiable label.

## Environments (all exact, finite)
- **F_M**: observed-state Markov environment (S = O = 3, identity emission, 3 actions) — the learner's class contains the truth. `markov_env`.
- **F_H**: episodic hidden-state POMDP (4 hidden, 3 obs, 3 actions; action 2 reveals) — outside the order-1 class, resets every T = 4 steps. `make_e0`.
- **F_R**: continuing hidden-regime process (slow hidden chain, no resets). `scripts/phase8_transient.py`.

## Cases (each with ground truth, observer information, and the identifiable label set)
| # | Case | Ground truth | Observer sees | Label set identifiable from the permitted data | Realised by |
|---|---|---|---|---|---|
| 1 | Additional data resolves uncertainty (A) | F_M, small n_train, unchanged kernel | (a, o) | {A}: stationarity holds; learning error ∝ 1/n | D2 S0, D3 |
| 2 | Truth outside learned class (B) | F_H with order-1/2 count class | (a, o) | {B} only with a richer comparator and n ≥ n\*; otherwise {A, B} | D3 |
| 3 | Observation distribution changes, no mechanism change (C) | F_M, policy shifts narrow → wide | (a, o) | {C or A}: conditional kernel stationary | D2 S1, D4a |
| 4 | Mechanism changes (D) | F_M, action-2 rows change at t₀ | (a, o) | {D} if action 2 reached; {A, C, D} if not | D2 S2 vs S3 |
| 5 | Two explanations indistinguishable | latent context shift ≡ mechanism change; stationary hidden regime ≡ random-time change | (a, o), single trajectory | **{C, D} (and B for F_R)**: abstention required | T4 exact check; D2b |
| 6 | Intervention makes 5 distinguishable | observed context c; or reset that redraws the regime; or play the revealing action | (a, o) + c / resets | {C} vs {D} (or {B} vs {D}) | S4/S5 vs D2b (reset); T4 (context) |
| 7 | Masking | F_H mechanism change not representable by the order-1 class | (a, o) | {A, B, D} for order-1; {D} for a richer class | D2 S6 |
| 8 | Negative control | split-state (bisimilar) variant; no action 2 | (a, o) | label undefined (TV = 0) | X1 H2 |

## Scoring (prevents rewarding guesses)
The observer outputs a *set* of labels (or ⊥ for "no inadequacy"). For each case the experimenter knows the consistent set K (cases above). Score = 1[true ∈ output] − (|output| − 1)/3. On cases with |K| > 1 the optimal output is exactly K (singleton guesses are correct with probability 1/|K|); an output smaller than K is penalised by expected coverage loss, an output larger by the size term. Calibration is scored separately (Brier/ECE on the set-membership probabilities) only on identifiable cells.

# Candidate learned-observer designs (staged; start small)
| Stage | Observer | Purpose | Added only if |
|---|---|---|---|
| O0 | Exact finite-state reference (X1 e-process) | upper bound for power; validity reference | – |
| O1 | Dirichlet count Markov learner, order 1 and 2 (exists) | tests T3/T4/T6 with closed-form likelihoods | – |
| O2 | Bayesian finite-state HMM learner (small S) with EM/variational | learned null with latent structure; tests T6d confidence-set denominator | O1 results require a latent class |
| O3 | Bootstrap ensemble of O1 | whether ensemble disagreement tracks epistemic gap or misspecification (not assumed) | O1 stage complete |
| O4 | GRU world model (exists from Phase 5) | whether T6 results transfer to a neural null | O1–O3 predictions hold or fail in a way an RNN could explain |
| O5 | Transformer sequence model | not planned | an unresolved question requires it |
Controls across stages: training volume, coverage, capacity, compute, calibration (temperature scaling), observation noise, seeds, and hyperparameters fixed *before* confirmatory seeds. Ensemble disagreement and predictive confidence are **not** treated as epistemic uncertainty or correctness; they are measured against the exact epistemic gap on F_M where it is computable.
