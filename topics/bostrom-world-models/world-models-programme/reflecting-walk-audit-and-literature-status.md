# Reflecting-walk programme: independent audit, corrections and literature status

**2026-11-06.** Phase 1 (verification) and Phase 5 (literature, classification) of the MLR investigation. Companion notes: `mlr-and-single-crossing-theorem.md`, `memory-hierarchy-and-walk-nonoptimality.md`.

## 1. Independent reconstruction and audit
`scripts/mlr_model.py` rebuilds the model from transition matrices (reflecting walk on {0..m−1}; informative phase up-probability ½ ± c; phase laws ν_{h,j} = law at the start of phase j; μ_h = K⁻¹ Σ_j ν_{h,j}); stationary laws by linear least squares in float and, in `scripts/mlr_exact.py`, by exact Gauss–Jordan elimination over ℚ. Phase-averaging convention: step-start laws; the end-of-step convention is the same cyclic average.
Audit of the repository's claimed results against this independent model:
| claim (note) | independent check | result |
|---|---|---|
| TV_4(K,c) = 4c/K, all K ≥ 2 (`exact-four-state-all-period-theorem`) | K ∈ {2,3,5,8,13}, c = 0.2 | holds to 10⁻¹⁰ |
| TV_2 = 2c/K (my two-state theorem) | K ∈ {1,2,3,5,8} | holds exactly |
| TV_5(2,c) = 4c(4c²+15)/(16c⁴+24c²+25); TV_6 = c(9−4c²)/(3+4c²); TV_7 = 8c(16c⁴−48c²−21)/F(c); TV_8 = 4c/(1+4c²) (`exact-five-six`, `exact-seven-eight`) | c ∈ {0.05, 0.17, 1/6, 0.3, 0.45} | all agree to 9 digits |
| TV_3(K,c) all-period formula (`all-period-three-state-separation-theorem`) | K = 2…19, c ∈ {0.03, 0.17, 0.33, 0.48} | max error 4×10⁻¹⁶ |
| Poisson-response bound TV ≤ 2c(m−1)/K (`sharp-poisson-response-norm`) | m ≤ 11, K ∈ {2,3,5,9,17}, c up to 0.49 | holds; maximum ratio TV·K/(2c(m−1)) = 1.0000 (attained at m = 2) |
| stochastic dominance of phase laws (`all-memory-stochastic-dominance`) | implied by Theorem 1 (monotone mass functions) | consistent |
**No algebraic error found in any of these formulas.** Boundary cases: m = 2 (B maps every law to the uniform law; the phase average is still strict), c → 0 (all laws → uniform, MLR margin ∝ c), c → ½ (ratios blow up but stay ordered). The proofs of the exact formulas were not re-derived symbolically here (only the formulas were checked against the independent model); the mechanisms (matrix identities, cofactor expansions) were not audited line by line.

## 2. Corrections and updated dependencies
1. **"Single crossing / MLR unproved"** (stochastic-dominance note, cofactor note): now proved (strict). The cofactor note's absolute values may be removed (TV = Σ_{i>(m−1)/2} Δ_i; Theorem 2c).
2. **Optimality of the walk**: nothing in the repository claimed it, but the framing "hierarchy of observers" invited it; it is **false** (exact certificate, `memory-hierarchy-and-walk-nonoptimality.md` §B). All TV_m results describe the walk, not the best m-state observer; any statement about *optimal* m-state discrimination (e.g. about removing the logarithmic gap in joint m, K scaling) must be restated for the walk or reproved for the optimum.
3. Float scans can mislead on exact ties: phasewise cross-products of order −10⁻¹⁰ near c = 0.49 were rounding; exact arithmetic shows exact zeros (parity ties) or positive values.

## 3. Literature (Phase 5) — access levels: **E** read in extracted full text earlier in this programme; **F** fetched page/summary; **S** search summary only; **N** not accessed
| topic | source | what it provides | access | relation to our results |
|---|---|---|---|---|
| finite-memory hypothesis testing | Hellman & Cover, *Learning with finite memory*, Ann. Math. Stat. 41 (1970) 765–782; Cover (1969); restated in Leung, arXiv:2009.11917 (E) | m-state time-invariant automata: optimal asymptotic error 1/(1+λ^{m−1}) for two simple hypotheses; sticky/persistent optimal automata; time-varying automata can reach 0 | originals N; restatement E | the sticky 3-state certificate is a hidden-phase instance of their mechanism; reflecting walk is far from their optimal automaton |
| monotone/stochastically monotone Markov chains | Keilson & Kester, *Monotone matrices and monotone Markov processes*, SPA 5 (1977) 231–241, DOI 10.1016/0304-4149(77)90033-3; *Unimodality preservation in Markov chains*, SPA 7 (1978) 179–190 | monotone stochastic matrices (rows stochastically increasing); unimodality preservation and the variation-diminishing (TP2) property | S (bibliographic/abstract level) | our cone-invariance lemma is of the same family (preservation of monotone/unimodal shapes under Markov kernels) but concerns **mass functions under v ↦ vP**, and the kernels are not TP2; whether the lemma is a corollary is **unverified** |
| total positivity | Karlin, *Total Positivity* (1968) | TP2 kernels preserve likelihood-ratio order | N | does not apply: interior walk kernel has negative 2×2 minor −¼ (bipartite) |
| stochastic orders | Shaked & Shanthikumar, *Stochastic Orders* (2007) | likelihood-ratio order, preservation under kernels | N | context for Theorem 2 |
| birth–death chains, monotone kernels | monotone BD kernel preserves increasing functions (lemma in arXiv:0801.2625, cutoff note) | S | | same circle of ideas; distinct statement |
| Poisson equation | Glynn & Meyn (1996); Meyn & Tweedie | Lyapunov bounds for Poisson equation solutions | N | the repository's Poisson-response norm identity is a finite-state exact version; not re-derived |
| reflected walks | M/M/1/K-type stationary laws (Asmussen, *Applied Probability and Queues*) | geometric stationary law of the reflecting chain with constant drift | N | K = 1 case of our model (geometric law ⇒ MLR) |
| periodic chains | standard (Kemeny–Snell; Meyn–Tweedie) | cyclic structure, convergence of the period kernel | N | used in the definition of ν_{h,j} |
**Classification.**
1. *Established (prior literature)*: Hellman–Cover finite-memory floor and sticky optimal automata; stochastic monotonicity of birth–death chains; TP2 preservation of LR order; geometric stationary laws of constant-drift reflected walks.
2. *Independently reproduced here*: two-state 1/K dilution (my Theorem 3; contains the m = 2 K = 1 Hellman–Cover value); all exact 3–8-state formulas of the repository; the Poisson-norm bound.
3. *Potentially original (novelty unverified, probably elementary)*: Theorem 1 (strictly increasing phase-averaged mass function; monotone-cone invariance for any p_t ≥ ½ schedule), Theorem 2 (strict MLR and single crossing for the walk, all m, K, c); the K = 2 even-m product-form law and TV_{4L} = tanh(L·artanh 2c); the K = 2 even-memory hierarchy (Theorem A3); the exact rational non-optimality certificate.
4. *Open conjectures*: strict monotonicity of TV_m in m for all K, c (verified numerically m ≤ 40); closed forms for odd m at K = 2; the exact optimum TV*(m,K,c); the K/m → α limit; whether sticky automata under hidden phase achieve a Hellman–Cover-type exponent with a K-dependent dilution.
5. *Disproved*: "the reflecting-walk observer is optimal among m-state observers" (exact certificate, m = 3, K ∈ {2,3}); the earlier worry that single crossing might fail for the walk (it holds, strictly).
Novelty is not asserted: a result's absence from the sources I could access is not evidence of originality.
