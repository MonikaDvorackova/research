# Contribution 2 Reconstruction Experiment — Report

Execution date: 2026-08-23. Implementation: `../src/`. Raw output:
`../results/raw_results.jsonl`. This report follows the pre-registered
interpretation table frozen in `../PRE-EXECUTION-MANIFEST.md` before this
run was executed.

# Research question

> Given complete independent version histories for policy, evidence,
> authority, model, and relevant context, does versioning alone suffice
> for temporally correct reconstruction of why a historical AI-mediated
> decision was authorized, or does explicit decision-time binding
> materially improve reconstruction?

Primary comparison: Regime B (versioned, unbound) vs. Regime C (versioned,
bound). Regime A is a floor/manipulation-check condition only.

# Hypotheses

- **H0**: explicit decision-time binding provides no meaningful
  reconstruction advantage over complete independent version histories.
- **H1**: explicit decision-time binding materially improves Temporal
  Correctness and reduces False Historical Confidence, concentrated in
  cases involving retroactive correction or concurrency ambiguity (Cases
  3, 8, 9, 10), not spread uniformly.

# Experimental setup

Synthetic "Tier-2 Access Advisor" system (`experiment-design/experimental-system.md`).
Deterministic decision rule; deterministic, rule-based reconstruction
procedure (no human or LLM investigator), applied identically in structure
across regimes, differing only in which artifacts each regime's view
exposes (`src/reconstruction.py`).

# Preservation regimes

- **A — Bare**: outcome log only; live-only current values at query time.
- **B — Versioned, unbound**: full bitemporal policy/authority history,
  full model/watchlist valid-time history, a per-decision event trace of
  raw values read at t0. No decision→version-identifier binding.
- **C — Versioned, bound**: everything in B plus one
  `DecisionBindingRecord` per decision, authored at t0.

The B/C information-equivalence invariant (C adds no new fact, only a
reference to facts already in B) was machine-checked for every case before
scoring (`src/regimes.py::verify_b_c_equivalence`, run inline in
`run_experiment.py` and in `tests/test_regimes.py`); it held for all 11
decisions with no exceptions.

# Case matrix

Ten structural cases (11 decisions; Case 10 has two), per
`experiment-design/perturbation-matrix.md`: 1 control, 5 forward-drift
(2, 4, 5, 6, 7), 1 retroactive-drift (3), 2 combined-drift (8, 9), 1
concurrency (10). Exact parameters: `PRE-EXECUTION-case-manifest.json`.

# Metrics

Artifact Identification Accuracy (AIA), Temporal Correctness (TC,
primary), Authorization Correctness (AC), Justification Completeness
(JC), False Historical Confidence (FHC, primary diagnostic), exactly as
defined in `experiment-design/metrics-and-scoring.md`, computed per case
per regime and aggregated by perturbation category (never pooled) in
`src/scoring.py`.

# Results

Full tables: `results-summary.md`. Headline numbers:

| Category | B: TC / FHC | C: TC / FHC |
|---|---|---|
| control (1) | 1.00 / 0.00 | 1.00 / 0.00 |
| forward-drift (2,4,5,6,7) | 1.00 / 0.00 | 1.00 / 0.00 |
| retroactive-drift (3) | **0.00** / **0.50** | 1.00 / 0.00 |
| combined-drift (8,9) | **0.00** / **0.63** (avg) | 1.00 / 0.00 |
| concurrency (10) | 1.00 / 0.00 | 1.00 / 0.00 |

Manipulation check (Step 0) passes: Regime A is measurably worse than
both B and C on AC and AIA across all four forward-drift cases, and on TC
specifically on the two of those cases where policy/authority themselves
drift (see `results-summary.md`). The case matrix has genuine drift bite.

# B vs C primary comparison

**On Cases 1, 2, 4, 5, 6, 7 (control + all forward-drift): B and C are
identical (TC = 1.00, FHC = 0.00, both regimes, every case).** Complete,
competently implemented bitemporal history is sufficient by itself when
drift is forward and non-retroactive. This is not a weak or partial
match to the design's prediction — it is exact.

**On Cases 3, 8, 9 (retroactive/combined-retroactive drift): C strictly
and categorically dominates B.** B's Temporal Correctness drops to 0.00 on
all three; C's stays at 1.00. B's False Historical Confidence rises to
0.50–1.00 on these cases (a concrete, wrong, confidently-stated policy
and/or authority version); C's stays at 0.00. The failure tracks exactly
the theorized mechanism: B's as-of-t0 bitemporal query is objectively
correct in its logic, and still returns the wrong version, because a
retroactive correction recorded after t0 changes what "the latest known
truth about t0" is. Binding, fixed at decision time and never
retroactively alterable, does not have this instability by construction.

**On Case 10 (concurrency): B and C are identical (both succeed).** This
diverges from `perturbation-matrix.md`'s a priori forecast that B "is
expected to risk misattribution." The reason is disclosed and was fixed
before execution (`PRE-EXECUTION-MANIFEST.md`): this implementation models
the policy boundary with exact, non-fault-injected timestamps, so there is
no genuine ambiguity for B's query to fail on. This case, as built, does
not test the concurrency-ambiguity mechanism at all — it is untested here,
not disconfirmed.

# False Historical Confidence

FHC is the sharpest result in this run. On Cases 3, 8, and 9, Regime B
does not fail by going silent (`UNDETERMINED`) — it fails by confidently
naming a concrete, wrong policy and/or authority version, exactly the
"reconstruction that looks complete and confident but is silently wrong"
failure mode the design's primary diagnostic metric exists to catch.
Regime C's FHC is 0.00 in every single case, with no exception. This is
the cleanest evidence in the run that binding's advantage is not merely
about raw correctness but specifically about converting a plausible,
undetectable wrong answer into either a correct answer or an honest
abstention — and in this run it is always a correct answer, never an
abstention, because C's binding resolves the reference directly, with no
inferential step that could fail.

# Failure taxonomy

Every Regime B failure (Cases 3, 8, 9) is a **conflicting valid-time /
transaction-time interpretation**, caused by a **missing binding** — never
"insufficient underlying evidence" (B's bitemporal history genuinely
contains all the facts; the query is simply misled) and never a
"reconstruction-algorithm limitation" (the query implements the
objectively correct valid-time semantics; a smarter algorithm applied to
the same data cannot recover the truth once the transaction-time record
itself has been altered). Full per-case breakdown: `results-summary.md`.

# Prior-art interpretation

- **Did strong bitemporal history suffice?** No — not once a retroactive
  correction is recorded. It fully sufficed for every non-retroactive
  case (1, 2, 4, 5, 6, 7), confirming Regime B was not strawmanned.
- **Did event sourcing suffice?** Partially, and precisely along the line
  `preservation-regimes.md` predicted: B's per-decision event trace
  captures raw evidence and watchlist *values*, and this fully protected
  Case 5's evidence-supersession scenario without any binding. It does
  not capture a model or policy *version identifier*, and policy/authority
  identification is exactly where the retroactive-correction failures
  occurred. This is the exact, narrow distinction the design's event-
  sourcing section anticipated: capturing values is not the same
  discipline as capturing version identifiers at consultation time, and
  the difference is measurable, not merely definitional.
- **Did explicit provenance linkage collapse B into C?** No, by
  construction — B never contains a decision→version-identifier reference,
  which is the one property the equivalence check confirms is exclusive
  to C.
- **Does C merely instantiate existing provenance semantics?** Yes,
  exactly as `preservation-regimes.md` already conceded before this run;
  nothing in this run's results contests that concession.
- **Is the surviving contribution mechanism novelty, synthesis, or
  empirical demonstration?** Empirical demonstration. This run is the
  first point in the research programme where "binding is behaviorally
  consequential, not just conceptually distinct" has direct, measured
  support — narrowly, for the retroactive-correction mechanism, in a
  synthetic controlled setting.

# Threats to validity

Unchanged from `experiment-design/validity-and-confounders.md`, with one
addition specific to this run's results: **the concurrency-ambiguity
mechanism (Case 10) was not actually exercised**, because this
implementation chose exact timestamp semantics over fault injection (a
disclosed, pre-registered-as-open choice, not a post hoc excuse). Any
claim this run supports about binding's necessity is therefore properly
scoped to the retroactive-correction mechanism only, not to concurrency
ambiguity — construct validity for the concurrency half of H1 was not
established one way or the other by this run.

# Conclusion

The pattern most closely matches pre-registered row 1 (strong support),
restricted specifically to the retroactive-correction mechanism (Cases 3,
8, 9), where it is an exact, clean match: C dominates B categorically, the
non-drift and forward-drift cases show B ≈ C exactly as the row requires,
and the manipulation check passes. It does not match row 1 in full,
because row 1 also predicts the gap on Case 10, and Case 10 shows B ≈ C
here — not because the mechanism is false, but because this run's Case 10
never tested it. This combination — one of the two theorized mechanisms
strongly confirmed, the other genuinely untested rather than
disconfirmed — is closest to pre-registered row 8's shape ("one mechanism
real, the other not demonstrated by this design"), applied to an
implementation choice rather than to the case's structural design.

**Final interpretation: PARTIAL SUPPORT.** Not "strong support" across the
full H1 claim, because Case 10 does not contribute the evidence H1's
operational criterion asks it to contribute. Not "null," "against
thesis," or "inconclusive/design failure," because the manipulation check
passes cleanly and the retroactive-correction half of H1 is confirmed with
an unambiguous, categorical result, not a marginal or noisy one.

# What the result supports

- In this synthetic, controlled system: when a policy or authority record
  is retroactively corrected after a decision was made, a competently
  implemented bitemporal query — even one using genuinely correct
  valid-time semantics over a genuinely complete history — can be
  confidently and silently wrong about which version actually applied at
  decision time.
- An explicit, decision-time binding, fixed at t0 and never retroactively
  alterable, avoids this specific failure by construction, in this system,
  for this mechanism.
- Capturing raw values in an event trace (a real, strong event-sourcing
  practice) is not the same discipline as capturing version identifiers,
  and the difference between them is measurable, not merely definitional:
  it fully protected evidence-supersession (Case 5) but did not protect
  policy/authority identification under retroactive correction.

# What the result does NOT support

- That the concurrency-ambiguity mechanism (the second half of the
  bitemporal-collision argument in `preservation-regimes.md`) is real or
  unreal — it was not tested by this run.
- That this finding generalizes beyond this synthetic testbed to real
  production AI systems, their prevalence, their severity, or their
  directionality (`validity-and-confounders.md`'s external-validity
  section, unchanged and unaddressed by this run).
- That explicit binding is universally necessary, that all AI systems
  have this problem, that compliance is improved, or that trustworthiness
  is proven. This is a synthetic, controlled, ten-case diagnostic study.
- That Regime B is representative of typical current AI/ML tooling — it
  was deliberately built stronger (fully bitemporal, fully event-sourced)
  than the prior-art audit found typical tooling to be, specifically so
  that any observed B-vs-C gap could not be attributed to underpowering B.

# Consequence for Contribution 2

See `../../novelty-verdict.md`'s appended post-experiment update for the
full statement. Summary: this run narrows and empirically grounds, rather
than broadens, the surviving thesis. The retroactive-correction half of
"versioned is not bound" now has direct empirical support in a controlled
setting; the concurrency-ambiguity half remains an open, undemonstrated
claim requiring a follow-up run with genuine timestamp-precision fault
injection before it can be reported as tested one way or the other.
