---
id: review-2026-07-29-google-ml-metadata
title: "Review: Google ML Metadata (MLMD) against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, ml-metadata, lineage, reconstruction]
refs: [google2026mlMetadata]
sut: "Google ML Metadata (MLMD) v1.21.0 — data model and documented Metadata Store capabilities"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C5]
---

## Review

## Bibliographic Information

**Title:** ML Metadata (MLMD) — library and Metadata Store data model

**Authors / maintainers:** Google (open-source project `google/ml-metadata`)

**Venue:** Open-source library (GitHub / PyPI); documentation via project docs and TensorFlow Extended guide pages

**Year / version pinned:** **v1.21.0** (GitHub release 2026-06-09; PyPI package `ml-metadata` 1.21.0)

**DOI / URL:**

- Release: <https://github.com/google/ml-metadata/releases/tag/v1.21.0>
- Repository: <https://github.com/google/ml-metadata>
- Docs (tag): <https://github.com/google/ml-metadata/blob/v1.21.0/docs/index.md>
- Published site: <https://google.github.io/ml-metadata/>
- No DOI asserted on sources inspected for this review

**Primary sources inspected (SUT):**

| Source @ v1.21.0 | Role |
|---|---|
| `ml_metadata/proto/metadata_store.proto` | Normative data model |
| `ml_metadata/proto/metadata_store_service.proto` | Record/retrieve API surface |
| `docs/index.md` | Documented concepts, intended questions, data-model narrative |

**Companion (not scored as SUT):** TFX-hosted MLMD guide / tutorial links; README install notes.

**Documentation gap:** README links to `g3doc/get_started.md`, which returns **404** at `v1.21.0` and `master`. This review does not rely on that missing file.

**Evaluated unit:** MLMD **data model** and **documented Metadata Store capabilities** for recording/retrieving ML workflow metadata (artifacts, executions, events, contexts, lineage).

**Not evaluated:** TFX orchestration, vendor platforms, organization-specific type schemas, custom property conventions, or integrations with other standards.

---

## Evaluation boundary

This review evaluates only capabilities documented or structurally represented
by MLMD itself.

Capabilities that depend on organization-specific schemas, conventions,
external services, or custom metadata profiles are not credited unless they are
documented as first-class MLMD concepts.

In particular, `properties` / `custom_properties` maps are **not** treated as
evidence that MLMD systematically preserves any reconstruction checklist item
beyond what first-class types and relations already express.

---

## Summary

MLMD is a library for recording and retrieving metadata associated with ML developer and data scientist workflows. It can be used independently of TFX. The Metadata Store records metadata about pipeline artifacts, component/step executions, and pipeline lineage. The documented data model centres on typed **Artifacts** and **Executions** linked by **Events**, optionally grouped by **Contexts** via **Attribution** and **Association**, with **LineageGraph** aggregation and query APIs.

Documented example questions include which dataset a model trained on, which pipeline/training run created a model, which TensorFlow version created a model, and when a failed model was pushed. The guide likens this metadata to logging for debugging interconnected pipeline parts.

---

## 1. Observed capabilities (explicitly documented / structural)

The following are taken only from primary sources (no reconstruction scoring yet).

### 1.1 First-class structural types (`metadata_store.proto`)

| Construct | Observed capability |
|---|---|
| `Artifact` / `ArtifactType` | Typed artifacts with `uri`, optional `name`/`external_id`, lifecycle `State` (e.g. PENDING, LIVE, DELETED, ABANDONED, REFERENCE), create/update timestamps; type schema via `ArtifactType.properties`; optional system base types DATASET, MODEL, METRICS, STATISTICS |
| `Execution` / `ExecutionType` | Typed workflow step/component runs with `last_known_state` (NEW→RUNNING→COMPLETE\|CACHED\|FAILED\|CANCELED), create/update timestamps; optional system base types TRAIN, TRANSFORM, PROCESS, EVALUATE, DEPLOY; optional input/output `ArtifactStructType` on the execution type |
| `Event` | Links `artifact_id` ↔ `execution_id` with `Type` (DECLARED_INPUT/OUTPUT, INPUT/OUTPUT, INTERNAL_*, PENDING_OUTPUT), optional path, `milliseconds_since_epoch` |
| `Context` / `ContextType` | Conceptual grouping of artifacts/executions (docs examples: projects, pipeline runs, experiments, owners); Attribution/Association edges; ParentContext hierarchy |
| `LineageGraph` | Bundle of types, nodes (artifacts/executions/contexts), and edges (events/attributions/associations/parent_contexts) |
| `Value` | Typed scalar/struct/any values for properties |

### 1.2 Documented Metadata Store behaviour (`docs/index.md`)

- Registers metadata about artifacts, executions, and pipeline lineage.
- Events record artifacts used and produced by an execution; MLMD can recurse from an artifact to upstream inputs.
- Intended analyses include: dataset used for training; hyperparameters used; pipeline/training run that created a model; TensorFlow version; push time of a failed model.
- Supported functional examples include DAGs of related executions and I/O artifacts under a context; reverse event recursion; forward artifact impact; detecting prior executions with same inputs; recording/querying workflow-run context (e.g. owner, changelist) and grouping lineage by experiments/projects.

### 1.3 Explicitly absent from first-class MLMD concepts (observation)

Primary sources do **not** define first-class types or relations for: governing policy, policy version, applicable rules, constraints, authorization outcomes, justification criteria, relied-upon vs merely available evidence beyond event input/output typing, legal/jurisdictional frame, prompts, confidence scores as decision gates, or cryptographic signatures.

---

## 2. Reconstruction Capabilities (repository interpretation)

Scores use the repository scale:

- 0 = Not addressed
- 1 = Mentioned or partially supported
- 2 = Substantially supported
- 3 = Explicitly and systematically supported

N/A = outside MLMD’s legitimate documented scope.

Scores do **not** use conclusions from the PROV-DM or OpenTelemetry reviews.

### Template criteria

#### System state — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | `Artifact` with `uri`, `state`, type identity, and timestamps (`metadata_store.proto` Artifact); system base types DATASET/MODEL/METRICS/STATISTICS; docs: Metadata Store holds artifact metadata from pipeline components (`docs/index.md` §§ Metadata store, Data model). |
| **Justification** | MLMD systematically represents durable ML pipeline artifact instances and their known lifecycle states as first-class store objects—substantial support for reconstructing *artifact-centric* pipeline state. |
| **Why not higher** | No first-class “system state at decision time” or decision-episode state model; runtime application/service state outside artifacts/executions is not a documented MLMD concept. |
| **Confidence** | High |

#### Decision process — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | `Execution` as “record of a component run or a step in an ML workflow” (`docs/index.md` Data model); `Event` links used/produced artifacts; docs: show DAG of related executions and I/O under a context; system execution base types TRAIN/TRANSFORM/PROCESS/EVALUATE/DEPLOY. |
| **Justification** | First-class executions + events systematically reconstruct ML *pipeline step* process structure and input/output flow. |
| **Why not higher** | Process here is workflow/component execution, not normative decision-making (authorization/justification/validity gates). No first-class decision outcome or permit/deny structure. |
| **Confidence** | High |

#### Evidence — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | `Event` INPUT/OUTPUT (and declared/internal variants) between executions and artifacts; docs: events record every artifact used and produced; recurse to upstream inputs; example questions about which dataset trained a model (`docs/index.md`). |
| **Justification** | First-class input/output event typing substantially supports reconstructing which artifacts participated in a step—core evidential lineage for ML pipelines. |
| **Why not higher** | No first-class distinction between evidence available vs evidence relied upon for a *decision* (IC-11), nor excluded evidence (IC-12). Event type nuances (`DECLARED_*` / `INTERNAL_*`) address pipeline declaration/caching semantics, not justification reliance. |
| **Confidence** | High |

#### Rules — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | No policy/rule/constraint messages in `metadata_store.proto`. Docs list hyperparameters as an example *question* MLMD can help answer, but hyperparameters are not a first-class type—only illustratively answerable via typed properties in examples (`docs/index.md` intro questions; example `ExecutionType`/artifact properties in integrate-workflow section). Under the evaluation boundary, property-based encoding is not credited. |
| **Justification** | Governing rules/policies are not addressed as first-class MLMD concepts. |
| **Why not higher** | Any score >0 would require treating extensible properties or org schemas as systematic rule preservation. |
| **Confidence** | High |

#### Human context — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | `ContextType` / `Context` for conceptual groups; docs examples include “owners”, “track the owner and changelist used for a workflow run” (`docs/index.md` Data model; MLMD Functionality). Proto comment on ContextType names: “e.g., Pipeline, Task, Session, User, etc.” (`ContextType.name`). Attribution/Association bind artifacts/executions to contexts. |
| **Justification** | Partial support: workflow grouping contexts can carry owner-like shared information as documented examples, but there is no first-class actor/authority/responsibility model. |
| **Why not higher** | “User”/“owner” appear as naming/examples, not as systematic agent, delegation, or authorization constructs. No required human-identity schema. |
| **Confidence** | High |

#### Temporal continuity — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | `create_time_since_epoch` / `last_update_time_since_epoch` on Artifact, Execution, Context; `Event.milliseconds_since_epoch` (`metadata_store.proto`). Docs ask “When was the failed model pushed?” as an intended lineage/debug question. |
| **Justification** | First-class timestamps on core nodes/edges substantially support temporal ordering of pipeline metadata events. |
| **Why not higher** | No first-class binding of historically applicable policy/model *criteria* versions to a decision time (beyond artifact/execution type `version` strings and timestamps of metadata records). Not a bitemporal decision-validity model. |
| **Confidence** | High |

### Checklist mapping (expressiveness of first-class MLMD constructs)

| ID | Category | Mark | Notes |
|---|---|---|---|
| IC-01 | Decision identity | PARTIAL | Execution/Artifact/Context ids exist; no decision-episode type |
| IC-02 | Decision outcome | PARTIAL | Output artifacts / execution state; not a decision outcome relation |
| IC-03 | Decision time | PARTIAL | Event and create/update timestamps |
| IC-04 | Actor(s) | PARTIAL | Context “owner”/“User” examples only |
| IC-05 | Authority | FAIL | Not first-class |
| IC-06 | Governing policy | FAIL | Not first-class |
| IC-07 | Policy version | FAIL | Type `version` ≠ governing policy version |
| IC-08 | Applicable rules | FAIL | Not first-class |
| IC-09 | Constraints | FAIL | Not first-class |
| IC-10 | Evidence used | PASS | Event INPUT (+ declared/internal variants) to artifacts |
| IC-11 | Evidence relied upon | FAIL | No reliance construct beyond I/O events |
| IC-12 | Excluded evidence | FAIL | Not first-class |
| IC-13 | Model version | PARTIAL | MODEL artifacts + type/artifact version fields; not decision-time normative binding |
| IC-14 | Prompts | **N/A** | Outside documented MLMD purpose (ML pipeline/workflow metadata) |
| IC-15 | Tools | PARTIAL | Executions as components/steps; not tool-call semantics |
| IC-16 | External services | FAIL | Not first-class |
| IC-17 | Confidence | FAIL | Not first-class |
| IC-18 | Assumptions | FAIL | Not first-class |
| IC-19 | Temporal context | PARTIAL | Metadata/event times; limited as-of semantics |
| IC-20 | Legal context | **N/A** | Outside documented MLMD purpose |
| IC-21 | Integrity information | FAIL | Not first-class (storage backend choice ≠ integrity metadata model) |
| IC-22 | Signatures | **N/A** | Outside documented MLMD purpose |
| IC-23 | Provenance | PASS | Events + lineage recursion are first-class documented capabilities |
| IC-24 | Lineage | PASS | LineageGraph / documented lineage features |

**Triad roll-up (MLMD alone, base profile):**

| Target | Result |
|---|---|
| Authorization reconstructable | **FAIL** (IC-05–IC-08 absent as first-class) |
| Justification reconstructable | **PARTIAL/FAIL** (IC-10 strong; IC-11–IC-12 and criteria absent) |
| Validity reconstructable | **FAIL** (rules/constraints/legal N/A or absent) |
| Faithful reconstruction (base) | **FAIL** for MLMD alone under checklist §8.3 |

---

## Strengths

1. First-class **artifact–execution–event** graph for ML pipeline lineage.
2. Explicit **input/output event typing** and documented upstream recursion.
3. **Contexts** for grouping runs/experiments/projects with attribution/association.
4. System-defined **base types** for common ML artifacts and execution intents (DATASET, MODEL, TRAIN, EVALUATE, etc.).
5. Clear documentation of intended debugging/lineage questions (dataset, run identity, framework version, push timing).

---

## Limitations

1. Scope is **ML workflow/pipeline metadata**, not legally relevant decision justification/authorization/validity.
2. No first-class policy, rule, constraint, reliance, or authority constructs.
3. Extensible properties can store arbitrary values in deployments; under the evaluation boundary they do **not** count as systematic MLMD capabilities.
4. Human/organisational context is only weakly represented via optional context examples (owner/user), not a responsibility model.
5. Missing `g3doc/get_started.md` limits access to README-advertised introductory material (not used as positive evidence here).

---

## 3. Threats to validity

This review evaluates only the MLMD data model and official documentation at v1.21.0.

It does not evaluate:

- reference database backend behaviour beyond the data model,
- TensorFlow Extended orchestration or standard components,
- commercial / managed ML platforms,
- organization-specific ArtifactType / ExecutionType / ContextType schemas,
- custom metadata profiles or property conventions,
- integrations with other standards (e.g. PROV, OpenTelemetry, policy engines).

Therefore the conclusions apply only to **MLMD as structurally defined and documented**, not to “ML metadata” practice in general.

Additional threats:

- Example questions in docs (e.g. hyperparameters) may suggest broader coverage than first-class types provide.
- Companion TFX materials may describe richer pipeline practices than MLMD alone guarantees.

---

## 4. Remaining uncertainty

- Whether a future MLMD system-defined context/execution vocabulary could encode decision-normative fields without leaving the MLMD project (would require a new source revision).
- Empirical frequency of org schemas that *do* encode policy/justification in properties — out of scope; would be a separate evaluation unit.
- Relationship between ArtifactType/ExecutionType `version` fields and checklist IC-07/IC-13 in real governance scenarios remains modeler-dependent.
- Claim **C5** receives supporting evidence for this **MLMD unit** (lineage ≠ justification triad) but is not promoted repository-wide solely by this review.

---

## What this source does not establish

- That production ML platforms using MLMD fail or pass faithful reconstruction of legally relevant decisions.
- That property-level conventions cannot encode the triad (would be a profile/composition evaluation).
- Completeness of TFX or other orchestrators that write into MLMD.

---

## Overall Assessment

**MLMD v1.21.0 substantially supports reconstruction of ML pipeline lineage: which artifacts were used/produced by which executions, under which workflow contexts, with first-class timestamps and artifact lifecycle states.** It does **not**, by itself, systematically preserve the normative information required for faithful reconstruction of legally relevant AI-supported decisions under the repository checklist (authorization policy/rules, justification reliance, validity constraints).

This is consistent with treating MLMD as an instance of **data/model provenance / MLOps lineage** under claim-inventory **C5** for this evaluation unit only.

**Aggregate comparison matrix / CSV:** not updated (per task instruction).

**Next research step:** Evaluate a distinct SUT for authorization (e.g. OPA/Cedar decision logs), and/or a declared composition of MLMD lineage + policy decision records with explicit binding.
