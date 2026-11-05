# Sharp Poisson-response operator norm for the reflecting-walk observer

**2026-11-05. Status:** exact algebraic norm identity and improved finite-size discrimination bound. The adjective *sharp* applies to the matrix norm, **not** to the achievable discrimination or to all possible observers. Novelty not established.

## Setup

For the m-state reflecting-walk observer from `arbitrary-memory-rare-phase-asymptotics.md`, m≥2, let B be the fair Bernoulli transition, D=∂T(p)/∂p, π uniform, Π=1π and Z=(I−B+Π)^{-1}. The exact phase-average response identity gives

μ_+−μ_−=(c/K)(v_++v_−)DZ,

where v_± are probability rows. Thus TV≤(c/K)max_i ||(DZ)_{i,:}||_1. We compute this maximum **exactly**.

## Lemma: exact rows of DZ

For a test vector f with ||f||∞≤1, put g=Zf and f̄=m^{-1}∑f_j. The Poisson equation (I−B)g=f−f̄1 gives the discrete gradient

g_{j+1}−g_j=−2[∑_{r=0}^j f_r−(j+1)f̄],  0≤j≤m−2.

At the left endpoint (Dg)_0=g_1−g_0; at the right endpoint (Dg)_{m−1}=g_{m−1}−g_{m−2}; at an interior index 1≤i≤m−2, (Dg)_i=g_{i+1}−g_{i−1}. Therefore, writing R=DZ,

R_{0,j}=−2(1_{j=0}−1/m),

R_{m−1,j}=−2(1_{j≤m−2}−(m−1)/m),

and for 1≤i≤m−2,

[
R_{i,j}=-2\left[\mathbf1_{j\le i-1}+\mathbf1_{j\le i}-\frac{2i+1}{m}\right].
]

Consequently the endpoint row l1 norms equal 4(m−1)/m. The interior row l1 norm is

[
r_i=i\left(4-\frac{2(2i+1)}m\right)
+2\left|1-\frac{2i+1}m\right|
+(m-i-1)\frac{2(2i+1)}m.
]

**Exact maximum:**

[
\boxed{\max_{0\le i\le m-1}r_i=2(m-1).}
]

To verify the maximum algebraically, split at 2i+1=m. For 2i+1≤m, simplify r_i to 4(2i+1)(m-i-1)/m; for 2i+1≥m, simplify to 4i(2m-2i-1)/m. Each expression is a concave quadratic in i, increasing toward the central index and decreasing afterward. The center gives 2(m−1) (for even m, the two central indices; for odd m, the single central index). The endpoint formula also respects the maximum, including m=2.

This is the induced matrix norm ||DZ||_{∞→∞}=2(m−1), equivalently the largest row l1 norm.

## Theorem: improved finite-size TV upper bound

For all integers m≥2, K≥2 and c∈(0,1/2),

[
\boxed{\operatorname{TV}_m(K,c)\le
\min\left\{1,\frac{2c(m-1)}K\right\}.}
]

**Proof.** Since v_++v_− is a nonnegative row of total mass 2, its product with R is a positive combination of R's rows with coefficients summing to 2. Thus

|| (v_++v_−)R ||_1≤2 max_i||R_{i,:}||_1=4(m−1).

The exact response identity and the factor 1/2 in total variation yield TV≤(c/(2K))·4(m−1)=2c(m−1)/K. Also TV≤1. ∎

This improves the prior coarse 4cm/K bound by nearly a factor of two. It proves TV→0 whenever m/K→0, including K≈αm². It **does not** by itself close the intermediate K≈m regime.

## Independent arithmetic check

Directly form B, D and Z using floating-point linear algebra for each m=2,…,12, and compute the row l1 norms of DZ. The maxima were, respectively,

m=2: 2; m=3: 4; m=4: 6; m=5: 8; m=6: 10; m=7: 12; m=8: 14; m=9: 16; m=10: 18; m=11: 20; m=12: 22,

matching 2(m−1) to floating-point tolerance. This check supplements, but does not replace, the exact row formula and algebraic proof.

## Scope and next research

The norm identity is sharp for arbitrary row-probability mixtures, but the phase-start distributions v_± are constrained by the periodic stationary dynamics. Therefore the TV bound need not be attained by this observer. Nor is it an upper bound over *all* m-state automata. Classical Green-function/Poisson-equation identities may already contain this result; **novelty unverified**.

A promising next target is the m,K→∞ window K/m→α>0, where a continuum reflected-drift approximation could potentially yield a nontrivial scaling function. The current norm bound only supplies TV≤min(1,2c/α) in that regime, and the earlier Lyapunov estimate does not prove a matching lower bound.
