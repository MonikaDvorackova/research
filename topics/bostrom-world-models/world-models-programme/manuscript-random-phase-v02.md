# Randomization Advantage in Three-State Testing of Random-Phase Periodic Signals

**Working manuscript v0.2 — 2026-11-06. Not submitted.**

## Abstract

We study finite-horizon binary hypothesis testing by a time-homogeneous three-state automaton observing a periodically informative Bernoulli process with an unobserved, uniformly random initial phase. One observation in each two-step period is Bernoulli with parameter 1/2 ± c under the two hypotheses, and the other is fair. The observer has no phase clock and starts with a uniform memory distribution. After four observations, we prove that the optimal deterministic three-state automaton has memory-state total variation 5c/4 for every 0<c<1/2. An explicit fixed randomized observer attains 9403c/7500, yielding a strict advantage of 7c/1875. Under an alternative explicitly defined phase-averaged readout, the deterministic optimum is c(61+4c²)/48 and another fixed randomized observer exceeds it by c(1372515−991204c²)/102400000. All deterministic bounds follow from an exhaustive, exact-rational 729-rule certificate. The result is a specific periodic-source separation, not a claim to originate finite-time randomized finite-memory hypothesis testing.

## 1. Introduction

Finite-memory binary hypothesis testing is classical: Hellman and Cover (1970, 1971) studied randomized finite-state observers; Flower and Hellman (1972) explicitly analyzed finite-time randomized testing and slow convergence. Our proposed contribution is narrower: an exact, all-bias finite-horizon deterministic envelope and explicit randomized separation for an alternating informative/fair source with a genuinely random and unobserved initial phase. This model is non-IID conditional on the initial phase, and its initial phase is sampled once rather than independently at every step. Novelty beyond this precise combination remains subject to literature review.

## 2. Model

Let H∈{−1,+1} and 0<c<1/2. Draw Z uniformly from {0,1}, independently of H. Conditional on H=h and Z, observations are independent; alternating steps are informative, with Pr(Y=1)=1/2+hc, and fair, with Pr(Y=1)=1/2. A time-homogeneous memory observer has row-stochastic 3×3 matrices T0,T1, with no knowledge of Z or the time index. Its common initial memory law is u=(1/3,1/3,1/3). Define B=(T0+T1)/2 and A_h=(1/2−hc)T0+(1/2+hc)T1.

Two readout conventions are studied:

**Terminal after four observations:** ν_h=u[(A_h B)^2+(B A_h)^2]/2.

**Phase-averaged:** ν̄_h=u[(A_h B)^2(I+A_h)+(B A_h)^2(I+B)]/4. This averages the memory law immediately after four observations and after one further phase-dependent observation; it is NOT the same as the terminal readout.

In either case D=TV(ν_+,ν_−)=1/2 Σ_i |ν_+(i)−ν_−(i)|. Under equal hypothesis priors, optimal terminal Bayes error is (1−D)/2. There are 3^6=729 deterministic ordered transition pairs.

## 3. Theorem: unknown initial phase

**Theorem 1.** For every 0<c<1/2 and common uniform initialization:

(a) The global deterministic optimum for the terminal readout is

D_det,terminal*(c)=5c/4.

Let

R0(ε)=[[1−ε,ε,0],[0,0,1],[0,0,1]],

R1(ε)=[[1,0,0],[1,0,0],[0,ε,1−ε]].

For ε=9/10, D_rand,terminal(c)=9403c/7500, hence

**D_rand,terminal−D_det,terminal*=7c/1875>0.**

(b) The global deterministic optimum for the phase-averaged readout is

D_det,phaseavg*(c)=c(61+4c²)/48.

For the same randomized family at ε=17/20,

D_rand,phaseavg(c)=c(394517545+22626388c²)/307200000,

hence

**D_rand,phaseavg−D_det,phaseavg*=c(1372515−991204c²)/102400000>0.**

The stochastic witnesses are not asserted to be globally optimal among all randomized observers.

### Proof

For any deterministic pair, let d(c)=ν_+(c)−ν_−(c) (or the phase-averaged counterpart). Its coordinates sum to zero, so TV=max over subsets S of Σ_{i∈S} d_i. Every d_i(c) is an odd polynomial in c of degree at most three: the terminal law has two A_h factors, while the phase-averaged law has at most three. Therefore for each subset S, g_S(x)=Σ_{i∈S} d_i(c)/c is affine in x=c²∈[0,1/4].

The claimed deterministic envelopes divided by c are also affine in x. It therefore suffices to verify each upper bound at x=0 and x=1/4. Exact enumeration over all 729 deterministic rules, six nonempty proper subsets and two endpoints verifies 8,748 rational inequalities for each readout. The attained endpoint maxima are terminal (5/4,5/4) and phase-averaged (61/48,31/24). The reflecting deterministic maps f0=(0,0,1), f1=(1,2,2) attain the bounds identically, proving sharpness.

Direct rational multiplication of R0,R1 yields the stated randomized performance. The terminal gap is positive for c>0. The phase-averaged gap is positive because 1372515−991204c²>1372515−991204/4=1124714>0. QED.

The independently implemented rational arithmetic certificate, requiring only the Python standard library, is at topics/bostrom-world-models/world-models-programme/random-phase-independent-audit.py. It was also run separately in a fresh local environment on 2026-11-06: both sets of 8,748 inequalities passed and both randomized witnesses beat the deterministic optimum at c=1/5. The exact general witness identities are documented in all-bias-random-initial-phase-theorem.md.

## 4. Complementary fixed-initial-phase theorem

When the initial source phase is fixed informative-first, the different phase-averaged memory law is μ_h=u(A_hB)^2(I+A_h)/2. Its deterministic optimum is c(31+4c²)/24, and R0,R1 with ε=7/10 exceed it by c(74857−78964c²)/1600000. This result is not interchangeable with Theorem 1; in particular, phase-averaged readout is not equivalent to an unknown random initial phase.

## 5. Related work, scope and limitations

Hellman–Cover (1970, 1971) establish the classical importance of randomized finite-state updates. Flower–Hellman (1972) study finite-time finite-memory testing under IID observations, including rare-transition/slow-convergence phenomena. The present theorem concerns a concrete non-IID periodic model and exact all-bias deterministic envelopes. No general discovery of finite-time randomization or metastability is claimed.

All comparisons assume exactly three states, two-step periods, four observations, uniform initial memory, equal-prior total-variation evaluation, and the specified readout. No global stochastic optimum is established. A time-varying deterministic rule with a phase clock, a different initial memory state, or a different readout is outside the theorem. The result has no empirical implication for philosophical simulation hypotheses.

## 6. Conclusion

A single fixed randomized three-state rule strictly exceeds the global deterministic optimum for every nonzero admissible signal strength when observing a periodic binary source with an unobserved random initial phase. The advantage holds for both terminal and specified phase-averaged readouts, with separate exact formulas and witnesses. The finite deterministic benchmark is fully certified by exact enumeration.

## References

1. Hellman, M. E., and Cover, T. M. (1970). Learning with Finite Memory. Annals of Mathematical Statistics 41(3), 765–782. DOI 10.1214/aoms/1177696958.
2. Hellman, M. E., and Cover, T. M. (1971). On Memory Saved by Randomization. Annals of Mathematical Statistics 42(3), 1075–1078.
3. Flower, R. A., and Hellman, M. E. (1972). Hypothesis Testing With Finite Memory in Finite Time. IEEE Transactions on Information Theory 18(3), 429–431. DOI 10.1109/TIT.1972.1054820.
4. Hellman, M. E. (1972). The Effects of Randomization on Finite-Memory Decision Schemes. IEEE Transactions on Information Theory 18(4), 499–502.
5. Berg, O., Ordentlich, O., and Shayevitz, O. (2020). Binary Hypothesis Testing with Deterministic Finite-Memory Decision Rules. arXiv:2005.07445.

## Outstanding publication gates

- [x] Unknown random initial phase explicitly modeled.
- [x] Two all-bias deterministic envelopes and rational stochastic witnesses.
- [x] Independent local exact-rational 17,496-inequality audit.
- [ ] GitHub Actions CI workflow with passing public run.
- [ ] Complete targeted non-IID finite-state testing novelty search.
- [ ] Submission-grade LaTeX, bibliography and supplementary proof archive.
- [ ] Independent expert review of mathematical assumptions and novelty.

**Status: coherent v0.2 research draft, not submission-ready.**
