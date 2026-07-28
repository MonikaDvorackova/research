---
id: arch-ai-infrastructure-gap-claim-inventory
title: "Claim inventory: Preserving Justification in AI Systems"
topic: ai-infrastructure-gap
type: architecture
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [claims, architecture, governance]
---

## Claim inventory

All items below are **hypotheses** unless later promoted with evidence. None should be cited in publications as established fact.

---

### C1 — Reconstruction requirements exceed loosely coupled artifact retention

| Field | Content |
|---|---|
| **Claim** | Retaining execution state, events, traces, model outputs, policies, and provenance as separate artifact classes is not, by itself, sufficient to reconstruct why a historically situated decision was justified, authorized, and valid. |
| **Status** | `hypothesis` |
| **Required evidence** | Concrete decision scenarios where each artifact class is present yet reconstruction of the triad fails; explicit missing bindings identified. |
| **Strongest counterargument** | Failures are operational (retention, correlation IDs, policy decision logging not enabled), not architectural. |
| **Possible falsification** | Show representative systems where existing artifacts, correctly configured, fully support reconstruction. |
| **Publication relevance** | Core thesis for article A (problem framing). |

---

### C2 — Justification, authorization, and validity are separable reconstruction targets

| Field | Content |
|---|---|
| **Claim** | “Why justified,” “why authorized,” and “why valid” demand partially distinct retained structure; satisfying one (e.g., allow/deny policy log) does not automatically satisfy the others. |
| **Status** | `hypothesis` |
| **Required evidence** | Scenario matrix showing orthogonal failure modes (authorized but unjustified; justified narrative without authority; valid constraints with opaque justification). |
| **Strongest counterargument** | In practice these collapse into a single policy decision record. |
| **Possible falsification** | Demonstrate a minimal policy-decision + provenance schema that reconstructs all three without additional structure. |
| **Publication relevance** | Sharpens vocabulary and evaluation criteria for A; constrains solution shape for B. |

---

### C3 — Temporal binding of criteria is a first-order requirement

| Field | Content |
|---|---|
| **Claim** | Without durable binding to the *then-applicable* policy, model, and criterion versions, historical reconstruction is systematically unreliable even if current-state stores are rich. |
| **Status** | `hypothesis` |
| **Required evidence** | Cases where drift of policy/model/criteria changes post-hoc “explanation” relative to decision-time reality; show whether temporal DB / version pins already solve this. |
| **Strongest counterargument** | Temporal databases and versioned policy bundles already solve this when used. |
| **Possible falsification** | Kill-list evaluation shows temporal + policy versioning closes the gap in target scenarios. |
| **Publication relevance** | Discriminates E4 vs E5; critical for A’s kill list; design constraint for B. |

---

### C4 — Distributed tracing does not encode normative basis

| Field | Content |
|---|---|
| **Claim** | OpenTelemetry-style traces reconstruct causal execution paths but do not, in typical usage, encode justification/authorization/validity criteria as reconstructable structure. |
| **Status** | `hypothesis` |
| **Required evidence** | Analysis of standard semantic conventions and representative traces; attempt to reconstruct the triad from traces alone. |
| **Strongest counterargument** | Baggage, attributes, and event payloads can carry normative context if conventions exist and are adopted. |
| **Possible falsification** | Exhibit a tracing profile that makes the triad reconstructable without additional stores. |
| **Publication relevance** | Kill-list section of A; avoids false novelty against observability. |

---

### C5 — Provenance (including W3C PROV) does not equal justification

| Field | Content |
|---|---|
| **Claim** | Data/model provenance and PROV graphs answer “what derived from what / who did what” more readily than “why was this decision justified and authorized under then-valid criteria.” |
| **Status** | `hypothesis` |
| **Required evidence** | Mapping exercise: required reconstruction fields vs. PROV entity/activity/agent relations; identify unforced gaps. |
| **Strongest counterargument** | PROV is expressive enough; gaps are modeling choices, not limits of the abstraction. |
| **Possible falsification** | Produce a PROV profile that captures the triad for target scenarios. |
| **Publication relevance** | Kill-list rigor for A; prevents rediscovering provenance under a new name. |

---

### C6 — Policy decision logs are necessary but not sufficient

| Field | Content |
|---|---|
| **Claim** | OPA/Cedar-style decision logs are necessary for authorization reconstruction but insufficient for full justification/validity reconstruction in AI-mediated decisions that depend on model outputs, evidence thresholds, and multi-party authority. |
| **Status** | `hypothesis` |
| **Required evidence** | Scenarios with complete policy logs where justification or validity still cannot be reconstructed; document missing fields. |
| **Strongest counterargument** | Richer policy inputs/outputs and obligations already cover those cases. |
| **Possible falsification** | Show policy-engine logging patterns that close the triad for agreed scenarios. |
| **Publication relevance** | Central kill-list item for A; defines integration surface for any B solution. |

---

### C7 — Explainability and reasoning traces are not durable justification records

| Field | Content |
|---|---|
| **Claim** | Contemporaneous explanations and model reasoning traces, as commonly retained, are not reliable architectural mechanisms for historical reconstruction of justification under authorization and validity constraints. |
| **Status** | `hypothesis` |
| **Required evidence** | Stability, faithfulness, retention, and binding failures relative to decision identity and policy versions. |
| **Strongest counterargument** | With mandated retention and schema, reasoning traces *are* the justification record. |
| **Possible falsification** | Show deployments where retained traces meet reconstruction requirements for the triad. |
| **Publication relevance** | Separates ML explainability literature from architectural claim in A. |

---

### C8 — If a residual gap remains, composition may still beat a new layer

| Field | Content |
|---|---|
| **Claim** | Even if C1 holds, the appropriate response may be a composition profile (schemas, bindings, retention) over existing abstractions rather than a new architectural layer under any candidate formulation. |
| **Status** | `hypothesis` |
| **Required evidence** | Side-by-side: composition profile vs. layer proposal on complexity, adoptability, and reconstruction completeness. |
| **Strongest counterargument** | Without a named layer and interfaces, composition remains aspirational and inconsistently implemented. |
| **Possible falsification** | Show that only a distinct layer with enforced interfaces achieves completeness in practice. |
| **Publication relevance** | Guards B against premature layer branding; frames Radar piece as demonstration of *whatever* survives evaluation. |

---

### Claim status legend

| Status | Meaning |
|---|---|
| `hypothesis` | Unverified; default for this inventory |
| `supported` | Positive evidence accumulated (not used yet) |
| `weakened` | Counterevidence exists but claim not rejected |
| `rejected` | Falsified for stated scope |
| `reframed` | Replaced by a sharper claim |
