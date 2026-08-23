---
id: note-contribution-02-deferred-contribution-03
title: "Contribution 2 Audit — Material Deferred to Contribution 3"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, contribution-03, deferred, scope-discipline]
refs: [../claim-graph.md, ../conceptual-inversions.md]
---

## Material Encountered and Deferred to Contribution 3

Scope: Task 15. No synthesis, no development — a bare log of material
encountered during this audit that belongs to Contribution 3 (capability vs.
understanding; the fragmentation of explainability/observability/governance;
the Understanding Layer; epistemic debt; broad historical claims about
software engineering). Per the brief: source, one-sentence relevance, why
deferred. Nothing here should be read as advancing Contribution 3's
argument.

---

- **Source:** Source A, "Why capability is advancing faster than
  understanding" (full essay section).
  **Relevance:** Frames explainability, interpretability, observability,
  provenance, governance, and auditability as fragmented, parallel
  responses to one deeper problem.
  **Why deferred:** This is Contribution 3's central fragmentation claim
  (C9a/C9b in `../claim-graph.md`); Contribution 2 needs only the narrow
  claim that decision-provenance binding is under-solved, not the broader
  claim that all of these fields are secretly one field.

- **Source:** `../claim-graph.md`, node C9m ("The recurring preservation
  pattern in software engineering").
  **Relevance:** Encountered while sourcing the general software-engineering
  analogy (version control, transaction logs, tracing as recurring
  responses to complexity).
  **Why deferred:** This audit used version control, event sourcing, and
  tracing only as specific, narrow prior-art comparisons for Contribution
  2's technical claims — not as instances of a general historical pattern
  about software engineering's relationship to complexity, which is
  Contribution 3's own claim, flagged in `../claim-graph.md` as requiring a
  dedicated, not-yet-done historical/comparative literature review (Step 6
  in `../research-roadmap.md`).

- **Source:** OAIS Reference Model (ISO 14721) and the OCLC/RLG
  "Preservation Metadata and the OAIS Information Model" framework document,
  encountered during the digital-preservation prior-art search.
  **Relevance:** OAIS's broader archival-science framing of "authenticity"
  and "long-term interpretability of records" touches on epistemological
  questions (what does it mean for a record to remain meaningful/
  interpretable decades later) that go beyond Contribution 2's narrower,
  technical reconstruction-of-a-specific-decision claim.
  **Why deferred:** Contribution 2 uses OAIS only for its concrete PDI
  (Preservation Description Information) structure as a conceptual
  analogue, per `prior-art-audit.md`; it deliberately does not engage OAIS's
  broader archival-science literature on authenticity-as-a-philosophical-
  property, which would drift toward Contribution 3's or the "digital
  preservation" literature's deeper epistemological territory the brief
  explicitly excludes.

- **Source:** NIST AI Risk Management Framework, "Govern" function
  (encountered indirectly via `../research-program/aigov-role.md` and
  `article-01-decision-level-control/novelty-audit.md`, not re-researched in
  this pass).
  **Relevance:** Organizational/process-level treatment of AI risk across a
  full system lifecycle; potentially relevant background for Contribution
  3's discussion of how governance, explainability, and auditability
  literatures describe their own relationships to one another.
  **Why deferred:** Already flagged for Contribution 3 in
  `../article-01-decision-level-control/novelty-audit.md` Task F; not
  re-engaged here because this audit's object (decision-time binding) does
  not depend on organizational governance-process framing.

- **Source:** Deontic Policies / AgenticRei paper (arXiv:2606.19464),
  encountered previously in `../article-01-decision-level-control/
  novelty-audit.md` and referenced again during this audit's search for
  agentic-runtime governance literature.
  **Relevance:** The paper's obligation-lifecycle and dispensation semantics
  (permissions that must be tracked and honored over a time horizon, and
  conditions that waive them) are conceptually adjacent to broader questions
  about how autonomous systems maintain normative context over time —
  arguably touching Contribution 3's territory on what autonomy requires of
  system self-knowledge.
  **Why deferred:** Contribution 2 uses this paper's relevance only
  narrowly, as confirmation that current academic work in agentic
  governance already exceeds the simple permit/prohibit vocabulary
  Contribution 1 uses (already noted in the prior audit); this pass does
  not extend that into any claim about autonomous systems' general
  epistemic requirements, which belongs to Contribution 3 if pursued at
  all.

- **Source:** General "observability ≠ explainability" folklore in
  distributed-systems engineering, quoted within Source A itself ("the
  existence of telemetry does not guarantee the existence of explanation")
  and encountered again during the OpenTelemetry prior-art search.
  **Relevance:** This is close to a general epistemic claim about the limits
  of instrumentation — exactly the register Contribution 3 operates in.
  **Why deferred:** This audit uses the same underlying fact only in its
  narrow, technical form (Objection 6: tracing answers how, not why, for a
  specific decision) — not as evidence for a general claim about
  observability's relationship to "understanding" as a systems property,
  which is Contribution 3's claim.

- **Source:** Aviation FDR/CVR incident-investigation practice, researched
  in this pass as a safety-critical-industry analogue (flagged as
  unresearched in `../conceptual-inversions.md` Inversion E).
  **Relevance:** The observation that even the most mature reconstruction-
  oriented engineering discipline treats execution-preservation and
  regulatory/authority-preservation as separate systems could be read as
  supporting a broader claim about engineering's general relationship to
  "understanding" as capability grows — Contribution 3's territory.
  **Why deferred:** This audit uses the aviation analogy only for its
  narrow, structural content (execution reconstruction ≠ justification
  reconstruction, confirmed institutionally) in `prior-art-audit.md`; it
  does not extend the analogy into a general claim about safety-critical
  industries "investing in understanding" as capability grows, which would
  be Contribution 3's C9m-adjacent historical-pattern argument, not
  Contribution 2's.
