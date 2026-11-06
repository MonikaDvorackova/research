# Prior-art correction and a universal stochastic upper bound

Date: 2026-11-06. Research note; theorem below is proved for strictly positive transition matrices. Do not claim originality.

## Prior art

Hellman and Cover, *Learning with Finite Memory*, Annals of Mathematical Statistics 41 (1970), 765–782, DOI 10.1214/aoms/1177696958, established classical finite-memory hypothesis-testing bounds and randomized epsilon-optimal automata. Hellman and Cover, *On Memory Saved by Randomization*, Annals of Mathematical Statistics 42 (1971), 1075–1078, DOI 10.1214/aoms/1177693334, proved that randomized finite-state machines can outperform deterministic ones by arbitrarily large memory factors. Sources:
- https://www-ee.stanford.edu/~hellman/publications/09.pdf
- https://www.mendeley.com/catalogue/b5cc9f1f-909a-3784-8715-90cfe756a96e/
- https://isl.stanford.edu/~cover/papers/paper17.pdf

**Novelty correction:** A randomization advantage per se is not new. Our possible contribution would need to rest on the unknown-phase periodic model, exact finite-state classification, or genuinely new bounds. Existing Hellman–Cover iid bounds cannot be imported without proof: the hidden-phase periodic observations are not iid.

## General universal bound for positive stochastic updates

Let m≥2, K≥2, 0<c<1/2, and let T_0,T_1 be m×m strictly positive row-stochastic matrices. Put B=(T_0+T_1)/2, A_h=(1/2−hc)T_0+(1/2+hc)T_1, and P_h=A_h B^{K−1}. Let v_h be the unique stationary row of P_h and μ_h=(1/K)∑_{j=0}^{K−1}v_h A_h B^j, with the phase-start law included at j=−1; equivalently μ_h=(1/K)[v_h+∑_{j=0}^{K−2}v_h A_h B^j] for K≥2. Define r=(1+2c)/(1−2c)>1.

**Correct phase averaging:** μ_h=(1/K)[v_h+∑_{j=0}^{K−2}v_h A_h B^j]. At K=2 this is v_h(I+A_h)/2.

For every i,j, r^{-1}≤A_+(i,j)/A_−(i,j)≤r because A_h are positive mixtures of the same T_y. Multiplication by common B^{K−1} preserves this entrywise comparison, hence r^{-1}≤P_+(i,j)/P_−(i,j)≤r.

By the Markov chain tree theorem, each stationary coordinate v_h(j) is a ratio of sums of products of m−1 entries of P_h. Thus each unnormalized tree weight ratio is in [r^{−(m−1)},r^{m−1}], and the normalization ratio is also in that interval. Consequently
r^{−2(m−1)} ≤ v_+(j)/v_−(j) ≤ r^{2(m−1)}.

Applying A_+ versus A_− and then common B^j, each phase-specific law has coordinatewise ratio within [r^{−(2m−1)},r^{2m−1}], except the initial v_h which has the tighter exponent 2m−2. Summing the phase-specific distributions preserves the wider bound. Therefore
\[
r^{-(2m-1)}\le \frac{\mu_+(j)}{\mu_-(j)}\le r^{2m-1}.
\]
For any two probability distributions p,q with pointwise likelihood ratio between 1/R and R, TV(p,q)≤(R−1)/(R+1). Hence
\[
\boxed{\mathrm{TV}(\mu_+,\mu_-)\le
\frac{r^{2m-1}-1}{r^{2m-1}+1}
=\tanh((2m-1)\operatorname{artanh}(2c)).}
\]

This bound is **valid but weak** and is not claimed sharp. For m=3, c=1/5 it is much larger than the sticky lower bound ≈0.388. It holds for every period K and all strictly positive stochastic T_y; extension to sparse kernels needs a separate irreducibility/tree-support argument.

## Independent exact recheck of sticky construction at c=1/5

With ε=1/10000, ℓ=1/30 and the T_0,T_1 in \`uniform-bias-randomization-advantage.md\`, exact SymPy rational linear algebra reproduces:
\[
\mu_+-\mu_-=(0,-q,q),\quad
q=56152526035739308/144699267323882167.
\]
Thus TV=q, independent of any floating-point approximation.

## Next research priorities

1. Tighten the universal stochastic bound; the present estimate is not near the lower bound.
2. Check whether the periodic hidden-phase model can be reduced to a known iid finite-memory testing problem with an augmented clock or Markov observation process; do not assume it can.
3. Produce a standalone executable audit script and compare all previously stated exact formulas before submission.
4. Verify novelty with a systematic literature search, especially finite-memory testing for non-iid, Markov-modulated, periodic and hidden-phase observations.
