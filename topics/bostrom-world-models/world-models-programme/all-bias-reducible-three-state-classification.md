# All-bias classification of reducible deterministic three-state observers

**2026-11-06. Status: exact symbolic computational classification; independently executed locally.** Together with \`all-bias-deterministic-three-state-optimum.md\` this closes the full deterministic three-state problem for K=2 under the specified initialization. Not peer reviewed; novelty unverified.

## Setup and initialization

Consider m=3, K=2, 0<c<1/2. Each deterministic clockless observer is a pair of maps f_0,f_1:{0,1,2}→{0,1,2}, represented by 3×3 row-stochastic zero-one matrices T_0,T_1. Define B=(T_0+T_1)/2 and A_h=(1/2−hc)T_0+(1/2+hc)T_1. The one-period transition is P_h=A_hB. The common initialization at phase zero is u=(1/3,1/3,1/3), independent of the hypothesis.

For a possibly reducible P_h define the Cesàro projection

\[
v_h=\lim_{N\to\infty}N^{-1}\sum_{n=0}^{N-1}uP_h^n,\qquad
\mu_h=v_h(I+A_h)/2.
\]

The Cesàro limit exists for every finite Markov chain. It is determined uniquely by v_h(P_h−I)=0 and v_hH_h=uH_h, where columns of H_h span the right nullspace of P_h−I. These conditions preserve all harmonic observables and uniquely specify the stationary projection.

## Exhaustive exact classification

There are 3^6=729 labeled deterministic pairs. The support graph of P_h is that of (T_0+T_1)^2, independent of h and c in the open interval. Exactly 290 pairs have irreducible two-step support; **439** do not.

An independent SymPy enumeration of all 439 nonirreducible rules over the rational-function field Q(c) produced **exactly six distinct total-variation functions**:

| TV(c) | Number of labeled rules |
|---|---:|
| 0 | 265 |
| 4c/(9−4c²) | 96 |
| c | 48 |
| 2c/3 | 12 |
| 8c/[3(9−4c²)] | 12 |
| c/3 | 6 |
| **Total** | **439** |

The sign of every coordinate difference μ_+(i)−μ_−(i) was resolved symbolically, with polynomial root checks away from the endpoints and exact evaluation at c=1/5. All six final rational functions are positive and regular throughout 0<c<1/2. (Endpoint zeros at c=0 were handled separately.) This yields the exact reducible-class optimum

\[
\boxed{\max_{\mathrm{nonirreducible\ deterministic}}\mathrm{TV}(\mu_+,\mu_-)=c,\quad 0<c<1/2.}
\]

Indeed, 9−4c²>8, so 4c/(9−4c²)<c/2 and 8c/[3(9−4c²)]<c/3, while 2c/3<c and c/3<c.

## Full deterministic theorem

The earlier exact symbolic classification of the 290 irreducible rules established their maximum as W(c)=12c/(9−4c²), attained by six relabelings of the reflecting walk. Since

\[
W(c)-c=\frac{c(3+4c²)}{9-4c²}>0,
\]

combining the two disjoint classes proves

\[
\boxed{
\max_{\substack{f_0,f_1:\{0,1,2\}\to\{0,1,2\}\\\mathrm{deterministic,\ clockless}}}
\mathrm{TV}(\mu_+,\mu_-)
=\frac{12c}{9-4c²},\qquad 0<c<1/2,
}
\]

where reducible chains are interpreted via **common uniform phase-zero initialization and Cesàro stationary projection**. Exactly six labeled rules attain the optimum, all reflecting-walk relabelings.

## Why this is stronger than the earlier result

The earlier all-bias theorem excluded nonirreducible one-period chains. The earlier full 729-rule enumeration covered only c=1/5. This note completes the remaining 439-rule all-bias classification and removes both limitations **within the stated initialization convention**.

The stochastic sticky-decision counterexample at c=1/5 has TV≈0.388064 > 60/221, so the full deterministic optimum is strictly below what randomized updates can attain at that point. This does not establish the stochastic optimum.

## Computational reproducibility

A self-contained implementation should enumerate \`itertools.product(range(3),repeat=6)\`; build T_y; classify irreducibility by reachability in the graph of (T_0+T_1)^2; compute the right nullspace of P_h−I over Q(c); solve the stacked linear constraints (P_h^T−I)v_h^T=0 and H_h^Tv_h^T=H_h^Tu^T; obtain μ_h=v_h(I+A_h)/2; simplify each coordinate difference; resolve signs with exact rational-function arithmetic and polynomial root isolation on (0,1/2); count the resulting rational TV functions.

The symbolic enumeration of the 439 nonirreducible rules was executed in approximately 13 seconds locally and independently of previously stored results. It returned exactly the six functions and counts above. The preceding 290-rule all-bias theorem is used as an existing input; this run did not re-audit all 290 symbolic proofs.

## Remaining limitations

- The observer class excludes stochastic updates, a phase clock, active sensing decisions, and additional memory.
- Initialization is a modeling assumption; different hypothesis-independent initial distributions can affect reducible chains.
- This is a finite computational theorem, not an analytic classification independent of enumeration.
- Mathematical novelty relative to existing finite-memory hypothesis-testing literature is unverified.
