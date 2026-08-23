---
id: note-contribution-02-experiment-system
title: "Contribution 2 Experiment — Domain-Neutral Test System"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, test-system]
refs: [research-question.md, ../minimal-decision-record.md]
---

## Unit of Analysis

**One historical AI-mediated decision event, D, made at t0.** Each unit
carries exactly the fields `../problem-formalization.md` and
`../minimal-decision-record.md` already establish as necessary, no more:

| Field | Value in this system |
|---|---|
| Decision identifier | A unique ID per case |
| Timestamp (t0) | The instant D was made |
| Proposed action | "Grant Tier-2 access to requester R" |
| Resulting action / state transition | GRANT or DENY, applied at t0 |
| Model/version | The scoring-function version that computed the risk score |
| Relevant input/context | The requester's evidence attributes, as they stood at t0 |
| Decision requirements | The policy rule: grant iff score < threshold, requester not on watchlist, and an authorized approver role exists |
| Evidence | The specific attribute values consulted (see below) |
| Policy applicable at t0 | The specific threshold value and its valid-time interval |
| Authority applicable at t0 | The specific agent/role holding "Approver" status and its valid-time interval |
| Actual authorization result | GRANT or DENY, deterministically computed from the above |

A case is a single D plus its full t0 state plus a specified t0→t1
perturbation (`perturbation-matrix.md`). The experiment is a set of ~10
such cases, not a single long-running system.

---

## The synthetic scenario: "Tier-2 Access Advisor"

Chosen deliberately to avoid unnecessary regulated-domain complexity (no
finance, health, or legal vocabulary), while remaining structurally
identical to the class of decisions Contribution 1 and Contribution 2 both
address (an AI-derived output authorizing a consequential state change).
It is intentionally close in shape to Contribution 1's own running example
(model-promotion / access-grant) for continuity with the rest of the
research programme, per `../empirical-program.md`'s own reuse decision —
not because domain realism matters here.

**Narrative:** An internal system decides whether requester R should be
granted "Tier-2" access to a synthetic internal resource. A scoring
function produces a risk score in [0, 1] from R's evidence attributes. A
policy sets a threshold: access is permitted only if the score is below
the threshold. An authority rule requires that a currently-designated
"Approver" role exists and is exercised. An external watchlist can
independently veto a grant regardless of score.

**Decision rule (fully deterministic, so ground truth is always exactly
knowable):**

```
GRANT  iff  (score < threshold)
             AND (an agent held the "Approver" role at t0)
             AND (requester R was NOT on the watchlist at t0)
DENY   otherwise
```

**Scoring function (deliberately a trivial stand-in, not a real ML model):**
`score = f(evidence, model_version)`, where `f` is a fixed, versioned
arithmetic function (e.g., a weighted sum of 2–3 numeric evidence
attributes, with the weights themselves constituting the "model version").
The scoring function's realism is irrelevant — the experiment tests
information architecture, not model quality, per the brief's explicit
guidance (item 9). Using a real ML model would introduce stochasticity and
non-determinism that only obscures the property under test.

---

## Controllable dimensions (and what was deliberately excluded)

| Dimension | Included? | Reason |
|---|---|---|
| **Model/scoring version** | Yes | Represents sub-problem B (execution) drift — needed to test whether model rotation alone (without policy/authority drift) creates a distinct failure mode. |
| **Evidence** | Yes | Sub-problem C — the attribute values consulted at t0, and whether they can later be "corrected" or superseded upstream (e.g., an incident record later expunged). |
| **Policy (threshold)** | Yes | Sub-problem D — the central object of the bitemporal test (`preservation-regimes.md`). |
| **Authority (Approver role assignment)** | Yes | Sub-problem E — structurally parallel to policy but tracked as an independent history, since roles and rules change independently of each other. |
| **Context (watchlist)** | Yes, minimally | Represents sub-problem F (context) as a single, bounded external dependency — included specifically to test one case of a dependency that is neither "evidence" nor "policy" in the strict sense, without opening an unbounded context category (per `../problem-formalization.md`'s explicit warning against letting F become unbounded). |
| **Separate "configuration" dimension** | No — merged into Policy | The threshold *is* the configuration value of interest; introducing a second, distinct configuration object (e.g., a rounding rule) would add a component that does not by itself test a different failure mechanism than policy drift already tests. Per the brief's instruction not to introduce components that don't affect the experimental question, this is deliberately omitted from the first experiment and flagged as a possible extension only. |
| **Prompt template** | No | This system does not use an LLM in its decision path (the scoring function is a fixed arithmetic stand-in) — a prompt dimension would require introducing an LLM component solely to have a prompt to version, which is exactly the kind of unnecessary complexity item 4 in the brief warns against. If a future secondary experiment uses an LLM-based investigator (`research-question.md`, `metrics-and-scoring.md`), a prompt-version dimension could be reintroduced there. |

---

## Why ground truth is perfectly known

Because the decision rule and scoring function are fully deterministic and
specified in closed form, the true applicable policy version, authority
version, evidence values, model version, and correct GRANT/DENY outcome
for any case are computable directly from the case's t0 specification,
independent of and prior to constructing any regime's preserved artifacts.
Ground truth is authored once, per case, before the three regimes'
artifact sets are derived from it (see `preservation-regimes.md`) — the
regimes are downstream projections of a single ground-truth case
specification, never an independent source of truth themselves. This
satisfies the requirement that ground truth be usable purely for scoring
and never visible to the reconstruction procedure being evaluated.
