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
