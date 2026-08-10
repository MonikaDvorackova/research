---
id: pub-03-ltkm-monika-deliverable
title: "Monika mid-August deliverable — Publication 03"
type: research-notes
status: active
created: 2026-07-31
updated: 2026-07-31
---

# Monika mid-August deliverable (updated for S1)

**Objective:** Conceptual/scientific spine for a collaborative ICLR paper — approximately one-third of a three-author paper — **after** the archive Pareto pilot passes go criteria.  
**Target window:** mid-August (exact date TBD).  
**Form:** Markdown drafts in this package (or Overleaf once SOT decided). **No fabricated results. No manuscript prose until pilot go.**

**Scientific frame (authoritative):**  
[`research-question.md`](research-question.md) · [`research-specification-v0.1.md`](research-specification-v0.1.md) · [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md)

---

## What Monika owns now (S1)

| Ownership | Content |
|---|---|
| Conceptual framing | Fixed-budget allocation between current-use knowledge and retained superseded knowledge |
| Definitions | Current-state vs historical-state objectives; superseded knowledge; archive ratio \(\alpha\); Pareto characterization language |
| Research question & hypotheses | S1 RQ; H0/H1; falsification and claim discipline |
| Literature positioning | Gap as resource-allocation / current–historical trade-off (not “new hierarchy”) |
| Interpretation | Pareto regimes: when archive retention is beneficial, costly, or unnecessary |
| Writing (post-go only) | Introduction; Discussion; contribution wording under conservative “trade-off characterization” language |
| Claim hygiene | Forbid hierarchy-superiority, universal archive necessity, and CR-Gap imports |

## What Monika does **not** own (unless re-agreed)

Implementation; world-generator code; baseline runs; statistical analysis; hardware; result tables; ablation plots.

---

## Pre-pilot Monika work (authorized now)

These are planning/science artefacts, **not** manuscript sections:

1. Maintain RQ + Spec + pilot protocol alignment (done in this pass).  
2. Draft a **literature map skeleton** for fixed-budget / bitemporal / staleness / agent-memory allocation papers (citation slots only; no overclaim).  
3. Draft a **glossary** of S1 terms (\(B\), \(\alpha\), superseded, \(A_c\), \(A_h\), Pareto frontier).  
4. Review pilot `go_nogo.md` when produced; advise continue vs reframe (S2/S4).

**Do not write full Introduction/Related Work prose claiming results.**

---

## Post-go deliverable package (mid-August target)

Only if pilot **go** criteria pass:

1. Introduction (draft) — motivates fixed-budget current vs historical trade-off; states S1; positions LTKM as platform  
2. Research Gap (draft) — allocation/Pareto gap, not taxonomy novelty  
3. Problem Formulation (draft) — \(B_c+B_a=B\), \(\alpha\), query types, objectives  
4. Terminology / glossary (frozen draft)  
5. Design Principles (draft) — principles about **allocation and retention**, mapped to pilot analyses  
6. Conceptual platform description (draft) — how active vs archive expose \(\alpha\) (not “five layers are novel”)  
7. Related Work structure + literature map (+ partial prose)  
8. Discussion skeleton — regime interpretation placeholders tied to actual plots  
9. Contribution wording — empirical Pareto / trade-off characterization; conditional on full results  

### Contribution wording template (conditional)

> We formulate long-term agent memory under a **fixed total budget** as an allocation between knowledge for **current-state** queries and retained **superseded** knowledge for **historical-state** queries. Using a hierarchical long-term knowledge memory system as an experimental platform, we empirically characterize the **current–historical accuracy Pareto frontier** induced by archive ratio \(\alpha\), and identify regimes where archive retention is beneficial, costly, or unnecessary. **Quantitative claims are contingent on completed experiments.**

---

## Section notes (post-go)

### Introduction

| | |
|---|---|
| **Purpose** | Motivate competing current vs historical objectives under capacity constraints; state S1; preview Pareto analysis |
| **Can write after go** | Problem; RQ; platform role; contribution forms without overclaiming universality |
| **Placeholders** | Numeric frontier highlights; baseline names as run |
| **Prohibited** | Hierarchy is better; archives always help; CR-Gap/LiC as this paper’s results |

### Research Gap

| | |
|---|---|
| **Purpose** | Position vs agent memory, bitemporal stores, forgetting, conflict/staleness benchmarks |
| **Emphasis** | Missing fixed-\(B\) current–historical Pareto under archive allocation |
| **Prohibited** | Declaring five-layer taxonomy uniquely novel |

### Problem Formulation

| | |
|---|---|
| **Purpose** | Formalize \(B,\alpha\), evolving world, \(A_c,A_h\), Pareto object |
| **Required inputs** | Pilot/main generator notation from collaborators |

### Design Principles

| | |
|---|---|
| **Purpose** | Justify measuring allocation, matched budgets, separate reporting of \(A_c\) and \(A_h\), flat temporal control |
| **Prohibited** | Treating principles as empirically proven before analyses exist |

### Discussion skeleton

| | |
|---|---|
| **Purpose** | Slots for regime map, when \(\alpha\) is wasteful, demotion of architecture if flat matches, limitations of synthetic world |
| **Prohibited** | Inventing which regime “won” before tables exist |

---

## Mid-August definition of done (Monika)

**If pilot go:**

- [ ] Glossary v0 shared and revised once  
- [ ] Intro + Gap + Problem + Principles + platform conceptual drafts  
- [ ] Related Work map with ≥15 candidate keys  
- [ ] Discussion skeleton tied to real Pareto figures  
- [ ] Contribution wording uses trade-off/Pareto language only  
- [ ] No invented numbers  

**If pilot no-go:**

- [ ] Written recommendation: stop S1 / reframe to S2 or S4 / report negative characterization  
- [ ] No manuscript sections claiming S1 success  

## Explicitly out of scope

Implementation, benchmark code, baseline runs, statistical analysis, hardware sections, result tables—unless ownership is reassigned in writing.
