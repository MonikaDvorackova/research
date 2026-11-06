---
id: topic-bostrom-world-models-phase9-po
title: "Proof-obligation status register and the PO-8/PO-10/PO-12 results"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [proofs, obligations]
---

# Proof-obligation register (Phase 9)
Status vocabulary: **PROVED**, **DISPROVED**, **REDUCED TO KNOWN RESULT**, **OPEN WITH PRECISE OBSTACLE**.
| ID | Obligation | Status | Where |
|---|---|---|---|
| O1 | continuous-space extensions of P1, P3, P4, P7, P8 | OPEN WITH PRECISE OBSTACLE (measurability, regular conditional probabilities; Kleijn–van der Vaart-type conditions for P8) | – |
| O2 | link ε_t to generalisation of a learned class | OPEN (not attempted) | – |
| O3 | tightness of c^t in P3(a) | OPEN WITH PRECISE OBSTACLE (no lower-bound construction found) | – |
| O4 | check P1 against Armstrong/Castro full texts | OPEN (inaccessible/abstract only) | – |
| O5 | composite-null/optional-stopping P5 | **REDUCED TO KNOWN** (e-processes; Ville) | `01` |
| O6 | theorem on when adaptivity strictly increases sup TV | OPEN | – |
| O7 | finite-sample absorption | OPEN | – |
| PO-2 | adaptive Wald lower bound | **PROVED** | `01` |
| PO-7 | validity of confidence-set denominator | **PROVED under stated assumptions (A4)**; power studied empirically only | `01`, dev F |
| PO-8 | adaptive design frontier | **REDUCED TO KNOWN RESULT** (Chernoff max–min; Prop E below) + dev evidence that the benchmark has almost no tension between targets | below |
| PO-9 | latent dimension to absorb a deterministic change | OPEN WITH PRECISE OBSTACLE: needs Hankel-rank theory for non-stationary laws; the counter construction gives an upper bound T·S only | – |
| PO-10 | validity under persistence and misspecification | **REDUCED TO KNOWN RESULT** (positive parts) + **PROVED impossibility** (single trajectory, persistent regime) | below |
| PO-11 | n⋆ ≈ (d_rich − d)/(2δ) | OPEN (folklore; two numerical instances) | Phase 8 D3 |
| PO-12 | reset semantics | **PROVED** (R1–R5) | below |

## PO-10: validity under latent persistence and misspecification
Let 𝒩 be a null (set of data laws) and φ a level-α procedure over 𝒩.
**Prop A (reduced to known).** If 𝒩 = {laws with conditional kernel p_θ(o_t | h_{t−1}, a_t), θ ∈ Θ₀}, q is any predictable normalised conditional law and the denominator is the exact sup over Θ₀, then P_θ(∃t: q(D_t)/sup_{θ′∈Θ₀} p_θ′(D_t) ≥ 1/α) ≤ α for adaptive predictable policies. *Proof:* D1 §1; Emmenegger et al. Thm 1; Wasserman et al. Thm 9/11.
**Prop B (what E_ctx tests).** For E_ctx, 𝒩_ctx = laws under which the conditional law of o_t given the *entire past* and a_t equals ν(·|x_t) with ν time-invariant. A stationary hidden-state generator is in 𝒩_ctx iff its observation process is first-order Markov in x_t, which is non-generic. **No mixing or memory condition changes this**: mixing makes pooled frequencies converge but does not make the conditional law given the past depend on x_t only. Hence "robust validity of E_ctx under misspecification" is **false as a theorem**, and rejections are rejections of 𝒩_ctx.
**Prop C (valid under any stationary generator with perfect resets).** Let episodes be independent given their action sequences with common conditional law ν(·|c) (perfect resets of state *and* regime; any hidden structure). Then the categorical episode-level model {ν} contains the truth, and Prop A gives validity for E_ep. *Cost:* the numerator's regret is ≈ ((|C|(|Y|−1))/2) ln n with |C|·|Y| = 27·81; the dev run shows zero rejections even for a large change (M3, 0/30).
**Prop D (valid under arbitrary dependence).** Let f_t, g_t be predictable probability forecasts, S a proper score with range width w, Δ_t = S(f_t, o_t) − S(g_t, o_t), μ_t = E[Δ_t | F_{t−1}]. Under 𝒩_comp = {Σ_{s≤t} μ_s ≤ 0 ∀t a.s.}, P(∃t: Σ_{s≤t} Δ_s ≥ (w/2)√((t+ρ) ln((t+ρ)/(ρα²)))) ≤ α. *Proof.* Z_s = Δ_s − μ_s are martingale differences with conditional range ≤ w, hence conditionally (w/2)²-sub-Gaussian (Hoeffding's lemma). For λ ~ N(0, 1/(σ²ρ)) the process M_t = ∫ exp(λ S^Z_t − λ²σ²t/2) dλ = √(ρ/(ρ+t)) exp((S^Z_t)²/(2σ²(t+ρ))) is a nonnegative supermartingale with M₀ = 1; Ville gives P(∃t: M_t ≥ 1/α) ≤ α; M_t ≥ 1/α ⇔ (S^Z_t)² ≥ σ²(t+ρ) ln((t+ρ)/(ρα²)). Under 𝒩_comp, Σ Δ ≤ S^Z. ∎ (Reduced to Choe–Ramdas-type constructions and Robbins' normal mixture; sources not read.) The null is **predictive**: it says the class forecaster is not conditionally worse than the comparator; a rejection licenses "the comparator predicts better", not any statement about mechanism. Validity holds under persistence, misspecification and hidden regimes because no model of the data is assumed.
**Prop F (impossibility, single trajectory).** Let P_reg be the law of a stream produced by a stationary generator with a persistent latent regime (switching with probability ε per episode) and P_chg the law of a stream with a mechanism change at a random time with the same distribution and the same pre/post kernels. If P_reg = P_chg as laws on the observed stream (exact check: `regime_hmm_law` = `change_time_mixture_law` to 10⁻¹⁵), every procedure has equal rejection probability under both. Hence no procedure that is valid over a null containing P_reg can have power against P_chg. *PROVED* (equality of laws). Replicates of the same process do not help, because the equality holds for the replicate law too.
**Mixing remark (reduced to known, unverified).** If the stream is β-mixing with known coefficients and the test uses blocks separated by gaps k, a coupling argument gives type-I ≤ α + (#blocks)·β(k) (Berbee, Yu; `[memory]`, not read). It requires a *known* mixing rate, which is itself an untestable premise in the persistent-regime case (Prop F).
**Verdict PO-10.** A guarantee under misspecification exists only for **predictive** nulls (Prop D) or for **saturated nulls under resets** (Prop C), both known. A guarantee for "no mechanism change" under latent persistence is impossible (Prop F). There is **no** nontrivial robust-validity theorem for restricted-kernel stationarity tests (Prop B).

## PO-8: adaptive intervention and identification
**Prop E (reduced to known).** For finitely many hypotheses and iid outcomes per action, the optimal error exponent for deciding between the true hypothesis h⋆ and a set 𝒜 of alternatives with an adaptive design is max_{λ∈Δ(actions)} min_{h′∈𝒜} Σ_a λ_a KL(h⋆(·|a)‖h′(·|a)) (Chernoff 1959 `[memory]`; Naghshvar–Javidi 2013 `[memory]`). Taking whole action sequences as "actions" (valid under perfect resets) applies it to the POMDP benchmark. Different targets (class adequacy, member identification, learned-model uncertainty) correspond to different alternative sets 𝒜, hence different LPs; the Pareto frontier is the set of maximisers of convex combinations.
**Evidence.** (i) Dev B: the Chernoff-optimal gain over uniform design is 2.17, 2.39, 2.57 (pc0–pc2); X1 observed P4/P2 gains 2.01, 1.74, 1.85 = 93 %, 73 %, 72 % of optimum. (ii) Dev G: the member-identification exponent changes by 17 % as q goes 0 → 1 while adequacy detection rises 37-fold: the targets are nearly non-conflicting in this benchmark. (iii) Identifying a member within M is ≈ 40× slower than detecting a gross inadequacy.
**Verdict PO-8.** No minimax/regret frontier beyond known Chernoff theory and the policy-coverage bound (Prop 3) was found. A conflict between targets requires a constructed case where the disagreement sets lie on different actions; none was built. Status: REDUCED TO KNOWN; the open item is an *adaptive* (history-dependent) Chernoff analysis for non-iid POMDP outcomes (OPEN WITH PRECISE OBSTACLE: outcomes are not iid per action).

## PO-12: reset semantics
Five operations act on the experiment, not on the world's law unless stated.
**R1.** *Observation reset* (an episode-boundary marker that is a function of the agent's own clock/interface) and *agent-memory reset* do not change the law of the (action, observation) stream. They cannot break any observational equivalence; a memory reset can only coarsen the observer (restricts tests to episode-local ones). *Proof:* equivalence is equality of laws; a deterministic function of the record adds nothing; restricting the test class shrinks the set of distinguishers. ∎
**R2.** *Environment-state reset* (hidden state redrawn from b₀, regime/parameters persist) does not break the equivalence "persistent regime ≡ random-time change": the law of the episode stream is the regime-chain mixture (exact equality, `test_regime_chain_equals_change_time_mixture_exactly`). ∎
**R3.** *Latent-regime redraw* (regime resampled independently at each reset) makes episodes i.i.d. mixtures; then "stationary regime" (iid) and "persistent change" (non-iid) have **different** laws whenever the kernels differ, so they are distinguishable (Prop C gives a valid test). ∎ But R3 is an *intervention on the environment*: it exists only if the reset reaches the regime variable.
**R4.** *Full generative reset* (independent replicate runs of the whole process, change schedule included) breaks the equivalence "world constant θ₀ fixed" ⇔ "θ₀ drawn once per run from a prior and realised as θ₀": single-run laws coincide for the realised value, replicate laws differ (two-point example: θ ∈ {0.3, 0.7} drawn per run). It does **not** break equalities of the single-run law such as R2. ∎
**R5 (interface lemma).** No operation that merely repackages the record (R1) breaks an equivalence; only operations that alter the environment's response law (R3, R4, or playing a discriminating action — Prop 1′) can. Whether such an operation is *available* is a premise about the agent's action space/interface, not something the data supply. In particular an "episode reset" supplied by an experimenter's interface does not establish that the hidden physical mechanism or regime was reset; the validity of E_ep rests on that unverifiable premise (it is part of the null).
