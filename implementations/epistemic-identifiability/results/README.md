---
id: impl-epistemic-identifiability-results-readme
title: "Results directory"
type: implementation
status: active
created: 2026-11-03
updated: 2026-11-03
topic: bostrom-world-models
---

## Results

| Directory | Config | Description |
|---|---|---|
| `poc_v1/` | `configs/poc.yaml` at commit of the first run | First full run (10 seeds). Controls: E0, E0split, Ealt. Kept unchanged for the record. Its `metrics.csv` has no AltOOD columns. |
| `poc_v2/` | `configs/poc.yaml` | Identical configuration plus the post-hoc control AltOOD (added after reading v1). Same seeds, so shared columns reproduce v1 exactly (checked by comparing the tables). |

Each directory holds `metrics.csv` (per seed, quality, policy, horizon), `quality.csv`, `summary.md`, `summary.json`, `config_used.json`, `run.log`, and `auroc_by_horizon.png`. Interpretation and limits: `topics/bostrom-world-models/notes/results.md`.
