---
id: arch-ai-infrastructure-gap-knowledge-continuity-model
title: "Knowledge Continuity Model: Decision Episode composition architecture"
topic: ai-infrastructure-gap
type: architecture
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [architecture, decision-episode, composition, reconstruction, knowledge-continuity]
checklist_version: "0.1.0"
normative_for: reconstruction-composition
derived_from:
  - architecture/reconstruction-checklist.md
  - evaluation/coverage-audit.md
  - evaluation/reconstruction-scenarios.md
  - evaluation/composition-analysis.md
---

# Knowledge Continuity Model

**Document role.** First normative engineering proposal of this research programme: a **technology-neutral composition architecture** that preserves the minimum information and bindings required for **deterministic faithful reconstruction** of one historically situated AI-assisted decision (reconstruction checklist v0.1.0 §3).

**Derivation.** The model is derived from unit-review evidence, the coverage audit, reconstruction scenarios, and composition analysis. It does **not** introduce a product stack. It defines persistent **objects**, **bindings**, and a **reconstruction procedure**.

**Status.** `draft` — normative for evaluation of composition profiles and future designs; not a certified standard.

---

## 1. Design objective

Enable a competent reconstructor, given only retained structured information and a publicly stated reconstruction procedure, to:

1. identify one decision episode unambiguously;
2. state the outcome;
3. locate the episode in time and versioned contexts;
4. restate **authorization**, **justification**, and **validity** as of decision time;
5. distinguish historical structure from current system narrative.

The architecture must satisfy checklist information categories and §7 binding criteria while remaining **technology-neutral** and **incrementally adoptable** over existing governance components.

---

## 2. Guiding principles

Each principle follows from evaluation findings (composition analysis §7; scenarios 1–6; checklist §3–§7).

| Principle | Statement | Evaluation basis |
|---|---|---|
| **Decision Episode as primary object** | The unit of retention and reconstruction is the decision episode, not the model, policy engine, workflow, or log stream. | Composition failure when strong components remain unbound (C1; Scenario 5). |
| **Stable semantic identity** | Every episode has an immutable identifier usable across systems. | Identity fragmentation (Scenario 5; checklist §3.3, §7.1). |
| **Durable cross-system bindings** | Associations among episode objects must be explicit and retained, not inferred. | Missing bindings table (composition analysis §3). |
| **Historical rather than runtime truth** | Reconstruction uses decision-time structure, never silent substitution of current artifacts. | Checklist §3.1 item 7; Scenarios 2, 4. |
| **Explicit temporal validity** | Policies, authorities, models, and evidence carry validity intervals relative to decision time. | C3; Scenario 2; checklist IC-07, IC-19. |
| **Versioned references** | References point to immutable version identifiers (or content hashes), not “latest.” | Model/dataset/policy drift (Scenario 4). |
| **Human responsibility preservation** | Human actors, authority, review acts, overrides, and reasons are first-class episode content. | WS-HumanTask capability vs missing preservation; Scenario 3; C2/C6. |
| **Minimal sufficient reconstruction** | Preserve normative and evidential basis; do not require bit-exact compute replay. | Checklist §3.2. |
| **Technology neutrality** | No mandated store, ledger, graph, bus, or vendor. | Checklist §1.3; composition analysis scope. |
| **Incremental adoptability** | Organizations may bind existing tools into episodes without replacing them. | C8 framing; coverage audit stopping rule. |

---

## 3. Decision Episode

### 3.1 Definition

A **Decision Episode** is the bounded set of facts, versions, bindings, and acts associated with one decision identity at decision time, plus subsequent review, appeal, and correction acts that refer to that identity (checklist §2 working sense of decision episode, extended for continuity).

### 3.2 Boundaries

**In boundary:**

- the commit to an action, classification, recommendation acceptance/rejection, or controlled outcome in which AI outputs materially participated;
- the evidence and criteria treated as applicable then;
- human interventions that produced or altered the outcome;
- notices, appeals, and corrections that reference the episode.

**Out of boundary:**

- unrelated system telemetry;
- later model training runs not referenced by the episode;
- organization-wide policy repositories except via versioned references;
- live feature stores except via evidence snapshots.

### 3.3 Lifecycle

| Phase | Content |
|---|---|
| **Formation** | Identity minted; inputs assembled; inference and/or policy evaluation executed; optional human review. |
| **Commitment** | Outcome recorded; decision time fixed; required bindings sealed. |
| **Disclosure** | Notification to subject where applicable. |
| **Contest** | Appeal / explanation request / complaint linked to identity. |
| **Correction** | Remediation or amendment recorded as new acts bound to the same identity (append-only history). |
| **Retention** | Episode retained per policy; components may age out only if reconstruction requirements for the declared profile remain met. |

### 3.4 Immutable identity

Each Decision Episode has a single **Decision ID** that:

- is minted at or before commitment;
- never reused;
- is the join key for all bindings;
- remains stable across appeal and correction.

Mutable business keys (case numbers, ticket IDs) may *alias* the Decision ID but must not replace it.

### 3.5 Participants (conceptual)

| Class | Examples within an episode |
|---|---|
| **Actors** | Subject; human reviewers; automated principals; organizations |
| **Systems** | Inference service; policy engine; workflow; notification system |
| **Evidence** | Snapshots of inputs relied upon and, where required, available/excluded sets |
| **Policies** | Governing policy versions and evaluation results |
| **AI components** | Model version; dataset version; feature pipeline version; inference record |
| **Human interventions** | Review, approval, rejection, override, escalation |
| **Outcomes** | Final decided outcome at commitment |
| **Later review** | Investigation, audit access, reconstruction runs |
| **Appeal / correction** | Contest records; remediation acts |

### 3.6 Why the Decision Episode is fundamental

Models, policy engines, and workflows answer **native** questions (how was the model trained; was access allowed; who completed a task). Faithful reconstruction asks a **cross-cutting** question: why *this* outcome was justified, authorized, and valid *then*. Evaluation showed those native answers do not compose without a shared episode object. Therefore the Decision Episode—not the model card, decision log, or task instance alone—is the primary engineering object of knowledge continuity.

---

## 4. Required persistent objects

Objects are conceptual. Attributes are minimum information requirements, not schemas.

Retention: **R-mand** = mandatory for base triad continuity; **R-cond** = conditionally mandatory by scenario profile; **R-rec** = recommended.

### 4.1 Decision

| Field | Content |
|---|---|
| **Purpose** | Anchor object for the episode (IC-01, IC-02, IC-03). |
| **Minimum attributes** | `decisionId`; `outcome`; `decisionTime`; `clockDomain`; `status` (committed / superseded-by-correction metadata pointer); `profile` (base/audit/forensic). |
| **Identity** | `decisionId` (immutable). |
| **Timestamps** | `decisionTime` required. |
| **Relationships** | Binds to all other episode objects below. |
| **Retention** | R-mand for the reconstruction horizon of the profile. |

### 4.2 Subject

| Field | Content |
|---|---|
| **Purpose** | Identify whom the decision concerns. |
| **Minimum attributes** | `subjectId` (or privacy-preserving durable reference); `subjectType`. |
| **Identity** | Stable within retention/legal constraints. |
| **Timestamps** | Optional `asOf`. |
| **Relationships** | Decision → Subject; Notification/Appeal → Subject. |
| **Retention** | R-cond (always for person-affecting decisions). |

### 4.3 Human Actor

| Field | Content |
|---|---|
| **Purpose** | Identify human participants (IC-04). |
| **Minimum attributes** | `actorId`; `displayName` or org directory ref; `actorKind` (reviewer, approver, override agent). |
| **Identity** | `actorId` at decision time (not recycled without history). |
| **Timestamps** | Participation times via Human Review / Override. |
| **Relationships** | Actor → Authority; Actor → Human Review / Override. |
| **Retention** | R-mand when humans affect outcome. |

### 4.4 Organization

| Field | Content |
|---|---|
| **Purpose** | Organizational principal responsible for deployment/decision context. |
| **Minimum attributes** | `orgId`; `roleInEpisode` (provider, deployer, processor). |
| **Identity** | `orgId`. |
| **Timestamps** | Optional. |
| **Relationships** | Organization → Authority; Organization → Decision. |
| **Retention** | R-rec / R-cond for multi-party settings. |

### 4.5 Authority

| Field | Content |
|---|---|
| **Purpose** | Mandate under which an actor or system may decide (IC-05). |
| **Minimum attributes** | `authorityId`; `authorityType` (role, delegation, statutory mandate, system charter); `holderRef` (actor/org/system); `validFrom`; `validTo`. |
| **Identity** | `authorityId` + version or content hash. |
| **Timestamps** | Validity interval required. |
| **Relationships** | Decision → Authority (at decisionTime); Human Review → Authority. |
| **Retention** | R-mand when authorization is in scope. |

### 4.6 AI Inference

| Field | Content |
|---|---|
| **Purpose** | Record of model participation that materially affected the outcome. |
| **Minimum attributes** | `inferenceId`; `output`; `confidence` if used as gate (IC-17); `decisionId`. |
| **Identity** | `inferenceId`. |
| **Timestamps** | `inferenceTime`. |
| **Relationships** | Inference → Model Version; Inference → Evidence Snapshot; Inference → Decision. |
| **Retention** | R-mand when AI materially participates. |

### 4.7 Model Version

| Field | Content |
|---|---|
| **Purpose** | Immutable reference to the model artifact used (IC-13). |
| **Minimum attributes** | `modelVersionId`; `modelFamilyId`; `versionLabel` or content hash; optional pointer to documentation artifact. |
| **Identity** | Content-addressed or immutable version id. |
| **Timestamps** | `publishedAt`; lifetime optional. |
| **Relationships** | Inference → Model Version; Model Version → Dataset Version(s) as declared. |
| **Retention** | R-mand for model-participating decisions (reference must resolve for reconstruction horizon). |

### 4.8 Dataset Version

| Field | Content |
|---|---|
| **Purpose** | Immutable reference to training/reference datasets material to interpretation (IC-23/IC-24 as conditioned). |
| **Minimum attributes** | `datasetVersionId`; content hash or version label; role (train/eval/reference). |
| **Identity** | Immutable version id. |
| **Timestamps** | `publishedAt`. |
| **Relationships** | Model Version → Dataset Version; Feature Pipeline → Dataset Version. |
| **Retention** | R-cond when disputes turn on data heritage or reference matching. |

### 4.9 Feature Pipeline Version

| Field | Content |
|---|---|
| **Purpose** | Transformation path producing inference features. |
| **Minimum attributes** | `pipelineVersionId`; version/hash; optional step list digest. |
| **Identity** | Immutable version id. |
| **Timestamps** | `publishedAt`. |
| **Relationships** | Inference → Feature Pipeline Version; Pipeline → Dataset Version. |
| **Retention** | R-cond when features are derived. |

### 4.10 Evidence Snapshot

| Field | Content |
|---|---|
| **Purpose** | Preserve inputs available and relied upon (IC-10, IC-11; IC-12 when conditioned). |
| **Minimum attributes** | `snapshotId`; `availableEvidenceRefs[]`; `reliedUponRefs[]` or weighting record; optional `excludedRefs[]` + reasons; content hashes. |
| **Identity** | `snapshotId` (content-addressed preferred). |
| **Timestamps** | `capturedAt` (= decision-time evidence as-of). |
| **Relationships** | Decision → Evidence Snapshot; Inference → Evidence Snapshot. |
| **Retention** | R-mand for evidence-using decisions; redaction must leave reconstructable reliance semantics. |

### 4.11 Policy

| Field | Content |
|---|---|
| **Purpose** | Identify governing policy artifact family (IC-06). |
| **Minimum attributes** | `policyId`; `name` or URI. |
| **Identity** | `policyId`. |
| **Timestamps** | Via Policy Version. |
| **Relationships** | Policy → Policy Version*. |
| **Retention** | R-mand when policy-governed. |

### 4.12 Policy Version

| Field | Content |
|---|---|
| **Purpose** | Immutable governing rules at decision time (IC-07; IC-08 as conditioned). |
| **Minimum attributes** | `policyVersionId`; content hash; `validFrom`; `validTo`; optional `applicableRulePath` / evaluation trace digest. |
| **Identity** | Immutable version id / hash. |
| **Timestamps** | Validity interval required. |
| **Relationships** | Decision → Policy Version; Policy evaluation result bound to Decision. |
| **Retention** | R-mand when policy-governed. |

### 4.13 Explanation

| Field | Content |
|---|---|
| **Purpose** | Decision-time human-facing account bound to the episode (not a substitute for justification structure). |
| **Minimum attributes** | `explanationId`; `content` or content hash; `audience`; `methodId` (optional); `producedAt`. |
| **Identity** | `explanationId`. |
| **Timestamps** | `producedAt` ≤ commitment + declared skew policy. |
| **Relationships** | Decision → Explanation; Explanation → Inference (optional). |
| **Retention** | R-cond when transparency/contestability profiles require it; **never** sole justification record. |

### 4.14 Human Review

| Field | Content |
|---|---|
| **Purpose** | Structured human-gate act (approve, reject, request changes). |
| **Minimum attributes** | `reviewId`; `decisionId`; `actorId`; `authorityId`; `action` (approve/reject/escalate/…); `rationale` (required for base human-gated profile); `reviewTime`. |
| **Identity** | `reviewId`. |
| **Timestamps** | `reviewTime`. |
| **Relationships** | Decision → Human Review; Review → Authority; Review may reference Inference. |
| **Retention** | R-mand when humans affect outcome. |

### 4.15 Override

| Field | Content |
|---|---|
| **Purpose** | Explicit record that human disregarded/reversed system output. |
| **Minimum attributes** | `overrideId`; `decisionId`; `actorId`; `authorityId`; `originalInferenceRef`; `replacementOutcome`; `rationale` (required); `overrideTime`. |
| **Identity** | `overrideId`. |
| **Timestamps** | `overrideTime`. |
| **Relationships** | Decision → Override; Override → Inference; Override → Authority. |
| **Retention** | R-mand when override occurs. |

### 4.16 Notification

| Field | Content |
|---|---|
| **Purpose** | Notice to subject of AI-assisted decision / use. |
| **Minimum attributes** | `notificationId`; `decisionId`; `subjectId`; `channel`; `contentHash`; `sentAt`. |
| **Identity** | `notificationId`. |
| **Timestamps** | `sentAt`. |
| **Relationships** | Decision → Notification → Subject. |
| **Retention** | R-cond for person-affecting / regulated profiles. |

### 4.17 Appeal

| Field | Content |
|---|---|
| **Purpose** | Contest, explanation request, or complaint bound to the episode. |
| **Minimum attributes** | `appealId`; `decisionId`; `subjectId`; `grounds`; `status`; `openedAt`; `closedAt` optional. |
| **Identity** | `appealId`. |
| **Timestamps** | `openedAt`; resolution times. |
| **Relationships** | Decision → Appeal; Appeal may spawn Remediation. |
| **Retention** | R-cond for contestability profiles. |

### 4.18 Remediation

| Field | Content |
|---|---|
| **Purpose** | Correction, withdrawal, compensation, or re-decision linked to the episode. |
| **Minimum attributes** | `remediationId`; `decisionId`; `actionType`; `result`; `actorId`; `remediationTime`; optional `supersedingDecisionId`. |
| **Identity** | `remediationId`. |
| **Timestamps** | `remediationTime`. |
| **Relationships** | Decision → Remediation; may create new Decision bound as correction-of. |
| **Retention** | R-cond when corrections occur; R-rec for audit profiles. |

### 4.19 Audit Record

| Field | Content |
|---|---|
| **Purpose** | Integrity and access/event trail for episode objects (IC-21 elevated). |
| **Minimum attributes** | `auditId`; `decisionId`; `eventType`; `actorOrSystem`; `payloadDigest`; `eventTime`. |
| **Identity** | `auditId`. |
| **Timestamps** | `eventTime`. |
| **Relationships** | Decision → Audit Record*. |
| **Retention** | R-rec base; R-mand for integrity-elevated profiles. |

---

## 5. Required bindings

Each binding is defined **exactly once**. All are associations to `decisionId` unless noted. **Immutable after commitment** means the association and referenced version ids cannot be rewritten; corrections append new objects.

| Binding | Why it exists | What it preserves | Immutable after commitment? | Version changes? | Failure if absent |
|---|---|---|---|---|---|
| **Decision ↔ AI Inference** | AI participation must be recoverable | Output that influenced the outcome | Yes | New inferences require new episode or explicit re-decision | Cannot reconstruct model role (Scenarios 1, 4) |
| **Decision ↔ Evidence Snapshot** | Justification needs relied-upon inputs | IC-10/IC-11 structure | Yes (snapshot frozen) | New evidence ⇒ new snapshot + correction/re-decision | Justification FAIL (Scenarios 3, 6) |
| **Decision ↔ Policy Version** | Authorization/validity need then-applicable rules | IC-06/IC-07 | Yes | Policy updates do not rewrite binding | Validity/authorization FAIL (Scenario 2) |
| **Decision ↔ Model Version** | Historical model identity | IC-13 | Yes | Model updates unbound | Scenario 4 drift |
| **Decision ↔ Dataset Version** | Interpret training/reference heritage | Conditioned IC-23/24 | Yes when required by profile | Dataset updates unbound | Partial/heritage disputes fail |
| **Decision ↔ Feature Pipeline** | Feature derivation at decision time | Pipeline identity for inputs | Yes when derived features used | Pipeline updates unbound | Non-reproducible features |
| **Decision ↔ Human Review** | Human gate is part of outcome formation | Actor, action, rationale, time | Yes for completed reviews | Amendments via Remediation/Appeal | Scenario 3 outcome-only failure |
| **Decision ↔ Authority** | Separate “who may” from “who did” | IC-05 at decisionTime | Yes | Role changes unbound | Unauthorized-looking history |
| **Decision ↔ Explanation** | Bind contemporaneous account | Decision-time explanation artifact | Yes if retained | Post-hoc explanations must be marked non-historical | C7 / post-hoc substitution |
| **Decision ↔ Notification** | Continuity of disclosure | Notice content and time | Yes for sent notices | Re-notices append | Contestability gap |
| **Decision ↔ Appeal** | Contest refers to same episode | Appeal thread | Appeal records append-only | Status updates allowed | Orphan appeals (Scenario 6) |
| **Decision ↔ Remediation** | Corrections do not erase history | Append-only fix trail | Original decision immutable | Remediation appends | Silent outcome mutation |
| **Decision ↔ Later Correction** | Same as Remediation / superseding Decision link | Explicit supersession | Original retained | New Decision may supersede | Checklist §3.3 narrative rewrite |

**Additional mandatory intra-episode bindings (normative):**

- Human Review ↔ Authority; Override ↔ Authority; Override ↔ AI Inference (original).
- AI Inference ↔ Model Version; AI Inference ↔ Evidence Snapshot.
- Policy evaluation result (permit/deny/path digest) recorded on Decision or as attached evaluation object bound to Decision ↔ Policy Version.

---

## 6. Temporal model

### 6.1 Time axes

| Axis | Meaning |
|---|---|
| **Decision time** | Instant the outcome is committed (`Decision.decisionTime`). Primary anchor. |
| **Effective time** | Instant (or interval) at which referenced policies, authorities, and reference data are considered applicable. |
| **Inference time** | When AI output was produced (may precede decision time). |
| **Review time** | When human review/override occurred. |
| **Notification time** | When notice was sent. |
| **Appeal time** | Open/close times of contest. |
| **Remediation time** | When correction occurred. |
| **Reconstruction time** | When a later party runs the reconstruction procedure (must not alter episode). |

### 6.2 Validity intervals

| Object | Interval |
|---|---|
| Policy Version | `validFrom`–`validTo` must contain decision effective time |
| Authority | `validFrom`–`validTo` must contain review/decision time as applicable |
| Model Version | lifetime / publication; must match inference reference |
| Dataset Version | publication/lifetime; referenced as-of snapshot time |
| Evidence Snapshot | `capturedAt` as-of for live sources |

### 6.3 Correction history

Corrections **append**. The original Decision remains. Remediation or a superseding Decision references the original `decisionId`. Reconstruction returns the commitment-time state plus an ordered correction chain.

### 6.4 Why “latest only” fails

Retaining only current policy, model, features, explanations, or roles rewrites historical authorization, justification, and validity (Scenarios 2, 4; checklist §3.3). Knowledge continuity forbids latest-only stores as the sole source of truth for reconstruction.

---

## 7. Base triad support

### 7.1 Authorization

| Element | Objects / bindings |
|---|---|
| Who/what decided | Human Actor and/or system principal; Human Review / Override |
| Under which authority | Authority valid at decision/review time |
| Under which policy | Policy Version + evaluation result bound to Decision |
| When | decisionTime / reviewTime |

**Deterministic later evaluation:** Resolve Decision → verify Authority interval contains act time → load Policy Version by id → confirm evaluation result digest matches retained evaluation → confirm actors match Human Review/Override records.

### 7.2 Justification

| Element | Objects / bindings |
|---|---|
| Evidence relied upon | Evidence Snapshot (`reliedUponRefs`) |
| AI contribution | AI Inference output bound to Decision |
| Human reasons | Human Review / Override `rationale` |
| Criteria | Policy Version rules / rule path; optional Explanation as *account*, not sole basis |

**Deterministic later evaluation:** Load Evidence Snapshot and Inference by Decision bindings → distinguish relied-upon vs available → include human rationales → do not accept unbound post-hoc explanations as historical justification.

### 7.3 Validity

| Element | Objects / bindings |
|---|---|
| Rules in force | Policy Version validity interval vs effective/decision time |
| Constraints | Represented in Policy Version / evaluation; optional constraint objects profile-elevated |
| Conformity representation | Outcome + evaluation result; Remediation chain if later non-conformity handling |

**Deterministic later evaluation:** Confirm Policy Version interval coverage → confirm constraint/evaluation artifacts → compare outcome to recorded evaluation → separate remediation from original validity.

---

## 8. Reconstruction algorithm (technology-neutral)

**Input:** `decisionId`  
**Output:** Structured historical decision context sufficient for checklist §3.1 statements under the declared profile.

1. **Resolve Decision Episode** — load Decision by `decisionId`; read outcome, decisionTime, status, profile.  
2. **Recover Evidence Snapshot** — load bound snapshot; list available vs relied-upon (and excluded if profile requires).  
3. **Recover Policy Version** — load bound Policy Version; verify validity interval against decision/effective time; load evaluation result.  
4. **Recover AI Inference** — load bound inference output and times.  
5. **Recover Model, Dataset, Feature Pipeline Versions** — follow inference and snapshot references; verify identifiers resolve.  
6. **Recover human actions** — load Human Review and Override records; include rationales.  
7. **Recover Authority** — load Authority objects for each act; verify intervals.  
8. **Recover Explanation** — load decision-time Explanation if present; mark any later explanations as non-historical.  
9. **Recover Notification, Appeal, Remediation** — ordered by time; include supersession links.  
10. **Evaluate triad** — produce authorization, justification, and validity statements; emit explicit gaps if any mandatory binding is missing (reconstruction **FAIL** rather than silent guesswork).

No executable code; any conforming implementation must preserve this logical order and fail closed on missing mandatory bindings.

---

## 9. Evaluation against reconstruction scenarios

### Scenario 1 — Model-assisted eligibility denial

| Item | Content |
|---|---|
| **Required objects** | Decision, Subject, AI Inference, Model Version, Evidence Snapshot, Policy Version, Human Review, Authority, Notification; Appeal/Remediation if used; Explanation if profile requires |
| **Required bindings** | All decision↔{inference, evidence, policy version, model version, human review, authority, notification} |
| **Expected outcome** | **PASS** for base triad if mandatory fields populated at commitment |
| **Assumptions** | Authority objects exist in org directory; evidence snapshot captured before live-store mutation |
| **Limitations** | Does not judge whether denial was fair or correct |

### Scenario 2 — Policy change after decision

| Item | Content |
|---|---|
| **Required objects** | Decision, Policy Version (historical), evaluation result; current policy is *not* used |
| **Required bindings** | Decision ↔ Policy Version (immutable) |
| **Expected outcome** | **PASS** for historical authorization/validity relative to bound version |
| **Assumptions** | Policy Version content remains retrievable by id/hash |
| **Limitations** | Does not prevent operators from failing to register Policy Version objects |

### Scenario 3 — Human override without preserved rationale

| Item | Content |
|---|---|
| **Required objects** | Override with **required** rationale; original Inference; Authority |
| **Required bindings** | Decision ↔ Override ↔ Inference; Decision ↔ Authority |
| **Expected outcome** | **PASS** if model enforced; **FAIL** if organization stores outcome only (non-conformant deployment) |
| **Assumptions** | Commitment gate rejects override without rationale |
| **Limitations** | Quality of rationale text is out of scope |

### Scenario 4 — Model or dataset update

| Item | Content |
|---|---|
| **Required objects** | Model Version, Dataset Version, Feature Pipeline Version, Evidence Snapshot, Inference |
| **Required bindings** | Decision ↔ Inference ↔ Model/Dataset/Pipeline versions |
| **Expected outcome** | **PASS** for justification context and model identity; bit-exact replay still not required (§3.2) |
| **Assumptions** | Version artifacts remain resolvable |
| **Limitations** | Non-determinism of model internals may remain; faithfulness ≠ full reproducibility |

### Scenario 5 — Logging without shared identity

| Item | Content |
|---|---|
| **Required objects** | Decision with `decisionId` propagated to all emitters |
| **Required bindings** | Every component record carries `decisionId` |
| **Expected outcome** | **PASS** under conformant adoption; **FAIL** if only correlating legacy logs without Decision object (non-conformant) |
| **Assumptions** | Emitters instrumented to attach Decision ID |
| **Limitations** | Retroactive stitching of pre-adoption logs may remain PARTIAL |

### Scenario 6 — Appeal after partial data deletion

| Item | Content |
|---|---|
| **Required objects** | Evidence Snapshot retained under reconstruction retention; Appeal bound to Decision; lawful redaction rules |
| **Required bindings** | Decision ↔ Evidence; Decision ↔ Appeal |
| **Expected outcome** | **PASS** if snapshot retained (possibly redacted with explicit reliance semantics); **PARTIAL** if law forces deletion of relied-upon raw data but digests/categories remain; **FAIL** if relied-upon evidence wholly destroyed without lawful reconstruction substitute |
| **Assumptions** | Retention schedule reconciles privacy law with declared profile |
| **Limitations** | Privacy constraints may force PARTIAL profiles; model does not override law |

---

## 10. Relationship to existing governance components

| Existing component | Continues to provide | Knowledge Continuity Model adds |
|---|---|---|
| Provenance (e.g. PROV) | Derivation graphs | Decision ID binding; episode membership |
| Observability (e.g. OTel) | Execution paths | Decision ID on spans/events; not treated as justification alone |
| Lineage / ML metadata | Pipeline/artifact versions | Version refs attached to Inference/Evidence |
| Policy engines (e.g. OPA) | Evaluation + optional logs | Decision ↔ Policy Version seal at commitment |
| Authorization languages (e.g. Cedar) | Eval semantics | Durable evaluation result + Decision binding |
| Documentation (cards/datasheets) | Release-time descriptions | Optional pointers from Model/Dataset Version objects |
| Explainability | Explanation quality | Decision-time Explanation object; not sole justification |
| Legal logging (e.g. AI Act logs) | Retention-backed events | Semantic episode composition beyond purpose-based events |
| Human workflow (e.g. WS-HumanTask) | Task lifecycle | Map task completion to Human Review/Override with Decision ID + required rationale |
| AI RMF-style governance | Organizational process | Process does not replace episode objects |

**Clear statement:** Existing components remain valuable. This proposal defines the **persistent composition layer**—objects and bindings—that connects them for reconstruction. It does not replace them.

---

## 11. Minimal adoption strategy

### 11.1 Mandatory elements (base triad profile)

- Mint and propagate **Decision ID**.
- Persist **Decision** (outcome + decisionTime).
- Persist **Evidence Snapshot** with reliance distinction for evidence-using decisions.
- Persist **Policy Version** reference + evaluation result for policy-governed decisions.
- Persist **Model Version** + **AI Inference** when AI participates.
- Persist **Human Review** / **Override** with actor, authority, rationale when humans affect outcome.
- Append-only **Remediation** / correction links.

### 11.2 Recommended elements

- Notification and Appeal bindings for person-affecting decisions.
- Feature Pipeline Version.
- Decision-time Explanation object.
- Audit Record digests for integrity-elevated needs.
- Organization object in multi-party deployments.

### 11.3 Optional extensions

- Full excluded-evidence accounting (IC-12).
- Cryptographic integrity/signatures (IC-21/IC-22).
- Rich provenance graphs beyond version refs.
- Forensic profiles with extended retention.

### 11.4 Incremental path

1. Introduce Decision ID at the business commitment point.  
2. Wrap existing OPA/Cedar results, model registry versions, and workflow completions as bound objects.  
3. Add evidence snapshotting beside live feature access.  
4. Enforce commitment gates (reject incomplete bindings).  
5. Extend to notice/appeal systems.  

No requirement to replace existing tooling in step 1.

---

## 12. Scope limitations

This proposal **does not** solve:

- decision quality, accuracy, or optimality;
- fairness, bias, or non-discrimination substantive assessment;
- security hardening or adversarial robustness;
- privacy compliance by itself (it must be reconciled with retention);
- organizational governance maturity;
- legal compliance as a complete programme;
- runtime performance optimization;
- foundation-model training methods;
- automatic generation of good rationales.

It addresses **reconstruction capability** only: whether retained structure supports deterministic faithful reconstruction of authorization, justification, and validity for a Decision Episode.

---

## 13. Threats to validity

| Threat | Why it does not invalidate the conceptual model |
|---|---|
| Implementation variability | Non-conformant deployments can FAIL scenarios; that falsifies adoption, not the necessity of bindings identified by evaluation. |
| Organizational adoption | Incremental strategy acknowledges partial rollout; Scenario 5 PASS requires conformance. |
| Future standards | May standardize the same bindings under other names; the information requirements remain. |
| Domain-specific extras | Profiles may elevate optional objects without removing mandatory bindings. |
| Alternative composition mechanisms | C8 remains open: a profile over existing stores that realizes these objects/bindings would satisfy the model without a new product layer. |

---

## 14. Conclusions

The Knowledge Continuity Model elevates the **Decision Episode** as the primary engineering object, defines minimum persistent objects and **exactly once** mandatory bindings, and specifies a technology-neutral reconstruction procedure aligned with checklist v0.1.0.

It treats existing governance infrastructure as necessary components and supplies the missing **durable cross-system composition** layer identified by the composition analysis. Under conformant population of mandatory objects and bindings, Scenarios 1–5 are designed to **PASS** base reconstruction; Scenario 6 may be **PASS**, **PARTIAL**, or **FAIL** depending on lawful evidence retention.

**Not claimed:** universal impossibility of reconstruction today, or that only a branded new product can succeed. **Claimed:** without episode-centric durable bindings, the reviewed ecosystem does not guarantee deterministic faithful reconstruction; with this model’s information requirements met, such reconstruction becomes structurally possible.

---

## Related artifacts

| Artifact | Relationship |
|---|---|
| [reconstruction-checklist.md](reconstruction-checklist.md) | Normative information categories and triad |
| [composition-analysis.md](../evaluation/composition-analysis.md) | Problem diagnosis this model answers |
| [reconstruction-scenarios.md](../evaluation/reconstruction-scenarios.md) | Scenario set used in §9 |
| [coverage-audit.md](../evaluation/coverage-audit.md) | Corpus completeness; stop unit expansion |
| [claim-inventory.md](claim-inventory.md) | Hypotheses; not updated by this document |
