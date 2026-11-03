---
id: topic-bostrom-world-models-phase10-proofs
title: "Bounded theoretical investigation T1–T6: statements, proofs, failed attempts, counterexamples"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [theory, proofs, counterexamples]
---

# T1–T6
Verdict vocabulary: PROVED / DISPROVED / REDUCED TO KNOWN / OPEN WITH PRECISE OBSTACLE. **Nothing here is claimed as a new theorem.** Code: `src/eid/{certified_null,phase10_exact}.py`; tests `tests/test_certified_null.py`, `tests/test_phase9_audit.py`.

## T1 — Validity versus detection efficiency
**Prop T1 (lower bound; PROVED, elementary; known form).** Let 𝒩 be a set of laws, P an alternative, τ a stopping time with P(τ<∞)=1 and Q(τ<∞) ≤ α for every Q ∈ 𝒩. Then for every Q ∈ 𝒩: E_P[Σ_{t≤τ} δ_t^Q] ≥ ln(1/α), δ_t^Q the conditional KL of P from Q given the past. If δ_t^Q ≤ κ_Q for all t then E_P[τ] ≥ ln(1/α)/κ_Q; hence E_P[τ] ≥ ln(1/α)/min_{Q∈𝒩} κ_Q.
*Proof.* Data processing on the stopped σ-field with R = {τ<∞}: KL(P|_{F_τ}‖Q|_{F_τ}) ≥ KL(Ber(1)‖Ber(Q(R))) = ln(1/Q(R)) ≥ ln(1/α); the chain rule/optional stopping identifies the left side with E_P Σ_{t≤τ} δ_t^Q. ∎
**Corollaries.** (a) Enlarging the null from 𝒩₀ to 𝒩 ⊇ 𝒩₀ costs exponent loss min_{𝒩₀}KL − min_𝒩 KL ≥ 0, zero iff the KL-nearest member lies in 𝒩₀. (b) Achievability of exponent min_𝒩 KL(P‖Q) by a mixture/GRO e-process is known (Safe Testing, SD) and was not re-proved. **Closest prior:** Wald/Lai-type bounds `[memory]`; GROW. **Novelty:** none.
**Regret term (REDUCED TO KNOWN):** the *finite-n* cost of breadth is the redundancy of the numerator/null learner, ≈ (d/2) ln n for d free parameters (Rissanen; KT) `[memory]`. **Measured** (`07`): evidence needed grows ≈ **10.4 nats per null cell** (K = 8, 16, 32), versus ≈ 4–5 naive; K = 64, 128 not detected within 12 000 post-change observations.
**Unresolved (OPEN WITH PRECISE OBSTACLE):** a non-asymptotic *minimax lower bound on detection delay with unknown pre- and post-change laws*. Attempt 1: Bayes-mixture reduction of the null gives the coding redundancy lower bound, not a delay bound. Attempt 2: the Lai–Xing asymptotics `[memory]` (unread) show the unknown-parameter penalty can be second order (ln ln of the run length) when the pre-change segment is long; so the "price of breadth" depends on whether the null law is learnable from pre-change data at that resolution (K ≪ n₀). **Stopping criterion met:** two reductions failed to produce a delay bound.

## T2 — Learned-null uncertainty
**Prop T2 (PROVED, elementary).** Let C be the LR confidence set built from training counts n. For per-observation context weights w and post-change kernel ν₁, the achievable exponent of the certified test is Λ_cert = min_{ν∈C} Σ_c w_c KL(ν₁_c‖ν_c). Then: (a) on {ν\* ∈ C}, Λ_cert ≤ Λ_orc = Σ w_c KL(ν₁_c‖ν\*_c); (b) Λ_cert is continuous in C, so Λ_cert → Λ_orc as C shrinks to {ν\*} (full coverage, n_train → ∞); (c) contributions of contexts with zero training counts vanish (C is unconstrained there).
*Gaussian illustration* (shift μ, half-width ρ of the confidence interval, unit variance): Λ_cert/Λ_orc = (1 − ρ/μ)² for ρ < μ.
**Measured** (60 independent Markov structures; exact projections): retained fraction ρ̄ = **0.010, 0.240, 0.395, 0.691** (narrow/10³, narrow/10⁴, uniform/10³, uniform/10⁴); between-structure SD 0.014–0.12. Uniform coverage: 1−ρ̄ falls from 0.605 to 0.309 for ×10 training (∝ n^{−0.29} on two points; not a rate theorem). Observed delay inflation tracks the exact prediction: log(observed ratio/predicted ratio) = −0.05 (uniform/10⁴), +0.13, +0.19 (uniform/10³, narrow/10⁴).
**Unresolved:** a rate for 1 − ρ̄(n_train) in general (OPEN; would follow from the radius of C, ~ (dimension × ln n)/n_c, and the curvature of KL — not worked out).

## T3 — Misspecification and impossibility
**Prop T3a (PROVED, elementary).** If the alternative kernel ν₁ differs from ν\* only at contexts that have zero reach probability under the training policy, then (training law, test-stream law) under "ν\* in training, ν₁ in test" equals that under "ν′ in both", where ν′ := ν₁ on the unreachable contexts and ν\* elsewhere. Hence every procedure whose validity extends to the null "unchanged kernel ν′" has equal rejection probability under the change and cannot detect it. (Proposition 1′ applied to the two-sample structure.)
**Prop T3b (PROVED).** If P ∈ closure of 𝒩 then min_𝒩 KL = 0 and Λ = 0 for every valid procedure (Prop T1).
**Prop T3c (PROVED; Phase 9).** Persistent-regime ≡ random-time-change laws coincide (checked to 10⁻¹⁵), so no procedure valid over the stationary-regime null has power against the random-time change in a single trajectory.
**New counterexamples (explicit).** (i) *Approximate maximiser, exact dynamic programming* (`phase10_exact`): Bernoulli stream, truth p = 0.5 inside the null interval [0.3, 0.7]. Exact supremum denominator: P(reject within N) = 0.0001 (N = 100…5000). Denominator maximised over the grid {0.3, 0.7} (truth missed): **0.716 (N = 100), 1.000 (N ≥ 500)**. Grid {0.3, 0.4, 0.6, 0.7}: 0.0001 (N = 100), **0.767 (N = 500), 1.000 (N ≥ 1500)** — any finite grid that omits the truth eventually yields rejection probability → 1, at a speed set by KL(truth‖nearest grid point). (ii) *Fixed-n intervals under optional stopping*: Clopper–Pearson 95 % excludes the true p = ½ at some n ≤ 2000 in **468/1000** runs; the LR confidence sequence (δ = 0.05) in **32/1000**.

## T4 — Intervention coverage
**Prop T4 (PROVED).** If discriminating histories are reached with per-step probability q and carry per-visit KL κ, then any valid procedure needs E[τ] ≥ ln(1/α)/(qκ) (Prop T1 with δ_t ≤ qκ). Coverage thus multiplies the whole cost by 1/q, whereas model capacity enters additively through the redundancy. **Evidence:** at fixed training size 10⁴, uniform vs narrow coverage changes ρ̄ 0.691 vs 0.240 (×2.9); at fixed uniform coverage, ×10 training changes ρ̄ 0.395 → 0.691 (×1.75); narrow coverage, ×10 training: 0.010 → 0.240 (×24, but from a vacuous start). Active *test-time* design has headroom bounded by the Chernoff ratio (2.2–2.6× in Phase 9). **Verdict:** coverage dominates capacity when q is small; REDUCED TO KNOWN (Prop 3, Chernoff).

## T5 — Computational approximation
**Prop T5 (PROVED, elementary).** (a) If D_t ≥ sup_{Q∈𝒩} Q(D_t) pointwise then q/D_t is valid. (b) An approximate maximiser D̃_t = D_t·exp(−s_t), s_t ≥ 0 (shortfall), yields E_t^{approx} = E_t e^{s_t}: validity can fail whenever s_t exceeds the numerator's deficit by ln(1/α). (c) For fully observed categorical kernels the supremum over the null (and over an LR set) is exactly computable (closed form / one-dimensional bisection resolved in the conservative direction, `04-…`). (d) For latent-variable nulls no certified upper bound is available in this work. (e) A sup-free denominator (Bayes marginal under a prior π) is valid only **on average over π**: exact check — Bernoulli, null [0.3, 0.7], uniform prior: prior-average rejection probability 0.0458 (≤ 0.05) but **0.147 at the edges p = 0.3, 0.7** (`exact_checks.md`).
**Measured** (`05-…`): multi-start EM leaves a shortfall; a good alternative makes the e-process fail (15 % and 44 % type-I for 1-start budgets 60 and 20; 0/120 for ≥ 5 starts × ≥ 300 iterations with tolerance 10⁻⁶).
**Unresolved (OPEN WITH PRECISE OBSTACLE):** a certified upper bound on the HMM likelihood supremum. A Lipschitz/branch-and-bound relaxation over a small confidence region would be valid but pays ≈ n_test · L · r in the denominator (L Lipschitz constant of log-likelihood per observation, r the region radius); r ~ n_train^{-1/2} gives a penalty ~ n_test/√n_train — an *explicit computational price of certification*, not analysed. Hardness of HMM likelihood maximisation `[memory: Abe–Warmuth]`, unread.

## T6 — Hidden-state persistence and reset semantics
Restated from Phase 9 (R1–R5, Prop F): observation/memory resets change no law; state resets leave regime persistence intact (exact equality of the regime chain and the change-time mixture); only regime redraw or replicate resets are informative, and each is an interface assumption. **No mixing-rate-free guarantee exists** for single-trajectory persistent regimes (Prop F). A mixing-dependent guarantee needs a *known* β-coefficient (unverified Berbee/Yu), itself untestable under persistence. Status: REDUCED TO KNOWN + PROVED impossibility; no mixing result attempted beyond that.

## Failed or abandoned attempts (with stopping criteria)
1. Minimax detection-delay lower bound with unknown pre-change law — stopped after two reductions (above).
2. Robust-validity theorem for restricted-kernel stationarity tests under mixing — **disproved** (Prop B, Phase 9): the null is false for non-Markov generators.
3. General "approximate EM preserves validity" — **disproved** by the exact DP counterexample and the EM dose–response.
4. A price-of-validity lower bound beyond the information projection — none found; none is expected from T1.
5. A closed-form rate for 1 − ρ̄(n) — not attempted (stopping criterion: needs KL curvature on a confidence set; outside the bounded effort).

## Supplement: Prop D′ (predictive-comparison test with a predictable conditional range) — derivation
Let p_t, q_t be predictable forecasts (class, comparator) and Δ_t = Brier(p_t, o_t) − Brier(q_t, o_t). Whatever the outcome law, Δ_t takes one of the values d_o = (‖p_t‖² − ‖q_t‖²) − 2(p_{t,o} − q_{t,o}), so its conditional range is the predictable R_t = 2(max_o(p_{t,o} − q_{t,o}) − min_o(p_{t,o} − q_{t,o})). With Z_t = Δ_t − E[Δ_t | F_{t−1}], Hoeffding's lemma gives E[e^{λ Z_t} | F_{t−1}] ≤ e^{λ² R_t²/8}. Put V_t = Σ_{s≤t} R_s²/4 (predictable). For every λ, exp(λ S^Z_t − λ² V_t/2) is a nonnegative supermartingale; averaging over λ ~ N(0, 1/ρ) gives M_t = √(ρ/(ρ+V_t)) exp((S^Z_t)²/(2(ρ+V_t))), and Ville yields P(∃t: S^Z_t ≥ √((V_t+ρ) ln((V_t+ρ)/(ρα²)))) ≤ α. Under the weak null Σ_{s≤t}E[Δ_s|F_{s−1}] ≤ 0 ∀t, S_t = ΣΔ_s ≤ S^Z_t, so the same boundary controls P(reject). **Status:** PROVED (elementary; follows the Howard et al./Choe–Ramdas template with a predictable range); Monte-Carlo check with dependent signs and a time-varying predictable range: 0/300 rejections (`test_adaptive_range_boundary…`). Not found in the sources read in this exact form (class: corollary).
