# Contribution 2 Reconstruction Experiment — Implementation

Implements and executes the experiment designed in `../experiment-design/`
(read that directory first — it is authoritative; nothing here revises it).
Pure Python 3 standard library, no third-party dependencies.

## Layout

```
experiment/
├── README.md
├── PRE-EXECUTION-MANIFEST.md       # frozen before the run in results/
├── PRE-EXECUTION-case-manifest.json
├── RESULT.md                       # short, human-readable verdict
├── src/
│   ├── domain.py                   # schemas + the fixed decision rule
│   ├── cases.py                    # the 10-case perturbation matrix
│   ├── regimes.py                  # Regime A/B/C views + B/C equivalence check
│   ├── reconstruction.py           # the deterministic investigator
│   ├── scoring.py                  # AIA / TC / AC / JC / FHC
│   └── run_experiment.py           # orchestrator (CLI entry point)
├── tests/                          # 31 pre-execution invariant tests
├── results/                        # raw + aggregated output (generated)
└── analysis/                       # results-summary.md, experiment-report.md
```

## Reproduce

```
cd experiment
pytest tests/ -q                        # 31 tests, must all pass first
python3 -m src.run_experiment --manifest  # regenerate the structural case manifest
python3 -m src.run_experiment             # regenerate results/*.{jsonl,csv}
```

Fully deterministic: no randomness is used anywhere in this experiment, so
no seed is required and re-running always reproduces byte-identical
`case_level_results.csv`/`aggregate_by_category.csv` content (timestamps
inside `raw_results.jsonl` are the synthetic cases' own fixed t0/query_time
values, not wall-clock time).

## Status

Implemented and executed. See `RESULT.md` for the short verdict,
`analysis/experiment-report.md` for the full report, and
`../novelty-verdict.md`'s post-experiment update for the consequence to
Contribution 2's thesis.
