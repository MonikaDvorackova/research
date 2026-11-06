# Proof note: a two-state time-homogeneous observer with a hidden periodic informative phase

Self-contained for independent review. **Status: Theorem 3 below is proved (complete argument; each step also checked numerically — see the last section); it has not been externally reviewed.** It is a modest, special-case result; its novelty is *not established* (it contains the two-state case of the Hellman–Cover finite-memory optimum as K = 1). See `originality-and-proof-status.md`.

## Setting
Two hypotheses h ∈ {0,1}. A hidden phase cycles deterministically with period K ≥ 1; phase 0 is *informative*. The observer is a **time-homogeneous 2-state stochastic automaton**: memory M_t ∈ {0,1}; from memory state i it picks action probe with probability q_i (otherwise idle), receives a signal Y ∈ {0,1}, and moves to memory state 1 with probability t_{iy}. Signal law: if (probe and phase 0), P_h(Y=1) = p_h; otherwise P(Y=1) = ½ under both hypotheses. Let p_1 = ½ + c, p_0 = ½ − c, 0 < c < ½. The observer sees neither phase nor time. It guesses g(M_t) with g optimal; with equal priors the asymptotic (Cesàro-averaged) error is ½(1 − TV), TV being the total variation distance between the time-averaged memory laws under h = 1 and h = 0; for two states TV = |P̄_1(M=1) − P̄_0(M=1)|. We consider **irreducible** automata: b_0, b_1 ∈ (0,1) (notation below), for which every map below is a contraction and the periodic stationary regime is unique.

## Notation
b_i = ½(t_{i0}+t_{i1}); δ_i = t_{i1} − t_{i0}; r_i = q_i δ_i; σ = b_1 − b_0; s = 1 − σ; u = 1 − b_1; v = b_0 (so s = u + v); B(x) = b_0 + σx; R(x) = r_0(1−x) + r_1 x. Constraints: |r_i| ≤ ρ_i with ρ_0 = 2min(v, 1−v), ρ_1 = 2min(u, 1−u) (because |δ_i| ≤ 2min(b_i, 1−b_i)). Let γ = σ^{K−1}, ε = γc/(1−γσ), η = sε, θ = ε²(r_1 − r_0)², x_B = b_0/(1−σ).

## Lemma 1 (one-step maps)
For x = P(M_t = 1): an uninformative step maps x ↦ B(x); the informative step under h maps x ↦ A_h(x) = B(x) + c_h R(x), with c_1 = c, c_0 = −c.
*Proof.* From memory state i the probability of moving to 1 is α_i = t_{i0} + P(Y=1|i)δ_i. Uninformative: P(Y=1|i) = ½ ⇒ α_i = b_i. Informative under h: P_h(Y=1|i) = ½ + c_h q_i ⇒ α_i = b_i + c_h r_i. Then x′ = α_0(1−x) + α_1x. ∎

## Lemma 2 (exact identity)
TV = 2c |R(x̂₀)| / (K(1 − σ)), where x̂₀ is the mean of the two hypotheses' memory laws at the start of the informative step in the periodic stationary regime.
*Proof.* Let d = x^{(1)} − x^{(0)}. Since R is linear, at the informative step d′ = σd + c(R(x^{(1)}) + R(x^{(0)})) = σd + k with k = 2cR(x̂₀); at uninformative steps d′ = σd. Periodicity with d₀ the value at the start of the period: d¹ = σd₀ + k, d^K = σ^{K−1}d¹ = d₀, so d₀ = σ^{K−1}k/(1−σ^K), d¹ = k/(1−σ^K). The sum over the K step-start values is S = d₀ + d¹(1+σ+…+σ^{K−2}) = k/(1−σ^K)·[σ^{K−1} + (1−σ^{K−1})/(1−σ)] = k/(1−σ). The Cesàro-averaged difference is S/K. ∎

## Lemma 3 (closed form for R(x̂₀))
R(x̂₀)(1 − θ) = R(x_B) = (r_0 u + r_1 v)/s.
*Proof.* The entry law satisfies u_h = B^{K−1}(A_h(u_h)). With w_h = u_h − x_B and B^n(y) − x_B = σ^n(y − x_B): w_h = γ(σw_h + c_hR(u_h)), so w_h = γc_hR(u_h)/(1−γσ). Hence u_1 − u_0 = 2γcR(x̂₀)/(1−γσ) and x̂₀ − x_B = ½(w_1+w_0) = γc(r_1−r_0)(u_1−u_0)/(2(1−γσ)) = γ²c²(r_1−r_0)R(x̂₀)/(1−γσ)². Insert in R(x̂₀) = R(x_B) + (r_1−r_0)(x̂₀−x_B) and solve; 1 − x_B = u/s and x_B = v/s give R(x_B). ∎

## Proposition 4 (achievability)
sup TV ≥ 2c/K. *Proof.* t_{iy} = 1[y=1], q_i = 1 ("memory = last signal"): b_i = ½, σ = 0, r_i = 1, R ≡ 1, so TV = 2c/K by Lemma 2. ∎

## Reduction of the upper bound
By Lemmas 2–3, TV ≤ 2c/K ⇔ |R(x̂₀)| ≤ s ⇔ |r_0u + r_1v| ≤ s²(1 − θ) (when θ < 1), i.e.
 (★) F(r_0, r_1) := |r_0u + r_1v| + η²(r_1 − r_0)² ≤ s², for all |r_i| ≤ ρ_i.
(★) also implies θ ≤ 1, with θ = 1 only if r_0u + r_1v = 0; those degenerate parameters are limits of parameters with θ < 1, and TV is continuous in the parameters on the compact admissible set, so the bound extends.
F is convex in (r_0, r_1) and even, so (★) holds on the whole box iff it holds at the two vertex types (ρ_0, ρ_1) and (ρ_0, −ρ_1).

## Lemma 5 (vertex inequalities for |η| ≤ ½)
If |η| ≤ ½, (★) holds for every (u, v) ∈ [0,1]² and every (r_0, r_1) in the box.
*Proof.* F increases with η², so take η² = ¼. Four regions:
(i) u, v ≤ ½ (ρ_0 = 2v, ρ_1 = 2u): vertex 1: 4uv + (u−v)² = s²; vertex 2: 0 + (u+v)² = s². Equality.
(ii) u ≤ ½ < v (ρ_0 = 2(1−v), ρ_1 = 2u): vertex 1: 2u + (s−1)² ≤ s² ⇔ v ≥ ½; vertex 2: 2u(2v−1) + (1−v+u)² ≤ s² ⇔ 2u(2v−1) ≤ (2v−1)(2u+1), true.
(iii) v ≤ ½ < u: symmetric to (ii) (F is symmetric under (r_0,u) ↔ (r_1,v)).
(iv) u, v > ½ (ρ_0 = 2(1−v), ρ_1 = 2(1−u)): vertex 1: 2s − 4uv + (v−u)² ≤ s² ⇔ s ≤ 4uv, and 4uv − u − v = (2u−1)(2v−1) + u + v − 1 ≥ 0; vertex 2: 2|u−v| + (2−s)² ≤ s² ⇔ |u−v| ≤ 2(u+v−1), true for u, v ≥ ½. ∎

## Lemma 6 (size of η)
(a) K = 1: γ = 1, η = c < ½.
(b) K ≥ 2, σ ≥ 0: 0 ≤ η ≤ c, since γs = σ^{K−1} − σ^K ≤ 1 − σ^K = 1 − γσ.
(c) K ≥ 2, σ = −τ < 0, τ ≤ ½: |η| ≤ c, since (1+τ)τ^{K−1} ≤ |1 − (−τ)^K| (even K: τ^{K−1} + 2τ^K ≤ 1 holds for τ ≤ ½; odd K: trivial).
(d) K ≥ 2, σ = −τ with τ > ½: then s = 1+τ > 3/2 forces u, v ≥ τ > ½ (region (iv)), and |η|(ρ_0+ρ_1) = 2c(1−τ²)τ^{K−1}/|1−(−τ)^K| ≤ 2cτ (since (1−τ²)τ^{K−2} ≤ 1 ∓ τ^K).

## Theorem 3 (two-state hidden-phase optimum)
For every period K ≥ 1, every c ∈ (0, ½) and every irreducible 2-state time-homogeneous automaton as above, TV ≤ 2c/K. Hence the optimal asymptotic error is **½ − c/K** = ½ − (p_1 − p_0)/(2K) and is attained by the memoryless last-signal automaton; no 2-state automaton can use persistence to avoid the 1/K dilution.
*Proof.* Cases (a)–(c): |η| ≤ ½, so (★) holds by Lemma 5. Case (d): |r_0u + r_1v| ≤ ρ_0u + ρ_1v = 2s − 4uv ≤ 2(1+τ) − 4τ = 2 − 2τ (u, v ∈ [τ,1] gives uv ≥ τ), and η²(r_1−r_0)² ≤ η²(ρ_0+ρ_1)² ≤ 4c²τ² ≤ τ²; so F ≤ 2 − 2τ + τ² ≤ (1+τ)² = s² because 4τ ≥ 1. Thus (★) holds in all cases, so |R(x̂₀)| ≤ s and TV ≤ 2c/K by Lemma 2; Proposition 4 gives equality. ∎
**Remarks.** (1) For K = 1 this independently proves the two-state case of the Hellman–Cover optimum 1/(1+λ), λ = p_1/(1−p_1) (the known statement is cited from Leung 2020's restatement; the original paper was not accessible). (2) The proof does not characterise the set of optimal automata; the memoryless last-signal automaton attains the bound. (3) The result is for two memory states: for m ≥ 3 stochastic searches found errors slightly *below* the random-phase dilution value (K = 2: 0.334 vs 0.3378; K = 3: 0.3894 vs 0.3902 at λ = 2), suggesting persistence can be exploited with three states, but those searches did not converge reliably (a repeat for K = 1, m = 3 returned 0.2612 against the Hellman–Cover 0.2) and **no claim is made for m ≥ 3**.

## Numerical checks (O; none is part of the proof)
* Lemma 2 identity: max error 1.8×10⁻¹⁵ over 2×10⁵ random parameters (`scripts/embedded_m2_identity_check.py`).
* Lemma 3: max error 3.9×10⁻¹⁶ over 2×10⁵ random parameters, K ≥ 2 (`scripts/embedded_m2_lemma4_check.py`).
* Global search over the four-parameter family (24 cells: p_1 ∈ {0.6, 2/3, 0.75, 0.9}, K ∈ {1,2,3,4,6,10}): sup TV = 2c/K to within 2×10⁻¹⁵, never above (`scripts/embedded_m2_exact.py`).
* Independent stochastic optimisation of the full automaton, including action probabilities (K ≤ 5, λ ∈ {1.5, 2, 3}): identical optima (`results/embedded/m2_scaling_check.json`).
* Vertex inequality (`scripts/embedded_m2_vertex_check.py`) over a 201 × 201 grid in (u, v), K = 1…40 and three values of c: minimum margin s² − F = 0 (equality), never negative.
