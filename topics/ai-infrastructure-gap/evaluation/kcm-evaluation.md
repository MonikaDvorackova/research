---
id: eval-ai-infrastructure-gap-kcm-evaluation-2026-07-29
title: "Evaluation: Knowledge Continuity Model against reconstruction checklist"
topic: ai-infrastructure-gap
type: evaluation
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, knowledge-continuity, reconstruction, checklist, scenarios]
checklist_version: "0.1.0"
sut: "Knowledge Continuity Model (architecture/knowledge-continuity-model.md)"
sut_kind: proposed-architecture
depends_on:
  - architecture/reconstruction-checklist.md
  - architecture/knowledge-continuity-model.md
  - evaluation/reconstruction-scenarios.md
  - evaluation/composition-analysis.md
  - evaluation/methodology/review-methodology.md
related_claims: [C1, C2, C3, C8]
---

# Evaluation: Knowledge Continuity Model

**Document role.** Unit-style evaluation of the proposed Knowledge Continuity Model (KCM) against reconstruction checklist v0.1.0, using the same scoring methodology applied to existing sources. This is **not** a literature review, **not** a new architectural proposal, and **not** a claim-status promotion.

**SUT.** Knowledge Continuity Model as specified in `architecture/knowledge-continuity-model.md` (conceptual objects, bindings, temporal model, reconstruction procedure). Scored as **model expressiveness and normative information requirements**—the same stance used for standards such as PROV-DM (expressiveness of retained structure if the model is followed), not as a measured production deployment.

**Composition context.** Prior composition analysis found that the reviewed ecosystem **FAIL**s base-triad reconstruction without durable cross-system bindings. This evaluation asks whether KCM’s Decision Episode objects and bindings close that compositional gap **when populated as the model requires**.

---

## 1. Evaluation method

### 1.1 Same checklist and scoring rules

This evaluation applies:

| Artifact | Role |
|---|---|
| [reconstruction-checklist.md](../architecture/reconstruction-checklist.md) v0.1.0 | Normative information categories (IC-01–IC-24), binding criteria (§7), triad roll-up (§8.3), faithful-reconstruction definition (§3) |
| [review-methodology.md](methodology/review-methodology.md) | Evidence discipline: scores require explicit support in the SUT; no credit for unstated practice |
| Unit-review mark set | Checklist marks: `PASS` \| `PARTIAL` \| `FAIL` \| `N/A` (PARTIAL requires stated missing element). Triad: `PASS` only if §8.3 conditions hold |
| Methodology 0–3 scale | Applied once to the six high-level reconstruction-capability rows for consistency with unit reviews |

**No new scoring rules** are introduced. Completeness profile for triad and scenarios: **base triad**, unless a row states an elevated/conditional class.

### 1.2 What is credited

| Credited | Not credited |
|---|---|
| Information categories and bindings that KCM **defines as persistent objects or mandatory associations** | Hypothetical extra fields an implementer might add |
| Reconstruction procedure fail-closed behaviour (§8 of KCM) | Organizational willingness to adopt |
| Conditional objects when the model states R-cond / profile elevation | Bit-exact model replay (checklist §3.2 explicitly excludes this from faithfulness) |
| Scenario outcomes **under conformant population** of mandatory objects | Non-conformant “outcome-only” deployments (those FAIL the model, as KCM §9 Scenario 3 already states) |

### 1.3 Evaluation unit framing

KCM is evaluated as a **proposed composition architecture** derived from prior evaluation, not as a peer bibliographic standard. Where scores differ from reviewed ecosystem sources, the difference is attributed to KCM’s first-class Decision Episode, reliance distinction, policy-version binding, and human-act/rationale objects—not to implementation technology.

---

## 2. Checklist evaluation

### 2.1 High-level reconstruction capabilities (methodology 0–3)

| Criterion | Score | Evidence from KCM |
|---|---:|---|
| System state | 2 | Decision + Evidence Snapshot + versioned Model/Dataset/Pipeline refs capture decision-time state relevant to the episode; not a general system-state store. |
| Decision process | 3 | Formation → commitment → disclosure → contest → correction lifecycle; Human Review / Override; reconstruction algorithm steps 1–10. |
| Evidence | 3 | Evidence Snapshot with `availableEvidenceRefs` and `reliedUponRefs` (IC-10/IC-11); optional excluded set. |
| Rules | 3 | Policy + Policy Version with validity intervals; evaluation result / path digest bound to Decision. |
| Human context | 3 | Human Actor, Authority, Human Review, Override with required rationale when humans affect outcome; Notification / Appeal / Remediation for continuity. |
| Temporal continuity | 3 | Decision/effective/inference/review/notification/appeal/remediation/reconstruction time axes; validity intervals; append-only correction history; explicit ban on latest-only substitution. |

### 2.2 Category scores (checklist §8.2)

Profile: **base triad**. Marks reflect whether KCM **systematically** supplies the category as bound Decision Episode structure.

| ID | Category | Class | Score | Supporting architectural elements | Remaining assumptions | Why different from typical unit SUTs |
|---|---|---|---|---|---|---|
| IC-01 | Decision identity | Required | **PASS** | Immutable `decisionId`; join key for all bindings (§3.4, §5) | ID minted and propagated to emitters | Ecosystem: islands (OPA/HT) only; Scenario 5 FAIL |
| IC-02 | Decision outcome | Required | **PASS** | `Decision.outcome` required (§4.1) | Outcome recorded at commitment | Many logs omit first-class outcome |
| IC-03 | Decision time | Required | **PASS** | `decisionTime` + `clockDomain` (§4.1, §6.1) | Clock domain declared | Often optional timestamps only |
| IC-04 | Actor(s) | Req/Cond | **PASS** | Human Actor; system principals; review/override actor refs (§4.3, §4.14–4.15) | Actor ids stable for retention horizon | HT strong for task actors; not episode-bound by default |
| IC-05 | Authority | Cond | **PASS** | Authority object with `validFrom`/`validTo`; Review/Override ↔ Authority (§4.5, §5) | Org maintains authority registry resolvable at reconstruction | HT roles ≠ mandate; AI Act oversight duty ≠ artifact |
| IC-06 | Governing policy | Cond/Req | **PASS** | Policy + Decision ↔ Policy Version (§4.11–4.12, §5) | Decision is policy-governed (programme default) | PROV/OTel/XAI: FAIL; OPA: island only |
| IC-07 | Policy version | Req w/ IC-06 | **PASS** | Immutable Policy Version; validity interval; sealed binding (§4.12, §6.2, §6.4) | Version content remains retrievable by id/hash | Scenario 2 ecosystem FAIL outside OPA log island |
| IC-08 | Applicable rules | Cond | **PASS** | Evaluation result / `applicableRulePath` or path digest bound to Decision (§4.12, §5 additional bindings) | Multi-rule policies record path/digest at commitment | OPA can log path inside engine; not cross-episode |
| IC-09 | Constraints | Cond | **PARTIAL** | Treated as content of Policy Version / evaluation; optional elevated constraint objects (§7.3) | Constraints encoded in retained policy/eval artifacts | Missing element: no mandatory first-class Constraint object separate from policy |
| IC-10 | Evidence used | Req if evidence-using | **PASS** | Evidence Snapshot `availableEvidenceRefs` (§4.10) | Snapshot captured before live-store mutation | Lineage/PROV: usage without decision snapshot duty |
| IC-11 | Evidence relied upon | Req/Req | **PASS** | `reliedUponRefs` or weighting record (§4.10); binding criterion separation of reliance | Reliance recorded at commitment (not inferred later) | Corpus-wide weak/FAIL; primary compositional gap closed |
| IC-12 | Excluded evidence | Cond | **PARTIAL** | Optional `excludedRefs` + reasons; R-cond; listed as optional extension (§4.10, §11.3) | Profile elevates when exclusion occurred | Supported when used; not mandatory for base triad |
| IC-13 | Model version | Cond | **PASS** | Model Version immutable id/hash; Inference → Model Version (§4.7–4.8, §5) | Artifact remains resolvable | Model Cards document versions; unbound to episodes |
| IC-14 | Prompts | Cond | **PARTIAL** | Expressible as Evidence Snapshot / Inference payload content; no dedicated Prompt object | Prompts material to outcome are snapshotted as evidence | Missing element: first-class prompt/template version object |
| IC-15 | Tools | Cond | **PARTIAL** | Tool results may appear in Evidence Snapshot / Inference; no dedicated Tools object | Tool invocations retained in snapshot when material | Missing element: first-class tool version/args object |
| IC-16 | External services | Cond | **PARTIAL** | External responses via Evidence Snapshot as-of capture; no dedicated External Service object | Service identity/version included in snapshot refs | Missing element: first-class external-service version object |
| IC-17 | Confidence | Cond | **PASS** | `AI Inference.confidence` when used as gate (§4.6) | Gate thresholds recorded when outcome-affecting | Often attributes-only in other SUTs |
| IC-18 | Assumptions | Cond | **PARTIAL** | May appear in rationales, policy text, or snapshot metadata; no Assumptions object (§4) | Material assumptions written into retained fields | Missing element: systematic assumptions structure (IC-18) |
| IC-19 | Temporal context | Cond | **PASS** | Multi-axis temporal model; validity intervals; evidence `capturedAt` (§6) | Effective time declared when distinct from decisionTime | Ecosystem temporal islands; latest-only failure |
| IC-20 | Legal context | Cond | **PARTIAL** | Organization / Authority types may carry mandate frame; no Legal Context object (§4.4–4.5) | Jurisdiction/regime identifiers recorded when multi-jurisdiction | Missing element: first-class legal/jurisdictional frame object |
| IC-21 | Integrity information | Opt/Cond | **PARTIAL** | Audit Record digests; R-rec base, R-mand integrity-elevated (§4.19, §11.2) | Elevated profile demands integrity | Optional for base faithfulness (§5 checklist); elevated needs adoption |
| IC-22 | Signatures | Opt/Cond | **PARTIAL** | Optional extension (crypto/signatures) (§11.3); not first-class | Non-repudiation profile supplies signatures | Same optional stance as checklist default |
| IC-23 | Provenance | Cond | **PASS** | Decision-bound derivation via Inference/Evidence/Model/Dataset/Pipeline bindings (§5); complements external PROV (§10) | Version refs resolve; richer graphs optional | Unlike PROV alone: provenance is *decision-bound* |
| IC-24 | Lineage | Opt/Cond | **PASS** | Dataset Version + Feature Pipeline Version bound when derived features/heritage in scope (§4.8–4.9, §5) | Heritage disputes use retained version ids | OpenLineage/MLMD strong for pipelines; unbound to decisions without KCM |

### 2.3 Checklist outcome summary

| Roll-up | Result |
|---|---|
| Required identity/outcome/time (IC-01–03) | **PASS** |
| Authorization-critical (IC-04–08 as applicable) | **PASS** (IC-09 constraints **PARTIAL** when constraints are not encoded in policy/eval) |
| Justification-critical (IC-10–11) | **PASS**; IC-12 **PARTIAL** unless elevated |
| Model participation (IC-13, IC-17) | **PASS** |
| Conditionally thin rows (IC-14–16, IC-18, IC-20) | **PARTIAL** — expressible via snapshot/policy/authority but not first-class |
| Integrity elevated (IC-21–22) | **PARTIAL** / optional — does not fail base triad |
| Decision-bound provenance/lineage (IC-23–24) | **PASS** when conditioned |
| **Faithful reconstruction (base)** | **PASS** under conformant mandatory population (§3 below) |

---

## 3. Base triad

Scoring uses checklist §8.3. “Satisfies” means: under KCM’s own mandatory objects/bindings and stated assumptions, a competent reconstructor can restate the target **as of decision time** without undocumented heuristics or latest-only substitution.

### 3.1 Authorization

| Aspect | Assessment |
|---|---|
| **Required persistent objects** | Decision; Human Actor and/or system principal; Authority; Policy Version; policy evaluation result; Human Review and/or Override when humans affect outcome |
| **Required bindings** | Decision ↔ Authority; Decision ↔ Policy Version; Decision ↔ evaluation result; Decision ↔ Human Review/Override; Review/Override ↔ Authority |
| **Temporal requirements** | Authority `validFrom`–`validTo` contains act time; Policy Version interval contains decision/effective time; act times recorded |
| **Conformance requirements (conceptual)** | Mandatory authorization objects populated; no rewrite of sealed version bindings; fail closed if missing |
| **Remaining limitations** | Quality/correctness of authority registry; recycled actor ids; legal mandate depth beyond Authority attributes |
| **Satisfies criterion?** | **Yes — PASS** for base authorization when mandatory bindings present |

### 3.2 Justification

| Aspect | Assessment |
|---|---|
| **Required persistent objects** | Decision; Evidence Snapshot (available + relied-upon); AI Inference when AI participates; Model Version; Human Review/Override rationales when humans affect outcome; optional Explanation (account only, not sole basis) |
| **Required bindings** | Decision ↔ Evidence Snapshot; Decision ↔ AI Inference; Inference ↔ Model Version / Evidence; Decision ↔ Human Review/Override |
| **Temporal requirements** | Snapshot `capturedAt` as decision-time evidence as-of; inference time retained; post-hoc explanations marked non-historical |
| **Conformance requirements (conceptual)** | Reliance distinction retained; unbound post-hoc explanation insufficient |
| **Remaining limitations** | Opaque models may leave IC-11 coarse; prompt/tool/external-service detail PARTIAL; deleted raw evidence under law (Scenario 6) |
| **Satisfies criterion?** | **Yes — PASS** for base justification when Evidence Snapshot + inference/human rationales retained |

### 3.3 Validity

| Aspect | Assessment |
|---|---|
| **Required persistent objects** | Decision (outcome); Policy Version; evaluation/conformity representation; constraints as policy/eval content; Remediation chain for later handling (does not rewrite original validity) |
| **Required bindings** | Decision ↔ Policy Version; evaluation result bound; temporal interval coverage verified at reconstruction |
| **Temporal requirements** | Historical policy only; current policy MUST NOT substitute (KCM §6.4) |
| **Conformance requirements (conceptual)** | Interval coverage check; outcome vs recorded evaluation; separate remediation from original validity |
| **Remaining limitations** | IC-09 not first-class; IC-20 legal frame PARTIAL; does not assess substantive fairness/correctness (KCM §12) |
| **Satisfies criterion?** | **Yes — PASS** for base validity when historical Policy Version + evaluation retained and interval-checked |

### 3.4 Faithful reconstruction (base)

| Target | Score |
|---|---|
| Authorization reconstructable | **PASS** |
| Justification reconstructable | **PASS** |
| Validity reconstructable | **PASS** |
| **Faithful reconstruction (base)** | **PASS** (under stated assumptions in §6) |
| Faithful reconstruction (elevated integrity) | **PARTIAL** until IC-21/IC-22 profile objects populated |

**Contrast with composition analysis:** reviewed ecosystem compositional triad = **FAIL**. Difference is KCM’s durable Decision Episode bindings, not superior native logging technology.

---

## 4. Scenario evaluation

Scenarios are those in [reconstruction-scenarios.md](reconstruction-scenarios.md). Results assume **conformant** KCM population unless noted. Determinism means reconstruction procedure yields the same structural triad statements from retained bindings without heuristic correlation (checklist §3.3).

### Scenario 1 — Model-assisted eligibility denial

| Item | Result |
|---|---|
| **Reconstruction result** | **Complete** base triad PASS if mandatory objects at commitment (Decision, Subject, Inference, Model Version, Evidence Snapshot, Policy Version, Human Review, Authority, Notification as conditioned) |
| **Required assumptions** | Authority registry; evidence snapshot before feature mutation; Decision ID on notice/appeal systems |
| **Remaining limitations** | Does not judge fairness of denial; Explanation optional unless profile requires |
| **Deterministic?** | **Yes**, under assumptions |

### Scenario 2 — Policy change after decision

| Item | Result |
|---|---|
| **Reconstruction result** | **Complete** for historical authorization/validity via immutable Decision ↔ Policy Version; current `P2` unused |
| **Required assumptions** | Historical Policy Version content retrievable by id/hash |
| **Remaining limitations** | Operators may fail to register Policy Version (non-conformant → FAIL) |
| **Deterministic?** | **Yes** when binding present |

### Scenario 3 — Human override without preserved rationale

| Item | Result |
|---|---|
| **Reconstruction result** | **Complete** if Override with required rationale + original Inference + Authority committed; **Failed** if outcome-only store (non-conformant) |
| **Required assumptions** | Commitment gate rejects override without rationale |
| **Remaining limitations** | Rationale *quality* out of scope |
| **Deterministic?** | **Yes** when conformant; ecosystem outcome-only path remains FAIL |

### Scenario 4 — Model or dataset update

| Item | Result |
|---|---|
| **Reconstruction result** | **Complete** for historical justification context (model/dataset/pipeline versions + evidence snapshot + inference); **not** bit-exact replay |
| **Required assumptions** | Version artifacts remain resolvable |
| **Remaining limitations** | Internal model non-determinism may remain; faithfulness ≠ full reproducibility (§3.2) |
| **Deterministic?** | **Yes** for normative/evidential basis; **No** claim of compute-identical replay |

### Scenario 5 — Logging without shared identity

| Item | Result |
|---|---|
| **Reconstruction result** | **Complete** if Decision ID minted and attached to all emitters; **Failed** if only timestamp/email correlation of legacy islands (explicitly disallowed) |
| **Required assumptions** | Instrumentation attaches `decisionId` |
| **Remaining limitations** | Pre-adoption log stitching may remain PARTIAL |
| **Deterministic?** | **Yes** under conformant adoption; **No** for unbound legacy correlation |

### Scenario 6 — Appeal after partial data deletion

| Item | Result |
|---|---|
| **Reconstruction result** | **Complete** if Evidence Snapshot retained (possibly redacted with explicit reliance semantics) and Appeal bound; **Partial** if law forces deletion of raw relied-upon data but digests/categories remain; **Failed** if relied-upon evidence wholly destroyed without lawful substitute |
| **Required assumptions** | Retention schedule reconciles privacy law with declared profile |
| **Remaining limitations** | Model does not override law; justification may be forced PARTIAL |
| **Deterministic?** | **Yes** for whatever structure remains; outcome class depends on lawful retention |

### Scenario summary table

| Scenario | Ecosystem (prior) | KCM (conformant) | Deterministic under assumptions? |
|---|---|---|---|
| 1 Eligibility denial | Impossible / FAIL | Complete PASS | Yes |
| 2 Policy change | Partial island / FAIL triad | Complete PASS (historical policy) | Yes |
| 3 Override sans rationale | Impossible (outcome-only) | Complete if gated; else Failed | Yes if conformant |
| 4 Model/dataset update | Impossible / weak partial | Complete (basis, not bit-replay) | Yes for basis |
| 5 No shared identity | Impossible | Complete if ID propagated | Yes if conformant |
| 6 Appeal after deletion | Impossible / partial authz | Complete / Partial / Failed by retention | Yes within retained set |

---

## 5. Comparison with existing ecosystem

Capability comparison is **information and binding** only—not implementation technologies.

| Concern | Current reviewed ecosystem | Knowledge Continuity Model |
|---|---|---|
| **Decision identity** | Local islands (policy decision id, task id, trace id); no shared episode key | First-class immutable Decision ID as join key |
| **Temporal continuity** | Optional event times; organizational change mgmt ≠ decision as-of | Multi-axis times + validity intervals; latest-only forbidden |
| **Human review** | Strong workflow (WS-HumanTask) without retention/rationale mandate or decision binding | Human Review / Override with actor, authority, required rationale, Decision binding |
| **Policy preservation** | OPA bundle revision inside logs; Cedar often non-durable; repos drift to current | Immutable Policy Version sealed to Decision |
| **Evidence preservation** | Live stores / lineage of pipelines; weak IC-11 | Evidence Snapshot with available vs relied-upon |
| **Explanation** | Quality principles / rights; post-hoc regeneration risk | Optional decision-time Explanation; never sole justification |
| **Authority** | Task roles / eval principals; weak external mandate artifact | Authority object with temporal validity bound to acts |
| **Remediation** | Process docs / rights; weak technical linkage | Append-only Remediation / superseding Decision links |
| **Cross-system composition** | **FAIL** without custom bindings (composition analysis) | Durable bindings defined exactly once; reconstruction algorithm fail-closed |

**Verdict of comparison:** KCM does not replace provenance, observability, lineage, policy engines, documentation, explainability, human workflow, or legal logging. It supplies the missing **episode-centric composition** those components lack for deterministic faithful reconstruction.

---

## 6. Remaining limitations

KCM still does **not** solve:

1. **Organizational adoption** — non-instrumented emitters and outcome-only stores FAIL scenarios despite the model.
2. **Incomplete retention** — if mandatory objects age out before the reconstruction horizon, triad PASS collapses.
3. **Legal restrictions** — personal-data minimization may force Scenario 6 PARTIAL/FAIL; KCM must be reconciled with law, not override it.
4. **Unavailable historical evidence** — snapshots never captured cannot be reconstructed; fail-closed reports gaps rather than inventing content.
5. **Implementation quality** — buggy registries, recycled actor ids, unresolved content hashes, or skipped commitment gates yield non-conformance.
6. **Governance failures outside the model** — unfair, inaccurate, or unauthorized *substance* of decisions; security; privacy programme completeness; rationale text quality (KCM §12).
7. **Category thinness** — IC-09, IC-12, IC-14–16, IC-18, IC-20 remain PARTIAL without profile elevation or careful snapshot encoding.
8. **Elevated integrity** — IC-21/IC-22 not required for base faithfulness.
9. **Retroactive legacy** — pre-adoption logs without Decision ID remain non-deterministic to stitch.
10. **Universal completeness** — not claimed; sufficiency is relative to checklist base triad under stated assumptions.

---

## 7. Threats to validity

| Threat | Discussion |
|---|---|
| **Conceptual evaluation** | Scores assess specified objects/bindings, not field deployments. A conformant implementation might still be rare; that constrains **adoption claims**, not the checklist mapping of the specification text. |
| **Absence of deployment measurements** | No frequency estimates of PASS/FAIL in industry; scenarios remain adversarial analytical tests. |
| **Dependency on correct implementations** | Triad PASS is conditional on commitment gates and retention. Implementation failure falsifies a deployment, not the checklist alignment of the model text—consistent with how optional features in OPA/HumanTask were scored. |
| **Sector-specific adaptations** | Profiles may elevate IC-12/IC-20/IC-21 without changing base triad rules; domain extras are out of scope here. |
| **Future standards** | A composition profile over existing stores that realizes the same objects/bindings would also PASS (KCM §13 / C8 framing). This evaluation does not assert that only a branded product layer can succeed. |
| **Authoring bias** | KCM was derived to answer composition failures; evaluation risks circular confirmation. Mitigation: same checklist marks and scenario set used against the ecosystem; PARTIAL rows and Scenario 6 limits are recorded explicitly. |

---

## 8. Conclusions

| Dimension | Outcome |
|---|---|
| **Checklist** | Required identity, policy version, evidence reliance, model version, human acts/authority, and decision-bound provenance/lineage **PASS**. Constraints, excluded evidence, prompts/tools/external services, assumptions, legal context, and integrity/signatures remain **PARTIAL** or optional as classed. |
| **Base triad** | Authorization, justification, and validity **PASS** under conformant mandatory population → base faithful reconstruction **PASS**. |
| **Scenarios** | Scenarios 1–5 **Complete PASS** when conformant (Scenario 3/5 FAIL if non-conformant). Scenario 6 **Complete / Partial / Failed** by lawful evidence retention. |
| **Remaining limitations** | Adoption, retention, law, implementation quality, and out-of-scope governance substance (§6). |

**Sufficiency statement (bounded):** Under its stated assumptions—mandatory Decision Episode objects and bindings populated at commitment, historical version artifacts resolvable, retention horizon honoured, and reconstruction fail-closed on gaps—the Knowledge Continuity Model **appears sufficient** for **deterministic faithful reconstruction** of the base justification / authorization / validity triad as defined by checklist v0.1.0 §3 and §8.3.

**Not claimed:** perfection; universal deployment success; bit-exact replay; legal compliance completeness; or that no alternative composition profile could realize the same information requirements.

---

## Related artifacts

| Artifact | Relationship |
|---|---|
| [reconstruction-checklist.md](../architecture/reconstruction-checklist.md) | Scoring criteria (unchanged) |
| [knowledge-continuity-model.md](../architecture/knowledge-continuity-model.md) | SUT (unchanged) |
| [reconstruction-scenarios.md](reconstruction-scenarios.md) | Scenario set (unchanged) |
| [composition-analysis.md](composition-analysis.md) | Ecosystem FAIL baseline (unchanged) |
| [conformance-specification.md](../architecture/conformance-specification.md) | Normative testability companion (not modified; not rescored here) |
| [review-methodology.md](methodology/review-methodology.md) | Evidence/scoring discipline (unchanged) |
