---
id: impl-epistemic-identifiability-results-readme-phase5
title: "Results directory, Phase 5"
type: implementation
status: active
created: 2026-11-03
updated: 2026-11-03
topic: bostrom-world-models
---

### Phase 5 directories

| Directory or file | Description |
|---|---|
| `bayes1_dev/`, `bayes2_dev/`, `bayes2_dev_v0_small_model/` | Development runs (exploratory; development seeds). The `v0` run used a GRU budget too small for the intended regime and is kept for the record. Produced before the stream-index fix (not bit-reproducible). |
| `bayes1_confirm/`, `bayes2_confirm/` | **Confirmatory run A** (held-out seeds 300–311; primary pre-specified analysis in `confirmatory.md`; raw posteriors in `seed*.npz`). `PREREG_COMMIT.txt` records the pre-specification commit. Not bit-reproducible (randomised stream index; corrections log #14). |
| `bayes1_confirm_runB/`, `bayes2_confirm_runB/` | **Run B**: identical configuration and seeds with the deterministic stream index (bit-reproducible). Raw arrays are git-ignored; their SHA-256 hashes are in `MANIFEST_phase5.sha256`. |
| `bayes1_stress_*` (run A) and `*_runB` | Exploratory stress tests (seeds 400–405): coverage, fidelity, incomplete hypothesis spaces, misleading priors. |
| `compare_runs_bayes1.md`, `compare_runs_bayes2.md` | Decision-by-decision comparison of run A and run B. |
| `repro_bayes1_seed300.txt`, `repro_bayes2_seed300.txt` | Exact re-run of one confirmatory seed per environment against the stored run B (0 mismatching arrays). |
| `stress_summary.md`, `stress_summary_runB.md` | Stress-test tables (exploratory). |
| `phase4_equivalence_posthoc.md` | Post hoc equivalence tests on the frozen Phase 4 results. |
| `figures/phase5_*.png` | Figures for the Phase 5 confirmatory data. |
| `MANIFEST_phase4.sha256`, `MANIFEST_phase5.sha256` | SHA-256 manifests (LF-normalised); guarded by `tests/test_results_manifest.py`. |
