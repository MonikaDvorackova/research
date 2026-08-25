---
id: note-contribution-03-article-empirical-traceability
title: "Contribution 3 Article draft-v1 — Empirical Traceability"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, traceability]
refs: [../draft-v1.md, ../../experiment/results/aggregate_by_regime.json, ../../experiment/results/case_level_results.csv, ../../experiment/results/edge_level_results.csv]
---

Every numeric or count claim in `draft-v1.md`, checked directly against
`experiment/results/*` in this session (re-read fresh, not trusted from
`draft-v1-audit.md`).

| Exact claim in draft-v1 | Location | Raw file | Case/regime | Metric | Raw value | PASS/FAIL |
|---|---|---|---|---|---|---|
| "Local Decision Reconstruction... was 1.00 in both regimes, across all six cases" | line 57 | `aggregate_by_regime.json` | T1, T2 | `local_decision_reconstruction_rate` | T1: 1.0, T2: 1.0 | **PASS** |
| "Trajectory Identifiability... was 1.00 under T2" | line 59 | `aggregate_by_regime.json` | T2 | `trajectory_identifiability_rate` | 1.0 | **PASS** |
| "0.33 (two of six cases) under T1" | line 59 | `aggregate_by_regime.json`; `case_level_results.csv` | T1 | `trajectory_identifiability_rate`; count of `trajectory_identifiable=True` | 0.3333333333333333 (rounds to 0.33); exactly 2 rows True (C3-1, C3-6) | **PASS** |
| "The two T1 successes were the control case... and the negative control" | line 59 | `case_level_results.csv` | T1 | `trajectory_identifiable` by `case_id` | `C3-1,T1,...,True`; `C3-6,T1,...,True`; all of C3-2/3/4/5,T1 = `False` | **PASS** |
| "Dependency Edge Accuracy... was 1.00" | line 67 | `aggregate_by_regime.json` | T1 | `dependency_edge_accuracy` | 1.0 | **PASS** |
| "False Global Confidence... was 0.00" | line 67 | `aggregate_by_regime.json` | T1 | `false_global_confidence_rate` | 0.0 | **PASS** |
| "Every one of the four cases T1 failed to identify, it failed honestly: it returned AMBIGUOUS" | line 67 | `edge_level_results.csv` | T1, C3-2/3/4/5 | `reconstructed_status`, `classification` | all four rows: `AMBIGUOUS` / `AMBIGUOUS`; zero `WRONG_UNIQUE` anywhere in the file | **PASS** |
| "C3-6 is built identically to the value-collision case that fails under T1 [C3-2]... with exactly one difference" | line 75 | `experiment/src/cases.py` | C3-2 vs. C3-6 | structural comparison | confirmed by direct inspection: both use `output_value=7`/`consumed_input_value=7`, D1/D2 independent producers; only C3-6's `t1_view` populates `causal_trace_event` (`src/regimes.py` lines 26–27) | **PASS** |
| "the case resolves correctly, T2-style" (re: C3-6/T1) | line 75 | `edge_level_results.csv` | C3-6, T1 | `classification` | `CORRECT_UNIQUE`, predecessor `D1`, matching `true_predecessor=D1` | **PASS** |
| "six designed cases are not a statistical sample" / no prevalence claim | line 101 | article text | — | grep for "sample," "p-value," "significant," "prevalence," "statistically" | only occurrence is line 101 itself, in the correct disclaiming direction ("nothing about prevalence... not a statistical sample... no inference... is appropriate"); no other line uses any of these terms, and no line uses them to assert a rate, sample, or significance claim (re-grepped in this session) | **PASS** |
| Word count: "3,257 (full file...)" | line 127 | `draft-v1.md` | — | `wc -w draft-v1.md` | 3257 | **PASS** (re-run fresh in this session, matches exactly) |
| Citation markers [1]–[5] each used once, each has a References entry | lines 83–87, 113–123 | article text | — | grep `\[[0-9]\]` | `[1]` line 83; `[2]`,`[3]` line 85; `[4]`,`[5]` line 87; all five present in References (lines 115–123); no dangling or unused entries | **PASS** |

## Not independently re-derivable from the raw CSV/JSON alone (design claims, checked against source instead)

| Claim | Location | Source checked | PASS/FAIL |
|---|---|---|---|
| "that check re-runs automatically before every execution of the experiment. If it fails, the run halts. It never failed." | line 49 | `experiment/src/run_experiment.py`: `verify_t1_t2_local_equivalence(world)` called for every world before any regime is scored, unconditionally, before results are written | **PASS** |
| "No field on the record type stores any relation to another decision at all" (T1) | line 45 | `experiment/src/domain.py`, `DecisionRecordT1` (lines 43–55): no field encodes a cross-decision relation except `causal_trace_event`, populated only for C3-6 | **PASS**, and see `reviewer-report.md` Objection 6 for the interpretive consequence of this being true |
| "An investigator was built for each regime. Neither is a strawman." | line 53 | `experiment/src/reconstruction.py`: T1 path attempts value-collision resolution and order resolution before falling back to NO_DEPENDENCY; never guesses among tied candidates | **PASS** |

## Overall

**Zero factual/numeric discrepancies found.** Every number, count, and
structural claim in draft-v1 matches the raw results and source files
exactly. The issues this review raises (Objection 6, construct validity,
title overclaim, formalization triviality) are interpretive and framing
issues, not traceability failures — the article does not misreport its
own data anywhere.
