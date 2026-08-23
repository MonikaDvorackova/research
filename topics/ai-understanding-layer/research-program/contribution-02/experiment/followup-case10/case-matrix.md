# Follow-up Case 10 — Case Matrix (locked before implementation)

## Mechanism selection (Step 3)

Selected: **A — timestamp precision loss.** A decision's true moment
(`true_t0`) is known only to ground truth, at microsecond precision. The
*observable*, persisted decision timestamp (`observed_t0`) is truncated
down to whole-second precision. This models a realistic, common logging
practice (many systems log request timestamps at second granularity) and
is the smallest mechanism that can produce genuine, non-manufactured
ambiguity: when a version-boundary instant falls strictly inside the
one-second observable window `[observed_t0, observed_t0 + 1s)`, no
amount of correct querying over the observable record can determine which
side of the boundary the decision's true moment actually fell on — not
because the data is missing, but because the data that *would*
disambiguate it (sub-second decision timing) was never observable in the
first place.

**Why not clock skew (B), general ordering ambiguity (C), or missing
causal relation (D) as the primary mechanism:** clock skew requires
simulating multiple components with independent, bounded-offset clocks —
a materially more complex fault model whose ambiguity is a composite of
skew magnitude *and* precision, harder to isolate cleanly. General
ordering ambiguity (C) is a generalization of precision loss for this
single-timeline system with one decision at a time; precision loss alone
already produces it without needing a second concurrent timeline. Missing
causal relation (D) is not a fault mechanism at all — it is the absence of
Regime C's own binding, which is not a variable to combine into B's
ambiguity condition, and is separately, deliberately probed by F10-6 as a
negative control rather than folded into the primary mechanism. Combining
mechanisms would make any observed effect harder, not easier, to
attribute — Step 3 explicitly asks for the smallest sufficient mechanism.

`precision = 1 second`. `observed_t0 = floor(true_t0, precision)`.
Regime A/B never receive `true_t0`, only `observed_t0` (see
`../PRE-EXECUTION-MANIFEST.md`'s equivalence checks). Regime C's binding
is authored using `true_t0` (i.e., at the moment of the decision itself,
which by construction had access to its own true moment even though the
system's outcome/event log only ever persisted `observed_t0`) — this
mirrors the primary experiment's Regime C exactly (binding authored at
decision time, not retrofitted).

All boundary instants below fall strictly inside `[observed_t0,
observed_t0 + 1s)` by construction (`observed_t0 = 12:00:00`, boundary =
`12:00:00.500000`), and `true_t0 = 12:00:00.750000` is always strictly
after the boundary in every ambiguous case, so ground truth always
resolves to the *later* (v2 / Agent-2 / m2) candidate. No case is
retroactive: every boundary is authored once, forward, never corrected.

| Case | Ambiguous dimension(s) | Policy | Authority | Model | True t0 | Ground truth |
|---|---|---|---|---|---|---|
| **F10-1** | none (control) | v1 (θ=0.50), wide-open | Agent-1, wide-open | m1 (w1=w2=0.5), wide-open | 12:00:00.200 | v1 / Agent-1 / m1, score 0.41, GRANT |
| **F10-2** | policy only | v1→v2 (θ=0.30) at boundary 12:00:00.500 | Agent-1, wide-open | m1, wide-open | 12:00:00.750 | **v2** / Agent-1 / m1, score 0.41, **DENY** (0.41 ≥ 0.30) |
| **F10-3** | authority only | v1 (θ=0.50), wide-open (unperturbed) | Agent-1→Agent-2 at boundary 12:00:00.500 | m1, wide-open | 12:00:00.750 | v1 / **Agent-2** / m1, score 0.41, GRANT |
| **F10-4** | model/config only | v1 (θ=0.50), wide-open (unperturbed) | Agent-1, wide-open | m1→m2 (w1=0.2,w2=0.8) at boundary 12:00:00.500 | 12:00:00.750 | v1 / Agent-1 / **m2**, score 0.404, GRANT |
| **F10-5** | policy + authority | v1→v2 at 12:00:00.500 | Agent-1→Agent-2 at 12:00:00.500 | m1, wide-open | 12:00:00.750 | **v2** / **Agent-2** / m1, score 0.41, **DENY** (0.41 ≥ 0.30) |
| **F10-6** | policy only, **+ causal event given to B** | v1→v2 at 12:00:00.500 (identical to F10-2) | Agent-1, wide-open | m1, wide-open | 12:00:00.750 | **v2** / Agent-1 / m1, score 0.41, **DENY** (0.41 ≥ 0.30) |

Note: the evidence baseline (`account_age_norm=0.42, prior_incidents_norm=0.40`,
score 0.41 under m1's weights) was fixed once across all six cases for
comparability. Under v1's threshold (0.50) this is GRANT; under v2's
threshold (0.30) this is DENY. This is incidental to what the matrix
tests (temporal/version identification and ambiguity detection, not the
authorization outcome itself) and is stated here precisely so the
authorization-correctness metric's expected values are unambiguous before
execution, not adjusted after seeing them.

Evidence is fixed across every case (`account_age_norm=0.42,
prior_incidents_norm=0.40`) and never itself ambiguous — evidence has no
version-interval table in this design (matching the primary experiment;
see `preservation-regimes.md`), so it is not a candidate dimension for
observational-precision ambiguity here.

## F10-6's negative control, precisely

B receives one additional field on its event trace: a
`causal_consumption_event` recording `{"policy_version_id": "v2"}` — the
version the request handler actually consulted, logged as an ordinary
consumption event, not framed, named, or structured as a
`DecisionBindingRecord`. This is deliberately the minimal signal
sufficient to disambiguate, so that if B-with-this-event matches C, the
honest conclusion is that *any* causal linkage suffices, not specifically
Regime C's binding schema (`research-question.md`, Formulation B).

C in F10-6 is unchanged from every other case — it still only has its
standard `DecisionBindingRecord`. F10-6 is the one case in this matrix
where B, not C, receives an extra artifact; this is disclosed here and
in `PRE-EXECUTION-MANIFEST.md`'s equivalence-check section, which
verifies the B/C equivalence invariant holds unmodified for F10-1..F10-5
and is explicitly, separately exempted only for F10-6.

## Expected difficulty (a priori, checked against actual scoring, not
asserted as foregone)

- F10-1: both B and C fully correct, unique, no ambiguity flagged.
- F10-2 through F10-5: C fully correct and unique on the ambiguous
  dimension(s) (via binding); B expected to correctly report `AMBIGUOUS`
  on the ambiguous dimension(s) specifically (not `WRONG_UNIQUE` — the
  bucket-overlap query never guesses, per `../reconstruction-task.md`'s
  discipline, reused here) and remain correct/unique on the
  non-ambiguous dimension(s).
- F10-6: tests whether B, once given *any* causal consumption signal,
  matches C's Correct-Unique result — the answer is not assumed here.
