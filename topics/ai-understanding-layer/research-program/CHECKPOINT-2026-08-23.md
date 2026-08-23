---
id: note-ai-understanding-layer-checkpoint-2026-08-23
title: "AI Understanding Layer — Research Programme Checkpoint (2026-08-23)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [checkpoint, resume-document, programme-status]
refs: [research-program/research-roadmap.md, research-program/contribution-boundaries.md]
---

# Research Programme Status — Resume Document

This file exists so a future session can resume this programme without
reading the full prior conversation history. It is a snapshot as of
2026-08-23; treat any claim about "current" repository state as frozen at
this commit, not as live fact — verify against the actual files before
acting on anything below.

---

## Contribution 1 — Decision-Level Control

**Status: substantially complete.**

- Complete: spine, evidence inventory, three drafting iterations
  (`draft-v1.md`, `draft-v2.md`), a full adversarial prior-art audit
  (`novelty-audit.md`, verdict: **Position B — new synthesis, not new
  mechanism**), and a claim-by-claim sourcing audit (`sourcing-audit.md`).
  Two O'Reilly-facing drafts exist (`oreilly-submission-draft.md`,
  `oreilly-submission-disruptive.md`).
- No mechanism novelty is claimed anywhere in this material — every draft
  explicitly concedes the underlying mechanisms (access control, admission
  control, supply-chain attestation) are pre-existing; the claimed
  contribution is the model-vs-decision synthesis and framing.
- **What remains:** no further research is required for this contribution
  to stand on its own. Whether either O'Reilly draft is actually submitted
  for publication is an open, human decision not made by this programme
  (see "O'Reilly status" below).

---

## Contribution 2 — Preservation & Reconstruction

**Status: prior-art audit complete; experiment designed; NOT implemented;
NOT executed; NO results exist.**

- **Prior-art verdict:** **B — narrowed survival**
  (`research-program/contribution-02/novelty-verdict.md`). Every
  individual primitive needed (bitemporal valid-time semantics, W3C PROV
  lineage, in-toto/Sigstore attestation, event-sourced replay) already
  exists in mature, separate literatures; none is applied by default to
  the AI-specific set of transient dependencies (prompts, live retrieval,
  policy-as-config, delegated authority), and no existing artifact
  combines them with an explicit per-decision binding for this purpose.
- **Surviving thesis:** "State Is Not Knowledge" is retired as the
  technical thesis (retained only as practitioner-register color).
  Replacement: *retained system state does not, by default, bind a
  decision to the temporally valid versions of the evidence, policy, and
  authority that made it valid when it occurred.* Working shorthand:
  **"Versioned is not bound."**
- **Experiment design status:** Complete
  (`research-program/contribution-02/experiment-design/`, 10 files).
  Design verdict: **READY FOR IMPLEMENTATION.** Compares Regime B
  (independently versioned, unbound) against Regime C (versioned and
  explicitly bound at decision time) as the scientific center, with Regime
  A (bare) as a floor/manipulation-check condition. Primary metric:
  Temporal Correctness; primary diagnostic metric: False Historical
  Confidence. Uses a pre-registered, pattern-based diagnostic evaluation
  over a ~10-case perturbation matrix and a deterministic (not human or
  LLM) reconstruction procedure, deliberately to avoid conflating
  information-architecture sufficiency with investigator skill.
- **NO experiment code exists. NO experiment has been run. NO results —
  positive, negative, or partial — exist anywhere in this repository.**

---

## Contribution 3 — The Understanding Layer

**Status: reserved. Not drafted. Not developed.**

- Its research gaps remain exactly as `claim-graph.md` and
  `research-roadmap.md` Step 6 describe them: a dedicated
  historical/comparative literature review (does the software-engineering
  "recurring preservation pattern" claim survive scrutiny — e.g., Git's
  actual origin is distributed collaboration/merge-conflict resolution,
  not explicitly "preserving knowledge," a complication flagged but not
  yet investigated) and a resolution of the missing generalizing premise
  between decision-specific reconstruction (Contribution 2) and
  system-behavior-wide "understanding" (Contribution 3) — flagged in
  `recommended-program.md`'s adversarial self-review (Q3) and never
  argued for directly in either primary source.
- Material encountered during the Contribution 2 audit that touches this
  territory was logged, not developed, in
  `research-program/contribution-02/deferred-contribution-03.md`.
- **This contribution must not be started before Steps 1 (done), 5
  (Contribution 2 drafting, not yet reached — see "Next exact action"
  below), and 6 (this literature review) are complete**, per
  `research-roadmap.md`'s explicit sequencing and the terminal-thesis
  protection reconfirmed across both prior adversarial passes.

---

## Current Publication Architecture

**Approved: three independent contributions**
(`contribution-boundaries.md`, Task 5), **sharing one root premise (C1:
output ≠ decision) but branching from there — not a strict linear chain.**

```
                  MODEL LEVEL (substrate, not a claim)
                        │
                        ▼
                 DECISION LEVEL (C1 — shared root)
                        │
           ┌────────────┴────────────┐
           ▼                         ▼
  CONTRIBUTION 1                HISTORICAL / PROVENANCE LEVEL
  Decision-Level Control        CONTRIBUTION 2
  (terminal on this branch)     Preservation & Reconstruction
                                         │
                                [generalizing premise,
                                 not yet argued]
                                         │
                                         ▼
                                CONTRIBUTION 3
                                The Understanding Layer
                                (terminal; requires 1 and 2
                                 as earned scaffolding first)
```

**This branching structure matters operationally:** Contribution 2 depends
only on Contribution 1's shared premise (C1), not on Contribution 1's
architecture, its drafts, or its publication status. Contribution 2's
prior-art audit and experiment design were correctly able to proceed
without waiting on any further Contribution 1 work, and did.

---

## O'Reilly Status

Two O'Reilly-facing drafts exist for Contribution 1 only
(`article-01-decision-level-control/oreilly-submission-draft.md` and
`oreilly-submission-disruptive.md`). **No further O'Reilly work is
required before resuming this programme.** Whether either draft is
actually submitted for publication is a decision this programme has not
made and does not make automatically — it requires an explicit human
choice to publish Contribution 1 separately, at whatever time that is
wanted. Nothing in Contribution 2's or Contribution 3's status depends on
that decision being made first.

---

## Book Status

The original book proposal (`sources/source-b-original-book-proposal.md`)
remains **source material only** — a verbatim historical capture, not a
draft. It has **not** been rewritten against the mature three-contribution
research programme that has since developed well beyond its original
scope (the proposal's own "controlled failure experiments" and
"repository audit" methodological claims were re-examined and substantially
redesigned for Contribution 2 in `empirical-program.md` and
`contribution-02/empirical-next-step.md` — the proposal's originally
intended use of those methods for Contribution 1 was found less
well-motivated than their redesigned use for Contribution 2). No decision
has been made about whether or when to revise the book proposal itself.

**Note on this file specifically:** as of this checkpoint, the personal
mailing address, phone number, and email fields in that source document
have been redacted (by explicit author instruction, given this repository
is public) — see the redaction note at the top of that file. No other
content was altered.

---

## Next Exact Action

**Implement the approved Contribution 2 reconstruction experiment from
`research-program/contribution-02/experiment-design/implementation-spec.md`,
then execute it only after a human confirms the design.**

This is a two-step gate, and both steps require explicit human
authorization before proceeding — this is the frozen workflow for this
programme going forward:

1. A human reviews the experiment design
   (`contribution-02/experiment-design/README.md` is the entry point) and
   either approves it, requests changes, or rejects it.
2. Only after approval does implementation begin; only after
   implementation is reviewed does execution begin. No session should
   implement or execute this experiment without that explicit
   authorization having been given in the conversation that does so.

---

## Known Open Questions

Only items that materially affect the next phase are listed; resolved
questions from earlier passes are not repeated here.

1. **Case 10's boundary-precision question** (`implementation-spec.md`,
   Section 5 and Section 7): whether the concurrency-ambiguity case should
   be built as a genuine fault-injection test or documented as a
   structural limitation of the synthetic design — left open for the
   implementer, not resolved by this checkpoint.
2. **External validity beyond the synthetic testbed** is explicitly
   unaddressed by the current design (`validity-and-confounders.md`) — a
   real-system follow-up study is anticipated but not designed.
3. **The missing generalizing premise for Contribution 3** (Q3 in
   `recommended-program.md`'s adversarial self-review) remains unresolved
   and gates Contribution 3's drafting, not Contribution 2's — no action
   needed until Contribution 2's own drafting (Step 5) is reached.
4. **Whether to submit either Contribution 1 O'Reilly draft** is an
   open human decision, independent of and not blocking any further
   research step.
5. **Whether/how to revise `source-b-original-book-proposal.md`** beyond
   this checkpoint's contact-info redaction remains undecided.
