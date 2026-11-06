# Joint memory–period growth: a nonasymptotic error bound

**2026-11-05. Status:** proved nonasymptotic bound for the reflecting-walk observer; novelty unverified. This tightens the scope of `arbitrary-memory-rare-phase-asymptotics.md` and does **not** solve the critical K≈m² regime.

## Model and exact identity

Use the binary hidden-phase model and m-state reflecting-walk observer of `arbitrary-memory-rare-phase-asymptotics.md`, m≥2, 0<c<1/2, K≥2. Let B be the fair-signal transition, D=T(1)−T(0), π the uniform stationary row, Π=1π, Z=(I−B+Π)^{-1}, and v_± the phase-start stationary rows under A_±=B±cD. The exact identity is

μ_+−μ_−=(c/K)(v_++v_−)DZ.

Write w=πDZ, w_i=(2/m)(2i−m+1), and L_m=∑|w_i|=m for even m and m−1/m for odd m.

## Theorem: uniform finite-(m,K,c) remainder

For all m≥2, K≥2 and 0<c<1/2,

[
\boxed{
\left|\operatorname{TV}_m(K,c)-\frac{cL_m}{K}\right|
\le \frac{2c\sqrt m}{K}\,
\frac{\rho_m^{K-1}}{1-\rho_m},
\qquad \rho_m=\cos(\pi/m).
}
]

**Proof.** Since B is symmetric and its eigenvalues are cos(jπ/m), j=0,…,m−1, its operator norm on the orthogonal complement of constants is ρ_m. The phase-start stationary rows obey v_h=(v_hA_h)B^{K−1}; hence, since v_hA_h is a probability row,

||v_h−π||_2 ≤ ρ_m^{K−1}||v_hA_h−π||_2 ≤ ρ_m^{K−1}.

The zero-sum subspace is invariant under D on the right because D1=0. The fundamental matrix Z has operator norm at most 1/(1−ρ_m) on the zero-sum subspace. Also ||D||_2≤2: each row and column of D has absolute sum at most 2, so ||D||_2≤√(||D||_1||D||_∞)≤2. Therefore

||(v_++v_−−2π)DZ||_1
≤√m · ||(v_++v_−−2π)DZ||_2
≤√m · 2ρ_m^{K−1} · 2/(1−ρ_m)
=4√m ρ_m^{K−1}/(1−ρ_m).

Using | ||a||_1−||b||_1 |≤||a−b||_1 and TV=(1/2)||μ_+−μ_−||_1 gives the displayed bound. ∎

## Corollary: a justified joint limit

Let m→∞ and K=K(m)≥2. If K/(m² log m)→∞, then uniformly for c∈(0,1/2),

[
\frac{\operatorname{TV}_m(K,c)}{cL_m/K}\longrightarrow1.
]

**Proof.** Since L_m≥m−1/m and 1−cos(π/m)~π²/(2m²), the relative error is bounded by

2√m ρ_m^{K−1}/[(1−ρ_m)L_m]
=O(m^{3/2} \exp[-(π²/2+o(1))K/m²]).

Under K/(m² log m)→∞, this tends to zero. The c factor cancels, so the bound is uniform over all c∈(0,1/2). ∎

This condition is **sufficient, not necessary**. The bound is too coarse to decide the crossover K≈m² or even the entire region K≫m².

## Verification and limitations

The Poisson solution w was checked with exact rational matrix arithmetic for m=2,…,8; in every case ∑|w_i| equals the parity formula. This is a mathematical consistency check, not an independent proof of the theorem.

The norm estimate is conservative; no claim of sharp constants or optimality among all m-state automata is made. In particular the relative 4/3 gain for m=3 and the linear-in-m coefficient for fixed m are consistent with this theorem. The large-m, K≈m² diffusion crossover remains open.

## Next problem: critical scaling

Seek an exact spectral expansion for v_h and μ_h with m-dependent mode coefficients, then analyze K/m²→α∈(0,∞). The expected continuum object is a reflected diffusion with a localized informative transition; **this is a conjectural direction, not an established limit**. Check classical perturbation theory for finite Markov chains, reflected random-walk spectral asymptotics, and finite-memory hypothesis testing before making novelty claims.

**Verdict: CONTINUE.** The joint-limit sufficient regime is proved; the critical scaling and optimal finite-memory discrimination remain unresolved.
