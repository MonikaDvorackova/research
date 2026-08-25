---
id: note-oreilly-article-revision-plan-v2
title: "O'Reilly Article — Revision Plan for draft-v2"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, review, revision-plan]
refs: [VERDICT.md, reviewer-report.md, section-review.md, claim-review.md, citation-review.md, title-review.md]
---

Identification only. No replacement sections written here, per this
review's scope. `draft-v1.md` is not modified.

## P0 — technical/evidence correctness (mandatory before publication)

1. **Location:** Section 4, lines 61 and 63.
   **Issue:** claims a consumption relation must be "made at decision
   time... not... assembled after the fact," directly contradicting
   Article 2's own frozen, accepted position.
   **Required change:** rewrite to state the property as a preserved
   consumption relation "however that relation ends up being captured:
   authored explicitly when the decision is made, or reliably derivable
   afterward from other retained event or provenance data, as long as
   it identifies the version used rather than merely narrowing the
   candidates."
   **Reason/source:** `contribution-02/article/draft-v2.md` line 43
   ("does not survive this case... not the only way") and line 53 (the
   Cases 3/9 rescue via value cross-referencing).
   **Expected effect:** restores Article 2's actual accepted claim;
   removes the single most serious factual risk in the article.

## P1 — thesis/synthesis/prior-art

2. **Location:** Section 3, line 47.
   **Issue:** "a boundary most ML pipelines don't yet treat as a
   distinct, enforced checkpoint at all" — unsupported prevalence claim.
   **Required change:** remove the quantifier; replace with a structural
   (non-frequency) framing, e.g. "a boundary that doesn't map cleanly
   onto model registries, model cards, or evaluation reports."
   **Reason/source:** no contribution in this programme measured
   pipeline prevalence (`claim-review.md`).
   **Expected effect:** removes an unsupported empirical claim without
   weakening the underlying point.
3. **Location:** Section 2, line 17; Section 6, line 81.
   **Issue:** two more instances of the same unsupported-prevalence
   pattern ("most systems," "in most production AI systems today").
   **Required change:** same treatment as item 2 — remove or convert to
   structural claims.
   **Reason/source:** same as item 2.
   **Expected effect:** consistent evidence discipline across the whole
   article, not just the one instance most likely to be caught.
4. **Location:** Section 7, lines 114 and 116.
   **Issue:** "will, sooner or later" / "will eventually" — deterministic
   causal claim the controlled experiments don't support.
   **Required change:** reframe as a design-necessity argument: "a
   system with only two possible outputs — a specific answer, or an
   error — has no way to represent this situation honestly: when the
   record genuinely can't determine a unique answer, that design forces
   a choice between reporting one candidate as fact or failing outright,
   and neither is honest."
   **Reason/source:** the research demonstrated this outcome *can* occur
   and *can* be avoided by design; it did not demonstrate inevitability
   in unspecified future systems (`reviewer-report.md` §8).
   **Expected effect:** preserves the point's force while matching the
   evidence discipline the rest of the article otherwise maintains.
5. **Location:** Section 3, line 45.
   **Issue:** "exactly three possible outcomes" overstates generality.
   **Required change:** "these four together give the gate three
   outcomes" (drop "exactly").
   **Reason/source:** `reviewer-report.md` §5; real systems sometimes
   have finer-grained outcomes than allow/block/escalate.
   **Expected effect:** minor, low-risk precision fix.
6. **Location:** Title and dek.
   **Issue:** "The Relations, Not the Records" is a false dichotomy — a
   consumption relation is itself a record; the title also covers only
   the reconstruction half of a two-part article.
   **Required change:** retitle to **"Authorized Now, Reconstructable
   Later"** (primary recommendation) or **"The Record That Authorized It
   May Not Reconstruct It"** (runner-up); replace the dek with a
   version free of unsupported prevalence language — see
   `title-review.md` for the exact recommended pairing.
   **Reason/source:** `title-review.md`, full attack and ranking.
   **Expected effect:** title accurately represents both halves of the
   article and removes a technical error from the article's most visible
   sentence.
7. **Location:** Throughout, especially the dek, Section 1's heading,
   and Section 4's opening question.
   **Issue:** "explainable"/"explain" is used as the primary operative
   term despite carrying XAI risk that the article's own disambiguation
   sentence has to fight against.
   **Required change:** switch the technical spine to
   "reconstructable"/"reconstruct" as the primary term from Section 1
   onward; allow "explain" to survive only in already-disambiguated,
   plain-English moments if desired.
   **Reason/source:** `reviewer-report.md` §4, flagged as this review's
   second-most-important finding after the P0 item.
   **Expected effect:** removes the need for readers to hold two
   meanings of "explain" simultaneously; strengthens title/dek options
   that already use "reconstructable" (see `title-review.md`).
8. **Location:** Section 6, citation base.
   **Issue:** four uncited factual prior-art claims (Kubernetes
   admission control, PDP/PEP, in-toto/SLSA, workflow provenance); the
   [4] citation's full author list unconfirmed.
   **Required change:** add the five citations specified in
   `citation-review.md`'s "Citation plan for v2," including the
   already-verified Buneman et al. why/where-provenance citation
   currently unused in this article despite being available elsewhere
   in the programme.
   **Reason/source:** `citation-review.md`.
   **Expected effect:** closes a real prior-art-fairness gap without
   requiring new research.

## P2 — structure/practitioner clarity

9. **Location:** Section 7's seven-item checklist.
   **Issue:** "Reconstruction outcome" is listed alongside decision-time
   facts, but it is the output of a later reconstruction process, not a
   fact available at decision time.
   **Required change:** split the list into two explicitly labeled
   groups — "what to persist at decision time" (six items) and "what a
   reconstruction process should be able to output later" (reconstruction
   outcome, alone).
   **Reason/source:** `reviewer-report.md` §12; a structural/conceptual
   issue, not a factual error.
   **Expected effect:** removes a real implementation confusion an
   engineer following the checklist literally could hit.
10. **Location:** Section 1, disambiguation sentence (line 15) relative
    to the section's opening punchline (line 13).
    **Issue:** the XAI disambiguation arrives one paragraph after
    "explainable" has already been used twice (line 13, section title).
    **Required change:** move the disambiguation earlier, or fold a
    compressed version into the section-1 heading/dek.
    **Reason/source:** `section-review.md`, Opening review.
    **Expected effect:** removes the brief window where a skimming
    reader could form the wrong (XAI) impression.
11. **Location:** Section 2, line 27 (fraud-scoring aside).
    **Issue:** minor example drift — a second scenario introduced for
    one sentence.
    **Required change:** optional — replace with a model-promotion-
    consistent illustration, or leave as-is (low priority).
    **Reason/source:** `reviewer-report.md` §11.
    **Expected effect:** marginal coherence improvement; not required.
12. **Location:** Section 8, paragraph order.
    **Issue:** disclaimers precede the payoff paragraph, costing
    momentum at the article's close.
    **Required change:** consider reordering so the affirmative
    synthesis paragraph leads and the boundary list follows as a
    shorter coda; no content change required.
    **Reason/source:** `section-review.md`, Ending review.
    **Expected effect:** stronger close without losing any required
    boundary claim.

## P3 — polish

13. **Location:** Section 4, line 63, "first-class fact."
    **Issue:** reads slightly proprietary/custom-terminology-flavored.
    **Required change:** soften alongside the P0 fix (item 1) — the
    rewrite already required there naturally removes this phrasing.
    **Reason/source:** `reviewer-report.md` §6.
    **Expected effect:** minor tone improvement, bundled with item 1.

## Net effect on length

None of the above are primarily length-driven. Per `section-review.md`'s
net assessment, a v2 built from this plan should land within
**3,700–3,950 words** — essentially flat relative to draft-v1's 3,882.
