---
id: topic-ai-infrastructure-gap-charter
title: "Preserving Justification in AI Systems"
topic: ai-infrastructure-gap
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [architecture, governance, ai-systems]
---

# Topic: Preserving Justification in AI Systems

**Slug:** `ai-infrastructure-gap`  
**Status:** `active`  
**Owner:** Monika Dvořáčková

## 1. Observed architectural problem

Modern AI systems commonly retain rich operational and governance artifacts: execution state, events, traces, model outputs, policies, and provenance records. Despite that retention, it is not obvious that they retain *enough structured information*—in the right bindings, at the right times—to reconstruct **why a historically situated decision was justified, authorized, and valid** when it was made.

This is stated as an **open architectural question**, not as an established deficit. The investigation must determine whether the apparent shortfall is:

- a genuine gap in what systems preserve;
- a composition gap (artifacts exist but are not linked for reconstruction);
- a semantic gap (artifacts exist but lack normative or temporal meaning); or
- a misconception (existing abstractions already suffice when used correctly).

No new architectural layer is assumed to be necessary.

## 2. Scope of the investigation

**In scope**

- Decision episodes in AI-mediated systems where justification, authorization, and validity may need later reconstruction (audit, incident review, regulatory inquiry, engineering debugging of governance failures).
- Structural properties of records and bindings required for such reconstruction.
- Systematic comparison of existing abstractions against those properties (see kill list).
- Careful comparison of candidate *formulations* of any residual gap—without adopting a branded layer prematurely.
- Relationship of findings to AIGov Core concepts and boundaries (see §9).

**Out of scope (for this topic’s charter; may appear as adjacent work)**

- Building a production governance product.
- Training or evaluating foundation models for “better explanations.”
- Legal advice or jurisdiction-specific compliance checklists.
- Exhaustive survey of every logging vendor or MLOps platform.

## 3. Central research hypothesis

**Hypothesis (provisional):** Systems that preserve execution state, events, traces, outputs, policies, and provenance **as loosely coupled artifact classes** still may fail to support faithful reconstruction of historical *justification*, *authorization*, and *validity*, because reconstruction requires durable binding among (a) the decision identity, (b) the criteria and authority under which it was allowed, (c) the evidence or inputs then considered decisive, and (d) the temporal and versioned context in which those criteria applied—bindings that current stacks often leave implicit, incomplete, or reconstructable only with unreliable external narrative.

This hypothesis is **falsifiable**. If disciplined use of existing abstractions already provides those bindings in representative architectures, the hypothesis fails and the contribution becomes a composition guide rather than a gap claim.

## 4. Competing explanations

| Explanation | Claim |
|---|---|
| E1 — No real gap | Operators already have sufficient reconstruction via logs + traces + policy + provenance when configured properly. |
| E2 — Composition gap | Sufficient artifact types exist; the failure is missing schemas, correlations, and retention policies that bind them to a decision episode. |
| E3 — Semantic / normative gap | Technical provenance and traces do not capture *justification* or *authorization* criteria; normative structure is missing. |
| E4 — Temporal gap | Criteria, models, and policies drift; systems retain latest state but not historically applicable versions bound to the decision. |
| E5 — New layer required | Residual requirements cannot be met by composing existing abstractions; a dedicated concern (under some formulation) is warranted. |

Work proceeds by attempting to **kill E5 first** and to force a choice among E1–E4 with evidence.

## 5. Candidate formulations (not adopted)

The following names are **competing candidate formulations** of a residual concern—not product names and not commitments:

- Decision Knowledge Layer
- Justification Layer
- Decision Integrity Layer
- Decision Reconstruction Layer

Any eventual recommendation may conclude that **none** of these should exist as a separate layer, and that composition of existing abstractions is sufficient.

## 6. Kill list — existing abstractions

For each candidate, state what would count as evidence that it **already solves** the reconstruction problem as framed above.

| Abstraction | What “already solves it” would look like |
|---|---|
| **Audit logging** | For representative decision types, audit records alone suffice to restate justification, authorization basis, and validity criteria *as of decision time*, including applicable policy/model versions, without ad hoc tribal knowledge. |
| **Event sourcing** | The event log plus projections can rehydrate the decision episode such that authorization and justification criteria are first-class recoverable state, not only business payload. |
| **Distributed tracing / OpenTelemetry** | Trace graphs plus baggage/attributes reconstruct not only causal execution paths but the normative basis (why allowed / why considered valid) for the decision span. |
| **Data and model provenance** | Provenance chains identify inputs/models *and* bind them to the decision’s justification and authorization criteria at the relevant time. |
| **W3C PROV** | A PROV graph for the decision episode encodes agents, entities, activities, and derivations such that justification/authorization/validity are explicit and historically queryable. |
| **Policy engines (OPA, Cedar, …)** | Policy decision logs (inputs, policies, versions, obligations) plus related context reconstruct authorization *and* connect to justification/validity beyond a boolean allow/deny. |
| **Workflow engines** | Workflow history reconstructs human/machine steps *and* the criteria that made each gate justified and valid when taken. |
| **Knowledge graphs** | The graph stores decision episodes with temporal/normative relations sufficient for reconstruction without external narrative glue. |
| **Explainability methods** | Explanations retained at decision time are durable, faithful enough for historical reconstruction of justification (not only contemporaneous UX), and bound to authorization/validity. |
| **Model reasoning traces** | Retained chains-of-thought / tool traces reconstruct justification under the policies and authorities then in force—not merely token-level paths. |
| **Decision records** | Explicit decision-record schemas already capture the required bindings; widespread patterns close the gap if adopted. |
| **Temporal databases** | Bitemporal (or equivalent) retention of criteria, evidence, and policy/model versions yields correct historical reconstruction by query. |
| **Cryptographic ledgers** | Ledger entries provide integrity *and* sufficient structured content for justification/authorization/validity reconstruction (integrity alone is not enough). |

Failure of an abstraction on this test does not imply a new layer; it may imply better composition (E2), semantics (E3), or temporality (E4).

## 7. Falsification criteria

The central hypothesis is weakened or rejected if research shows that:

1. **Representative architectures** using only items from the kill list (possibly composed) can reconstruct justification, authorization, and validity for agreed decision scenarios with acceptable completeness; or
2. Apparent failures are explained entirely by **misconfiguration / non-adoption**, and corrected application of existing abstractions closes the gap; or
3. The triad “justified / authorized / valid” cannot be made precise enough for architectural requirements (problem dissolves into underspecified goals).

The hypothesis is **supported** (not proven) only if residual reconstruction failures remain after charitable, expert composition of existing abstractions, and those failures cluster into stable missing properties.

## 8. Research questions

1. What minimal structured information and bindings are required to reconstruct why a historically situated AI-mediated decision was justified, authorized, and valid?
2. Which kill-list abstractions already provide which parts of that minimum, and where do they stop?
3. Are residual failures best classified as E1–E5?
4. How should candidate layer formulations be compared if—and only if—E5 remains standing?
5. What does a rigorous problem-framing article need as evidence before any solution article is warranted?

## 9. Expected technical contributions

- A precise problem statement and vocabulary (with unresolved terms listed explicitly).
- A kill-list evaluation method and initial results against reconstruction requirements.
- A claim inventory with statuses, evidence needs, and falsifiers (no unverified claims as facts).
- If a gap survives: a **composition or extension** proposal—possibly without a new layer.
- If a gap does not survive: a negative result that is still publishable as architectural clarification.

## 10. Relationship to AIGov Core

This topic is adjacent to **AIGov Core** insofar as governable AI systems require accountable decision episodes. The relationship is investigative, not product-roadmap:

- Findings may inform what AIGov Core should *assume* must already exist in the platform vs. what governance logic must supply.
- This topic does **not** treat AIGov Core as proof that a new layer exists, nor as a venue to smuggle branding into research claims.
- Interfaces, terminology, and boundaries relative to AIGov Core will be recorded as evidence accumulates; no implementation work is in scope for topic initialization.

## 11. Intended publications

| Order | Venue | Intent |
|---|---|---|
| A | Website / long-form architectural article | Standalone **problem** framing, kill-list analysis, falsification stance |
| B | O’Reilly Radar (follow-up) | Propose and **demonstrate** a technical solution—only after A’s problem claim is earned |

No publication drafts are created in this initialization.

## 12. Explicit non-goals

- Declaring that a “Justification Layer” (or synonym) must be built.
- Shipping reference implementation or CI/site scaffolding under this topic’s init.
- Inflating novelty by ignoring the kill list.
- Producing literature notes with artificial citations.
- Conflating explainability UX with durable historical justification records.
- Equating cryptographic integrity or trace completeness with justification completeness.

## 13. Unresolved terminology

The following terms are **not yet fixed**; working senses are provisional and must be sharpened or replaced:

| Term | Working sense (provisional) | Open issue |
|---|---|---|
| Decision | An identifiable AI-mediated commit to an action or outcome | Boundaries vs. recommendation, score, or plan |
| Justification | Reasons treated as supporting the decision under stated criteria | Relation to explanation, rationale, evidence |
| Authorization | Permission under applicable authority/policy at decision time | Human vs. machine authority; policy decision vs. business approval |
| Validity | Conformance to applicable rules/constraints then in force | Legal vs. technical vs. organizational validity |
| Reconstruction | Ability of a later party to restate justification/authorization/validity from retained structure | Completeness thresholds; audience (auditor, engineer, court) |
| Historically situated | Bound to time, versions, and context of the original episode | What clock and version axes are mandatory |
| Layer | A distinct architectural concern with interfaces | Whether “layer” is the right unit vs. pattern/profile |

## Entry points

| Kind | Path |
|---|---|
| Claim inventory | `architecture/claim-inventory.md` |
| Research plan | `future-work/research-plan.md` |
| Primary specification | `specifications/` (none yet) |
| Active publications | none yet (see `meta.yaml` candidate_publications) |

## Related topics

None registered yet.
