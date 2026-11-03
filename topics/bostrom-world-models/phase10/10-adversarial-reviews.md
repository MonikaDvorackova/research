---
id: topic-bostrom-world-models-phase10-reviews
title: "Phase 10 adversarial reviews (internal, same agent; not external peer review)"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-04
tags: [review, adversarial]
---

# Three internal reviews
Each lists: strongest objection; evidence supporting it; what would resolve it; whether it blocks the next phase.

## Mathematical statistics reviewer
**Strongest objection.** "Every guarantee is Ville plus a known supermartingale (Emmenegger et al. Thm 1; Wasserman et al.). Your 'price' is the Stein/Chernoff exponent of a composite null; your 'regret' is KT redundancy. Your certified test rejected nothing in 7200 null runs, so the calibration experiments cannot separate validity from conservatism; the exact enumeration crossing probabilities were 0.0000 (you said so)."
**Evidence.** `04-…` §3: exact crossing 0.0000; expected e-value ≤ 0.23; 0/7200; the adaptive-range boundary is a derivation not found in the text read.
**What resolves it.** (i) A less conservative certified test whose empirical type-I is close to α (so that calibration is informative); (ii) exact DP with a fast solver at a horizon where crossings occur; (iii) an external read of the proofs (Prop D′, certified theorem); (iv) reading Chernoff, Safe Testing, Podkopaev–Ramdas in full.
**Blocks?** Blocks any claim that validity was *demonstrated empirically*; does not block further theory. **Secondary objections:** 120 EM runs with 0 events (UB 0.025) do not certify symmetric optimisers; type-I ICC is undefined, so dependence for type-I claims is unmeasured; interval methods undercover near the boundary (0.84–0.97).
## Machine-learning reviewer
**Strongest objection.** "The only certified procedure lives in the class where certification is trivial (fully observed categorical Markov kernels, closed-form MLE). The learned *world models* that motivated the project (latent, recurrent) are exactly where there is no certified supremum, and the EM results show the uncertified route fails when the alternative is good. A confirmatory E6′ on count tables with A = O = 3, T = 4 would not speak to neural world models."
**Evidence.** `05-…`, `06-…` (interface limits); no neural or ensemble experiment; generator diversity is structural (random tensors), not architectural; certified test has no latent-state version.
**What resolves it.** A certified or at least conservatively bounded denominator for a latent null (PO-13), or an explicit neural-null experiment with a stated, tested safeguard; ensembles only if disagreement is calibrated against the exact epistemic gap on the Markov family.
**Blocks?** **Blocks confirmatory E6′** (G7): the result would be about count learners. Does not block the theory/dev work on PO-13.
## Philosophy-of-science reviewer
**Strongest objection.** "'Price of validity' is an engineering quantity about the power of calibrated tests of a restricted class. Moving from it to claims about what an embedded *observer can know about its environment's generative nature* needs premises you have not defended: that a stationarity-in-a-class null is the relevant null, that resets reset the regime, that a comparator is declared before data. These are theory-laden choices (Duhem–Quine; Laudan–Leplin), and the results are about what tests can *license*, not about knowledge."
**Evidence.** Phase 9 `02-…`: rejection licenses only "class inadequate relative to a comparator"; reset semantics R5 (interface assumptions); Prop F (equivalence); no result bears on simulation.
**What resolves it.** A premise-by-premise account linking each procedure's formal null to a claim (done at the level of the ladder in Phase 9, not extended); or dropping the epistemological headline in favour of a methodological one.
**Blocks?** Does not block theory; **blocks any manuscript framing** that presents the price as an epistemic limit of embedded intelligence.
## Disagreements retained
The statistician would prioritise a tighter/less conservative construction and external proof checking; the ML reviewer would prioritise latent/neural nulls; the philosopher would prioritise the premises (and doubts the project's epistemological payoff). They do not agree on what a "meaningful result" would be.
