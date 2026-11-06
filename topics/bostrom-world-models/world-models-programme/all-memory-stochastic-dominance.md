# Stochastic-order theorem for all reflecting-walk memory sizes and periods

**2026-11-05. Status:** proved order theorem by monotone coupling. This does **not** prove a single-crossing property of probability mass functions, monotonicity of total variation in memory size, or optimality. Novelty not established; stochastic monotonicity is classical.

## Model

For integer m≥2, K≥2, and 0<c<1/2, the memory is M∈{0,…,m−1}. Given a binary observation y∈{0,1}, update by

F(i,1)=min(i+1,m−1),  F(i,0)=max(i−1,0).

Exactly one step per K-period is informative, with Y_+~Bernoulli(1/2+c) and Y_-~Bernoulli(1/2−c); other steps have fair Bernoulli signals. The automata have no phase information. Let ν_{h,j} be the unique periodic stationary memory law at phase j under h∈{+,−}, and μ_h=K^{-1}∑_{j=0}^{K−1}ν_{h,j} the phase-averaged stationary law.

## Theorem: first-order stochastic dominance

For every phase j and every increasing function f:{0,…,m−1}→R,

\[
\boxed{\mathbb E_{\nu_{+,j}}f(M)\geq \mathbb E_{\nu_{-,j}}f(M).}
\]

The same holds for the phase averages μ_+, μ_−. Equivalently, for each threshold r,

\[
\boxed{\nu_{+,j}\{M\geq r\}\geq\nu_{-,j}\{M\geq r\},\qquad
\mu_+\{M\geq r\}\geq\mu_-\{M\geq r\}.}
\]

Moreover μ_+≠μ_- (strict inequality for at least one threshold), and hence TV(μ_+,μ_-)>0.

### Proof: explicit monotone coupling

For each time t, draw a common independent U_t~Uniform(0,1). Under h=+, take Y_{+,t}=1_{U_t≤p_{+,t}}, and under h=− take Y_{-,t}=1_{U_t≤p_{-,t}}, where at the informative phase p_{+,t}=1/2+c≥p_{-,t}=1/2−c and elsewhere both equal 1/2. Thus Y_{+,t}≥Y_{-,t} almost surely.

The update map F is nondecreasing separately in i and y. Therefore, whenever M_{+,t}≥M_{-,t}, we also have M_{+,t+1}≥M_{-,t+1} almost surely. Initialize the two memory states equally (for example at zero), so the order holds pathwise at every subsequent time.

At any fixed phase j, observe the coupled chains after n complete periods. The one-period transition products are irreducible and aperiodic finite-state kernels (all signal probabilities are strictly between zero and one, and the reflecting boundaries allow self-loops), hence each marginal converges to its unique periodic stationary phase law ν_{h,j}. The pathwise ordering passes to the limit, proving stochastic dominance at each phase. Averaging over phases preserves stochastic order.

For strictness of the phase-average laws, suppose μ_+=μ_-. At each phase, the difference in the expectation of the increasing function f(i)=i is nonnegative, and their average is zero, so the expected memory values must be equal at **every** phase. At the phase immediately before the informative observation, the two phase laws are stochastically ordered and have the same mean; on a finite totally ordered state space this implies that the two phase laws are identical, say ν. But after the informative observation the laws are ν A_+ and ν A_−. Their expected memory values differ by

\[
\mathbb E_{\nu A_+}M-\mathbb E_{\nu A_-}M
=2c\sum_{i=0}^{m-1}\nu_i[F(i,1)-F(i,0)]>0,
\]

because F(i,1)>F(i,0) for every i when m≥2. This contradicts equality of the means at every phase. Therefore μ_+≠μ_− and TV>0. ∎

## What this does and does not resolve

- It establishes a universal stochastic-order relation for this **specific** reflecting-walk observer, independent of m,K,c.
- It implies every increasing decision statistic has no smaller expectation under h=+.
- It does **not** imply that the signed probability mass difference μ_+−μ_- has one sign change. Stochastic dominance controls **cumulative tails**, not pointwise signs. Thus it does not justify removing the absolute values in the all-m cofactor formula.
- It does **not** prove that TV_m is increasing with m, even though finite symbolic examples suggest that.
- It does not show anything about physical simulation hypotheses. Its mathematical mechanism is classical monotone coupling.

## Next step

Seek a **likelihood-ratio ordering** or total-positivity property for the periodic stationary laws. Such a stronger order would imply single crossing of the signed masses, but it must be proved for the actual K-step transition products; ordinary stochastic dominance is insufficient. Another option is to construct a counterexample to single crossing for some m,K,c before pursuing a universal theorem.

**Novelty:** unverified; monotone coupling itself is standard.

## Update 2026-11-06 (supersedes the "does not prove" caveats)
Single crossing and strict monotone likelihood ratio ordering are now **proved** for all m ≥ 2, K ≥ 1, 0 < c < 1/2 in `mlr-and-single-crossing-theorem.md`, via invariance of the cone of nondecreasing mass functions under the informative and fair kernels plus mirror symmetry. Stochastic dominance (above) remains correct and is implied. The statement that strict dominance does not by itself give single crossing remains true as a logical remark.
