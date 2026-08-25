---
id: note-contribution-03-experiment-research-question
title: "Contribution 3 Experiment — Research Question and Hypotheses"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, experiment, research-question]
refs: [../composition-review.md, ../generalization-from-c2.md, ../FINAL-RESEARCH-VERDICT.md]
---

## Primary research question

> If every individual decision in a multi-step AI-mediated trajectory is
> uniquely reconstructable from the retained record (Contribution 2's G1
> property, achieved perfectly, unconditionally, for every decision in
> this experiment), is the trajectory itself **necessarily** uniquely
> reconstructable?

## Trajectory, defined

A trajectory is an ordered sequence of decisions D1, D2, ..., Dn, where a
later decision may depend on an output or state transition produced by
an earlier one. Trajectory reconstruction is **not** sorting decisions
by timestamp — it additionally requires recovering:

1. which decisions occurred (trivial, always retained);
2. the local context and result of each decision (Contribution 2's own
   object — guaranteed perfect here, not re-tested);
3. the dependency edges between decisions (which earlier decision, if
   any, each later decision actually consumed);
4. the execution/causal order, where distinguishable from local records
   alone;
5. whether the resulting dependency graph is the unique one consistent
   with the retained record, or whether multiple globally different
   graphs remain compatible with it.

## Hypotheses (locked before implementation)

**H0:** If every decision is individually reconstructable, the complete
trajectory is also reconstructable from the union of those decision
records.

**H1:** There exist systems in which every decision is individually
reconstructable, but multiple globally different trajectories remain
compatible with the retained decision-local records.

## Local vs. global information, cleanly separated

**Local** (present in every regime, every case, guaranteed correct):
decision ID, observable decision time, exact consumed context (a
placeholder field standing in for Contribution 2's model/policy/
evidence/authority/config versions — not re-tested here), the raw output
value a decision produces (if any), the raw input value a decision
consumes (if any), and the decision's own result.

**Global** (present only in Regime T2, and — for exactly one disclosed
negative-control case — as an ordinary trace field in Regime T1):
an explicit record of which specific earlier decision's output a later
decision actually consumed.

The experiment tests whether *this one class of cross-decision relation*
is required for trajectory-level reconstruction, holding every local
fact fixed and identical between regimes.

## Why this is not a re-test of Contribution 2

Contribution 2 tested whether a *single* decision's consumed context
(which policy/authority/evidence/model version) is reconstructable. That
property is held **unconditionally true** in every case and regime of
this experiment — verified directly, before execution
(`tests/test_local_reconstruction.py`) — so any observed failure here
cannot be attributed to Contribution 2's mechanism recurring. This
experiment tests a structurally different property: not "which version
did this decision use," but "which earlier decision did this decision
depend on."

## Relationship to `generalization-from-c2.md`

This experiment is the empirical test `../generalization-from-c2.md`
identified as required before G3 (trajectory reconstructability) could
be assessed as anything other than "requires new evidence." It does not
test G4, G5, or G6 (deployed-system-state, behavioral-envelope, or
operator-knowledge reconstructability) — those remain out of scope, per
`../FINAL-RESEARCH-VERDICT.md`'s own conservative boundary.
