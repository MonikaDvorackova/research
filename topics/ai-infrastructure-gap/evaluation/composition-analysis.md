---
id: eval-ai-infrastructure-gap-composition-analysis-2026-07-29
title: "Composition analysis: reconstructing historical AI-assisted decisions"
topic: ai-infrastructure-gap
type: evaluation
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, composition, reconstruction, bindings, synthesis]
checklist_version: "0.1.0"
related_claims: [C1, C2, C3, C4, C5, C6, C7, C8]
depends_on:
  - architecture/reconstruction-checklist.md
  - evaluation/coverage-audit.md
  - evaluation/reconstruction-scenarios.md
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

## Composition analysis: reconstructing historical AI-assisted decisions

**Purpose.** Synthesize the completed unit-review corpus, coverage audit, and reconstruction scenarios into a **compositional** argument: what happens when independently adequate infrastructure components must jointly support **faithful reconstruction** of one historically situated AI-assisted decision (checklist v0.1.0 §3).

**Method.** Unit reviews are treated as evidence of *component capability*. Composition requires checklist §7 **same-identity binding** and **decision-time binding**. Two components that each pass native success criteria are **not** jointly sufficient unless their outputs are stably and durably bound to the same decision episode.

**Not this document.** New source reviews; claim-status promotion; comparison-matrix or dataset updates; product design; literature expansion.

---

## 1. Composition model

### 1.1 Minimal components of one historical decision episode

Reconstructing one legally or operationally consequential AI-assisted decision involves, at minimum, the following **independent** infrastructure concerns. They are listed as components because, in the reviewed ecosystem, they are typically owned by different standards, products, teams, or retention regimes:

| Component | Role in the episode |
|---|---|
| **Decision identity** | Unambiguous key for the episode (checklist IC-01) |
| **Subject identity** | Who the decision concerns |
| **Human actor** | Who participated in producing or accepting the outcome (IC-04) |
| **Actor authority** | Under what mandate/role the actor was permitted to decide (IC-05) |
| **AI inference** | Model participation that materially affected the outcome |
| **Model version** | Which model artifact participated (IC-13) |
| **Dataset / feature lineage** | Training/reference/feature heritage relevant to interpretation (IC-23/IC-24; inputs IC-10) |
| **Policy evaluation** | Permit/deny or structured policy result |
| **Policy version** | Governing policy as applicable at decision time (IC-06/IC-07) |
| **Evidence snapshot** | Inputs available and, critically, relied upon (IC-10/IC-11) |
| **Explanation** | Human-facing account of model or process behaviour |
| **Human review** | Structured human-gate work (claim, complete, fail, etc.) |
| **Override** | Human disregard, reverse, or replacement of system output |
| **Timestamps** | When the decision (and related acts) occurred (IC-03; IC-19 as conditioned) |
| **Provenance** | Derivation relations among entities/activities/agents |
| **Audit records** | Event logs retained for monitoring, compliance, or investigation |
| **Notification** | Notice to affected persons that an AI-assisted decision occurred |
| **Appeal** | Contest / explanation-request / complaint pathway |
| **Remediation** | Later correction, withdrawal, or compensatory action |

### 1.2 Independence and the binding requirement

These components are **not** facets of a single normative information model in the reviewed corpus. Provenance graphs, traces, model cards, policy engines, human-task processors, risk-management frameworks, explainability principles, and legal logging duties each optimize for a different native goal (derivation, execution path, release documentation, authorization eval, workflow, organizational risk, explanation quality, operational monitoring).

**Faithful reconstruction** (checklist §3.1) requires that a later reconstructor can identify the episode and restate authorization, justification, and validity **as of decision time**. That is possible only if the components above are linked by **durable bindings**: explicit associations to the same decision identity and to decision-time version axes—not by informal correlation of timestamps, usernames, or “the latest” artifacts (checklist §3.3, §7).

Runtime execution can succeed with ephemeral correlation. Historical reconstruction cannot.

---

## 2. Component capability

For each component: contribution, supporting unit evidence, what is not preserved, and interaction dependence. Unit reviews are cited as evidence, not restated.

### Decision identity

- **Contributes:** Anchor for all other bindings (IC-01).
- **Supported by:** OPA decision-log identifiers (island); WS-HumanTask task identifiers (island); EU AI Act use-period recording for Annex III 1(a) biometric subclass (narrow). Coverage audit: **partial**.
- **Does not preserve:** A cross-system, business-level decision episode key spanning inference, policy, human gate, notice, and appeal.
- **Depends on:** Nothing—but every other component depends on *it* for composition.

### Subject identity

- **Contributes:** Links the episode to the affected person or entity.
- **Supported by:** Application payloads in OPA/HumanTask/OTel (external assumption); not first-class in Model Cards, Datasheets, PROV-as-SUT, or NISTIR 8312.
- **Does not preserve:** Stable subject keys under privacy minimization, nor binding of subject to technical logs after deletion (Scenario 6).
- **Depends on:** Decision identity; evidence snapshot; notification/appeal case files.

### Human actor

- **Contributes:** Who acted (IC-04).
- **Supported by:** WS-HumanTask actual owner / CreatedBy / roles (**strong**); EU AI Act biometric verifier identity (subclass); OPA/Cedar principals in eval context; PROV agents; AI RMF role documentation (organizational, not episode).
- **Does not preserve:** Legal identity proof; continuity when accounts are recycled.
- **Depends on:** Actor authority; human review / override records; decision identity.

### Actor authority

- **Contributes:** Permission to decide (IC-05), distinct from “who clicked complete.”
- **Supported by:** WS-HumanTask role/state authorization for *task operations*; Cedar/OPA authorization evaluation; AI Act oversight “authority” expectations; AI RMF accountability roles.
- **Does not preserve:** External mandate/delegation artifacts bound to the episode; separation of task-role authority from legal authority.
- **Depends on:** Policy evaluation + policy version; human actor; decision time.

### AI inference

- **Contributes:** Model output that participated in the decision.
- **Supported by:** Application-level events (OTel spans/logs); HumanTask input payloads; MLMD executions (pipeline-centric more than decision-centric).
- **Does not preserve:** Normative status of the output (recommendation vs binding); reliance weighting.
- **Depends on:** Model version; evidence snapshot; decision identity.

### Model version

- **Contributes:** Which model participated (IC-13).
- **Supported by:** Model Cards (version/date fields); MLMD artifacts; System Cards “current version” (weak); OpenLineage/PROV can reference model entities if modeled.
- **Does not preserve:** Binding of card/artifact version to a specific decision at IC-03.
- **Depends on:** Inference event; dataset/feature lineage; decision identity.

### Dataset / feature lineage

- **Contributes:** Heritage of training/reference/feature data (IC-23/IC-24; context for IC-10).
- **Supported by:** OpenLineage; MLMD; Datasheets; PROV; Annex IV-style system docs (EU AI Act technical documentation—system level).
- **Does not preserve:** Point-in-time inference feature vectors as decision evidence; reliance subset (IC-11).
- **Depends on:** Evidence snapshot; model version; decision identity.

### Policy evaluation

- **Contributes:** Structured authorization/policy result.
- **Supported by:** OPA evaluation + decision logs; Cedar PARC evaluation (diagnostics not durable by language alone).
- **Does not preserve:** Full justification of AI-mediated eligibility; human override semantics.
- **Depends on:** Policy version; actor/subject attributes; decision identity; often inference outputs as policy input.

### Policy version

- **Contributes:** Then-applicable governing rules (IC-06/IC-07).
- **Supported by:** OPA bundle revision in decision logs (strongest unit island); Cedar policies without mandated versioned decision log; AI RMF organizational policy documentation (not episode-bound).
- **Does not preserve:** Cross-store effective-date intervals tied to business decisions; presence in AI Act general event logs.
- **Depends on:** Policy evaluation; timestamps; decision identity.

### Evidence snapshot

- **Contributes:** What was available and relied upon (IC-10/IC-11).
- **Supported by:** Partial—OPA input documents; HumanTask input/attachments (attachments optional); EU AI Act biometric match inputs (subclass); OTel/payload logs (unspecified schema).
- **Does not preserve:** Systematic reliance distinction; excluded evidence (IC-12); survival under personal-data deletion.
- **Depends on:** Decision identity; retention regime; subject identity constraints.

### Explanation

- **Contributes:** Recipient-facing account of behaviour or process.
- **Supported by:** NISTIR 8312 principles (Explanation, Meaningful, Explanation Accuracy, Knowledge Limits); EU AI Act Art. 86 explanation *right*; Model Cards optional interpretability notes; AI RMF explainability characteristic.
- **Does not preserve:** Durable decision-time justification under authorization/validity constraints; retention; policy-version binding (C7-relevant unit evidence).
- **Depends on:** Inference; evidence; decision identity—bindings not defined by 8312.

### Human review

- **Contributes:** Lifecycle of human-gate work.
- **Supported by:** WS-HumanTask (states, claim/complete/fail, history API); AI Act Art. 14 oversight design; AI RMF human-oversight process outcomes.
- **Does not preserve:** Mandated retention; mandatory rationale; legal authority objects.
- **Depends on:** Decision identity; inference payload as task input; actor authority.

### Override

- **Contributes:** Record that humans disregarded or reversed system output.
- **Supported by:** Art. 14 *capability* to disregard/override/reverse; WS-HumanTask *can* encode divergent complete/fail outputs—application semantics, not a named override type; AI RMF appeal/override monitoring language (organizational).
- **Does not preserve:** Mandatory override audit fields for general high-risk systems (EU AI Act review).
- **Depends on:** Human review; original inference; reasons; decision identity.

### Timestamps

- **Contributes:** Temporal location of acts (IC-03; supports IC-19).
- **Supported by:** OTel; OPA logs; OpenLineage; MLMD; HumanTask Created/Activation/Complete-by times; AI Act biometric use intervals.
- **Does not preserve:** Clock-domain agreement across systems; as-of binding of reference data.
- **Depends on:** Decision identity (else timestamps only enable probabilistic correlation—Scenario 5).

### Provenance

- **Contributes:** Derivation structure (entities, activities, agents).
- **Supported by:** PROV-DM; MLMD; OpenLineage; partial Annex IV / training-data provenance notes.
- **Does not preserve:** Justification criteria, governing policy version, or decision episode schema (C5 unit evidence).
- **Depends on:** Decision identity to become decision-bound rather than pipeline-bound.

### Audit records

- **Contributes:** Retained events for monitoring/compliance/investigation.
- **Supported by:** EU AI Act Arts. 12/19/26 (≥6 months when under control); OPA decision logs; OTel logs/traces; HumanTask history (API, no retention floor).
- **Does not preserve:** Semantic completeness of decision episodes; integrity/tamper-evidence (generally absent).
- **Depends on:** Decision identity; aligned retention across stores.

### Notification

- **Contributes:** Informing affected persons of AI use / decision.
- **Supported by:** EU AI Act Art. 26(11) (inform persons subject to Annex III decision assistance); HumanTask notifications (deadline/informational, not legal notice).
- **Does not preserve:** Notice content bound to decision ID and evidence package.
- **Depends on:** Decision identity; subject identity; appeal pathway.

### Appeal

- **Contributes:** Contestability / explanation-request pathway.
- **Supported by:** Art. 86 right to explanation; AI RMF / Art. 27 complaint-mechanism *arrangements*; not a retained appeal-record schema in unit SUTs. Coverage: **partial** contestability.
- **Does not preserve:** Appeal case ↔ technical episode linkage.
- **Depends on:** Notification; decision identity; evidence/explanation retention.

### Remediation

- **Contributes:** Later correction or system-level corrective action.
- **Supported by:** EU AI Act Art. 20 (system non-conformity corrective actions); AI RMF incident/change processes—not per-decision remediation records.
- **Does not preserve:** Correction history bound to the original episode.
- **Depends on:** Decision identity; outcome linkage.

---

## 3. Binding analysis

Bindings required for faithful reconstruction under checklist §7. “Preserved by reviewed standards” means a **cross-component, durable, normative** binding—not an in-island identifier.

| Binding | Required? | Standardized across families? | Durable? | Reconstructable years later? | Commonly implemented (as shared contract)? | Preserved by reviewed standards as cross-system contract? |
|---|---|---|---|---|---|---|
| Decision ↔ inference | Yes | No | Only if retention aligned | Only if snapshotted + bound | Ad hoc correlation IDs | **No** |
| Decision ↔ policy evaluation | Yes (policy-governed) | Partial within OPA | If decision logs retained | If logs + bundle revision kept | Often in authz stacks; rarely linked to AI decision SOR | **No** (OPA island only) |
| Decision ↔ evidence snapshot | Yes | No | Often weakened by live stores / deletion | Unreliable | Feature stores overwrite | **No** |
| Decision ↔ model version | Yes (model-participating) | No | Docs ≠ runtime binding | Weak without inference pin | Model registry + serving tags vary | **No** |
| Decision ↔ dataset version | Conditionally | No | Lineage ≠ inference features | Weak | Pipeline lineage common; decision link rare | **No** |
| Decision ↔ human review | Yes (human-gated) | No (task ID ≠ decision ID) | HumanTask has no retention floor | Unreliable | Workflow engines common; binding custom | **No** |
| Decision ↔ actor authority | Yes when authorization in scope | No | Role logs ≠ mandate artifacts | Weak | IAM + workflow rarely joined to policy version | **No** |
| Decision ↔ explanation | Conditionally (transparency/contestability) | No | 8312 does not require retention | Often regenerated post hoc | XAI at decision time common; archive rare | **No** |
| Decision ↔ notification | Conditionally | No | Notice systems separate | Weak | CRM/case tools | **No** |
| Decision ↔ appeal | Conditionally | No | Rights ≠ records | Weak | Case management separate | **No** |
| Decision ↔ remediation | Conditionally | No | System corrective ≠ episode correction | Weak | Incident tools | **No** |
| Decision ↔ later correction | Conditionally | No | Seldom first-class | Weak | Manual process | **No** |

**Result.** The corpus shows **local** identifiers (OPA decision id; HumanTask task id; biometric use interval) but **no** reviewed standard defines the full set of cross-system bindings as a durable composition contract.

---

## 4. Temporal composition

Historical reconstruction is harder than runtime execution because components **evolve on different clocks**:

| Drift class | Effect if unbound to decision time | Unit / scenario evidence |
|---|---|---|
| Policy changes | Current Rego/Cedar/org policy silently substitutes for historical authorization | Scenario 2; OPA bundle revision helps *only* inside retained decision logs |
| Model replacement | New scores/explanations displace historical model behaviour | Scenario 4; Model Cards document versions but do not bind them to episodes |
| Dataset / feature evolution | Live features ≠ decision-time evidence | Scenario 4; OpenLineage/MLMD track pipelines, not decision snapshots |
| Authorization / role changes | Actor still employed under new entitlements | HumanTask/IAM roles change; authority at IC-03 lost |
| Personnel turnover | Institutional memory replaces records | Checklist §3.3 |
| Deleted evidence | Justification collapses despite remaining logs | Scenario 6; AI Act defers to personal-data law |
| Expired credentials / keys | Integrity and access paths break | Integrity elevated/optional; not solved by content logs |
| Changing explanations | Post-hoc XAI ≠ decision-time account | NISTIR 8312; checklist §4 explainability row; C7 |
| Changing legal rules | Validity frame shifts | Art. 86/FRIA are rights/process, not bi-temporal validity stores |

**Isolated artifacts are insufficient** because each store answers its native question at *query time* using *its* retention and *its* identity scheme. Without decision-time binding, a reconstructor inevitably mixes historical fragments with current components—the failure mode checklist §3.1 item 7 and §3.3 forbid.

---

## 5. Base triad composition

### 5.1 Authorization

**Contributing components:** actor; actor authority; policy evaluation; policy version; timestamps; (sometimes) human review completion as the authorizing act.

**Required bindings:** decision ↔ policy evaluation ↔ policy version ↔ actor authority ↔ time; if human-gated, decision ↔ human review ↔ actor.

**Why the ecosystem cannot guarantee reconstruction:** OPA can retain allow/deny with bundle revision, but eligibility decisions also depend on AI inference and human acceptance. Cedar evaluates without mandating durable logs. HumanTask records who completed a task, not the legal mandate. AI Act requires oversight competence/authority as a design duty, not an authority artifact bound to each decision. Across Scenarios 1–3 and 5, authorization either remains an **island** or fails identity binding.

**Compositional result:** **FAIL** for full-episode authorization; **PARTIAL** only for narrow policy-log islands.

### 5.2 Justification

**Contributing components:** evidence snapshot (available + relied upon); inference output; explanation; human reasons; applicable criteria; model/dataset context as background.

**Required bindings:** decision ↔ evidence snapshot (IC-10/IC-11); decision ↔ inference; decision ↔ explanation/human rationale; criteria/policy linkage where criteria are rule-encoded.

**Why the ecosystem cannot guarantee reconstruction:** IC-11 reliance is weakly supported corpus-wide. NISTIR 8312 improves explanation *quality* without retention or decision binding. Art. 86 creates a right to obtain explanations, not a retained justification package. HumanTask comments/attachments are optional. Provenance/lineage explain derivation, not relied-upon decision evidence (C5). Scenario 3 (outcome-only) and Scenario 6 (deleted inputs) are decisive.

**Compositional result:** **FAIL**.

### 5.3 Validity

**Contributing components:** policy version; constraints; temporal context; legal/regulatory frame; conformity of outcome to then-applicable rules.

**Required bindings:** decision ↔ policy version ↔ effective interval; decision ↔ evidence/constraints then in force; distinction from current rules (Scenario 2, 4).

**Why the ecosystem cannot guarantee reconstruction:** Validity is historically indexed. Without IC-07/IC-19-style binding, reviewers assess today’s policy against fragments of yesterday’s evidence. AI Act logs support monitoring/traceability of *functioning*, not validity reconstruction under then-applicable criteria. AI RMF temporal Profiles describe organizational risk posture, not decision as-of axes.

**Compositional result:** **FAIL**.

### 5.4 Faithful reconstruction (base)

Under checklist §8.3, base faithful reconstruction requires all three triad rows to PASS for the declared profile. **Compositional result across the scenario set: FAIL.** This is not a claim that reconstruction is metaphysically impossible everywhere; it is the finding that the **reviewed** composition of standards and frameworks does not define a sufficiently complete, durable, cross-system decision composition model for **deterministic** faithful reconstruction without custom integration beyond those sources.

---

## 6. Failure modes

Grouped by **architectural cause**, using scenarios as illustrations (not per-SUT score repetition).

### 6.1 Identity fragmentation

- Missing shared decision identity (Scenario 5).
- Incompatible identifiers (OPA decision id ≠ HumanTask task id ≠ business case id ≠ trace id).
- Ambiguous correlation via time/user (checklist §3.3).

### 6.2 Version unbound from episode

- Missing policy version at decision time outside policy-log islands (Scenario 2).
- Model/dataset updates without inference snapshot binding (Scenario 4).
- “Current” System Card / dashboard substitution.

### 6.3 Authority and human-gate gaps

- Missing authority evidence distinct from login/role (Scenarios 1, 3).
- Human review without preserved rationale (Scenario 3).
- Override capability without override record (EU AI Act Art. 14 vs recordkeeping).

### 6.4 Semantic thinness of logs

- Logs without semantic linkage to justification/authorization/validity (AI Act purpose-based events; OTel paths).
- Retention without compositional integrity (uneven TTLs; six-month floors vs multi-year appeals).

### 6.5 Explanation detached from decision

- Explanation principles/rights without durable decision-time package (NISTIR 8312; Art. 86; Scenarios 1, 6).
- Post-hoc regeneration after model drift.

### 6.6 Provenance without decision context

- Rich lineage/PROV graphs that never mention the eligibility decision (Scenario 4; C5).

### 6.7 Contestability without record composition

- Notification/appeal/remediation processes that do not key technical episode artifacts (Scenario 6).

---

## 7. Architectural synthesis

Existing AI governance infrastructure consists of numerous individually valuable components: provenance and lineage models; observability; ML metadata; policy engines and authorization languages; model/dataset/system documentation; AI risk-management frameworks; explainability principles; legally mandated operational logging; and human-task workflow records. The unit-review corpus establishes that these families are real and often mature for their native purposes (coverage audit: strong coverage across those families).

The principal limitation identified by composition analysis is **not** the absence of logging, provenance, explainability, documentation, or human oversight **individually**.

The principal limitation is the **absence of a durable cross-system composition model** capable of preserving one **decision episode**—identity, decision-time versions, evidence reliance, authorization result, human action, and later contestation/correction—across heterogeneous technical and organizational boundaries.

That statement is supported by: checklist §7 binding criteria; repeated unit-level triad FAIL with complementary strengths; coverage audit’s shift from missing families to compositional residuals; and Scenarios 1–6, which fail deterministically when bindings are absent even when multiple strong components are notionally “present.”

---

## 8. Relationship to claims

Claim files are **not** modified. Support type refers to this composition analysis relative to existing hypotheses.

| Claim | How composition analysis relates | Support type |
|---|---|---|
| **C1** | Artifact classes can be present yet triad fails without bindings; Scenario 5 is the pure form | **Direct** + **scenario-based** |
| **C2** | Authorization islands (OPA) separable from justification (evidence/reasons) and validity (historical policy); Scenarios 2–3 | **Direct** + **scenario-based** |
| **C3** | Temporal composition section; Scenarios 2, 4, 6 | **Direct** + **scenario-based** |
| **C4** | OTel contributes paths/timestamps, not normative basis; needs bindings it does not define | **Indirect** (unit) + **compositional** |
| **C5** | Provenance/lineage without decision context failure mode | **Indirect** (unit) + **compositional** |
| **C6** | Policy logs necessary-island but insufficient for AI+human episodes; Scenarios 1–3 | **Direct** + **scenario-based** |
| **C7** | Explanation components detach from durable justification; Scenarios 1, 6 | **Direct** (with NISTIR 8312 unit) + **scenario-based** |
| **C8** | Residual gap is binding/profile-shaped; analysis does **not** yet choose layer vs composition profile, but frames the residual as composition failure rather than missing peer families | **Indirect** / framing for later falsification |

---

## 9. Threats to validity

| Threat | Discussion |
|---|---|
| **Dependence on available standards** | The corpus is strong on published primary sources selected for family coverage; unpublished org schemas might bind better. That would be a **composition profile** success (relevant to C8), not evidence that the reviewed standards already define the bindings. |
| **Implementation variability** | Engines may log more than specs require. Unit methodology forbids scoring implementation generosity; composition likewise refuses credit for non-normative practice. |
| **Optional specification features** | HumanTask attachments/comments (`MAY`), Cedar without log sink, OTEL attributes as open bags—optionality widens capability *ceilings* but not guaranteed reconstruction. |
| **Sector-specific sources** | AI Act biometric minimum fields and Art. 26(10) patterns are narrow; generalizing them would overstate decision-record completeness (coverage audit discipline). |
| **Evolving regulation / standards** | Future harmonised standards or profiles could add bindings; the finding is about the **reviewed** ecosystem at pin dates, not perpetual impossibility. |
| **Absence of empirical deployment measurements** | Scenarios are adversarial analytical tests, not field epidemiology. They show structural failure modes consistent with unit boundaries; they do not estimate frequency in industry. |

These limitations constrain **scope and strength**, not the internal compositional claim: where bindings are undefined and retention unaligned, deterministic faithful reconstruction is not guaranteed by the reviewed sources.

---

## 10. Conclusions

**Individual capability.** The reviewed ecosystem provides substantial native capabilities: derivation (PROV/MLMD/OpenLineage), execution observability (OTel), authorization evaluation and logging (OPA/Cedar), release documentation (Model Cards/Datasheets/System Cards), organizational risk governance (AI RMF), explanation quality principles (NISTIR 8312), retention-backed operational logging (EU AI Act), and human-task lifecycle records (WS-HumanTask).

**System composition.** Those capabilities remain **loosely coupled**. Local identities and version pins exist inside islands; cross-system decision-episode bindings, aligned retention, reliance accounting, and contestation linkage are not specified as a shared durable model.

**Faithful reconstruction.** Under checklist v0.1.0 base triad rules, compositional evaluation of the scenario set yields **FAIL** for authorization, justification, and validity as a joint result. The appropriate statement is not universal impossibility; it is that **the reviewed ecosystem does not presently define a sufficiently complete, durable, cross-system decision composition model for deterministic faithful reconstruction** of historical AI-assisted decisions without custom integration beyond the reviewed sources.

**Next analytical step (not performed here):** design and score explicit composition profiles (C8) against the same scenarios—still without expanding the unit-SUT corpus unless a blocking family gap reappears.

**Not modified:** unit reviews; claim inventory statuses; comparison matrix; evaluation dataset; BibTeX; coverage audit; reconstruction scenarios (referenced, not overwritten).
