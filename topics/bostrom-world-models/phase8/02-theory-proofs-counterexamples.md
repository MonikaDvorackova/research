---
id: topic-bostrom-world-models-phase8-theory
title: "Phase 8 theory: propositions, proofs, counterexamples, unresolved obligations (T1–T6)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [theory, proofs, counterexamples]
---

# T1–T6

Evidence code: **P** = proved here (elementary); **X** = exact finite-state verification; **S** = simulation diagnostic (exploratory); **O** = open obligation. **No result below is claimed as a new theorem.** Each is classified A (known) / B (restricted-setting instance). Files: `src/eid/phase8.py`, `tests/test_phase8.py`, `scripts/phase8_diagnostics.py`, `scripts/phase8_transient.py`, `results/phase8/`.

## T1 — Different causes, identical observable distributions  [P, X; class A]
**Prop T1.** A label ℓ ∈ {A,B,C,D} that depends on anything beyond P_E^π cannot be computed from data. *Proof.* If E, E′ have equal laws on Π but ℓ(E) ≠ ℓ(E′), any measurable function of data takes the same value in distribution on both. ∎
**Counterexamples (explicit).**
1. *C vs D (latent context ≡ mechanism change)*: see T4; exact check, max |Δ law| = 2.8×10⁻¹⁷ over all 81 action sequences (`test_time_varying_kernel_equals_stationary_counter_model`).
2. *B_Π vs not-B_Π′*: the Phase 5 control (Eeq vs Et) and X1 H2: TV = 0 without action 2 (exact).
3. *Stationary hidden regime ≡ random-time mechanism change* (continuing run): the same process; see D2b.
4. *A vs B* at scale ε ≲ 1/n: T3.

## T2 — Intervention-dependent identifiability  [P, X, S; class A/B]
**Prop T2.** If P_E^π = P_{E′}^π for all π ∈ Π₀ and TV(P_E^π′, P_{E′}^π′) > 0 for some π′ ∈ Π ∖ Π₀, then E, E′ are indistinguishable under Π₀ and distinguishable under Π; a test at budget n has power governed by the *reach probability* of the discriminating histories under π′ (Prop. 3, policy-ratio c^t). Minimal assumptions: (i) a policy in Π that reaches the disagreement set with positive probability, (ii) enough budget relative to the reach-weighted KL.
**New instances.** (a) Stationarity e-process, kernel change in action-2 rows: detected 100/100 under the wide policy (median detection 275 episodes after the change), **0/100 when action 2 is rare** (S2 vs S3). (b) *Reset with latent-regime redraw* is itself an intervention: it removes the B-vs-D confound (S4/S5: 0/100 false alarms for a hidden-state truth with 4-step episodes; D2b: 40/40 for a continuing run). The identifying content of the reset is that the regime is redrawn; a reset that preserves a persistent regime changes nothing (O: not run).
**Proof sketch for the reset claim.** If the regime process is stationary and independent across resets, the episode-indexed kernels are exchangeable, so no systematic drift across episodes exists, while a calendar-time mechanism change leaves all later episodes different from earlier ones.

## T3 — Finite-data ambiguity (epistemic vs misspecification)  [P, S; class A]
**Prop T3 (two-point bound).** For any n, any policy π (adaptive allowed), any m ∈ M and environment E with per-episode KL_π(E‖m) ≤ ε, any test φ with P_m(φ = 1) ≤ α has P_E(φ = 1) ≤ α + √(½ n ε). *Proof.* Pinsker and the chain rule for KL of adaptively collected histories. ∎
**Consequences.** (i) Misspecification of size ε < 2(β − α)²/n cannot be detected with power β at budget n: **A and B are confounded below that scale for every test**. (ii) A d-parameter learner has expected excess loss ≈ d/(2n); misspecification of size ≲ d/(2n) is indistinguishable in magnitude from estimation error; the crossover of a richer comparator class occurs at n\* ≈ (d_rich − d)/(2δ). (iii) The plateau of one class's learning curve is H + δ (entropy plus misspecification); **a single learning curve cannot split aleatoric entropy from misspecification** — a comparator class is needed (the same fact as X1's need for an alternative family W).
**Evidence (D3).** Order-1 count learner, Markov truth: excess loss × n = 11.7 at n = 1000 and 12.4 at n = 10⁴ (d/2 = 12). Hidden-state truth E0: exact plateaus δ₁ = 5.54×10⁻² (order 1), δ₂ = 4.95×10⁻² (order 2); the comparator gap L₁ − L₂ is −2.8×10⁻³ at n = 3000 and +3.3×10⁻³ at n = 10⁴ — predicted crossover (d₂ − d₁)/(2δ₁₂) ≈ 6×10³. The richer learner is *worse* until then.

## T4 — Distribution shift vs mechanism change  [P, X, S; class A]
**Prop T4 (absorption).** For any finite-horizon time-varying kernel sequence (K_t)_{t≤T} there is a stationary POMDP (state × counter) with the same observation law for every policy. *Proof.* Augment the latent state by a counter c_t advancing deterministically; define emission/transition by K_{c}. ∎ (Hidden-mode MDPs, Choi–Yeung–Zhang 1999, are a stochastic version; summary-level.) **Exact check:** `counter_augmented` vs independent time-varying recursion, max difference 2.8×10⁻¹⁷.
**Corollary.** Shift (θ fixed, context varies) and mechanism change (θ_t varies) are observationally identical when the context is latent and the trajectory is single. Any claimed distinction rests on a premise: (P1) context observed, (P2) context manipulable, (P3) modularity / sparse mechanism shift (only a few mechanisms change; Schölkopf et al., Perry et al., Chen et al. — search-description level), (P4) replicates with latent reset, (P5) bounded latent dimension k.
**Does the distinction need privileged access?** Yes, to context or to structure; without it the label is not a property of the data.
**Within a class that contains the truth and a conditional kernel given observed contexts, C is distinguishable from D** (S1 vs S2).
**Prop T4′ (validity of the stationarity e-process).** Let contexts x_t = (previous observation, action) be predictable and the null be "o_t | x_t has one time-invariant law ν(·|x)". E_k = [G⁻¹ Σ_j ML(counts before τ_j) ML(counts after τ_j)] / sup_ν ∏ ν(o_t | x_t), with Dirichlet(½) marginal likelihoods, satisfies P_ν(∃k: E_k ≥ 1/α) ≤ α. *Proof.* The numerator is a mixture of predictable laws; the denominator dominates ν\*'s likelihood; E_k ≤ L_k, a nonnegative supermartingale; Ville. ∎ Evidence: 0/100 false alarms in S0, S1 (Markov truth, including policy shift). It is a standard change-detection e-process (Shin–Ramdas–Rinaldo e-detectors, summary-level); **class A**.
**Counterexample to robustness (S, the strongest of this phase).** If the truth is *not* in the null (conditional law given x_t is not time-invariant), Prop T4′ gives no guarantee, and it fails: a stationary hidden-regime process (4 hidden states, dwell ~1/ε steps, order-1 observation class) triggers rejection in **40/40** continuing runs for ε = 0.0005, 0.002 and 39/40 for ε = 0.01 — **and 40/40 when the hidden chain is started from its stationary distribution**, so the rejection is caused by regime persistence, not by an initial transient. With episode resets (4-step episodes) the same hidden-state structure gives 0/100 (S4, S5). So a mechanism-change detector's type-I error depends on an unverifiable mixing/reset premise.

## T5 — Predictive success vs mechanism identification  [P, X; class A (Lindley–Bartlett), B (instance)]
**Prop T5 (dissociation).** Let m₁ imply Bernoulli(½) on the probed class and m₂ imply Bernoulli(ψ), ψ ~ U(0,1), with the truth being m₂ at ψ = ½; the two differ only under an unprobed intervention. With equal prior, E[P(m₂ | D_n)] = Σ_k Bin(n, ½)(k) · 2ⁿ/(2ⁿ + (n+1)C(n,k)), which decays proportionally to n^{-1/2} (the posterior odds are ≈ (π/2n)^{1/2} at k = n/2; the expectation over k is about twice that at n ≈ 10³) while the predictive KL of the posterior-mean predictive tends to 0 like 1/n. So mechanism-identification accuracy (posterior mass on the true mechanism) **decreases** while predictive accuracy **improves**. *Proof.* Posterior odds m₂:m₁ = 2ⁿ / ((n+1)C(n,k)) ≈ (π/2n)^{1/2} for k ≈ n/2 (Stirling). ∎
**Exact values** (`occam_dissociation`): n = 10: E P(m₂|D) = 0.374, KL 1.4×10⁻²; n = 100: 0.186, 9.0×10⁻⁴; n = 1000: 0.077, 3.8×10⁻⁵; n = 3000: 0.048, 8.1×10⁻⁶.
**Also** Prop 3 (Phase 5/6): the mechanism distance on the wide class exceeds the training-class distance by a factor ≈ 1/q (Phase 6 diagnostic). These are the known facts (Bayesian Occam factor / Jeffreys–Lindley; nonidentifiability results in ICA/representation learning, search-description level). **Class A.** The tight general frontier (X2) remains O.

## T6 — Which X1 guarantees survive learned/estimated likelihoods  [P, S; class A/B]
Recall Prop X1-V (D1): E_t = q(D_t)/max_{m∈M} p_m(D_t) is valid because max_m p_m(D_t) ≥ p_{θ*}(D_t) and q is predictable.
**T6a (frozen learned null is invalid).** Replace the denominator by a fixed estimate p̂ (trained once). Under the *unchanged* truth, log E_t grows at rate KL(E‖p̂) − KL(E‖q) per observation; if p̂ ≠ E on any context the test rejects with probability → 1 as the test horizon → ∞ (LLN), with typical rejection time ≈ regret(q)/KL(E‖p̂). *D4a:* count model trained once on a narrow policy (p(action 2) = 0.02) and tested on a wide stream of the **same** Markov kernel (pure policy shift): false-alarm rate **100/100 (n_train = 100), 98/100 (1000), 3/100 (10⁴), 2/100 (10⁵)** within N = 3000; median rejection episodes 115, 808, 2, 1. The decline at large n_train is the regret-limited power of the alternative within a finite N, not validity: onset time grows ∝ n_train.
**T6b (under-optimised maximiser).** If the denominator is an *approximate* supremum p̃ ≤ sup, then E_t^{approx} = E_t · sup/p̃ and the guarantee is void; log E grows at KL(E‖approx class) − KL(E‖q). *D4b:* truth = member n10 of the class, denominator maximising over a coarse subset: **39/40** rejections vs **0/40** with the exact maximiser. (If the search space is *smaller by design* the test is of the smaller class and rejection is correct for it; the failure is the silent mismatch between the intended and searched class.)
**T6c (stationarity e-process).** Valid with the in-sample MLE (no external model) when the truth is in the class (T4′); fails beyond (T4 counterexample).
**T6d (repair, proved, not implemented).** Let C be a (1−α₁) confidence set for θ\* from independent training data; E′_t = q_t / sup_{θ∈C} p_θ(D_t). Then P(reject) ≤ α + α₁. *Proof.* On {θ\* ∈ C}, E′_t ≤ L_t; union bound. ∎ Cost: power loss from the widened denominator (≈ the confidence radius); computing a certified sup over C for neural world models is an open problem **[O]**.
**Not shown:** that estimated likelihoods *with* certified upper bounds lose little power; behaviour for GRU/transformer nulls.

## Summary of obligations
| ID | Statement | Status |
|---|---|---|
| PO-7 | Validity for learned/estimated nulls via confidence-set denominator (T6d) | proved; power not studied |
| PO-8 | Margin law for adaptive minimax | open |
| PO-9 | Minimal latent dimension needed to absorb a deterministic change of known time | open |
| PO-10 | Robust validity of the stationarity e-process under misspecification with mixing assumptions (what dwell/mixing bound suffices?) | open; counterexample for long dwell |
| PO-11 | Quantitative n\* ≈ (d_rich − d)/(2δ) as a theorem under regularity | open (folklore; one numerical instance) |
| PO-12 | Reset-with-persistent-regime does not break the C/D confound (T2 sketch) | open |
