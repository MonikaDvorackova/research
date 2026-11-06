# Sharper universal TV bound via likelihood-ratio oscillation

Date: 2026-11-06. Exact analytic proof, conditional on strictly positive update kernels. Corrects the loose bound in prior-art-and-stochastic-universal-bound.md.

## Setting

Let T_0,T_1 be strictly positive m×m row-stochastic matrices, m≥2. For 0<c<1/2, h∈{+1,−1}, set A_h=(1/2−hc)T_0+(1/2+hc)T_1 and B=(T_0+T_1)/2. For a period K≥2 define P_h=A_h B^{K−1}. Its stationary row v_h is unique. The phase-averaged memory law is

\[
\mu_h=\frac1K\left[v_h+\sum_{j=0}^{K-2}v_h A_hB^j\right].
\]

Put r=(1+2c)/(1−2c)>1.

## Lemma: oscillation-bound TV

If p,q are strictly positive probability vectors and

\[
\frac{\max_i(p_i/q_i)}{\min_i(p_i/q_i)}\le R,
\]

then TV(p,q)≤(√R−1)/(√R+1).

Proof: write L_i=p_i/q_i, a=min L_i, b=max L_i, with E_q L=1. Convexity of |L−1| shows its expectation is maximized, at fixed a,b, by a two-point distribution at a,b, yielding TV≤(b−1)(1−a)/(b−a). Maximizing over 0<a≤1≤b with b/a≤R gives a=R^(−1/2), b=R^(1/2), and the claimed expression. (The endpoint degenerate case p=q is immediate.)

## Theorem

For every m≥2, K≥2 and 0<c<1/2,

\[
\boxed{\mathrm{TV}(\mu_+,\mu_-)\le \tanh\!\left(m\,\operatorname{artanh}(2c)\right).}
\]

Proof: The positive matrices satisfy r^(−1)≤A_+(i,j)/A_−(i,j)≤r, and by common postprocessing with B^(K−1), the same entrywise bound holds for P_+/P_−. By the Markov chain tree theorem, each unnormalized stationary tree weight τ_h(i) is a sum of products of m−1 entries of P_h, hence

\[
r^{-(m-1)}\le \tau_+(i)/\tau_-(i)\le r^{m-1}.
\]

Let Z_h=∑_iτ_h(i). The phase-averaged law can be written as μ_h(i)=N_h(i)/(KZ_h), where

\[
N_h(i)=\tau_h(i)+\sum_{j=0}^{K-2}(\tau_h A_hB^j)(i).
\]

All terms are nonnegative. For each j, the numerator vectors under h=± obey coordinatewise ratio between r^(−m) and r^m: the τ terms have the tighter exponent m−1; multiplying τ by A_h adds at most one factor r, and common multiplication by B^j preserves inequalities. Therefore

\[
r^{-m}\le N_+(i)/N_-(i)\le r^m.
\]

The normalization factor Z_−/Z_+ is common to all coordinates, so the likelihood-ratio **oscillation** of μ_+/μ_− is at most r^(2m). Apply the lemma with R=r^(2m):

\[
\mathrm{TV}\le \frac{r^m-1}{r^m+1}
=\tanh(m\operatorname{artanh}(2c)).
\]

The bound is independent of K and is strictly stronger than the previous bound tanh((2m−1)atanh(2c)) for m≥2.

## Exact numerical comparison

At m=3, c=1/5, r=7/3:

- previous bound = (r^5−1)/(r^5+1)=8282/8525≈0.9714956012;
- new bound = (r^3−1)/(r^3+1)=158/185≈0.8540540541;
- fixed sticky observer lower bound = 56152526035739308/144699267323882167≈0.3880636514.

The gap remains large; no stochastic optimum is identified.

## Scope and literature

This is an upper bound, not a claim of sharpness or novelty. Strict positivity is used to invoke the tree theorem with nonzero weights and to define all likelihood ratios; extension to sparse irreducible kernels may be possible with care. The classic iid finite-memory testing results of Hellman and Cover (1970, 1971) are relevant but do not immediately imply this periodic hidden-phase formula.

References:
- Hellman & Cover (1970), Learning with Finite Memory, DOI: 10.1214/aoms/1177696958.
- Hellman & Cover (1971), On Memory Saved by Randomization, https://www-ee.stanford.edu/~hellman/publications/09.pdf.
