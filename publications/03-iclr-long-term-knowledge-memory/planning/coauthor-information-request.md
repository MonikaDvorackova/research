---
id: pub-03-ltkm-coauthor-information-request
title: "Coauthor information request — freeze Research Spec before drafting"
type: research-notes
status: active
created: 2026-07-31
updated: 2026-07-31
source: research-specification-v0.1.md
---

# Coauthor information request

**Purpose:** Single structured review cycle to freeze Publication 03’s scientific specification.  
**Source of gaps:** [`research-specification-v0.1.md`](research-specification-v0.1.md).  
**Rule:** Complete every field. Write precise wording. Do not answer with “TBD later” on **blocking** items.  
**Manuscript drafting:** Not authorized until §9 checklist is approved.

**Respondents:** fill names below.

| Role | Name | Affiliation | Date |
|---|---|---|---|
| Collaborator A (tech lead / method) | | | |
| Collaborator B (benchmark / experiments) | | | |
| Monika (conceptual / integration) | Monika Dvořáčková | | |

---

## Section 1 — Scientific object

**Spec ref:** §1.3, §5.

### Q1.1 Primary scientific object (select exactly one)

- [ ] Learning method  
- [ ] Memory representation / organization  
- [ ] Inference method  
- [ ] Retrieval / update policy  
- [ ] Benchmark  
- [ ] Evaluation methodology  
- [ ] Interaction protocol  
- [ ] Other: _______________

**Answer (one sentence):**  
> 

### Q1.2 If a secondary object exists, justify coupling in ≤5 lines (or write “none”)

> 

### Q1.3 One-sentence ML claim (non-engineering)

> 

### Q1.4 Venue confirmation

- [ ] ICLR remains the target  
- [ ] Reconsider venue because contribution is primarily systems/benchmark  

**If reconsider:** preferred venue: _______________

### Q1.5 Problem definition (one paragraph)

Must name: (a) agent/task setting; (b) what “long-term knowledge consistency” measures; (c) what fails under existing approaches in *this* team’s framing.

> 

### Q1.6 Gap evidence basis

Insufficiency of existing agent memory is:

- [ ] Assumed from prior literature (list must-cites in Q1.7)  
- [ ] Shown in an internal pilot (cite path/result)  
- [ ] To be demonstrated on the new benchmark only  

### Q1.7 Must-cite / closest systems (list)

| System / paper | Why it is not sufficient (one line) |
|---|---|
| | |
| | |
| | |

---

## Section 2 — Research question

**Spec ref:** §2–§3.

### Q2.1 Final primary research question (exact wording)

Approve Spec v0.1 RQ-A, or paste replacement:

- [ ] Approve Spec v0.1 RQ-A as written  
- [ ] Replace with:

> 

### Q2.2 Definition of “long-term knowledge consistency” (exact wording)

> 

### Q2.3 Primary hypothesis (exact wording)

> 

### Q2.4 H0 (exact wording)

> 

### Q2.5 H1 (exact wording)

> 

### Q2.6 Rejection criterion for H1 (exact rule)

Include: primary metric name; comparison baseline(s); indifference margin and/or significance rule; whether H1 applies to aggregate only or each task family.

> 

### Q2.7 If H1 fails, paper policy (select one)

- [ ] Report negative / ablation-driven reformulation  
- [ ] Pivot to benchmark-only contribution  
- [ ] Withdraw ICLR target  
- [ ] Other: _______________

---

## Section 3 — Proposed method

**Spec ref:** §6.

### Q3.1 System identity

| Field | Answer |
|---|---|
| System name | |
| Codebase URL / path | |
| Integration target (agent stack) | |
| What is novel beyond the five-layer taxonomy | |

### Q3.2 Complete method description (≤1 page equivalent; paste or link)

Mechanisms, algorithms, learning objectives, orchestration. Not marketing prose.

> 

### Q3.3 Knowledge lifecycle definition

| Operator | Trigger | Effect | Invariant |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Q3.4 Read / write / update rules

| Rule type | Specification |
|---|---|
| Write path (what gets stored when) | |
| Read / retrieval policy | |
| Conflict resolution | |
| Update / revise / deprecate | |

### Q3.5 Learned vs rule-based vs prompt-only

| Mechanism | Learned / Rule / Prompt / N/A | Notes |
|---|---|---|
| Working | | |
| Session | | |
| Long-term | | |
| Graph | | |
| Archive | | |
| Lifecycle transitions | | |

### Q3.6 Component status

| Component | Conceptual only | Implemented | Future work |
|---|---|---|---|
| Working | [ ] | [ ] | [ ] |
| Session | [ ] | [ ] | [ ] |
| Long-term | [ ] | [ ] | [ ] |
| Graph | [ ] | [ ] | [ ] |
| Archive | [ ] | [ ] | [ ] |
| Lifecycle engine | [ ] | [ ] | [ ] |

### Q3.7 Explicit assumptions (observability, tools, frozen model, etc.)

> 

---

## Section 4 — Benchmark

**Spec ref:** §7.

### Q4.1 Benchmark identity

| Field | Answer |
|---|---|
| Name | |
| Exists already? (yes/no + path/paper) | |
| Owner | |
| Public release plan / license | |

### Q4.2 World generator

| Field | Answer |
|---|---|
| World state schema | |
| Evolution operators | |
| n worlds / horizon / seeds | |
| Generation procedure | |

### Q4.3 Task families (confirm or amend)

| Family | In scope? | Gold-answer rule (exact) | n instances |
|---|---|---|---|
| Current | [ ] Y [ ] N | | |
| Historical | [ ] Y [ ] N | | |
| Conflicting | [ ] Y [ ] N | | |
| Multi-hop | [ ] Y [ ] N | | |
| Temporal | [ ] Y [ ] N | | |
| Other: ___ | [ ] Y [ ] N | | |

### Q4.4 Scoring

| Field | Answer |
|---|---|
| Primary metric | |
| Secondary metrics | |
| Scoring code location | |
| LLM-as-judge for any primary score? (yes/no) | |
| Train / val / test protocol | |

### Q4.5 Fairness vs baselines

| Control | Specification |
|---|---|
| Identical world traces | |
| Context / token budget | |
| Write privileges | |
| Tool access | |
| Other | |

---

## Section 5 — Experiments

**Spec ref:** §8–§9.

### Q5.1 Baselines (committed list)

| Baseline | Family | Will run? | Fair protocol notes |
|---|---|---|---|
| | | [ ] Y [ ] N | |
| | | [ ] Y [ ] N | |
| | | [ ] Y [ ] N | |

### Q5.2 Metrics (aligned with Q2.6 / Q4.4)

| Metric | Primary? | Definition |
|---|---|---|
| | [ ] | |
| | [ ] | |

### Q5.3 Statistical protocol

| Field | Answer |
|---|---|
| Seeds / repeats | |
| CIs | |
| Significance tests | |
| Multiple-comparison policy | |

### Q5.4 Ablations (committed)

| Ablation | Removes / changes | Tests which claim |
|---|---|---|
| | | |
| | | |

### Q5.5 Compute budget

| Field | Answer |
|---|---|
| Models | |
| Decoding settings | |
| Hardware | |
| Approx. runtime / cost | |
| Who runs experiments | |
| Results freeze date | |

### Q5.6 Expected experimental tables / figures

| ID | Content | Owner |
|---|---|---|
| Table 1 | | |
| Table 2 | | |
| Table 3 | | |
| Fig. … | | |

---

## Section 6 — Scientific claims

**Spec ref:** §4, §9.

List every claim the paper intends to make. Claims without experiment+table/figure support = **unsupported** (cannot appear as established in the paper).

| Claim ID | Exact claim sentence | Supporting experiment | Figure | Table | Supported? |
|---|---|---|---|---|---|
| C1 | | | | | [ ] Y [ ] N — unsupported |
| C2 | | | | | [ ] Y [ ] N — unsupported |
| C3 | | | | | [ ] Y [ ] N — unsupported |
| C4 | | | | | [ ] Y [ ] N — unsupported |

### Q6.1 Indispensable contribution (without which there is no paper)

> 

### Q6.2 Contribution inventory mapping to deliverables

| Contribution type | Deliverable by submission | Owner |
|---|---|---|
| Conceptual | | |
| Methodological | | |
| Engineering | | |
| Experimental | | |

---

## Section 7 — Writing ownership

**Spec ref:** author-responsibilities (provisional). Confirm or amend.

| Section | Owner | Reviewers | Dependencies |
|---|---|---|---|
| Abstract | | | Results freeze |
| Introduction | | | RQ/H1/claims freeze |
| Related Work | | | Must-cite list (Q1.7) |
| Problem Formulation | | | Benchmark freeze |
| Design Principles | | | Method freeze |
| Method / Architecture | | | Q3 complete |
| Benchmark | | | Q4 complete |
| Experiments | | | Q5 complete |
| Results | | | Runs complete |
| Discussion | | | Results + claims |
| Conclusion | | | Full draft |
| Appendix | | | |

---

## Section 8 — Infrastructure

| Field | Answer |
|---|---|
| Submission venue | |
| Submission year | |
| Deadline | |
| Author list (order) | |
| Corresponding author | |
| Canonical Overleaf project (URL) | |
| Overleaf owner | |
| Canonical manuscript source (Overleaf / repo Markdown) | |
| Canonical repository branch | |
| Zotero collection name | |
| Zotero owner (dedup / export) | |
| Better BibTeX → `references/bib/library.bib` workflow confirmed? | [ ] Y [ ] N |
| Policy on closed exploratory packages (cr-gap / topic-search) | [ ] Exclude [ ] Cite as prior exploratory [ ] Other |
| Working title / keyword freeze | |

---

## Section 9 — Blocking decisions checklist

Manuscript drafting may begin only when every **blocking** item is `Approved`.

| ID | Decision | Blocking? | Owner | Status |
|---|---|---|---|---|
| B1 | Primary scientific object selected (Q1.1) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B2 | Final RQ wording (Q2.1) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B3 | Consistency definition (Q2.2) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B4 | H0 / H1 / rejection criterion (Q2.3–Q2.6) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B5 | Method beyond taxonomy + lifecycle ops (Q3.1–Q3.4) | **Blocking** | Collab A | [ ] Open [ ] Approved |
| B6 | Component implemented vs future (Q3.6) | **Blocking** | Collab A | [ ] Open [ ] Approved |
| B7 | Benchmark + generator + gold + scoring (Q4) | **Blocking** | Collab B | [ ] Open [ ] Approved |
| B8 | Primary metric + LLM-judge policy (Q4.4) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B9 | Committed baselines + fair protocol (Q5.1, Q4.5) | **Blocking** | Collab B | [ ] Open [ ] Approved |
| B10 | Committed ablations (Q5.4) | **Blocking** | Collab A/B | [ ] Open [ ] Approved |
| B11 | Claim→experiment→table map (Q6) with no unsupported core claims | **Blocking** | Shared | [ ] Open [ ] Approved |
| B12 | H1-failure policy (Q2.7) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B13 | Section ownership table (Q7) | **Blocking** | Shared | [ ] Open [ ] Approved |
| B14 | Venue + year + deadline (Q8) | **Blocking** | Shared | [ ] Open [ ] Approved |
| N1 | Overleaf URL + manuscript SOT | Non-blocking* | Shared | [ ] Open [ ] Approved |
| N2 | Zotero owner + bib workflow | Non-blocking* | Shared | [ ] Open [ ] Approved |
| N3 | Public release / license | Non-blocking | Collab B | [ ] Open [ ] Approved |
| N4 | Results freeze date | Non-blocking† | Collab B | [ ] Open [ ] Approved |
| N5 | Expected table/figure list polish | Non-blocking | Shared | [ ] Open [ ] Approved |
| N6 | Author affiliations / corresponding author | Non-blocking‡ | Shared | [ ] Open [ ] Approved |
| N7 | Exploratory-package cite policy | Non-blocking | Shared | [ ] Open [ ] Approved |
| N8 | Working title freeze | Non-blocking | Shared | [ ] Open [ ] Approved |

\*Required before Overleaf drafting sync, but scientific freeze can complete first in this repo.  
†Required before Results section, not before Intro skeleton after scientific freeze.  
‡Required before submission; can follow scientific freeze.

### Sign-off

| Author | Spec freeze approved? | Date | Signature / initials |
|---|---|---|---|
| Collaborator A | [ ] Y [ ] N | | |
| Collaborator B | [ ] Y [ ] N | | |
| Monika | [ ] Y [ ] N | | |

**After all blocking items Approved:** update Spec to **v0.2**, then authorize manuscript drafting.
