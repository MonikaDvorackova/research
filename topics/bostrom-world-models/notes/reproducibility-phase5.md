---
id: topic-bostrom-world-models-reproducibility-phase5
title: "Reproducibility documentation (Phases 1–5)"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [reproducibility, provenance]
---

## Reproducibility documentation

### Software and hardware (recorded in each result directory's `provenance.json`)

Python 3.12.1; PyTorch 2.15.0 (float32, CPU; one thread per worker process via `torch.set_num_threads(1)`); NumPy 2.5.4; SciPy 1.18.1; scikit-learn 1.9.1; PyYAML 6.0.3; Matplotlib 3.11.2; pytest 9.2.0. macOS 26.2 on Apple M4 Pro (arm64), 12 cores, 24 GB. Workers are started with the `spawn` method. NumPy's BLAS thread count is not pinned; the experiments are small enough that this did not change results in the determinism test, but cross-machine bit-identity is **not claimed**.

### Where randomness enters and how it is controlled

- All random streams come from `numpy.random.SeedSequence([seed, tag, extra])` (environment 1 phases 1–4: `eid.run.rng_for`; Phase 5: `eid.bayes1.brng`, `eid.run_bayes2.rs`). Tags separate roles (observer theory data, world-model data, alternative matching, simulation, candidate actions, evaluation, calibration, adaptation). Torch network seeds are fixed functions of the seed and the network index. Distinctness is tested (357 identifiers in phases 1–4; every tag × index in Phase 5).
- **Defect and fix.** Phase 5 run A derived the interaction-phase stream index from Python's randomised `hash()` of strings; see `corrections-log.md` #14. After the fix every cell has a deterministic collision-free index, and `tests/test_determinism_bayes.py` checks identical output across separate processes with different `PYTHONHASHSEED`. **Run A is preserved but not bit-reproducible; run B (`*_runB`) is: re-running one full confirmatory seed per environment in a fresh process reproduced all stored arrays exactly (300 arrays for environment 1 seed 300 and 450 for environment 2 seed 300, 0 mismatching).**
- Seeds: Phase 1–4 experiments 0–9; Phase 5 development 200–204 (environment 1) and 200–203 (environment 2); confirmatory 300–311; stress 400–405. Confirmatory seeds were never used in development.

### Models and training

- **Environment 1** (fully observed): E₀ with σ = 0.1, coupling 0.2, initial-state sd 0.5. Learned models are Gaussian MLPs predicting the next state residually: tanh, 2 hidden layers of 64 units (world model; observer's tanh theories), or ReLU, 3 hidden layers of 128 units (observer's ReLU theories and some world-model variants); Adam, learning rate 3e-3, batch 256, 1,500 steps, Gaussian NLL, log-std clamped to [−5, 1]. Training data: episodes of 20 steps from E₀ with actions uniform on [−1, 1] unless a configuration states otherwise; the observer's theories use one sample of 5,000 transitions with bootstrap resampling; observer's world-model guesses use independent samples of 500, 2,500 and 12,500 transitions; the true world model uses 12,500 (stress: 500, 2,500).
- **Environment 2** (POMDP): hidden states 4, observations 3, actions 3, structured transitions with per-seed jitter 0.08; GRU world models with 64 units, autoregressive categorical output with previous observation and action as input; Adam, learning rate 5e-3, batch 128, 3,000 steps, 12-step episodes, 40,000 episodes (observer's guesses of other sizes: 5,000, 15,000, 40,000), training policy probabilities (0.49, 0.49, 0.02). Training budget selected on development seed 200 only (see leakage audit #18).
- **Observer hypothesis spaces:** environment 1 deviation grids γ ∈ geomspace(0.05, 1.6, 9), δ ∈ geomspace(0.1, 3.0, 9); environment 2 contamination grid η ∈ {0.02, 0.05, 0.1, 0.2, 0.35, 0.5}. Priors, decision threshold (0.95) and checkpoints are in the configuration files.

### Intervention policies

Environment 1: passive (uniform on [−1, 1]), wide (uniform on [−3, 3]), sweep (cycle over 11 actions in [−3, 3]), eig (myopic class-level EIG by Monte Carlo over 16 random candidates, 24 posterior-predictive draws, re-estimated with 128 fresh draws for the recorded value). Environment 2: passive (training-like), random (uniform), sweep (cycle 0, 1, 2), no2 (uniform over {0, 1}), eig (exact myopic), eig2 (exact two-step, open-loop plans, first action executed). No policy has access to the true environment.

### Statistical procedures

Unit of analysis: the seed. Intervals: percentile bootstrap over seeds (2,000 resamples; 5,000 for confirmatory tables). Directional tests: exact one-sided Wilcoxon signed-rank against the threshold, Holm-adjusted within the pre-specified family. Equivalence: paired TOST (t-based) at the stated margin, Holm-adjusted within its family. Practical thresholds and margins are fixed in `preregistration-phase5.md` (confirmatory) or in the script header (Phase 4 post hoc tests). Phase 1–4 paired comparisons: `eid.stats`. Calibration: ECE with 10 equal-width bins on the confidence (class-balanced weights); Platt-based calibration in Phase 1–4 is experimenter-side only.

### Commands

```bash
cd implementations/epistemic-identifiability
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
export PYTHONPATH=src
pytest -q                                                      # all tests
python -m eid.run_bayes1 --config configs/bayes1_confirm.yaml --out results/bayes1_confirm_runB
python -m eid.confirm_bayes1 --dir results/bayes1_confirm_runB --out results/bayes1_confirm_runB/confirmatory.md
python -m eid.run_bayes2 --config configs/bayes2_confirm.yaml --out results/bayes2_confirm_runB
python -m eid.confirm_bayes2 --dir results/bayes2_confirm_runB --out results/bayes2_confirm_runB/confirmatory.md
python scripts/reproduce_check.py poc_v2 abl_analytic ...     # Phase 1-4 seed-0 re-runs
python scripts/equivalence_demo.py                             # exact intervention-class equivalence demonstration
```

### Integrity checks in the repository

`tests/test_results_manifest.py` (frozen Phase 1–4 results, SHA-256 of LF-normalised bytes); `results/MANIFEST_phase5.sha256` (Phase 5 results, added at the end of the phase); golden-output test for the default Phase 1–4 path; determinism test for the Bayesian runners; leakage audit (`leakage-audit.md`); corrections log (`corrections-log.md`); pre-specification commits `413fd43` (environment 1) and `23896a3` (environment 2) precede their confirmatory data.
