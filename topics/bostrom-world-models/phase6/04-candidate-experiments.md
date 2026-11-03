---
id: topic-bostrom-world-models-phase6-candidates
title: "Candidate experiment portfolio (designs only, none executed)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [experiments, design]
---

# Candidate experiment portfolio

Designs only. Fields: (1) question, (2) competing hypotheses, (3) formal model, (4) environment, (5) observer, (6) observations, (7) interventions, (8) controls, (9) primary metrics, (10) failure modes, (11) statistics, (12) compute, (13) falsifier, (14) meaningful contribution, (15) literature that could already explain it.

## X1 — Detecting hypothesis-class inadequacy: criticism evidence and design (Directions C+E)
1. Can an embedded Bayesian observer detect that the truth lies outside its finite class, and how much does the choice of intervention policy matter?
2. H_a: criticism-driven design detects out-of-class truth faster than random wide and than within-class EIG. H_b: within-class EIG is no better than random (P10). H_0: all policies equal.
3. Finite controlled processes; class M = {reference POMDP and members differing in emission noise/state-splitting}; truth ∈ M (null) or truth = Et(ε) ∉ M. Test: anytime-valid e-process E_t = q_t(D_t)/sup_{θ∈M} p_θ(D_t) with a predictable saturated order-k alternative q (universal-inference construction).
4. Env 2 POMDP (exact forward algorithm). 5. Oracle-likelihood Bayesian observers with the four policies; criticism statistic computed without a learned model. 6. Observation sequences and own actions. 7. Action sequences over {0,1,2}, open loop and adaptive.
8. Truth in M (type-I error); bisimilar split-state truth (must not reject); q = 0 policy (must not reject, exact); misleading prior.
9. Rejection rate at α = 0.05 vs budget; episodes-to-reject; proportion of rejections whose evidence comes from action 2.
10. Saturated alternative too weak at small budgets (low power); e-process conservative; truth ∉ M but TV(M, truth) tiny on the probed class.
11. Exact type-I check by enumeration at small horizon; bootstrap CIs over seeds; paired comparisons across policies with Holm; TOST for equivalence controls.
12. CPU only; minutes per seed (exact enumeration, no neural training).
13. H_a falsified if criticism design speeds detection by < 1.5× vs random wide (CI lower bound) or if type-I error > α under any in-class truth.
14. A quantified, exact account of when an embedded observer can *know its class is inadequate* as a function of design and intervention coverage; a P10-style result for criticism design.
15. Gelman–Shalizi; universal inference; Catanach–Das; Wald bound. Likely explained by them; the contribution would be the design comparison, not the test.

## X2 — Prediction–identification frontier (Direction A, theory + exact check)
1. How far can the mechanism distance on class Π′ exceed the predictive distance on training class Π? 2. H: sup ratio is governed by the maximal policy likelihood ratio on the reachable set (Prop. 3), i.e. tight; H′: structure (hidden-state quotients) gives strictly larger gaps for some pairs. 3. Finite POMDP families; distances = per-episode KL or TV on Π and Π′. 4. Random POMDPs on 3–4 hidden states + the benchmark. 5. No learner; exhaustive/LP computation of the frontier. 6–7. Policy classes parametrised by q. 8. Positive control: pairs with identical kernels (frontier 0). 9. Frontier curves; fraction of random pairs saturating the Prop. 3 bound. 10. Bound loose generically (then the result is “not tight”, itself a finding). 11. Exact; random-family sampling with bootstrap. 12. Light. 13. Falsified if a pair exceeds the Prop. 3 bound (would indicate a proof error) or if the bound is never approached. 14. A tight characterisation or a counterexample class. 15. Data-processing inequality, Prop. 3, coverage/concentrability in offline RL (not yet read).

## X3 — Generalisation of the learned-observer failure (Directions A/E, generality test)
1. Is likelihood inversion/overconfidence a property of the *learners used* or of coverage? 2. H_cov: failure occurs iff training coverage misses the probed range, for every learner family; H_arch: failure persists under full coverage for some families. 3. As in Phase 5, plus learner families. 4. A third environment (discrete-state Markov chain with known kernel; and env 2 with nonstationary drift). 5. Count-based/Dirichlet-smoothed tabular model, GRU, small transformer, deep ensemble, a calibration-corrected (temperature-scaled) variant; Bayesian observer from each. 6–7. As Phase 5. 8. Training on matched-coverage vs narrow data. 9. Accuracy, ECE, false-identification rate, inversion rate versus coverage fraction. 10. Hyperparameter sensitivity; fidelity confound. 11. Pre-specified, held-out seeds ≥ 20, mixed-effects over learner family, equivalence tests for “no effect under full coverage”. 12. GPU not needed; hours. 13. H_cov falsified if any family fails under full coverage. 14. Evidence that the failure is not an architecture artefact (or a characterised exception). 15. Nalisnick; Ren; ensembles/calibration literature (unread).

## X4 — Hypothesis expansion and discovery (Direction C)
1. Can an agent, after rejecting its class, propose a member that is validated on held-out interventions? 2. Expansion from a proposal family (mixtures, state-splits) recovers truth only if truth is in the family. 3. X1 plus a proposal grammar. 4–7 as X1. 8. Truth outside the grammar (must fail honestly). 9. Held-out predictive loss on probed and unprobed interventions. 10. Overfitting the probed class (prediction ≠ identification again). 13. Falsified if expansion improves in-sample but not held-out interventional loss. 14. A clean demonstration of the updating/criticism/expansion/discovery separation. 15. Gelman–Shalizi; program-synthesis/structure-learning literatures. Depends on X1 passing.

## X5 — Observer-effect nonstationary POMDP (Direction E)
Mechanism switches when the informative action is used too often (an adversarial/closed-loop environment). Question: does adaptivity create a *new* barrier beyond coverage? Hypotheses: yes only if the switch is itself undetectable; no if the switch can be modelled as a larger POMDP (then it reduces to known equivalence). Exact; likely reducible to a bigger POMDP — risk of triviality high. Falsifier: reduction proof. Literature: POMDP augmentation (standard).

## X6 — Computational indistinguishability (Direction B)
Hidden-state emission from a keyed PRF vs true randomness; bounded learners vs unbounded. Question: gap between bounded and unbounded observers. Result expected from cryptography; low novelty; defer.

## X7 — Nested simulation (Direction D)
Per the brief, no implementation. Pre-condition: a formal model where nesting depth changes a posterior over a parent parameter given identical non-nested experiments. None exists; see open-question map.

## Not-implemented-by-design
X4–X7 are not to be built before X1/X3 results. No large-scale runs authorised.
