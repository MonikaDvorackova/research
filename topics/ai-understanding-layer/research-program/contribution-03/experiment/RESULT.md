# RESULT — Trajectory-Composition Experiment

**Proposition tested:** Per-decision reconstructability does not
necessarily compose into trajectory-level reconstructability.

**H0** (composes) vs. **H1** (does not necessarily compose) — locked in
`PRE-EXECUTION-MANIFEST.md` before execution.

## Verdict

**H1 SUPPORTED.**

- Local Decision Reconstruction: **1.00** in both regimes, all 6 cases
  (required precondition for validity — confirmed, see
  `analysis/results-summary.md`).
- Trajectory Identifiability: **1.00 under T2**, **0.33 (2/6) under
  T1** — despite T1 and T2 being field-for-field identical on every
  local fact (`verify_t1_t2_local_equivalence`, enforced both as a
  pre-execution test and at the start of every execution run).
- The four T1 failures (C3-2, C3-3, C3-4, C3-5) are exactly the four
  cases built around a cross-decision ambiguity mechanism; control
  (C3-1) and negative control (C3-6) both resolved correctly.
- **No false confidence occurred**: Dependency Edge Accuracy = 1.00,
  False Global Confidence Rate = 0.00 under T1. Every unresolved case
  was honestly reported AMBIGUOUS, never guessed.

Interpretation category (per the pre-registered table): **B** — a clean
composition gap attributable specifically to the missing cross-decision
relation, with zero instances of category C (false confidence).

## Relationship to Contribution 2

Same family of finding as Contribution 2's "retained is not consumed"
result (structural completeness does not guarantee the specific relation
a use case requires), one level up: trajectory vs. single decision. This
run's absence of false confidence is a genuine, disclosed difference
from Contribution 2's Case 8 finding (false historical confidence did
occur there) — attributable to testing a different mechanism, not to
this result being "better" in some general sense (see Limitations in
`analysis/experiment-report.md`).

## Article 3 consequence

Technical article **survivable**, narrowly: trajectory reconstructability
requires an explicit retained cross-decision relation, not merely more
per-decision detail. Must use "trajectory reconstructability" /
"compositional reconstructability" framing only — no "Understanding
Layer," no "capability-vs-understanding" (per this pass's binding
instruction and the prior novelty verdict demoting that framing to
metaphor).

## Contribution 3 empirical phase

**CLOSED**, pending Article 3 drafting authorization (not authorized in
this pass).

## Full detail

See `analysis/results-summary.md` (raw-data walkthrough) and
`analysis/experiment-report.md` (narrative, prior-art interpretation,
scientific limitations).
