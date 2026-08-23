# Follow-up Case 10 — Locked Research Question and Hypotheses

## Question

> If the temporal information available to a reconstruction procedure
> identifies multiple historically plausible artifact versions, can
> version history alone recover the actual decision context, or does
> explicit decision-time binding provide information that cannot be
> inferred from the available temporal record?

This is deliberately narrower than the primary experiment's question. It
does not ask whether versioning helps in general (settled), and it does
not ask about retroactive correction (already tested by the primary
experiment, Cases 3/8/9). It asks specifically: when the *observable*
temporal record is genuinely insufficient to distinguish which of several
version-boundary-adjacent artifacts applied, does anything other than an
explicit, decision-time-authored binding resolve that insufficiency.

## Hypotheses (locked before implementation)

**H0-F10**: Under controlled timestamp/ordering ambiguity, complete
version histories without explicit decision-time binding (Regime B)
achieve the same temporal reconstruction correctness as explicit
decision-time binding (Regime C).

**H1-F10**: Under controlled timestamp/ordering ambiguity, explicit
decision-time binding improves temporal reconstruction correctness,
because version history alone cannot uniquely identify the artifact
context actually used by the decision.

**Operational criterion**: H1-F10 is supported if, on cases where the
observable record is genuinely ambiguous (F10-2 through F10-5), Regime C
achieves Correct-Unique reconstruction on the ambiguous dependency while
Regime B does not (either because B correctly reports `AMBIGUOUS`, which
is an honest non-failure distinct from being wrong, or because B is
`WRONG_UNIQUE`, a genuine failure) — while both B and C achieve Correct-
Unique reconstruction on the non-ambiguous control (F10-1). H0-F10 is not
falsified if B also achieves Correct-Unique reconstruction on the
ambiguous cases (i.e., the observable record, despite the constructed
bucket overlap, turns out not to actually underdetermine the answer for
B's algorithm) or if B's failure mode there is indistinguishable in kind
from C's.

## What this follow-up does not test (out of scope, by the mechanism
choice in `case-matrix.md`)

- Clock skew between components (mechanism B in the original task
  framing) — a different, more complex fault model, not needed to test
  the core question.
- Missing causal relation in the general, open-ended sense (mechanism D)
  — narrowly probed only by the F10-6 negative control, not the subject
  of H0-F10/H1-F10 themselves.
- Retroactive correction — already tested by the primary experiment.
  No follow-up case uses a backdated `valid_from` or a corrected
  `recorded_at`; this is verified by `tests/test_case_integrity.py`.

## Formulations this result will be used to distinguish

Stated here, before execution, per the authorizing instructions (Step
15), so the mapping from result to formulation cannot be chosen after
seeing which one is flattering:

- **Formulation A** — Explicit decision-time binding is required for
  reconstruction under temporal ambiguity. (Supported if C succeeds where
  B is AMBIGUOUS or WRONG on every ambiguous case, and F10-6's causal
  event does *not* let B match C.)
- **Formulation B** — Some preserved causal relation between decision and
  context is required; explicit decision binding is one implementation,
  not the only one. (Supported if F10-6 shows B-with-a-causal-event
  matches C's performance.)
- **Formulation C** — Complete temporal/event history already suffices;
  explicit binding adds no meaningful reconstruction value under
  ambiguity. (Supported if B matches C on F10-2 through F10-5 without any
  causal-event enrichment.)
- **Formulation D** — Inconclusive. (If results do not cleanly separate
  the above, or if the manipulation/construction checks in
  `PRE-EXECUTION-MANIFEST.md` fail.)

The narrowest formulation actually supported by the data is reported,
per Step 15's explicit instruction not to protect Formulation A if B
succeeds.
