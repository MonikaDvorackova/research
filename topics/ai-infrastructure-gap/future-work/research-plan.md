---
id: future-ai-infrastructure-gap-research-plan
title: "Research plan: minimum path to articles A and B"
topic: ai-infrastructure-gap
type: note
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [future-work, research-plan]
---

# Research plan

Minimum work required to earn two publications—**without** drafting them yet.

| ID | Publication | Goal |
|---|---|---|
| **A** | Standalone architectural article | Describe the problem, vocabulary, kill-list evaluation, and falsification stance |
| **B** | O’Reilly Radar follow-up | Propose and demonstrate a technical solution—only after A’s problem claim is earned |

**Rule:** Do not start B’s solution narrative until A has a defendable gap-or-composition conclusion.

---

## Phase 0 — Stabilize the question (prerequisite for A)

1. Freeze working definitions for *decision*, *justification*, *authorization*, *validity*, and *reconstruction* sufficiently for evaluation (document remaining disputes in the charter’s terminology table).
2. Select **3–5 decision scenarios** (AI-mediated) that make reconstruction demands concrete.
3. Derive a **minimum reconstruction checklist** (fields + bindings) from those scenarios—not from a preferred layer name.

**Exit:** Checklist exists; scenarios written under `notes/`.

---

## Phase 1 — Kill-list evaluation (core of A)

4. For each kill-list abstraction in the charter, score against the checklist: *covers / partial / absent*, with notes on what “already solves it” would require.
5. Attempt a **best-faith composition** (e.g., policy decision log + provenance + temporal versions + trace correlation). Record whether the checklist is met.
6. Update `architecture/claim-inventory.md` statuses (support, weaken, reject, reframe)—never leave A dependent on untouched hypotheses presented as facts.

**Exit:** Written evaluation table; explicit stance among competing explanations E1–E5.

---

## Phase 2 — Article A only

7. Draft publication **spine** (later, under `publications/articles/`) from: problem statement, scenarios, checklist, kill list, falsification, negative-or-positive conclusion.
8. Keep solution proposals out of A except as *open options* (composition profile vs. candidate formulations).

**Exit:** A ready for internal review; catalog publication entry when drafting begins.

---

## Phase 3 — Minimum path to B (only if warranted)

9. If E1 or successful composition: B becomes a Radar piece on **composition patterns**, not a new layer.
10. If residual gap remains: choose the **smallest** intervention (schema/profile vs. candidate layer formulation) that closes the checklist on one reference scenario.
11. Demonstrate on a **minimal** example (description or thin prototype later—not in topic init). Measure against the same checklist used in A.

**Exit:** B has a demo-backed claim continuous with A’s evaluation—not a rebrand of provenance or policy logging.

---

## Priority order (first work)

| Priority | Task | Supports |
|---|---|---|
| 1 | Write scenario set + reconstruction checklist | A |
| 2 | Kill-list evaluation pass (all charter rows) | A |
| 3 | Best-faith composition attempt + claim inventory update | A |
| 4 | Decide E1–E5 stance; outline article A spine | A |
| 5 | Only then: solution selection + demo plan for Radar | B |

## Explicitly deferred

- Literature notes with real sources (add when reading begins; no artificial refs).
- Specifications and implementations.
- Publication Markdown drafts.
- Astro, CI, and product alignment work beyond notes on AIGov Core boundaries.
