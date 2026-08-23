---
id: note-contribution-02-experiment-readme
title: "Contribution 2 — Reconstruction Experiment Design (Index)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, index]
refs: []
---

## Contribution 2 Reconstruction Experiment — Design Index

**Status: design complete. Not implemented. Not executed. No results
exist.**

This directory operationalizes the empirical next step identified in
`../empirical-next-step.md` and `../novelty-verdict.md` (Verdict B —
narrowed survival) into a concrete, falsifiable experiment design. It does
not implement or run anything.

## Reading order

1. `research-question.md` — the locked primary empirical question, H0/H1,
   and why this is a pre-registered diagnostic design rather than a
   significance test.
2. `experimental-system.md` — the unit of analysis and the synthetic
   "Tier-2 Access Advisor" test system.
3. `preservation-regimes.md` — the three regimes (Bare / Versioned-unbound
   / Versioned-bound) defined precisely, including the B-vs-C
   information-equivalence table and direct answers to the bitemporal,
   W3C PROV, and event-sourcing collision questions.
4. `perturbation-matrix.md` — ground truth specification and the ten-case
   perturbation matrix, including the theoretically central
   retroactive-correction case (Case 3) and the concurrency-ambiguity case
   (Case 10).
5. `reconstruction-task.md` — the eight-question reconstruction task and
   the justification for using a deterministic reconstruction procedure
   rather than a human or LLM investigator for this first experiment.
6. `metrics-and-scoring.md` — the five metrics (Artifact Identification
   Accuracy, Temporal Correctness [primary], Authorization Correctness,
   Justification Completeness, False Historical Confidence [primary
   diagnostic]), scoring procedure, and explicit success/failure criteria,
   including what result would specifically kill the thesis.
7. `validity-and-confounders.md` — threats to construct, internal,
   external, and ecological validity; researcher-bias controls; the
   prior-art-equivalence concession; and the required manipulation check.
8. `preregistered-interpretation.md` — the interpretation table, written
   before implementation, mapping result patterns to conclusions.
9. `implementation-spec.md` — data schemas, concrete case parameters, and
   pseudocode-level algorithms sufficient for a future session to
   implement the experiment without reopening any conceptual decision made
   here. Contains no executable code.

## Design verdict (Task 18)

**Is the B-vs-C distinction sufficiently well-defined that running the
experiment can genuinely falsify something?**

**Yes.** The information-equivalence table in `preservation-regimes.md`
establishes that Regime C differs from Regime B by exactly one property
(explicit decision-time version-identifier binding) and no other. The
perturbation matrix includes cases specifically constructed to produce a
measurable difference if the theorized mechanism is real (Cases 3, 8, 9,
10) and cases specifically constructed to produce *no* difference if the
theorized mechanism is correctly scoped (Cases 1, 2, 4, 5, 6, 7). The
pre-registered interpretation table commits, in advance, to result
patterns that would weaken or falsify the thesis, including the specific
result that would kill it outright. Ground truth is fully and
deterministically computable, independent of any regime's artifacts.

**Design status: READY FOR IMPLEMENTATION.**

**This design has not been implemented. This experiment has not been
executed. No results — positive, negative, or partial — exist anywhere in
this repository.** Implementation and execution require a separate,
explicitly authorized future session, per the research programme's
frozen workflow (see `../../CHECKPOINT-2026-08-23.md`).
