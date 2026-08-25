---
id: note-contribution-03-article-revision-plan-v2
title: "Contribution 3 Article — Revision Plan for draft-v2"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, revision-plan]
refs: [VERDICT.md, reviewer-report.md, section-review.md, title-review.md]
---

Per `VERDICT.md`: Independent Article 3 = **BORDERLINE**, required
revision = **MAJOR**, ready for v2 = **YES, conditional on
reconceptualization, not line-editing.** This is a real v2 plan, not a
merge plan — but §6 below specifies the merge-into-Article-2 fallback
explicitly, per this task's instruction, in case v2 does not achieve
sufficient independent weight after the changes below.

No implementation performed here. `draft-v1.md` remains unmodified.

## P0 — must fix before any v2 is publishable

1. **Disclose Objection 6 explicitly.** Add a paragraph (recommended
   location: "The Experiment" or "What the Experiment Does Not Show")
   conceding that `DecisionRecordT1`'s schema structurally has no field
   capable of encoding a cross-decision relation, so the *direction* of
   the T1/T2 gap is guaranteed by construction — a manipulation check,
   not a discovery. Relocate the article's actual empirical claim to
   where the evidence supports it: P5 (honest ambiguity vs. false
   confidence), which the schema does not force.
2. **Rebalance toward P5.** Currently "Perfect Local Records, Ambiguous
   Global History" (the guaranteed-by-construction result) is the
   headline and "Ambiguous Is Better Than Wrong" (the genuinely open
   result) is the follow-up. Invert the emphasis: state the T1/T2 gap
   briefly as expected/designed, then spend the article's persuasive
   weight on the honest-vs-false-confident distinction.
3. **Fix the title.** Replace "When Reconstructable Decisions Produce an
   Unreconstructable System" with "When Reconstructable Decisions
   Produce an Ambiguous Trajectory" (primary) or "Local Reconstruction
   Is Not Trajectory Reconstruction" (runner-up, especially if word
   count compresses toward the research-note range) — see
   `title-review.md`.
4. **Add the missing citation.** Buneman, Khanna, Tan, "Why and Where: A
   Characterization of Data Provenance," ICDT 2001 — cite alongside [1]
   in "This Is Not a New Provenance System," since this programme's own
   `provenance-review.md` already identifies it as the sharper, older
   formalization of exactly the claim being made there.
5. **Cut or relabel the formalization.** ∀i identifiable(C(di)) ⇏
   identifiable(E) either removed entirely, or kept with an explicit
   sentence stating it restates the schema design rather than proving a
   result — per `reviewer-report.md` §17.

## P1 — should fix, materially strengthens the piece

6. **Name and answer Objection 1 directly** ("isn't this just basic
   compositional-systems theory?") using the same direct-address format
   already used for the provenance objection — the article's own best
   rhetorical device, currently applied to only one of the two hardest
   objections.
7. **Disclose the construct-validity gap**: Trajectory Identifiability
   and Dependency Edge Accuracy only score decisions with a true
   predecessor; root decisions are never tested for false-edge
   invention. One sentence in "What the Experiment Does Not Show"
   suffices.
8. **Add the three-way honest-ambiguity taxonomy** from
   `reviewer-report.md` §6 (ambiguous record vs. weak algorithm vs.
   false confident answer) explicitly in "Ambiguous Is Better Than
   Wrong" — this is the article's strongest conceptual material and
   currently under-articulated relative to its own importance.
9. **Add the AI-specificity grounding** from `ai-systems-review.md`
   (S13/S23, "depth without integration" in 2026 AI/agent observability
   tooling) as one sentence in "What to Preserve Across Decisions" or
   the closing section — legitimate, current, citable AI-relevance that
   strengthens the piece without overclaiming AI uniqueness.
10. **Merge the two definitional sections** ("Local Reconstruction Is
    Not Trajectory Reconstruction" + "What Has to Compose") into one,
    removing the redundant restatement — see `section-review.md`.

## P2 — optional, polish-level

11. Add Sigelman et al., Dapper (2010) as an academic companion to the
    OpenTelemetry citation [2], strengthening the tracing concession
    with a primary academic source alongside the practitioner docs.
12. Note the diagnosability-of-histories connection explicitly (per
    `prior-art-review.md`'s diagnosability section) rather than leaving
    "trajectory reconstructability" implicitly freestanding vocabulary.
13. Remove the redundant restatement between "Perfect Local Records,
    Ambiguous Global History" and "The Composition Question" (closing) —
    the two currently make substantially the same claim twice.

## Target shape for v2

- **Word count target: 1,800–2,400** (down from 3,257), driven by the
  P1.10/P2.13 merges and by the general compression a structurally
  simple central mechanism warrants (`section-review.md`'s net
  assessment).
- **Structure** (revised from draft-v1's ten sections):
  1. Opening paradox (keep, tightened)
  2. Local vs. trajectory reconstruction, + composition question
     (merged from two sections)
  3. The experiment (T1/T2, six cases) — with the Objection 6 disclosure
     folded in here, not left implicit
  4. The honest-ambiguity result (promoted to the article's centerpiece)
  5. The negative control
  6. Prior art: "this is not a new provenance system" (+ Buneman
     citation, + named answer to Objection 1)
  7. What to preserve (engineering takeaway, + AI-specificity sentence)
  8. Limitations (+ construct-validity disclosure)
  9. Closing (shortened, no restatement of §3's headline)

## §6 — Merge-into-Article-2 fallback (specified, not performed)

If v2, after the above changes, still does not clear an independent bar
(i.e., if the compressed, reconceptualized version still reads as an
extension rather than a standalone contribution), the defensible
fallback is **not** publishing Article 3 as a separate piece, but adding
a new closing subsection to Article 2's own "The Question to Ask"
material. Specified here for planning purposes only — **not performed in
this pass**, and Contribution 2's frozen `draft-v2.md` remains untouched
regardless of what this review recommends:

- **What would merge:** the trajectory-vs-decision distinction (P2), the
  T1/T2 experiment's headline numbers, the honest-ambiguity finding
  (P5), and the negative-control result — condensed to roughly
  400–600 words as a new subsection, e.g., "Does This Compose Across a
  Trajectory?", positioned after Article 2's existing "Limitations"
  section and before "The Question to Ask."
- **What would be discarded:** the standalone title and dek, the
  four-decision opening-paradox walkthrough (Article 2 already has its
  own opening device), the full six-case narration, the formalization,
  and the separate References list (the two new citations — [4]
  Sampath et al., [5] Bakirtzis & Topcu — would be appended to Article
  2's existing five-item list instead of maintaining a second list).
- **What would need separate authorization regardless:** any edit to
  Contribution 2's frozen `draft-v2.md` or `FINAL-ACCEPTANCE.md` — both
  remain untouched by this review and by this hypothetical merge
  specification.
