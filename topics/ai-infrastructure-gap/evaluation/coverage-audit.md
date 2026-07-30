---
id: eval-ai-infrastructure-gap-coverage-audit-2026-07-29
title: "Coverage audit of completed reconstruction reviews"
topic: ai-infrastructure-gap
type: evaluation
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, coverage, reconstruction, kill-list, synthesis-readiness]
checklist_version: "0.1.0"
scenarios_doc: evaluation/reconstruction-scenarios.md
---

# Coverage audit of completed reconstruction reviews

**Purpose:** Assess whether the current review corpus covers the main *families* of approaches relevant to reconstructing legally relevant AI decisions, and whether the corpus may stop unit-source expansion in favour of scenario/composition analysis.

**Not this document:** methodology-consistency audit; scientific synthesis conclusion; approach ranking; claim promotion; matrix/dataset updates.

**Completed SUTs (unit reviews, 2026-07-29):**

| SUT | File |
|---|---|
| W3C PROV-DM | `2026-07-29-w3c-prov-dm.md` |
| OpenTelemetry Spec | `2026-07-29-opentelemetry-specification.md` |
| Google ML Metadata | `2026-07-29-google-ml-metadata.md` |
| OpenLineage | `2026-07-29-openlineage.md` |
| Open Policy Agent | `2026-07-29-open-policy-agent.md` |
| Cedar Policy Language | `2026-07-29-cedar.md` |
| Model Cards (Mitchell et al.) | `2026-07-29-model-cards.md` |
| Datasheets for Datasets | `2026-07-29-datasheets-for-datasets.md` |
| System Cards (Procope et al.) | `2026-07-29-system-cards.md` |
| NIST AI RMF 1.0 | `2026-07-29-nist-ai-rmf-1.0.md` |
| NISTIR 8312 (XAI principles) | `2026-07-29-nistir-8312-xai-principles.md` |
| EU AI Act record-keeping / logs | `2026-07-29-eu-ai-act-decision-audit-records.md` |
| OASIS WS-HumanTask 1.1 | `2026-07-29-oasis-ws-humantask-human-review-workflow.md` |

**Scenario / composition analysis:** `evaluation/reconstruction-scenarios.md` (2026-07-29).

---

## 0. Minimum-before-synthesis reassessment

### Former minimum (§4.1 prior revision)

1. Explanation / contestability (or XAI principles) — unlock **C7**  
2. Technical logging / decision records — audit-logging + decision-record kill-list gap  
3. Human decision and review records — workflow / human-gate family  
4. **Plus one of:** legal/regulatory documentation duties (EU AI Act) **or** management-system standard (ISO/IEC 42001)

### Evidence check against the current corpus

| Requirement | Status | Evidence |
|---|---|---|
| (1) XAI / explanation family | **Met** | NISTIR 8312 unit review — explanation principles; **not** full contestability/appeal-record coverage |
| (2) Decision / audit records | **Met (with discipline)** | EU AI Act Arts. 12/19/26 — mandated automatic logs + retention; **not** a complete decision-episode schema for all high-risk systems |
| (3) Human review workflow | **Met (with discipline)** | WS-HumanTask 1.1 — task identity, roles, complete/fail/forward, history API; **workflow capability ≠ preservation duty** |
| (4a) Legal documentation / logging duties | **Met** | Same EU AI Act review (technical documentation Art. 11/18/Annex IV + record-keeping) |
| (4b) Management-system standard | **Not met — explicitly deferred** | No ISO/IEC 42001 (or equivalent MS) unit review; allowed because §4.1 required *one of* {legal duty, MS}, and (4a) is done |

### Decision

**The former minimum before synthesis is satisfied.**

**Stop unit-source expansion** unless a concrete scenario exposes a requirement that no existing family can even partially address (see §6). Residual gaps are **compositional bindings**, optional breadth (ISO 42001, temporal DB, SLSA), or **partial** dimensions (contestability depth, system-doc thinness)—not missing mandatory families from the former minimum set.

**Exact reason:** Items (1)–(3) and (4a) each have a version-pinned primary-source unit review. Claim hooks **C4–C7** each now have at least one dedicated unit review. Further peer SUTs would not add a new first-class capability category relative to checklist IC-01–IC-24 beyond what scenario/composition work must test (**C1**, **C3**, **C8**).

---

## 1. Family coverage

Coverage status meanings:

- **Strong** — at least one version-pinned primary-source review that is a central exemplar of the family  
- **Partial** — family touched by a completed SUT, but the exemplar is thin, adjacent, leaves a distinct sub-family untested, or capability ≠ preservation  
- **Missing** — no completed unit review whose first-class concepts are primarily of that family  
- **Not needed for current synthesis** — optional/deferred under the stopping rule; labeled so synthesis does not pretend coverage

### 1.1 Provenance models — **Strong**

Covered by W3C PROV-DM. No further unit SUT required for family coverage.

### 1.2 Runtime observability — **Strong**

Covered by OpenTelemetry Specification. Claim **C4** exemplar.

### 1.3 ML lifecycle metadata — **Strong**

Covered by Google ML Metadata.

### 1.4 Data lineage — **Strong**

Covered by OpenLineage.

### 1.5 Policy engines — **Strong**

Covered by Open Policy Agent (Rego, bundles, decision logs). Claim **C6**.

### 1.6 Authorization policy languages — **Strong**

Covered by Cedar (language/diagnostics without first-class durable decision-log schema).

### 1.7 Model documentation — **Strong**

Covered by Model Cards (Mitchell et al. 2019).

### 1.8 Dataset documentation — **Strong**

Covered by Datasheets for Datasets.

### 1.9 System documentation — **Partial**

Covered by System Cards (Procope et al. 2022)—thin foundational note. Sufficient with Model Cards + Datasheets for documentation-stack coverage; IBM FactSheets optional breadth.

### 1.10 AI governance frameworks (process/culture) — **Partial**

Covered partly by NIST AI RMF GOVERN. Dedicated multi-stakeholder documentation-process playbooks not unit-reviewed. **Not needed for current synthesis** beyond RMF.

### 1.11 AI risk management standards — **Strong**

Covered by NIST AI RMF 1.0.

### 1.12 Management-system standards — **Missing** → **Not needed for current synthesis**

Still no ISO/IEC 42001 (or peer MS) unit review. Explicitly **deferred**: legal-duty instrument (EU AI Act) was the chosen alternative in the former minimum pair. Re-open only if synthesis must answer “certified AI MS already forces reconstruction records.”

### 1.13 Legal and regulatory documentation duties — **Strong** (was missing)

Covered by EU AI Act review (Art. 11/18, Annex IV technical documentation; record-keeping Arts. 12/19/26). **Do not** mark this family missing after that review. GDPR-only packaging remains optional breadth.

### 1.14 Technical logging and decision/audit records — **Partial** → **Strong/Partial (disciplined)**

| Sub-assessment | Status |
|---|---|
| Legally mandated automatic event logs + retention | **Strong** via EU AI Act |
| Explicit general decision-episode record schema | **Partial** — biometric Annex III 1(a) minimum fields only; general high-risk logs are purpose-based without full IC-01–IC-11 schema |
| Policy-engine decision logs | **Strong** via OPA (narrow authorization slice) |

**Discipline:** logging existence ≠ full decision-record coverage. Family is **no longer missing**; synthesis must treat it as **strong on retention-backed operational logs**, **partial on decision-episode completeness**.

### 1.15 Software supply-chain attestations — **Missing** → **Not needed for current synthesis**

Optional (IC-21/IC-22 elevated profiles). Defer SLSA/in-toto.

### 1.16 Explainability — **Strong** (was missing)

Covered by NISTIR 8312 (four principles). Unlocks **C7** unit testing.

### 1.17 Contestability — **Partial**

| Source | Contribution |
|---|---|
| NISTIR 8312 | Explanation quality — **not** contestability/appeal records |
| EU AI Act Art. 86 | Right to explanation of individual decisions — **right**, not retained appeal schema |
| AI RMF / Art. 27 FRIA | Complaint-mechanism *arrangements* mentioned — process, not episode records |

**Discipline:** do **not** call contestability fully covered because NISTIR 8312 discusses explanations. Full appeal/remediation record family remains **partial**. Optional later SUT: GDPR Art. 22 package—only if a scenario cannot be evaluated with Art. 86 + process mentions.

### 1.18 Human review and override records — **Strong/Partial (disciplined)** (was missing)

Covered by WS-HumanTask 1.1 (task ID, roles, complete/fail/forward/delegate, optional comments, history API). EU AI Act Art. 14 adds override *capability* and biometric verifier logging.

**Discipline:** do **not** call human review records missing after WS-HumanTask; do **distinguish workflow capability from preservation duty** (no retention floor; reasons optional; legal authority objects absent).

### 1.19 Temporal binding (decision-time criteria) — **Partial**

Unit fragments: OPA bundle revision; Model Cards model date/version; Datasheets dataset timeframes; AI Act use-period timestamps (biometric); HumanTask timestamps; AI RMF temporal Profiles (org-level). **No** dedicated temporal-DB SUT. Advance via **scenarios** (especially policy/model drift)—not blocking for stopping unit reviews.

### 1.20 Policy-version preservation — **Partial**

Strongest unit support: OPA decision logs + bundles. Not general across AI Act logs or HumanTask. Composition gap.

### 1.21 Authorization-at-decision-time — **Partial**

OPA/Cedar evaluate authorization; OPA can log; HumanTask records who acted; AI Act assigns oversight authority expectations. Binding actor+policy+time+decision still compositional.

### 1.22 Evidence-at-decision-time — **Partial**

Inputs appear as payloads/logs in places (OPA input, HumanTask input, biometric match inputs). **IC-11 reliance** remains weakly supported corpus-wide.

### 1.23 Decision identity — **Partial**

OPA decision_id (island); HumanTask task identifier (island); AI Act use-period (biometric subclass). **No** cross-family shared decision identity. Scenario 5 stress-tests this.

### 1.24 Appeal and remediation records — **Partial**

Art. 86 rights; Art. 20 corrective actions (system-level); FRIA complaint arrangements; HumanTask has no appeal object. Not strong.

---

## 2. Cross-walk to charter kill list (coverage only)

| Kill-list abstraction | Coverage via completed reviews | Gap |
|---|---|---|
| Audit logging | **Strong/Partial** — AI Act retention-backed logs + OPA decision logs | General decision-episode schema still thin |
| Event sourcing | Missing | Optional / not needed now |
| Distributed tracing / OTel | Strong | — |
| Data and model provenance | Strong | — |
| W3C PROV | Strong | — |
| Policy engines (OPA, Cedar, …) | Strong | — |
| Workflow engines / human tasks | **Strong/Partial** — WS-HumanTask | Preservation/retention not mandated |
| Knowledge graphs | Missing | Optional / not needed now |
| Explainability methods / principles | **Strong** — NISTIR 8312 | Reasoning-trace *products* optional depth |
| Model reasoning traces | Partial via 8312 boundary (out of scope algorithms) | Optional depth for C7 |
| Decision records | **Partial** — AI Act + OPA + HT islands | Shared decision ID + IC-11 |
| Temporal databases | Missing | Optional; C3 via scenarios |
| Cryptographic ledgers | Missing | Optional / not needed now |

---

## 3. Claim-test readiness (coverage lens only)

| Claim | Unit-review coverage | Scenario/composition next |
|---|---|---|
| C1 | Strong unit illustration + scenarios 1, 5 | Bindings analysis (done in scenarios doc); no more peer SUTs |
| C2 | Strengthened by OPA vs HT vs provenance orthogonality; scenarios 2–3 | Continue scenario matrix |
| C3 | Partial unit fragments; scenarios 2, 4, 6 | Optional temporal-DB SUT only if scenarios insufficient |
| C4 | Strong (OTel) | — |
| C5 | Strong (PROV, MLMD, OpenLineage) | — |
| C6 | Strong (OPA, Cedar) + scenarios 1–3 | — |
| C7 | **Now unit-tested** (NISTIR 8312) + scenarios 1, 6 | Optional reasoning-trace depth |
| C8 | Not a unit-SUT claim | **Primary next**: composition profile vs layer using scenarios |

Claim inventory **statuses were not updated** by this audit (remain `hypothesis`). New reviews/scenarios supply **unit- and scenario-level evidence** only.

---

## 4. Unit versus composition (summary)

Every strong/partial family still fails checklist §7 **same-identity binding** when composed naively. See `reconstruction-scenarios.md` §1 and §3 for the binding list (decision ID ↔ inference, policy eval, human task, evidence snapshot, notice/appeal, correction; model ↔ dataset/features; policy version ↔ effective interval).

**Synthesis implication:** the research gap to argue is **missing durable cross-system bindings** (and uneven retention), not absence of provenance *or* policy engines *or* human workflow *or* logging *as isolated families*.

---

## 5. Recommendations (updated)

### 5.1 Unit reviews

**Do not add** further unit-SUT reviews for family coverage.

**Exception:** add a unit review only if a written scenario demonstrates a **blocking** requirement that no existing family addresses even partially—and document that reason in this audit before writing the review.

### 5.2 Immediate next steps (synthesis path)

1. **Scenario analysis** — maintain/extend `evaluation/reconstruction-scenarios.md` (six scenarios defined 2026-07-29).  
2. **Composition analysis** — deepen binding contracts / best-faith composition profiles against checklist §7 (**C8**).  
3. **Claim handling** — refine support **only at unit/scenario evidence level** until workflow explicitly permits aggregate claim status changes (Phase 1 research-plan step 3).  

### 5.3 Optional breadth (not blocking)

| Candidate | When to consider |
|---|---|
| ISO/IEC 42001:2023 | If MS-certification counterargument must be closed |
| Temporal DB / SQL:2011 temporal | If C3 needs a dedicated falsification SUT beyond scenarios |
| SLSA / in-toto | Elevated integrity profiles |
| GDPR Art. 22 package | If contestability depth blocks a specific scenario evaluation |
| IBM FactSheets | System-doc depth only |

### 5.4 Still redundant

Additional authz languages after OPA+Cedar; additional lineage stores after OpenLineage+MLMD; vendor card templates; Generative AI Profile after AI RMF 1.0 Core; second general provenance model.

### 5.5 Stopping rule (applied)

| Condition | Met? |
|---|---|
| Family coverage strong / partial-with-deferral / addressed by former minimum | **Yes** |
| C4–C7 each have ≥1 dedicated unit review | **Yes** (C7 via NISTIR 8312) |
| Next SUT would not add new IC capability category | **Yes** for typical candidates |
| Diminishing returns within families | **Yes** |
| Corpus supports kill-list narrative by family; residuals labeled composition (**C8**) | **Yes** |

**Stop unit expansion. Proceed with scenarios and composition.**

---

## 6. Remaining evidence gaps

### Blocking for *family-coverage synthesis readiness*

**None.**

### Non-blocking / compositional (must be handled in synthesis narrative, not by more peer SUTs)

- Cross-system **decision identity** and durable bindings  
- **IC-11** relied-upon evidence  
- **Contestability/appeal** record schemas (rights ≠ records)  
- **Retention** mismatch (AI Act floors vs HumanTask/OTel/lineage TTLs)  
- **Management-system** counterargument (deferred ISO 42001)  
- **Temporal-DB** counterargument (deferred; scenarios carry C3 for now)

### Genuinely blocking a *specific* future claim

Only if publication claims “ISO 42001 already requires reconstruction-complete records” or “bitemporal databases already solve C3 in production AI stacks” without evidence—then reopen the corresponding optional SUT. Those claims are **not** required for current synthesis kickoff.

---

## 7. Bottom line

| Class | Families |
|---|---|
| **Strong** | Provenance; observability; ML metadata; data lineage; policy engines; authorization languages; model documentation; dataset documentation; AI risk management; explainability principles (NISTIR 8312); legal documentation/logging duties (EU AI Act) |
| **Partial** | System documentation; governance-as-process; decision-episode completeness; contestability; human-review *preservation*; temporal binding; policy-version breadth; authorization-at-decision-time composition; evidence-at-decision-time (esp. IC-11); decision identity; appeal/remediation records |
| **Missing** | — for former minimum set |
| **Not needed for current synthesis** | Management-system standards (ISO 42001 deferred); supply-chain attestations; event sourcing; knowledge graphs; cryptographic ledgers; temporal-DB SUT |

**Minimum before synthesis:** **satisfied.**  
**Unit-source expansion:** **stop.**  
**Next:** scenario + composition analysis (`reconstruction-scenarios.md`); later claim inventory updates only when workflow Phase 1 explicitly runs aggregate claim revision.

**Not modified by this audit:** existing unit reviews or their scores; claim inventory statuses; comparison matrix; evaluation dataset; BibTeX.
