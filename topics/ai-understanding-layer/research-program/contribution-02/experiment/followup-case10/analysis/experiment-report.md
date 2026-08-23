# Follow-up Case 10 — Report

Execution date: 2026-08-23. Implementation: `../src/`. Raw output:
`../results/raw_results.jsonl`. Follows the pre-registered interpretation
table frozen in `../PRE-EXECUTION-MANIFEST.md` before this run.

# Research question

> If the temporal information available to a reconstruction procedure
> identifies multiple historically plausible artifact versions, can
> version history alone recover the actual decision context, or does
> explicit decision-time binding provide information that cannot be
> inferred from the available temporal record?

# Hypotheses

- **H0-F10**: complete version histories without explicit binding achieve
  the same temporal reconstruction correctness as binding, under
  controlled timestamp/ordering ambiguity.
- **H1-F10**: binding materially improves temporal reconstruction
  correctness under such ambiguity.

# Experimental setup

Mechanism: timestamp precision loss (`case-matrix.md`). A decision's true
moment is truncated to whole-second precision before being persisted;
Regime B/C only ever see the truncated `observed_t0`. When a
policy/authority/model version boundary falls inside the resulting
one-second observable window, no amount of correct querying over complete
history can determine, from timing alone, which side of the boundary the
decision's true moment fell on. Not retroactive correction (already
tested by the primary experiment) — no case here backdates a
`valid_from` or corrects a `recorded_at`.

# Preservation regimes

Regime B (versioned, unbound) and Regime C (versioned, bound) only —
Regime A out of scope by disclosed choice (`research-question.md`). B/C
equivalence machine-checked for all six cases, with one disclosed
exemption: F10-6 gives B (never C) one additional field, a
`causal_consumption_event`, as a deliberate negative control.

# Case matrix

Six cases: F10-1 (no-ambiguity control), F10-2/F10-3/F10-4 (isolated
policy/authority/model ambiguity), F10-5 (combined policy+authority
ambiguity), F10-6 (negative control: F10-2's ambiguity plus a
non-binding causal event given to B only). Exact parameters:
`case-matrix.md`, `PRE-EXECUTION-case-manifest.json`.

# Metrics

Temporal Correctness (TC, scoped to policy+authority, matching the
primary experiment), Unique Reconstruction Rate (URR, all three
dependencies), Ambiguity Detection Rate (ADR, ground-truth-ambiguous
dimensions only), Authorization Correctness (AC), False Historical
Confidence (FHC) — with `AMBIGUOUS` explicitly and structurally excluded
from FHC (`src/scoring.py`).

# Results

Full tables: `results-summary.md`. Headline: B never produces a
confidently wrong answer anywhere in this run (FHC = 0.00 on all 12
case-regime rows). Where the observable record is genuinely ambiguous, B
correctly says so (ADR = 1.00 throughout F10-2..F10-5) rather than
guessing. C resolves every case correctly and uniquely via its binding.
F10-6 shows this specific failure mode is not fixed by binding alone
being possible — it is fixed by *any* signal connecting the decision to
the version it actually consumed, whether or not that signal is called
"binding."

# B vs C primary comparison

**F10-1: identical, both fully correct.** Ordinary reconstruction ability
is untouched.

**F10-2, F10-3, F10-5 (ambiguity present, no causal signal): C
categorically dominates B on TC, URR, and AC**, while **FHC stays at 0.00
for B on every one of them** — this is not a "B is wrong" result, it is a
"B is honestly stuck, C is not" result, and the distinction is load-bearing
for what this run can claim.

**F10-4: same honest-ambiguity pattern, but on the one dependency (model)
TC does not score.** URR (0.67 for B vs. 1.00 for C) is what actually
shows this case's effect; TC alone would have hidden it entirely, which
is exactly why URR was specified as a separate metric before execution.

**F10-6: B matches C exactly, once given a non-binding causal
consumption event.** This is the single most important result in this
follow-up.

# Ambiguity Detection

Regime B's Ambiguity Detection Rate is 1.00 on every case where ground
truth records a genuinely ambiguous dimension (F10-2 through F10-5), and
0.00 (correctly — nothing to detect) on F10-1 and F10-6. The
bucket-overlap query never guesses through unresolved ambiguity: it is
architecturally the same "never force a confident answer" discipline the
primary experiment already used for its `UNDETERMINED` token, applied
here with the additional precision Step 7 required (distinguishing an
honest multi-candidate report from a data-absence report).

# False Historical Confidence

Zero, everywhere, in this run — for both regimes, on every case. This is
a meaningfully different profile from the primary experiment, where
Regime B's retroactive-correction failures *were* confidently wrong
(FHC up to 1.00 on Cases 8/9). Here, under a precision-loss mechanism
rather than a retroactive-correction mechanism, Regime B's bucket-overlap
query has no way to be confidently wrong — a boundary either falls inside
the observable window (producing an honest `AMBIGUOUS`) or it does not
(producing a correct `UNIQUE`). This is a structural property of the
precision-loss mechanism as implemented here, not a general claim that
precision loss can never produce false confidence under a different
query design (e.g., one that resolved ties by picking the most recent
candidate instead of reporting ambiguity would reintroduce FHC risk —
this implementation deliberately does not do that, per Step 7).

# Negative control result (F10-6)

The result is unambiguous: Regime B, given `{"policy_version_id": "v2"}`
as an ordinary event-trace field (never named, structured, or framed as
a "decision binding"), achieves `CORRECT_UNIQUE` on the same dependency
that was `AMBIGUOUS` in the structurally identical F10-2. Every metric
(TC, URR, AC, FHC) becomes identical to Regime C's. This is the outcome
`case-matrix.md` flagged in advance as the one this follow-up was
genuinely unsure about, and it resolved in the direction that narrows the
thesis: **the operative requirement is a preserved causal relation from
decision to consumed version, not specifically a schema named
"binding."**

# Which formulation survives (Step 15)

- **Formulation A** (binding specifically required): **not** the
  narrowest formulation supported — F10-6 directly contradicts the
  "specifically" in this formulation.
- **Formulation B** (some preserved causal relation required; binding is
  one implementation): **supported**, and is the narrowest formulation
  consistent with all six results. F10-2 through F10-5 show that version
  history without *any* causal signal fails to uniquely resolve genuine
  ambiguity (supporting H1-F10 over H0-F10 in the "no signal at all"
  case); F10-6 shows that the specific signal does not need to be
  Regime C's `DecisionBindingRecord` schema to work.
- **Formulation C** (history alone always suffices): **not** supported —
  contradicted directly by F10-2, F10-3, F10-5's honest-but-unresolved
  `AMBIGUOUS` results, which are not `CORRECT_UNIQUE`.
- **Formulation D** (inconclusive): **not** applicable — the pattern is
  clean and consistent across all six cases, with no internal
  contradiction requiring debugging before interpretation.

Per the authorizing instructions' explicit direction not to protect
Formulation A if B succeeds: it does not survive as the narrowest
account. Formulation B does.

# Threats to validity

Same synthetic/controlled scope limitations as the primary experiment
(`../experiment-design/validity-and-confounders.md`), unchanged and not
revisited here. Specific to this follow-up: only one precision magnitude
(1 second) and one boundary offset (0.5s into a 1s bucket) were tested;
whether the ambiguity/no-ambiguity boundary behaves consistently at other
magnitudes was not explored, and should not be assumed from this single
setting. F10-6's causal event was constructed to always name the
*correct* consumed version — this follow-up does not test what happens
if a causal-event-style signal is itself unreliable, incomplete, or
contested (a materially different question from the one asked here).

# Conclusion

The precision-loss mechanism — the concurrency-ambiguity half of the
original thesis left untested by the primary experiment's Case 10 — is
now directly, cleanly demonstrated: complete version history without any
decision-to-version causal signal does not suffice for unique temporal
reconstruction under observable timestamp-precision loss, and it fails
honestly (as ambiguity) rather than confidently (as a wrong answer) in
this implementation. The negative control narrows the explanation: what
resolves the ambiguity is a preserved causal relation from decision to
consumed version, of which Regime C's explicit binding is one sufficient,
buildable, disclosed implementation — not a uniquely necessary one.

# What the result supports

- In this synthetic system, under timestamp-precision loss specifically,
  complete bitemporal/valid-time version history alone does not uniquely
  resolve which version a decision actually consumed, when a version
  boundary falls inside the decision's observable timestamp bucket.
- The reconstruction procedure used here fails this scenario honestly
  (reporting ambiguity, never a confident wrong answer) rather than
  falsely — a materially better failure mode than the primary
  experiment's retroactive-correction result, and worth reporting as its
  own finding, not folded into a single undifferentiated "B fails" claim.
- Any preserved causal signal connecting a decision to the specific
  version it consumed — not specifically a schema named "decision
  binding" — resolves this ambiguity. Explicit binding is a legitimate,
  general, systematic way to guarantee this signal exists for every
  decision; it is not shown here to be the only way.

# What the result does NOT support

- That "decision-time binding," specifically as Contribution 2's named
  schema, is uniquely necessary — F10-6 is direct evidence against that
  specific, narrower claim.
- Generalization beyond this synthetic testbed, this one precision
  magnitude, or this one boundary offset.
- Anything about clock skew, general concurrent ordering ambiguity across
  multiple independent timelines, or unreliable/contested causal signals
  — none of these were tested here (`research-question.md`'s explicit
  scope boundary).

# Consequence for Contribution 2

See `../../novelty-verdict.md`'s follow-up-dated update. Summary: this
result closes the primary experiment's one disclosed empirical gap
(Case 10) and, in doing so, narrows the surviving thesis from "explicit
decision-time binding is required" to "a preserved causal relation from
decision to consumed version is required, and explicit binding is one
general, buildable way to guarantee it." This is a scientifically
stronger, more defensible, and more precisely scoped claim than the one
it replaces.
