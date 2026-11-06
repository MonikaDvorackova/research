# Primary-source comparison: Flower–Hellman (1972) and our hidden-periodic theorem

Date: 2026-11-06. Sources inspected: full text of https://ee.stanford.edu/~hellman/publications/10.pdf (IEEE Trans. Inf. Theory 18(3):429–431, DOI 10.1109/TIT.1972.1054820); abstract/full text of https://ee.stanford.edu/~hellman/publications/11.pdf; Hellman–Cover 1970/1971.

## What Flower and Hellman actually did

- Finite-memory, finite-time binary hypothesis testing with **independent identically distributed** observations under each hypothesis. Their formal example is symmetric coin tossing, P(H|H0)=p and P(H|H1)=1-p.
- Time-invariant, possibly randomized update function on m states, plus a fixed decision map. Error is evaluated after N observations.
- A computational search for favorable randomized automata up to seven states and up to 222 observations, subject to restrictions described as conjectures.
- In particular, their symmetry conjecture was **false for odd m**: asymmetric machines improved finite-time performance. Their randomization occurs on transitions toward less reliable memory states.
- They explicitly identify a small-transition-probability / long-time-constant tradeoff, and asymptotic behavior of optimal transition probabilities and finite-horizon error on the order of (log N)/N in their setup.

Consequences: neither 'finite-time randomization advantage' nor 'near-reducible stochastic memory leads to slow convergence' is a safe standalone novelty claim. The related-work section must prominently credit this paper rather than treating it as a peripheral reference.

## Our actual theorem and precise differences

- Observations are independent but **not identically distributed**: one informative Bernoulli step per hidden period K=2 and one fair step.
- Time-homogeneous, phase-unaware m=3 memory update; common **uniform initial memory distribution**.
- A phase-averaged memory law after n=2 complete periods; comparison by **total variation of memory-state laws**, equivalent to the best equal-prior *terminal* state classifier but not necessarily to a particular fixed decision map.
- Exact all-bias deterministic maximum c(31+4c²)/24, via exhaustive 729-rule rational certificate, and one fixed stochastic witness with strictly larger TV for all 0<c<1/2.
- A family-specific exact crossover limit n epsilon -> t; this should be framed as an explicit calculation, not the discovery of the generic slow-convergence phenomenon.

## Caveat: 'hidden phase' nomenclature

Our source model specifies an informative step followed by a fair step, with **phase-zero initialization** and a **phase-averaged readout**. It is not yet a model with an unknown random initial phase of the observation stream. 'No phase clock for the observer' is justified; 'unknown initial phase' or 'phase-agnostic initial phase' is **not** justified without a distinct mixture over initial phase and new proof. This distinction should be made explicit in the paper.

## Essential revisions to manuscript

1. In introduction, cite Flower–Hellman 1972 as the closest finite-time randomized-automaton predecessor.
2. Credit their observation that rare transitions produce long time constants; position our exact crossover as a special, calculable example.
3. State that our exact theorem is conditional on a phase-zero start and a phase-averaged terminal readout; do not conflate it with a hidden/random initial phase.
4. Distinguish equal-prior terminal Bayes error (1-TV)/2 from arbitrary prior or an observer whose decision map must be chosen independently of the hypothesis but may depend on c.
5. Add a section explicitly comparing iid symmetric coin tossing against alternating informative/fair observation laws and exhaustive deterministic certification.
6. Do not claim novelty cleared until other periodic finite-state hypothesis-testing papers are searched.

## Verified citations

- Flower, R. A., and Hellman, M. E. (1972). 'Hypothesis Testing With Finite Memory in Finite Time.' IEEE Trans. Information Theory 18(3), 429–431. DOI 10.1109/TIT.1972.1054820.
- Hellman, M. E. (1972). 'The Effects of Randomization on Finite-Memory Decision Schemes.' IEEE Trans. Information Theory 18(4), 499–502.
- Hellman, M. E., and Cover, T. M. (1970). 'Learning with Finite Memory.' Annals of Mathematical Statistics 41(3), 765–782.
- Hellman, M. E., and Cover, T. M. (1971). 'On Memory Saved by Randomization.' Annals of Mathematical Statistics 42(3), 1075–1078.

## Immediate research next steps

- Formulate and test the **random unknown initial phase** version separately, because it is currently absent.
- Verify the all-bias finite-horizon certificate in clean CI, not just internal symbolic calculations.
- Check whether our exact result can be reframed as a genuinely new theorem under a source-model assumption rather than only a special case of known finite-time randomized testing.
