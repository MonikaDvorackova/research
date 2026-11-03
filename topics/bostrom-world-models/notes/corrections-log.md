---
id: topic-bostrom-world-models-corrections-log
title: "Errors discovered and corrected"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [integrity, corrections]
---

## Errors discovered and corrected

Every error found during the project, in order, with what was affected and how it was handled. Earlier results are not rewritten; corrections are recorded here and in the affected notes.

| # | Phase | Error | Impact | Handling |
|---|---|---|---|---|
| 1 | 1 | Ramezanian arXiv:2609.10864 characterised as a closest philosophical neighbour from a search snippet | Novelty assessment | Withdrawn after reading the abstract in Phase 2: not about simulation |
| 2 | 4 | Test of Proposition 8-style posterior concentration used two models almost equidistant from the truth | A test, not a proposition | Margin made decisive in Phase 4; the test now asserts the margin |
| 3 | 2 | Control AltOOD added to the environment dictionary shifted random-stream indices, causing stream collisions across policies | `poc_v2` first run | Detected by comparing with `poc_v1` (534 of 720 rows differed in shared columns); fixed by separate tags; run repeated; v2 then matched v1 in all shared columns; v1 kept unchanged |
| 4 | 2 | `sed` failure in a chained command meant edits were not applied | Documentation | Detected by grep; edits redone |
| 5 | 2 | Phase 2 README claimed v2 reproduced v1 before it did | Documentation | Retracted and fixed once true |
| 6 | 3 | Claim that Chalmers "states his arguments do not require undetectable simulation" came from a search summary, not the text | Literature review | Qualified; not relied on |
| 7 | 3 | The "matched-divergence" control Ealt did not test the intended point (different discrepancy profile) | Interpretation of F5 | Disclosed; AltOOD added as an explicitly post hoc control; interpretation of both revised in Phase 3 and Phase 4 |
| 8 | 4 | "Low ECE reflects uninformative scores" (F6) was incomplete | Interpretation | Corrected: Platt scaling fitted on labels recalibrates inverted scores; ECE and Brier not meaningful where AUROC < 0.5 |
| 9 | 4 | The two "W = ReLU" conditions were suspected of coupling; their FPR rows equalled other conditions' rows | None (expected) | Explained: FPR is measured on controls with the theory alone; recorded as a sanity check |
| 10 | 4 | Quoted stream count 330; the actual number is 357 | Documentation | Corrected in Phase 4 |
| 11 | 4 | Corollary stated "the expected number of episodes needed is ln ω / KL" | Formal statement | **False as worded** (Wald overshoot); corrected to E[τ] ≥ ln ω / KL in Phase 5, with a visible correction note |
| 12 | 4 | Proposition 8(c) lacked the assumption that test episodes are independent of adaptation episodes; Proposition 9(a) did not state that it concerns KL and fixed-size tests | Formal statements | Assumption and scope added in Phase 5 |
| 13 | 5 | Conjecture that a catch-all hypothesis would make myopic EIG explore an untried action | Conjecture, never reported as a result | Refuted by exact computation; recorded as a counterexample; corrected statement is Proposition 10(c) |
| 14 | 5 | The Bayesian runners (`run_bayes1.py`, `run_bayes2.py`) derived the interaction-phase random stream from Python's built-in `hash()` of a tuple of strings, which is randomised per process | **Reproducibility defect.** The stored first runs ("run A": `bayes1_dev`, `bayes2_dev`, `bayes1_confirm`, `bayes2_confirm`, the four stress runs) are statistically valid (each cell still receives an independent stream, apart from a few-percent chance per seed that two cells shared a stream through hash collisions in a space of 100,000 identifiers) but are **not bit-reproducible**. Found while preparing the reproducibility documentation, after the pre-specified confirmatory analyses had been run on run A | Fixed by a deterministic collision-free cell index; regression test `tests/test_determinism_bayes.py` (identical output across processes with different `PYTHONHASHSEED`). The confirmatory and stress runs were repeated with the fixed code as "run B" with identical configurations and seeds. Run A is preserved unchanged and its pre-specified analysis stands as the primary analysis; run B is reported as a bit-reproducible replication, and any disagreement between them is reported. The only change to code after the pre-specification commits is the stream-index line in the two runners; the analysis scripts are unchanged |
| 15 | 5 | I appended Phase 5 notes to `results/README.md`, a file frozen by the Phase 4 manifest | None (documentation only), but a frozen file was modified | Caught by `tests/test_results_manifest.py` the same hour; the file was restored from git and the Phase 5 notes moved to `results/README_phase5.md`; the manifests were regenerated and the full suite re-run |
| 16 | 9 | Phase 8 called rejections under out-of-class truths "false alarms/invalid/fails" (T4 counterexample, T6a, T6b) | **Semantic error** (a rejection of a false formal null is not a type-I error); interpretation ("mechanism changed") was the actual error | Three-way separation (type-I / misspecification / false attribution) in `phase9/02`; erratum appended to `phase8/02`; Phase 8 files preserved |
| 17 | 9 | Phase 8 T4′ cited "0/100 in S4, S5" as robustness under misspecification | Over-reading: null false, non-rejection = low power | Claim withdrawn (`phase9/01` A2) |
| 18 | 9 | Phase 8 T5 stated that identification of the true mechanism decreases with n | Valid only at the non-generic truth ψ₀ = ½; recovers for any fixed ψ₀ ≠ ½ | Restated as a window; exact table (`phase9/01` §3) |
| 19 | 9 | Phase 8 T6d confidence-set repair stated without assumptions; dev implementation uses fixed-n CP boxes | Assumptions (independence, coverage on all contexts, time-uniform set) missing; implementation not rigorous | Assumptions stated; LR confidence sequences specified for E6′ |
| 20 | 9 | Prop 5 rejection-event bound uses exact size α | Scope: conservative tests (size < α) need the exact size | Scope note (`phase9/01` A5) |
| 21 | 9 | Phase 8 E6 analysis plan: "CP upper bound ≤ 0.07", pooled run-level intervals, 30 structures × 20 runs | Weaker-than-nominal criterion; pooled CP undercovers under clustering (0.81 at ICC 0.2); R = 20 cannot certify per-structure bounds | Corrected plan (`phase9/06`) |
| 22 | 9 | PO-2 listed as open | Provable by optional stopping with δ_max | Proved (`phase9/01`) |
