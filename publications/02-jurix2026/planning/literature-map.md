---
id: pub-02-jurix2026-literature-map
title: "Literature map — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, literature, publication-02]
source: planning/jurix-specification.md
---

## Literature map

**Role.** Supporting map for Section 3 and related claims. The specification remains authoritative; literature supports differentiation and positioning.

**Discipline.** Prefer peer-reviewed AI & Law, XAI, KR, provenance, accountability, contestability, reviewability, AI governance, and primary EU AI Act text. Mark vendor/white-paper items as non-primary.

---

### Explainable AI

| Tier | Works (indicative) | Role for this paper |
|---|---|---|
| Foundational | Doshi-Velez & Kim (2017) towards rigorous science of interpretability; Lipton (2018) mythos of model interpretability; Guidotti et al. (2018) survey of methods | Establish that XAI primarily targets model behaviour at prediction time |
| Recent | NISTIR 8312 four principles (Phillips et al., 2021); process-centric explanation for contestability (Yurrita et al., 2023) | Show principles/methods ≠ durable retention of decision context |
| Likely JURIX citations | Atkinson/Bench-Capon line on justification vs prediction; hybrid ADF–ML explanation papers (Mumford, Atkinson, Bench-Capon, JURIX/FAIA) | Anchor “legal justification ≠ post-hoc feature attribution” |
| Open gap | XAI seldom specifies what must be *preserved* after model/tools/prompts change so that later legal reasoning remains possible | Spec research gap |

---

### Legal explainability

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | Wachter, Mittelstadt & Russell (2017) counterfactual explanations & GDPR; Edwards & Veale (2017) on limits of a “right to explanation”; Selbst & Powles (2017) meaningful information | Separate legal reason-giving from technical XAI |
| Recent | Analyses of XAI vs legal reason-giving functions (decision-subject / decision-maker / ecosystem); AI Act Art. 86 right to explanation debates | Support §6 claim: explainability depends on preserved knowledge |
| Likely JURIX | Bench-Capon & Atkinson tradition; factor-based case explanation | Show JURIX expects legally structured justification |
| Open gap | Legal explainability literature often assumes access to relevant facts/reasons at review time; under-theorizes engineering disappearance of context | Spec §2–§4 |

---

### AI and Law

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | Early AI & Law on justification and case-based reasoning (e.g. Ashley; Bench-Capon surveys); McCarty TAXMAN reflections | Position paper in AI & Law not pure ML ops |
| Recent | Hybrid symbolic–ML legal reasoning with explainable process (Mumford/Atkinson/Bench-Capon JURIX 2021–2022) | Contrast: explaining *legal* structure vs preserving *decision-time* knowledge in deployed systems |
| Likely JURIX | Prior JURIX/ICAIL on explanation, argumentation, evidence | Mandatory CFP expectation |
| Open gap | Strong on argumentation/justification models; thinner on lifecycle preservation in LLM/tool-augmented deployments | Spec main idea |

---

### Knowledge Representation

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | Situation calculus (McCarthy & Hayes); event calculus (Kowalski & Sergot); Allen temporal intervals; case-based reasoning (Aamodt & Plaza) | Motivate structured, temporally situated representations |
| Recent | Ontologies / legal KR surveys; agent memory & intermediate-artifact durability (emerging, treat cautiously) | Show KR supplies vocabulary for “decision knowledge as artifact” |
| Likely JURIX | Legal KR / ontologies / normative systems tracks | Align with JURIX topic I |
| Open gap | Classical KR models events/situations; rarely engineered as retention contracts for legally relevant AI decisions under continuous model change | Spec contributions 2–4 |

---

### Provenance

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | W3C PROV-DM (Moreau et al.); data lineage traditions | Provenance records *how data/products were derived* |
| Recent | Decision provenance (Singh, Cobbe & Norval / related decision-provenance work); Huynh et al. provenance-based explanations | Closest technical neighbours; must differentiate |
| Likely JURIX | Provenance for evidence/accountability papers | Show substrate, not full decision knowledge |
| Open gap | Provenance graphs can encode derivation without guaranteeing legal criteria, human rationale, policy constraints, or review context bound to one decision for later contestation | Spec research gap |

---

### Audit trails

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | Logging/observability practices; compliance audit traditions | Preserve operational events |
| Recent | Governance “decision event” schemas (emerging preprints—cite carefully); NIST AI RMF documentation/governance functions | Audit ≠ structured decision knowledge |
| Likely JURIX | Compliance-checking / auditing computational methods papers | Topic I |
| Open gap | Audit trails preserve *behaviour*; specification argues legal review needs *decision knowledge* | Spec §2 |

---

### Accountability

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | Wieringa (2020) what does accountability mean for algorithms?; Diakopoulos algorithmic accountability | Define accountability relations |
| Recent | Socio-technical ADM accountability; transparency limits (Ananny & Crawford) | Support thesis: accountability needs more than state dumps |
| Likely JURIX | Governance / responsibility computational models | Link §6 |
| Open gap | Accountability frameworks name duties/forums; under-specify engineering artifact that must persist | Spec contribution 3 |

---

### Contestability

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | Hirsch et al. designing contested systems; Almada contestability; Lyons et al. contestability concepts | Contestability as design goal |
| Recent | Alfrink et al. (2022) Contestable AI by Design; process-centric explanations for contestability (Yurrita et al., 2023); explainability–contestability in public-sector AI regulation (Schmude et al., 2025) | Contestability requires tools for scrutiny *and* retained context |
| Likely JURIX | Contestability / due process / ADM papers | Primary topic |
| Open gap | Design frameworks specify features/practices; less on what must be preserved when prompts/tools/models change before a contest arrives | Spec |

---

### Reviewability

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational / core | Cobbe, Lee & Singh (2021) Reviewable Automated Decision-Making (FAccT) | Strongest adjacent socio-technical framework |
| Recent | Extensions linking reviewability to organisational record-keeping | Closest competitor to “knowledge continuity” framing |
| Likely JURIX | Administrative-law-inspired ADM accountability | Highly relevant |
| Open gap / differentiation | Reviewability = systematic record-keeping for meaningful review across ADM process. This paper’s *Decision Knowledge* / *Knowledge Continuity* = engineering artifact + system property focused on structured knowledge for later legal reasoning. Overlap is real; novelty claim must be precise (epistemological/engineering layer), not “first to care about records” | Critical for §3 |

---

### AI governance

| Tier | Works (indicative) | Role |
|---|---|---|
| Foundational | OECD AI principles; NIST AI RMF 1.0 | Governance functions (map, measure, manage) |
| Recent | Technical AI governance; documentation (model cards, datasheets) | Governance docs ≠ decision-time knowledge packages |
| Likely JURIX | AI & data governance computational methods | Topic I |
| Open gap | Governance frameworks rarely define “decision knowledge” as first-class engineering object across lifecycle | Spec §5 |

---

### EU AI Act

| Tier | Works (indicative) | Role |
|---|---|---|
| Primary | Regulation (EU) 2024/1689 — logging, record-keeping, transparency, Art. 86 explanation rights (as applicable) | Legal stress-test, not scientific object |
| Commentary | Emerging AI Act scholarship on logging and explanation | Support legal implications (Havlíková) |
| Likely JURIX | AI Act compliance / governance papers | Secondary topic—open question on depth |
| Open gap | Act imposes duties; does not fully specify engineering representation of decision knowledge for future legal reasoning | Spec implications |

---

### Cross-cutting neighbours to differentiate carefully

| Neighbour | Relationship | Differentiation task |
|---|---|---|
| Decision provenance (Singh et al.) | Provenance of decisions across systems | Spec needs structured legal/review context + continuity under change, not only flow tracing |
| Reviewability (Cobbe et al.) | Socio-technical record-keeping for review | Spec proposes named engineering artifact/property (Decision Knowledge / Knowledge Continuity) |
| Contestable AI by design (Alfrink et al.) | Features/practices for contestation | Spec focuses on *preservation* of knowledge that contestation consumes |
| Counterfactual XAI (Wachter et al.) | Contest-oriented explanations | Spec: explanations fail if underlying decision knowledge was never retained |
| PROV / lineage | Derivation substrate | Necessary but insufficient alone |

---

### Literature acquisition notes

- Prefer published venue versions (FAccT, Minds & Machines, JURIX/FAIA, AI & Law journal, Harvard JOLT) over blogs/vendor PDFs.
- Emerging 2025–2026 arXiv “decision trace” schemas: mention only with caution; do not treat as settled prior art.
- Do **not** treat unpublished O’Reilly argument as citable scientific evidence; convert to research claims with independent support (§2 author note).
