---
id: review-2026-07-29-opentelemetry-specification
title: "Review: OpenTelemetry Specification against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, observability, opentelemetry, tracing, reconstruction]
refs: [openTelemetry2026specification]
sut: "OpenTelemetry Specification v1.59.0 (core signals)"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
---

# Review

## Bibliographic Information

**Title:** OpenTelemetry Specification

**Authors / editors:** OpenTelemetry Authors (CNCF OpenTelemetry project; community-maintained specification)

**Venue:** OpenTelemetry specification repository / published docs

**Year / version pinned for this review:** Specification release **v1.59.0** (GitHub release published 2026-07-10)

**DOI / URL:**

- Release tag: https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.59.0
- Spec tree at tag: https://github.com/open-telemetry/opentelemetry-specification/tree/v1.59.0/specification
- Published docs entry: https://opentelemetry.io/docs/specs/otel/
- No DOI is asserted on the sources inspected for this review.

**Primary documents inspected (SUT):**

| Document | Path at v1.59.0 |
|---|---|
| Overview | `specification/overview.md` |
| Glossary | `specification/glossary.md` |
| Trace API | `specification/trace/api.md` |
| Baggage API | `specification/baggage/api.md` |
| Context / propagators | `specification/context/api-propagators.md` |
| Resource data model | `specification/resource/data-model.md` |
| Logs data model | `specification/logs/data-model.md` |
| Metrics data model (scope check) | `specification/metrics/data-model.md` |
| Semantic conventions pointer | `specification/semantic-conventions.md` |

**Companion sources (identified; not the scored SUT):**

- OpenTelemetry Semantic Conventions (separate repository), release **v1.43.0** (2026-07-03): https://github.com/open-telemetry/semantic-conventions  
- GenAI semantic conventions have been moved to https://github.com/open-telemetry/semantic-conventions-genai (noted; not scored as a complete primary unit in this review)
- W3C Trace Context / W3C Baggage (referenced by OTel for propagation formats)

**Evaluated unit:** OpenTelemetry **specification** information model for observability signals (traces, logs, metrics as defined, baggage, resource, context propagation) — what structured information the model can preserve. **Not** observability research generally; **not** vendor APM products; **not** language SDK implementations; **not** Collector pipelines.

**Primary source availability:** Complete for the pinned OpenTelemetry Specification v1.59.0 documents listed above (`HTTP 200`, full Markdown retrieved from the release tag).

---

## Summary

OpenTelemetry organises client telemetry into **signals** (tracing, metrics, logs, baggage, and related concerns) that share **context propagation** but function independently. A **distributed trace** is a DAG of **spans** linked by parent/child relationships (and optional links), representing events consolidated across components for a single logical operation. Spans carry identifiers conforming to W3C Trace Context, optional attributes, timed events, status, and span kind. **Baggage** propagates application-defined name/value pairs for annotating observability events across a transaction; the specification states it is **primarily intended** for OpenTelemetry observability systems, while noting it can prototype other cross-cutting concerns. A **Resource** identifies the observed entity producing telemetry via attributes/entities. The **logs data model** defines structured log/event records with timestamps, optional trace context fields, severity, body, resource, instrumentation scope, and attributes.

Without evaluation: OpenTelemetry systematically preserves causal execution structure, timing, service/resource identity, and freely typed attributes/events. It does not define first-class constructs for governing policy, authorization outcomes, justification criteria, relied-upon evidence, or legal context.

---

## Reconstruction Capabilities

Scores use the repository scale (review methodology):

- 0 = Not addressed
- 1 = Mentioned or partially supported
- 2 = Substantially supported
- 3 = Explicitly and systematically supported

| Criterion | Score | Evidence |
|---|---:|---|
| System state | 1 | **Source:** Resource data model — attributes identifying the observed entity (e.g. container/pod/host hierarchy); span/log attributes as open key-value maps (`resource/data-model.md`; Trace API Set Attributes; Logs Attributes). **Relevance:** Can capture deployment/runtime identity and ad hoc state fields. **Interpretation:** Substantial for *resource identity*, weak for decision-time application state as a bound episode; no system-state snapshot type. **Confidence:** high |
| Decision process | 2 | **Source:** Tracing Signal — traces as DAG of spans for a logical operation crossing process boundaries (`overview.md`); SpanKind clarifies client/server/producer/consumer relationships (`trace/api.md`). **Relevance:** Systematic causal process graph for distributed execution. **Interpretation:** Reconstructs *how work executed* across services; does not systematically encode normative decision steps (allow/deny, acceptance, criteria evaluation). “Decision” in the Trace API refers primarily to **sampling** decisions, not legal/business authorization. **Confidence:** high |
| Evidence | 1 | **Source:** Span attributes/events; log body/attributes; baggage as contextual name/value pairs (`trace/api.md`, `logs/data-model.md`, `baggage/api.md`, overview Baggage Signal). **Relevance:** Can carry payloads that *happen* to be evidence references. **Interpretation:** No first-class evidence, reliance, or exclusion model (IC-10–IC-12). Attribute bags are unconstrained relative to evidential semantics. **Confidence:** high |
| Rules | 0 | **Source:** Searched primary SUT documents for policy/authorization/justification constructs; Trace/Baggage/Logs/Resource models define observability structures, not governing rules. Semantic conventions pointer lists reserved operational attributes (e.g. `service.name`, `error.type`) — not policy versions or rule paths (`semantic-conventions.md`). **Relevance:** Rules/policies are outside the core information model. **Interpretation:** Not addressed as reconstructable structure. Application-specific attributes *could* store rule ids, but that is profile work, not OTel Spec content. **Confidence:** high |
| Human context | 1 | **Source:** Baggage overview examples include “API user or token that is responsible for that request” (`overview.md` Baggage Signal); end-user related conventions live in semantic conventions (companion), not as core types. **Relevance:** Propagatable user/token context is contemplated for observability indexing. **Interpretation:** Partial — no systematic actor/authority/delegation model comparable to PROV agents; human context is optional attributes/baggage, not a responsibility algebra. **Confidence:** high |
| Temporal continuity | 2 | **Source:** Trace timestamps/durations (`trace/api.md` Time); span events with timestamps; log `Timestamp` / `ObservedTimestamp` (`logs/data-model.md`); span start/end lifetime. **Relevance:** Strong event/operation timing. **Interpretation:** Substantial for execution timelines; does not mandate binding of historically applicable policy/model versions to a decision time (IC-07, IC-13, IC-19 as normative axes). Sampling and attribute mutation rules constrain what is retained, not legal temporality. **Confidence:** high |

### Checklist mapping (expressiveness of OpenTelemetry Specification constructs)

Marks concern what the **specification model** can express/retain, not typical vendor deployments.

| ID | Category | Mark | Notes (evidence pointer) |
|---|---|---|---|
| IC-01 | Decision identity | PARTIAL | TraceId/SpanId identify operations (`SpanContext`); not a decision-episode type — correlation by convention |
| IC-02 | Decision outcome | PARTIAL | Span status / attributes / log body can encode outcomes; not a distinguished decision-outcome relation |
| IC-03 | Decision time | PARTIAL | Span and log timestamps; clock-domain policy not a legal as-of model |
| IC-04 | Actor(s) | PARTIAL | Via attributes/baggage/user conventions; not first-class agents |
| IC-05 | Authority | FAIL | Not first-class |
| IC-06 | Governing policy | FAIL | Not in core model |
| IC-07 | Policy version | FAIL | Not in core model |
| IC-08 | Applicable rules | FAIL | Not in core model |
| IC-09 | Constraints | FAIL | Not in core model |
| IC-10 | Evidence used | PARTIAL | Only if encoded in attributes/events/logs |
| IC-11 | Evidence relied upon | FAIL | No reliance distinction |
| IC-12 | Excluded evidence | FAIL | Not addressed |
| IC-13 | Model version | PARTIAL | Possible via attributes; GenAI conventions (companion repo) may standardize model ids — not scored as SUT here |
| IC-14 | Prompts | PARTIAL | Same — companion GenAI conventions, not core Spec |
| IC-15 | Tools | PARTIAL | Spans for tool calls possible; not normative decision binding |
| IC-16 | External services | PASS/PARTIAL | Client/server spans + resource attributes systematically model service calls |
| IC-17 | Confidence | PARTIAL | Attributes only |
| IC-18 | Assumptions | FAIL | Not addressed |
| IC-19 | Temporal context | PARTIAL | Execution time yes; policy/data as-of binding no |
| IC-20 | Legal context | FAIL | Not addressed |
| IC-21 | Integrity information | PARTIAL | Not core; export pipelines may add integrity outside Spec |
| IC-22 | Signatures | FAIL | Not addressed in SUT documents |
| IC-23 | Provenance | PARTIAL | Causal span graphs are execution provenance, not PROV-style derivation/responsibility |
| IC-24 | Lineage | PARTIAL | Service call graphs ≠ data/model lineage |

**Triad roll-up (OpenTelemetry Specification alone, base profile):**

| Target | Result |
|---|---|
| Authorization reconstructable | **FAIL** (IC-05–IC-08 missing as first-class structure) |
| Justification reconstructable | **FAIL** / weak PARTIAL (no IC-11; evidence only via unconstrained attributes) |
| Validity reconstructable | **FAIL** (rules/constraints/legal context absent) |
| Faithful reconstruction (base) | **FAIL** for OpenTelemetry Specification alone under checklist §8.3 |

**C4 counterargument note:** Baggage, span attributes, and events *can* carry normative fields if a profile defines them. The Specification itself states baggage is primarily for observability indexing and does **not** standardize justification/authorization/validity schemas. A falsifying “tracing profile” would be a separate evaluation unit.

---

## Strengths

1. **Systematic causal execution model** (traces as span DAGs) with cross-process context propagation — strong for reconstructing distributed *process* structure.
2. **First-class timing** on spans, events, and logs.
3. **Resource identity** for locating which entity emitted telemetry.
4. **Open attributes/events/logs** provide an extension surface for domain profiles (including future decision-normative conventions).
5. **Explicit separation of signals** clarifies what is and is not guaranteed when “OpenTelemetry” is present.

---

## Limitations

1. Designed for **observability** (describe software behaviour), not for reconstructing justification, authorization, or validity of legally relevant decisions.
2. No first-class policy, rule, constraint, reliance, or legal-context types in the Specification.
3. Baggage is intentionally narrow: primarily observability annotation/propagation, not a decision-record bus (`overview.md` Baggage Signal).
4. Semantic conventions (companion) standardize many operational domains; they do not, in the core Spec, supply the checklist triad. GenAI conventions live in a separate repository and were not fully scored here.
5. Sampling can drop spans; reconstruction completeness depends on retention/export configuration outside the information model’s guarantees.

---

## What this source does not establish

- That production systems using OpenTelemetry fail or pass faithful reconstruction (empirical deployment claim).
- That no attribute profile could encode the triad (C4 falsification path remains open).
- Completeness of Collector processors, vendor backends, or language SDKs.
- Equivalence between span graphs and W3C PROV-style provenance.

---

## Uncertainties and scope limitations

- GenAI semantic conventions were relocated; a follow-up review of `semantic-conventions-genai` may raise IC-13/IC-14 expressiveness without changing core Spec scores for IC-06–IC-12.
- Metrics were inspected only enough to confirm they record measurements/aggregates, not decision justification structure.
- “Typical usage” in claim C4 is broader than this Spec-only review; this review addresses **model capability**, which already fails base triad reconstruction without a normative profile.

---

## Threats to validity

This review evaluates only the normative specification.

It does not evaluate:

- reference implementations,
- commercial platforms,
- domain-specific extensions,
- organization-specific profiles,
- integrations with other standards.

Therefore the conclusions apply only to the specification itself.

---

## Overall Assessment

**OpenTelemetry Specification v1.59.0 substantially supports reconstruction of distributed execution paths, timing, and resource identity.** It does **not**, by itself, systematically preserve the normative information required for faithful reconstruction of legally relevant AI-supported decisions under the repository checklist.

This supplies direct evidence for inventory claim **C4** at the level of the OpenTelemetry Specification unit: traces (plus baggage/attributes/logs as specified) reconstruct causal execution more readily than justification/authorization/validity. C4 is not globally closed: a dedicated semantic profile could still be evaluated as a composition/falsification attempt.

**Aggregate comparison matrix:** not updated (per task instruction).

**Next research step:** (1) optional focused review of GenAI semantic conventions as a separate unit; (2) OPA/Cedar decision-log review for authorization contrast; (3) if pursuing C4 falsification, specify an explicit OTel attribute/baggage profile mapped to IC-06–IC-12 and re-score as composition.
