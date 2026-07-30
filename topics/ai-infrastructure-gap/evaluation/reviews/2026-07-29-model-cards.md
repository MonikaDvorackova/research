---
id: review-2026-07-29-model-cards
title: "Review: Model Cards (Mitchell et al., FAT* 2019) against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, model-cards, documentation, transparency, reconstruction]
refs: [mitchell2019modelCards]
sut: "Mitchell et al., Model Cards for Model Reporting (FAT* 2019) — original proposal and documented information model"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C1, C3]
---

# Review

## Bibliographic Information

**Title:** Model Cards for Model Reporting

**Authors:** Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, Timnit Gebru

**Venue:** FAT* ’19: Conference on Fairness, Accountability, and Transparency, January 29–31, 2019, Atlanta, GA, USA. ACM.

**Version pin:** ACM published proceedings version (10 pages), DOI [10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596); arXiv preprint [1810.03993](https://arxiv.org/abs/1810.03993) inspected as accessible full text of the same work.

**DOI / URL:**

- DOI: https://doi.org/10.1145/3287560.3287596
- PDF (arXiv): https://arxiv.org/pdf/1810.03993.pdf

**Primary sources inspected:**

| Source | Role |
|---|---|
| Mitchell et al., FAT* 2019 full paper (ACM / arXiv 1810.03993) | Design intent; §4 Model Card sections (information model); §5 worked examples (Figures 2–3); discussion/limitations |
| In-paper Figure 1 | Summary of proposed sections and prompts |
| In-paper Figures 2–3 | Example cards (smile detector; Perspective TOXICITY) |

**Supplementary material:** The paper does **not** cite a separate official supplementary package required to define the information model. Worked examples are embedded as figures in the main text. No external supplement was required for this review.

**Primary source availability:** Sufficient for a complete review.

**Not SUT:** Hugging Face model-card templates; Google internal deployments; organization-specific templates; regulatory adaptations; AI platform implementations; Datasheets/Nutrition Labels/Data Statements/Factsheets (cited as complementary, not scored as Model Cards content).

**Pre-scoring notes:**

- **Design intent:** stakeholder-facing documentation of *trained model* characteristics—not retention of decision-episode knowledge.
- **First-class vs later practice:** Only §4 section prompts and what the paper explicitly places in cards receive credit.
- **Likely N/A:** IC-14 prompts (not a proposed card field in this 2019 proposal); IC-01–IC-03 as *decision-episode* identifiers (outside purpose); authorization policy engines.
- **Threats (preview):** Flexible/non-formalized cards; integrity depends on creators; documentation ≠ bound decision records.

---

## 1. Design intent

The paper proposes **model cards**: short (one-to-two-page) documents that **accompany released trained machine learning models** to report performance characteristics, intended use context, evaluation procedures, and related information (Abstract; §1).

Goals include clarifying intended use cases, discouraging use in unsuitable contexts, supporting stakeholder comparison of models (practitioners, developers, policymakers, organizations, impacted individuals), and encouraging disaggregated (unitary and intersectional) evaluation relevant to fairness and inclusion (§1; §3).

Model cards are positioned as **complements** to dataset documentation paradigms (e.g., Datasheets for Datasets), focusing on **trained model** characteristics rather than dataset-only reporting (§1). Sections are **suggested, not exhaustive**, and “may be tailored depending on the model, context, and stakeholders” (§4). The authors state cards are unlikely to be formalized enough near-term to prevent misleading representations and should be one transparency tool among many (§6).

**Intent for this review:** evaluate whether the **original Model Cards information model** preserves information needed for faithful reconstruction of historically situated, legally relevant AI-supported *decisions*—not whether model cards improve model transparency or fairness reporting in general.

---

## 2. Observed capabilities

(First-class / documented in the paper only.)

### 2.1 Proposed card sections (Figure 1 / §4)

| Section | Documented content prompts |
|---|---|
| **Model Details** | Developer person/org; model date; model version; model type; training algorithms/parameters/fairness constraints/features; paper/resources; citation; license; contact |
| **Intended Use** | Primary intended uses; primary intended users; out-of-scope use cases |
| **Factors** | Relevant factors; evaluation factors (groups, instrumentation, environment, etc.) |
| **Metrics** | Performance measures; decision thresholds; approaches to uncertainty/variability |
| **Evaluation Data** | Datasets; motivation; preprocessing |
| **Training Data** | Ideally mirror evaluation data; if not possible, minimal allowable information (e.g., distributions over factors) |
| **Quantitative Analyses** | Unitary and intersectional results |
| **Ethical Considerations** | Sensitive data; human-life stakes; mitigations; risks/harms; fraught use cases |
| **Caveats and Recommendations** | Residual concerns; missing groups; further testing; ideal eval-dataset characteristics |

Optional additional detail mentioned (not required sections): interpretability approaches, stakeholder-relevant explanations, privacy approaches used in training/serving (§4).

### 2.2 Explicit non-capabilities (observation)

The proposal does **not** define: decision-episode identity; binding of a card to a specific authorization/justification event; durable logs of inputs/outputs for individual decisions; governing organizational policy identity/version; relied-upon vs available evidence for a decision; legal jurisdiction objects; or mandatory machine-readable schemas.

---

## 3. Checklist interpretation

Nearest claim-inventory items: **C1** (loosely coupled artifact retention insufficient for triad reconstruction) and **C3** (temporal binding of criteria/model versions)—Model Cards propose **model date/version** documentation but not decision-time binding.

Interpretive distinctions:

| Distinction | Application to Model Cards |
|---|---|
| **Model documentation vs decision reconstruction** | Cards document a *released model’s* characteristics and evaluation; they do not record a *decision episode*. |
| **Intended use vs authorization** | Out-of-scope uses and ethical caveats guide suitable deployment; they are not authorization decisions under governing policy. |
| **Disaggregated metrics vs justification evidence** | Unitary/intersectional metrics characterize model behaviour on evaluation sets; they are not the evidence package for a particular historical decision. |
| **Model version on a card vs IC-07/IC-13 binding** | Card fields support identifying *which model version the card describes*; they do not, by themselves, bind that version to a decision at IC-03. |

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside the legitimate purpose of a model-reporting documentation proposal.

Scores are independent of other SUT reviews. Only concepts in the FAT* 2019 proposal receive credit.

### System state — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | Factors may include environmental/instrumentation conditions affecting *model performance* (§4.3); Training/Evaluation Data describe datasets used to build/test the model (§4.5–4.6). No section defines system state at a decision episode. |
| **Justification** | Not addressed as reconstructable decision-time system state. |
| **Why not higher** | Environment/instrumentation prompts concern evaluation conditions for the model artifact, not retained state of an operational decision. |
| **Confidence** | High |

### Decision process — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | Cards accompany trained models to inform suitability and stakeholder decisions *about adopting/using a model* (§3); they do not define steps, gates, or records of an AI-supported business/legal decision process. |
| **Justification** | Decision-process reconstruction for checklist episodes is not addressed. |
| **Why not higher** | “Decision thresholds” (§4.4) are model-output operating points for metrics reporting, not a decision-process log. |
| **Confidence** | High |

### Evidence — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Evaluation Data and Training Data sections; Quantitative Analyses over factors; Metrics including uncertainty/confidence intervals (§4.4–4.7). |
| **Justification** | Partial support for documenting *evaluation/training evidence about the model* (datasets, metrics, disaggregated results)—useful background if that model later participates in decisions. |
| **Why not higher** | Not a first-class model of evidence used or relied upon *in a decision episode* (IC-10/IC-11). No excluded-evidence construct for decisions (IC-12). |
| **Confidence** | High |

### Rules — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Intended Use (including out-of-scope uses) (§4.2); Metrics decision thresholds (§4.4); Ethical Considerations and Caveats (§4.8–4.9); stakeholder note that knowledgeable users may add “additional rules and constraints” when curating models (§3)—aspirational, not a card schema for governing policy. |
| **Justification** | Partial: cards systematically prompt use-scope boundaries and threshold choices as reporting content, which are weak forms of normative guidance about *model use*. |
| **Why not higher** | No governing policy identity/version, applicable rule paths, or authorization constraints as reconstructable decision structure (IC-06–IC-09). Out-of-scope text is documentation, not an authorization engine. |
| **Confidence** | High |

### Human context — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Model Details: person/organization developing the model (§4.1); Intended Use: primary intended users (§4.2); Factors: demographic/phenotypic *evaluation groups* (§4.3); Ethical Considerations: impacted stakes (§4.8). |
| **Justification** | Partial support for documenting developers, intended user classes, and evaluation populations. |
| **Why not higher** | No first-class actors/authority for a decision episode; evaluation “groups” are fairness analysis categories, not decision principals. |
| **Confidence** | High |

### Temporal continuity — **Score: 2**

| Field | Content |
|---|---|
| **Evidence** | Model Details explicitly include **model date** and **model version**, including how a version differs from previous versions (§4.1). Example toxicity card contrasts TOXICITY v.1 and v.5 and stresses updating cards with each release (§5.2). |
| **Justification** | Substantial, systematic support for documenting **which model version** a card describes and **when** it was developed—directly relevant to model-version awareness (checklist IC-13-like concerns at the *artifact documentation* layer). |
| **Why not higher** | Does not provide decision-time binding of that version to an episode (IC-03/IC-07/IC-19 as decision temporality). No bitemporal policy/criteria axes. Card freshness depends on release practice (§5.2; §6). |
| **Confidence** | High |

### Checklist marks (original Model Cards proposal only)

| ID | Mark | Notes |
|---|---|---|
| IC-01 | FAIL | No decision-episode identity |
| IC-02 | FAIL | No decision outcome record |
| IC-03 | FAIL | Model date ≠ decision time |
| IC-04 | PARTIAL | Developers / intended users only |
| IC-05 | FAIL | Not defined |
| IC-06 | FAIL | Intended use ≠ governing policy |
| IC-07 | FAIL | Policy version not defined |
| IC-08–IC-09 | FAIL/PARTIAL | Thresholds / out-of-scope text only |
| IC-10 | PARTIAL | Train/eval datasets for the model |
| IC-11–IC-12 | FAIL | Not defined |
| IC-13 | PASS | Model version (and type/date) as proposed card fields |
| IC-14 | **N/A** | Outside 2019 Model Cards purpose/fields |
| IC-15–IC-16 | FAIL | Not defined as decision tool/service bindings |
| IC-17 | PARTIAL | Confidence intervals / uncertainty for *metrics* |
| IC-18 | PARTIAL | Assumptions via model details / ethical narrative |
| IC-19 | PARTIAL | Model date; not decision as-of frame |
| IC-20 | **N/A**/PARTIAL | Ethical considerations prompts; not legal jurisdiction objects |
| IC-21–IC-22 | FAIL | Integrity/signatures of cards not specified |
| IC-23–IC-24 | PARTIAL | Pointers to train/eval data; not lineage graphs |

**Triad roll-up (Model Cards alone, base profile for legally relevant AI-supported decisions):**

| Target | Result |
|---|---|
| Authorization reconstructable | **FAIL** |
| Justification reconstructable | **FAIL** |
| Validity reconstructable | **FAIL** |
| Faithful reconstruction (base) | **FAIL** under checklist §8.3 |

Model Cards may still inform *ex ante* suitability assessment of a model; that is outside faithful *historical decision* reconstruction.

---

## 5. Evaluation boundary

Only concepts explicitly defined by the original Model Cards proposal receive credit:

- §4 section prompts, Figure 1 summary, and in-paper example card contents may be credited **as documentation fields the proposal defines**.
- Hugging Face templates, Google deployments, organizational checklists, regulatory model-card variants, and platform auto-generated cards receive **no** credit.
- Datasheets and related dataset docs are complementary citations, not Model Cards capabilities.
- Implementation practice (whether organizations fill cards well) must **not** influence scoring; scores reflect the proposal’s information model expressiveness for reconstruction.

---

## 6. Threats to validity

- The paper itself states cards are flexible, non-exhaustive, and unlikely to be formalized enough to prevent misleading representations (§4; §6)—expressiveness upper-bounds are soft.
- Worked examples illustrate possible content; they are not a normative schema language.
- Scoring documentation *fields* must not be confused with claiming that a card is retained and bound at decision time (retention/binding are outside the proposal).
- arXiv vs ACM pagination/wording drift is minor for this review; DOI version is authoritative for citation.

---

## 7. Remaining uncertainty

- Whether a *composition* of Model Cards + decision records + policy logs could satisfy the triad is out of scope (composition review).
- Relationship to later “model card” ecosystems is excluded by boundary; a separate review would be required to score those.
- Claims **C1**/**C3** receive unit-level illustration here but are **not** updated in aggregate inventories by this task.

---

## 8. Overall assessment

**Mitchell et al. (FAT* 2019) systematically propose a documentation information model for reporting trained ML models**—especially model identity/version/date, intended use, factors, metrics (including thresholds and uncertainty), train/eval data pointers, disaggregated quantitative analyses, and ethical caveats. That is valuable transparency for *model release and adoption*.

Against the repository reconstruction checklist, Model Cards **do not** systematically preserve decision-episode system state, decision process, decision-bound evidence, authorization rules, or decision actors. Temporal support is **substantial for documenting model version/date**, but **not** for binding criteria to a historical decision. Faithful reconstruction of justification, authorization, and validity for legally relevant AI-supported decisions **fails** for Model Cards alone.

This is consistent with treating original Model Cards as unit-level evidence toward **C1** (documentation artifacts ≠ sufficient reconstruction structure) and as only a partial, unbound contribution to **C3**’s model-version concern.

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims.
