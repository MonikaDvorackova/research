---
id: eval-ai-infrastructure-gap-reconstruction-scenarios-2026-07-29
title: "Reconstruction scenarios and composition analysis"
topic: ai-infrastructure-gap
type: evaluation
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, scenarios, composition, reconstruction, bindings]
checklist_version: "0.1.0"
related_claims: [C1, C2, C3, C4, C5, C6, C7, C8]
unit_reviews_basis:
  - 2026-07-29-w3c-prov-dm.md
  - 2026-07-29-opentelemetry-specification.md
  - 2026-07-29-google-ml-metadata.md
  - 2026-07-29-openlineage.md
  - 2026-07-29-open-policy-agent.md
  - 2026-07-29-cedar.md
  - 2026-07-29-model-cards.md
  - 2026-07-29-datasheets-for-datasets.md
  - 2026-07-29-system-cards.md
  - 2026-07-29-nist-ai-rmf-1.0.md
  - 2026-07-29-nistir-8312-xai-principles.md
  - 2026-07-29-eu-ai-act-decision-audit-records.md
  - 2026-07-29-oasis-ws-humantask-human-review-workflow.md
---

# Reconstruction scenarios and composition analysis

**Purpose:** Move from unit-source reviews to **adversarial scenarios** and **composition** analysis. Test whether families that individually contribute capabilities can reconstruct justification, authorization, and validity when combined **without** inventing cross-system bindings the sources do not define.

**Method:** Checklist v0.1.0 (base triad profile). Unit scores are taken from completed reviews; composition scores require **explicit, durable binding** between components. Two adequate components without a stable shared identity and retention of that binding are treated as **insufficient**.

**Not this document:** new unit-SUT reviews; claim promotion; comparison-matrix/dataset updates; product designs.

---

## 1. Unit capability versus compositional sufficiency

For strongly/partially covered families: what each provides, what it lacks, what it would need to compose with, whether either source defines the binding, and whether later reconstruction works without custom integration.

| Family (unit SUT) | Provides | Does not provide | Needs to compose with | Binding required | Binding defined by either source? | Temporal persistence of binding required? | Reconstruction without custom integration? |
|---|---|---|---|---|---|---|---|
| Provenance (PROV-DM) | Entities/activities/agents; derivation | Policy/version as governing rule; reliance subset; decision episode schema | Policy logs; decision ID; evidence store | Decision ID ↔ PROV graph / used entities | No shared decision ID in PROV alone | Yes | No |
| Observability (OTel) | Traces/spans/logs/baggage | Normative criteria; durable decision identity | Decision record; policy log; model version | Decision ID ↔ trace/span | No standard decision-episode semantic | Yes | No |
| ML metadata (MLMD) | Artifacts/executions/events/contexts | Decision episode; authorization; reliance | Inference event; decision ID; policy | Model/run ID ↔ decision ID | No | Yes | No |
| Data lineage (OpenLineage) | Job/dataset lineage events | Decision identity; authorization; reliance | Feature/inference snapshot; decision ID | Dataset version ↔ decision inputs | No | Yes | No |
| Policy engine (OPA) | Decision logs; bundle revision | Full AI justification; human gate; evidence reliance | Human task; model output; evidence; decision ID | Decision ID ↔ policy decision id / bundle revision | Partial within OPA only | Yes (bundle revision at eval time) | No (cross-system) |
| Authz language (Cedar) | PARC eval; diagnostics | Durable decision log | External log sink + decision ID | Decision ID ↔ authz response | No durable log in language | Yes | No |
| Model docs (Model Cards) | Model version/date reporting fields | Decision binding | Inference log; decision ID | Model card version ↔ decision | No | Yes | No |
| Dataset docs (Datasheets) | Dataset lifecycle documentation | Decision binding | Input snapshot; decision ID | Datasheet/dataset version ↔ decision | No | Yes | No |
| System docs (System Cards) | System composition overview | Episode records | Runtime logs; decision ID | System version ↔ decision | No (current version only) | Yes | No |
| AI RMF 1.0 | Org risk/oversight documentation | Episode reconstruction schema | Operational stores | Process docs ↔ episodes | No | Org temporal ≠ decision temporal | No |
| XAI principles (NISTIR 8312) | Explanation quality properties | Durable justification record; identity; retention | Decision record; policy; evidence | Explanation ↔ decision ID at decision time | No | Yes | No |
| Legal logging (EU AI Act Arts. 12/19/26) | Automatic event logs; ≥6 mo retention; biometric min fields; Art. 86 explanation *right* | General decision ID schema; policy version in logs; reliance; override audit | Policy log; human task; evidence; model version | Decision/use ID ↔ all episode artifacts | Partial only for Annex III 1(a) fields | Yes (retention floor) | No for general high-risk |
| Human workflow (WS-HumanTask) | Task ID; roles; complete/fail/forward; I/O; history API | Retention duty; policy/model version; legal authority object | Decision ID; authz; evidence; policy | Task ID ↔ decision ID; task input ↔ model output | No cross-system decision ID | Yes (API ≠ archive) | No |

**Composition rule used below:** a cell counts as reconstructable only if the required information is present **and** associable to the same decision identity without undocumented heuristics (checklist §7).

---

## 2. Scenarios

### Scenario 1 — Model-assisted eligibility denial

**Narrative:** A person is denied eligibility based partly on an AI-generated recommendation. A human reviewer accepts the recommendation. Months later, the person challenges the denial.

**Reconstruction objective:** Recover the exact decision, model output used, inputs, model version, policy/rule, responsible human and authority, accept/reject/modify action, reasons, notice, appeal/reconsideration path, and any later correction.

**Required checklist items (primary):** IC-01–IC-05, IC-06–IC-08, IC-10–IC-11, IC-13, IC-17 (if thresholded), IC-19–IC-20 as conditioned; human-action binding; outcome.

**Relevant families:** Model docs; MLMD/OpenLineage; OPA/Cedar; WS-HumanTask; EU AI Act logs/Art. 86; NISTIR 8312; OTel; AI RMF (oversight process docs).

| Aspect | Assessment |
|---|---|
| **Available unit capabilities** | Model version *documentation* (Model Cards); possible run lineage (MLMD/OpenLineage); policy eval/log (OPA); human task complete + optional comment (WS-HumanTask); retention-backed events (AI Act); explanation *quality* principles / Art. 86 *right* |
| **Missing bindings** | Shared **decision ID** across inference, policy eval, human task, notice, and appeal; task input ↔ model output hash; policy bundle revision ↔ decision; model version ↔ inference event ↔ decision |
| **Missing retention** | WS-HumanTask has no retention floor; AI Act logs ≥6 months may be shorter than appeal windows; explanations not required to be retained as decision packages |
| **Missing identities** | Subject identity not first-class in technical SUTs; decision outcome often not a required log field (AI Act general) |
| **Missing authority evidence** | HumanTask roles ≠ legal mandate; AI Act “authority” for oversight persons not an authority artifact store |
| **Missing policy/evidence versions** | Policy version at decision time not bound unless OPA bundle revision is *also* keyed to decision ID; relied-upon evidence (IC-11) absent across corpus |
| **Base triad** | Authorization **FAIL**; Justification **FAIL**; Validity **FAIL** |
| **Faithful reconstruction** | **Impossible** as deterministic reconstruction without custom integration profile |
| **Mode** | **Impossible** (default composition); at best **probabilistic** correlation of timestamps/IDs if operators invent ad-hoc keys |

---

### Scenario 2 — Policy change after decision

**Narrative:** A decision was valid under policy bundle `P1`. Before review, the organization deploys `P2`. Reviewers open current policy stores and current dashboards.

**Reconstruction objective:** Distinguish policy at decision time vs current policy; applicability/effective dates; authorization under historical policy; evidence available then.

**Required checklist items:** IC-01, IC-03, IC-06–IC-08, IC-07 especially, IC-10–IC-11, IC-19.

**Relevant families:** OPA bundles/decision logs; Cedar (eval without durable log); AI Act logs; Model Cards (not policy); AI RMF change management.

| Aspect | Assessment |
|---|---|
| **Available unit capabilities** | OPA **bundle revision** in decision logs (unit **PARTIAL/strong** for policy-version *if logging enabled*); AI RMF change-management *process* docs |
| **Missing bindings** | Decision ID ↔ bundle revision (present inside OPA log events, **not** linked to human task / model inference / eligibility outcome store); no first-class effective-interval object across systems |
| **Missing retention** | Cedar diagnostics not durable; if only current Rego repo retained, historical authorization collapses |
| **Missing identities** | Outcome store may not key OPA `decision_id` |
| **Missing authority evidence** | Historical actor authorization under `P1` needs actor + policy version + decision time together |
| **Missing policy/evidence versions** | Evidence snapshot at decision time often replaced by live feature stores |
| **Base triad** | Authorization **PARTIAL** *inside* OPA-only slice if decision log retained; **FAIL** for full episode; Justification **FAIL**; Validity **FAIL** (historical validity needs then-applicable rules + evidence) |
| **Faithful reconstruction** | **Partial** for authorization-only if OPA logs complete; **impossible** for full triad |
| **Mode** | **Partial** (policy-log island); otherwise **impossible** |

---

### Scenario 3 — Human override without preserved rationale

**Narrative:** The system recommends deny; a human overrides to approve. Only the final eligibility outcome is retained in the business system of record.

**Reconstruction objective:** Who overrode; authority; original recommendation; reason; evidence; timestamp; downstream effects.

**Required checklist items:** IC-01–IC-05, IC-10–IC-11, human action/override, IC-02 outcome linkage.

**Relevant families:** WS-HumanTask; EU AI Act Art. 14 (override *capability*); OTel; OPA; NISTIR 8312.

| Aspect | Assessment |
|---|---|
| **Available unit capabilities** | WS-HumanTask *can* record complete/fail with output differing from input and optional comments—**if used**; Art. 14 requires ability to disregard/override, **not** a mandated override audit record for general high-risk |
| **Missing bindings** | Outcome store ↔ human task ID; task input ↔ recommendation payload; override reason field not mandatory |
| **Missing retention** | If only final outcome kept, HumanTask history may be purged (no retention duty) |
| **Missing identities** | Override actor absent from outcome-only store |
| **Missing authority evidence** | Role on task ≠ proof of legal authority to override |
| **Missing policy/evidence versions** | Original recommendation and evidence often discarded |
| **Base triad** | All **FAIL** under outcome-only retention |
| **Faithful reconstruction** | **Impossible** under stated retention; **partial** if HumanTask instance+history retained and bound |
| **Mode** | **Impossible** (as stated); **partial** (best-case HumanTask composition with custom binding) |

---

### Scenario 4 — Model or dataset update

**Narrative:** After denial, the model is retrained and the reference dataset is refreshed. The subject challenges the original score.

**Reconstruction objective:** Reproduce or justify the original result using original model version, dataset version, feature transformation, inference inputs, environment, policy, and human action.

**Required checklist items:** IC-01, IC-03, IC-10–IC-13, IC-19, IC-23–IC-24 as conditioned; human action if any.

**Relevant families:** Model Cards; Datasheets; MLMD; OpenLineage; OTel; OPA; WS-HumanTask.

| Aspect | Assessment |
|---|---|
| **Available unit capabilities** | Model Cards model version/date; Datasheets dataset versions; MLMD/OpenLineage lineage of training/jobs; OTel execution traces |
| **Missing bindings** | Inference request ↔ model artifact version ↔ feature pipeline version ↔ decision ID; environment pin rarely bound |
| **Missing retention** | Feature stores overwrite; training lineage ≠ inference input snapshot |
| **Missing identities** | Decision ID across lineage and business outcome |
| **Missing authority/policy versions** | Policy and human action orthogonal unless bound |
| **Missing policy/evidence versions** | Point-in-time inference features often absent (IC-10/IC-11) |
| **Base triad** | Justification **FAIL**; Validity **FAIL**; Authorization depends on unrelated stores → **FAIL** compositionally |
| **Faithful reconstruction** | **Impossible** to bit-reproduce; **partial** narrative justification only if inference inputs and model hash were snapshotted—which unit sources do not require for *decisions* |
| **Mode** | **Impossible** (reproduction); **partial** (weak post-hoc story) |

---

### Scenario 5 — Logging exists but identity binding fails

**Narrative:** OTel traces, OPA decision logs, AI Act system logs, OpenLineage jobs, and WS-HumanTask history each record events for the same business denial. There is **no** stable shared decision identifier—only approximate timestamps and user emails.

**Reconstruction objective:** Reliably compose logs into one decision episode without ambiguity.

**Required checklist items:** IC-01 (binding criterion §7); all triad items depend on it.

**Relevant families:** All logging/lineage/workflow families.

| Aspect | Assessment |
|---|---|
| **Available unit capabilities** | Rich per-system events (each family contributes islands) |
| **Missing bindings** | **Decision identity** across stores; checklist §7 same-identity binding |
| **Missing retention** | Uneven TTLs cause partial disappearance of islands |
| **Missing identities** | Ambiguous correlation (multiple decisions per user per minute) |
| **Missing authority/policy/evidence versions** | Cannot attribute versions to *the* decision under ambiguity |
| **Base triad** | All **FAIL** (identity failure cascades) |
| **Faithful reconstruction** | **Impossible** without undocumented heuristics (explicitly disallowed by checklist §3.3) |
| **Mode** | **Impossible** |

---

### Scenario 6 — Appeal after partial data deletion (optional)

**Narrative:** An affected person exercises Art. 86-style explanation / complaint rights after personal data minimization deleted raw input features. Aggregated AI Act logs and a HumanTask completion record remain; feature vectors are gone.

**Reconstruction objective:** Provide meaningful historical justification and validity assessment despite deletion.

**Required checklist items:** IC-10–IC-12, IC-02, IC-07, IC-19; notice/appeal linkage.

**Relevant families:** EU AI Act (retention vs personal-data law carve-outs); WS-HumanTask; NISTIR 8312; OPA; Model Cards.

| Aspect | Assessment |
|---|---|
| **Available unit capabilities** | Possible retained logs (≥6 months, subject to data-protection law); task output/comment; explanation right (not retained schema); model card for *current* or released model |
| **Missing bindings** | Appeal case ID ↔ original decision ID ↔ deleted evidence |
| **Missing retention** | Personal-data law may force deletion of the very evidence IC-10/IC-11 need; AI Act expressly defers to that law |
| **Missing identities** | Appeal dossier may not key technical logs |
| **Missing authority/policy versions** | May survive in OPA logs if not personal data—still unbound to appeal file |
| **Base triad** | Justification **FAIL** (evidence gone); Validity **FAIL**; Authorization **PARTIAL** only if authz logs retained and bound |
| **Faithful reconstruction** | **Impossible** for justification/validity; explanation right cannot recreate deleted inputs |
| **Mode** | **Impossible** (triad); **partial** narrow authorization island |

---

## 3. Composition table

Legend: **D** = provided directly by that family (first-class); **P** = partially provided; **E** = external assumption / application payload only; **N** = not provided.

Columns: PROV | OTel | MLMD | OpenLineage | OPA | Cedar | Model Cards | Datasheets | System Cards | AI RMF | NISTIR 8312 | EU AI Act logs | WS-HumanTask

| Capability | PROV | OTel | MLMD | OL | OPA | Cedar | MC | DS | SC | RMF | 8312 | AI Act | HT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Decision identity | N | N | N | N | P | N | N | N | N | N | N | P | P |
| Subject identity | E | E | E | E | E | E | N | N | N | N | N | E | E |
| Actor identity | P | P | N | P | P | P | P | P | P | P | N | P | D |
| Actor authority | P | N | N | N | P | P | N | N | N | P | N | P | P |
| Model identity/version | E | E | D | P | E | N | D | N | P | P | N | P | E |
| Dataset identity/version | E | N | D | D | N | N | P | D | P | P | N | P | E |
| Input evidence | P | P | P | P | P | E | N | P | P | P | P | P | P |
| Policy identity/version | N | N | N | N | D | P | N | N | N | P | N | N | N |
| Explanation | N | N | N | N | N | N | P | N | N | P | D | P | E |
| Human action | P | P | N | N | N | N | N | N | P | P | N | P | D |
| Override | N | N | N | N | N | N | N | N | N | P | N | P | P |
| Timestamp | P | D | D | D | D | E | P | P | P | P | N | P | D |
| Retention | N | N | N | N | E | N | N | N | N | P | N | D | N |
| Integrity | N | N | N | N | P | N | N | N | N | N | N | N | N |
| Provenance | D | P | D | D | N | N | P | P | P | P | N | P | P |
| Appeal | N | N | N | N | N | N | N | N | N | P | N | P | N |
| Remediation | N | N | N | N | N | N | N | N | N | P | N | P | N |
| Outcome linkage | E | E | E | E | P | E | N | N | N | N | N | P | P |

### Minimum cross-component bindings required

1. **decision ID ↔ model inference event** (model version, inputs, outputs)  
2. **decision ID ↔ policy evaluation** (policy id + version/bundle revision + permit/deny/path)  
3. **decision ID ↔ human task** (task ID, actual owner, complete/fail/override semantics, timestamps)  
4. **human task ↔ actor authorization** (authority/mandate distinct from task role)  
5. **decision ID ↔ evidence snapshot** (relied-upon subset, not live store)  
6. **decision ID ↔ notice and appeal** (Art. 86/complaint case linkage)  
7. **decision ID ↔ later correction/remediation**  
8. **model version ↔ dataset and feature pipeline versions** (for challenge after drift)  
9. **policy version ↔ effective-date interval** and decision timestamp (IC-07/IC-19)  

**None** of these bindings is jointly defined as a normative, durable cross-standard contract by the unit sources reviewed. Islands exist (e.g., OPA decision_id within OPA logs; HT task identifier within HumanTask).

---

## 4. Base-triad result (compositional)

Evaluated across Scenarios 1–6 under checklist §7–§8.3. Partial evidence in unbound systems does **not** yield PASS.

### Authorization

| Question | Result |
|---|---|
| Can a later reviewer prove the actor/system was authorized at the exact time of action? | **No** in full-episode composition. **Partial** only inside an OPA decision-log island *if* retained and if that island is accepted as the whole authorization story (it is not, when humans and AI outputs co-determine eligibility). |
| **Across scenarios** | **FAIL** compositionally |

### Justification

| Question | Result |
|---|---|
| Can a later reviewer recover evidence, rule, model output, human reason, and rationale? | **No.** IC-11 reliance missing corpus-wide; explanations (8312 / Art. 86) are not durable justification packages; HumanTask reasons optional; evidence snapshots not required. |
| **Across scenarios** | **FAIL** |

### Validity

| Question | Result |
|---|---|
| Can a later reviewer determine validity under historical state, policy, authority, and evidence? | **No.** Policy/model/dataset drift scenarios (2, 4) expose missing decision-time binding; deletion (6) removes evidence; identity failure (5) blocks attribution. |
| **Across scenarios** | **FAIL** |

### Overall faithful reconstruction (base)

| Result | **FAIL** across all six scenarios for default (non-custom) composition |
|---|---|
| Best islands | OPA policy-versioned authorization (Scenario 2); HumanTask human-gate record *if* retained and bound (Scenario 3 best case) |
| Determinism | **Impossible** as deterministic full-triad reconstruction; occasional **partial** single-dimension islands; correlation without shared ID is **probabilistic** and checklist-disallowed |

---

## 5. Claim relevance (unit- and scenario-level evidence only)

| Claim | Evidence from this phase | Aggregate claim file updated? |
|---|---|---|
| **C1** | Scenarios 1, 5: many artifact classes present, triad fails without bindings | **No** |
| **C2** | Scenario 2 (authz island ≠ justification); Scenario 3 (outcome ≠ human rationale) | **No** |
| **C3** | Scenarios 2, 4, 6: drift/deletion without decision-time pins | **No** |
| **C4** | Scenario 5 / unit OTel: traces do not supply normative basis | **No** |
| **C5** | Scenario 4: lineage ≠ justification of eligibility decision | **No** |
| **C6** | Scenarios 1–3: OPA/Cedar insufficient without human/evidence/model bindings | **No** |
| **C7** | Scenario 1, 6 + NISTIR 8312 unit review: explanation principles/rights ≠ durable justification | **No** |
| **C8** | Composition table: residual gap is binding/profile-shaped; scenarios do not yet choose layer vs profile | **No** |

No universal conclusion is drawn from a single scenario; the pattern is repeated failure modes under missing bindings.

---

## 6. Implications for synthesis

1. **Stop unit-source expansion** for family coverage: the former minimum set is met (see coverage audit).  
2. **Next work** is binding/profile design and scenario falsification of **C8** (composition vs new layer)—not more peer SUTs.  
3. Optional later SUTs (ISO/IEC 42001; temporal DB; SLSA) remain **breadth**, not blockers, unless a scenario specifically requires MS certification clauses or integrity elevation.

**Not modified by this document:** unit reviews; scores inside reviews; claim inventory statuses; comparison matrix; evaluation dataset; BibTeX.
