---
id: review-2026-07-29-datasheets-for-datasets
title: "Review: Datasheets for Datasets (Gebru et al., CACM 2021) against reconstruction checklist"
topic: ai-infrastructure-gap
type: review
status: active
created: 2026-07-29
updated: 2026-07-29
tags: [evaluation, datasheets, documentation, datasets, reconstruction]
refs: [gebru2021datasheets]
sut: "Gebru et al., Datasheets for Datasets (Communications of the ACM, Dec 2021) — original proposal, questionnaire, and official appendix"
checklist_version: "0.1.0"
review_kind: complete
primary_sources_available: true
related_claims: [C1, C3]
---

# Review

## Bibliographic Information

**Title:** Datasheets for Datasets

**Authors:** Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford

**Venue:** *Communications of the ACM*, Vol. 64, No. 12, pp. 86–92, December 2021

**Version pin:** Final published CACM version, DOI [10.1145/3458723](https://doi.org/10.1145/3458723), including the official online appendix referenced by that article (example datasheet for Pang and Lee’s polarity dataset). Earlier arXiv drafts (e.g. [1803.09010](https://arxiv.org/abs/1803.09010)) are treated as development history only and are **not** the scored SUT when they diverge from the CACM text.

**DOI / URL:**

- Article: https://doi.org/10.1145/3458723
- Open HTML: https://cacm.acm.org/research/datasheets-for-datasets/
- Appendix (via ACM DL DOI page): https://dl.acm.org/doi/10.1145/3458723

**Primary sources inspected:**

| Source | Role |
|---|---|
| CACM 2021 article body | Objectives; development process; full questionnaire/workflow; impact/challenges |
| Official CACM appendix (polarity dataset example) | Illustrative answers; confirms questions may be unanswered (“Unknown…”) |

**Primary source availability:** Sufficient for a complete review (published questionnaire retrieved in full; appendix role confirmed by the article).

**Not SUT:** Hugging Face dataset cards; Data Statements; Dataset Nutrition Labels; Factsheets; organization-specific templates; regulatory documentation frameworks; custom metadata systems; implementation platforms; external lineage/audit tooling; Model Cards (cited as follow-on, not scored here).

**Pre-scoring notes:**

- **Design intent:** document *datasets as artefacts* through a reflective questionnaire—not decision episodes.
- **Credit rule:** prompts score only for information they explicitly ask or systematically structure; “Any other comments?” and voluntary elaboration earn no extra credit; skipping inapplicable questions is explicit—optional population ≠ systematic reconstruction support.
- **Likely N/A / FAIL:** decision identity/outcome; authorization; decision-bound reliance; prompts (IC-14).
- **Threats (preview):** non-prescriptive questions; dynamic datasets; documentation ≠ binding.

---

## 1. Design intent

Datasheets for Datasets propose that every dataset be accompanied by a **datasheet** documenting motivation, composition, collection process, recommended uses, and related information, by analogy with electronics component datasheets (CACM Objectives / introduction).

Primary objectives:

1. **Dataset creators** — encourage careful reflection on creating, distributing, and maintaining a dataset (assumptions, risks, implications of use).
2. **Dataset consumers** — supply information needed for informed selection and to avoid unintentional misuse.

Secondary objective: aid reproducibility by enabling others to create alternative datasets with similar characteristics when the original is inaccessible.

The authors state questions are **not intended to be prescriptive**, will vary by domain and organizational workflow, are **not a checklist**, and that creating a datasheet is **not intended to be automated**. Not all questions apply to all datasets; inapplicable ones should be skipped; creators should answer as many as possible rather than skip datasheet creation entirely (Questions and Workflow).

**Intent for this review:** evaluate whether this **original questionnaire information model** preserves information needed for faithful reconstruction of historically situated, legally relevant AI-supported *decisions*—not whether datasheets improve dataset transparency or selection in general.

---

## 2. Observed capabilities

(First-class / documented in the CACM proposal only.)

### 2.1 Questionnaire sections (dataset lifecycle grouping)

| Section | What the prompts systematically structure |
|---|---|
| **Motivation** | Purpose/task/gap; who created and for which entity; funding; optional other comments |
| **Composition** | Instance types and counts; sample vs complete; contents/features; labels; missing fields; relationships; recommended splits; noise/errors; external-resource dependence and temporal/archival/license issues; confidentiality/offensiveness; people-related subpopulations, identifiability, sensitive data |
| **Collection process** | Acquisition method; mechanisms; sampling; collectors/compensation; collection timeframe vs instance creation timeframe; ethical review; people-related notice/consent/revocation/impact analysis |
| **Preprocessing/cleaning/labeling** | Whether/how processed; whether raw retained; software availability |
| **Uses** | Prior uses; paper/system repositories; possible tasks; composition/collection factors affecting future uses and mitigations; tasks for which the dataset **should not** be used |
| **Distribution** | Third-party distribution; how/when distributed; DOI; copyright/IP/ToU; third-party restrictions; export/regulatory restrictions |
| **Maintenance** | Hosting/support contact; erratum; update plans/communication; retention limits (people data); older-version support; contribution mechanisms |

### 2.2 Explicit non-capabilities (observation)

The proposal does **not** define: decision-episode identity; records of evidence relied upon in a concrete AI decision; authorization allow/deny structure; governing policy identity/version for a decision; legal justification of an outcome; binding a datasheet answer set to a decision timestamp; or mandatory machine-readable schemas. A separate “Legal and Ethical Considerations” section was **removed** during development in favor of factual prompts integrated into lifecycle sections; creators are not asked to make legal judgments about regulatory compliance as such (Development Process).

Generic “Any other comments?” fields exist in several sections; under the evaluation boundary they do **not** establish first-class support for decision reconstruction categories.

---

## 3. Checklist interpretation

Nearest claim-inventory items: **C1** (loosely coupled artifact retention insufficient for triad reconstruction) and **C3** (temporal binding of criteria/versions)—Datasheets structure *dataset* lifecycle and update/version hosting questions, not decision-time binding.

| Distinction | Application to Datasheets |
|---|---|
| **Dataset artefact documentation** | Composition/Distribution describe what the dataset is and how it is released. |
| **Creation and maintenance documentation** | Collection, Preprocessing, Maintenance structure how the dataset was built and how it will be updated/hosted. |
| **Provenance and intended use (of the dataset)** | Collection/Preprocessing document creation provenance of the *dataset*; Uses documents recommended/non-recommended *dataset* tasks—not legal justification of a decision. |
| **Evidence relied upon in a concrete AI decision** | Not structured. A datasheet may describe a dataset that *later* appears in a decision, but does not record reliance for an episode. |
| **Specific decision episode** | Not structured (no decision identity, outcome, or decision-time binding). |
| **Legal or policy justification** | Factual GDPR/sensitivity/export prompts about the dataset ≠ justification/authorization of a decision under then-applicable rules. |
| **Preserving validity over time** | Maintenance/update/older-version and external-resource constancy prompts address *dataset* obsolescence—not validity of a historical decision under then-applicable constraints. |

---

## 4. Scored criteria

Scale: 0 = Not addressed; 1 = Mentioned or partially supported; 2 = Substantially supported; 3 = Explicitly and systematically supported.  
N/A = outside the legitimate purpose of a dataset-documentation questionnaire.

Scores are independent of other SUT reviews. Optional/skip-able answers do not raise scores above what the prompts structurally define for *dataset* documentation; they never invent decision-episode structure.

### System state — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | Composition documents dataset contents, splits, and external dependencies; Collection documents acquisition context. No prompt asks for operational system state at a decision episode. |
| **Justification** | Decision-time system state is not addressed. |
| **Why not higher** | Dataset composition is artefact description, not reconstructable system state bound to a decision. |
| **Confidence** | High |

### Decision process — **Score: 0**

| Field | Content |
|---|---|
| **Evidence** | Workflow groups questions by dataset lifecycle stages for *datasheet authors* (Questions and Workflow). Uses asks about tasks the dataset has been or should/should not be used for. |
| **Justification** | No decision-episode process, gates, or authorization/justification workflow is defined. |
| **Why not higher** | Creator reflection workflow ≠ retained decision process for AI-supported outcomes. |
| **Confidence** | High |

### Evidence — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Composition systematically asks what instances represent, what each consists of, labels/targets, missing information, relationships, noise, and external resources; Collection/Preprocessing document how those contents were acquired and transformed. |
| **Justification** | Partial support for documenting a **dataset artefact** that may later serve as training/evaluation material—i.e., background about a potential evidence *source*, not evidence used in a decision. |
| **Why not higher** | No structure for evidence actually available vs relied upon in a concrete decision (IC-10/IC-11), nor for decision-level excluded evidence (IC-12). Voluntary narrative cannot upgrade this. |
| **Confidence** | High |

### Rules — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Uses asks what tasks the dataset could be used for and **tasks for which it should not be used**, plus composition/collection factors that might cause unfair treatment or other risks and possible mitigations. Distribution asks about licenses/ToU and export/regulatory restrictions on the dataset. |
| **Justification** | Partial: recommended/non-recommended *dataset uses* and distribution constraints are systematically prompted as documentation about the artefact. |
| **Why not higher** | Not governing policy, applicable rule paths, or authorization constraints for a decision episode (IC-06–IC-09). “Should not be used” is consumer guidance, not an authorization decision record. |
| **Confidence** | High |

### Human context — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Motivation: who created the dataset and on behalf of which entity; funding. Collection: who was involved and compensation; people-related notice, consent, revocation, impact analysis. Composition (people-related): subpopulations, identifiability, sensitive data. Maintenance: owner/curator contact. |
| **Justification** | Partial support for documenting **dataset creation/stewardship actors** and data-subject process facts when the dataset relates to people. |
| **Why not higher** | Not decision-episode principals, multi-party authority, or authorization responsibility for an outcome. |
| **Confidence** | High |

### Temporal continuity — **Score: 1**

| Field | Content |
|---|---|
| **Evidence** | Collection: timeframe of data collection vs creation timeframe of instance data. Composition: whether linked external resources will exist/remain constant over time; archival versions. Distribution: when the dataset will be distributed; DOI. Maintenance: update frequency/communication; whether older versions remain supported; retention limits for people-related data. Impact section: if a dataset changes infrequently, updated versions should get updated datasheets. |
| **Justification** | Partial support for documenting **dataset lifecycle time and version-hosting plans**—relevant to knowing which dataset snapshot a datasheet describes. |
| **Why not higher** | Does not bind dataset (or criteria) versions to a decision time (IC-03/IC-07/IC-19 as decision temporality). Answers are skip-able; no mandatory as-of/bitemporal decision model. Dynamic datasets are acknowledged as a challenge, not solved. |
| **Confidence** | High |

### Checklist marks (original Datasheets proposal only)

Exactly one mark per item.

| ID | Mark | Notes |
|---|---|---|
| IC-01 | FAIL | No decision-episode identity |
| IC-02 | FAIL | No decision outcome |
| IC-03 | FAIL | Collection/distribution times ≠ decision time |
| IC-04 | PARTIAL | Creators/collectors/stewards; not decision actors |
| IC-05 | FAIL | Not defined for decisions |
| IC-06 | FAIL | Recommended dataset uses ≠ governing policy |
| IC-07 | FAIL | No policy version for decisions |
| IC-08 | FAIL | Not defined |
| IC-09 | PARTIAL | “Should not be used” / risk mitigations for dataset consumers only |
| IC-10 | PARTIAL | Documents dataset contents, not decision-used evidence |
| IC-11 | FAIL | No reliance distinction for decisions |
| IC-12 | FAIL | Instance “missing information” ≠ excluded decision evidence |
| IC-13 | N/A | Outside datasheet purpose (model version) |
| IC-14 | N/A | Outside datasheet purpose |
| IC-15 | FAIL | Not decision tool-call structure |
| IC-16 | PARTIAL | External resources linked by the dataset only |
| IC-17 | FAIL | Not defined |
| IC-18 | PARTIAL | Motivation/reflection prompts; not decision assumptions |
| IC-19 | PARTIAL | Dataset collection/maintenance timeframes; not decision as-of |
| IC-20 | FAIL | Dataset sensitivity/export facts ≠ decision legal context |
| IC-21 | FAIL | Not defined for decision integrity |
| IC-22 | N/A | Outside purpose as reviewed |
| IC-23 | PARTIAL | Collection/preprocessing document dataset creation provenance |
| IC-24 | PARTIAL | Instance relationships / external links; not decision lineage |

**Triad roll-up (Datasheets alone, base profile for legally relevant AI-supported decisions):**

| Target | Result |
|---|---|
| Authorization reconstructable | FAIL |
| Justification reconstructable | FAIL |
| Validity reconstructable | FAIL |
| Faithful reconstruction (base) | FAIL |

---

## 5. Evaluation boundary

Only concepts explicitly defined by the original Datasheets for Datasets proposal receive credit:

- Questionnaire prompts receive credit only for information they **explicitly require or systematically structure**.
- An item does **not** receive credit merely because an author could voluntarily add it (including “Any other comments?”).
- Generic narrative fields are **not** first-class support for decision identity, decision evidence, legal justification, authorization, or temporal continuity of decisions.
- Later templates, industrial implementations, Hugging Face dataset cards, Data Statements, and organization-specific extensions receive **no** credit.
- Implementation practice (how completely teams fill datasheets) must **not** influence scoring.
- The official appendix illustrates answering; example completeness does **not** expand the information model.

---

## 6. Threats to validity

- Questions are explicitly non-prescriptive and skip-able; scored “structure” is an upper bound on what a filled datasheet *might* contain, not a guarantee of retention.
- Dynamic datasets are called out as difficult; recommendation to update datasheets is guidance, not a binding temporal mechanism.
- Appendix answers include “Unknown to the authors of the datasheet,” showing documentation gaps are expected—must not be read as systematic completeness.
- Impact/challenges discuss industry pilots and follow-on artefacts; those are **out of SUT** and must not inflate scores.
- Preprint appendices (e.g. LFW examples on arXiv) are not used to redefine the CACM information model.

---

## 7. Remaining uncertainty

- Whether composition of Datasheets + Model Cards + decision records could close triad gaps is a separate composition evaluation.
- How DOI + maintenance-of-older-versions practices behave empirically is outside this proposal-only review.
- Claims **C1**/**C3** receive unit-level illustration only; aggregate claim status is **not** updated here.

---

## 8. Overall assessment

**Gebru et al. (CACM 2021) systematically structure documentation of datasets as artefacts**—motivation, composition, collection, preprocessing, intended/non-intended uses, distribution, and maintenance—including creation-oriented provenance and lifecycle/update questions. That serves transparency between dataset creators and consumers.

Against the reconstruction checklist, Datasheets **do not** document specific decision episodes, evidence actually relied upon in a concrete AI decision, legal or policy justification of outcomes, or authorization. Temporal prompts partially address **dataset** timeframe and version hosting, not decision-time validity binding. Faithful reconstruction of justification, authorization, and validity for legally relevant AI-supported decisions **fails** for Datasheets alone.

This aligns with unit-level illustration of **C1** (dataset documentation artefacts ≠ sufficient decision-reconstruction structure) and only a weak, unbound contribution to **C3**’s temporal-binding concern at the dataset layer.

**Not updated:** comparison matrix; reconstruction evaluation dataset; aggregate claims.
