---
id: topic-bostrom-world-models-experiment-registry
title: "Experiment registry"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance, experiments]
---

# Experiment registry
| ID | Phase | Type | Config / script | Seeds | Results dir | Status |
|---|---|---|---|---|---|---|
| poc_v1, poc_v2 | 2–3 | pilot | `configs/poc.yaml` | see config | `results/poc_v*` | frozen; v1 superseded by v2 after stream-collision correction |
| abl_* | 3–4 | ablations | `configs/abl_*.yaml` | see config | `results/abl_*` | frozen |
| adaptive_tanh | 4 | adaptive observer | `configs/adaptive_tanh.yaml` | see config | `results/adaptive_tanh` | frozen; negative for original thesis |
| bayes1_dev / bayes2_dev | 5 | development | `bayes{1,2}_dev.yaml` | 200 | `results/bayes*_dev` | frozen |
| bayes1_confirm | 5 | confirmatory | `bayes1_confirm.yaml` | 300–311 | `results/bayes1_confirm` (+`_runB`) | frozen |
| bayes2_confirm | 5 | confirmatory | `bayes2_confirm.yaml` | 300–311 | `results/bayes2_confirm` (+`_runB`) | frozen |
| stress_{cov,fid500,fid2500,hyp} | 5 | exploratory | `bayes1_stress_*.yaml` | 400–405 | `results/stress_*` | frozen |
| phase6 prediction-vs-identification | 6 | exploratory exact diagnostic | `scripts/phase6_prediction_vs_identification.py` | none (exact) | `results/phase6/` | done |
| X1 | 6 (proposed) | confirmatory (planned) | not yet written | dev 500–505; conf 600–619 | – | proposal |
| X3 | planned | confirmatory | – | ≥ 20 | – | not designed in detail |
| X2 | planned | exact/theory | – | – | – | not started |
