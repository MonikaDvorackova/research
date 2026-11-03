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
| x1_dev_v0_5policies | 7 | development | 5 policies (P0–P4), earlier version of `x1_dev.yaml` (config stored in its meta.json) | 500–505 | `results/x1_dev_v0_5policies` | kept for the record; superseded by `x1_dev` (P5 added) |
| x1_dev | 7 | development | `configs/x1_dev.yaml` | 500–505 | `results/x1_dev` | frozen; used for implementation validation and sample-size reasoning only |
| x1_confirm | 7 | **confirmatory** | `configs/x1_confirm.yaml` @ 02bad01 | 600–629 | `results/x1_confirm` | complete; checksums in `MANIFEST_raw.sha256` |
| x1_audit | 7B | independent checks | `scripts/x1_independent_audit.py` | – | `results/x1_audit` | pass |
| x1 supplementary | 7B | exploratory | `scripts/x1_supplementary_analysis.py` | 600–629 | `results/x1_confirm/supplementary_exploratory.md` | labelled exploratory |
| phase8 diagnostics | 8 | exploratory exact + simulation | `scripts/phase8_diagnostics.py`, `scripts/phase8_transient.py`, `src/eid/phase8.py` | SeedSequence-keyed integers (8–13) | `results/phase8/` | done; no confirmatory claim |
| E6 validity map | 8 (proposed) | confirmatory (planned) | not yet written | dev 700–709, conf 800–829 | – | proposal; needs external design review |
| phase9 dev semantics | 9 | development (exploratory) | `scripts/phase9_dev_semantics.py` | namespace 9000 (10 instances × 3 reps × 10 scenarios) | `results/phase9_dev/` | done; determinism 30/30 |
| phase9 dev audit / EM / CS / trade-off | 9 | development (exact + small simulations) | `scripts/phase9_dev_audit.py`, `phase9_dev_em_cs.py` | namespace 9000 | `results/phase9_dev/` | done |
| E6′ | 9 (proposed) | confirmatory (planned) | not written | dev 9000 + reserved 700–719; confirmatory ≥ 60 structures per family (to be extended from reserved 800–829) | – | **not launched; REVISE** |
