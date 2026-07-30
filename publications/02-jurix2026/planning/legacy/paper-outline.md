---
id: pub-jurix2026-paper-outline
title: "JURIX 2026 paper outline: Engineering Knowledge Continuity for Legally Relevant AI Systems"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, lncs, outline, knowledge-continuity, reconstruction]
source_topics: [ai-infrastructure-gap]
target_venue: JURIX 2026
venue_format: LNCS (approx. 16 pages)
publish: false
checklist_version: "0.1.0"
---

<!-- markdownlint-disable MD026 MD029 -->

> **Legacy precursor.** This file is an older JURIX 2026 outline preserved for history. It is **not** the authoritative outline for Publication 02. The authoritative planning spine is `../outline.md` (derived from `../jurix-specification.md`). Do not merge this document into the current manuscript automatically.

## Paper outline — JURIX 2026

**Working title:** Engineering Knowledge Continuity for Legally Relevant AI Systems

**Document role.** Publication-oriented outline mapping completed `topics/ai-infrastructure-gap` research artifacts into a coherent JURIX manuscript plan. **Not** full prose; **not** new research; **not** a change to architecture, evaluation, claims, or BibTeX.

**Venue assumptions.** JURIX / Springer LNCS long paper ≈ **16 pages**. Structure below follows a conventional LNCS research-paper spine (Introduction → Background → Method → Results → Proposal → Discussion → Threats → Conclusion).

---

## Front matter (placeholders)

| Field | Value |

|---|---|
| **Title** | Engineering Knowledge Continuity for Legally Relevant AI Systems |
| **Authors** | *[to be filled — do not invent]* |
| **Affiliations** | *[to be filled]* |
| **ORCID** | *[to be filled]* |
| **Corresponding author** | *[to be filled]* |
| **Acknowledgements** | *[to be filled — funding, reviewers, tooling]* |
| **Keywords (draft)** | AI governance; decision reconstruction; knowledge continuity; provenance; authorization; explainability; EU AI Act; conformance |

**Publication discipline (from claim inventory):** Internal claims C1–C8 remain **hypotheses** unless and until explicitly promoted. The manuscript must present evaluation findings as evidence relative to the reconstruction checklist, not as established universal laws. Do not cite the claim inventory as settled fact.

---

## Section 1 — Introduction

**Target length:** ~1.5–2 pages.

### 1.1 Motivation

- Legally and operationally consequential AI-assisted decisions may later require reconstruction (audit, appeal, incident review, regulatory inquiry).

- Organizations already retain rich artifacts: traces, logs, provenance, policy decisions, model cards, human-task records, risk documentation.
- **Practical question:** whether retained structure supports reconstructing *why* a historically situated decision was justified, authorized, and valid *when made*.
- **Source:** `topics/ai-infrastructure-gap/charter.md` §1–§3.

### 1.2 Practical problem

- Reconstruction often collapses into informal correlation of timestamps, usernames, and “current” dashboards.

- Policy, model, and feature drift silently rewrite post-hoc accounts (latest-only substitution).
- Human overrides and explanations may leave no durable, decision-bound record.
- **Source:** `evaluation/reconstruction-scenarios.md` (Scenarios 2–5); `evaluation/composition-analysis.md` §4–§6.

### 1.3 Research gap

- Unit capabilities in the reviewed ecosystem are often strong for *native* goals (derivation, observability, authorization eval, documentation, oversight workflow, legal logging).

- Gap is primarily **compositional**: missing durable cross-system bindings for one decision episode—not absence of logging/provenance/XAI individually.
- Competing explanations E1–E5 from charter (no gap / composition / semantic / temporal / new layer) frame the investigation; evaluation supports composition/temporal/semantic residuals without prematurely asserting a branded product layer.
- **Sources:** `charter.md` §4–§5; `evaluation/composition-analysis.md` §7; `evaluation/coverage-audit.md`.

### 1.4 Research question

**Draft RQ (aligned with charter; not a new claim):**

*Can existing AI governance infrastructure, alone or in composition, support deterministic faithful reconstruction of justification, authorization, and validity for historically situated AI-assisted decisions—and if not, what minimum information and bindings are required?*

### 1.5 Contribution summary

Outline contributions (map to later sections; no stronger wording than evaluation supports):

1. **Reconstruction checklist** — technology-neutral information categories and base triad (justification / authorization / validity). → §3
2. **Structural evaluation** — unit reviews, coverage audit, adversarial scenarios, composition analysis showing compositional FAIL without durable bindings. → §4–§5
3. **Knowledge Continuity Model (KCM)** — Decision Episode objects, bindings, temporal model, reconstruction procedure. → §6
4. **Conformance specification** — KC Core / KC Extended normative requirements with pass/fail verification. → §7
5. **Model evaluation** — KCM scored with the *same* checklist methodology; base triad PASS under stated assumptions; limitations retained. → §5/§8

### 1.6 Paper structure

One

-paragraph roadmap: §2 related work families → §3 checklist → §4 method → §5 results → §6 KCM → §7 conformance → §8 discussion → §9 threats → §10 conclusion.

**Figures:** introduce Figure 1 (research workflow) here or at end of §1.

---

## Section 2 — Background and Related Work

**Target length:** ~2.5–3 pages (**condensation risk: high**).

Map completed unit reviews into families. For each: purpose, principal sources (review files + BibTeX keys already in `references/bib/library.bib`), remaining limitation *as scored*—do not add literature.

### 2.1 Provenance

| | |

|---|---|
| **Purpose** | Derivation: entities, activities, agents; “from what / by whom.” |
| **Principal sources** | W3C PROV-DM (`evaluation/reviews/2026-07-29-w3c-prov-dm.md`) |
| **Remaining limitation** | Not a decision-episode / policy-version / reliance model; triad FAIL alone. |

### 2.2 Observability and execution telemetry

| | |

|---|---|
| **Purpose** | Traces, metrics, logs of runtime paths. |
| **Principal sources** | OpenTelemetry specification review |
| **Remaining limitation** | Paths ≠ normative basis; no standard decision-episode semantic. |

### 2.3 ML metadata and data lineage

| | |

|---|---|
| **Purpose** | Artifact/execution graphs; job/dataset lineage. |
| **Principal sources** | Google ML Metadata; OpenLineage reviews |
| **Remaining limitation** | Pipeline-centric; unbound to business decision identity; weak IC-11. |

### 2.4 Policy and authorization engines

| | |

|---|---|
| **Purpose** | Evaluate allow/deny; optional decision logs / diagnostics. |
| **Principal sources** | Open Policy Agent; Cedar reviews |
| **Remaining limitation** | Strong *islands*; cross-system episode binding absent; Cedar durability not mandated. |

### 2.5 Model, dataset, and system documentation

| | |

|---|---|
| **Purpose** | Release-time reporting of models, datasets, systems. |
| **Principal sources** | Model Cards; Datasheets for Datasets; System Cards reviews |
| **Remaining limitation** | Documentation ≠ episode records; current-version substitution risk. |

### 2.6 Organizational AI governance / risk management

| | |

|---|---|
| **Purpose** | Organizational risk, roles, oversight processes. |
| **Principal sources** | NIST AI RMF 1.0 review |
| **Remaining limitation** | Process documentation ≠ decision-time reconstruction schema. |

### 2.7 Explainability

| | |

|---|---|
| **Purpose** | Explanation quality properties for AI systems. |
| **Principal sources** | NISTIR 8312 review |
| **Remaining limitation** | Quality principles ≠ durable decision-bound justification package. |

### 2.8 Legal logging and record-keeping duties

| | |

|---|---|
| **Purpose** | Automatic logging, retention floors, selected high-risk fields; explanation *rights*. |
| **Principal sources** | EU AI Act decision/audit records review |
| **Remaining limitation** | Purpose-based events ≠ general decision composition schema; privacy law may force deletion (Scenario 6). |

### 2.9 Human oversight workflow

| | |

|---|---|
| **Purpose** | Human task lifecycle, roles, completion history. |
| **Principal sources** | OASIS WS-HumanTask 1.1 review |
| **Remaining limitation** | No retention duty; rationale optional; no cross-system Decision ID. |

### 2.10 Synthesis pointer

Close §2 by stating that related work supplies complementary *capabilities* evaluated further in §5; defer composition argument (avoid duplicating §5).

**Table:** Table 1 — reviewed source families (compact).

---

## Section 3 — Reconstruction Checklist

**Target length:** ~1–1.5 pages.

**Primary source:** `architecture/reconstruction-checklist.md` (v0.1.0).

### Outline bullets-

**Motivation:** Judge reconstruction by recoverable *information and bindings*, not by presence of a technology brand (checklist §1.3).

- **Methodology:** Engineering criteria for faithful reconstruction (§3); what reconstruction is *not* (replay, audit logging, provenance, XAI, traces, reproducibility) (§4).
- **Checklist structure:** Requirement classes Required / Conditionally required / Optional (§5); information categories IC-01–IC-24 (§6); binding/composition criteria (§7).
- **Base triad:** Authorization, Justification, Validity as separable targets; roll-up rules (§8.3).
- **Scoring approach:** PASS / PARTIAL / FAIL / N/A; composition allowed only with declared bindings; no credit for adjacent capability (§7–§8).

**Table:** Table 2 — checklist summary (triad + exemplar IC categories; not all 24 rows in full).

**Do not** reprint the full checklist.

---

## Section 4 — Evaluation Methodology

**Target length:** ~1–1.5 pages.

**Sources:** `evaluation/methodology/review-methodology.md`; coverage audit; scenarios; composition analysis (method parts only).

### Outline bullets-

**Unit reviews:** One publication/standard/approach per review; map to checklist; record strengths/limitations; 13 completed reviews (list families, cite review paths).

- **Scoring:** Methodology 0–3 scale for high-level capability rows; checklist marks PASS/PARTIAL/FAIL/N/A; no scoring of implementation generosity beyond what the source mandates.
- **Coverage audit:** Family coverage vs residuals; stop unit-source expansion; shift to scenarios/composition (`evaluation/coverage-audit.md`).
- **Scenarios:** Six adversarial reconstruction scenarios (`evaluation/reconstruction-scenarios.md`).
- **Composition analysis:** Same-identity and decision-time binding required; two adequate components without durable binding = insufficient (`evaluation/composition-analysis.md` §1).
- **KCM evaluation method:** Same checklist applied to proposed model (`evaluation/kcm-evaluation.md` §1)—mention here or bridge at end of §4 / start of §5.

**Figure:** Figure 1 — Research workflow (checklist → unit reviews → coverage → scenarios → composition → KCM → conformance → KCM evaluation).

**Do not** duplicate long evidence tables from reviews.

---

## Section 5 — Evaluation Results

**Target length:** ~2–2.5 pages (**condensation risk: high**).

### 5.1 Coverage findings

- Strong coverage across provenance, observability, lineage/ML metadata, policy/authz, documentation, RMF, XA

I, legal logging, human workflow.

- Residual is compositional, not a missing peer family.
- **Source:** `evaluation/coverage-audit.md`.

### 5.2 Scenario findings

- Summarize

Scenarios 1–6 outcomes under default ecosystem composition (mostly Impossible / FAIL triad).

- **Source:** `evaluation/reconstruction-scenarios.md`.
- **Table:** Table 3 — scenario evaluation summary.

### 5.3 Composition findings-

Principal limitation: absence of durable cross-system decision-episode composition.

- Base triad compositional result: Authorization FAIL (PARTIAL islands); Justification FAIL; Validity FAIL; faithful reconstruction FAIL.
- Critical missing bindings (decision ID across inference, policy, evidence, human task, notice/appeal, correction).
- **Source:** `evaluation/composition-analysis.md` §§3–7.
- **Figure:** Figure 2 — Fragmented governance ecosystem.
- **Table:** Table 4 — composition comparison (ecosystem vs required bindings).

### 5.4 Major architectural gaps (manuscript wording)

List only gaps already identified (no new ones):

1. Shared decision identity
2. Decision-time policy/model/evidence version seals
3. Relied-upon vs available evidence
4. Authority distinct from task role
5. Human override/rationale retention
6. Contestability linkage (notice/appeal/remediation)
7. Aligned retention across stores

### 5.5 KC

M evaluation results (bridge)- Same checklist: base triad **PASS** under conformant assumptions; PARTIAL on IC-09/12/14–16/18/20–22; Scenario 6 retention-dependent.

- **Source:** `evaluation/kcm-evaluation.md` §§2–4, §8.
- Emphasize: does **not** change prior ecosystem FAIL results; evaluates the proposal against the same bar.

---

## Section 6 — Knowledge Continuity Model

**Target length:** ~2–2.5 pages (**condensation risk: medium–high**).

**Primary source:** `architecture/knowledge-continuity-model.md` (**unchanged**; outline only).

### Outline bullets-

**Design objective:** Deterministic faithful reconstruction per checklist §3; technology-neutral; incremental adoptability (KCM §1, §11).

- **Design principles:** Ten principles condensed to prose bullets (Decision Episode primary; stable identity; durable bindings; historical truth; temporal validity; versioned refs; human responsibility; minimal sufficient reconstruction; neutrality; incremental adoption) (§2).
- **Decision Episode:** Definition, boundaries, lifecycle, immutable identity (§3).
- **Persistent objects:** Decision, Subject, Actors, Authority, Inference, Model/Dataset/Pipeline versions, Evidence Snapshot, Policy/Policy Version, Explanation, Human Review, Override, Notification, Appeal, Remediation, Audit Record—grouped summary, not full attribute tables (§4).
- **Semantic bindings:** Decision ↔ {inference, evidence, policy version, model version, human review, authority, …}; immutability after commitment; fail if absent (§5).
- **Temporal model:** Time axes; validity intervals; append-only correction; why latest-only fails (§6).
- **Reconstruction algorithm:** Ten logical steps; fail closed (§8)—detail deferred to Figure 5 / short enumeration.
- **Relationship to existing components:** Complements, does not replace (§10).
- **Scope limitations:** Point to KCM §12 (quality, fairness, privacy-by-itself, etc.).

**Figures:** Figure 3 — Decision Episode; Figure 4 — Knowledge Continuity Model (objects + bindings overview).

**Do not** introduce new objects or bindings.

---

## Section 7 — Conformance Specification

**Target length:** ~1–1.5 pages.

**Primary source:** `architecture/conformance-specification.md` (**unchanged**; outline only).

### Outline bullets-

**Objective:** Normative, testable, technology-neutral PASS/FAIL for implementations claiming KCM support (RFC 2119 keywords).

- **Conformance classes:** KC Core; KC Extended; future classes reserved undefined.
- **Normative requirements:** KC-01…KC-34 summarized by theme (identity, episode, evidence/policy/AI/human/authority/temporal/explanation/contestability/bindings/reconstruction completeness/neutrality)—**do not** reprint all 34 full requirement blocks.
- **Reconstruction verification:** Complete / partial / failed reconstruction; required inputs/outputs; fail-closed.
- **Base-triad verification:** Objective evidence criteria for Authorization, Justification, Validity.
- **Relationship to checklist:** Traceability matrix principles → requirements → checklist categories.
- **Scope exclusions:** No mandated storage, crypto, schemas, protocols, vendor APIs.

**Table:** Table 5 — conformance overview (classes + requirement theme counts).

---

## Section 8 — Discussion

**Target length:** ~1–1.5 pages.

Placeholders for prose expansion (content grounded only in existing artifacts):

### 8.1 Implications-

*[Prose TBD]* For AI governance engineering, legal-tech reconstruction, and audit practice: episode-centric bindings as first-order requirement.

- Tie to charter explanations E2–E4 without promoting C1–C8 beyond hypothesis status in external citation.
- **Sources:** composition analysis §7; KCM evaluation §8; charter §4.

### 8.2 Engineering trade-offs-

*[Prose TBD]* Retention vs privacy (Scenario 6); snapshot cost vs live feature stores; commitment-gate strictness vs operational friction; minimal sufficient reconstruction vs forensic elevation (IC-21/22).

- **Sources:** KCM §11–§12; kcm-evaluation §6; scenarios Scenario 6.

### 8.3 Comparison with current practice-

*[Prose TBD]* Reuse Table 4 / ecosystem vs KCM comparison from kcm-evaluation §5 (identity, temporal, human review, policy, evidence, explanation, authority, remediation, composition).

- Explicit: complements provenance, observability, lineage, policy engines, documentation, XAI, human workflow, AI governance—does not replace them.

### 8.4 Deployment considerations-

*[Prose TBD]* Incremental adoption path (mint Decision ID → wrap existing engines → snapshot evidence → commitment gates → notice/appeal).

- Non-conformant deployments still FAIL (Scenario 3/5).
- **Source:** KCM §11.

---

## Section 9 — Threats to Validity

**Target length:** ~0.75–1 page.

Map **directly** from existing documents (merge, do not invent new threat classes):

| Threat | Source documents |
|---|---|
| Dependence on available / published standards | `composition-analysis.md` §9 |
| Implementation variability / optional features | composition-analysis §9; unit-review methodology |
| Sector-specific narrow fields (e.g. biometric subclass) | composition-analysis §9; coverage-audit |
| Evolving regulation / future standards | composition-analysis §9; KCM §13 |
| Absence of deployment frequency measurements | composition-analysis §9; kcm-evaluation §7 |
| Conceptual evaluation of KCM (not field trial) | kcm-evaluation §7 |
| Dependency on correct KCM implementations | kcm-evaluation §7; KCM §13 |
| Authoring bias (proposal derived to answer gaps) | kcm-evaluation §7 |
| Alternative composition profiles (C8 framing) | KCM §13; composition-analysis §8 |

---

## Section 10 — Conclusion

**Target length:** ~0.5–0.75 page.

### Outline bullets-

**Research question:** Restate RQ; answer in bounded form.

- **Findings:** Reviewed ecosystem does not guarantee deterministic faithful reconstruction without custom durable bindings; compositional triad FAIL; KCM under assumptions appears sufficient for base triad PASS (kcm-evaluation §8 wording—avoid stronger claims).
- **Contribution:** Checklist + evaluation + KCM + conformance as engineering pathway for knowledge continuity.
- **Future work:** Composition-profile falsification (C8); optional sector profiles; deployment studies; elevated integrity profiles—**no new literature campaign**.
- **Sources:** `future-work/research-plan.md` (select only items consistent with completed Phase results); kcm-evaluation §8; composition-analysis §10.

---

## Figure plan

| ID | Title | Purpose | Source documents | Expected message |

|---|---|---|---|---|
| **Figure 1** | Research workflow | Show methodological pipeline from problem framing to conformance | charter; checklist; methodology; coverage-audit; scenarios; composition-analysis; KCM; conformance-spec; kcm-evaluation | Evaluation precedes proposal; same checklist closes the loop |
| **Figure 2** | Fragmented governance ecosystem | Depict capability islands without shared Decision ID | composition-analysis §§1–3; scenarios Scenario 5; unit reviews (families) | Strong components ≠ compositional reconstruction |
| **Figure 3** | Decision Episode | Define episode lifecycle and boundary | KCM §3 | Episode is the primary engineering object |
| **Figure 4** | Knowledge Continuity Model | Objects + principal bindings overview | KCM §§4–5 | Durable bindings seal decision-time structure |
| **Figure 5** | Reconstruction process | Technology-neutral reconstruction steps / fail-closed | KCM §8; conformance-spec reconstruction verification | Deterministic procedure from Decision ID to triad statements |

**Optional (if page budget allows):** Figure 6 — Scenario 2 policy drift (historical vs current policy). Drop first under condensation.

---

## Table plan

| ID | Title | Purpose | Source documents |

|---|---|---|---|
| **Table 1** | Reviewed source families | Compact related-work map (family / exemplar SUT / triad alone) | 13 unit reviews; coverage-audit |
| **Table 2** | Reconstruction checklist summary | Triad roll-up + selected IC categories / classes | reconstruction-checklist.md |
| **Table 3** | Scenario evaluation | Scenarios 1–6: ecosystem result vs KCM (conformant) | reconstruction-scenarios.md; kcm-evaluation §4 |
| **Table 4** | Composition comparison | Required bindings vs ecosystem provision | composition-analysis §§3–5; kcm-evaluation §5 |
| **Table 5** | Conformance overview | KC Core / Extended; requirement themes; verification categories | conformance-specification.md |

**Optional:** Table 6 — KCM checklist scores (PASS/PARTIAL summary). Drop or move to appendix if over length.

---

## Word / page budget (LNCS ≈ 16 pages)

Approximate allocation (body + figures/tables sharing space):

| Section | Pages (approx.) | Words (approx.) | Condensation notes |
|---|---:|---:|---|
| Front matter + abstract | 0.5 | 150–250 (abstract) | Abstract written at prose stage |
| §1 Introduction | 1.5–2 | 700–900 | Keep RQ + contributions tight |
| §2 Background / related work | 2.5–3 | 1100–1400 | **High risk** — family subsections must be 1 short para each; push detail to Table 1 |
| §3 Reconstruction checklist | 1–1.5 | 450–650 | Summarize; no full IC dump |
| §4 Evaluation methodology | 1–1.5 | 450–650 | Pointer-style |
| §5 Evaluation results | 2–2.5 | 900–1200 | **High risk** — rely on Tables 3–4 + Figure 2 |
| §6 Knowledge Continuity Model | 2–2.5 | 900–1200 | **Medium–high risk** — Figures 3–4 carry structure; cut attribute tables |
| §7 Conformance specification | 1–1.5 | 450–650 | Theme summary + Table 5; no KC-01…34 full text |
| §8 Discussion | 1–1.5 | 450–650 | Four short subsections |
| §9 Threats to validity | 0.75–1 | 300–450 | Single consolidated table/list |
| §10 Conclusion | 0.5–0.75 | 200–350 | Bounded sufficiency claim only |
| References | 1–1.5 | — | BibTeX keys already in library; **do not expand literature** |
| **Total** | **≈ 16** | **≈ 6000–8000 body words** | Figures/tables consume page share |

**Sections most likely to require substantial condensation:** §2, §5, §6, References.

---

## Traceability matrix### Repository document → paper section(s)

| Repository artifact | Paper section(s) | Planned use |

|---|---|---|
| `charter.md` | §1, §8, §10 | Motivation, competing explanations, RQ framing |
| `architecture/claim-inventory.md` | §1 (discipline note), §8/§9 (hypothesis status) | **Internal guardrail** — do not cite claims as established fact; do not modify file |
| `architecture/reconstruction-checklist.md` | §3, Table 2, Figures 1/5 | Normative evaluation criteria |
| `architecture/knowledge-continuity-model.md` | §6, Figures 3–5, §8 | Proposal content |
| `architecture/conformance-specification.md` | §7, Table 5 | Normative conformance |
| `evaluation/methodology/review-methodology.md` | §4 | Scoring discipline |
| `evaluation/coverage-audit.md` | §4, §5.1 | Coverage / stop rule |
| `evaluation/reconstruction-scenarios.md` | §4, §5.2, Table 3 | Scenario set |
| `evaluation/composition-analysis.md` | §5.3–5.4, Figure 2, Table 4, §9 | Compositional FAIL argument |
| `evaluation/kcm-evaluation.md` | §4, §5.5, Table 3, §8, §9, §10 | Proposal scored on same bar |
| Unit reviews (13 files under `evaluation/reviews/2026-07-29-*.md`) | §2, Table 1, §5 | Family evidence |
| `evaluation/reviews/template.md` | — | **No planned manuscript use** (process template) |
| `references/bib/library.bib` | References | Citation keys for reviewed sources only; **unchanged** |
| `future-work/research-plan.md` | §10 | Future work bullets (selective) |
| `evaluation/approach-comparison-matrix.md` | — / optional appendix | **Currently limited use** — matrix largely scaffolding; not required for outline spine |
| `evaluation/data/reconstruction-evaluation.csv` | — / optional appendix | **Currently limited use** — dataset may be incomplete relative to narrative results |
| Topic READMEs (`architecture/README`, evaluation stubs, `literature/`, `notes/`, `ideas/`, `specifications/`, `reviews/README`, `future-work/README`) | — | **No planned manuscript use** |
| `topics/ai-infrastructure-gap/README.md` | — | Index only; no planned use |

### Artifacts with no / limited planned use1. `evaluation/reviews/template.md` — process only.

2. Topic folder READMEs and empty stub directories — navigation only.
3. `evaluation/approach-comparison-matrix.md` — not yet a primary evidence carrier; optional later appendix if filled from reviews without changing results.
4. `evaluation/data/reconstruction-evaluation.csv` — optional machine-readable companion; narrative results already in reviews/scenarios/composition docs.
5. Claim inventory — **not** a citeable results table; publication discipline source only.

Every **major** completed research artifact (charter, checklist, 13 reviews, methodology, coverage audit, scenarios, composition analysis, KCM, conformance, KCM evaluation) has a destination above.

---

## Manuscript expansion notes (next step — out of scope here)1. Write abstract (150–250 words) from §1.5 + §5 + §10.

2. Expand outline bullets to LNCS prose without adding sources.
3. Draft figures as TikZ/SVG from figure plan.
4. Generate tables from existing evaluation docs.
5. Select BibTeX entries already present—**no new literature review**.
6. Freeze wording of evaluation results and KCM/conformance to match source documents.

---

## Validation checklist (outline stage)

| Check | Status |

|---|---|
| Every major repository artifact referenced in traceability | Yes |
| No new research claims introduced | Yes — findings restated from existing eval docs; claims remain hypotheses |
| Architecture unchanged | Yes — KCM referenced only |
| Evaluation unchanged | Yes — results mapped, not rewritten as new scores |
| Conformance unchanged | Yes |
| BibTeX unchanged | Yes (no edit) |
| LNCS-consistent spine | Yes (Intro→Related→Method→Results→Proposal→Discussion→Threats→Conclusion) |
| Commit | **Not created** |
