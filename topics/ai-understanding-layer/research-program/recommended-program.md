---
id: note-research-program-recommended-program
title: "Research Programme — Recommended Architecture and Adversarial Self-Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, recommendation, adversarial-review]
refs: []
---

## Research Programme — Recommended Architecture and Adversarial Self-Review

Scope: Task 9, plus the brief's required adversarial self-review, which is treated as gating this recommendation rather than as a closing formality — if either of the two decisive self-review questions had returned "no," this recommendation would need to be rewritten, not merely footnoted.

---

## Task 9 — Recommendation

### Recommendation: Architecture C, built on Architecture B's claim-cluster boundaries

Optimizing in the order specified:

1. **Intellectual strength.** Each unit argued in the register that earns it credibility — an experiment where an experiment answers something (C2), historical/comparative argument where that is the only honest form of evidence available (C3), a complete architecture argument where the mechanism question is already settled (C1).
2. **Defensible novelty.** Confirmed per-contribution in `contribution-boundaries.md`: C1 is a new synthesis, not a new mechanism (audited); C2 is the freshest, least-collided material in the programme (Inversions D/E, 5/5 disruptive potential); C3 is explicitly protected from premature, under-evidenced publication.
3. **Cumulative argument.** Control → provenance → understanding, without requiring acceptance of the deepest, hardest claim before the concrete, already-demonstrated one.
4. **Independent falsifiability.** Each contribution has its own, distinct falsification condition (`contribution-boundaries.md`) — none borrows another's evidence to appear falsifiable.
5. **Evidence quality.** Matching form to substance means C2's evidence is genuinely gathered (not merely asserted) and C3's evidence is genuinely historical/comparative (not a forced pseudo-experiment) — this criterion is precisely what distinguishes Architecture C from B.
6. **Minimal duplication.** By construction (Task 4/5 in `contribution-boundaries.md`).
7. **Preservation of deeper later contributions.** C3 is explicitly sequenced last and explicitly barred from carrying C8/F alone (Inversion F) or from being drafted before its own historical/prior-art audit.
8. **Usefulness to the eventual O'Reilly synthesis.** A three-part structure maps directly onto a natural synthesis arc — see `oreilly-role.md`.
9. **Usefulness to the eventual book.** See `book-implications.md` — the three-contribution structure maps onto a three-part book arc more naturally than either a two-unit or a uniform-register structure would.

**Why Architecture A loses:** Rejected primarily on criteria 2 and 5 — bundling C6/C7 (defensibility 3/5, real falsification path) with C8/C9 (defensibility 2/5, no clean falsification path) into one document lets the weak half drag down the strong half's credibility.

**Why Architecture B loses to C:** B gets the claim boundaries right (identical content to C) but loses specifically on criterion 5 (evidence quality) and, secondarily, criterion 1 (intellectual strength) — forcing C2 and C3 into the same register as each other (implicitly, "a paper") either strips C3 of its honest interpretive character or holds C2 to a lighter evidentiary bar than its falsifiable claims deserve. C wins by keeping B's exact claim-cluster boundaries while fixing this register mismatch.

### What this recommendation does not decide

Venues (out of scope). C2's or C3's exact thesis wording (pending the audits in `research-roadmap.md`). Any timeline commitment for the optional capstone (C4) — see `oreilly-role.md`.

---

## Adversarial self-review

The brief requires this before the recommendation stands. Each question is answered against the claim graph and prior-art work, not against the recommendation's own convenience.

### 1. Are we actually studying one problem or several loosely connected ones?

**One problem at the framing level, two genuinely distinct sub-problems at the research level — not "loosely connected."** The claim graph (`claim-graph.md`) shows a single shared root (C1, output ≠ decision) branching into two clusters with independent truth conditions and independent evidence types. "Loosely connected" would imply the branches don't actually share a real logical root; they do — C1 is a genuine, load-bearing premise for both, not a rhetorical bridge invented to make two unrelated topics look unified.

### 2. Does decision-level authorization logically lead to historical reconstruction, or are we forcing the connection?

**No — and this is the single most important finding to carry forward.** Per `claim-graph.md`'s dependency diagram, C5 does not entail C6; they are siblings sharing only C1. The original three-article decomposition's linear framing ("Decision-Level Control → State Is Not Knowledge → Understanding Layer") implied a forced logical progression the claim graph does not actually support. This is not a flaw in the earlier work — it was a reasonable narrative hypothesis — but it does not survive this adversarial test as a *logical* claim, only as a *possible publication sequence* (which remains defensible on rhetorical/pedagogical grounds, per `research-roadmap.md`, even though not on logical-entailment grounds).

### 3. Does historical reconstruction logically lead to capability-vs-understanding, or is another premise missing?

**A premise is missing, and this pass identifies it explicitly for the first time.** C6/C7 are scoped to *decisions specifically*. C8/C9 generalize to *system behavior broadly* (model internals, non-decision behavior, explainability, observability). The move from "decision-specific reconstruction fails" to "AI system understanding in general is at risk" requires an additional generalizing premise — something like "the decision-reconstruction problem is illustrative of a more general preservation-of-understanding problem across AI system behavior broadly" — that Source A asserts rhetorically but does not argue for directly. This is flagged as an open gap in `claim-graph.md`'s Task 1 analysis and must be addressed explicitly in Step 6 of `research-roadmap.md` (the C9m historical audit) before C3 is drafted — either by arguing the generalization properly, or by scoping C9's eventual thesis down to "AI decision behavior specifically," a more modest but fully defensible alternative.

### 4. Is "Understanding Layer" a real architectural concept or merely a memorable label?

**Currently, a memorable label, not a specified architecture.** No interfaces, components, or implementation sketch exist anywhere in Source A beyond the AIGov Core anecdote, which `aigov-role.md` shows does not actually describe gate/enforcement mechanics or, in fact, any specific architecture beyond "preserve evidence, authority, policy context, and assumptions." Source A itself concedes this ("whether this particular approach is correct remains an open question"). `contribution-boundaries.md` and `claim-graph.md` (C9b) both already recommend framing this claim explicitly as a problem statement / call for architecture rather than a proposed design — this self-review question confirms that framing is not merely cautious but necessary.

### 5. Is "state is not knowledge" technically precise enough?

**Not yet, for a rigorous audience.** Flagged explicitly in `claim-graph.md`'s C6 entry: "knowledge" does significant informal work; a technically tighter formulation ("retained system state does not entail retained justificatory context," or similar) should be adopted before C2's paper is drafted. The evocative phrase is appropriate for practitioner framing (and is retained, correctly, in `oreilly-submission-disruptive.md`'s register) but not yet precise enough for a systems paper's thesis statement. This precision work belongs in Step 2 of `research-roadmap.md`.

### 6. Is the model-centric critique fair to modern MLOps / agent architectures?

**Fair, provided the existing concessions are maintained, not extended into an unfair version.** `novelty-audit.md` and both O'Reilly drafts already explicitly concede MLflow, Databricks Unity Catalog, and Vertex AI Model Registry prior art, and MCP's human-in-the-loop consent model. The critique would become *unfair* if restated as "MLOps/agent tooling has no decision-level constructs at all" — which this programme has consistently not claimed. The fair, checked claim is narrower: these tools govern model *versions* and *approval states*, not a general, model-agnostic decision-boundary abstraction that generalizes across model boundaries (the "one model, many decisions" point) — a distinction, not an omission, in existing tools.

### 7. Are we rediscovering access control, provenance, event sourcing, observability, or safety engineering under new names?

**Partially yes, by design, and stated as such throughout.** `novelty-audit.md`'s Position B verdict (new synthesis, not new mechanism) and Inversion G in `conceptual-inversions.md` both confirm this directly rather than deny it. The honest answer is: yes for the mechanisms (access control, admission control, supply-chain attestation, transactional commit are all pre-existing and explicitly credited); no for the AI-specific application (the model-vs-decision critique, the transient-context problem) and no for the meta-level synthesis connecting decision-level control and long-horizon preservation as siblings of one shared root problem, which — as far as the research conducted so far shows — is not an existing packaged argument elsewhere.

### 8. What remains specifically novel after all prior-art collisions are acknowledged?

Three things survive rigorous testing: (1) the evidenced observation that ML-specific tooling has not yet absorbed access control's request-level (not identity-level) authorization lesson — still organizing around the model (Inversion A); (2) the evidenced observation that existing preservation tooling (Git, transaction logs, tracing, SLSA) was not built to capture AI-specific transient context (Inversions D/E); (3) the meta-level synthesis connecting these two as siblings sharing one root cause — AI engineering's dominant abstraction remaining the model rather than the decision (Inversion G). Everything else in the programme reduces, honestly, to "apply a known mechanism here too."

### 9. Could the deepest programme survive if AIGov Core did not exist?

**Yes.** Established directly in `aigov-role.md`: every claim in `claim-graph.md` is sourced to Source A's or Source B's text, or to this programme's own reasoning during O'Reilly drafting — not to AIGov Core's existence, design, or any result from it (of which there are none; `aigov-role.md`'s theory→evidence table shows zero evidence currently attaches to AIGov Core). AIGov Core is useful as motivating color for Contribution 2 and as a future implementation target; it is load-bearing for nothing in the graph.

### 10. Could the deepest programme survive if the O'Reilly article were never published?

**Yes.** The claim graph is derived from Source A and Source B directly. The O'Reilly drafting *process* was genuinely useful for discovering C1b (model-is-wrong-unit) and C5h (human-in-the-loop) — but once discovered, those claims stand on their own reasoning (illustrated by the concrete "one LLM, four decisions" example and the HITL authority/evidence/refusal analysis), not on the fact of a specific article's publication. If `oreilly-submission-disruptive.md` were deleted tomorrow, Contribution 1's thesis, evidence, and prior-art mapping (`article-01-decision-level-control/novelty-audit.md`, `sourcing-audit.md`) would remain fully intact as research artifacts independent of that one downstream draft.

### Gate result

**Both decisive questions (9 and 10) return "survives."** Per the brief's own stated rule, this means the research programme is not too dependent on implementation or publication framing, and the recommended architecture stands without requiring revision on this account. The two genuine open items surfaced by this self-review — the missing generalizing premise between C6/C7 and C8/C9 (Q3), and the imprecision of "state is not knowledge" as a technical formulation (Q5) — are carried forward as explicit, named tasks in `research-roadmap.md` rather than left as unaddressed caveats.
