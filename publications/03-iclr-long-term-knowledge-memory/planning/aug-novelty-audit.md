---
id: pub-03-aug-novelty-audit
title: "AUG novelty / occupation audit"
type: research-notes
status: audit
created: 2026-08-01
updated: 2026-08-01
purpose: kill-test AUG as Pub-03 scientific object
---

# AUG novelty / occupation audit

**Object under audit:** Adequacy–Utilization Gap — \(I\) adequate under explicit \(f_T\) and \(M(x,I)\neq y^*\).  
**Stance:** Attempt to **kill**, not defend.

**Verdict on universal AUG as a scientific object:** **OCCUPIED**  
(with secondary remark: as a paper-level “object” without a specific law, also **TOO BROAD TO BE A SCIENTIFIC OBJECT**).

---

## Occupation criterion (frozen for this audit)

**OCCUPIED** if prior primary work (2023–2026) already:

1. separates **context/information sufficiency** from **model error**, and  
2. documents nontrivial rates of **wrong answers under sufficient / gold / oracle information**, and  
3. treats that residual as a first-class analytical object (not a passing remark),

under any of: context utilization, sufficient-context failure, gold-in-context / oracle-retrieval residual, post-retrieval reasoning failure, retrieval–utilization gap.

Cosmetic renaming does not create openness.

---

## Closest-work matrix (methods/experiments, not abstracts only)

| Work | Exact definition used | Sufficiency independent of \(M\)? | Retrieval controlled? | One task vs general object? | Cross-task utilization law? | Overlap with AUG | Residual (if any) |
|---|---|---|---|---|---|---|---|
| **Joren et al., ICLR 2025** *Sufficient Context* | Context sufficient iff a plausible answer exists from \((Q,C)\) (AIS-inspired; autorater) | Yes (autorater on \(Q,C\); not “strong model succeeds”) | Analyzes RAG datasets; sufficiency labeled post-hoc | General RAG/QA lens across HotPot, Musique, FreshQA, etc. | Behavioral stratification + selective generation; **no compositional interference law** | **Near-total:** adequate-ish \(I\) + wrong \(M\) is core finding (“open-book QA cannot be solved by retrieval alone”) | Uniqueness of gold \(y^*\) not always required; little binding/swap taxonomy |
| **DeepResearch-Slice (arXiv:2601.03261)** | Retrieval–Utilization Gap: fail to use gold evidence though retrieved | Gold-in-context style utilization conditional | Explicit retrieved gold tracking | Multi-benchmark agent/research setting | Mitigation via hard span filter; not a general law of cue composition | High: \(P(\mathrm{use}\mid\mathrm{retrieved})\) | Mechanism = noise/context-blindness; not unique \(f_T\) |
| **RECON (arXiv:2607.16716)** | Failures persist when retrieval succeeds / oracle graph upper bound | Oracle/retrieval success separated from reasoning | Yes (oracle retrieval studied) | Compositional reasoning after change; case files | Empirical “~4/5 failures persist when retrieval succeeds” | High: post-retrieval residual | Not adequacy formalized as \(f_T(x,I)=y^*\); not cue geometry |
| **“Diagnosing Retrieval vs Utilization” (arXiv:2603.02473)** | Stage attribution write×retrieve on LoCoMo | Partial | Varies by method | Memory QA | Mostly retrieval dominates | Medium: residual utilization underexplored | Does not define AUG as object |
| **Liu et al., TACL 2024** *Lost in the Middle* | Relevant evidence present; position IV | Gold/relevant present by construction | Controlled multi-doc | Multi-doc QA + key-value | Position U-shape; not utilization-vs-adequacy general law | Partial: gold-present error | Position, not adequacy theory |
| **Feng & Steinhardt, ICLR 2024** Binding ID | Causal binding mechanism | N/A (full constructed context) | N/A | Synthetic binding | Representational mechanism | Low as AUG; high as binding | Different object |
| **Knowledge conflict surveys / ECHOQA (2024)** | PK vs CK interplay | Context given | Controlled conflict types | Multi knowledge types | Behavioral PK suppression | Partial: wrong use of context, not adequacy | Conflict ≠ unique entailment failures |
| **Lost-in-the-Later (arXiv:2507.05424)** | Contextual vs parametric grounding | Entailment-based CK | Prompt context | Grounding quantification | Positional grounding | Partial | Grounding ≠ adequacy–utilization law |
| **Oracle-RAG baselines (2025 tooling)** | Gold context ceiling | Gold passages supplied | Oracle | Eval ceiling | None | Partial: isolates generation residual | Standard method, not a theory paper |

### Primary occupying paper

**Joren et al., “Sufficient Context…”, ICLR 2025.**

They explicitly pose: errors from **failure to utilize** vs **insufficient context**; define sufficiency independently of ground-truth-free autorater judgment; show **nontrivial errors under sufficient context**; conclude retrieval alone cannot solve open-book QA. That **is** the AUG existence claim at conference scale.

RECON and Retrieval–Utilization Gap papers reinforce occupation of the *post-retrieval residual* niche.

---

## Classification

| Label | Decision |
|---|---|
| OPEN | **No** |
| PARTIALLY OPEN | **No** for universal AUG (no clean residual law left that is both unoccupied and ICLR-deep) |
| **OCCUPIED** | **Yes** — sufficient-context / utilization residual is established |
| TOO BROAD TO BE A SCIENTIFIC OBJECT | **Also yes** as a *paper title object* without a specific falsifiable law — AUG names a **category**, not a contribution |

**Implication for Pub 03:** Do **not** adopt “AUG” as the primary scientific claim. Renaming Sufficient Context / utilization gap does not create novelty.

---

## What would still be needed for PARTIALLY OPEN (not claimed here)

A residual would require something **Sufficient Context does not already own**, e.g. a **cross-family compositional law of failures under uniquely adequate \(I\)**.  
Prior repo evidence does **not** establish that residual (see `aug-cross-phenomenon-hypotheses.md`). Therefore: **not PARTIALLY OPEN**.
