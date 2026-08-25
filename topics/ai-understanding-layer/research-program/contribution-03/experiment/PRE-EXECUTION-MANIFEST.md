# Pre-Execution Manifest — Contribution 3 Trajectory-Composition Experiment

Frozen prior to running `src/run_experiment.py`. Nothing below may change
after execution without a disclosed, append-only note explaining why —
matching the discipline established for Contribution 2's primary
experiment and its Case 10 follow-up.

## Hypotheses (locked)

- **H0**: Per-decision reconstructability composes into trajectory-level
  reconstructability — if every decision in a trajectory is individually
  reconstructable (Local Decision Reconstruction = 1.00), the trajectory
  as a whole (its dependency edges) is also reconstructable.
- **H1**: Per-decision reconstructability does **not necessarily**
  compose into trajectory-level reconstructability — Local Decision
  Reconstruction can be 1.00 while Trajectory Identifiability is < 1.00,
  because the missing information is a cross-decision relation, not a
  local fact.

The experiment is designed so it is **not allowed to succeed
automatically**: Regime T1 gives the investigator every local fact plus
full license to infer a dependency wherever the evidence uniquely
determines one (never a dumb/blind baseline). If T1 achieves perfect
Trajectory Identifiability on every case, H1 is not supported by this
run and that must be reported as such.

## Cases (locked, 6 cases — case-matrix.md)

| Case | Mechanism | Ambiguous decision(s) |
|---|---|---|
| C3-1 | Fully identifiable control | none |
| C3-2 | Identical-value provenance ambiguity | D3 |
| C3-3 | Branch/abstraction ambiguity | D3 |
| C3-4 | State-write ambiguity | D3 |
| C3-5 | Concurrent/near-concurrent order ambiguity | D3 |
| C3-6 | Negative control (ordinary causal trace event) | none |

## Regimes (locked)

- **T1**: locally complete, globally unlinked. No
  `consumed_from_decision_id` field exists on the record type at all.
- **T2**: locally complete + the one additional cross-decision relation
  (`consumed_from_decision_id`), authored from ground truth at record
  construction time, never inferred.
- Machine-checked invariant: `verify_t1_t2_local_equivalence` — all
  `_LOCAL_FIELDS` are field-for-field identical between T1 and T2 for
  every decision in every case (verified in
  `tests/test_trajectory_experiment.py::test_t1_t2_local_records_are_identical`,
  and re-run as the first step of `run_experiment.py` itself, so a
  violation halts execution rather than being silently scored).

## Reconstruction procedure (locked, src/reconstruction.py)

**T1**, per decision, in this fixed priority order:
1. `causal_trace_event` present (C3-6/D3 only) → UNIQUE, no inference.
2. `depends_on_most_recent` → compare `observed_t0` of all
   strictly-earlier decisions; unique latest → UNIQUE; tied latest →
   AMBIGUOUS (lists all tied candidates).
3. `consumed_input_value` set → match against all strictly-earlier
   decisions' `output_value`; 0 matches → NO_DEPENDENCY; 1 → UNIQUE; 2+ →
   AMBIGUOUS (lists all candidates).
4. Otherwise → NO_DEPENDENCY (root decision).

**T2**: read `consumed_from_decision_id` directly. Present → UNIQUE, no
inference. Absent → NO_DEPENDENCY.

The investigator never guesses among tied/multiple candidates in either
regime.

## Ground truth (locked, src/cases.py, unchanged since implementation)

`TrajectoryGroundTruth.true_edges` and `.ambiguous_by_construction` per
case, as written in `src/cases.py`. Never passed into `reconstruct()`;
consulted only in `src/scoring.py`.

## Metrics (locked, src/scoring.py)

- **Local Decision Reconstruction** — fraction of decisions with correct
  local facts (`context`, `result`). Required to equal 1.00 in every
  case and regime for the experiment to be valid (checked by
  `test_local_decision_reconstruction_is_perfect_in_every_case_and_regime`).
- **Trajectory Identifiability** (primary metric) — case-level binary:
  every dependent edge in the case is CORRECT_UNIQUE. Aggregate =
  fraction of cases fully identifiable.
- **Dependency Edge Accuracy** — among edges the investigator claimed
  UNIQUE, the fraction that are actually CORRECT_UNIQUE.
- **Ambiguity Detection Rate** — among edges genuinely ambiguous by
  construction, the fraction the investigator correctly classified
  AMBIGUOUS (rather than guessing).
- **False Global Confidence Rate** — WRONG_UNIQUE edges / all dependent
  edges. The trajectory-level analogue of Contribution 2's FHC: a
  confidently wrong global answer, categorically worse than an honest
  AMBIGUOUS.

## Interpretation table (locked in advance, to be applied — not
redesigned — after results are in)

| Outcome | Reading |
|---|---|
| A | T1 Trajectory Identifiability = 1.00 on every case → H1 not supported by this run; composition holds for these mechanisms. |
| B | T1 Trajectory Identifiability < 1.00 on the value-collision / order-timing cases, = 1.00 on C3-1/C3-6 → H1 supported; the gap is specifically the missing cross-decision relation, not a general reconstruction failure. |
| C | T1 produces WRONG_UNIQUE (false confidence) on any ambiguous case → categorically worse than B; the investigator is not just incomplete but actively misleading. |
| D | T2 fails to reach Trajectory Identifiability = 1.00 on any case → design defect (T2 is constructed to resolve trivially); must be treated as a bug, not a finding. |
| E | Results vary in a way this table doesn't anticipate → report as-is, do not force into A–D. |
| Combinations (e.g. A+B: some cases fall under A, others under B) are expected and should be reported as such, not collapsed into one label. |

## What must NOT happen after this point

- No case in `src/cases.py` may be edited to change an outcome.
- No metric definition in `src/scoring.py` may be changed post-hoc.
- No new case may be added after seeing results without disclosure.
- The interpretation category (A–E) is chosen from the table above based
  on actual results, not decided before running the experiment.

Tests green at freeze time: 11/11
(`tests/test_trajectory_experiment.py`, run via
`/Users/monikadvorackova/.pyenv/shims/pytest tests/ -v`).
