---
id: topic-bostrom-world-models-repro-checklist
title: "Reproducibility checklist"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance, reproducibility]
---

# Checklist (apply before every confirmatory run and before each gate)
- [ ] Pre-specification committed before data; hash of commit recorded in the results README.
- [ ] Config file versioned; seeds listed; dev and confirmatory seeds disjoint.
- [ ] All random streams derived from deterministic counters (no Python `hash()`, no global RNG).
- [ ] Run twice; compare arrays (`scripts/compare_runs.py`); record differences.
- [ ] Software versions recorded (Python 3.12, torch 2.15.0, numpy 2.5.4, scipy 1.18.1, sklearn 1.9.1).
- [ ] Hash manifest written; `test_results_manifest.py` passes; earlier manifests unchanged.
- [ ] Full test suite passes.
- [ ] Leakage audit updated (no test-seed information in training or in thresholds).
- [ ] Equivalence controls and positive controls included.
- [ ] Exploratory analyses labelled and kept out of confirmatory tables.
- [ ] Second machine / person replication scheduled (open).
