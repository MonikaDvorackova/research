# Memory-size hierarchy and (non-)optimality of the reflecting-walk observer

**2026-11-06. Status:** (A) closed forms and a proved strict hierarchy for K = 2 and even m; (B) an **exact rational disproof** that the reflecting walk is optimal among m-state clockless observers; (C) open questions. Code and certificates: `scripts/mlr_k2_*.py`, `scripts/mlr_counterexample_certificate.py`, `scripts/mlr_optimality_search_floored.py`; results in `results/mlr/`. Not externally reviewed.

## A. K = 2, even m: product-form law and closed forms (proved)
Let r = (½+c)/(½−c) = p/q, so rq = p, and m = 2M.
**Lemma A1.** The phase-0 (entry) law of the + chain is ν_{+,0}(i) = C r^{⌊i/2⌋} with C = (r−1)/(2(r^M−1)), and ν_{+,1}(i) = 2Cp r^{⌈i/2⌉−1}.
*Proof.* Direct verification of ν_{+,0} A_p B = ν_{+,0}: with a(i) = C r^{⌊i/2⌋}, (aA_p)(0) = 2Cq = 2Cp/r; (aA_p)(2k) = p C r^{k−1} + q C r^k = 2pC r^{k−1} (k ≥ 1); (aA_p)(2k+1) = pC r^k + qC r^{k+1} = 2pC r^k; top: (aA_p)(m−1) = 2pC r^{M−1}; i.e. ν_{+,1}(i) = 2Cp r^{⌈i/2⌉−1}. Applying B: (ν_{+,1}B)(0) = Cp(1+1/r) = C (since p(r+1)/r = 1), (ν_{+,1}B)(2k+1) = Cp r^{k−1}(1+r) = C r^k, because p(1+r) = p/q = r; the even and top indices work the same way; so ν_{+,0} is stationary. Normalisation Σ a = 2C Σ_{k<M} r^k = 1. ∎
Averaging, μ_+(i) = (C/2)[r^{⌊i/2⌋} + 2p r^{⌈i/2⌉−1}], i.e. f(2k) = r^{k−1}(r+2p), f(2k+1) = r^k(1+2p). Successive ratios alternate between α = r(1+2p)/(r+2p) > 1 and β = (r+2p)/(1+2p) > 1: μ_+ is strictly increasing (consistent with Theorem 1 of `mlr-and-single-crossing-theorem.md`).
**Theorem A2 (closed forms; proved).** With L ≥ 1: TV_{4L}(2,c) = (r^L − 1)/(r^L + 1) = **tanh(L·artanh(2c))**. For m = 4L+2, with S_n = Σ_{k<n} r^k:
 TV_{4L+2}(2,c) = 1 − [4S_L + r^{L−1}(r + 2p)] / (2 S_{2L+1}), S_{2L+1} = S_L(1 + r^L) + r^{2L}.
*Proof.* Theorem 2c of the MLR note (TV = 1 − 2μ_+{M < m/2}), the formula for μ_+ above and the identity p(1 + 1/r) = 1 (each pair of states contributes 4 r^k to Σ f). ∎ Checks: L = 1 gives TV_4 = 2c; L = 2 gives TV_8 = 4c/(1+4c²); the m = 6 formula equals the repository's c(9−4c²)/(3+4c²) symbolically; TV_{10} = c(16c⁴+24c²+25)/(16c⁴+40c²+5); numerical agreement with the independent model to 4×10⁻¹⁴ for all even m ≤ 40.
**Theorem A3 (K = 2 even-memory hierarchy; proved).** With x = r^L ≥ r > 1:
 TV_{4L+2} − TV_{4L} = x(r−1)(3rx − r + x − 3) / [2(r+1)(x+1)(rx²−1)] > 0,
 TV_{4L+4} − TV_{4L+2} = x(r−1)(r²x + 3rx − 3r − 1) / [2(r+1)(rx+1)(rx²−1)] > 0.
*Proof.* Symbolic simplification (SymPy, `scripts/mlr_k2_hierarchy_symbolic.py`); positivity: 3rx − r + x − 3 > 4x − 4 > 0 and r²x + 3rx − 3r − 1 > 3r(x−1) + r²x − 1 > 0 for r > 1, x ≥ r. ∎ So TV_4 < TV_6 < TV_8 < TV_10 < … for K = 2 and all c, and TV_m → 1 geometrically as m → ∞ along even m (error of order r^{−m/4}). **Odd m (K = 2): no product form found; the hierarchy through odd m is not proved.**

## B. The reflecting walk is **not** optimal among m-state clockless observers (disproved; exact certificate)
Claim tested: among all m-state, time-homogeneous, irreducible stochastic observers (memory transitions T(i,y,·), probe probability q_i), the reflecting walk maximises TV(μ_+, μ_−).
**Counterexample (m = 3, rational).** Sticky decision automaton S(ε, ℓ), always probe: state 0: y=0 → (ε, 1−2ε, ε), y=1 → (ε, ε, 1−2ε); state 1: y=0 → (ε, 1−2ε, ε), y=1 → (ℓ, 1−ℓ−ε, ε); state 2: y=0 → (ℓ, ε, 1−ℓ−ε), y=1 → (ε, ε, 1−2ε) (rows list probabilities of next states 0,1,2). With ε = 1/10000, ℓ = 1/30, exact Fraction arithmetic gives
| K, c | reflecting-walk TV | S(ε,ℓ) TV | ratio |
|---|---|---|---|
| 2, 1/5 | 0.271493 | 0.388064 | 1.429 |
| 2, 2/5 | 0.574163 | 0.779107 | 1.357 |
| 3, 3/10 | 0.265152 | 0.387557 | 1.462 |
| 2, 1/20 | 0.066741 | 0.096900 | 1.452 |
(`results/mlr/optimality_counterexample_certificate.json` stores the exact fractions.) Random-restart optimisation with a probability floor also found 4-state automata beating the 4-state walk (K = 2, c = 0.2: 0.4677 vs 0.4; K = 3, c = 0.3: 0.5074 vs 0.4) — not yet certified in exact arithmetic.
**Mechanism.** State 0 re-decides from one signal; states 1 and 2 are nearly absorbing (Hellman–Cover-style persistence) with rare leaks back. This is the m = 3 analogue of the sticky optimal automaton of finite-memory testing, and it exploits what the reflecting walk cannot: persistence of the decision across the uninformative phases.
**Consequences.** All "TV_m" results in the repository (exact 3–8-state formulas, hierarchies, Poisson-norm bounds, asymptotic regimes for the walk) are statements about the *walk observer*, not about optimal m-state observers; none of them gives a lower bound on the optimal TV that is tight. The two-state optimality theorem (Theorem 3 of `proof-note-two-state-hidden-phase.md`) is unaffected (it covers all 2-state automata). Which of the "log-gap" and "K/m → α" questions are meaningful for the true optimum is open.

## C. Numerical checks of the hierarchy for the walk (not proofs)
TV_m(K,c) is strictly increasing in m for m = 2…40 at K ∈ {2,3,4,5,7,10,20,50} and c ∈ {0.01,…,0.49}: no violation, minimum relative increment positive up to rounding (`results/mlr/hierarchy_optimality_search.json`). Monotonicity in m for all (K,c,m) is **open** (proved: K = 2 even m; m ≤ 8 at K = 2 by the repository's exact formulas).

## D. Open questions
1. Strict monotonicity of TV_m in m for the walk, all K, c (odd m at K = 2 included).
2. The exact optimum TV*(m, K, c) over all m-state automata; whether sticky automata achieve the Hellman–Cover-type exponent 1/(1+λ^{m−1}) under hidden phase (K ≥ 2) with a K-dependent dilution, and how the optimal m scales with K.
3. For the walk: the regime K/m → α (a reflected-drift scaling limit).
