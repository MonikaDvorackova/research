---
id: review-2026-07-29-openlineage
title: "Review: OpenLineage specification against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, openlineage, lineage, reconstruction]
refs: [openLineage2026specification]
sut: "OpenLineage specification (project release 1.52.0; core JSON Schema $id 2-0-2)"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C5]
---

# Review

## Bibliographic Information

**Title:** OpenLineage Specification (core object model, run lifecycle, and standard facets)

**Authors / maintainers:** OpenLineage project contributors (LF AI & Data / OpenLineage community)

**Venue:** OpenLineage specification repository and published documentation

**Version pin:**

- **Project / docs release:** **1.52.0** (GitHub release 2026-07-23; docs site versioned `1.52.0`)
- **Core JSON Schema `$id`:** `https://openlineage.io/spec/2-0-2/OpenLineage.json` (SCHEMAVER MODEL-REVISION-ADDITION; versioned independently of library releases per `spec/Versioning.md`)

**DOI / URL:**

- Release: https://github.com/OpenLineage/OpenLineage/releases/tag/1.52.0
- Spec narrative: https://github.com/OpenLineage/OpenLineage/blob/1.52.0/spec/OpenLineage.md
- Spec schema: https://github.com/OpenLineage/OpenLineage/blob/1.52.0/spec/OpenLineage.json
- OpenAPI companion: https://github.com/OpenLineage/OpenLineage/blob/1.52.0/spec/OpenLineage.yml
- Object model docs: https://openlineage.io/docs/spec/object-model/ (version 1.52.0)
- No DOI asserted on sources inspected

**Primary sources inspected (SUT):**

| Source @ `1.52.0` | Role |
|---|---|
| `spec/OpenLineage.md` | Normative narrative: core concepts, lifecycle, **Standard Facets** |
| `spec/OpenLineage.json` | Formal JsonSchema for RunEvent / JobEvent / DatasetEvent and core entities |
| `spec/OpenLineage.yml` | OpenAPI for HTTP-based implementations (companion to core schema) |
| `spec/Versioning.md` | Spec versioning rules |
| Official facet schemas under `spec/facets/` named as **Standard Facets** in `OpenLineage.md` (e.g. ownership, schema, columnLineage, nominalTime, parent, errorMessage) | First-class standard facets |
| https://openlineage.io/docs/spec/object-model/ (1.52.0) | Design intent / object-model documentation aligned to the release |

**Primary source availability:** Sufficient for a complete specification review (`HTTP 200` for core markdown, JSON Schema, OpenAPI, standard facet schemas, and versioned object-model docs).

**Note:** `spec/Naming.md` at this tag states it is obsolete and points to the website naming conventions page; naming details were not required for scoring beyond identity fields already in `OpenLineage.json`.

---

## 1. Design intent

OpenLineage is designed to enable **large-scale observation of datasets as they move through complex pipelines**, emitting **real-time lineage events** as datasets are created and transformed, and optionally **design-time lineage** as transformations are defined or altered (`object-model` docs, v1.52.0).

The specification cares **how Datasets come into being**, not merely that relationships exist. The core model therefore includes both **Jobs** and **Datasets**. Backends learn about datasets primarily by receiving job observations; a lineage graph is formed by weaving together many job observations across platforms.

Event kinds:

- **RunEvent** — runtime job-run state updates  
- **JobEvent** — static/design job metadata (not associated with a Run)  
- **DatasetEvent** — static/design dataset metadata (not associated with a Run)

This intent is **data/job lineage observation for pipelines**, not reconstruction of legally relevant decision justification, authorization, or validity.

---

## 2. Observed specification capabilities

(Only first-class core entities and **Standard Facets** listed in `OpenLineage.md` / corresponding facet schemas. No credit for custom facets.)

### 2.1 Core entities (`OpenLineage.md`, `OpenLineage.json`)

| Construct | Observed capability |
|---|---|
| **RunEvent** | Observed state of a job run; requires START and one of COMPLETE/FAIL/ABORT; optional RUNNING/OTHER; `eventTime`, `producer`, `schemaURL`; `run`, `job`, optional `inputs`/`outputs` |
| **Job** | Process definition consuming/producing datasets; identified by `namespace` + `name` |
| **Run** | Job instance with start/completion; globally unique `runId` (UUID) |
| **Dataset** | Abstract representation of data; `namespace` + `name` (typically from physical location) |
| **InputDataset / OutputDataset** | Datasets attached as run inputs/outputs, with optional input/output facets |
| **Facet** | Atomic metadata attached to Run, Job, or Dataset; same-name facet replaces prior instance |
| **JobEvent / DatasetEvent** | Design-time metadata events without a Run |

### 2.2 Lifecycle (`OpenLineage.md`)

Metadata is captured when a run transitions state. Metadata is **additive** across events (e.g. additional inputs/outputs may appear later without re-emitting earlier ones). Examples of collected metadata at START vs COMPLETE include run/job ids, event type/time, optional source location/version, schemas, and I/O.

### 2.3 Standard Facets (explicitly listed in `OpenLineage.md`)

| Area | Standard facets (first-class) |
|---|---|
| Run | `nominalTime`, `parent`, `errorMessage` |
| Job | `sourceCodeLocation`, `sourceCode`, `sql`, `ownership` |
| Dataset | `schema`, `dataSource`, `lifecycleStateChange`, `version`, `columnLineage`, `ownership` |
| Input | `dataQualityMetrics`, `dataQualityAssertions`, `inputStatistics` |
| Output | `outputStatistics` |

### 2.4 Explicitly not first-class in the specification

The core schema and Standard Facets list do **not** define governing policy, policy versions, applicable authorization rules, legal jurisdiction, decision outcomes (allow/deny), relied-upon vs available evidence for a normative decision, prompts, or cryptographic signatures.

**Custom facets** are explicitly allowed as project-prefixed extensions (`OpenLineage.md` Facets / Custom Facet Naming) and are **out of credit** under the evaluation boundary unless promoted into the standard list.

---

## 3. Checklist interpretation

OpenLineage maps naturally to **data lineage / job-run observation** (charter kill-list “data and model provenance”; claim inventory **C5** as the nearest registered claim about provenance vs justification).

Under checklist v0.1.0:

- Strongest fit: IC-10-like “what datasets were used/produced”, IC-23/IC-24 lineage, temporal event ordering, partial ownership.
- Weak/absent fit: IC-05–IC-09 (authority/policy/rules/constraints), IC-11–IC-12 (reliance/exclusion for decisions), IC-20 legal context.

Scores below evaluate **specification expressiveness only**, not producers, Marquez, Spark/Airflow integrations, or backends.

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside OpenLineage’s legitimate design intent as documented.

Scores do **not** use conclusions from PROV-DM, OpenTelemetry, or ML Metadata reviews.

### System state — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | `Dataset` as abstract data with namespace/name; Standard Facets `schema`, `dataSource`, `version`, `lifecycleStateChange` (`OpenLineage.md` Dataset Facets; `OpenLineage.json` Dataset). Object model: observe datasets as they move through pipelines. |
| **Justification** | Partial support for reconstructing *dataset* identity and selected static/dynamic dataset metadata related to pipeline observation. |
| **Why not higher** | No first-class model of decision-time application/system state beyond dataset/job observation; schema/version facets describe datasets, not a bound decision-episode system snapshot. |
| **Confidence** | High |

### Decision process — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | `Job` / `Run` / `RunEvent` with required START and terminal COMPLETE/ABORT/FAIL; additive lifecycle metadata (`OpenLineage.md` Core concepts, Lifecycle; `OpenLineage.json` `eventType` enum). Object model: OpenLineage cares how datasets come into being via Jobs. Standard `parent` run facet for spawned runs. |
| **Justification** | Systematic support for reconstructing data-processing *job-run* process structure and parent/child run hierarchy. |
| **Why not higher** | “Decision process” here is pipeline job execution, not normative decision-making (authorization/justification/validity). No first-class decision-gate or permit/deny semantics. |
| **Confidence** | High |

### Evidence — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | First-class `inputs` / `outputs` on RunEvent; Standard Facets `columnLineage`, `inputStatistics`, `outputStatistics`, data-quality input facets (`OpenLineage.md`; `ColumnLineageDatasetFacet.json`). |
| **Justification** | Substantial, systematic support for which datasets (and optionally columns) participated as job inputs/outputs—core evidential lineage for data pipelines. |
| **Why not higher** | No first-class distinction between evidence available to a *legally relevant decision* vs evidence relied upon (IC-11), nor excluded evidence (IC-12). Column lineage describes field derivation, not normative reliance. |
| **Confidence** | High |

### Rules — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | No policy/rule/constraint entities in `OpenLineage.json`. Standard `sql` job facet captures SQL query text (`OpenLineage.md` Job Facets)—a job description, not governing authorization/validity rules. Custom facets are excluded from credit. |
| **Justification** | Governing rules/policies are not addressed as first-class specification concepts. |
| **Why not higher** | Crediting SQL text or custom facets as “rules” would violate the evaluation boundary. |
| **Confidence** | High |

### Human context — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Standard `ownership` Job and Dataset facets; owners identified by recommended URN-like names (e.g. `user:jdoe`, `team:data`) with optional ownership type (`OwnershipDatasetFacet.json`; `OpenLineage.md`). |
| **Justification** | Partial support for recording owners of jobs/datasets as first-class standard facets. |
| **Why not higher** | Ownership ≠ authority/delegation/accountability model for decision authorization; no required actor identity for a decision episode; run-level human approval constructs are not standard facets. |
| **Confidence** | High |

### Temporal continuity — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Required `eventTime` on events (`OpenLineage.json` BaseEvent); run lifecycle timestamps via event sequence; Standard `nominalTime` run facet for scheduled vs actual time (`OpenLineage.md`). |
| **Justification** | Substantial support for temporal ordering of lineage observations and nominal schedule time. |
| **Why not higher** | No first-class binding of historically applicable *policy/model criteria versions* to a decision time; dataset `version` facet is datastore versioning (e.g. Iceberg snapshot), not decision-normative temporality (IC-07/IC-19 as legal/policy as-of). |
| **Confidence** | High |

### Checklist marks (first-class only)

| ID | Mark | Notes |
|---|---|---|
| IC-01 | PARTIAL | `runId` / job identity; not a decision-episode type |
| IC-02 | PARTIAL | Outputs / COMPLETE|FAIL|ABORT; not decision outcome |
| IC-03 | PARTIAL | `eventTime` / nominalTime |
| IC-04 | PARTIAL | ownership facets |
| IC-05 | FAIL | Not first-class |
| IC-06–IC-09 | FAIL | Not first-class |
| IC-10 | PASS | inputs/outputs |
| IC-11–IC-12 | FAIL | Not first-class |
| IC-13 | PARTIAL | dataset/job versioning & sourceCodeLocation—not model decision binding |
| IC-14 | **N/A** | Outside design intent |
| IC-15 | PARTIAL | Jobs as processes; not tool-call decision semantics |
| IC-16 | PARTIAL | `dataSource` facet / namespaces—not general external-service authorization inputs |
| IC-17–IC-18 | FAIL | Not first-class |
| IC-19 | PARTIAL | event/nominal time |
| IC-20 | **N/A** | Outside design intent |
| IC-21 | FAIL | Not first-class |
| IC-22 | **N/A** | Outside design intent |
| IC-23–IC-24 | PASS | Core lineage purpose + columnLineage standard facet |

**Triad roll-up (specification alone, base profile):** Authorization **FAIL**; Justification **PARTIAL/FAIL**; Validity **FAIL**; Faithful reconstruction (base) **FAIL**.

---

## 5. Evaluation boundary

This review evaluates only capabilities explicitly documented or structurally represented by the OpenLineage specification (core JsonSchema/narrative and **Standard Facets** named in `OpenLineage.md`).

- Generic extensibility, **custom facets**, vendor extensions, and organization-specific conventions **do not** receive credit unless they are first-class concepts defined by the specification (promoted standard facets).
- Implementation behaviour (Marquez, Spark/Airflow producers, collectors, backends) **must not** influence scoring.
- `BaseFacet.additionalProperties: true` in JSON Schema is an extension hook; it does **not** by itself establish checklist support.

---

## 6. Threats to validity

- Spec-only evaluation: real deployments may emit richer or poorer metadata than the standard requires.
- Standard facet *existence* does not imply producers always populate them.
- Object-model website text is documentation aligned to 1.52.0; formal authority for structure remains `OpenLineage.json` + `OpenLineage.md`.
- Schema `$id` **2-0-2** vs project release **1.52.0** can confuse version citation; both are recorded explicitly.
- Adjacent ecosystem docs/integrations could inflate perceived capability if mistakenly treated as part of the SUT.

---

## 7. Remaining uncertainty

- Whether future standard facets could encode decision-normative fields without leaving OpenLineage (would require a new spec revision and re-review).
- How often `ownership` URNs correspond to accountable legal/organisational roles—empirical, out of scope.
- Claim **C5** receives unit-level support (lineage observation ≠ justification triad) but is not updated in aggregate inventories by this task.

---

## 8. Overall assessment

**OpenLineage specification 1.52.0 (core schema 2-0-2) systematically preserves job-run and dataset lineage observations: which jobs ran, which datasets were inputs/outputs, with standard support for schema, column lineage, ownership, and event timing.** It does **not**, by itself, systematically preserve the normative information required for faithful reconstruction of legally relevant AI-supported decisions (authorization policy/rules, justification reliance, validity constraints).

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims.

**Next research step (optional):** authorization-focused SUT (e.g. OPA/Cedar decision logs), or a declared composition of OpenLineage lineage + policy decision records with explicit binding.
