# Monotone likelihood ratio and single crossing for the reflecting-walk observer: **PROVED**

**2026-11-05/06. Status:** complete proofs below (checked numerically in float and in exact rational arithmetic; not externally reviewed). **Verdicts: MLR — PROVED. Single crossing — PROVED (strict).** Novelty: *not established*; the mechanism (a cone of monotone mass functions invariant under the kernels) is elementary and probably known in the spirit of monotone/unimodality-preserving Markov chains (Keilson–Kester 1977, 1978; originals not accessed). Code: `scripts/mlr_*.py`; results: `results/mlr/`.

## Model (independently reconstructed from the transition matrices)
m ≥ 2 memory states. Kernel A_p on {0,…,m−1}: up with probability p to min(i+1, m−1), down with probability 1−p to max(i−1, 0). Fair step B = A_{1/2}. Period K ≥ 1; phase 0 is informative with up-probability p_h = ½ ± c (h = ±), 0 < c < ½; phases 1,…,K−1 use B. Write p = ½ + c, q = ½ − c. The periodic stationary law at the start of phase 0 is the unique ν_{h,0} with ν_{h,0} = ν_{h,0} A_{p_h} B^{K−1}; ν_{h,j} are its successive images; μ_h = K⁻¹ Σ_j ν_{h,j}. (Convention: step-start laws; the end-of-step convention gives the same average.) Existence/uniqueness: the one-period kernel is irreducible and aperiodic (strictly positive transition probabilities along reflecting self-loops), so ν_{h,0} = lim_n v₀ (A B^{K−1})ⁿ for any initial law v₀.

## Lemma 1 (mirror symmetry)
With J(i) = m−1−i: ν_{−,j}(i) = ν_{+,j}(m−1−i) for every phase j, hence μ_−(i) = μ_+(m−1−i).
*Proof.* If X is the − chain, Y = m−1−X moves up exactly when X moves down; with reflecting boundaries mapped to reflecting boundaries, Y uses kernel A_{1−(½−c)} = A_p at the informative phase and B elsewhere, i.e. the + kernels. Uniqueness of the periodic stationary law gives ν_{−,j} = Jν_{+,j}. ∎

## Lemma 2 (cone invariance)
Let 𝒞 = {v ∈ ℝ^m_{≥0} : v(0) ≤ v(1) ≤ … ≤ v(m−1)}. For every p ∈ [½, 1), v ∈ 𝒞 ⇒ vA_p ∈ 𝒞. More precisely, with d_k = v(k+1) − v(k) ≥ 0 and w = vA_p, d′_k = w(k+1) − w(k):
 interior (1 ≤ k ≤ m−3): d′_k = p d_{k−1} + q d_{k+1};
 d′_0 = (p−q) v(0) + q d_1; d′_{m−2} = p d_{m−3} + (p−q) v(m−1) (m ≥ 3); for m = 2, d′_0 = (p−q)(v(0)+v(1)). Here q = 1−p.
*Proof.* (vA_p)(0) = q(v(0)+v(1)); (vA_p)(j) = p v(j−1) + q v(j+1) for 1 ≤ j ≤ m−2; (vA_p)(m−1) = p(v(m−2)+v(m−1)). Subtract consecutive entries. All terms are ≥ 0 because d_k ≥ 0, v ≥ 0 and p ≥ q. ∎ (For p = ½ this is the statement for B: d′_k = ½(d_{k−1} + d_{k+1}) with the convention d_{−1} = d_{m−1} = 0.)

## Theorem 1 (monotone mass functions)
For all m ≥ 2, K ≥ 1, 0 < c < ½, every phase law ν_{+,j} is nondecreasing in i, and the phase-average μ_+ is **strictly increasing**: μ_+(i+1) > μ_+(i) for all i.
*Proof of monotonicity.* The uniform law lies in 𝒞; by Lemma 2 each factor of AB^{K−1} preserves 𝒞, so v₀(AB^{K−1})ⁿ ∈ 𝒞 for all n; 𝒞 is closed, so the limit ν_{+,0} ∈ 𝒞; images under A, B stay in 𝒞. Averages stay in 𝒞.
*Proof of strictness.* Let d_k(j) be the increments of ν_{+,j}; all are ≥ 0. Suppose μ_+(i+1) = μ_+(i). Then d_i(j) = 0 for every phase j (increments are ≥ 0 and average to 0). Let Z_j be the set of k with d_k(j) = 0. By Lemma 2, if k ∈ Z_{j+1} then (interior) both d_{k−1}(j) = 0 and d_{k+1}(j) = 0, i.e. k±1 ∈ Z_j (for a fair step with the convention d_{−1} = d_{m−1} = 0); and after the informative step d′_0 ≥ (p−q)ν_j(0) > 0 and d′_{m−2} ≥ (p−q)ν_j(m−1) > 0, so 0, m−2 ∉ Z_{j+1} there (ν_j(0), ν_j(m−1) > 0 as stationary laws of an irreducible chain). Since i ∈ Z_j for all j, induction on t gives [i−t, i+t] ∩ [0, m−2] ⊆ Z_j for all j and t. For t ≥ m this contains the index 0 at the phase immediately after the informative step, contradicting d′_0 > 0. ∎

## Theorem 2 (MLR and single crossing)
For all m ≥ 2, K ≥ 1, 0 < c < ½ and 0 ≤ i ≤ m−2:
 (a) **MLR (strict):** μ_+(i+1)/μ_−(i+1) > μ_+(i)/μ_−(i), equivalently μ_+(i+1)μ_−(i) − μ_+(i)μ_−(i+1) > 0. The same holds, weakly (≥), at every phase for ν_{±,j}.
 (b) **Single crossing:** Δ_i = μ_+(i) − μ_−(i) satisfies Δ_i < 0 for i < (m−1)/2, Δ_i > 0 for i > (m−1)/2 and Δ_{(m−1)/2} = 0 if m is odd: exactly one sign change.
 (c) **Threshold optimality and absolute values removed:** the equal-prior Bayes rule "guess + iff M ≥ ⌈m/2⌉" (ties at the middle state are immaterial) is optimal, and
 TV(μ_+, μ_−) = 2 μ_+{M ≥ m/2} − 1 (m even), TV = μ_+{M > (m−1)/2} − μ_+{M < (m−1)/2} (m odd).
*Proof.* (a) By Lemma 1, ρ(i) := μ_+(i)/μ_−(i) = μ_+(i)/μ_+(m−1−i). The numerator is strictly increasing in i (Theorem 1) and the denominator μ_+(m−1−i) is strictly decreasing in i, so ρ is strictly increasing; the cross-product equals μ_−(i)μ_−(i+1)(ρ(i+1) − ρ(i)) > 0. The phasewise statement is identical using the weak monotonicity of ν_{+,j} (ties occur and are exact; see below). (b) Δ_i = μ_+(i) − μ_+(m−1−i) is negative when i < m−1−i because μ_+ is increasing, positive when i > m−1−i, zero at i = (m−1)/2. (c) The Bayes rule decides + exactly where Δ_i > 0, i.e. above the midpoint; (c) follows by summing Δ_i over that set and using μ_−(i) = μ_+(m−1−i). ∎
**Remarks.** (1) The proof uses only: p_t ≥ ½ at every step, mirror symmetry of the two hypotheses, and reflecting boundaries; it holds for any periodic schedule of kernels A_{p_t} with p_t ≥ ½ (any number of informative phases). (2) Phasewise ties are real: for even K the phase laws have exactly equal consecutive masses at alternating positions (a parity effect of the bipartite walk), so phasewise MLR holds with equalities, while the phase average is strict. Exact rational data: e.g. m = 10, K = 2, c = 49/100 has cross-products exactly 0 at alternating indices. (3) First-order stochastic dominance (the previous note) is strictly weaker than Theorem 1; the new ingredient is the invariant cone of nondecreasing *mass functions*. (4) The kernels are **not** TP2 (the interior walk has zero holding: the 2×2 minor P(i,i)P(i+1,i+1) − P(i,i+1)P(i+1,i) = −¼ < 0), so classical total-positivity preservation of likelihood-ratio order does not apply; the cone argument is a different mechanism.

## Verification (O)
* Cone invariance: 2×10⁵ random nondecreasing vectors (m = 2…12, p ∈ [½, 1)) mapped by A_p and B: minimum increment 0.0, never negative (`scripts/mlr_proof_check.py`).
* Exact Fraction arithmetic: 175 (m ≤ 8, K ∈ {2,3,4,5,7}, c ∈ {1/100, 1/10, 1/4, 2/5, 49/100}) cases: every phase law nondecreasing, mirror symmetry exact, 0 violations (`results/mlr/proof_check.json`).
* Float scan m ≤ 14, K ≤ 60, c from 10⁻³ to 0.499: minimum relative cross-product 1.3×10⁻⁴ > 0; no MLR violation.
* Absolute-value-free formula for TV agrees with ½‖μ_+ − μ_−‖₁ to 1.5×10⁻¹⁴ (m ≤ 24; `results/mlr/tv_formula_check.json`).
* Apparent phasewise violations of size ≈ −10⁻¹⁰ in a float scan were rounding noise: in exact arithmetic the corresponding cross-products are exactly 0 or positive.

## Corollaries and what changes in earlier notes
The cofactor representation of TV_m(2,c) in `arbitrary-memory-k2-cofactor-formula.md` may now drop its absolute values (Theorem 2c). The statement in `all-memory-stochastic-dominance.md` that MLR/single crossing were unproved is superseded. Nothing else in the earlier notes depends on single crossing.
