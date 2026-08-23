# Contribution 2 Reconstruction Experiment — Pre-Execution Manifest

This file is the freeze point required by the authorized implementation
workflow's PHASE 2. Everything below (hypotheses, cases, metrics, regimes,
algorithm versions, expected interpretation table) is fixed as of this
point. It must not be altered based on the outcome of the run that follows.

## Git state

- Repository: `research` (this workspace)
- Branch: `fix/research-agent-audit-status`
- Base commit this implementation was built on: `21dbbd39e065dd48a49b989b940d176ff6933068`
- Working tree at freeze time: all changes are new, untracked files under
  `topics/ai-understanding-layer/research-program/contribution-02/experiment/`
  (no other path modified).

## Authorization

Implementation and execution were explicitly authorized in the same
conversation that performs them, per the two-step gate described in
`../../CHECKPOINT-2026-08-23.md` ("Next Exact Action").

## Disclosed pre-freeze debugging (transparency, not a redesign)

Before this manifest was generated, a manual debugging pass (running the
reconstruction+scoring pipeline over all cases and eyeballing the
case-level metric table) surfaced and fixed two genuine implementation
bugs, neither of which changed any hypothesis, metric definition, case
structure, or regime definition:

1. **`_close_and_append` duplicate-row bug** (`src/cases.py`): closing out
   a superseded artifact appended the closed copy *and* the new row
   without removing the original, never-closed row from history. For
   PolicyVersion/AuthorityAssignment this was harmless (reconstruction
   always resolves via the *latest* `recorded_at` per identity, so the
   stale duplicate was never selected). For ModelVersion — which has no
   `recorded_at` field at all, by design (`domain.py`; no retroactive-
   correction case targets model version) — the stale duplicate created a
   genuine, unintended two-way match in Case 7's Regime B model-version
   query, incorrectly forcing `UNDETERMINED` and a spurious Authorization
   Correctness failure unrelated to any mechanism under test. Fixed by
   having `_close_and_append` replace the closed row in place rather than
   duplicating it (see the function's docstring for why this cannot
   change any policy/authority case's result).
2. **Over-strict Temporal Correctness check**: the initial scoring
   implementation required an investigator's reported `valid_to` to
   exactly equal a value that, for an artifact still open at t0, is only
   knowable in the future (e.g. Regime B correctly reporting policy v1's
   *eventual* close time after v2 legitimately supersedes it in Case 2,
   versus Regime C correctly reporting v1's still-open `valid_to=None` as
   it stood at decision time). `metrics-and-scoring.md` defines Temporal
   Correctness as naming "the version whose valid-time interval actually
   contained t0" — a statement about version identity and containment, not
   about reproducing a specific future-dependent timestamp. Scoring was
   corrected to check version-identity match plus self-consistent interval
   containment of t0, which is what the metric's own prose specifies. This
   is a bug fix against the written metric definition, not a metric
   redesign, and it was necessary for Case 2 (a case the design predicts
   B *should* pass) to be scored correctly at all.

No hypothesis, metric, case, or regime definition was changed by either
fix. Both are implementation-correctness fixes, made before this freeze
and before any case's outcome was treated as an experimental result. The
one open implementation decision the design explicitly leaves to the
implementer — Case 10's boundary-precision question
(`implementation-spec.md` Section 5/7) — was resolved in favor of the
"documented limitation" branch (clean, non-fault-injected half-open
interval semantics), not fault injection; this is recorded here, not
decided after seeing its effect on results, since the case's mechanical
behavior (whether the two decisions land on the correct side of the
boundary) follows directly and deterministically from that choice and was
verified structurally by `tests/test_case_integrity.py::test_case_10_boundary_is_implemented_as_documented_clean_semantics_not_fault_injection`
before this freeze.

## Locked research question

> Given complete independent version histories for policy, evidence,
> authority, model, and relevant context, does versioning alone suffice
> for temporally correct reconstruction of why a historical AI-mediated
> decision was authorized, or does explicit decision-time binding
> materially improve reconstruction?

Primary comparison: **Regime B (versioned, unbound) vs. Regime C
(versioned, bound)**. Regime A is a floor/manipulation-check condition
only, per `experiment-design/research-question.md`.

## Locked hypotheses

- **H0**: Explicit decision-time binding provides no meaningful
  reconstruction advantage over complete independent version histories
  (Temporal Correctness, False Historical Confidence).
- **H1**: Explicit decision-time binding materially improves Temporal
  Correctness and reduces False Historical Confidence, and this advantage
  is concentrated in Cases 3, 8, 9, 10 (retroactive/concurrency), not
  spread uniformly across all cases.

Full operational criteria: `experiment-design/research-question.md`.

## Locked regimes

- **A — Bare**: `DecisionOutcomeLog` only; live-only current values for
  policy/authority/model/watchlist at query time.
- **B — Versioned, unbound**: full bitemporal policy/authority history,
  full model/watchlist valid-time history, per-decision event trace of
  raw values read at t0. No decision→version-identifier binding.
- **C — Versioned, bound**: everything in B, plus one
  `DecisionBindingRecord` per decision, authored at t0.

Implementation: `src/regimes.py`. The B/C information-equivalence
invariant is machine-checked by `regimes.verify_b_c_equivalence`, run for
every case in `tests/test_regimes.py` (pre-execution) and again inline at
the start of every world's processing in `src/run_experiment.py::run`
(so a violation halts execution rather than producing results).

## Locked case matrix (10 structural cases, 11 decisions)

See `PRE-EXECUTION-case-manifest.json` (generated by
`python3 -m src.run_experiment --manifest`, structural metadata only —
no reconstruction or scoring was run to produce it) for the exact,
machine-readable case list. Categories: control (1), forward-drift (2,4,
5,6,7), retroactive-drift (3), combined-drift (8,9), concurrency (10, two
decisions D10x/D10y).

Manipulation-check case set (`src/cases.py::MANIPULATION_CHECK_CASE_IDS`):
Cases 2, 4, 6, 7.

## Locked reconstruction algorithm

`src/reconstruction.py::reconstruct`, one function shape per regime, same
structure across regimes, differing only in which artifacts the assigned
regime's view exposes. Documented completion of one spec gap (model
version / watchlist status resolution, not explicitly covered by
`implementation-spec.md`'s pseudocode): see the module docstring. This
completion does not affect either primary metric (TC, FHC), which
`metrics-and-scoring.md` scopes to Q4/Q6 (policy, authority) only.

## Locked scoring algorithm

`src/scoring.py::score_case` — Artifact Identification Accuracy (AIA),
Temporal Correctness (TC, primary), Authorization Correctness (AC),
Justification Completeness (JC), False Historical Confidence (FHC, primary
diagnostic), exactly as defined in `experiment-design/metrics-and-scoring.md`,
aggregated by perturbation category in `aggregate_by_category`.

## Expected interpretation table

Reproduced from `experiment-design/preregistered-interpretation.md` and
treated as fixed. The actual result must be mapped onto one of the 9 rows
below, or reported as an explicitly labeled unanticipated result if none
fits.

| # | Result pattern | Interpretation |
|---|---|---|
| 1 | C >> B on TC/FHC, concentrated in Cases 3,8,9,10; B ≈ C on 1,2,4,5,6,7 | Strong support |
| 2 | C >> B uniformly, including 2,4,6,7 | Support, but broader than predicted — check for a weak B algorithm first |
| 3 | C ≈ B in all categories, but both >> A | Thesis not supported as stated — push toward Verdict C |
| 4 | B >> A but C ≈ B, specifically on Cases 3 and 10 | Strongest possible disconfirmation of H1 |
| 5 | A ≈ B ≈ C across all categories | Ambiguous — run manipulation check first |
| 6 | C improves JC/AIA over B but not TC/FHC | Different mechanism than hypothesized (completeness, not temporal correctness) |
| 7 | C reduces FHC without improving raw AC | Partial support (epistemic honesty, not bottom-line correctness) |
| 8 | B fails Case 10 but succeeds Case 3, or vice versa | Partial mechanism confirmation — report which one |
| 9 | B succeeds Case 8 despite failing Case 3 | Internal inconsistency requiring debugging, not interpretation |

## Confirmation

No case-level or aggregate result produced by the frozen algorithms above
(`src/reconstruction.py`, `src/scoring.py` as they exist at this commit)
has been used to alter any hypothesis, metric, case, or regime definition
after this point. The pre-freeze debugging pass described above fixed two
implementation bugs against the written specification; it did not tune
toward any outcome, and both fixes are disclosed above rather than
silently folded in. The formal run that produces
`results/raw_results.jsonl` is executed fresh after this manifest is
written, via `python3 -m src.run_experiment`, with no code changes in
between.
