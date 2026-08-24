---
id: note-contribution-03-generalization-from-c2
title: "Contribution 3 — Generalization from Contribution 2 (RQ3)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, generalization, RQ3]
refs: [../contribution-02/article/FINAL-ACCEPTANCE.md, composition-review.md]
---

## RQ3

> Can Contribution 2's decision-specific result about consumed-context
> identifiability be generalized into any defensible system-level
> property, or must it remain decision-local?

## The six levels, tested conservatively

| Level | Description | Status |
|---|---|---|
| **G1 — Decision-context identifiability** | Can a specific historical decision's consumed context (model/policy/evidence/authority/config version) be uniquely reconstructed? | **SUPPORTED BY CONTRIBUTION 2**, directly — this is exactly what was tested, measured, and frozen (`../contribution-02/article/FINAL-ACCEPTANCE.md`). |
| **G2 — Execution-context identifiability** | Can the same guarantee be extended to every decision point within one execution/trajectory (e.g., an agent making several tool-mediated decisions in sequence)? | **PLAUSIBLE EXTENSION.** The same consumption-relation logic should, in principle, apply pointwise to each decision within a trajectory — nothing in Contribution 2's design forecloses this. But it has not been tested, and `composition-review.md` shows composition effects are real and evidenced for a *different* property (predictability) at exactly this kind of aggregation step — so plausibility is not confirmation. |
| **G3 — Trajectory reconstructability** | Can the *entire* trajectory (not just each decision point individually, but the trajectory as a composed whole, including how decisions influenced each other) be reconstructed? | **REQUIRES NEW EVIDENCE.** This is a strictly stronger claim than G2 (pointwise) — it additionally requires that inter-decision dependencies compose correctly, which is precisely the open question `composition-review.md` isolates as untested for reconstructability specifically. |
| **G4 — Deployed-system-state reconstructability** | Can the full state of a deployed system (all trajectories, all decisions, over its operational history) be reconstructed? | **REQUIRES NEW EVIDENCE**, and a materially larger claim than G3 — no material in this programme addresses aggregate system-state reconstruction as opposed to per-decision or per-trajectory reconstruction. |
| **G5 — Behavioral-envelope understanding** | Can what the system *can* do, across possible future conditions, be characterized? | **UNSUPPORTED LEAP.** This is a forward-looking, possibility-space question (system identification's and behavioral verification's object, `diagnosability-review.md`), categorically different from Contribution 2's backward-looking, single-instance reconstruction object. Nothing in Contribution 2 bears on this. |
| **G6 — Operator understanding** | What do the humans who built/operate the system actually know about it? | **UNSUPPORTED LEAP.** A human-factors/organizational-knowledge question (architectural knowledge management's own object, `../program-comprehension-review.md`), not addressed by any formal or empirical material in Contribution 2. |

## Highest defensible generalization level

**G1 is fully earned. G2 is the highest level this review is willing to
call a "plausible extension" rather than a leap — and even G2 is
explicitly not confirmed, only plausible.** G3 is the first level this
review classifies as requiring genuinely new evidence, not a natural
next step — this is the precise boundary a conservative reading of
Contribution 2 supports.

## Why the boundary sits between G2 and G3

The distinction is exactly the one `composition-review.md` isolates:
G2 only requires that the *same, already-tested* guarantee holds
independently at each decision point (a pointwise claim, not requiring
anything new). G3 requires that guarantees about *individual* decision
points **compose** into a guarantee about the *trajectory as a whole*,
including whatever dependencies exist *between* decisions — and
composition effects are directly, currently evidenced in the adjacent
literature (compositional verification, emergent behavior) as a genuine,
non-trivial risk, not a safe default assumption. Treating G3 as
automatically true because G1 is true would be exactly the kind of
unsupported leap this review's own decision rule (Section 24) and the
authorizing task's explicit instruction to "be conservative" prohibit.

## Consequence

Contribution 2's result **remains decision-local, with a plausible but
unconfirmed pointwise extension to execution-level (G2)**. It does
**not** currently support any claim at the trajectory, system, envelope,
or organizational-knowledge levels (G3–G6). Any future Article 3 draft
that uses Contribution 2 as a premise for a system-level claim beyond G2
would be overclaiming relative to what this review can confirm — this is
the load-bearing finding for `article-03-options.md`'s ranking.
