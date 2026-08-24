---
id: note-contribution-03-residual-gap-analysis
title: "Contribution 3 — Residual Gap Analysis"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, residual-gap]
refs: [prior-art-collision-matrix.md, earned-premises.md]
---

## Levels of analysis (Section 20)

Used throughout this review; existing fields located precisely, per the
matrix in `prior-art-collision-matrix.md`.

| Level | Question | Fields operating here |
|---|---|---|
| 1. Model | What happens inside a learned model? | Mechanistic interpretability, XAI (attribution) |
| 2. Inference/decision | What inputs/evidence/policy produced a specific output? | XAI (per-output), agent/LLM observability |
| 3. Pipeline/system | How did components interact? | Tracing, replay, program comprehension, architecture recovery, runtime verification |
| 4. Historical system | What did the system know/use at a past point? | Provenance, bitemporal databases, Contribution 2's own object |
| 5. Behavioral envelope | What can the system do across possible conditions? | Formal verification (partially), evaluation/testing (out of scope here) |
| 6. Human/system knowledge | What do operators/designers actually know about the system? | Architectural knowledge management, assurance cases |

**No field reviewed operates natively across all six levels.** The
closest attempt at cross-level coordination is assurance cases (Level
5–6, consuming evidence from Levels 1–4), and even that is a structuring
methodology, not a source of Level 1–4 content (`ai-systems-review.md`).

## Testing each candidate outcome (Section 23)

**A — Nothing; existing disciplines already cover it.** **Not
supported.** Every field reviewed is real and often deep at its own
level, but none spans Levels 5–6 while also supplying Levels 1–4's
content natively. Rejected as the residual-gap verdict — there is a real
seam, even if it is smaller than Source A claims.

**B — Integration gap: mechanisms exist but no unified system property
connects them.** **Strongly supported**, and the strongest-evidenced
option in this review. Direct, current (2026), technical confirmation:
"the AI observability landscape... is characterized by impressive depth
at individual layers but limited integration across them" [S13] —
exactly this claim, stated by current practitioner/research literature,
not asserted by this programme. The collision matrix's own structure
(no row spans more than 2–3 levels) is independent, structural
confirmation of the same finding.

**C — AI-specific composition gap: mechanisms exist individually but
learned/agentic systems combine failure modes in a new way.**
**Partially supported, narrowly.** Sculley et al.'s entanglement/hidden-
feedback-loop findings [S21] are genuine, literature-supported,
AI/ML-specific complications. Contribution 2's own earned finding (a
single decision routinely depends on model + policy + evidence +
authority + configuration simultaneously) is a real, narrow instance of
compositional complexity — but it is *decision-specific*, not yet shown
to generalize to system-wide behavior (`earned-premises.md`'s explicit
scope limit).

**D — Measurement gap: "understanding" is discussed but not measured at
system level.** **Strongly supported**, second-strongest option. Program
comprehension measures comprehension *of source code* [S6][S7].
Mechanistic interpretability's own leading researchers report many
queries *intractable* at the *model* level [S22]. No source found in
this entire review measures "understanding" as a property of a
multi-component AI decision *system*, across Levels 1–4 jointly. This is
a genuine, well-evidenced absence — not proof nothing could measure it,
but confirmation nothing found here does yet.

**E — Architectural gap: genuinely missing runtime/system abstraction.**
**Not supported as stated.** Applying Section 16's test directly: no
source reviewed, and no argument constructed in this review, can specify
a precise invariant, input/output contract, system boundary, or failure
condition for a new "Understanding Layer" that is not already
achievable by better discipline (capturing identifiers not values,
integrating existing layered observability, adopting assurance-case
coordination) within the fields already reviewed. See
`novelty-verdict.md`'s disposition of the term.

**F — Temporal gap: existing approaches poorly preserve evolving
AI-system knowledge.** **Partially supported, at Contribution 2's own
scope only.** The bitemporal/transaction-time gap Contribution 2
demonstrated for a single decision is real and earned
(`earned-premises.md`). Whether it generalizes to *system-wide* evolving
knowledge (Level 5–6) is untested by any material in this programme or
found in this review.

**G — Other: a taxonomy gap.** `provenance-review.md`'s finding that
reconstruction, interpretation, explanation, prediction, and control are
related but not unified by any single framework found in this review is
real but minor — a conceptual clarification opportunity, not a missing
mechanism or architecture.

## Ranked residual gap

1. **B — Integration/coordination gap** (strongest evidence, current and
   direct).
2. **D — Measurement gap** (strong, well-evidenced absence).
3. **C — AI-specific composition gap** (real but narrow, inherited
   mostly from Contribution 2's own earned scope plus Sculley et al.).
4. **F — Temporal gap** (real at decision-scope, untested at
   system-scope).
5. **G — Taxonomy gap** (minor, clarificatory).
6. **E — Architectural gap** (not supported; see `novelty-verdict.md`).
7. **A — Nothing missing** (rejected).

**The residual gap, stated in one paragraph:** existing disciplines
(program comprehension, observability, provenance, replay, XAI, formal
verification, assurance cases) each competently cover their own level
and their own object of study, and — per current 2026 industry/research
sources, not this programme's own assertion — are demonstrably *not
integrated* with each other, especially for AI-agent systems
specifically. Nobody found in this review has *measured* system-level
understanding across a multi-component AI decision pipeline, even though
the pieces needed to attempt such a measurement (Contribution 2's own
consumption-relation property, layered agent observability, assurance-
case structuring) already exist separately. The gap is real, is smaller
and more specific than Source A's framing, and is best characterized as
**integration and measurement**, not as a missing mechanism or a
missing architecture.
