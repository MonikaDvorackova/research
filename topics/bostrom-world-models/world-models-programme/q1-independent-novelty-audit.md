# Q1 independent novelty audit — preliminary research gate (2026-11-05)

Status: independent critical review of the synthesis decision, NOT proof of novelty, NOT peer review. No experiments performed.

## Decision

**REVISE Q1 BEFORE ANY THEOREM OR EXPERIMENT.** A strict interface hierarchy is not by itself a novel claim. The existing active automata learning literature explicitly distinguishes reset, input/output queries, and equivalence queries, and extends learning to stochastic reactive systems. Any new theorem must improve on this prior art rather than rephrase it.

## Critical definitional problems

1. **Interfaces are not yet a justified nested chain.** L0 passive, L1 interactive, L2 episodic reset, L3 counterfactual replay are descriptions, not complete mathematical oracle models. Specify exact observations, accessible states, whether actions can be adaptive, reset target and cost, and whether hidden random bits are resampled or held fixed.
2. **Reset and replay are not synonyms.** Resetting to the same initial *distribution* differs from restoring a particular hidden state; replay with the same exogenous randomness can reveal counterfactual couplings not recoverable from separate runs. L3 may be a strictly stronger oracle than L2, but this requires a formal joint-outcome definition.
3. **Behavioural equivalence vs identification in the limit.** Equality of induced laws defines information-theoretic indistinguishability. Distinct induced laws need not imply uniformly reliable identification over an infinite or noncompact model class, and no computational or sample-efficiency guarantee follows.
4. **'Embedded' is not automatically a mathematical novelty.** An agent with a non-resettable, reach-restricted interface is already a controlled-learning problem unless self-reference imposes an additional formal constraint.
5. **Global hidden-state structure is not identifiable up to arbitrary labels/representations.** State relabelling, nonminimal realizations, and unreachable states make naive structural recovery impossible; target effective behavioural properties or minimal realizations.
6. **Resource-bounded indistinguishability requires a family and security parameter.** Negligible advantage is asymptotic, not an equivalence relation on a fixed pair of finite mechanisms without further specification.

## Prior art that must be addressed before novelty is asserted

- Angluin-style active automata learning: membership and equivalence queries; query complexity and the role of resets. https://doi.org/10.1016/j.jlamp.2018.03.002
- Black-box Mealy learning with explicit reset/output/equivalence operations: https://link.springer.com/article/10.1007/s10817-018-9486-0
- Active model learning of stochastic reactive systems, including MDP extensions: https://link.springer.com/article/10.1007/s10270-024-01158-0
- Recent extensions of active automata learning: https://doi.org/10.3233/FAIA250992
- Source list in `literature-and-novelty-map.md` includes Gold, Kelly, Jaeger, Hsu–Kakade–Zhang, Jin et al., and Ryabko as **not accessed**; those are still outstanding. The present audit does not establish that Q1 is open.

## Proposed narrowed research question — provisional, NOT a novelty claim

For an explicitly specified class of finite-state, partially observed controlled stochastic processes, compare **one non-resettable adaptive trajectory** with **independent episodic resets to the initial distribution**, holding action and observation alphabets fixed. Which *behaviourally invariant properties* can be reliably identified under each oracle, and how do recurrence, mixing, synchronisation and reachability assumptions affect the existence and sample complexity of consistent learners?

This question remains provisional: its answer may be a direct corollary of active stochastic automata learning and controlled HMM identification theory.

## Exact next gate

1. Define two oracle models (single-trajectory and iid-reset), including stopping, adaptation, budget, randomness, and target property.
2. Read primary results on resettable vs non-resettable stochastic automata/POMDP learning, mixing/ergodicity and active query models; record exact theorem hypotheses and conclusions.
3. Either exhibit a precise candidate separation with an explicit finite-state witness and explain why existing theorems do not cover it, or mark Q1 as already known and STOP this direction.
4. Do not run an experiment, train a world model, or assert a new theorem until that comparison is complete.

## Bostrom connection

Any theorem here concerns information accessible through a specified interface, not evidence for or against simulation of our universe. The philosophical connection is underdetermination; it cannot be used as a novelty claim for a theorem about learning finite-state systems.
