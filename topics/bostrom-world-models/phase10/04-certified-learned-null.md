---
id: topic-bostrom-world-models-phase10-certified
title: "Certified learned-null sequential procedure: construction, proof, verification"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [certified, e-process, learned-null]
---

# Certified learned-null procedure (`src/eid/certified_null.py`)

## 1. Specification
1. **Null model class.** Categorical context kernels ν(·|c), contexts c = x_t = (previous observation or START, action) predictable. Null: the conditional law of every outcome given the *entire past* (training and test) equals ν\*(·|x_t), ν\* time-invariant and unknown. (This is a restricted-kernel null; for non-Markov generators the null is false and rejection is misspecification, not type-I — Phase 9.)
2. **Training protocol.** Any predictable (adaptive) context/action sequence; the training length may be a data-dependent stopping time.
3. **Confidence set.** C_n = {ν: Σ_{c,o} n_co log ν_co ≥ log q(D_train) − log(1/δ)}, q = prequential Dirichlet(½) (predictable, normalised; log q = Σ_c Dirichlet-multinomial log-marginals, exactly the sequential product).
4. **Coverage guarantee (cited + proved).** R_n(ν\*) = q(D_n)/p_ν\*(D_n) is a nonnegative supermartingale (E[R_n | F_{n−1}] = R_{n−1} Σ_{o: p>0} q(o|·) ≤ R_{n−1}), so P(∃n: ν\* ∉ C_n) ≤ δ by Ville. This is Theorem 1 of Emmenegger–Mutný–Krause (read), in categorical form.
5. **Test statistic.** On a fresh stream with counts m_k after k checkpoints: E_k = exp(L_q(m_k) − sup_{ν∈C} Σ m_co log ν_co), L_q the Dirichlet(½) log marginal (the prequential numerator).
6. **Supermartingale property.** Condition on the training σ-field at a stopping time n̂; on A = {ν\* ∈ C_{n̂}} (F_{n̂}-measurable), E_k ≤ q(D_test)/p_ν\*(D_test) =: L_k, a nonnegative supermartingale with L_0 = 1.
7. **Predictability/measurability.** Test contexts are F-predictable (may depend on training data and earlier test outcomes); q is predictable; the denominator is a deterministic function of counts and C.
8. **Optional stopping.** Ville's inequality applies to L_k at arbitrary stopping times; coverage is time-uniform in n, so the training stopping time may be data-dependent.
9. **Adaptive interventions.** Policy factors cancel in the ratio q/p_ν\*; verified by exact enumeration with an adaptive context rule c_{t+1} = o_t and by an adversarial policy (below).
**Theorem (conditional validity).** Under 1–3, P_ν\*(∃k: E_k ≥ 1/α) ≤ α + δ. *Proof.* P(reject) ≤ P(A^c) + E[1_A P(∃k: L_k ≥ 1/α | F_{n̂})] ≤ δ + α. ∎ **The guarantee is α + δ, not α; both are accounted for.** The set C is a high-probability object: with probability up to δ the truth is outside and no claim is made.
**No independence assumption between training and test data is needed** for this null (the kernel condition is on the whole past); independence matters only for hidden-state truths, which are outside the null.

## 2. The supremum (exactness and conservatism)
Maximise Σ m log ν s.t. Σ n log ν ≥ γ, rows on the simplex. Lagrangian solution ν_co(λ) = (m_co + λ n_co)/(M_c + λ N_c); λ ≥ 0 by bisection so that the constraint binds (g(λ) = Σ n log ν(λ) − γ is increasing, g(∞) ≥ ln(1/δ) > 0 because the Dirichlet marginal never exceeds the maximised likelihood). The value Σ m log ν(λ) is non-increasing in λ, so returning the bisection endpoint at which the constraint is slightly violated gives a value ≥ the true supremum: **the numerical error is resolved in the safe direction.** If the bracket cannot be certified feasible the code falls back to the unconstrained MLE value (also ≥ sup). Rows with m_c = 0 or n_c = 0 are handled exactly (unvisited training contexts: the row is unconstrained).

## 3. Verification (Part V items 8–10)
| Check | Result |
|---|---|
| Supremum vs SLSQP on random instances | agrees (≥ and within 10⁻³) — `test_sup_matches_numerical_optimiser…` |
| **Exact** time-uniform coverage by exhaustive enumeration (2 contexts, adaptive rule, 4 training steps, δ = 0.3, 9 true kernels) | P(truth outside C at some prefix) ≤ 0.1252 (≤ 0.3) |
| **Exact** crossing probability (α = 0.4, 5 test steps) | 0.0000 for all 9 truths — **vacuous at this horizon; not evidence** |
| **Exact** expected e-value by DP over count states (N = 8, δ = 0.3, truth in C) | max E[E_N] = 0.20–0.23 (≤ 1); with truth outside C up to 0.93 (no guarantee) — `exact_checks.md` X3 |
| Time-uniform coverage, 60 independent Markov structures × 5 training streams of 5000 episodes (200 checkpoints) | exclusion in **0/300** (UB 0.010) |
| Type-I under the intended null, 60 structures × 30 runs per cell, four training conditions, 1500 test episodes | **0/7200**; per-cell 0/1800 (UB 0.0017); oracle 0/7200 |
| Adversarial adaptive test policy (contexts chosen to maximise the numerator's advantage), 30 structures × 10 runs, α = δ = 0.05 | **0/300** |
| Adversary against the *old* CP-box implementation | fixed-n CP boxes: truth excluded at some n in 468/1000 optional-stopping runs vs 32/1000 for the LR set |
| Determinism | 7 stored jobs re-executed: 0 mismatches |
**Limits of the evidence.** The procedure is very conservative (0 rejections everywhere), so the Monte-Carlo checks cannot distinguish "validity" from "never rejects"; the exact expectation and coverage checks are non-vacuous but small. The guarantee rests on the proof; the experiments check the implementation.
**What it cannot do.** It certifies nothing for latent-variable or neural nulls (no certified supremum); it has no power on contexts absent from training (T3a); and it tests a restricted-kernel null.
