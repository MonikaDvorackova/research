# Q1 prior-art gate: resetless learning (2026-11-05)

Status: primary-source-based novelty assessment. No experiments, no theorem claimed, no PR merge.

## Decision

**NO-GO for the broad L0–L3 hierarchy as a standalone novelty claim. REVISE toward a precise learning-complexity question.**

The key question is not whether resets matter: the literature already studies this extensively. A narrower possible question is whether a clearly defined class of *behaviourally identifiable*, partially observed controlled systems exhibits a provable separation in **sample/query complexity** between one uninterrupted adaptive trajectory and independently resettable episodes, under matched assumptions and targets. This is **not yet established as open**.

## Direct prior-art checks

1. Groz, Simao, Petrenko, Oriat (2015), *Inferring Finite State Machines Without Reset Using State Identification Sequences*, DOI: 10.1007/978-3-319-25945-1_10. Learns finite-state control structure without reset or an equivalence oracle, given a state bound and characterising sequences; polynomial test length with exponent depending on characterisation-set size. [publisher record](https://doi.org/10.1007/978-3-319-25945-1_10)
2. Even-Dar, Kakade, Mansour, *Reinforcement Learning in POMDPs Without Resets* (IJCAI 2005). Continuous interaction in connected POMDPs; approximate homing/reset strategy and asymptotic optimal average reward. **Important limitation**: reward optimisation is not identification of a mechanism. https://www.tau.ac.il/~mansour/papers/05ijcai.pdf
3. *Active model learning of stochastic reactive systems* (Software and Systems Modeling, DOI 10.1007/s10270-024-01158-0). Explicit stochastic model-learning teacher with `step` and `reset` operations. https://link.springer.com/article/10.1007/s10270-024-01158-0
4. *A research agenda for active automata learning* (2026), section 'Resets' / Challenge 20. States resetless algorithms already exist, often using homing sequences or characterising sets, while practical resetless applicability remains challenging. https://sfortz.github.io/publication/2026-al-agenda/2026-al-agenda.pdf

## Correction to the earlier synthesis

The proposed interface levels are not automatically strictly nested in **identifiable content**, and the presence of resets does not itself prove a novel theorem. Reset-to-initial-distribution, homing-to-belief-state and same-randomness counterfactual replay are different oracles.

Do not infer structural identifiability from a theorem guaranteeing near-optimal average reward.

## A concrete next theorem candidate (unverified)

Fix finite alphabets and a class C of minimal, partially observed, controlled stochastic machines with explicitly stated reachability and distinguishability assumptions. Define two oracle models:
- O_cont: one uninterrupted, adaptively controlled trajectory, no external reset.
- O_reset: independently repeated trajectories sampled from the same initial distribution, with reset costs accounted for.

Fix the target as identification of a behavioural equivalence class up to error epsilon and confidence 1-delta, not recovery of arbitrary hidden-state labels.

Ask whether there is a natural subclass C with **both** oracles information-theoretically consistent but a superpolynomial (or otherwise tight, significant) separation in optimal sample complexity, and identify the exact mixing/homing parameters that control it.

This is a *candidate question*, not a theorem, and could be answered already by prior work. Before doing any proof or experiment, check the closest POMDP learning, automata testing, mixing-time and lower-bound results theorem-by-theorem.

## Next hard gate

1. Specify C and both oracles exactly, including initial distribution, hidden-state equivalence, allowed adaptive policies, resets, randomisation and accounting of observations/actions.
2. Produce a closest-theorem comparison for the four references above plus POMDP sample-complexity and resetless automata literature.
3. Find a precise theorem gap with a candidate construction **or STOP**; lack of a search hit is not evidence of novelty.
4. No experiments, new agents, or speculative claims about detecting simulations.

## Scientific interpretation

The connection to Bostrom remains epistemological: an embedded observer's admissible interface bounds which effective laws can be distinguished. This does not produce empirical evidence for simulation or reveal the host substrate.
