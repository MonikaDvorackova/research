---
id: note-contribution-02-minimal-decision-record
title: "Contribution 2 — Minimal Decision Record (Conceptual Justification Only)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, decision-record, minimal-necessary-fields]
refs: [problem-formalization.md, temporal-semantics.md, prior-art-audit.md]
---

## Contribution 2 — Minimal Decision Record

Scope: Task 8. This is **not** a product schema. It asks only what
information is minimally necessary to answer, at t1, the justification
question G defined in `problem-formalization.md`: *why was D authorized at
t0?* Each candidate field is classified and compared against the existing
schemas surveyed in `prior-art-audit.md` (PROV, in-toto Predicates, SLSA
provenance, bitemporal record structure).

---

## Classification method

- **Necessary** — G is unanswerable without it, for at least one realistic
  drift scenario identified in `problem-formalization.md` or
  `collision-tests.md`.
- **Conditionally necessary** — required only when a specific sub-problem
  (C/D/E/F) is in scope for a given decision class; not universal.
- **Useful** — improves confidence or efficiency of reconstruction but is
  not itself load-bearing for answering G.
- **Unnecessary** — does not serve reconstruction; excluded even if it
  might serve other purposes (compliance reporting, debugging), to keep the
  record's scope disciplined.

---

## Field-by-field analysis

| Field | Classification | Why |
|---|---|---|
| **Decision identifier** | Necessary | Without a stable identifier, nothing else in the record can be addressed or queried later. This is the minimum structural requirement of having a record at all. |
| **Timestamp (decision time)** | Necessary | This is the query point every other binding is evaluated against (see `temporal-semantics.md`). Without it, "valid at t0" has no t0 to resolve against. |
| **Proposed action** | Necessary | Answers sub-problem A trivially, but is required as context for interpreting everything else in the record — evidence and policy are only meaningful relative to a specific proposed action. |
| **Resulting action / state transition** | Necessary | Distinguishes what was proposed from what actually took effect (they can differ, e.g., partial execution, downstream failure) — without this, G's "why was D valid" is ambiguous about which D is being asked about. |
| **Model/version identifiers** | Necessary | Sub-problem B's minimum requirement; also frequently a precondition for evidence to be interpretable (a retrieval result's relevance depends on the embedding model version that selected it). |
| **Evidence references, bound to a specific snapshot/version** | Necessary | This is the core of sub-problem C and the specific gap the audit found unaddressed by default (`prior-art-audit.md`). A reference to a *live, mutable* source (a document ID with no version pin) does not satisfy this — the reference must resolve to an immutable snapshot. |
| **Evidence-validity assertion (was this evidence considered current/accurate at t0)** | Conditionally necessary | Required whenever the decision class involves evidence whose accuracy can drift independent of its retrieval (e.g., a fact document, a compliance status) — not required for evidence that is definitionally always current (e.g., "did the model output exceed threshold X," which is self-evidently valid at its own generation time). |
| **Policy identifier and version** | Necessary | Sub-problem D's core requirement — without this, "why" collapses to "we don't know which rule applied." |
| **Policy-effective interval (valid time)** | Necessary | A version identifier alone does not establish that this version was the operative one at t0 rather than a version recorded later with a backdated effective time (see the retroactive-correction case in `temporal-semantics.md`) — the interval, not just the identifier, is what closes that gap. |
| **Authority (who/what approved, under what delegation)** | Necessary | Sub-problem E's core requirement. An "approved" flag with no named authority and no delegation basis is not distinguishable, at t1, from an unauthorized action that merely wasn't blocked. |
| **Authority-validity interval** | Conditionally necessary | Required whenever roles/delegations are mutable over time (nearly always in practice) — not required only in the degenerate case of a system with a single, permanently fixed authority for the decision class in question. |
| **Approval / escalation record (if human-in-the-loop)** | Conditionally necessary | Required only for decisions with an ESCALATE-shaped path (Contribution 1's vocabulary, imported here only because it is the natural description of this specific field, not as a broader dependency). Not applicable to fully automated decisions. |
| **Relevant configuration (thresholds, feature flags, sampling parameters active at t0)** | Conditionally necessary | Necessary specifically when configuration values are themselves decision-relevant (e.g., a threshold read from a live config service) — this is sub-problem F's most common concrete instance, and should be captured only for configuration values actually consulted by the decision logic, not exhaustively. |
| **Provenance links (to upstream entities/activities/agents, PROV-shaped)** | Useful | Improves the record's queryability and its ability to compose with existing provenance tooling (`prior-art-audit.md`'s PROV entry), but the record can answer G without a full PROV graph if the necessary fields above are present in a simpler form. |
| **Integrity information (signature, hash, transparency-log inclusion proof)** | Useful | Establishes that the record itself was not altered after t0 (in-toto/Sigstore-shaped, per `prior-art-audit.md`) — this protects trust *in* the record but does not add reconstructive content; a perfectly signed record that omits a necessary field is still insufficient, and an unsigned record with all necessary fields is reconstructively complete, only less trustworthy. |
| **Free-text justification / rationale** | Useful, not necessary | Where a human articulated *why* the evidence satisfied the policy, capturing that rationale directly answers G's normative-synthesis half without requiring the investigator to re-derive it. But it cannot be made structurally required, because for fully automated decisions no such rationale is ever authored — the record must remain reconstructable from the structural fields (evidence + policy + authority bindings) even when this field is absent. |
| **General-purpose observability data (full trace, all logs)** | Unnecessary as part of *this* record | Valuable for sub-problem B and for debugging, but including it in the decision record itself conflates execution-reconstruction (already well-served, per `problem-formalization.md`) with the specific justification content this record exists to guarantee. Should remain a separate, cross-referenced artifact, not a field of the decision record. |
| **Business/compliance metadata unrelated to validity (e.g., cost center, ticket number)** | Unnecessary | Serves organizational bookkeeping, not reconstruction. Including it would blur the record's disciplined scope and invite scope creep toward "record everything," which `collision-tests.md` Objection 9 shows is neither achievable nor the right target. |

---

## The one property none of the fields individually supply

Every field above, taken alone, is a reference or an identifier. **The
record's actual work is the binding**: the explicit, decision-time act of
asserting that *this* evidence snapshot, *this* policy version, and *this*
authority were the ones treated as operative for *this* decision, recorded
at t0, immutably. This is the structural element that distinguishes the
minimal decision record from a mere aggregation of pointers into
already-versioned systems — and it is exactly the property that
`collision-tests.md` Objection 8 shows is not automatically produced by
versioning infrastructure existing elsewhere, however complete that
infrastructure is.

---

## Comparison against existing schemas

- **Against in-toto's Statement/Predicate structure:** The minimal record
  above could be expressed as an in-toto Predicate type (a "decision
  justification" predicate), reusing the Statement envelope for signing and
  Rekor for tamper-evidence. This is a legitimate and probably the most
  practical implementation path identified in this audit — but no such
  predicate type exists today, and defining one is genuinely new,
  undone work, not a citation of existing practice.
- **Against W3C PROV:** The record's evidence/authority/policy bindings map
  cleanly onto PROV's Entity/Activity/Agent/Association/Delegation
  relations, but PROV alone cannot express the policy-effective-interval or
  authority-validity-interval fields without a bitemporal extension PROV
  does not natively provide (confirmed in `prior-art-audit.md`).
- **Against SLSA provenance:** SLSA's buildDefinition/runDetails split is
  structurally analogous (what was decided / how it executed) but is scoped
  to build platforms, not decision-authorization logic — the analogy is
  useful for the record's *shape*, not reusable as-is for its *content*.
- **Against EU AI Act Article 12's minimum content:** The Act's specified
  minimum (period of use, reference database, matched input, verifying
  person) is a strict subset of the fields above — it covers roughly the
  "resulting action" and "approval record" fields and none of the
  policy-version, policy-effective-interval, evidence-validity, or
  authority-validity fields. A system meeting only the Article's minimum
  would not satisfy this record's necessary-field set.

**Conclusion:** No existing schema, used as-is, already constitutes this
record. An in-toto-shaped predicate type populated with these fields is the
most direct available implementation path, but assembling it is exactly the
"useful synthesis" the novelty verdict (`novelty-verdict.md`) attributes to
Contribution 2 — not a rediscovery of an existing artifact.
