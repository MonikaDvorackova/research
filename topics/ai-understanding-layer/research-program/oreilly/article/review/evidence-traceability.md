---
id: note-oreilly-article-evidence-traceability
title: "O'Reilly Article draft-v1 — Evidence Traceability"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, review, evidence]
refs: [../draft-v1.md, ../../../contribution-02/article/FINAL-ACCEPTANCE.md, ../../../contribution-03/FINAL-EDITORIAL-DISPOSITION.md]
---

Every claim in draft-v1 traced to its originating contribution and
checked against whether the O'Reilly sentence exceeds the frozen
research result.

| Article sentence (paraphrased) | Contribution | Source file | Experiment (if any) | Evidence type | Safe / Unsafe |
|---|---|---|---|---|---|
| A model output is not a decision; a single model participates in many differently-requirement'd decisions | C1 | `article-01-decision-level-control/novelty-audit.md` | None (architecture argument) | ARCHITECTURE ARGUMENT | **Safe** |
| Evidence/requirements/authority/gate closes the authorization gap; ALLOW/BLOCK/ESCALATE | C1 | `article-01-decision-level-control/draft-v2.md` | None | ARCHITECTURE ARGUMENT | **Safe** |
| "Exactly three possible outcomes" | C1 | Same | None | ARCHITECTURE ARGUMENT | **Unsafe as worded** — the underlying pattern is safely sourced, but "exactly" claims a generality (all authorization systems have exactly three outcomes) the architecture argument never asserted. See `claim-review.md`. |
| "A boundary most ML pipelines don't yet treat... at all" | C1 (implied) | None | None | **No source** | **Unsafe** — no contribution in this programme measured pipeline prevalence; this is not traceable to any frozen result. |
| Retained ≠ consumed | C2 | `contribution-02/article/draft-v2.md`; `FINAL-ACCEPTANCE.md` | Primary Regime A/B/C experiment | EMPIRICAL, frozen, ACCEPTED | **Safe** |
| Consumption relation "made at decision time... not assembled after the fact" | C2 | `contribution-02/article/draft-v2.md` line 43 | Primary experiment, Cases 3/9 vs. Case 8 | EMPIRICAL | **Unsafe — exceeds the frozen result.** Article 2's frozen text explicitly states the opposite of what draft-v1 claims: "does not survive this case... not the only way." This is the review's central P0 finding — see `reviewer-report.md` §6. |
| Retroactive-correction example (policy updated in place, narrowed to 2–3 candidates) | C2 | `contribution-02/article/draft-v2.md` | Primary experiment, Case 8 | EMPIRICAL | **Safe** — faithful to Case 8's accepted, clean information-gap finding. |
| Bitemporal databases can solve reconstruction if instrumented | C2 | `FINAL-ACCEPTANCE.md`, "Explicit non-claim" | N/A | Frozen non-claim, correctly honored | **Safe** |
| Honest ambiguity ≠ false confidence | C2 + research note | `contribution-02/experiment/followup-case10/`; `contribution-03/experiment/RESULT.md` | Follow-up (F10 cases) + trajectory experiment | EMPIRICAL, both frozen | **Safe** |
| A system without an AMBIGUOUS outcome "will, sooner or later" produce false confidence | C2 + research note (extrapolated) | Same as above | Same | **Extrapolation beyond the tested cases** | **Unsafe as worded** — the experiments show this *can* happen and *was avoided* by deliberate design; they do not show it *will* happen in unspecified future systems. See `reviewer-report.md` §8. |
| Trajectory-level relation closes the gap; same mechanisms as single-decision case | Research note | `contribution-03/experiment/RESULT.md`; `FINAL-EDITORIAL-DISPOSITION.md` Findings B/C | Trajectory-composition experiment | EMPIRICAL, frozen, correctly bounded | **Safe** — matches the "supporting research note" disposition exactly, no case-level detail exceeded |
| Cross-decision dependency link via tracing/provenance, "nothing new required architecturally" | Research note | `FINAL-EDITORIAL-DISPOSITION.md` Finding B | Same | EMPIRICAL | **Safe** |
| Seven-field decision-record checklist | Synthesis (not directly from any one experiment) | `OREILLY-FINAL-BRIEF.md` §"Article spine" | None | SYNTHESIS, correctly framed as a design pattern | **Safe**, subject to the structural fix in `reviewer-report.md` §12 (a presentation issue, not an evidentiary overreach) |
| Dynamic/continuous assurance cases as the strongest prior-art collision | Cross-cutting | `contribution-03/assurance-integration-review.md`; `OREILLY-FINAL-BRIEF.md` | None (literature) | PRIOR-ART SUPPORTED | **Safe** |
| "None of this is unique to AI" | Cross-cutting | `OREILLY-FINAL-BRIEF.md` §"AI-specificity" | None | SYNTHESIS, correctly hedged | **Safe** |

## Summary

**Two unsafe evidentiary claims found, both already identified in
`reviewer-report.md`:** the P0 consumption-relation-at-decision-time
claim (exceeds Article 2's frozen, accepted position — the most serious
finding in this entire review) and the P1 "will, sooner or later"
deterministic-causation claim (extrapolates beyond what six to twelve
controlled cases can support). One additional unsourced prevalence claim
("most ML pipelines") has no traceable origin in any contribution at
all — not a misrepresentation of a frozen result, but a claim with no
evidentiary basis whatsoever. All three require correction before
publication; none require new research to fix, since the correct,
narrower claims are already sitting in the frozen record this article
should have quoted instead.
