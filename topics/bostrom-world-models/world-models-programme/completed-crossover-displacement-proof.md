# Self-contained displacement lemma and completed crossover proof

**Status: 2026-11-05.** This note supplies the missing elementary displacement estimate for the preceding note \`exact-edge-flux-and-joint-crossover.md\` and closes its mathematical proof for the **reflecting-walk observer**. This is an internal proof, not external peer review or a novelty claim.

## Model

Fix c∈(0,1/2), and let m→∞, K=K_m≥2 with K_m/m→α∈(0,∞). On {0,…,m−1}, let F(i,+1)=min(i+1,m−1) and F(i,−1)=max(i−1,0). Each period has one Bernoulli(1/2+c) step and K−1 fair steps, independently. Let v_m be the stationary law just before the biased step, and μ_m the average of the K phase laws. The negative-hypothesis law is the spatial reflection of the positive-hypothesis law.

## Lemma 1: a pathwise maximal-displacement bound

For **every deterministic** sequence ξ_1,…,ξ_t∈{−1,+1}, put S_s=∑_{r=1}^s ξ_r, S_0=0, and define X_s=F(X_{s−1},ξ_s) for arbitrary X_0∈{0,…,m−1}. Then

\[
\boxed{|X_t-X_0|\leq 2\max_{0\leq s\leq t}|S_s|.}
\]

**Proof.** Consider X_t≥X_0. If the path never visits the lower boundary 0 at a positive time, every step through time t has either the raw increment ξ_s or a **nonpositive** correction due to upper clipping. Consequently X_t−X_0≤S_t≤max_s|S_s|.

Otherwise let u∈{1,…,t} be the **last** time X_u=0. Since X_u=0 and no lower clipping is needed after u, all later corrections (if any) are nonpositive upper-clipping corrections, so X_t≤S_t−S_u. Therefore
X_t−X_0≤X_t≤S_t−S_u≤2max_s|S_s|.

The case X_t≤X_0 is symmetric, using the last visit to the upper boundary m−1: without such a visit, only lower clipping (nonnegative corrections) can occur, so X_t−X_0≥S_t; with such a visit at u, X_t−(m−1)≥S_t−S_u, hence X_0−X_t≤(m−1)−X_t≤S_u−S_t≤2max_s|S_s|. ∎

**Boundary detail:** A clipped step that *arrives* at a boundary is not a clipping correction; the argument uses only that after the last visit to one boundary, corrections at that boundary cannot occur. The argument remains valid if the last visit is at time t (then the relevant displacement is zero in the corresponding case).

## Lemma 2: expected displacement in one period

Write the increments as ξ_1=η (biased, |η|=1) and ξ_2,…,ξ_K independent fair signs. Set M_s=∑_{r=2}^s ξ_r for s≥2 and M_0=M_1=0. Then M_s is a martingale with E[M_K²]=K−1, and

\[
\mathbb E\max_{0\leq s\leq K}|S_s|
\leq 1+\mathbb E\max_{s\leq K}|M_s|
\leq1+2\sqrt{K-1}
\]

by Cauchy–Schwarz and Doob's L² maximal inequality. Thus, uniformly over the starting state and m,

\[
\boxed{\max_{0\leq t\leq K}\mathbb E|X_t-X_0|\leq2+4\sqrt{K-1}.}
\]

This estimate is valid for both signs of the informative bias.

## Lemma 3: phase-average and phase-start have the same weak limit

For any 1-Lipschitz function φ:[0,1]→R, couple the phase-t state to the phase-0 state by following the same path. Then

\[
\left|\mathbb E_{\mu_m}\phi(i/m)-\mathbb E_{v_m}\phi(i/m)\right|
\leq\frac{2+4\sqrt{K-1}}m\to0
\]

as K/m→α. Thus the bounded-Lipschitz distance between the rescaled phase-average and phase-start laws tends to zero.

## Theorem: exact joint scaling crossover

For every c∈(0,1/2) and every integer sequence K_m≥2 with K_m/m→α∈(0,∞),

\[
\boxed{\lim_{m\to\infty}\operatorname{TV}(\mu_{+,m},\mu_{-,m})=\tanh(c/\alpha).}
\]

Moreover, under the spatial embedding i↦i/m, the phase-averaged positive-hypothesis stationary measures converge weakly to the density

\[
\boxed{f_+(x)=\frac{a e^{ax}}{e^a-1},\quad a=4c/\alpha,\quad 0\leq x\leq1,}
\]

and the negative-hypothesis limit is f_−(x)=f_+(1−x).

### Proof

**1. Exact flux and bounded densities.** From the previously proved exact edge-flux identity,

\[
\mu_m(i+1)-\mu_m(i)=\frac{2c}{K}(v_m(i)+v_m(i+1))>0.
\]

Summing over edges gives μ_m(m−1)−μ_m(0)≤4c/K. Since ∑_i μ_m(i)=1, every μ_m(i)≤1/m+4c/K. Therefore the histogram density g_m(x)=m μ_m(i) on the cell [i/m,(i+1)/m) is uniformly bounded for K/m→α and nondecreasing in the cell index. The laws are tight on [0,1], and any weak subsequential limit has an L∞ nondecreasing density f with ∫_0^1 f=1. In particular the limit has no boundary atoms.

**2. Phase-start identification.** Lemma 3 implies the embedded v_m converges to the same subsequential weak limit f(x)dx.

**3. Distributional ODE.** Let φ∈C_c^∞(0,1). Multiply the exact edge-flux identity by m φ(i/m), sum i=0,…,m−2, and use summation by parts. The left side tends to −∫_0^1 f(x)φ'(x)dx: indeed the discrete sum equals minus ∑_i μ_m(i)·m[φ(i/m)−φ((i−1)/m)] up to vanishing boundary terms, with the index shifted appropriately. The right side equals

\[
\frac{2cm}{K}\sum_{i=0}^{m−2}(v_m(i)+v_m(i+1))\phi(i/m)
\longrightarrow\frac{4c}{\alpha}\int_0^1 f(x)\phi(x)\,dx.
\]

The boundary contributions from v_m(0),v_m(m−1) vanish: because v_m converges weakly to an atomless law, the endpoint masses tend to zero. Thus f'=af in distributions, a=4c/α. The only nonnegative normalized solution is f(x)=a e^{ax}/(e^a−1). This identifies all subsequential limits, so convergence holds along the full sequence.

**4. Exact single crossing and TV.** Reflection gives μ_{-,m}(i)=μ_{+,m}(m−1−i). The strict edge-flux identity implies μ_{+,m} is strictly increasing, so the signed difference μ_+−μ_- is negative below the midpoint and positive above. Hence

\[
\operatorname{TV}(\mu_{+,m},\mu_{-,m})
=\sum_{i>(m−1)/2}(\mu_{+,m}(i)-\mu_{-,m}(i)).
\]

As the two weak limits have continuous densities, the midpoint boundary has zero mass and the sum converges to

\[
\int_{1/2}^1(f_+(x)-f_-(x))\,dx
=\frac{e^{a/2}-1}{e^{a/2}+1}
=\tanh(a/4)=\tanh(c/\alpha).
\]

∎

## Scope and limitations

- This proves the **specific reflecting-walk construction** has a nontrivial joint K/m crossover, completing the earlier missing maximal-displacement argument.
- It does not prove any optimality among all m-state automata, and it does not imply any evidence for physical simulation.
- The limiting exponential density is consistent with reflected Brownian motion with drift 2c/α, but the proof does **not** require an external diffusion-approximation theorem.
- Literature novelty has not been established; the proof should be independently checked before publication.

## Next research priorities

1. Independently audit the exact rational sticky-automaton counterexample and the observer-class definition.
2. Compare this crossover theorem against classical drifted reflecting-walk/diffusion stationary limits to determine originality.
3. Investigate the true optimal TV*(m,K,c), not merely the reflecting-walk performance.
