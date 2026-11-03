---
id: topic-bostrom-world-models-wm-phase11-closure
title: "Phase 11 closure and verification report"
topic: bostrom-world-models
type: note
status: closed
created: 2026-11-05
tags: [closure, bounds]
---

# Phase 11 closure
**Scope.** The interrupted Phase 11 left `src/eid/hmm_small.py` and `src/eid/hmm_bounds.py` (commit `0df5186`) without tests. This note records what was implemented, verifies the claims, and closes the line. Phase 11 is **not** the central direction of the programme.

## What was implemented
- `hmm_small.py`: single-trajectory controlled HMM utilities (forward log-likelihood, exact rational likelihood, sampling incl. adaptive policies, Baum–Welch for one trajectory).
- `hmm_bounds.py`: (C) **type-class relaxation** for any S, O, A: latent paths are grouped by complete-data statistics c = (s₀, transition counts N, emission counts M); p_θ(D) = Σ_c W(c) f_c(θ) with f_c ≥ 0; U_C = Σ_c W(c) sup_θ f_c(θ) (closed-form complete-data MLE per class). (A/B) **interval branch-and-bound** for S = 2, O = 2, any A: monotone interval forward recursion over parameter boxes, level-synchronous splitting, EM warm start, floating-point inflation `1 + 16(n+2)u`, deflated lower bounds. (D) confidence-set-restricted variant (boxes discarded when the certified training upper bound is below the confidence level) — **not tested in this phase** and therefore unverified.
- Heuristic components: only the EM warm start (it supplies a *deflated* lower bound; it cannot invalidate an upper bound).

## Claims and verdicts
| Claim | Verdict | Evidence |
|---|---|---|
| p_θ(D) = Σ_c W(c) f_c(θ) exactly | **Proved and verified** | identity checked against the forward algorithm at 20 random θ and a boundary θ (deterministic transitions/emissions, point-mass b₀, many zeros); DP class dictionary equals brute-force enumeration over all S^{n+1} latent paths for four (S, O, A, n) settings; Σ W = S^{n+1} |
| L\* ≤ U_C | **Proved** (sup of a sum of nonnegative terms ≤ sum of sups); verified against random θ and exact rational likelihoods | `test_exact_rational_bound…` |
| U_C ≤ K·L\*, K = number of classes with W > 0 | **True for the unconstrained closed family** (b₀ may be a vertex; all rows free). Proof: L\* ≥ p_{θ_c}(D) ≥ W(c) f_c(θ_c) for every class c, hence U_C ≤ K·max_c W(c) f_c(θ_c) ≤ K·L\*. Verified with the forward algorithm at all class maximisers θ_c. **False for constrained families**: with emission P(o = 0 | s) ≤ 0.6 in every state and all-zero data, L\* ≤ 0.6ⁿ while U_C ≈ 1, so U_C/L\* ≥ e^{0.51 n} exceeds any fixed K (n = 24 > K). | `test_K_ratio_claim_fails_for_a_constrained_family_counterexample` |
| Zero probabilities / boundaries | handled: 0⁰ = 1 convention, rows with zero total use arbitrary θ_c rows, impossible-data cases give forward likelihood 0 | tests |
| Controlled HMMs, adaptive actions | **valid**: the likelihood is conditional on the realised actions; policy factors cancel | `test_adaptive_actions…` |
| Interval upper bound dominates every θ in the box | **Proved** (nonnegative entries, monotone product-sum); verified against exact Fraction likelihoods at 300 random in-box points | tests |
| Floating-point preservation | **Argued, not machine-checked:** relative error ≤ (1+u)^{16(n+2)} for IEEE-754 double without under/overflow; the float U_C is validated against exact rational arithmetic for n ≤ 8 (agreement 10⁻¹²) but carries no explicit inflation; for n ≥ 9 it is a high-confidence numerical value, not a certified one | stated limitation |
| Dense grid never exceeds the bounds | verified (9⁵ grid) | test |
| Determinism | verified | test |
**Measured (one random 2-state, 2-symbol model, A = 1, n = 4…20):** K = 22, 64, 116, 312, 450, 1148, 1674; the type-class bound lay 1.9–2.4 nats above the branch-and-bound certified upper bound (a-priori ceiling ln K = 3.1–7.4). Branch-and-bound reached a 0.1-nat gap at n = 4, 8, 12 and exhausted a 3–4.7 M box budget at n = 6, 10, 16, 20 (gaps 0.4–1.4 nats). One model, not a study.

## Literature verdict (access levels)
- **Interval branch-and-bound for certified global HMM maximum likelihood already exists:** Montanher, "Global estimation of Hidden Markov models using interval arithmetic" (2-page abstract, read in full: interval Newton, symmetry breaking, KKT box elimination, ε-global maximum). Gormley & Eisner, "Nonconvex Global Optimization for Latent-Variable Models" (ACL 2013; abstract/introduction read: branch-and-bound with RLT convex relaxations, upper bound on the global maximum, NP-hardness of the problem stated). **Algorithmic novelty of (B) is not claimable.**
- **Possible competing universal certificate:** Ziv's inequality (IEEE Trans. IT 1992; search description only) bounds the likelihood of finite-state sources through the Lempel–Ziv phrase count; its exact applicability to HMMs and its tightness were **not verified**. The Ephraim–Merhav survey page returned 404; Ziv's paper is not accessible.
- **Type-class relaxation:** no source found; it is an *elementary* consequence of "sup of a sum ≤ sum of sups" and exact grouping of terms. A survey statement that the method of types "applies to HMPs only if unifilar" (search description; not read) concerns type classes of *observation* sequences, not latent paths. Novelty is **not established** and the result is classified as elementary.

## Classification
| Item | Class |
|---|---|
| interval branch-and-bound | established method (restricted implementation, S = 2) |
| type-class bound, L\* ≤ U_C ≤ K L\* (unconstrained family) | valid restricted implementation; elementary result; novelty unverified |
| the K-ratio claim for constrained families | **invalid** (counterexample) |
| confidence-set-restricted variant | unresolved (untested) |
| universal bounds à la Ziv | unresolved (unread) |
| "price of certification" for sequential inference | unresolved: the additive gap ≤ ln K ≈ O(dim · ln n) would cost only O(ln n) nats, but computing U_C takes time polynomial in n of degree ≈ dimension of the count space (K = 1674 at n = 20 for S = 2, A = 1) |
**Decision: close Phase 11.** The prototype stays as supporting infrastructure (tests in `tests/test_hmm_bounds.py`). No further optimisation work.
