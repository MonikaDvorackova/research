---
id: note-contribution-02-article-review-empirical-traceability
title: "Contribution 2 Article — Empirical Traceability Table"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, traceability]
refs: [../draft-v1.md]
---

## Empirical Traceability Table

Every numerical or quantitative statement in `../draft-v1.md`, re-checked
directly against the committed raw/aggregate CSVs in this review session
(not merely re-trusting the prior self-audit's table).

| # | Claim (as written in draft-v1) | Experiment | Case(s) | Raw result file | Metric | Exact value found | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | "Regime B's temporal-correctness score on this case dropped to 0.00, versus 1.00 for Regime C" | Primary | Case 3 (D3) | `experiment/results/case_level_results.csv` | `tc` | B: `tc=0`; C: `tc=1` | **PASS** |
| 2 | "the two forward-drift cases where policy and authority genuinely changed... B and C were identical — both at 1.00" | Primary | Cases 2, 4 | Same file | `tc` | Case 2: B `tc=1`, C `tc=1`. Case 4: B `tc=1`, C `tc=1` | **PASS** |
| 3 | "two combined-drift cases... B's temporal correctness stayed at 0.00 while C stayed at 1.00" | Primary | Cases 8, 9 | Same file | `tc` | Case 8: B `tc=0`, C `tc=1`. Case 9: B `tc=0`, C `tc=1` | **PASS** |
| 4 | "On the retroactive-drift case, B's false-confidence rate was 0.50" | Primary | Case 3 (D3) | Same file | `fhc_rate` | B: `0.5000` | **PASS** |
| 5 | "on one of the combined-drift cases, 1.00" | Primary | Case 8 (D8) | Same file | `fhc_rate` | B: `1.0000` (Case 9's B `fhc_rate` is `0.5000` — the draft correctly says "one of," not both) | **PASS** |
| 6 | "Regime C's rate was 0.00 on every case in the experiment, without exception" | Primary | All 10 cases (11 rows) | Same file, all `regime=C` rows | `fhc_rate` | All `0.0000` | **PASS** |
| 7 | "each decision was recorded a full 60 seconds from the boundary, on its own side" | Primary | Case 10 (D10x, D10y) | `experiment/src/cases.py`, `case_10()` | timestamps | `boundary=12:00:00`, `t0_x=11:59:00` (60s before), `t0_y=12:01:00` (60s after) | **PASS** (verified directly against source, re-confirmed in this review, not only against the prior audit's table) |
| 8 | "the observable, persisted decision timestamp is truncated to the nearest second" | Follow-up | All F10 cases | `followup-case10/src/domain.py`, `PRECISION = timedelta(seconds=1)` and `observed_t0()` | design parameter | 1-second truncation, confirmed by source inspection | **PASS** |
| 9 | "Across the follow-up's four ambiguous cases... Regime B... correctly reported the dependency as ambiguous... every single time... and never when it didn't" | Follow-up | F10-2, F10-3, F10-4, F10-5 (ambiguous); F10-1, F10-6 (not ambiguous) | `followup-case10/results/case_level_results.csv` | `adr` and `*_class` | F10-2/3/4/5: `adr=1.0000` on the one ambiguous dimension each. F10-1: no ambiguous dimension (blank `adr`), all classes `CORRECT_UNIQUE`. F10-6: `adr=0.0000` (nothing to detect — B resolved uniquely), all classes `CORRECT_UNIQUE` | **PASS** |
| 10 | "Regime C, whose binding was authored using the decision's true, unrounded moment, resolved every one of the same cases correctly and uniquely" | Follow-up | F10-1 through F10-6 | Same file, all `regime=C` rows | `policy_class`, `authority_class`, `model_class`, `tc` | All `CORRECT_UNIQUE`; `tc=1` on all six | **PASS** |
| 11 | "With that one field present, Regime B matched Regime C exactly. Same unique, correct answer. Same score on every metric" | Follow-up | F10-6 | Same file, `case_id=F10-6` | `tc`, `urr`, `adr`, `ac`, `fhc_rate` | B: `tc=1, urr=1.0000, adr=0.0000, ac=1, fhc_rate=0.0000`. C: identical on every field | **PASS** |
| 12 | "Word count: 2,723" | Self-referential | — | `article/draft-v1.md` itself | word count | Recomputed independently in this review: `2,723` (regex word-count of the file excluding the footer line itself) | **PASS** |

## Result

**12 of 12 numerical claims PASS traceability — every number in
draft-v1's body is exactly correct against the committed raw/aggregate
data, with no rounding, estimation, or invention detected.**

This traceability result is **orthogonal to** `claim-review.md`'s
findings on claims 5, 7, and 19 (the "no amount of... fixes this" /
"solve it completely" overstatement) — those are **interpretation**
problems (the numbers are used to support a conclusion broader than the
numbers themselves justify), not **sourcing** problems (the numbers
themselves are exactly correct). A number can pass this traceability
check and still be attached to an overstated claim; both checks are
necessary and neither substitutes for the other. See
`reviewer-report.md` and `claim-review.md` for the interpretation-level
findings.
