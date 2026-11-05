# Exact discrete gradient and the joint memory–period crossover

**Status: 2026-11-05.** A new exact edge-flux identity, an elementary proof of strict single crossing, and a proposed complete asymptotic crossover theorem for the reflecting-walk observer. The diffusion-scale tightness argument below uses a standard reflected-walk maximal-displacement estimate; this lemma and its applicability to the clipped two-boundary walk should be checked independently before treating the crossover theorem as externally validated. Novelty not established.

## Setup

For m≥2, K≥2, 0<c<1/2, let B be the reflecting fair-walk row transition, D=∂_p T(p), and A_h=B+hcD for h=±1. Let v_h be the unique phase-0 stationary row vector, v_h=v_h A_h B^{K−1}. The phase-average memory law is μ_h=K^{-1}∑_{t=0}^{K−1}v_h A_h B^{t−1}, with t=0 interpreted as v_h. Reflection gives μ_−(i)=μ_+(m−1−i).

## Theorem 1: exact edge-flux identity

For every i=0,…,m−2,

\[
\boxed{\mu_h(i+1)-\mu_h(i)=\frac{2hc}{K}\big(v_h(i)+v_h(i+1)\big).}
\]

In particular μ_+ is strictly increasing, μ_− strictly decreasing, and the equal-prior optimal decision threshold is the midpoint. This is a shorter, direct proof of the phase-averaged part of the earlier MLR/single-crossing theorem; it does not by itself establish phasewise MLR.

### Proof

Phase averaging and the periodic stationary relation give

\[
\mu_h=\mu_h B+\frac{hc}{K}v_hD.
\]

Indeed each of the K fair-step contributions telescopes around the period, with one correction A_h−B=hcD. For any row law a, the signed edge current of the fair walk across (i,i+1) is (a_i−a_{i+1})/2. For the perturbation v_hD, the rightward signed edge current is v_h(i)+v_h(i+1), because D adds a right move and subtracts a left move at each state, including reflected boundary states. The stationarity equation says that the sum of these two currents has zero divergence. The left endpoint has zero external current, hence the current across every interior edge is zero:

\[
\frac{\mu_h(i)-\mu_h(i+1)}2+\frac{hc}{K}(v_h(i)+v_h(i+1))=0.
\]

This proves the identity. Every entry of v_h is positive by irreducibility. Reflection symmetry and strict monotonicity imply strict single crossing and MLR for the phase averages. ∎

## Corollary: uniform pointwise bound

Summing the edge identity for h=+ gives

\[
0<\mu_+(m−1)-\mu_+(0)
=\frac{2c}{K}\sum_{i=0}^{m−2}(v_i+v_{i+1})
\leq\frac{4c}{K}.
\]

Since the average of μ_+(i) is 1/m,

\[
\boxed{\max_i|\mu_+(i)-1/m|\leq4c/K.}
\]

This elementary bound prevents macroscopic boundary atoms when K/m→α>0.

## Theorem 2: crossover at K/m→α (proof strategy and result)

Fix c∈(0,1/2). Let m→∞ and K=K_m≥2 with K_m/m→α∈(0,∞). Embed μ_{+,m} into [0,1] by assigning mass μ_{+,m}(i) to i/m (or a cell of width 1/m). Then the limiting distribution is absolutely continuous with density

\[
\boxed{f_+(x)=\frac{a e^{ax}}{e^a-1},\qquad a=\frac{4c}{\alpha},\quad 0\leq x\leq1.}
\]

The negative-hypothesis limit is f_−(x)=f_+(1−x). Consequently, provided the displacement estimate detailed below is applied,

\[
\boxed{\lim_{m\to\infty,\ K_m/m\to\alpha}\mathrm{TV}_m(K_m,c)=\tanh(c/\alpha).}
\]

This identifies a nontrivial crossover function, closing the earlier logarithmic gap for the **specific reflecting-walk construction**. It is not an optimum over arbitrary finite-state automata.

### Proof

**Step 1 (compactness).** The exact edge identity implies μ_+ is increasing and 0≤mμ_+(i)≤1+4cm/K. For K/m→α, the histogram densities are uniformly bounded and monotone. Helly compactness therefore supplies a subsequential weak limit with bounded nondecreasing density f; no endpoint atoms are possible. The same applies to v if its weak limit can be identified.

**Step 2 (phase-start versus phase-average).** Let X_t be a reflecting walk started at X_0∼v_+, with one biased step followed by fair steps. For any 1-Lipschitz φ on [0,1],

\[
\left|\mathbb E\phi(X_t/m)-\mathbb E\phi(X_0/m)\right|
\leq\frac{\mathbb E|X_t-X_0|}{m}.
\]

A standard pathwise reflection estimate for a walk on [0,m−1] bounds its displacement by a constant times the maximal absolute partial sum of its ±1 increments, plus a constant for the one biased step. Doob's L² inequality for the centered fair increments yields \(\sup_{t\leq K}\mathbb E|X_t-X_0|\leq C(\sqrt K+1)\), uniformly in the starting state and m. Hence

\[
d_{\mathrm{BL}}(v_+,\mu_+)\leq C(\sqrt K+1)/m\longrightarrow0
\]

for K∼αm. Thus v_+ and μ_+ share every subsequential weak limit. (For a completely self-contained proof, expand the two-sided discrete Skorokhod reflection/maximal-displacement lemma; this is the remaining technical lemma to audit.)

**Step 3 (distributional equation).** For any smooth φ with compact support in (0,1), multiply

\[
\mu_+(i+1)-\mu_+(i)=\frac{2c}{K}(v_+(i)+v_+(i+1))
\]

by mφ(i/m), sum over i, and perform discrete summation by parts. The left side converges to \(-\int_0^1 f(x)\phi'(x)\,dx\). The right side converges to

\[
\frac{4c}{\alpha}\int_0^1 f(x)\phi(x)\,dx,
\]

using the common weak limit of v_+ and μ_+ and K/m→α. Therefore, distributionally,

\[
f'(x)=\frac{4c}{\alpha}f(x).
\]

The unique nonnegative normalized solution is f(x)=a e^{ax}/(e^a−1). Every subsequence has this limit, so the entire sequence converges weakly.

**Step 4 (TV convergence).** Theorem 1 gives exact single crossing for every finite m. Hence TV_m equals the signed difference of upper-half probabilities. The limiting densities are continuous and have no atom at x=1/2, so weak convergence suffices to pass these probabilities to the limit:

\[
\lim \mathrm{TV}_m
=\int_{1/2}^1(f_+(x)-f_-(x))\,dx
=\frac{e^{a/2}-1}{e^{a/2}+1}
=\tanh(a/4)=\tanh(c/\alpha).
\]

∎ subject to the explicitly flagged displacement lemma.

## Independent finite-size identity checks

Direct stationary solves with numpy for (m,K,c)=(5,3,0.2),(8,2,0.2),(12,7,0.1) give maximum absolute edge-identity residuals 6.25e−17, 3.12e−17, and 2.69e−17 respectively.

## Interpretation and open issues

- The crossover \(\tanh(c/\alpha)\) interpolates between vanishing discrimination as α→∞ and near-perfect discrimination as α→0.
- It is consistent with the earlier bound TV≤min{1,2c(m−1)/K} since tanh(c/α)≤c/α≤2c/α.
- The exact edge identity is proved directly and does not depend on the diffusion-limit argument.
- The reflected-walk displacement estimate must be independently expanded or sourced before the asymptotic proof is classified as fully self-contained.
- This does not establish novelty, physical simulation evidence, or optimality among all finite-state observers.

**Next:** provide a fully self-contained maximal-displacement lemma for two-sided clipped walks, and independently audit the finite-state optimality counterexample and admissible observer class.
