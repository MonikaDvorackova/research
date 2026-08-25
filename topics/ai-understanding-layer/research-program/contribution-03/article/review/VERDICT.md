---
id: note-contribution-03-article-verdict
title: "Contribution 3 Article draft-v1 — Final Adversarial Verdict"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, verdict]
refs: [reviewer-report.md, section-review.md, claim-review.md, empirical-traceability.md, prior-art-review.md, title-review.md, revision-plan-v2.md]
---

Independent review, not a re-trust of `draft-v1-audit.md`. `draft-v1.md`
was not modified in producing this verdict.

## Does draft-v1 survive?

**YES WITH MAJOR REVISION.**

Every empirical claim is accurate and fully traceable
(`empirical-traceability.md`: zero discrepancies found). No claim is
factually unsupported (`claim-review.md`). The prior-art concessions are
honest and, apart from one missing citation, well-grounded
(`prior-art-review.md`). But the article does not disclose that its
headline result (the T1/T2 Trajectory Identifiability gap) is close to
guaranteed by how `DecisionRecordT1`'s schema was defined
(`reviewer-report.md` Objection 6) — an unaddressed objection serious
enough that, as currently framed, a technical reviewer would reasonably
read the piece as more novel than its mechanism supports.

## Independent Article 3?

**BORDERLINE.**

Tested against the five independence criteria: separate research
question (partial — a direct one-level-up extension of Contribution 2's
own question, not an orthogonal one); separate experiment (yes, distinct
code and design); separate prior-art field (no — substantially
overlapping with Article 2's own citations: [1]/[2]/[3] are reused
verbatim from `contribution-02/article/draft-v2.md`'s reference list);
independently falsifiable thesis (yes, technically); distinct
engineering consequence (weak — "preserve cross-decision relations, not
just per-decision context" reads as a natural one-paragraph extension of
Article 2's own "preserve the consumption relation" takeaway, not a
qualitatively different engineering practice). 2 of 5 clear, 1 partial,
2 weak/failing.

## Publication classification

**D — Research note / short paper.**

Not B (full technical practitioner article) at its current length and
framing: once AI framing, custom terminology, and implementation detail
are stripped away, the residual claim is research-note-scale (§ Section
21 below). Not F (unpublishable): the piece is honestly scoped, fully
traceable, and contains one genuinely non-obvious result (P5). Not E
outright (forced merge): the diagnosability/compositional-verification
framing and the dedicated negative-control experiment carry enough
independent conceptual content to stand as a short, tightly-scoped note
— see `revision-plan-v2.md` for both the v2 path and the merge fallback,
specified but not performed.

## Single strongest contribution

A controlled, quantified demonstration that an investigator confronted
with complete-but-relation-free local decision records fails **honestly**
(never with false confidence) rather than silently guessing — Dependency
Edge Accuracy = 1.00 and False Global Confidence = 0.00 across all
cases, a property of investigator design that the experiment's own
schema does not force and that a differently built, still-reasonable
investigator could have violated.

## Single strongest weakness

The article's headline framing ("Perfect Local Records, Ambiguous Global
History") presents as a discovery a result that is close to guaranteed
by construction — `DecisionRecordT1` structurally has no field capable
of encoding the cross-decision relation later declared missing — and
this fact is disclosed nowhere in the article (Objection 6,
`reviewer-report.md`).

## Does empirical evidence materially add value?

**PARTIALLY.**

The T1/T2 magnitude numbers (0.33 vs. 1.00) add confirmatory,
quantified precision to an outcome that was largely guaranteed by design
— real value, but modest. The DEA/FGC numbers (1.00/0.00) add genuine,
non-guaranteed empirical value — the article's strongest evidence, and
currently under-weighted relative to the guaranteed-by-construction
numbers.

## Does prior art destroy novelty?

**NARROWS.**

Workflow provenance, distributed tracing, event sourcing, and
compositional verification all already provide the underlying
mechanisms and the underlying general principle (`prior-art-review.md`).
This does not destroy the article's value — draft-v1 already concedes
all of it honestly — but it does confirm the correct publication
register is a modest, quantified reminder for a specific object class,
not a new-mechanism claim, which the current title and structure do not
yet fully reflect.

## Is the experiment too structurally obvious?

**PARTIALLY.**

The T1-fails-to-recover-E direction: yes, obvious/guaranteed by
construction (Objection 6). The honest-ambiguity-vs-false-confidence
result (P5): no, genuinely open and the article's real contribution.
`reviewer-report.md` §4 works through this distinction fully.

## Required revision

**MAJOR** (bordering on RECONCEPTUALIZE — see `revision-plan-v2.md`'s
P0 items: disclose Objection 6, rebalance toward P5, retitle, add the
Buneman citation, cut/relabel the formalization). Not MINOR or MODERATE
— these changes reposition the article's own claim about itself, not
just its prose.

## Ready for v2?

**YES**, conditional on treating this as a reconceptualization pass, not
a line edit — the full P0/P1/P2 plan and target structure are in
`revision-plan-v2.md`, including a specified (not performed)
merge-into-Article-2 fallback if the reconceptualized v2 still does not
clear an independent bar.

## Section 21 — completed statements

> After removing AI framing, custom terminology, and implementation
> details, the strongest contribution of Article 3 is: **a
> demonstration that "insufficient information to resolve a
> cross-decision dependency" and "a wrong answer stated as fact" are
> empirically separable failure modes for a reconstruction procedure,
> and that a carefully built one produces only the first.**

> The strongest evidence is: **the paired 1.00/0.00 result (Dependency
> Edge Accuracy / False Global Confidence) across all six cases under
> Regime T1 — a result the experimental schema does not guarantee and
> that a differently built investigator could have violated.**

> The strongest prior-art objection is: **that workflow provenance
> (via W3C PROV and, more precisely, the Buneman why/where-provenance
> formalism the article does not cite) already models exactly the
> dependency edge Regime T2 adds — meaning the T1→T2 gap this
> experiment reports is close to guaranteed by how Regime T1's record
> type was defined, not a discovered fact about the world.**

> Article 3 survives / fails as an independent article because: **it
> survives, but only marginally, and only after the P0 revisions in
> `revision-plan-v2.md` are made — the honest-ambiguity finding (P5) is
> real and worth publishing, but it is currently subordinated to a
> headline claim (the T1/T2 gap itself) that overclaims relative to how
> guaranteed that claim actually was by design.**

## Scores (1–5)

| Dimension | Score | Required change (if <4) |
|---|---|---|
| Technical correctness | 5 | — |
| Novelty honesty | 3 | Disclose Objection 6 explicitly (P0.1); the article is honest about not inventing a mechanism but not self-aware about how guaranteed its headline result was. |
| Empirical credibility | 4 | Disclose the construct-validity gap — root decisions never scored for false-edge invention (P1.7). |
| Prior-art fairness | 4 | Add the Buneman/why-provenance citation (P0.4). |
| Conceptual clarity | 4 | Add the three-way honest-ambiguity taxonomy (P1.8); merge the two definitional sections (P1.10). |
| Practitioner usefulness | 4 | — |
| AI-specific relevance | 3 | Add the "depth without integration" (S13/S23) grounding (P1.9); currently honest but underdeveloped. |
| Independence from Article 2 | 2 | Substantially differentiate or compress toward a research note (see BORDERLINE verdict above and `revision-plan-v2.md`'s merge fallback). |
| Title accuracy | 2 | Retitle — fix both the "system" scope overclaim and the "unreconstructable" severity overclaim (`title-review.md`). |
| Publishability | 3 | Execute the full P0 list in `revision-plan-v2.md` before any submission. |

## O'Reilly note (Section 24, recorded here only — no synthesis drafted)

- The decision-level → per-decision-reconstruction → trajectory-
  reconstruction three-step arc (Articles 1→2→3) remains a clean
  narrative device for a synthesis chapter, independent of this
  article's own publication fate.
- The honest-ambiguity-vs-false-confidence distinction, generalized one
  level up from Article 2, is the one piece of this material worth
  carrying into synthesis regardless of what happens to Article 3 as a
  standalone piece.
- The negative-control finding (ordinary relations already fix this) is
  a useful anti-hype anchor for any synthesis chapter tempted to propose
  new architecture.
- **Article 3's material, as currently scoped, is thin enough that a
  synthesis chapter should treat it as a paragraph-level extension of
  Article 2's thesis, not as a load-bearing third pillar with equal
  weight to Articles 1 and 2** — this possibility is real and should not
  be planned around prematurely.
