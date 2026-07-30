---
id: pub-02-jurix2026-argument-map
title: "Argument map — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, argument-map, publication-02]
source: planning/jurix-specification.md
---

## Argument map

### Research question — critical evaluation

**RQ (specification):** How should AI systems preserve decision knowledge so that legally relevant decisions remain explainable, reviewable, contestable and justifiable over time?

| Criterion | Assessment |
|---|---|
| Precision | Moderately precise on *object* (decision knowledge) and *purpose* (four legal functions over time). Less precise on *scope* (which systems), *success criteria*, and *“how should”* (design norms vs empirical how). |
| Answerability | Answerable as a **conceptual / design** question (principles + framework), not as a single empirical measurement in this manuscript. Fits a full conceptual JURIX paper if claims stay non-evaluative. |
| JURIX alignment | Strong: legal explainability, accountability, KR, provenance, evidence, governance. Matches AI & Law audience better than pure ML venue. |
| Match to contributions | Good: C1 problem, C2–C4 answer vocabulary/framework, C5 links to the four functions in the RQ. |

#### Suggested improvement (optional, clearly justified)

Keep the central RQ. Add **operational sub-questions** in §1 (not new contributions):

1. What distinguishes decision knowledge from system state?
2. Why do existing XAI/provenance/audit/governance approaches not suffice?
3. What principles/concepts would make knowledge continuity an engineered system property?
4. What follows for legal explainability, review, contestation, and justification?

Rationale: reduces reviewer complaint that “how should” is unbounded, without changing the specification’s RQ.

---

### Thesis — critical evaluation

**Thesis (specification):** Current AI engineering primarily preserves system state; legal accountability depends on preserving decision knowledge; legally relevant AI systems require explicit engineering mechanisms for knowledge continuity rather than relying only on logs, provenance, or post-hoc XAI.

| Criterion | Assessment |
|---|---|
| Novelty | **Moderate.** Adjacent to reviewability, decision provenance, contestable AI by design. Novelty is the **named engineering artifact/property** (Decision Knowledge / Knowledge Continuity) and the **state vs knowledge** diagnosis for legally relevant systems—not the discovery that records matter. |
| Scientific strength | Strong as a **problem characterisation + conceptual response**. Weak if read as empirical proof of necessity or superiority. |
| Falsifiability | Partially: one can show a system that preserves only state fails specific later legal-reasoning tasks; or show an existing approach that already preserves the defined Decision Knowledge components. Harder to falsify “require explicit mechanisms” without agreed component minimum. |
| Clarity | High if definitions in §4 are fixed early. |
| Likely reviewer criticism | Overlap with Cobbe reviewability; “logs/PROV already”; conceptual-only; product/AIGov suspicion; AI Act diversion. |

---

### Contributions — evaluation

#### C1 — Formulation of the epistemological problem

| Dimension | Note |
|---|---|
| Originality | Problem framing (state vs decision knowledge under change) is the paper’s best claim if crisply differentiated from reviewability/provenance. |
| Relation to literature | Builds on accountability/explainability limits; must cite Cobbe, Singh, Alfrink, Wachter. |
| Scientific value | High for JURIX if it becomes a reusable problem statement. |
| Reviewer risk | “Not new” / “just compliance.” |
| Evidence required | Failure-mode analysis (§2); literature gap (§3). |

#### C2 — Decision Knowledge as an engineering artifact

| Dimension | Note |
|---|---|
| Originality | Term is not standardised in AI & Law; related to evidence packages, audit records, decision traces. |
| Relation to literature | KR artifact thinking; provenance entities; reviewability records. |
| Scientific value | Enables precise talk about what must be retained. |
| Reviewer risk | Terminology inflation; unbounded component list. |
| Evidence required | Definition + component inventory mapped to legal functions; contrast with logs/XAI outputs. |

#### C3 — Knowledge Continuity as a system property

| Dimension | Note |
|---|---|
| Originality | “Knowledge continuity” appears in KM/org-memory discourse; uncommon as formal AI & Law system property. |
| Relation to literature | Continuity/memory infrastructures (non-legal); reviewability over time. |
| Scientific value | Shifts claim from one-shot explanation to temporal system property. |
| Reviewer risk | Vague property; unmeasurable. |
| Evidence required | Definition; link to change scenarios; optional future metrics (out of scope now). |

#### C4 — Conceptual framework across the AI lifecycle

| Dimension | Note |
|---|---|
| Originality | Principles/concepts in spec are a **design sketch**, not a formal architecture. |
| Relation to literature | Overlaps contestable-AI features and reviewability checkpoints. |
| Scientific value | Bridges engineering and law if kept conceptual and honest. |
| Reviewer risk | Framework paper without evaluation; buzzword concepts (knowledge graph, audit chain). |
| Evidence required | Coherent mapping principles→concepts→legal functions; figures; explicit non-claims. |

#### C5 — Implications for legal functions

| Dimension | Note |
|---|---|
| Originality | Implications follow from C2–C4; not independent theory. |
| Relation to literature | Directly engages legal explainability, contestability, reviewability, AI Act. |
| Scientific value | Makes paper JURIX-relevant rather than pure systems. |
| Reviewer risk | Legal overclaim; insufficient doctrinal depth. |
| Evidence required | Careful implication language (“enables conditions for…”) not “satisfies Art. X”. |

**No additional contributions invented.**

---

### Global argument chain

```text
RQ (how preserve decision knowledge for legal functions over time)
  └─ Thesis (state ≠ decision knowledge; need engineered knowledge continuity)
       ├─ §2 Diagnose loss mechanisms (state mutates; knowledge disappears)
       ├─ §3 Show existing approaches stop short of structured decision knowledge
       ├─ §4 Define Decision Knowledge + Knowledge Continuity
       ├─ §5 Conceptual preservation principles/concepts
       ├─ §6 Implications for AI & Law (central claim on explainability)
       └─ §7–8 Limits, narrow contribution, future validation
```

### Claim → source tracing rule

Every manuscript claim must cite either:

- (a) `jurix-specification.md`, or
- (b) an identifiable literature source from `literature-map.md` (or later bibliography).

Do not import problem labels, evaluation scores, or architectures from other publications in this repository.
