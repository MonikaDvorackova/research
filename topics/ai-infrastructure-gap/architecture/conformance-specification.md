---
id: arch-ai-infrastructure-gap-conformance-specification
title: "Knowledge Continuity Model — Conformance Specification"
topic: ai-infrastructure-gap
type: architecture
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [architecture, conformance, knowledge-continuity, reconstruction]
checklist_version: "0.1.0"
normative_for: knowledge-continuity-conformance
specifies: architecture/knowledge-continuity-model.md
derived_from:
  - architecture/knowledge-continuity-model.md
  - architecture/reconstruction-checklist.md
---

# Knowledge Continuity Model — Conformance Specification

**Document role.** Normative, technology-neutral conformance specification for implementations claiming support for the Knowledge Continuity Model (KCM).

**Normative references (in-repo).**

- [knowledge-continuity-model.md](knowledge-continuity-model.md)
- [reconstruction-checklist.md](reconstruction-checklist.md) (v0.1.0)

**Status.** `draft`

---

## 1. Scope

This specification defines **minimum conformance requirements** and **verification methods** by which an independent evaluator determines whether an implementation conforms to the Knowledge Continuity Model for deterministic faithful reconstruction of historical AI-assisted Decision Episodes.

This specification concerns **conformance only**. It does not define implementation architecture, storage technologies, cryptographic mechanisms, database schemas, serialization formats, network protocols, vendor APIs, or deployment models.

---

## 2. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in RFC 2119.

No other dependency on RFC 2119 is required.

---

## 3. Terms

Terms inherit the Knowledge Continuity Model and reconstruction checklist v0.1.0 unless redefined here for testability.

| Term | Meaning for conformance |
|---|---|
| **Implementation** | Any system, composition, or declared profile under evaluation |
| **Decision Episode** | As in KCM §3 |
| **Decision ID** | Immutable episode identifier (KCM §3.4) |
| **Latest-only reference** | A reference that resolves to whatever artifact is current at query time rather than a sealed version/hash |
| **Declared profile** | The checklist completeness profile asserted by the implementer (base triad / audit / forensic, and any conditional elevations) |
| **Competent reconstructor** | Evaluator following the implementation’s published reconstruction procedure, using only retained structured information |

---

## 4. Conformance classes

### 4.1 KC Core

**KC Core** is the minimum class for claiming Knowledge Continuity reconstruction capability for the **base triad** profile (authorization, justification, validity) under checklist §8.3.

An implementation claiming **KC Core** MUST satisfy every requirement in this specification whose Conformance class is `Core`, including conditional Core requirements whenever their applicability condition holds for the Decision Episodes in scope.

### 4.2 KC Extended

**KC Extended** improves robustness, contestability linkage, and integrity-oriented reconstruction.

An implementation claiming **KC Extended** MUST conform to **KC Core** and MUST satisfy every requirement whose Conformance class is `Extended` that applies to its declared Extended profile scope.

### 4.3 Claims

Conformity claims MUST name the class (`KC Core` or `KC Extended`) and the declared profile. Vendor-specific profile names are out of scope for this specification.

---

## 5. Requirement identification

Requirements use stable identifiers of the form `KC-NN` (zero-padded). Identifiers MUST NOT be reused if a requirement is retired; retirement is marked obsolete without reassignment.

---

## 6. Normative requirements

For each requirement:

- **PASS** if the verification method succeeds for sample Decision Episodes in scope.
- **FAIL** if any MUST/MUST NOT clause is violated for an in-scope episode.
- Conditional requirements are **N/A** only when the stated applicability condition is false; they MUST NOT be treated as N/A merely because an implementation omitted the capability while the condition holds.

---

### KC-01 — Decision identity

| Field | Content |
|---|---|
| **Normative requirement** | Every Decision Episode MUST be assigned a Decision ID. The Decision ID MUST be available to the reconstructor as structured data. |
| **Rationale** | Without identity, bindings cannot be evaluated (KCM §3.4; composition Scenario 5). |
| **Checklist** | IC-01 |
| **KCM principles** | Decision Episode as primary object; Stable semantic identity |
| **Class** | Core |
| **Verification** | metadata inspection; record traceability |

---

### KC-02 — Decision Episode existence

| Field | Content |
|---|---|
| **Normative requirement** | For each in-scope historical decision under test, a Decision Episode object MUST exist and MUST be resolvable solely by Decision ID. |
| **Rationale** | Episode is the reconstruction unit (KCM §3). |
| **Checklist** | IC-01; §3.1 identify episode |
| **KCM principles** | Decision Episode as primary object |
| **Class** | Core |
| **Verification** | historical reconstruction; metadata inspection |

---

### KC-03 — Stable semantic identity

| Field | Content |
|---|---|
| **Normative requirement** | A Decision ID MUST NOT be reused for a different Decision Episode. A Decision ID MUST remain unchanged across appeal and remediation. Business aliases MAY exist and MUST NOT replace the Decision ID as the join key. |
| **Rationale** | Identifier collisions destroy deterministic composition. |
| **Checklist** | IC-01; §7.1 same-identity binding |
| **KCM principles** | Stable semantic identity |
| **Class** | Core |
| **Verification** | record traceability; graph consistency |

---

### KC-04 — Decision outcome and decision time

| Field | Content |
|---|---|
| **Normative requirement** | Each committed Decision Episode MUST record an interpretable `outcome` and a `decisionTime` with a declared clock domain. |
| **Rationale** | Checklist requires outcome and time for historically situated claims. |
| **Checklist** | IC-02; IC-03 |
| **KCM principles** | Historical rather than runtime truth; Explicit temporal validity |
| **Class** | Core |
| **Verification** | metadata inspection; temporal validation |

---

### KC-05 — Historical evidence preservation

| Field | Content |
|---|---|
| **Applicability** | Evidence-using Decision Episodes (default for AI-assisted decisions). |
| **Normative requirement** | The Episode MUST include an Evidence Snapshot captured for decision time. The Snapshot MUST remain resolvable for the declared retention horizon. Live stores MUST NOT be the sole source of evidence for reconstruction. |
| **Rationale** | Live feature stores overwrite historical inputs (KCM Scenario 4/6). |
| **Checklist** | IC-10 |
| **KCM principles** | Historical rather than runtime truth; Minimal sufficient reconstruction |
| **Class** | Core |
| **Verification** | historical reconstruction; version validation; temporal validation |

---

### KC-06 — Evidence reliance distinction

| Field | Content |
|---|---|
| **Applicability** | When KC-05 applies and selection/filtering can change justification. |
| **Normative requirement** | The Evidence Snapshot MUST distinguish evidence relied upon from evidence merely available. “All context logged” without reliance distinction MUST NOT be treated as satisfying this requirement. |
| **Rationale** | Checklist §7.3; IC-11. |
| **Checklist** | IC-11 |
| **KCM principles** | Minimal sufficient reconstruction |
| **Class** | Core |
| **Verification** | metadata inspection; historical reconstruction |

---

### KC-07 — Historical policy preservation

| Field | Content |
|---|---|
| **Applicability** | Policy-governed Decision Episodes. |
| **Normative requirement** | The Episode MUST reference a Policy Version whose rule content (or immutable content hash resolving to that content) is retrievable for the retention horizon. |
| **Rationale** | Current policy substitution falsifies authorization/validity (Scenario 2). |
| **Checklist** | IC-06; IC-07 |
| **KCM principles** | Versioned references; Explicit temporal validity |
| **Class** | Core |
| **Verification** | version validation; historical reconstruction |

---

### KC-08 — Policy version linkage

| Field | Content |
|---|---|
| **Applicability** | Policy-governed Decision Episodes. |
| **Normative requirement** | A binding Decision ↔ Policy Version MUST exist, MUST use the Decision ID, and MUST NOT be a latest-only reference. |
| **Rationale** | KCM binding table; checklist §7.2. |
| **Checklist** | IC-06; IC-07; §7 |
| **KCM principles** | Durable cross-system bindings; Versioned references |
| **Class** | Core |
| **Verification** | record traceability; version validation |

---

### KC-09 — Policy evaluation result

| Field | Content |
|---|---|
| **Applicability** | Policy-governed Decision Episodes. |
| **Normative requirement** | The Episode MUST retain the policy evaluation result (permit/deny or equivalent structured result) bound to the Decision ID. Where multi-rule policies require path interpretation, the Episode MUST retain applicable rule path or an equivalent evaluation digest sufficient for reconstruction. |
| **Rationale** | Bundle identity alone may be insufficient (IC-08). |
| **Checklist** | IC-08 (when conditioned); authorization triad |
| **KCM principles** | Durable cross-system bindings |
| **Class** | Core |
| **Verification** | historical reconstruction; metadata inspection |

---

### KC-10 — AI inference linkage

| Field | Content |
|---|---|
| **Applicability** | Decision Episodes where AI outputs materially participate. |
| **Normative requirement** | A binding Decision ↔ AI Inference MUST exist. The Inference record MUST include the output that participated and an inference time. |
| **Rationale** | KCM Decision ↔ AI Inference binding. |
| **Checklist** | IC-02 (outcome context); model-participating reconstruction |
| **KCM principles** | Durable cross-system bindings; Decision Episode as primary object |
| **Class** | Core |
| **Verification** | record traceability; historical reconstruction |

---

### KC-11 — Model version linkage

| Field | Content |
|---|---|
| **Applicability** | When KC-10 applies. |
| **Normative requirement** | A binding Decision ↔ Model Version (via Inference) MUST exist. The Model Version identifier MUST be immutable (version label or content hash). Latest-only model registry pointers MUST NOT be the sole reference. |
| **Rationale** | Model drift (Scenario 4); IC-13. |
| **Checklist** | IC-13 |
| **KCM principles** | Versioned references; Historical rather than runtime truth |
| **Class** | Core |
| **Verification** | version validation; record traceability |

---

### KC-12 — Dataset version linkage

| Field | Content |
|---|---|
| **Applicability** | When the declared profile requires training/reference heritage, or when reference-database matching is material to the decision. |
| **Normative requirement** | A binding Decision ↔ Dataset Version (directly or via Model/Inference) MUST exist using immutable version identifiers. |
| **Rationale** | KCM conditioned dataset binding; IC-23/IC-24. |
| **Checklist** | IC-23; IC-24 (as conditioned) |
| **KCM principles** | Versioned references |
| **Class** | Core (when applicable); otherwise Extended if voluntarily claimed |
| **Verification** | version validation; record traceability |

---

### KC-13 — Feature pipeline linkage

| Field | Content |
|---|---|
| **Applicability** | When derived features materially shape inference inputs. |
| **Normative requirement** | A binding Decision ↔ Feature Pipeline Version MUST exist using an immutable pipeline version identifier. |
| **Rationale** | Feature pipeline drift breaks justification context. |
| **Checklist** | IC-10; IC-15/IC-16 as conditioned analogs for transforms |
| **KCM principles** | Versioned references; Durable cross-system bindings |
| **Class** | Core (when applicable) |
| **Verification** | version validation; record traceability |

---

### KC-14 — Human review linkage

| Field | Content |
|---|---|
| **Applicability** | When a human materially affects the outcome. |
| **Normative requirement** | A binding Decision ↔ Human Review MUST exist. The Human Review MUST identify the actor and the action (e.g., approve, reject, escalate) and MUST record review time. |
| **Rationale** | Human-gate continuity (Scenario 1, 3). |
| **Checklist** | IC-04 |
| **KCM principles** | Human responsibility preservation |
| **Class** | Core |
| **Verification** | record traceability; historical reconstruction |

---

### KC-15 — Human review rationale

| Field | Content |
|---|---|
| **Applicability** | When KC-14 applies. |
| **Normative requirement** | Each Human Review that affects the outcome MUST include a non-empty rationale in retained structured form. Commitment of such a review without rationale MUST NOT be accepted by a conformant implementation. |
| **Rationale** | Scenario 3 failure mode. |
| **Checklist** | Justification triad; IC-04 context |
| **KCM principles** | Human responsibility preservation; Minimal sufficient reconstruction |
| **Class** | Core |
| **Verification** | metadata inspection; historical reconstruction |

---

### KC-16 — Override linkage

| Field | Content |
|---|---|
| **Applicability** | When a human disregards, reverses, or replaces an AI output for the Episode. |
| **Normative requirement** | A binding Decision ↔ Override MUST exist. The Override MUST reference the original AI Inference and the replacement outcome, actor, and override time. |
| **Rationale** | Override capability without record is non-conformant (KCM Scenario 3). |
| **Checklist** | IC-02; IC-04 |
| **KCM principles** | Human responsibility preservation; Durable cross-system bindings |
| **Class** | Core |
| **Verification** | record traceability; historical reconstruction |

---

### KC-17 — Override rationale

| Field | Content |
|---|---|
| **Applicability** | When KC-16 applies. |
| **Normative requirement** | Each Override MUST include a non-empty rationale. Commitment without rationale MUST NOT be accepted. |
| **Rationale** | Same as KC-15 for override acts. |
| **Checklist** | Justification triad |
| **KCM principles** | Human responsibility preservation |
| **Class** | Core |
| **Verification** | metadata inspection |

---

### KC-18 — Authority preservation

| Field | Content |
|---|---|
| **Applicability** | When authorization reconstruction is in scope (default for governance/audit Decision Episodes). |
| **Normative requirement** | For each human or system act that commits or overrides the outcome, an Authority object MUST be bound to the Decision Episode (directly or via Human Review/Override). Authority MUST be distinct from mere authentication identity when mandate/delegation differs from login. |
| **Rationale** | IC-05; KCM Authority object. |
| **Checklist** | IC-05 |
| **KCM principles** | Human responsibility preservation |
| **Class** | Core |
| **Verification** | metadata inspection; record traceability |

---

### KC-19 — Authority temporal validity

| Field | Content |
|---|---|
| **Applicability** | When KC-18 applies. |
| **Normative requirement** | Each Authority used MUST declare `validFrom` and `validTo` (or equivalent interval). The act time MUST fall within that interval, or reconstruction MUST report authority FAIL. |
| **Rationale** | Role drift after decision time. |
| **Checklist** | IC-05; IC-19 |
| **KCM principles** | Explicit temporal validity |
| **Class** | Core |
| **Verification** | temporal validation; historical reconstruction |

---

### KC-20 — Policy temporal validity

| Field | Content |
|---|---|
| **Applicability** | When KC-07 applies. |
| **Normative requirement** | Each bound Policy Version MUST declare a validity interval. Decision effective time (or decisionTime if effective time is not separately declared) MUST fall within that interval, or reconstruction MUST report validity FAIL. |
| **Rationale** | Scenario 2; IC-07/IC-19. |
| **Checklist** | IC-07; IC-19 |
| **KCM principles** | Explicit temporal validity; Historical rather than runtime truth |
| **Class** | Core |
| **Verification** | temporal validation; version validation |

---

### KC-21 — Explanation linkage

| Field | Content |
|---|---|
| **Applicability** | When the declared profile requires decision-time explanations, or when an explanation is retained for the Episode. |
| **Normative requirement** | If an explanation is claimed as historical, a binding Decision ↔ Explanation MUST exist, with production time, and MUST NOT be satisfied by an unbound post-hoc explanation generated at reconstruction time. Explanations MUST NOT be the sole justification record. |
| **Rationale** | C7; KCM Explanation object. |
| **Checklist** | Related to justification; not a substitute for IC-10/IC-11 |
| **KCM principles** | Historical rather than runtime truth; Minimal sufficient reconstruction |
| **Class** | Extended (Core when applicability claimed by profile) |
| **Verification** | historical reconstruction; metadata inspection |

---

### KC-22 — Notification linkage

| Field | Content |
|---|---|
| **Applicability** | Person-affecting Decision Episodes under profiles requiring notice. |
| **Normative requirement** | A binding Decision ↔ Notification MUST exist, identifying subject, send time, and content hash or retained content. |
| **Rationale** | Contestability continuity (KCM Notification). |
| **Checklist** | Human/subject context; disclosure |
| **KCM principles** | Durable cross-system bindings |
| **Class** | Extended (Core when applicability claimed) |
| **Verification** | record traceability |

---

### KC-23 — Appeal linkage

| Field | Content |
|---|---|
| **Applicability** | When an appeal, explanation request, or complaint exists for the Episode. |
| **Normative requirement** | A binding Decision ↔ Appeal MUST exist. Appeals MUST NOT be retained only as unbound case files. |
| **Rationale** | Scenario 6 orphan appeals. |
| **Checklist** | Continuity of contestation |
| **KCM principles** | Durable cross-system bindings |
| **Class** | Extended (Core when appeal exists) |
| **Verification** | record traceability; historical reconstruction |

---

### KC-24 — Remediation linkage

| Field | Content |
|---|---|
| **Applicability** | When correction, withdrawal, compensation, or re-decision occurs. |
| **Normative requirement** | A binding Decision ↔ Remediation MUST exist. Remediation MUST NOT silently overwrite the original Decision outcome. |
| **Rationale** | Append-only correction history (KCM §6.3). |
| **Checklist** | IC-02 continuity; §3.1 distinguish historical structure |
| **KCM principles** | Historical rather than runtime truth |
| **Class** | Core (when remediation occurs); Extended for proactive remediation audit trails |
| **Verification** | record traceability; historical reconstruction |

---

### KC-25 — Correction history

| Field | Content |
|---|---|
| **Normative requirement** | Corrections MUST be append-only relative to the original Decision ID. Superseding decisions MUST reference the original Decision ID. Reconstruction MUST be able to present commitment-time state and the ordered correction chain. |
| **Rationale** | KCM temporal model; checklist §3.3. |
| **Checklist** | §3.1 items 1–7 |
| **KCM principles** | Historical rather than runtime truth |
| **Class** | Core |
| **Verification** | historical reconstruction; graph consistency |

---

### KC-26 — Immutable historical references

| Field | Content |
|---|---|
| **Normative requirement** | References from a committed Decision Episode to Policy Version, Model Version, Dataset Version, Feature Pipeline Version, Evidence Snapshot, and Authority MUST NOT be latest-only. After commitment, those bindings MUST NOT be rewritten. |
| **Rationale** | Versioned references principle; Scenario 2/4. |
| **Checklist** | §7.2 decision-time binding; IC-07; IC-13 |
| **KCM principles** | Versioned references; Immutable historical references |
| **Class** | Core |
| **Verification** | version validation; metadata inspection |

---

### KC-27 — Cross-system bindings

| Field | Content |
|---|---|
| **Normative requirement** | Where episode components are stored in multiple systems, each retained component record used for reconstruction MUST carry the Decision ID or an explicit mapping to it that is itself retained. Correlation solely by approximate timestamps or personal identifiers MUST NOT be accepted as conformance. |
| **Rationale** | Scenario 5; checklist §3.3; §7.1. |
| **Checklist** | §7.1 |
| **KCM principles** | Durable cross-system bindings; Stable semantic identity |
| **Class** | Core |
| **Verification** | record traceability; graph consistency |

---

### KC-28 — Minimal reconstruction completeness

| Field | Content |
|---|---|
| **Normative requirement** | For the declared base triad profile, reconstruction using only retained structured information and the published procedure MUST yield Decision identity, outcome, decision time, and passing Authorization, Justification, and Validity results as defined in §8–§9. Bit-exact compute replay MUST NOT be required for Core conformance. |
| **Rationale** | Checklist §3.1–§3.2; KCM reconstruction algorithm. |
| **Checklist** | §3; §8.3 |
| **KCM principles** | Minimal sufficient reconstruction |
| **Class** | Core |
| **Verification** | historical reconstruction |

---

### KC-29 — Technology neutrality

| Field | Content |
|---|---|
| **Normative requirement** | A conformity claim for this specification MUST NOT require use of a particular storage technology, ledger, graph database, message bus, cloud vendor, or product. Conformance evaluation MUST assess information and bindings only. |
| **Rationale** | KCM technology neutrality; checklist §1.3. |
| **Checklist** | §1.3 |
| **KCM principles** | Technology neutrality |
| **Class** | Core |
| **Verification** | document inspection |

---

### KC-30 — Published reconstruction procedure

| Field | Content |
|---|---|
| **Normative requirement** | The implementer MUST publish a reconstruction procedure sufficient for a competent reconstructor to locate episode objects and bindings by Decision ID without undocumented operator memory. |
| **Rationale** | Checklist §3.1 preamble. |
| **Checklist** | §3.1 |
| **KCM principles** | Minimal sufficient reconstruction; Incremental adoptability |
| **Class** | Core |
| **Verification** | document inspection; historical reconstruction |

---

### KC-31 — Fail-closed reconstruction

| Field | Content |
|---|---|
| **Normative requirement** | If any Core-applicable mandatory binding or object is missing for an Episode, reconstruction MUST report failure for the affected triad element(s) and MUST NOT fabricate values via undocumented heuristics. |
| **Rationale** | Checklist §3.3; KCM algorithm step 10. |
| **Checklist** | §3.3 |
| **KCM principles** | Historical rather than runtime truth |
| **Class** | Core |
| **Verification** | historical reconstruction |

---

### KC-32 — Subject linkage

| Field | Content |
|---|---|
| **Applicability** | Person-affecting or entity-affecting Decision Episodes. |
| **Normative requirement** | The Episode MUST bind a Subject identifier (or lawful durable privacy-preserving reference) to the Decision ID. |
| **Rationale** | KCM Subject object. |
| **Checklist** | Episode interpretability; human context |
| **KCM principles** | Decision Episode as primary object |
| **Class** | Core (when applicable) |
| **Verification** | metadata inspection; record traceability |

---

### KC-33 — Audit record linkage (Extended)

| Field | Content |
|---|---|
| **Normative requirement** | Implementations claiming KC Extended integrity support MUST retain Audit Records bound to the Decision ID with event time and payload digest sufficient to detect tampering relative to stated trust assumptions. |
| **Rationale** | KCM Audit Record; IC-21 elevated. |
| **Checklist** | IC-21 |
| **KCM principles** | Durable cross-system bindings |
| **Class** | Extended |
| **Verification** | metadata inspection; record traceability |

---

### KC-34 — Excluded evidence accounting (Extended)

| Field | Content |
|---|---|
| **Applicability** | When exclusion/filtering occurred or the declared Extended profile requires negative evidential accounting. |
| **Normative requirement** | The Evidence Snapshot MUST record excluded evidence references and, where applicable, exclusion reasons. |
| **Rationale** | IC-12; KCM Evidence Snapshot optional fields elevated. |
| **Checklist** | IC-12 |
| **KCM principles** | Minimal sufficient reconstruction |
| **Class** | Extended |
| **Verification** | metadata inspection; historical reconstruction |

---

## 7. Reconstruction conformance

### 7.1 Input

Reconstruction evaluation MUST supply:

1. a Decision ID;
2. the implementation’s published reconstruction procedure;
3. access to retained structured stores declared by that procedure.

### 7.2 Minimum expected outputs

A reconstruction run MUST produce structured outputs stating:

1. Decision identity, outcome, decision time, clock domain;
2. Authorization statement (pass/fail + evidence pointers);
3. Justification statement (pass/fail + evidence pointers);
4. Validity statement (pass/fail + evidence pointers);
5. Lists of bound object identifiers used;
6. Explicit gap list for any missing mandatory element.

### 7.3 Outcome classes

| Class | Definition |
|---|---|
| **Complete reconstruction** | All Core-applicable requirements PASS for the Episode; triad elements in §9 all PASS. |
| **Partial reconstruction** | At least one triad element PASS and at least one FAIL or Core-applicable requirement FAIL; gaps MUST be explicit. |
| **Failed reconstruction** | Decision Episode not resolvable; or identity ambiguous; or reconstructor must use undocumented memory/heuristics; or all triad elements FAIL. |

### 7.4 Acceptable uncertainty

Uncertainty MAY remain regarding:

- bit-exact numerical reproduction of non-deterministic model internals;
- subjective quality of rationale text;
- information lawfully redacted **if** reliance semantics remain reconstructable.

Uncertainty MUST NOT be used to hide missing Decision ID, Policy Version, Evidence Snapshot reliance distinction, Authority, or rewritten historical bindings.

### 7.5 Historical consistency

Reconstruction MUST use sealed historical references. Use of current policy, current model, or current feature values in place of bound versions MUST cause FAIL for the affected triad element(s).

---

## 8. Base-triad verification

### 8.1 Authorization — PASS only if all hold

1. Actor(s) participating in commitment/override are identified (KC-14/KC-16 as applicable).
2. Authority for each such act is bound and temporally valid at act time (KC-18, KC-19).
3. For policy-governed episodes: Policy Version bound, temporally valid, and evaluation result retained (KC-07–KC-09, KC-20).
4. All of the above join on the same Decision ID (KC-01, KC-27).

Otherwise Authorization **FAIL**.

### 8.2 Justification — PASS only if all hold

1. Evidence Snapshot bound and resolvable (KC-05).
2. Reliance distinction present when applicable (KC-06).
3. If AI participated: Inference and Model Version bound (KC-10, KC-11); Feature Pipeline Version bound when applicable (KC-13).
4. If humans affected outcome: review/override rationales present (KC-15, KC-17 as applicable).
5. No dependence on unbound post-hoc explanation as sole justification (KC-21).

Otherwise Justification **FAIL**.

### 8.3 Validity — PASS only if all hold

1. Policy Version temporally covers decision/effective time when policy-governed (KC-20).
2. Evaluation result is consistent with recorded outcome representation, or an explicit Remediation chain documents later change without erasing commitment-time validity artifacts (KC-09, KC-24, KC-25).
3. Reconstruction does not substitute current rules for historical Policy Version (KC-26).

Otherwise Validity **FAIL**.

### 8.4 Faithful reconstruction (base)

**PASS** only if Authorization, Justification, and Validity all PASS for the Episode under the declared profile (checklist §8.3). Otherwise **FAIL** (or **PARTIAL** only as a reporting label when §7.3 partial applies; Core conformity claims require base PASS on sampled in-scope episodes).

---

## 9. Non-conformance

| Failure mode | Typical violated requirements | Effect |
|---|---|---|
| Missing Decision Episode | KC-02 | Failed reconstruction |
| Missing / colliding Decision ID | KC-01, KC-03, KC-27 | Failed reconstruction; identity ambiguity |
| Missing historical policy / latest-only policy | KC-07, KC-08, KC-26, KC-20 | Authorization/Validity FAIL |
| Missing authority | KC-18, KC-19 | Authorization FAIL |
| Broken bindings / timestamp-only join | KC-27 | Failed or non-deterministic reconstruction |
| Missing rationale on review/override | KC-15, KC-17 | Justification FAIL; Core FAIL |
| Orphan explanations | KC-21 | Explanation non-historical; cannot rescue Justification |
| Non-versioned evidence / live-only features | KC-05, KC-06, KC-26 | Justification FAIL |
| Missing timestamps / clock domain | KC-04 | Core FAIL; temporal validation impossible |
| Silent outcome overwrite | KC-24, KC-25 | Historical consistency FAIL |
| Technology-mandating conformity claim | KC-29 | Claim invalid under this specification |

---

## 10. Traceability matrix

Principles (KCM §2) → Requirements → Checklist categories.

| KCM principle | Requirements | Checklist / triad |
|---|---|---|
| Decision Episode as primary object | KC-01, KC-02, KC-04, KC-28, KC-32 | IC-01, IC-02, IC-03; §3.1 |
| Stable semantic identity | KC-01, KC-03, KC-27 | IC-01; §7.1 |
| Durable cross-system bindings | KC-08–KC-17, KC-22–KC-24, KC-27 | §7 |
| Historical rather than runtime truth | KC-05, KC-21, KC-25, KC-26, KC-31 | §3.1 item 7; §3.3 |
| Explicit temporal validity | KC-04, KC-19, KC-20 | IC-03, IC-07, IC-19 |
| Versioned references | KC-07, KC-11–KC-13, KC-26 | IC-07, IC-13, IC-23, IC-24 |
| Human responsibility preservation | KC-14–KC-19 | IC-04, IC-05; justification |
| Minimal sufficient reconstruction | KC-06, KC-28, KC-30, KC-31 | §3.1–§3.2; IC-10, IC-11 |
| Technology neutrality | KC-29 | §1.3 |
| Incremental adoptability | KC-27, KC-30 | §7.4 composition allowed |

| Checklist focus | Requirements |
|---|---|
| IC-01 Decision identity | KC-01, KC-02, KC-03 |
| IC-02 Outcome | KC-04, KC-16 |
| IC-03 Decision time | KC-04 |
| IC-04 Actors | KC-14, KC-16, KC-32 |
| IC-05 Authority | KC-18, KC-19 |
| IC-06/IC-07 Policy + version | KC-07, KC-08, KC-20, KC-26 |
| IC-08 Applicable rules | KC-09 |
| IC-10/IC-11 Evidence | KC-05, KC-06 |
| IC-12 Excluded evidence | KC-34 |
| IC-13 Model version | KC-11 |
| IC-19 Temporal context | KC-19, KC-20 |
| IC-21 Integrity | KC-33 |
| IC-23/IC-24 Lineage/heritage | KC-12 |
| §8.3 Authorization | §8.1; KC-07–09, KC-14–20, KC-27 |
| §8.3 Justification | §8.2; KC-05–06, KC-10–17, KC-21 |
| §8.3 Validity | §8.3; KC-07–09, KC-20, KC-24–26 |

---

## 11. Relationship to existing governance infrastructure

This specification **complements** and does **not replace**:

- provenance systems;
- observability systems;
- lineage and metadata systems;
- policy engines;
- authorization systems;
- documentation artifacts;
- explainability tooling;
- human workflow systems;
- AI governance / risk-management processes;
- legal/operational logging regimes.

Conformant implementations MAY realize episode objects and bindings by composing those components, provided KC-01–KC-31 (and applicable conditionals) are met.

---

## 12. Scope exclusions

Out of scope for this specification:

- implementation architecture;
- storage technologies;
- cryptographic mechanisms (except as optional Extended evidence under KC-33);
- database schemas;
- serialization formats;
- network protocols;
- vendor APIs;
- deployment models;
- decision quality, fairness, security, or privacy programmes as such.

---

## 13. Future extensions

Future revisions MAY define additional conformance classes (for example sector profiles or integrity-elevated classes). Such classes are **reserved** and are not defined by this draft.

---

## 14. Conformance statement template

Implementers SHOULD publish:

> “[Product/composition] claims **KC Core** | **KC Extended** conformance to the Knowledge Continuity Model Conformance Specification (draft [date]) for Decision Episodes of type [scope], under checklist profile [base triad | …]. Reconstruction procedure: [URI].”

---

## Related artifacts

| Artifact | Relationship |
|---|---|
| [knowledge-continuity-model.md](knowledge-continuity-model.md) | Normative model specified herein |
| [reconstruction-checklist.md](reconstruction-checklist.md) | Evaluation criteria mapped in §8–§10 |
| [composition-analysis.md](../evaluation/composition-analysis.md) | Problem diagnosis motivating testable bindings |
| [reconstruction-scenarios.md](../evaluation/reconstruction-scenarios.md) | Scenario set for practical verification campaigns |
