# Results Summary — Trajectory-Composition Experiment

Raw data: `results/case_level_results.csv`, `results/edge_level_results.csv`,
`results/aggregate_by_regime.json`. All numbers below are read directly
from those files, not recomputed independently in prose.

## Headline numbers

| Metric | T1 (locally complete, globally unlinked) | T2 (locally complete + relation) |
|---|---|---|
| Local Decision Reconstruction | 1.000 | 1.000 |
| Trajectory Identifiability | 0.333 (2/6) | 1.000 (6/6) |
| Dependency Edge Accuracy | 1.000 | 1.000 |
| Ambiguity Detection Rate | 1.000 (4/4) | 0.000 (0/4) |
| False Global Confidence Rate | 0.000 | 0.000 |

## Case-by-case (T1)

| Case | Mechanism | T1 trajectory identifiable? | T1 edge classification |
|---|---|---|---|
| C3-1 | control | True | CORRECT_UNIQUE |
| C3-2 | value collision | **False** | AMBIGUOUS |
| C3-3 | branch/abstraction collision | **False** | AMBIGUOUS |
| C3-4 | state-write collision | **False** | AMBIGUOUS |
| C3-5 | concurrent/order ambiguity | **False** | AMBIGUOUS |
| C3-6 | negative control | True | CORRECT_UNIQUE |

## Required validity check

Per PRE-EXECUTION-MANIFEST.md, the experiment is only valid if Local
Decision Reconstruction stayed perfect while Trajectory Identifiability
diverged. Confirmed: `local_decision_reconstruction_rate` = 1.0 in both
regimes for every one of the 12 (case × regime) runs
(`case_level_results.csv`, column 3, all rows), while
`trajectory_identifiable` is False for exactly the 4 cases built to
carry a cross-decision ambiguity mechanism (C3-2/3/4/5), and True for
the control and negative control. The divergence is present and is
attributable specifically to the missing cross-decision relation, not to
any loss of local information.

## False-confidence check

`dependency_edge_accuracy` = 1.0 and `false_global_confidence_rate` =
0.0 for T1: every edge T1 was willing to call UNIQUE was in fact
CORRECT_UNIQUE (C3-1/D2, C3-6/D3), and on every genuinely ambiguous edge
it returned AMBIGUOUS rather than guessing
(`edge_level_results.csv`, T1 rows for C3-2/3/4/5 all show
`reconstructed_status=AMBIGUOUS`, `classification=AMBIGUOUS`, never
`WRONG_UNIQUE`). No instance of false global confidence occurred in this
run.

## Negative control check

C3-6 is locally identical to C3-2 (same value-collision structure, same
`output_value`/`consumed_input_value`) except for one additional
ordinary trace field on T1's D3 record (`causal_trace_event`). C3-2/T1
is AMBIGUOUS; C3-6/T1 is CORRECT_UNIQUE. This isolates the effect to the
one added relation, not to some other difference between the cases
(verified directly in
`test_negative_control_c3_6_locally_equivalent_to_c3_2_except_one_relation`,
green before execution, and confirmed by the matching raw rows above).
