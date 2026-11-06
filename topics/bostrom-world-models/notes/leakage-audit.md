---
id: topic-bostrom-world-models-leakage-audit
title: "Information-leakage and coupling audit"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [audit, reproducibility]
---

## Information-leakage and coupling audit

Scope: `implementations/epistemic-identifiability` at the Phase 4 state. Each row names the risk, what was checked, and the test or result that enforces it. "Experimenter-side" means the quantity is computed for evaluation only and never reaches the agent.

| # | Risk | Check | Outcome |
|---|---|---|---|
| 1 | Shared random-number streams between roles (theory data, W data, test episodes, calibration episodes, adaptation episodes, controls) | Every `(tag, extra)` pair used by the pipeline maps to a `SeedSequence([seed, tag, extra])`. `tests/test_independence.py::test_all_random_streams_are_distinct` draws from all 357 identifiers for two seeds and asserts that no two produce the same numbers. Torch seeds: theory members `100s + k`, W `100s + 50 + q`, fine-tuning `1000s + 7·id + k` (distinct for distinct arguments). | **No collisions.** An earlier collision (stream indices overlapping across policies when the control AltOOD was first added) was found in Phase 2, fixed by giving AltOOD its own tags, and the run repeated; v2 then reproduced v1 exactly in all shared columns. |
| 2 | Agent theory and world model trained on overlapping data | `test_agent_theory_and_world_model_training_data_are_disjoint`: no identical rows between the theory's data and W's data, none between the two theory samples, and no correlated sample path. | **Disjoint.** Both are drawn from E0 (by design), from separate streams. |
| 3 | Agent access to anything beyond `env.step` (label, parameters, noise seed, W's weights) | `test_agent_only_uses_step`: an environment stub that raises on any attribute other than `step`; all three policies run to completion. | **Interface-only.** Oracle log-likelihood ratios, KL values, AltOOD matching and the quality metrics are computed in `run.py` after interaction and are never passed to the agent. |
| 4 | Coupling between W and the negative-control statistics | Structural: false-positive rates are computed from E0 and E0split episodes and the theory alone. Empirical: the FPR rows of "W = ReLU, theory tanh" equal the baseline's exactly, and those of "W = ReLU, theory ReLU" equal the ReLU-theory condition's exactly (they must, if W is not coupled). | **No coupling observed.** |
| 5 | The negative control exploited through an implementation artifact | AUROC between E0 and E0split (identical law, different noise mechanism): seed-averaged range 0.482–0.513 across all nine conditions and all cells; `test_negative_control_has_identical_law` (KS test and variance). | **Not exploited.** |
| 6 | Adaptation, calibration and test episodes overlapping | Adaptation uses tag `adapt`; calibration `cal` / `alto_cal`; test `eval` / `alto_eval`; all distinct (row 1). Adaptation data are used only to fine-tune the theory; test statistics are computed on separate fresh episodes. | **Disjoint.** |
| 7 | Experimenter-side label use that could be mistaken for agent-side performance | Platt scaling (ECE, Brier) is fitted on labelled calibration episodes and can learn a negative slope; in inverted cells it reports excellent calibration. AUROC, TPR, FPR are label-free for the agent (the α-test threshold is computed from the theory, not from labels). | **Disclosed.** ECE and Brier are reported only as experimenter-side measures and are not used for any claim where AUROC is below 0.5. |
| 8 | Information channel in the analytic-theory condition | The actions of the active policy there are chosen by a separately trained learned ensemble (disagreement); the test uses the analytic theory. The selector knows E0-trained structure, not W. | **No access to W.** Disclosed in the condition description. |
| 9 | Adaptive observer using reference information | Its replay buffer is its own earlier reference data (E0, in-distribution), i.e. prior experience. New information comes only from interaction with the environment under test. | **Legitimate prior experience.** |
| 10 | Pairing and independence across conditions | Conditions share seeds; W is identical across conditions that do not change W (checked: `quality.csv` identical). Comparisons across conditions therefore use seed-paired statistics; across seeds the replicates are independent (distinct streams). Conditions that change W's architecture are paired by seed index only. | **Handled by paired design; disclosed.** |
| 11 | Reproducibility | `scripts/reproduce_check.py` re-ran seed 0 of all nine stored conditions at full configuration: 72 rows each, 0 mismatches (tolerance 1e-9). A golden-output test shows that the ablation refactor left the default path bit-identical. | **Reproduces.** |

Residual risks not eliminated: a single machine and one library version were used (determinism across hardware and PyTorch versions is not claimed); the 10 seeds share code and environment family, so they do not guard against a systematic design error common to all conditions.

## Phase 5 additions (Bayesian observers, partially observed environment)

| # | Risk | Check | Outcome |
|---|---|---|---|
| 12 | The Bayesian observer reading the true environment's identity, parameters or weights | `tests/test_bayes1.py::test_observer_uses_only_env_step` and `tests/test_bayes2.py::test_observer_uses_only_the_observation_interface` run every policy (including EIG and two-step EIG) against environment stubs that raise on any attribute other than `step`/`reset`. The EIG computation uses only the observer's own members and posterior. | **Interface-only.** |
| 13 | The oracle regime leaking into the learned regimes | The oracle space is built from the true kernels (`ExactRef`, `W_true`, `gamma_star`, `delta_star` in environment 1; the exact POMDPs and the true GRU in environment 2). The learned and bma spaces are built only from `ctx["Q"]` and `ctx["Wp"]` (networks trained on independent samples) and fixed parameter grids. `gamma_star` and `delta_star` are not used by those regimes; the grids do not contain them. | **Separated by construction;** the grids (fixed before any run) bracket the truth without containing it. |
| 14 | Observer materials sharing data or random streams with the true world model | Separate stream families (`q`, `w2`, `wp` for the observer; `w` and `train` for the truth); `test_phase5_streams_are_distinct`, `test_independent_random_streams_for_observer_materials`; disjointness of training data already tested. | **Independent.** |
| 15 | Winner's-curse bias in the recorded expected information gain | The reported expected gain of the chosen action is re-estimated with fresh Monte-Carlo draws; MC EIG validated against numerical integration (`test_monte_carlo_eig_matches_numerical_integration`); in the oracle regime realised and expected gains agree (ratio 0.97 [0.96, 0.98] on confirmatory seeds). | **Corrected and validated.** |
| 16 | Bayesian machinery errors | Posterior equals a direct scipy computation; simulation-based calibration with truth drawn from the prior passes for passive and information-gain policies in both environments (`< 0.03` pooled reliability error); exact enumeration confirms the POMDP forward algorithm, one-step and two-step EIG. | **Passed (Gate 2).** |
| 17 | Score-orientation errors | `tests/test_orientation_and_streams.py`: a perfect observer gives AUROC 1.0 and an inverted observer is not rescued by the pairwise score; class-balanced accuracy independent of scenario counts. | **Passed.** |
| 18 | Hyperparameter selection bias in the second environment | The GRU training budget (40,000 episodes, 3,000 steps, 64 units) was selected on **development seed 200 only**, by the exact total-variation distance between the learned model and the reference under the training policy and others; confirmatory seeds were not used. The first development run with a smaller budget is kept as `results/bayes2_dev_v0_small_model/` (the learned world model was too poor for the intended regime). | **Disclosed.** |
| 19 | Confirmatory contamination | Confirmatory analysis code and configuration were committed before the confirmatory data existed (commit 413fd43); `git diff` of those files against that commit is empty at analysis time; the confirmatory seeds 300-311 were never used in development. | **Held.** |
