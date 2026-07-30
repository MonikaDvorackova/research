---
id: review-2026-07-29-system-cards
title: "Review: System Cards (Procope et al., Meta AI 2022) against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, system-cards, documentation, transparency, reconstruction]
refs: [procope2022systemCards]
sut: "Procope et al., System-Level Transparency of Machine Learning (Meta AI, 2022) — original System Cards proposal"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C1]
---

# Review

## Bibliographic Information

**Title:** System-Level Transparency of Machine Learning

**Authors:** Chavez Procope, Adeel Cheema, David Adkins, Bilal Alsallakh, Nekesha Green, Emily McReynolds, Grace Pehl, Erin Wang, Polina Zvyagina

**Venue / publisher:** Meta AI research publication (February 22, 2022)

**Version pin:** Official Meta AI PDF of *System-Level Transparency of Machine Learning* (5 pages), retrieved from the Meta Research publications page “Download the Paper” asset.

**DOI / URL:**

- Publication page: https://ai.meta.com/research/publications/system-level-transparency-of-machine-learning/
- Companion blog (not scored as SUT body): https://ai.meta.com/blog/system-cards-a-new-resource-for-understanding-how-ai-systems-work/
- No DOI asserted on the inspected PDF

**Source attribution note:** The task brief cited *Google Research, “System Cards: Model Reporting for Complex AI Systems.”* No publication matching that exact title/attribution was located (arXiv / web search, 2026-07-29). The earliest peer-facing proposal that introduces **System Cards** as a named documentation artefact for complex multi-component ML systems is this Meta AI paper. **That paper is the SUT.** Gemini docs, later Google deployments, and other vendors’ “system cards” are out of scope.

**Primary sources inspected:**

| Source | Role |
|---|---|
| Procope et al. 2022 PDF (§§1–4) | Design intent; System Cards information model (§3); challenges |
| Figure 1 (in PDF) | Archetypal content-ranking system overview diagram (illustrative) |

**Supplementary material:** None beyond the main 5-page PDF. No official appendix was identified for this publication.

**Primary source availability:** Sufficient for a complete review of the *original proposal’s* thin but explicit information model.

**Not SUT:** Instagram/Meta product System Card pilots beyond the paper’s fictional/illustrative diagram; Gemini documentation; later Google or OpenAI “system card” reports; organization-specific templates; regulatory adaptations; governance frameworks; custom documentation systems; Model Cards / Datasheets / FactSheets (cited as prior art, not credited as System Cards content except where §3 explicitly incorporates links to model cards).

**Pre-scoring notes:**

- **Design intent:** stakeholder transparency into *ML system architecture and operation*—not decision-episode reconstruction.
- **Credit rule:** only §3-structured elements; free-text description/purpose and example walkthroughs are not decision identity/evidence/authorization; maintenance/provenance called out as future work.
- **Likely N/A / FAIL:** decision identity/outcome; policy/legal justification; decision-bound reliance.
- **Threats (preview):** short foundational note; non-exhaustive schema; security-motivated information withholding.

---

## 1. Design intent

System Cards aim to increase transparency of **ML systems** (multiple models, datasets, and non-ML components working together) by giving stakeholders an overview of components, how they interact, and how data and protected information are used (Abstract; §1).

Motivation: Model Cards and Datasheets document individual models and datasets but may not capture **system-level** information needed for complex pipelines (e.g. content ranking with multiple modalities and human-in-the-loop steps) or model-to-model dependencies (embeddings / transfer learning) (§1).

The solution targets both expert stakeholders (developers, reviewers) and non-experts who want to understand ML underpinning their experiences (§1). The authors present the work as laying a **foundation** for which elements to include, at which intervention points, and for which audiences—not as a complete formal schema (§4).

**Intent for this review:** evaluate whether this **original System Cards information model** preserves information needed for faithful reconstruction of historically situated, legally relevant AI-supported *decisions*.

---

## 2. Observed capabilities

(First-class / documented in §3 of the proposal only.)

### 2.1 Documented System Card structure (§3)

A System Card provides:

1. **Overview of constituent ML models** and details about these components, plus a walkthrough with an example input.
2. **Overview First (entry page):**
   - brief description of the system and its **purpose**;
   - information about its **authors** and **current version**;
   - a **high-level diagram** of system components showing how they achieve the desired functionality (Figure 1: fictional content-ranking example with text/image/video modalities processed to a final ranking).
3. **Interactive Exploration:**
   - access **model cards** of the ML models in the system;
   - access a **summary of overall system performance** about non-ML components such as **human reviews**.
4. **Walkthrough with an Example Input:**
   - step-by-step demonstration of how the system processes an **actual input**;
   - optionally enable the user to **modify the input** and examine how the system’s response changes.

### 2.2 Explicit non-capabilities / deferred items (observation)

§4 identifies Automation, Maintenance, and Security as challenges. Maintenance notes that systems evolve as models are retrained/replaced and that easier **maintenance and provenance** of System Cards is future work—not a defined card field. Security may **restrict** what is disclosed by stakeholder. Fairness, robustness, and accountability integration are planned future work, not required sections of the §3 model.

---

## 3. Checklist interpretation

Nearest claim-inventory item: **C1** (loosely coupled artifact retention insufficient for triad reconstruction).

| Distinction | Application to System Cards |
|---|---|
| **Documenting an AI system** | Overview page + component diagram + links to model cards. |
| **Documenting deployment / operational composition** | Diagram of how modalities flow through components to a ranking (illustrative); human-review components mentioned. |
| **Documenting evaluation methodology** | “Summary of overall system performance” for non-ML components is named; no structured metrics/evaluation protocol section. |
| **Specific decision episode** | Not defined (no decision identity/outcome record). |
| **Evidence actually relied upon in an individual decision** | Example-input walkthrough demonstrates processing of *an* input; not a retained reliance record for a historical decision. |
| **Policy or legal justification** | Not structured in §3. |
| **Temporal reconstruction** | “Current version” on overview; update/provenance of cards deferred to future work (§4). |

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside the legitimate purpose of a system-level transparency documentation proposal.

Scores are independent of other SUT reviews.

### System state — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | High-level component diagram communicating how components process inputs to achieve functionality; walkthrough of processing an actual input (§3; Fig. 1). |
| **Justification** | Partial support for documenting **architectural / processing composition** of an ML system as presented to stakeholders. |
| **Why not higher** | No first-class snapshot of operational system state bound to a decision episode. Free-text description/purpose and illustrative diagrams are not systematic decision-state records. |
| **Confidence** | High |

### Decision process — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Step-by-step demonstration of how the system processes an example input; optional interactive modification of input to observe response change (§3). |
| **Justification** | Partial: an **illustrative processing walkthrough** can convey the system’s operational path for a sample input. |
| **Why not higher** | Demonstration ≠ retained multi-step decision process for a legally relevant episode (authorization gates, human acceptance, criteria evaluation). No decision-episode log. |
| **Confidence** | High |

### Evidence — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Abstract/§1: communicate how data and protected information are used; §3 walkthrough uses an actual input; interactive access to constituent model cards (which may document train/eval data—Model Cards themselves are not System Cards content beyond the link). |
| **Justification** | Partial support for documenting **what kinds of inputs/data the system uses** at a descriptive/system level. |
| **Why not higher** | No structure for evidence available vs relied upon in a concrete decision (IC-10/IC-11), nor excluded evidence (IC-12). Example inputs are pedagogical, not decision evidence packages. |
| **Confidence** | High |

### Rules — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | §3 does not define governing policy, applicable rules, constraints, or authorization criteria as System Card sections. Background mentions policy-makers as definition stakeholders (§2.3); not a card field. |
| **Justification** | Not addressed as reconstructable decision rules/authorization structure. |
| **Why not higher** | Crediting narrative purpose text or external product policies would violate the evaluation boundary. |
| **Confidence** | High |

### Human context — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Overview includes **authors**; non-ML components such as **human reviews**; stakeholders include end users interested in which parts of their information are used and opt-out (§3; §4 Security discussion). |
| **Justification** | Partial support for documenting card authors and the presence of human-review components / user-facing information concerns. |
| **Why not higher** | No first-class decision actors, authority, or multi-party authorization model for a decision episode. |
| **Confidence** | High |

### Temporal continuity — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Overview includes **current version** (§3). §4 Maintenance: systems evolve as models are retrained/replaced; cards should reflect changes; easier maintenance and **provenance** of System Cards is future work. |
| **Justification** | Partial: version labeling of the *documentation artefact* is named; temporal binding of decisions is not. |
| **Why not higher** | No decision-time binding of system/model/criteria versions; provenance/maintenance solutions are explicitly undeveloped in the proposal. |
| **Confidence** | High |

### Checklist marks (original System Cards proposal only)

Exactly one mark per item.

| ID | Mark | Notes |
|---|---|---|
| IC-01 | FAIL | No decision-episode identity |
| IC-02 | FAIL | No decision outcome record |
| IC-03 | FAIL | Card “current version” ≠ decision time |
| IC-04 | PARTIAL | Authors; human-review components; not decision principals |
| IC-05 | FAIL | Not defined |
| IC-06 | FAIL | Not defined |
| IC-07 | FAIL | Not defined |
| IC-08 | FAIL | Not defined |
| IC-09 | FAIL | Not defined |
| IC-10 | PARTIAL | Example inputs / data-use description only |
| IC-11 | FAIL | No reliance distinction |
| IC-12 | FAIL | Not defined |
| IC-13 | PARTIAL | Via linked model cards / version string—not decision-bound |
| IC-14 | N/A | Outside System Cards purpose as proposed |
| IC-15 | FAIL | Not tool-call decision structure |
| IC-16 | PARTIAL | Multi-component diagram may show non-ML pieces |
| IC-17 | FAIL | Not defined |
| IC-18 | FAIL | Not defined |
| IC-19 | PARTIAL | Current version; maintenance deferred |
| IC-20 | N/A | Outside purpose as proposed |
| IC-21 | FAIL | Not defined |
| IC-22 | N/A | Outside purpose as reviewed |
| IC-23 | PARTIAL | Component/dependency overview; card provenance future work |
| IC-24 | PARTIAL | Diagram of multi-component processing path |

**Triad roll-up (System Cards alone, base profile for legally relevant AI-supported decisions):**

| Target | Result |
|---|---|
| Authorization reconstructable | FAIL |
| Justification reconstructable | FAIL |
| Validity reconstructable | FAIL |
| Faithful reconstruction (base) | FAIL |

---

## 5. Evaluation boundary

Only concepts explicitly defined by the original System Cards proposal (§3) receive credit:

- Narrative description/purpose, authors, current version, component diagram, links to model cards, non-ML performance summary, and example-input walkthrough may be credited **only as structured by §3**.
- Generic free-text must **not** be treated as first-class support for decision identity, decision evidence, authorization, legal justification, or decision continuity.
- Instagram pilots, Gemini docs, later Google/OpenAI system-card reports, and organization templates receive **no** credit.
- Implementation practice must **not** influence scoring.
- Cited Model Cards/Datasheets/FactSheets are prior art; only the **incorporation by reference** of model cards into System Card exploration is in scope—and that still does not create decision-episode structure.

---

## 6. Threats to validity

- The proposal is a short foundational note; the information model is intentionally incomplete (“lay a foundation”).
- Security may withhold system detail by design (§4)—reconstruction completeness is not a goal.
- Figure 1 is fictional/illustrative; must not be read as a mandatory schema.
- Misattribution risk: “system cards” later used by many vendors for product safety reports that are **not** this SUT.
- Maintenance/provenance gaps mean even system-documentation freshness is not guaranteed by the proposal.

---

## 7. Remaining uncertainty

- Whether a later, more complete Meta/industry System Card schema expands reconstructable fields—would require a separate version-pinned review.
- Composition with decision records / policy logs remains out of scope.
- Claim **C1** receives unit-level illustration only; aggregate status is **not** updated.

---

## 8. Overall assessment

**Procope et al. (Meta AI, 2022) introduce System Cards as transparency documentation for multi-component ML systems:** overview (purpose, authors, version, component diagram), interactive access to constituent model cards and non-ML performance summaries, and an example-input walkthrough. That addresses a real gap relative to model-only or dataset-only cards for *system understanding*.

Against the reconstruction checklist, System Cards **do not** systematically preserve decision episodes, relied-upon evidence, authorization/policy justification, or decision-time temporal binding. Faithful reconstruction of justification, authorization, and validity for legally relevant AI-supported decisions **fails** for System Cards alone—consistent with unit-level illustration of **C1**.

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims.
