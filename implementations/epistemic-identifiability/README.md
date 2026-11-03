---
id: impl-epistemic-identifiability-readme
title: "Epistemic identifiability proof-of-concept"
type: implementation
status: active
created: 2026-11-03
updated: 2026-11-03
topic: bostrom-world-models
---

## Epistemic identifiability proof-of-concept

Small, CPU-only PyTorch experiment for the topic [`bostrom-world-models`](../../topics/bostrom-world-models/charter.md). It is a **proof of concept**, not the final study, and says nothing about the physical universe or about consciousness.

### What it does

An embedded agent interacts with a hidden environment through actions and state observations only. The environment is one of:

| Kind | Meaning |
|---|---|
| `E0` | Reference environment with known nonlinear stochastic dynamics |
| `E0split` | Negative control: same transition law as `E0`, implemented with a different noise mechanism |
| `W` | Learned world model trained on `E0` trajectories (four training-set sizes) |
| `Ealt` | Control: `E0` with a perturbed coupling, matched in divergence to `W`. A real mismatch that is not a learned model |

The agent holds its own independently trained ensemble `Q` of dynamics models (a "theory" built from in-distribution experience of `E0`) and tests whether the interaction is consistent with `Q`. It uses one of three intervention policies: `passive` (training-like actions), `wide` (random out-of-distribution actions), `active` (picks actions with maximal ensemble disagreement). Oracle likelihood-ratio statistics are computed on the experimenter side only, as an upper bound.

### Run

```bash
cd implementations/epistemic-identifiability
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=src
pytest -q                                   # automated tests
python -m eid.run --config configs/poc.yaml --out results/poc   # about 10 minutes on a laptop CPU
python -m eid.report --in results/poc       # summary tables
```

Ablations (each about 10 minutes): `abl_relu128` (different architecture), `abl_poly3` (different model class), `abl_qwide` (theory trained over the probed action range), `abl_analytic` (true-law theory; actions chosen by a learned ensemble). More conditions: `abl_qindep` (independently trained theory), `abl_wrelu_qtanh` and `abl_wrelu_qrelu` (second world-model architecture; theory architecture differing or shared), `adaptive_tanh` (adaptive observer: fine-tunes its theory on its own interaction before testing). Compare conditions with `python -m eid.compare`; paired statistics with `python -m eid.stats` (statistical and practical significance reported separately); figure with `python -m eid.figures`; exploratory mechanism check with `python scripts/mechanism_check.py`. Check reproducibility of stored results with `python scripts/reproduce_check.py poc_v2 abl_analytic ...` (re-runs seed 0 and compares to the stored CSV).

`configs/smoke.yaml` is a seconds-long configuration used by the tests. Results written to `results/` are the actual outputs of the executed configuration; see [`results/README.md`](results/README.md).


### Phase 5 additions (Bayesian observers, partially observed benchmark, adversarial validation)

| Component | Files |
|---|---|
| Bayesian model-selection observer, environment 1 | `src/eid/bayes1.py`, `run_bayes1.py`, `analyze_bayes1.py`, `confirm_bayes1.py` |
| Finite POMDP, GRU world model, observer with exact one- and two-step EIG, environment 2 | `src/eid/pomdp.py`, `gruworld.py`, `bayes2.py`, `run_bayes2.py`, `analyze_bayes2.py`, `confirm_bayes2.py` |
| Exact finite-state analyses (Propositions 7–10) | `src/eid/finite.py`, `finite_bayes.py`; tests `test_propositions_phase4.py`, `test_proposition10_exact.py`, `test_class_relative_equivalence.py` |
| Adversarial audit and integrity tests | `test_audit_properties.py`, `test_orientation_and_streams.py`, `test_determinism_bayes.py`, `test_results_manifest.py`, `test_independence.py` |
| Configurations | `configs/bayes1_dev.yaml`, `bayes1_confirm.yaml` (frozen), `bayes1_stress_*.yaml`, `bayes2_dev.yaml`, `bayes2_confirm.yaml` (frozen) |
| Scripts | `scripts/equivalence_demo.py`, `reproduce_bayes.py`, `compare_runs.py`, `phase4_equivalence_posthoc.py`, `mechanism_check.py` |
| Stress and figures | `src/eid/stress_summary.py`, `figures5.py` |

Pre-specification: `topics/bostrom-world-models/notes/preregistration-phase5.md`, committed before the confirmatory data (commits `413fd43`, `23896a3`). Confirmatory runs: `results/bayes1_confirm/`, `results/bayes2_confirm/` (run A, primary) and `*_runB/` (deterministic replication). The full list of commands is in `topics/bostrom-world-models/notes/reproducibility-phase5.md`; the Phase 5 result directories are described in `results/README_phase5.md`.
