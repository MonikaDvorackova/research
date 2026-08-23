# Follow-up Case 10 — Temporal Ambiguity from Observational Precision Loss

A narrowly scoped follow-up to the primary Contribution 2 reconstruction
experiment (`../`), addressing the one documented, disclosed limitation of
that experiment's Case 10: it did not actually test concurrency/timestamp
ambiguity, because its decision timestamps (11:59:00 and 12:01:00,
straddling a boundary at exactly 12:00:00) were full-precision and 60
seconds from the boundary — a plain half-open interval query resolves
that unambiguously. No observational precision loss was ever modeled.

**The primary experiment (commit `31c58ddc6e95b5f66153b4c2dd35d91f4ae8e725`)
is immutable.** Nothing here modifies `../src/`, `../tests/`,
`../results/`, `../analysis/`, `../RESULT.md`, or `../PRE-EXECUTION-MANIFEST.md`.
This follow-up imports only the stable, pure schema/logic pieces from
`../src/domain.py` (dataclasses and the fixed decision rule) — read-only,
unmodified — and defines everything else (cases, regimes, reconstruction,
scoring) fresh, specifically because this follow-up needs reconstruction
behavior (an explicit `AMBIGUOUS` outcome, never a forced guess) that the
primary experiment's algorithm does not need and should not be changed to
support.

## What this tests

Mechanism: **timestamp precision / ordering ambiguity** (Step 3's
mechanism A), not retroactive correction (already tested by the primary
experiment) and not clock skew or missing causal relations in general
(mechanisms B and D, out of scope — see `research-question.md`).

A decision's true moment (`true_t0`, microsecond precision) is known only
to ground truth. The *observable*, persisted decision timestamp
(`observed_t0`) is truncated to whole-second precision — a realistic,
common logging practice. When a policy/authority/model version boundary
falls strictly inside the one-second window `[observed_t0, observed_t0 +
1s)`, an investigator who only has the observable timestamp cannot tell,
from timing alone, which side of the boundary the decision actually fell
on: two versions are genuinely, honestly compatible with the observable
record.

## Reading order

1. `research-question.md` — locked question, H0-F10/H1-F10.
2. `case-matrix.md` — the six cases (F10-1..F10-6) and why this mechanism,
   not a combined one, was selected.
3. `PRE-EXECUTION-MANIFEST.md` — the freeze point.
4. `src/` — implementation.
5. `analysis/experiment-report.md`, `RESULT.md` — results, written after
   execution.

## Reproduce

```
cd followup-case10
pytest tests/ -q                          # must pass, including the
                                           # unchanged original 31 tests
                                           # re-run from ../tests/
python3 -m src.run_experiment --manifest
python3 -m src.run_experiment
```

No randomness anywhere; fully deterministic.
