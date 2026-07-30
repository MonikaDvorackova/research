---
id: pub-02-jurix2026-specification
title: "JURIX manuscript specification — Publication 02"
type: publication
status: draft
created: 2026-07-29
updated: 2026-07-29
tags: [jurix, specification, publication-02]
target_venue: JURIX 2026
publish: false
---

## JURIX Manuscript Specification

**Document role.** Single source of truth for Publication 02 (`publications/02-jurix2026/`). Preserved faithfully from the author-supplied specification. Do not improve, rewrite, or infer missing scientific content in this file.

## JURIX MANUSCRIPT SPECIFICATION

Venue: JURIX 2026

Submission type: Full paper

Format: Springer LNCS

Language: English

Review: Double-blind

Page limits:

- Full paper – 16 pages
- Short paper – 8 pages
- Poster/Demo – 4 pages

Submission requirements:

- Manuscript must be anonymised before submission.
- Remove author names, affiliations, acknowledgements and identifying project references.
- Self-citations should not reveal author identity.

Primary topics:

- legal explainability
- accountability
- reviewability
- knowledge representation
- provenance
- evidentiary reconstruction

Main research idea

Preserving decision knowledge in legally relevant AI systems.

Central Research Question

How should AI systems preserve decision knowledge so that legally relevant decisions remain explainable, reviewable, contestable and justifiable over time?

Main Thesis

Current AI engineering primarily preserves system state.

Legal accountability, however, depends on preserving decision knowledge.

This paper argues that legally relevant AI systems require explicit engineering mechanisms for knowledge continuity rather than relying only on logs, provenance records or post-hoc explainability techniques.

Proposed Contributions

1. Formulation of the epistemological problem emerging in legally relevant AI systems.

2. Decision Knowledge as an engineering artifact.

3. Knowledge Continuity as a system property.

4. A conceptual framework for preserving decision knowledge across the AI lifecycle.

5. Implications for

- legal explainability
- accountability
- reviewability
- contestability
- evidentiary reconstruction

## Section 1 — Introduction

Purpose

Introduce the main problem.

Topics

- why legally relevant AI systems require more than operational logging
- why post-hoc explainability may be insufficient
- why decision context disappears
- consequences for legal accountability and review
- relevance for AI and Law
- research question
- paper contributions

## Section 2 — The Missing Engineering Problem

Purpose

Explain the difference between preserving system state and preserving decision knowledge.

Topics

- overwritten prompts
- changing retrieval results
- changing external tools
- model updates
- human approvals without rationale
- missing policy constraints
- disappearing legal context
- why state is not the same as knowledge

Author note

This section should carry the core O'Reilly argument but rewritten as a research paper suitable for JURIX.

## Section 3 — Existing Approaches and Their Limits

Purpose

Position the paper within existing AI and Law literature.

Relevant areas

- Explainable AI
- Legal explainability
- Legal reasoning
- Knowledge representation
- Provenance
- Audit trails
- AI governance
- Accountability
- Reviewability
- Contestability
- EU AI Act

Research gap

Existing approaches explain outputs, trace data or audit behaviour, but they do not preserve the structured knowledge required for future legal reasoning about a specific AI-assisted decision.

Author note

This section is particularly suitable for contributions from all authors.

## Section 4 — From State to Decision Knowledge

Decision Knowledge

Definition

Decision Knowledge is the structured set of information required to explain, justify, review or contest a specific AI-assisted decision after the decision has been made.

Possible components

- input data
- prompt context
- retrieved evidence
- model version
- tool outputs
- policy constraints
- legal criteria
- human rationale
- uncertainty
- links between evidence, reasoning and output

Knowledge Continuity

Definition

Knowledge Continuity is the ability of an AI system to preserve the decision knowledge necessary for future explanation, accountability, contestation and legal review across time, system changes and institutional contexts.

Importance

- legal review occurs later
- accountability requires reconstruction
- contestability requires preserved context
- legal justification requires more than the final output
- explainability depends on preserved knowledge

## Section 5 — Engineering Knowledge Continuity

Purpose

Describe conceptually how decision knowledge could be preserved.

Possible principles

- preserve decision knowledge as a persistent engineering artifact
- capture transient context
- connect evidence to decisions
- preserve reviewability
- record rationale for approvals
- preserve governance constraints
- design preservation before deployment

Possible concepts

- decision object
- evidence object
- knowledge dependency
- review context
- governance primitive
- lifecycle model
- audit chain
- decision knowledge graph

## Section 6 — Implications for AI and Law

Topics

- legal explainability
- contestability
- administrative review
- evidentiary reconstruction
- accountability
- institutional responsibility
- AI governance compliance
- limits of technical explainability
- engineering artifacts and legal justification

Central claim

Explainability is not only a model property.

It also depends on whether the system preserved the knowledge necessary for future legal reasoning.

## Section 7 — Discussion

Topics

- strengths
- limitations
- over-documentation
- proportionality
- privacy
- implementation burden
- institutional adoption
- limits of reconstruction
- future validation

Author note

The contribution is intentionally narrow:

Decision knowledge preservation represents a missing engineering layer for legally relevant AI systems.

## Section 8 — Conclusion

Main message

Legally relevant AI systems should preserve the knowledge required for future explanation, review, contestability and legal justification.

Future work

- formal modelling
- implementation patterns
- case studies
- legal evaluation
- comparison with audit systems
- integration with AI governance

Potential Figures

Figure 1 – System State vs Decision Knowledge

Figure 2 – Knowledge Continuity across the AI lifecycle

Figure 3 – Conceptual model of decision knowledge preservation

Figure 4 – Relationship between decision, evidence, rationale, policy constraints and review context

Open Questions

- Is "Decision Knowledge" the best term?
- Is "Knowledge Continuity" the strongest framing?
- Should the paper include a legal case?
- Should AIGov be explicit?
- Which JURIX topic should be foregrounded?
- Should the paper include a formal model?
- Should the paper include a conceptual case study?
- How much AI Act discussion should be included?

Initial Author Notes

This document represents an initial proposal for discussion and may evolve during manuscript preparation.

All authors are encouraged to contribute across sections where appropriate.

Author responsibilities

Monika Dvořáčková

- overall research direction
- core concepts
- engineering perspective
- AI architecture
- conceptual framework
- connection to AIGov principles
- final manuscript integration

Štěpánka Havlíková

- legal implications
- AI Act
- AI Act and other legal requirements on logging in AI systems
- legal explainability of decisions made by AI systems
- administrative law and other sectoral legislation
- contestability
- legal literature

Jakub Harašta

- scientific framing
- research methodology
- AI and Law positioning
- related work
- argumentation
- overall consistency
- critical review
