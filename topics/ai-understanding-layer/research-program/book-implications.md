---
id: note-research-program-book-implications
title: "Research Programme — Implications for the Original Book Proposal"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, book-proposal, source-b]
refs: []
---

> **SUPERSEDED NOTICE (2026-08-25):** The three-part book arc proposed
> below (Parts I–III mirroring Contributions 1–3) assumed Contribution 3
> would become a full capstone. It is now retained as a supporting
> research note instead — see `PUBLICATION-ARCHITECTURE-FINAL.md`. The
> current recommendation on O'Reilly format is "article first, book
> later" (`OREILLY-SYNTHESIS-MAP.md` §11), not a book proposal at this
> document's originally assumed scope. This document's chapter-by-
> chapter diagnosis of Source B remains a useful historical analysis and
> is left unmodified; the strict claim-by-claim audit in
> `OREILLY-SYNTHESIS-MAP.md` §7 supersedes it as the current
> authoritative version.

## Research Programme — Implications for the Original Book Proposal

Scope: Task 11. Diagnosis only, as instructed — the book proposal itself is not rewritten here. Answers all nine sub-questions from the brief in order, returning to the complete Source B, not a summary of it.

### 1. Is Evidence-Gated AI still the central intellectual theory?

**No.** The claim graph (`claim-graph.md`) places Evidence-Gated AI's underlying architecture (C5) as the terminal node of exactly one branch of the programme — Contribution 1 — which shares only its root premise (C1, output ≠ decision) with the sibling Contribution 2/3 branch. It is not the root of everything; it is one of two things the shared premise gives rise to.

### 2. Or is Evidence-Gated AI an architectural mechanism inside a deeper theory?

**Yes.** This confirms and sharpens `novelty-audit.md`'s Position B finding and `../notes/intellectual-progression.md` (Task 7)'s prior finding that Evidence-Gated AI is "one enforcement mechanism," orthogonal to preservation. The precise structural reason: C5 answers the control question ("is this action authorized right now"); Contributions 2 and 3 answer the understanding question ("will anyone be able to know why, later, at increasing scope"). Evidence-Gated AI answers only the first.

### 3. Is decision-level auditability deep enough to organize a 250–300 page book?

**No.** It is deep enough to organize Part One (roughly the original Chapters 1–9), but the claim graph shows a whole sibling branch (Contributions 2 and 3) it does not touch or subsume. Organizing the entire book around it would either omit that material or force it in as an under-motivated addendum — the same dilution risk identified for Architecture A in `publication-architectures.md`, now applied to book structure.

### 4. Is the deeper organizing concept instead decision architecture, preservation of system knowledge, capability vs. understanding, understanding architecture, or something else?

**Understanding/knowability (Contribution 3's territory) is the strongest candidate for the book's title-level thesis, with decision architecture (Contribution 1) and preservation of system knowledge (Contribution 2) as its two operationalizing movements** — not four competing candidates but a nested structure, where the book's outer thesis is the terminal one and its parts operationalize it at different time horizons: present-tense control, then retrospective preservation, then the general synthesis. This mirrors the recommended publication architecture's three units, sequenced by actual research readiness (control first, provenance second, understanding last), the same sequencing logic `research-roadmap.md` uses for papers, now applied to book structure.

### 5. Which original chapters survive?

Chapters 1, 3, 4, 6, 7, 8, 9 (Why AI Systems Fail in Production; From Outputs to Decisions; Evidence as a First-Class Concept; Enforcement — Making Rules Real; CI Gates for AI Systems; Approval and Risk Review; System Architecture) survive largely intact as Part One material, and are now **stronger** than the original outline anticipated: the model-vs-decision inversion (C1b/C1c) and the "one model, many decisions" argument, discovered only during this programme's own O'Reilly drafting, were absent from Source B's original chapter descriptions and materially deepen what these chapters can now argue. Chapter 8 ("Approval and Risk Review") specifically gains the C5h human-in-the-loop critique (authority, evidence, scope, refusal, enforcement must all be explicit), which the original outline did not have.

### 6. Which original chapters should merge?

**Chapter 2 ("The Missing Layer — Decision Systems") and Chapter 3 ("From Outputs to Decisions") should merge.** Re-reading Source B closely: Chapter 2's own description ("Defining decision-level architecture") and Chapter 3's ("Why model outputs are not decisions") are, per the claim graph, the same claim cluster (C1/C1c/C1b) split across two chapters for narrative pacing rather than because they are logically distinct — exactly the kind of split `contribution-boundaries.md`'s ten-question test would flag as under-motivated at the chapter level, mirroring the paper-level finding that C1/C1c/C1b do not sustain independent treatment. Merging them would tighten Part One without losing content, and would make room for the additional inversion material (C1b, discovered during drafting) that neither original chapter anticipated.

### 7. Which original chapters become too narrow?

**Chapter 5, "Auditability as a System Property — what it means and how to achieve it,"** is under-scoped. The original proposal implicitly treated auditability as one property achievable via evidence + enforcement (C5-level machinery). C6's entire point is that this is false in general: a perfectly evidenced, perfectly gated decision can still become unreconstructable once its surrounding context drifts. Auditability, properly treated, needs Contribution 2's own dedicated development (an entire new Part), not one chapter inside Part One.

**Chapter 12, "Future of Auditable AI — Standards, regulation, and industry direction,"** is the right *location* for understanding-layer material but the wrong *framing* — as originally scoped (regulatory/standards-focused) it does not capture Contribution 3's epistemic depth (capability vs. understanding, the historical software-engineering pattern). It needs substantial rework, not merely narrowing.

### 8. What new chapters become necessary?

A new Part Two, built from Contribution 2's eventual research (not yet done — see `research-roadmap.md`, Steps 2–5), covering: the state-is-not-knowledge diagnosis (replacing and substantially expanding the original Chapter 5); decision provenance and evidence continuity as an architectural pattern; and, if the empirical programme in `empirical-program.md` is carried out, a chapter reporting the reconstruction-experiment findings honestly (including if they do not fully support the diagnosis — a live possibility per that document's falsification conditions). A new Part Three, built from Contribution 3's eventual research (Step 6 in `research-roadmap.md`), substantially reworking the original Chapter 12 into: the historical software-engineering pattern (version control, transaction logs, tracing), argued properly rather than asserted; the capability-vs-understanding critique of AI measurement culture; and the Understanding Layer itself, framed honestly as an open architectural problem rather than a specified design (per C9b's novelty-risk rating in `claim-graph.md`).

### 9. What is the new possible book-level argument arc?

A three-part structure:

- **Part I — Decisions.** Control, present-tense. Ready now; corresponds to `oreilly-submission-disruptive.md` and the surviving/merged Chapters 1–4, 6–9.
- **Part II — Provenance.** Preservation, retrospective. Needs new research (Contribution 2); would substantially expand and replace the original Chapter 5.
- **Part III — Understanding.** Synthesis, terminal. Needs new research (Contribution 3); would substantially rework the original Chapter 12 and supply the book's actual title-level thesis.

This is a genuine upgrade in ambition: the original single-theory "Evidence-Gated AI" book becomes the first movement of a more ambitious three-movement book whose overall thesis moves closer to Source A's "capability vs. understanding" framing than to Source B's original "auditability via enforcement" framing — achieved by treating Source B's original proposal as Part I of a larger, now better-justified book, rather than as the whole book. No rewriting of the proposal is done here; this is the diagnosis the next human decision would need before commissioning that rewrite.
