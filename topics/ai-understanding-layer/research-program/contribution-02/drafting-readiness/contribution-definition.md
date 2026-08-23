---
id: note-contribution-02-drafting-contribution-definition
title: "Contribution 2 Drafting Readiness — Contribution Definition"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, contribution-definition]
refs: [../problem-formalization.md, ../prior-art-audit.md, ../collision-tests.md, ../novelty-verdict.md, ../experiment/RESULT.md, ../experiment/followup-case10/RESULT.md]
---

## Contribution Definition

This document reconstructs, in one place, what Contribution 2 actually
contributes — grounded in the full prior-art audit
(`../prior-art-audit.md`, `../collision-tests.md`), the formal problem
decomposition (`../problem-formalization.md`, `../temporal-semantics.md`,
`../minimal-decision-record.md`), and both completed experiments
(`../experiment/`, `../experiment/followup-case10/`). Nothing here revises
any of those documents; it synthesizes what they already established.

## Problem

**The exact engineering problem:** at some later time t1, an investigator
asks why a historical, AI-mediated decision D (made at t0) was authorized.
This single question decomposes into seven sub-problems, of which most are
already well-solved by existing engineering practice
(`../problem-formalization.md`):

- **A (outcome)** and **B (execution)** — what happened, and what code/
  model/service path produced it — are ordinarily solved by default
  persistence, version control, model registries, and tracing.
- **C (evidence)**, **D (policy)**, and **E (authority)** — which specific
  version of each dependency was consulted — are only partially solved:
  the individual histories can exist (a policy version table, a retrieval
  corpus snapshot) without any record of which slice of that history
  applied to this particular decision.
- **F (context)** is an acknowledged, deliberately bounded residual, not a
  target for exhaustive solution.
- **G (justification)** — can we determine why D was judged valid, given
  the C/D/E/F that actually applied — is the sub-problem existing
  mechanisms address least directly, and is Contribution 2's actual
  target.

The precise engineering problem, stated narrowly: **evidence, policy, and
authority validity at decision time are not, by default, bound to the
decision itself** — and, after the two completed experiments, more
precisely still: **no causal relation between the decision and the
specific versions it consumed is preserved by default**, whether that
relation would be recorded as an explicit binding, an event-sourced
consumption record, or any other mechanism that connects D to the
specific x it used.

## Existing mechanisms

Per the prior-art audit (`../prior-art-audit.md`) and collision tests
(`../collision-tests.md`), the following already exist, are mature, and
are not reinvented by this contribution:

- **Bitemporal databases** (Snodgrass; SQL:2011) completely solve valid-
  time/transaction-time semantics for anything actually modeled this way
  — the strongest single collision in the audit (Objection 4).
- **W3C PROV** fully represents lineage relations (Entity/Activity/Agent,
  Usage/Generation/Association/Delegation) once populated (Objection 1).
- **Event sourcing** fully reconstructs internal application state via
  replay, for anything captured as a domain event (Objection 2).
- **in-toto/Sigstore** supply a durable, signed, tamper-evident container
  for structured claims about a subject (Objection 7) — the closest
  production-grade mechanism to a decision record's container shape.
- **Distributed tracing (OpenTelemetry)** captures the execution path with
  high fidelity, within its typical retention window (Objection 6).
- **Reproducible-ML practice** fully solves *replay* — obtaining the same
  output from the same versioned inputs (Objection 5).
- **Audit logging / EU AI Act Art. 12** mandate execution/outcome-scoped
  record-keeping, with strong integrity guarantees where implemented
  (Objection 3).

None of these, individually or combined by default, preserves the one
thing all of them can omit: a durable record of **which specific version**
of each dependency a specific decision actually consumed.

## Missing property

What remains unavailable, even when every mechanism above is present and
mature, is **a preserved causal relation between the decision and the
exact versions of policy, evidence, authority, model, and relevant
context it consumed** — not the artifacts themselves, and not their
version histories, but the pointer from D to the specific slice of each
history that applied.

This was demonstrated, not merely argued, by both completed experiments:

- The **primary experiment** (`../experiment/RESULT.md`) showed that even
  a fully bitemporal, fully event-sourced Regime B — deliberately built
  strong, not strawmanned — can be confidently and silently wrong about
  which policy/authority version applied, once a retroactive correction
  is recorded, precisely because nothing pinned the decision to the
  version it actually used at t0.
- The **Case 10 follow-up** (`../experiment/followup-case10/RESULT.md`)
  showed a second, independent way the same gap manifests: under
  timestamp-precision loss, complete version history can leave which
  version applied genuinely underdetermined — and, critically, that this
  underdetermination is resolved by *any* preserved causal signal from
  decision to consumed version (the F10-6 negative control), not
  specifically by a schema named "binding."

## Contribution

Classified honestly, against the categories the review must distinguish:

| Category | Applies? | Why |
|---|---|---|
| New mechanism | **No** | Every underlying primitive (bitemporal storage, event sourcing, PROV, in-toto/Sigstore) is pre-existing and unmodified. |
| New architecture | **No**, not as a novel structure — the minimal decision record (`../minimal-decision-record.md`) is a synthesis/assembly of existing structures (PROV-shaped relations, in-toto-shaped container, bitemporal fields), not a new architectural pattern. |
| New formal property | **Partially** — the C/D/E/F/G decomposition (`../problem-formalization.md`) and the replay-vs-reconstruction distinction (`../collision-tests.md` Task 6) are not found named this way in the surveyed prior art. This is a modest, checkable naming/formalization contribution, not a deep theoretical discovery. |
| New synthesis | **Yes, primarily.** The recognition that AI-mediated decisions need bitemporal validity + structured evidence + an explicit per-decision causal relation, combined and applied to a specific AI dependency set (prompts, live retrieval, policy-as-config, delegated agent authority) that current tooling does not treat this way by default. |
| New empirical demonstration | **Yes, and this is what the two experiments add beyond the original audit.** The audit alone (verdict B, "narrowed survival") established the synthesis was *conceptually* distinct from prior art; the experiments established it is *behaviorally consequential* — measurably, in a controlled setting — under two independent, named mechanisms (retroactive correction; timestamp-precision ambiguity), and that the negative control (F10-6) narrows the claimed necessary mechanism from a specific schema to a general property. |
| New practitioner framing | **Yes, secondarily.** "Versioned is not bound" (now: "versioned is not causally linked") is a practitioner-legible reframing of an otherwise diffuse set of prior-art gaps — useful communicatively, not a technical claim in itself. |

**Bottom line:** the contribution is a **synthesis, demonstrated
empirically, of a formal property (preserved causal decision-context
relation) that is under-applied by default in current AI/ML tooling** —
not a new mechanism, not a new architecture, and not, after the Case 10
follow-up, a claim that one specific schema (explicit decision-time
binding) is uniquely necessary to supply that property.

## Boundary

Contribution 2 explicitly does **not** claim:

- That versioning is useless. The primary experiment's own control and
  forward-drift cases (Cases 1, 2, 4, 5, 6, 7) show Regime B — versioned,
  unbound — performing identically to Regime C in every non-adversarial
  condition. Versioning is necessary; the claim is narrower than
  "versioning fails."
- That event sourcing is insufficient in every implementation. Objection
  2 and the primary experiment's Case 5 (evidence supersession) both show
  event sourcing fully solving the problems it is architecturally suited
  to solve (capturing raw values at consultation time); the gap is
  specifically about capturing version *identifiers*, not values, for the
  dimensions that require them.
- That W3C PROV cannot encode the required relation. Objection 1 states
  directly that PROV is structurally the right shape of graph; the gap is
  that valid-time semantics and a normative-adequacy vocabulary would need
  to be added, not that PROV is the wrong tool.
- That explicit decision-time binding is uniquely necessary. This was the
  original, narrower formulation; the F10-6 negative control directly
  falsifies the "uniquely" in that claim. The surviving, narrower claim is
  that *some* preserved causal relation is necessary — binding is one
  general, buildable way to guarantee it, not the only one.
- Anything about the prevalence of this gap in real production AI
  systems. Both experiments are synthetic and controlled
  (`../experiment/experiment-design/validity-and-confounders.md`); no
  claim is made, or can be made from this evidence, about how common the
  failure mode is outside this testbed.
- Anything from Contribution 3's territory: the capability-vs-
  understanding divergence thesis, the "understanding layer" as a general
  architectural response, or the fragmentation-of-explainability/
  observability/governance diagnosis. Contribution 2 is fully statable in
  decision/reconstruction vocabulary alone, exactly as
  `../deferred-contribution-03.md` already committed to keeping it.
