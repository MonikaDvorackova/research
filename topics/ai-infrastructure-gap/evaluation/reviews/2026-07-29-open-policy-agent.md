---
id: review-2026-07-29-open-policy-agent
title: "Review: Open Policy Agent (OPA) against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, opa, policy, authorization, reconstruction]
refs: [openPolicyAgent2026]
sut: "Open Policy Agent v1.18.2 — Rego, evaluation model, bundles, decision logging, official docs"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C6]
---

# Review

## Bibliographic Information

**Title:** Open Policy Agent (OPA) — policy engine, Rego language, bundles, and decision logging

**Authors / maintainers:** Open Policy Agent authors / CNCF graduated project

**Venue:** Official OPA documentation and project sources

**Version pin:** **v1.18.2** (GitHub release 2026-07-02)

**DOI / URL:**

- Release: https://github.com/open-policy-agent/opa/releases/tag/v1.18.2
- Docs (versioned): https://www.openpolicyagent.org/docs/v1.18.2/
- No DOI asserted on sources inspected

**Primary sources inspected (SUT @ v1.18.2):**

| Source | Role |
|---|---|
| `docs/docs/index.md` | Introduction / design framing |
| `docs/docs/philosophy/index.md` | Policy vs authorization; decoupling |
| `docs/docs/policy-language.md` | Rego language |
| `docs/docs/management-bundles/index.md` | Policy/data bundles, manifest `revision`, signing |
| `docs/docs/management-decision-logs.md` | Decision log events and fields |
| `docs/docs/management-introduction/index.md` | Management APIs (bundles, decision logs, status, discovery) |
| `docs/docs/rest-api.md` | Data API evaluation; optional `provenance` / `explain` / `metrics` |
| `docs/docs/external-data/index.md` | External data patterns (scope boundary aid) |

**Primary source availability:** Sufficient for a complete review (`HTTP 200` for versioned docs site and tag-pinned markdown sources above).

**Not SUT:** Gatekeeper, Styra DAS, Kubernetes admission ecosystems, org policy libraries, custom log sinks beyond OPA’s documented decision-log event schema, vendor integrations, AI governance products on top of OPA.

---

## 1. Design intent

OPA is a **general-purpose policy engine** that **unifies policy enforcement** by **decoupling policy decision-making from policy enforcement**. Services **query** OPA with structured input (e.g. JSON); OPA evaluates **policies and data** and returns structured results (not limited to boolean allow/deny) (`index.md`; `philosophy`).

A **policy** is a set of rules governing software-service behaviour. **Authorization** is treated as a special kind of policy (who/what may act on which resources), distinct from authentication, and may use authentication outputs (username, attributes, groups, claims) among broader context (`philosophy`).

OPA is **domain-agnostic**: policies may express many invariants (access, egress, placement, registries, capabilities, time-of-day, etc.) (`index.md`).

Management design: OPA enables distributed enforcement with in-memory policy/data; optional management APIs support **bundle distribution**, **decision telemetry (decision logs)**, status, and discovery. OPA **does not** ship a control-plane service out of the box (`management-introduction`).

**Intent for this review:** evaluate whether OPA’s **policy representation**, **evaluation**, **bundles**, and **decision logs** preserve information needed for faithful reconstruction of legally relevant AI-supported decisions—not whether OPA is a good policy engine in general.

---

## 2. Observed OPA capabilities

(First-class / documented only.)

### 2.1 Rego and evaluation model

- **Rego** is OPA’s declarative policy language for asserting over structured documents (JSON-like), inspired by Datalog (`policy-language.md`).
- Callers supply **input**; OPA evaluates policies against **policies + data** to produce **results** (`index.md`; Data API in `rest-api.md`).
- Decisions may be boolean or arbitrary structured documents (`index.md`).

### 2.2 Bundles

- Bundles are gzipped tarballs of policies and/or data, loadable without restart (`management-bundles`).
- Optional `.manifest` includes **`revision`** string identifying the bundle revision; also `rego_version` / per-file overrides (`management-bundles` Bundle File Format).
- Optional **bundle signing** and verification (`management-bundles` Signing).
- HTTP ETag / If-None-Match used for bundle caching/revision identity at the service API layer (`management-bundles` Caching).

### 2.3 Decision logging

When decision logging is enabled, OPA reports events that “describe policy queries,” including “the policy that was queried, the input to the query, bundle metadata, and other information that enables auditing and offline debugging of policy decisions.” API responses can include `decision_id` (`management-decision-logs.md`).

Documented decision-log event fields include (non-exhaustive; see source table): `labels`, `decision_id`, `trace_id`, `span_id`, `bundles` (with per-bundle `revision`), `path`, `query`, `input`, `result`, `requested_by`, optional HTTP header capture, `timestamp`, `metrics`, `erased` / `masked`, plus additional documented fields in the same table (`management-decision-logs.md`).

OPA supports masking/dropping events via `system.log` policies and rate limiting (`management-decision-logs.md`).

### 2.4 REST evaluation provenance / explain (API features)

- Data API supports `provenance=true` returning OPA build/version info and activated **bundle revisions** inline (`rest-api.md` Provenance)—**engine/bundle provenance**, not data-lineage provenance.
- Optional `explain` and `metrics` query parameters for evaluation explanation/performance (`rest-api.md`).

### 2.5 Explicit non-capabilities (observation)

OPA does not define first-class types for: legal jurisdiction, AI model versions, prompts, relied-upon vs available evidence for non-policy facts, human multi-party approval workflows, or durable storage of decision logs (it **emits** logs to console/HTTP/plugins; retention is outside OPA).

---

## 3. Checklist interpretation

Nearest claim-inventory item: **C6** (OPA/Cedar-style decision logs necessary but not sufficient for full justification/validity reconstruction in AI-mediated decisions).

Interpretive distinctions required by this task:

| Distinction | Application to OPA |
|---|---|
| **Policy representation vs policy provenance** | Rego + bundles represent policy content; `bundles[].revision` / manifest `revision` / API `provenance.bundles` identify **which bundle revision** was active—not full authorship/chain-of-custody provenance of every rule clause. |
| **Policy evaluation vs legal justification** | Evaluation yields `result` from Rego against `input`; that is an **authorization/policy decision**, not automatically a legal justification record for an AI-supported business decision. |
| **Authorization decisions vs preservation of decision knowledge** | Decision logs preserve query path, input, result, and bundle revision for **policy queries**; they do not by themselves preserve the full checklist triad for legally relevant AI decisions (model evidence reliance, non-policy constraints, legal context, etc.). |

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside OPA’s legitimate documented purpose.

Scores are **independent** of PROV-DM, OpenTelemetry, ML Metadata, and OpenLineage reviews.

### System state — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Decision-log field `input` retains the structured input document supplied to the policy query; docs state events include input for auditing/debugging (`management-decision-logs.md`). Callers may put arbitrary structured context into input (`index.md`). |
| **Justification** | When decision logging is used as documented, OPA systematically can preserve the **decision-time input document**—substantial support for reconstructing the state *as presented to the policy engine*. |
| **Why not higher** | OPA does not model or snapshot ambient system state itself; completeness of “system state” depends on what the integrating service puts in `input`. No first-class system-state schema. |
| **Confidence** | High |

### Decision process — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Query evaluation via Data API; decision logs record `path` / `query`, `result`, `decision_id`, `timestamp` (`rest-api.md`; `management-decision-logs.md`). Optional `explain` for evaluation traces at query time (`rest-api.md`). |
| **Justification** | Substantial, systematic support for reconstructing **policy evaluation episodes** (what was asked, what was returned, when, under which decision id). |
| **Why not higher** | This is the process of **policy evaluation**, not a general multi-step legally relevant decision workflow (human approvals, model inference steps, etc.). `explain` is an API option for a live query response, not specified as a durable decision-log field in the decision-log field table excerpted above. |
| **Confidence** | High |

### Evidence — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | `input` in decision logs; policies reason over structured input and `data` (`index.md`; `management-decision-logs.md`). |
| **Justification** | Substantial support for reconstructing evidence **as supplied to OPA** for the policy query. |
| **Why not higher** | No first-class IC-11 “relied upon vs available” within input; no IC-12 excluded evidence. Masking/erasure can remove fields from logs (`erased`/`masked`). External facts not in `input`/`data` are out of band. |
| **Confidence** | High |

### Rules — **Score: 3**

| Field | Content |
|---|---|
| **Evidence** | Rego as first-class policy language (`policy-language.md`); policies packaged/distributed in bundles with optional manifest `revision` (`management-bundles`); decision logs record `path` and `bundles[_].revision` used to produce the decision (`management-decision-logs.md`). |
| **Justification** | Explicit and systematic support for representing, distributing, version-identifying (via bundle revision), and logging **which policy path** produced a decision—OPA’s core purpose. |
| **Why not higher** | N/A (already maximum). Note: bundle `revision` identifies a bundle snapshot string; it does not by itself expand to clause-level legal citation unless encoded in Rego/data. |
| **Confidence** | High |

### Human context — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Philosophy: policies often use authentication results (username, attributes, groups, claims) (`philosophy`). Example policies reason about users/resources (`index.md`). `requested_by` in decision logs identifies the **client** that executed the query (`management-decision-logs.md`). |
| **Justification** | Partial: human/machine identity may appear inside `input` by convention and is discussed as typical policy context, but OPA defines no first-class actor/authority schema. |
| **Why not higher** | No mandatory principal model; `requested_by` is the OPA API client address/identifier, not necessarily the end-user principal. Multi-party authority is not a first-class construct. |
| **Confidence** | High |

### Temporal continuity — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Decision-log `timestamp` (RFC3339/RFC3999 per docs table); bundle `revision` at evaluation time in logs and optional Data API `provenance.bundles` (`management-decision-logs.md`; `rest-api.md` Provenance; `management-bundles` manifest `revision`). |
| **Justification** | Substantial support for **when** a policy decision was made and **which bundle revision** was active then. |
| **Why not higher** | No first-class bitemporal legal as-of model; clock domain beyond timestamp string; historical reconstruction of non-bundle external data depends on what was embedded in `input`/`data` at the time. |
| **Confidence** | High |

### Checklist marks (first-class OPA)

| ID | Mark | Notes |
|---|---|---|
| IC-01 | PASS | `decision_id` (when decision logging enabled) |
| IC-02 | PASS/PARTIAL | `result` (policy decision output; may be structured) |
| IC-03 | PASS | `timestamp` |
| IC-04 | PARTIAL | via `input` conventions; `requested_by` = API client |
| IC-05 | PARTIAL | only if encoded in policy/`input`; no first-class authority type |
| IC-06 | PASS | Rego policies / `path` |
| IC-07 | PASS | `bundles[_].revision` / manifest revision |
| IC-08 | PASS/PARTIAL | rule path + Rego content in bundle; not automatic clause enumeration unless authored that way |
| IC-09 | PARTIAL | expressible in Rego; not a separate constraint object model |
| IC-10 | PASS | `input` (+ `data` in engine) |
| IC-11 | FAIL | no reliance distinction |
| IC-12 | FAIL | not first-class (masking removes rather than records exclusion reasons) |
| IC-13 | FAIL/PARTIAL | only if model version placed in `input` by caller |
| IC-14 | **N/A** | outside OPA purpose unless carried in `input` by an app (not credited as OPA concept) |
| IC-15–IC-16 | PARTIAL | only via `input` |
| IC-17 | PARTIAL | expressible in Rego/`input` thresholds; not a dedicated confidence type |
| IC-18 | PARTIAL | expressible in policy; not first-class assumption records |
| IC-19 | PARTIAL | decision timestamp + bundle revision |
| IC-20 | **N/A** | legal jurisdiction not an OPA concept |
| IC-21 | PARTIAL | bundle signing documents integrity for bundles |
| IC-22 | PARTIAL | bundle signatures; not end-user decision non-repudiation objects |
| IC-23–IC-24 | PARTIAL | API “provenance” = build/bundle metadata, not data lineage |

**Triad roll-up (OPA alone, base profile for legally relevant AI-supported decisions):**

| Target | Result |
|---|---|
| Authorization reconstructable | **PASS / strong PARTIAL** for *policy-query authorization* when decision logs + bundle revisions retained as documented |
| Justification reconstructable | **PARTIAL/FAIL** for AI-mediated justification beyond policy input/result (no IC-11; model/evidence semantics not first-class) |
| Validity reconstructable | **PARTIAL** (policy constraints expressible; legal validity N/A / not first-class) |
| Faithful reconstruction (full triad for AI decisions) | **FAIL as sole SUT** under checklist §8.3 for legally relevant AI-supported decisions |

---

## 5. Evaluation boundary

Only capabilities explicitly represented by OPA itself receive credit:

- Rego policies, evaluation semantics, bundles (including manifest `revision` and documented signing), decision-log event fields, and documented Data API options (`provenance`, `explain`, `metrics`) may be credited **where documented**.
- External audit warehouses, custom policy metadata conventions, organization-specific Rego libraries, Gatekeeper/Styra/K8s ecosystems, and downstream AI governance products receive **no** credit.
- Implementation practices (e.g. “we always put model_id in input”) do **not** influence scoring unless specified as a first-class OPA concept.

---

## 6. Threats to validity

- Spec/docs-only: decision logging and bundle download must be **configured**; defaults may not retain logs.
- Masking/dropping/rate-limiting can omit fields or events by design.
- `explain` aids live debugging; durable reconstruction depends on what is **logged**, not what can be returned once.
- Bundle `revision` semantics are a string chosen by the bundle service—quality varies.
- Ecosystem project mentions on docs pages are explicitly out of SUT scope.
- Authorization success for *OPA queries* must not be conflated with legal justification of AI decisions.

---

## 7. Remaining uncertainty

- Whether richer structured `result` objects (obligations, reasons) authored in Rego can close more of IC-08/IC-09 in practice—possible, but depends on policy authoring (composition/profile), not credited beyond expressibility notes above.
- Interaction of external data (`external-data` docs) with decision-time completeness when data is pulled live—boundary case for future focused review.
- Claim **C6** receives unit-level support here but is **not** updated in aggregate claim inventories by this task.

---

## 8. Overall assessment

**OPA v1.18.2 systematically supports representation and evaluation of policy-as-code (Rego), distribution/version identification of policy via bundles, and—when decision logging is enabled—durable records of policy queries (`decision_id`, `path`/`query`, `input`, `result`, `timestamp`, bundle `revision`).** That is strong for reconstructing **authorization/policy decisions**.

OPA does **not**, by itself, systematically preserve the full information required for faithful reconstruction of **legally relevant AI-supported decisions** under the checklist: it does not first-class model AI evidence reliance, legal context, or non-policy justification structure. Distinguishing **policy evaluation** from **legal justification** and **authorization decisions** from **complete decision-knowledge preservation** is essential.

This aligns with treating OPA as central evidence for claim-inventory **C6** at the unit level (necessary for authorization reconstruction; not sufficient alone for the full AI decision triad).

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims.
