---
id: note-research-program-publication-architectures
title: "Research Programme — Alternative Publication Architectures"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, publication-architectures]
refs: []
---

> **SUPERSEDED NOTICE (2026-08-25):** The three-standalone-article
> architecture recommended below (Architecture C) has been superseded by
> a human editorial decision — see `PUBLICATION-ARCHITECTURE-FINAL.md`,
> the current authoritative publication map. Contribution 3 is now
> retained as a supporting research note, not a standalone Article 3.
> This document's analysis is left unmodified as a historical record of
> how that recommendation was originally reasoned.

## Research Programme — Alternative Publication Architectures

Scope: Task 8. Builds on the minimum independent contribution set established in `contribution-boundaries.md` (three contributions: Decision-Level Control; Preservation & Reconstruction; The Understanding Layer) and the research-form classification in `empirical-program.md`. This file only moves from contributions to publications — it does not repeat the falsification testing or the AIGov Core analysis, both housed in their own files. No venues, journals, conferences, or publishers are assigned anywhere below, per instruction.

---

## Architecture A — Minimal

Two publication units.

### A1 — Decision-Level Control

- **Working title:** Model Outputs Are Not Decisions: Building Evidence-Gated AI Systems.
- **Research question:** What must an architecture make explicit before an AI-derived output is allowed to cause a consequential action, and how is that made to actually constrain behavior?
- **Thesis:** An explicit decision layer — evidence, requirements, authority, a gate — attached to the decision (not the model) is required once outputs cause consequential actions.
- **Contribution:** New synthesis of established authorization/admission/supply-chain mechanisms, applied specifically to the model-vs-decision boundary, plus the "one model, many decisions" inversion.
- **Abstraction level:** Decision.
- **Required evidence:** Architecture argument (complete); optional repository audit / controlled failure experiment.
- **Prior-art fields:** Access control, admission control, software supply-chain security, CI/CD, ML model registries.
- **Dependency on previous work:** None.
- **What it deliberately does not cover:** Preservation over time, capability vs. understanding.
- **Novelty remaining for subsequent work:** Full — does not touch the other two contributions' material.
- **Overlap risk:** Low.
- **Salami-slicing risk:** N/A (this is already the merged, non-sliced unit).
- **Audience type:** Practitioner / ML engineering / systems.

### A2 — Preserving Decision Knowledge

- **Working title:** Preserving Decision Knowledge: State, Provenance, and the Understanding Layer.
- **Research question:** Combined — does current state suffice for reconstruction, and separately, is AI capability outpacing the mechanisms needed to preserve understanding of system behavior generally?
- **Thesis:** A single combined thesis spanning both the falsifiable, near-term provenance claim and the terminal, historical/comparative understanding-layer claim.
- **Contribution:** Merges Contributions 2 and 3 into one document.
- **Abstraction level:** Historical/provenance *and* Systems-knowledge, undifferentiated within one piece.
- **Required evidence:** Everything Contributions 2 and 3 individually need — a controlled failure experiment, a repository audit, *and* a dedicated historical/comparative literature review — inside one document.
- **Prior-art fields:** Provenance/supply-chain, digital preservation/archival science, and software-engineering history, all at once.
- **Dependency on previous work:** A1's shared premise (C1) only.
- **What it deliberately does not cover:** Nothing — this is the risk.
- **Novelty remaining for subsequent work:** Minimal — front-loads nearly everything.
- **Overlap risk:** Low between A1 and A2; **high internally**, between the falsifiable/evidence-driven half (C6/C7) and the terminal/interpretive half (C8/C9).
- **Salami-slicing risk:** Low (the opposite risk dominates here — see below).
- **Audience type:** Interdisciplinary / systems / AI governance, uncomfortably combined.

**Assessment:** The dominant risk is **dilution**, not fragmentation. A2 forces genuinely different evidence types and defensibility levels (C6/C7 audited at 3/5 defensibility with a clear falsification path; C8/C9 audited at 2/5 defensibility with no clean falsification path) into one document. A skeptical reviewer could reasonably treat the whole piece as under-evidenced because its strongest, most falsifiable material is inseparable from its weakest, most speculative material — precisely the premature-spend risk `contribution-boundaries.md` flags for C8 specifically.

---

## Architecture B — Maximal but non-salami

Three publication units, matching the claim graph's natural joints from `contribution-boundaries.md` exactly.

### B1 — Decision-Level Control

Identical to A1 above.

### B2 — State Is Not Knowledge

- **Working title:** State Is Not Knowledge: Why Decision Records Don't Guarantee Reconstructability (working title, pending Step 2's audit for a more technically precise formulation per `claim-graph.md`'s C6 precision concern).
- **Research question:** Does current system state — including stored decisions and their evidence — suffice to reconstruct why a past decision was valid, and what architectural commitment closes the gap if not?
- **Thesis:** Current state is insufficient because AI-specific transient context is never captured by default; decision provenance must become an explicit, versioned architectural concern.
- **Contribution:** The freshest, least prior-art-collided material in the whole programme (Inversions D and E, both 5/5 disruptive potential); the central falsifiable empirical opportunity of the programme.
- **Abstraction level:** Historical/provenance.
- **Required evidence:** A dedicated prior-art audit (not yet done), a controlled failure/reconstruction experiment, and a companion repository audit — full designs in `empirical-program.md`.
- **Prior-art fields:** SLSA/in-toto, bitemporal databases, digital preservation/archival science, incident-investigation practice (all only partially or not-yet researched).
- **Dependency on previous work:** B1's shared premise (C1) only — not B1's architecture.
- **What it deliberately does not cover:** Capability vs. understanding, the historical software-engineering pattern as a general claim, decision-time enforcement mechanics.
- **Novelty remaining for subsequent work:** Full — does not touch B3's material.
- **Overlap risk:** Low with B1 and B3.
- **Salami-slicing risk:** Low as a merged C6+C7 unit; would be high if split further into separate diagnosis-only and architecture-only pieces (tested and rejected in `contribution-boundaries.md`).
- **Audience type:** Systems / AI governance / academic.

### B3 — The Understanding Layer

- **Working title:** The Understanding Layer: Capability, Understanding, and the Missing Architecture.
- **Research question:** Does the recurring software-engineering pattern of building preservation mechanisms in response to complexity apply to AI, and is capability advancing faster than the mechanisms needed to preserve knowledge of system behavior?
- **Thesis:** AI may be the first major computing paradigm in which capability is scaling faster than preservation mechanisms; explainability/interpretability/observability/provenance/governance/auditability may be fragmented partial responses to one deeper requirement.
- **Contribution:** The deepest, most ambitious claim in the programme, explicitly framed as a diagnosis-plus-open-problem-statement rather than a specified architecture (per C9b's honest novelty-risk rating).
- **Abstraction level:** Systems-knowledge.
- **Required evidence:** A dedicated historical/comparative literature review (not yet done — the largest gap in the programme) plus synthesis of B1 and B2.
- **Prior-art fields:** History of software engineering; the explainability/interpretability/observability/governance/auditability research communities' own self-descriptions.
- **Dependency on previous work:** B1 and B2, both for concrete grounding and for earned credibility.
- **What it deliberately does not cover:** A specified interface or implementation for the "understanding layer" itself — explicitly out of scope until the concept is far more developed than the source material currently supports.
- **Novelty remaining for subsequent work:** Terminal — nothing follows it in this programme.
- **Overlap risk:** Low.
- **Salami-slicing risk:** Not applicable; the risk here is *premature publication*, addressed by strict sequencing (last).
- **Audience type:** Interdisciplinary / AI governance / systems.

**Assessment:** Structurally the strongest option of the three tested so far — but treats B1, B2, and B3 as the same *kind* of artifact, which undersells B3's actual character (closer to a position paper than a systems paper) and under-serves B2's actual character (a claim with a real, gatherable empirical answer that deserves a format including the evidence-gathering, not just an essay stating the diagnosis).

---

## Architecture C — Academic + practitioner hybrid

Same three claim-cluster boundaries as Architecture B, each assigned the register matching its actual epistemic character.

### C1 — Practitioner pattern article

Identical in content to A1/B1, but explicitly framed by register: a practitioner-facing pattern article (O'Reilly-style), not a systems paper. **Already substantially complete** — see `oreilly-role.md`.

### C2 — Rigorous systems/architecture paper with integrated empirical study

Same research question, thesis, contribution, dependency, and prior-art fields as B2, but explicitly specified as a **systems/architecture paper format that includes the empirical work as a first-class section**, not an essay that merely asserts the diagnosis. Audience type: systems / academic / AI governance.

### C3 — Conceptual/interdisciplinary essay

Same research question, thesis, and dependency as B3, but explicitly specified as a **shorter, conceptual essay format**, not forced into systems-paper structure, and explicitly not required to include an experiment it was never going to have (per `empirical-program.md`'s deliberate scoping decision). Audience type: interdisciplinary / thought-leadership / AI governance.

### C4 — Optional capstone synthesis (deferred)

A later O'Reilly/book-level piece tying C1–C3 together for practitioners, once C2 and C3 exist. Not scheduled; treated fully in `oreilly-role.md` and `book-implications.md`.

**Assessment:** Highest novelty-preservation of the three (C2 is not judged by essay standards it wasn't meeting, C3 is not judged by experimental standards it was never attempting), at the cost of more coordination overhead — two distinct registers, explicit editorial judgment required about which claims go where, four deliverables instead of two or three. Directly serves the "genuinely strong individual articles" and "preserve the deepest thesis until properly supported" criteria more precisely than B does, by removing the register mismatch B's uniform treatment would otherwise create.

---

The recommendation among these three, with full reasoning against the priority order given in Task 9, is in `recommended-program.md`.
