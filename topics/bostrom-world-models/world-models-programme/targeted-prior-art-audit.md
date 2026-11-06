# Targeted prior-art audit: finite-memory testing and periodic observations

Date: 2026-11-06. Preliminary bibliographic audit; not an exhaustive novelty clearance.

## Closest prior work

1. Hellman, M. E. and Cover, T. M. (1970), "Learning with Finite Memory," *Annals of Mathematical Statistics* 41(3), 765–782. DOI 10.1214/aoms/1177696958. Their baseline is IID observations and long-run error for time-invariant finite-memory hypothesis testing; randomized transitions are already central. Therefore our paper must **not** claim to discover randomization advantage in finite-memory hypothesis testing generally.

2. Hellman, M. E. and Cover, T. M. (1971), "On Memory Saved by Randomization," *Annals of Mathematical Statistics* 42(3), 1075–1078. DOI 10.1214/aoms/1177693334. They show potentially arbitrarily large memory savings through randomization. This strongly narrows novelty claims.

3. Flower, R. A. and Hellman, M. E. (1972), "Hypothesis Testing With Finite Memory in Finite Time," *IEEE Transactions on Information Theory* IT-18, May, 429–431. Primary author PDF: https://ee.stanford.edu/~hellman/publications/10.pdf . **Critical reference:** finite-time finite-memory hypothesis testing is explicitly addressed, contrary to any suggestion that finite-horizon analysis itself is new. Compare its model, initialization, update constraints, and randomization results carefully before submission.

4. Hellman, M. E. (1972), "The Effects of Randomization [in] Finite Memory Decision Schemes," *IEEE Transactions on Information Theory* IT-18, July, 499–502. Listed in Hellman's publication index; inspect full paper to compare randomized/deterministic separation.

5. Chandrasekaran, B. and Barley, T. J. (1970), "Finite memory hypothesis testing: Achieving performance bound without randomization," 9th IEEE Symposium on Adaptive Processes / Decision and Control. DOI 10.1109/SAP.1970.269941 (IEEE record; other secondary indexes inconsistently report 10.1109/SAP.1970.4044596). It describes simulating a randomizer using cross-problem statistical information. This does not immediately match our single-observer model, but must be distinguished.

6. Oleyaeimotlagh, Y. and Banerjee, T. (2026), "Modified Wald formulation for sequential binary hypothesis testing in statistically periodic processes," *Sequential Analysis* 45(2), 277–303, DOI 10.1080/07474946.2025.2579569. Periodic hypothesis testing is already a developed research topic. Its sequential, generally unconstrained-memory setting differs from our fixed three-state, phase-unaware finite-horizon setting, but a careful reading is required.

7. "Finite memory algorithms for testing Bernoulli random variables," *Information and Control* 24(1) (1974), 11–19, DOI 10.1016/S0019-9958(74)80019-7. Studies **time-varying** finite-state automata on IID Bernoulli data, another contrast to our time-homogeneous, hidden-phase model.

## Provisional differentiation matrix

| Feature | Our current theorem | Hellman–Cover 1970/1971 | Flower–Hellman 1972 | Periodic sequential testing 2026 |
|---|---|---|---|---|
| Three-state time-homogeneous observer | yes | finite-state time-homogeneous, general m | finite-memory; inspect precise constraints | not established |
| Hidden two-step periodic informative phase | yes | no: IID observations | not established; inspect | periodic process, phase information assumptions to inspect |
| Fixed horizon two complete periods | yes | asymptotic criterion | yes: finite-time theory | sequential criterion |
| All-bias explicit exact 729-rule deterministic envelope | yes | not established | not established | not established |
| Explicit strict randomized gap for every 0<c<1/2 | yes | randomized advantages in other models | inspect | not established |
| Phase-averaged memory-state TV | yes | long-run decision error | finite-time decision error | sequential error/delay |

'Not established' means not checked in the cited source, **not** a negative novelty finding.

## Wording required in manuscript

Use: "We give an explicit, exact, all-bias finite-horizon separation for a particular phase-unaware periodically informative source and three-state observer."

Avoid: "We first show randomization improves finite-memory hypothesis testing," "We introduce finite-time finite-memory testing," "We are the first to study periodic hypothesis testing," or "This is evidence of simulation."

The central unresolved novelty issue is whether the *combination* of hidden periodicity, time-homogeneous three-state updates, phase-averaged TV, uniform initialization, and exact all-bias separation has already been obtained or follows immediately from known finite-time theorems.

## Primary and secondary links

- https://doi.org/10.1214/aoms/1177696958
- https://doi.org/10.1214/aoms/1177693334
- https://ee.stanford.edu/~hellman/publications/10.pdf
- https://ee.stanford.edu/~hellman/publications.html
- https://ieeexplore.ieee.org/document/4044596/
- https://doi.org/10.1080/07474946.2025.2579569
- https://doi.org/10.1016/S0019-9958(74)80019-7

## Submission blockers

1. Read Flower–Hellman 1972 in full, compare finite-horizon theorem and setup.
2. Read Hellman 1972 on randomization.
3. Search more recent finite-state testing under non-IID/periodic and hidden-phase observations.
4. Validate manuscript formula and independent certificate in a clean reproducible environment; attach environment/CI evidence.
5. Reframe introduction and related work explicitly around these predecessors.

**Status:** meaningful differentiation hypothesis, not established originality.
