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

Ablations (each about 10 minutes): `abl_relu128` (different architecture), `abl_poly3` (different model class), `abl_qwide` (theory trained over the probed action range), `abl_analytic` (true-law theory; actions chosen by a learned ensemble). Compare conditions with `python -m eid.compare`. Check reproducibility of stored results with `python scripts/reproduce_check.py poc_v2 abl_analytic ...` (re-runs seed 0 and compares to the stored CSV).

`configs/smoke.yaml` is a seconds-long configuration used by the tests. Results written to `results/` are the actual outputs of the executed configuration; see [`results/README.md`](results/README.md).
