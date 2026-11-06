---
id: topic-bostrom-world-models-governance
title: "Research governance index"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance]
---

# Governance

| Register | Location |
|---|---|
| Research decision log | `decision-log.md` |
| Hypothesis registry | `hypothesis-registry.md` |
| Experiment registry | `experiment-registry.md` |
| Literature verification log | `../../literature/verification-log.md` (+ `../03-literature-search-log.md`) |
| Novelty-threat matrix | `../../literature/novelty-threat-matrix.md` |
| Formal proof-obligation register | `proof-obligations.md` |
| Negative-results register | `negative-results.md` |
| Reproducibility checklist | `reproducibility-checklist.md` |
| Corrections log | `../../notes/corrections-log.md` |

## Rules
1. Hypotheses are written and committed before the data they concern. A hypothesis changed after seeing results is labelled *post hoc* and listed as exploratory.
2. Results directories from earlier phases are immutable (hash manifests `MANIFEST_phase4/5.sha256`, guarded by `test_results_manifest.py`). New work goes in new directories (`results/phase6/...`).
3. Each configuration is versioned; seeds are recorded in the config; confirmatory seeds are disjoint from development seeds.
4. Failed experiments and corrections are recorded, not deleted.
5. Every claim in a note cites its evidence file or literature entry and its reading level.
6. No merge, no submission, no new repository; AIGov repositories untouched.
