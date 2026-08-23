---
id: note-contribution-02-problem-formalization
title: "Contribution 2 — Formalizing the Reconstruction Problem"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, problem-formalization, adversarial-audit]
refs: [claim-graph.md, conceptual-inversions.md, contribution-boundaries.md]
---

## Contribution 2 — Formalizing the Reconstruction Problem

Scope: Task 1 of the Contribution 2 adversarial audit. This document precedes
any literature comparison, per the brief's explicit sequencing requirement.
It does not import Contribution 1's enforcement vocabulary (gate, ALLOW/BLOCK/
ESCALATE) except where logically unavoidable, and it does not touch
Contribution 3's territory (capability vs. understanding, fragmentation of
explainability/observability/governance).

---

## Setup

A decision **D** is made at time **t0**. D is understood, per Contribution 1's
shared premise (C1, not reargued here), as an authorized state transition —
something happened in the world (a model was promoted, a transaction was
approved, an agent executed a tool call) because an AI-derived output was
treated as sufficient grounds to act.

At a later time **t1 > t0**, an investigator asks:

> Why was D permitted, selected, or considered valid at t0?

This single English sentence conflates several logically independent
questions. Treating "reconstructability" as one property — as the brief
warns — is the single most common failure mode in this kind of claim. The
sentence is decomposed below into seven sub-problems (A–G), each with its own
truth conditions, its own required inputs, and — critically — its own
relationship to mechanisms that already exist.

---

## A. Outcome reconstruction

**Question:** What happened? (What state transition occurred, what was its
final form, when did it take effect?)

**What answering it requires:** A retained record of the transition itself —
a row in a database, a deployment record, a completed transaction.

**Status:** Ordinarily solved by default. Any system that persists its own
state changes at all — which is nearly all production software — answers
this without any special design effort. This is not where the reconstruction
problem lives, and no part of Contribution 2 should be built around
demonstrating that outcome reconstruction is hard. It usually is not.

---

## B. Execution reconstruction

**Question:** What code, model, and system path produced the outcome? Which
function ran, which model version served the request, in what order did
services get called?

**What answering it requires:** Version-controlled code, a model registry
entry, and/or execution telemetry (traces, logs) covering the request.

**Status:** Well-served by existing, mature mechanisms — version control,
model registries (MLflow, Unity Catalog, Vertex AI Model Registry), and
distributed tracing (OpenTelemetry). Given sufficient retention, this is
usually reconstructable with high fidelity. Reproducible-ML practice (fixed
code + data + model version, deterministic pipeline) can, under favorable
conditions, go further and re-derive the *same output* — this is **replay**,
formalized separately below (Task 6 material, `collision-tests.md`
Objection 5).

---

## C. Evidence reconstruction

**Question:** What evidence was available to, and consulted by, the decision
process at t0 — which documents, retrieval results, sensor readings, or
prior outputs were treated as inputs to the decision?

**What answering it requires:** Not merely that the evidence *exists
somewhere today* (a retrieval corpus, a document store), but that the
*specific version or snapshot* consulted at t0 is durably identifiable and
retrievable, independent of whether the live source has since changed.

**Status:** Not solved by default. A live retrieval corpus, prompt template
store, or feature store is ordinarily a **mutable, overwrite-in-place**
system — it answers "what is true now," not "what was returned then." Unless
a system deliberately snapshots or versions what was actually consulted at
decision time, C is not answerable at t1, even though A and B may be
answerable perfectly. This is the first sub-problem where the reconstruction
gap becomes real.

---

## D. Policy reconstruction

**Question:** What rules, thresholds, or requirements applied to D at t0?

**What answering it requires:** A durable record not just of the policy
document as it exists today, but of the specific **version of the policy
that was in effect at t0** — its valid-time interval, not merely its
transaction (recording) time.

**Status:** This is a bitemporal problem in the technical sense (see
`temporal-semantics.md`). It is solvable with existing, decades-old database
theory (Snodgrass; SQL:2011) — *if* policy is stored in a system that
supports valid-time queries. In practice, policy documents, prompt-governing
rules, and configuration are rarely stored this way; they live in wikis, YAML
files under mutable paths, or config services with no valid-time model at
all. The gap here is one of **adoption**, not missing theory.

---

## E. Authority reconstruction

**Question:** Who, or what, had the authority to authorize D at t0 — under
what delegation, role assignment, or approval chain?

**What answering it requires:** A durable, time-scoped record of role and
delegation assignments — "Agent X was authorized to approve deployments of
class Y from t_a to t_b" — distinct from D. Like policy, this is a
bitemporal-shaped problem (role/delegation validity intervals), and it is
also distinct from evidence and policy: an agent can have had access to the
right evidence and consulted the right policy version and *still* have
lacked the authority to act on it, or vice versa.

**Status:** Rarely modeled explicitly at all. Most systems record *that* an
approval happened (a checkbox, a merged PR, an "approved" status) but not the
authority basis under which the approver was entitled to approve — which
matters when roles, delegations, or escalation policies themselves change
between t0 and t1.

---

## F. Context reconstruction

**Question:** What other contextual or environmental inputs shaped the
decision, beyond what was formally logged as "evidence" — configuration
flags, sampling parameters, external service responses, system load, or
other conditions that influenced the outcome without being treated as a
first-class input?

**What answering it requires:** Broader and less well-defined than C — this
is the residual category for inputs that mattered but were never designed to
be evidence. It is the sub-problem most vulnerable to becoming unbounded
("everything is context"), and Contribution 2 should resist trying to close
it exhaustively. It exists specifically to acknowledge that C, D, and E do
not jointly exhaust "what shaped the decision," not to license an
open-ended preservation mandate.

**Status:** Partially and unevenly captured by observability tooling
(tracing attributes, feature flags in logs) when developers happen to think
to record it; not systematically solved, and not solvable by any single
mechanism, because the boundary of "relevant context" is domain-specific.

---

## G. Justification reconstruction

**Question:** Given the evidence, policy, authority, and context that
existed at t0 — *specifically*, not as they exist today — can we determine
why D was permitted or selected?

**This is not the conjunction of A–F.** Having perfect answers to A–F does
not automatically yield G, for two reasons:

1. **The binding problem.** A–F may each be independently reconstructable
   (the policy's full version history exists; the retrieval corpus is
   snapshotted daily; the authority-delegation log is intact) without any
   record specifying **which of those versions was actually operative for
   this particular decision.** Versioning existing elsewhere is not the same
   as a per-decision binding being recorded at t0. This is the sharpest,
   most load-bearing distinction this audit identifies (developed fully in
   `collision-tests.md`, Objection 8).
2. **The normative-synthesis step.** Even with a correct binding, "why was D
   valid" is a claim about whether the bound evidence *satisfied* the bound
   policy under the bound authority — an evaluative judgment, not a lookup.
   If that judgment was never recorded (only its outcome — "approved" —
   was), G may be unanswerable even with perfect A–F reconstruction. This is
   Source A's own example: "the approval remains recorded, but the reasoning
   behind it does not."

**Status:** This is the actual target of Contribution 2, and the sub-problem
existing mechanisms address least directly.

---

## Which sub-problems does Contribution 2 actually require?

| Sub-problem | Contribution 2's stance |
|---|---|
| A. Outcome | Out of scope — already solved by ordinary persistence. Not a claim worth making. |
| B. Execution | Out of scope as a *novel* claim — well-served by version control, registries, tracing, reproducible-ML practice. Referenced only as a baseline against which C–G are shown to be different. |
| C. Evidence | **In scope.** The transient-context problem (mutable retrieval/prompt/config sources) is real and under-solved by default. |
| D. Policy | **In scope**, and shown below to be a bitemporal-data problem with existing, underused theory. |
| E. Authority | **In scope**, structurally parallel to D but a distinct record (delegation/role validity, not rule validity). |
| F. Context | **In scope only as an acknowledged residual**, not as a target for an exhaustive solution. |
| G. Justification | **The actual target claim.** Requires an explicit, decision-time **binding** across C/D/E (and relevant F), plus — where it existed — the normative rationale, persisted as a first-class artifact rather than reconstructed after the fact from memory or inference. |

**Consequence for framing:** Contribution 2 is not a claim that "AI decisions
are unreconstructable." Outcome and execution reconstruction are usually
fine. The precise, defensible claim is narrower: **that evidence, policy, and
authority validity at decision time are not bound to the decision by
default, and that this binding — not any of the individual artifacts it
would reference — is the missing engineering artifact.** This reframing is
carried forward into `prior-art-audit.md` and is the basis for the surviving
thesis in `novelty-verdict.md`.
