---
id: topic-bostrom-world-models-phase8-problem
title: "Phase 8: formal problem definition and identifiability taxonomy"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [formal, taxonomy, identifiability]
---

# Formal problem and taxonomy

## 0. Baseline check (X1 record, verified against artifacts)
Commit `2b482c8` is HEAD of `research/bostrom-world-models`; draft PR #10 is open; 274 tests now pass (269 before Phase 8). From `results/x1_confirm/`: 36 000 runs; pooled null rejection 244/14 400 = 1.69 %; H1–H3, H4a supported; H4b, H4c contradicted; H5 inconclusive by the rule. These match `analysis.md`/`analysis.json`. **"36 000 runs" are not 36 000 independent scientific units**: the independent units are 30 environment instances (seeds), each a ±8 % numerical jitter of one hand-built POMDP structure (so the number of independent *environment structures* is one), with R = 20 runs per cell sharing the instance. For null rejections the intra-seed correlation is empirically nil (ICC(seed) = −0.0003, design effect 1.00, computed from the raw runs in Phase 8), which is why run-level binomial bounds happened to be adequate; efficiency ratios use the seed as the unit. X1 is preserved unchanged.

## 1. Objects
- **Environment** E: a controlled stochastic process on histories. Observable content: the *interaction kernel* K_E(o_t | h_{t−1}, a_t), h = (a₁, o₁, …). Latent state, context and mechanism are modelling devices that generate K_E; the observer never sees them. A POMDP (S, A, O, T, Z, b₀) is one realisation; also allowed are a deterministic or random **context** c_t (exogenous) that enters the kernel, K_{θ,c_t}, and kernels that vary with time.
- **Agent history** h_t; **policy** π(a_t | h_{t−1}) (possibly randomised, adaptive); **admissible intervention class** Π (the policies the agent can execute); **resets** ρ: whether the agent can restart episodes and whether a restart redraws the latent regime.
- **Learned model class** M = {m_θ : θ ∈ Θ}: kernels, with prior/posterior over θ given D_n; **computational constraint** 𝒞: the maximisation/inference operations the agent can actually carry out (exact; certified-approximate; uncertified-approximate).
- **Budget** n (episodes) and horizon T per episode. The observer receives (a, o) only; it never receives E, θ, c (unless a variant states otherwise), labels, or oracle likelihoods.
- **Experimenter vs observer knowledge.** The experimenter knows the generator and so the exact law P_E^π on Π; the *identifiability partition* of a benchmark case (§3) is computed by the experimenter and used only for scoring.

## 2. Four explanations of predictive failure, defined by laws (not by labels)
Fix (M, Π, n, ρ). Let KL_π(E‖m) be the expected-per-episode KL under π.
- **A. Epistemic gap.** ∃ θ* with K_E = K_{m_θ*} on Π-reachable histories, but the posterior given D_n is not concentrated (credible set KL-diameter > τ). Property of (E, M, Π, n); resolves as n grows.
- **B. Class inadequacy.** inf_θ sup_{π∈Π} KL_π(E‖m_θ) > 0. **Relative to Π**: B_Π. If Π ⊂ Π′, B_Π can be false while B_Π′ is true (the benchmark's hidden-state control).
- **C. Distributional change (shift).** The *input* process to the learned kernel changes while the mechanism does not: the policy/visitation distribution, the initial condition, or an exogenous context c_t with K_{θ,c} fixed. Formally: E = (θ, c_·) with θ constant.
- **D. Mechanism change.** E = (θ_t, c_·) with θ_t not constant (transition or observation kernel changes).

**Non-circularity condition (Gate A).** A and B are defined from (K_E, M, Π) alone. **C and D are *not*:** they require a factorisation of K_E into (θ, c). That factorisation is a modelling choice and is not determined by K_E (Prop. T4). So the four-way partition is *not* an intrinsic property of an environment; **C vs D is meaningful only relative to a declared structure** 𝒮 ∈ {context observed?, context controllable?, modularity/sparsity of mechanism shifts, replicates with latent reset?, latent-dimension bound k}.

**Definition (mechanism change, class-relative).** D_k: the time-varying kernel sequence cannot be reproduced by any *stationary* process with at most k latent states (with a counter state, any finite-horizon change needs only O(horizon) states; so "genuine" change is relative to k and to the horizon). Without k the notion collapses (Prop. T4).

The categories are not mutually exclusive (e.g. B ∧ C, B ∧ D); the benchmark therefore labels *composite* cases explicitly.

## 3. Five notions of identifiability (kept separate)
1. **Structural identifiability** of a label ℓ: ℓ is constant on P-equivalence classes {E′ : P_{E′}^π = P_E^π ∀ π ∈ Π}. If ℓ is not constant, no observer, however powerful, can compute it.
2. **Statistical distinguishability:** TV(P_E^π, P_{E′}^π) > 0 for some π ∈ Π (n → ∞ separability).
3. **Finite-sample detectability:** exists a level-α test with power ≥ β at budget n against the specified alternative; bounded by TV(P_E^{π,n}, P_m^{π,n}) ≤ √(½ n ε) (Prop. T3).
4. **Computational feasibility:** the test/learning step is executable within 𝒞 with a guarantee (e.g. a *certified* upper bound on a likelihood supremum; Prop. T6).
5. **Epistemic justification:** the inferential step from a statistical conclusion (e.g. "M rejected") to a claim about mechanism, which needs premises beyond data (the ladder of Phase 6, Direction F).

## 4. Identifiability map (summary of Phase 8; details and evidence in `02-…`)
| Distinction | Structurally identifiable? | Under which assumptions it becomes possible | Evidence (this phase unless noted) |
|---|---|---|---|
| A vs B, below scale n·ε ≲ d | No (confounded, Le Cam) | n·ε ≳ c; a comparator class richer than M; plateau needs entropy reference | D3, T3 |
| A vs B, above scale | Yes statistically | comparator class of larger capacity and n ≥ n\* ≈ (d_rich − d)/(2δ) | D3: n\* ≈ 6×10³ predicted, sign change between 3×10³ and 10⁴ observed |
| B_Π vs B_Π′ | No under Π (TV = 0 without the discriminating action) | interventions reaching the disagreement set | X1 (H2), S3 |
| C (policy/coverage shift) vs D | **Yes within a class containing the truth** | conditional-kernel stationarity test; valid under pure policy shift | D2 S1: 0/100 false alarms; S2: 100/100 detections |
| C (latent context) vs D | **No** for a single trajectory (exact equivalence) | observed context; replicates with latent reset; modularity/sparsity premises | T4; exact check; D2b |
| B (stationary hidden regime) vs D (random-time change) | **No** (same law) in a continuing run | resets that redraw the regime; known dwell/mixing bound | D2b: 40/40 false alarms |
| D vs B when M cannot represent the change | masked | richer comparator | D2 S6: 0/100 |
| Prediction vs mechanism identification | **No** (dissociable) | interventions that separate the mechanisms | T5: Bayesian Occam |
| Learned-null adequacy testing | not a sound procedure unless the denominator dominates the true likelihood | certified sup; confidence-set denominator | T6: 98–100 % false alarms (frozen null), 39/40 (under-optimised maximiser) |
