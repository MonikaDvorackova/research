# Arbitrary finite memory: exact linear-response identity and rare-phase asymptotics

**2026-11-05. Status: mathematical proof with exact stationary identities, checked independently for m=2,…,6 using rational matrices. Novelty not established.** This extends `asymptotic-rare-phase-memory-advantage.md` beyond three states.

## Model

Fix an integer m≥2 and a signal bias 0<c<1/2. Two hypotheses h∈{+,−} generate Bernoulli(1/2±c) on exactly one phase of a hidden K-cycle, and fair independent Bernoulli(1/2) signals on the other K−1 phases. The observer has no phase or time access and always probes. It has memory i∈{0,…,m−1}, updating i←min(i+1,m−1) after signal 1 and i←max(i−1,0) after signal 0. Decisions use only current memory. The criterion is total variation between the phase-averaged periodic stationary memory distributions.

Write B for the m×m fair-signal reflecting random-walk transition, D for the derivative of the transition with respect to p, and A_±=B±cD. All are row-stochastic where appropriate; D has row sums zero. B is symmetric, irreducible, and aperiodic (boundary self-loops), with uniform stationary row π=(1/m,…,1/m). Let Π be the rank-one matrix whose rows equal π and Z=(I−B+Π)^{-1}. For every K, the phase-start stationary rows v_± solve v_±=v_± A_± B^{K−1}. Denote phase averages by μ_±.

## Theorem 1: exact finite-K response identity

For all m≥2, K≥1, and 0<c<1/2,

[
\boxed{\mu_\pm=\pi\pm\frac{c}{K}v_\pm DZ,\qquad
\mu_+-\mu_-=\frac{c}{K}(v_++v_-)DZ.}
]

**Proof.** Let μ be the average of the K stationary phase laws. At all but the informative step, the law evolves by B; at the informative step it evolves by A_h. Sum the K one-step balance equations over a full period. The telescoping left side is zero, giving μ(I−B)=(1/K)v_h(A_h−B)=±(c/K)v_h D. Also μ1=1, π1=1, and v_hD1=0. For any zero-sum row r, the unique zero-sum solution w of w(I−B)=r is w=rZ. Therefore μ−π=±(c/K)v_h DZ. Subtract the two signs. ∎

This identity does not assume weak c. It is exact at every finite K. Its conceptual origin is classical Markov-chain Poisson-equation/linear-response theory, not claimed novel.

## Theorem 2: general m asymptotic separation

For fixed m≥2 and c∈(0,1/2), as K→∞,

[
\boxed{\operatorname{TV}_m(K,c)=\frac{c}{K} L_m
+O_m\left(\frac{c\rho_m^{K-1}}{K}\right)}
]

where
[
L_m=\begin{cases}m,&m\text{ even},\\m-1/m,&m\text{ odd},\end{cases}
\qquad
\rho_m=\cos\left(\frac{\pi}{m}\right)<1.
]

The O_m constant is independent of c∈(0,1/2). Consequently the ratio to the proven optimal two-state observer obeys

[
\lim_{K\to\infty}\frac{\operatorname{TV}_m(K,c)}{\operatorname{TV}_{2,\mathrm{opt}}(K,c)}
=\begin{cases}m/2,&m\text{ even},\\(m-1/m)/2,&m\text{ odd}.\end{cases}
]

**Proof.** The eigenvalues of the reflecting-walk B are cos(jπ/m), j=0,…,m−1. Since B is symmetric, for every probability row z,
\|zB^{K−1}−π\|_2≤ρ_m^{K−1}\|z−π\|_2. Using v_h=(v_hA_h)B^{K−1}, we obtain \|v_h−π\|_2≤ρ_m^{K−1}\|v_hA_h−π\|_2≤ρ_m^{K−1}. This is uniform in c and h.

Let w=πDZ, so w1=0 and w(I−B)=πD. Since πD=(-2/m,0,…,0,2/m), the explicit solution is

[
\boxed{w_i=\frac{2}{m}(2i-m+1),\quad i=0,\ldots,m-1.}
]

To check, w_i−(w_{i−1}+w_{i+1})/2=0 at interior states; at the left endpoint (w_0−w_1)/2=−2/m, and at the right endpoint (w_{m−1}−w_{m−2})/2=2/m. The row sum vanishes by antisymmetry. Uniqueness of the zero-sum Poisson solution establishes the formula.

The exact identity from Theorem 1 gives
μ_+−μ_−=(2c/K)w+O_m(cρ_m^{K−1}/K) in l1, uniformly in c. Total variation is half the l1 norm. Hence
TV_m=(c/K)∑_i |w_i|+O_m(cρ_m^{K−1}/K).
Elementary summation gives
∑_i|w_i|=(2/m)∑_{i=0}^{m−1}|2i−m+1|=m for even m, and m−1/m for odd m. Divide by TV_{2,opt}=2c/K. ∎

## Numerical/exact consistency checks

m=2: L_m=2, recovering TV_{2,opt}=2c/K.
m=3: L_m=8/3, recovering the earlier asymptotic ratio 4/3.
m=4: L_m=4, asymptotic ratio 2.
m=5: L_m=24/5, asymptotic ratio 12/5.
m=6: L_m=6, asymptotic ratio 3.

The Poisson equation w(I−B)=πD was independently checked by exact rational arithmetic for m=2,…,6.

## Crucial limitation: order of limits

This theorem fixes m first and lets K→∞. Its error bound depends on m because ρ_m=cos(π/m)≈1−π²/(2m²). The mixing time grows quadratically with m, so the approximation requires K large relative to m². **Do not** extrapolate the leading coefficient to arbitrary joint m,K→∞. In particular TV≤1 always, so c m/K cannot be valid uniformly when m is comparable to or larger than K/c.

## Scientific interpretation and novelty gate

The result gives a constructive **lower bound** on optimal m-state discrimination; it does not prove the reflecting-walk automaton is optimal for m≥3. The m-linear coefficient is a classical Markov-chain response phenomenon, and the proof relies on a standard Poisson equation. The originality of applying it to the hidden-phase finite-memory model remains unverified. Compare against original Hellman–Cover, finite-memory sequential hypothesis testing, and periodically modulated hidden observation models before claiming a new contribution.

**Next:** derive nontrivial upper bounds for all m-state automata; examine joint m,K scaling; and perform a proper primary-literature novelty check. Do not prepare a publication claim based on this note alone.
