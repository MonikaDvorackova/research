---
id: pub-02-jurix2026-section-development
title: "Section development notes — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, outline, section-development, publication-02]
source: planning/jurix-specification.md
---

## Section development notes

Complete argument structure for the manuscript. **Not** full prose. Source: `jurix-specification.md`. Literature: `literature-map.md`.

---

### Section 1 — Introduction

#### Purpose

Introduce the main problem.

#### Scientific objective

State the problem of preserving decision knowledge in legally relevant AI systems; present RQ, thesis sketch, and contributions without solving them yet.

#### Logical flow

1. Legally relevant AI decisions have lasting consequences.
2. Operational logging and post-hoc XAI are the default engineering responses.
3. Decision context often disappears (preview of §2).
4. Legal accountability and review therefore face an engineering deficit.
5. Position in AI & Law.
6. RQ + contributions + roadmap.

#### Key arguments

- More than operational logging is required for later legal reasoning.
- Post-hoc explainability may be insufficient when context is gone.
- Relevance: explainability, accountability, reviewability, contestability, evidentiary reconstruction (spec primary topics).

#### Expected evidence

- Illustrative failure modes (non-empirical vignettes OK if labelled as such).
- Pointers to legal reason-giving / reviewability literature (not full review—that is §3).

#### Literature to review

- Legal explainability (Wachter; Edwards & Veale).
- Reviewability / contestability (Cobbe; Alfrink)—brief.
- JURIX expectations on justification (Atkinson/Bench-Capon).

#### Potential counterarguments

- “Logs already solve this.”
- “XAI already solves explainability.”
- “This is only a compliance/AI Act paper.”

#### Open issues

- How much concrete case vs abstract framing? (spec open question)
- Whether AIGov is named (spec open question)—prefer anonymised principles if double-blind/internal conflict.

#### Transition to next section

Move from problem statement to the engineering diagnosis: system state ≠ decision knowledge.

---

### Section 2 — The Missing Engineering Problem

#### Purpose

Explain the difference between preserving system state and preserving decision knowledge.

#### Scientific objective

Make the epistemological/engineering gap precise and concrete through failure modes listed in the specification.

#### Logical flow

1. Define “system state” as currently mutable runtime/config/store contents.
2. Walk failure modes: overwritten prompts; changing retrieval; changing tools; model updates; human approvals without rationale; missing policy constraints; disappearing legal context.
3. Argue each destroys or mutates information needed for later explanation/review/contestation/justification.
4. Conclude: state preservation ≠ knowledge preservation.

#### Key arguments

- Spec topics as mechanisms of knowledge loss.
- Core O’Reilly argument rewritten as research claim (author note)—must stand without citing unpublished Radar piece as authority.

#### Expected evidence

- Structured examples (synthetic or documented public incidents).
- Contrast table foreshadowing Figure 1.

#### Literature to review

- Provenance vs logs; decision provenance (Singh).
- Reviewability record-keeping (Cobbe).
- LLM/tooling change literature (lightly).

#### Potential counterarguments

- Version control / feature stores already pin everything.
- Bit-exact replay is the right goal.
- Only regulated systems need this.

#### Open issues

- Scope: legally relevant systems only (keep narrow—§7 author note).
- Avoid importing problem labels from other manuscripts outside this specification.

#### Transition to next section

Ask what existing literatures already cover—and where they stop.

---

### Section 3 — Existing Approaches and Their Limits

#### Purpose

Position the paper within existing AI and Law literature.

#### Scientific objective

Show coverage and limits of XAI, legal explainability, KR, provenance, audit trails, governance, accountability, reviewability, contestability, and AI Act duties; state the research gap exactly as in the specification.

#### Logical flow

1. Map each relevant area (spec list).
2. For each: what it preserves / enables.
3. Shared limit: not preserving structured knowledge required for *future legal reasoning about a specific AI-assisted decision*.
4. Explicit differentiation from closest neighbours (reviewability; decision provenance; contestable AI by design).

#### Key arguments

- Spec research gap (preserve wording).
- Neighbours are complementary substrates/frameworks, not substitutes.

#### Expected evidence

- Citation-backed capability claims.
- One synthesis table: approach → preserves → fails to preserve for later legal reasoning.

#### Literature to review

Full `literature-map.md`. All authors contribute (spec author note).

#### Potential counterarguments

- Reviewability already is this paper.
- PROV + audit logs suffice.
- AI Act logging duties close the gap.

#### Open issues

- Depth of AI Act discussion (spec open question).
- Which JURIX topic to foreground (spec open question).

#### Transition to next section

Introduce positive conceptual vocabulary: Decision Knowledge and Knowledge Continuity.

---

### Section 4 — From State to Decision Knowledge

#### Purpose

Define Decision Knowledge and Knowledge Continuity; motivate importance (spec).

#### Scientific objective

Stabilise terminology and component inventory so later engineering principles attach to clear referents.

#### Logical flow

1. Definition of Decision Knowledge (exact).
2. Possible components (spec list)—as a working inventory, not a final ontology.
3. Definition of Knowledge Continuity (exact).
4. Importance bullets (spec).
5. Relation: Knowledge Continuity is the system property of preserving Decision Knowledge under change.

#### Key arguments

- Decision Knowledge is an engineering artifact (contribution 2).
- Knowledge Continuity is a system property (contribution 3).
- Explainability/accountability/contestability/review depend on this preservation.

#### Expected evidence

- Conceptual consistency with §2 failure modes (each mode deletes some component).
- Alignment with legal functions of reason-giving / review (literature support).

#### Literature to review

- KR temporal/event representations (motivating structure).
- Contestability/reviewability requirements as consumers of components.
- Terminology conflicts (see `terminology-review.md`).

#### Potential counterarguments

- Terms already exist / are marketing.
- Component list is arbitrary or unbounded.
- Overlaps too much with “evidence package” / “audit record”.

#### Open issues

- Best term? (spec)
- Formal model now or later? (spec)
- Minimum vs maximal component sets.

#### Transition to next section

Ask how systems could engineer Knowledge Continuity.

---

### Section 5 — Engineering Knowledge Continuity

#### Purpose

Describe conceptually how decision knowledge could be preserved.

#### Scientific objective

Propose a conceptual framework (contribution 4) using principles and concepts from the specification—without claiming an implemented evaluation.

#### Logical flow

1. Principles (spec list) as design requirements.
2. Concepts (decision object, evidence object, knowledge dependency, review context, governance primitive, lifecycle model, audit chain, decision knowledge graph) as vocabulary—not product architecture.
3. Map principles → concepts → legal functions (explain / justify / review / contest).
4. Emphasise design-before-deployment.

#### Key arguments

- Preservation must be intentional engineering, not residual logging.
- Framework is conceptual; validation is future work (spec §8).

#### Expected evidence

- Worked conceptual scenario (if authors choose—open question).
- Figures 2–4.

#### Literature to review

- Contestable AI by design features (Alfrink)—complement.
- Reviewability points of intervention (Cobbe)—complement.
- Provenance as binding substrate.

#### Potential counterarguments

- Too vague / not formal.
- Another governance framework.
- Implementation impossible / too costly (preview §7).

#### Open issues

- Formal modelling (future work).
- Explicit AIGov (open question)—keep as principles connection for Monika’s responsibility without product pitch.

#### Transition to next section

Derive implications for AI & Law.

---

### Section 6 — Implications for AI and Law

#### Purpose

Connect engineering claims to legal explainability, contestability, administrative review, evidentiary reconstruction, accountability, institutional responsibility, governance compliance, and limits of technical explainability.

#### Scientific objective

Defend central claim: explainability is not only a model property; it depends on whether the system preserved knowledge necessary for future legal reasoning.

#### Logical flow

1. Restate central claim (exact).
2. Walk implications list (spec topics).
3. Engineering artifacts as necessary conditions for legal justification—not sufficient for correctness of decisions.
4. Limits: technical XAI cannot substitute missing preserved knowledge.

#### Key arguments

- Contribution 5 (implications).
- Legal duties (e.g. AI Act logging/explanation) stress-test the need; they do not replace the engineering thesis.

#### Expected evidence

- Mapping table: legal function → Decision Knowledge components required.
- Case sketches optional (open question).

#### Literature to review

- Legal explainability; contestability; reviewability; AI Act primary text; administrative law (Havlíková).

#### Potential counterarguments

- Law does not require this much retention.
- Privacy/data minimisation forbids it (§7).
- Institutional responsibility is organisational, not technical.

#### Open issues

- How much AI Act (spec).
- Whether to include a legal case (spec).

#### Transition to next section

Honest limits and trade-offs.

---

### Section 7 — Discussion

#### Purpose

Discuss strengths, limitations, and trade-offs; keep contribution intentionally narrow (spec author note).

#### Scientific objective

Pre-empt reviewer attacks on scope, cost, privacy, and validation.

#### Logical flow

1. Strengths: clear problem formulation; engineering vocabulary; AI & Law bridge.
2. Limitations: conceptual; no formal model/implementation/case study yet.
3. Trade-offs: over-documentation, proportionality, privacy, implementation burden, institutional adoption, limits of reconstruction.
4. Future validation path.
5. Narrow contribution statement (exact author note).

#### Key arguments

- Narrowness is a feature for JURIX page budget and falsifiable framing.
- Reconstruction has limits even with preservation.

#### Expected evidence

- Argumentative; cite privacy/data minimisation tensions.

#### Literature to review

- Transparency limits; data protection; governance adoption studies (light).

#### Potential counterarguments

- Too narrow to matter.
- Too broad without evaluation.
- Hidden product agenda (AIGov).

#### Open issues

- Validation plan for camera-ready vs workshop version.

#### Transition to next section

Compress into conclusion and future work.

---

### Section 8 — Conclusion

#### Purpose

Restate main message and future work (spec).

#### Scientific objective

Close without overclaiming.

#### Logical flow

1. Main message (exact).
2. Contributions recapitulation (1–5).
3. Future work list (exact).
4. Optional: open questions left for community.

#### Key arguments

- Legally relevant AI systems should preserve knowledge required for future explanation, review, contestability, and legal justification.

#### Expected evidence

None new.

#### Literature to review

None new.

#### Potential counterarguments

- Restatement without proof.

#### Open issues

None beyond future work.

#### Transition

End.
