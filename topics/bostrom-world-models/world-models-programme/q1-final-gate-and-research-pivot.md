# Q1 final gate and research pivot — 2026-11-05

Status: research decision, not a novel theorem or peer review. No experiments.

## Decision: NO-GO on generic reset/no-reset hierarchy as the primary contribution

The 2026-11-05 prior-art checks identify substantial theoretical competition:
- Mhammedi, Foster & Rakhlin, *The Power of Resets in Online Reinforcement Learning* (NeurIPS 2024), https://www.microsoft.com/en-us/research/publication/the-power-of-resets-in-online-reinforcement-learning/ — local simulator/reset access changes learnability assumptions in MDP RL.
- Chen, Wang, Xiong, Mei & Bai, *Lower Bounds for Learning in Revealing POMDPs* (ICML 2023), https://proceedings.mlr.press/v202/chen23ae.html — information-theoretic lower bounds in partially observable RL.
- Hsu, Kontorovich & Szepesvári, *Mixing Time Estimation in Reversible Markov Chains from a Single Sample Path* (NeurIPS 2015), https://papers.nips.cc/paper_files/paper/2015/hash/7ce3284b743aefde80ffd9aec500e085-Abstract.html — inference from one non-resettable path.
- Groz et al., *Inferring Finite State Machines Without Reset Using State Identification Sequences* (2015), DOI 10.1007/978-3-319-25945-1_10 — reset-free finite automata learning.

These do not prove that every specific controlled-HMM identification question is solved; they do make generic 'resets improve identification/learning' an unconvincing novelty claim.

## Concrete elementary counterexample (NOT novel)

Let M_b have initial state s0 and absorbing state s1. On the first action, the observer receives a Bernoulli(b) output and enters s1; thereafter it always observes zero regardless of action. For b in {1/3,2/3}, an uninterrupted trajectory contains exactly one informative Bernoulli sample, even as its length tends to infinity; its best classification error under equal priors is 1/3. With independent resets to s0, n episodes give n independent Bernoulli samples and the classification error tends to zero. This shows a strict separation in consistent identification, but it is elementary and cannot support a publication claim.

It also exposes the core problem: without a recurrence or recoverability assumption, the reset separation is almost tautological. With strong recurrence/mixing assumptions, it may collapse, but proving this would largely re-enter existing ergodic and automata-learning theory.

## Decision on the broader programme

Retain the fundamental distinction between effective observable laws and host implementation. Do not equate a model's predictive adequacy with identifying a physical substrate. This is established epistemology, not a discovery about our universe.

**Primary recommendation:** move to a rigorously sourced conceptual/theoretical paper only if it can offer a clearly original synthesis or a new formal impossibility/complexity result after expert review. A survey or philosophical analysis can be valuable, but must not be marketed as a new mathematical theorem.

**Do not** launch further world-model, symbolic-regression, or reset experiments. Do not assert the simulation hypothesis is empirically supported.

## Next concrete milestone

Produce a tightly scoped 2-page research prospectus that (1) states one exact claim worth defending, (2) cites closest opposing and supporting primary literature, (3) distinguishes a conceptual contribution from a theorem, (4) lists explicit reviewer objections, and (5) gives a STOP criterion. Obtain external disciplinary review before writing a full manuscript. If no original claim survives, end the research line and archive the project as a negative methodological study.

This decision supersedes the earlier provisional endorsement of Q1 as a theorem programme.
