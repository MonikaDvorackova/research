---
id: topic-bostrom-world-models-wm-pilot
title: "Pilot experiment: finite precision vs stiction — design, results, controls, and the inference to Bostrom"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-05
tags: [pilot, results, Bostrom-inference]
---

# 1. Design (development, exploratory; seed namespace 12000; nothing confirmatory)
System x' = x + dt(−kx + bu) (dt = 0.1, k = 0.5, b ~ U[0.7, 1.3] known to the agent), observation y = x + N(0, σ²), episodes of 20 steps from x₀ = 0, controls |u| ≤ 2. Seven generators: cont; quant(q ∈ {0.1, 0.2, 0.4}) (finite precision: lattice state); stiff(δ ∈ {0.05, 0.1, 0.2}) (continuous-valued dead zone, the *physical* alternative; stiff(q/2) shares quant(q)'s dead zone). Agents: Bayesian structural comparison over the 7 hypotheses (the discovery-oriented agent; with `passive` large random controls = strong non-neural baseline; `probe` random-amplitude controls; `active` greedy EIG over a menu of 18 control programs); an MLP one-step predictor (prediction-oriented). 12 episodes, 40 replicate noise/b draws per cell. **Pre-declared development hypotheses:** H1 matched predictive accuracy but different structural identification across planners; H2 active > passive where passive information is scarce; H3 interface-limited pairs stay at chance for every policy. **Failure criteria:** H1 fails if predictive RMSE differs by > 10 % across planners; H2 fails if passive ≥ active everywhere; H3 fails if any planner separates the pair.
**First run** (σ ∈ {0.005, 0.05, 0.2}) was a design failure: exact KL (P1) shows one episode already yields > 3 nats for nearly every pair, so passive agents solve the task (`pilot_results_sigma_low.md`). I kept it and re-ran with the informative grid σ ∈ {0.2, 0.8, 3.2} chosen from the exact map (`pilot_results_sigma_high.md`); the σ grid was chosen from the exact KL table, not from agent outcomes.

# 2. Results
**P1 exact identifiability map** (per-episode KL, nats; `pilot_results.md`): at σ = 0.8: cont vs quant(0.2) 11.5 (best program) vs 0.37 (random large controls); cont vs stiff(0.1) 9.2 vs 0.18; **matched pair quant(0.2) vs stiff(0.1)** 0.40 vs 0.23; at σ = 3.2: 0.72/0.023, 0.58/0.011 and **0.025/0.014** (≈ 120 episodes for 3 nats with the best program). At σ = 0.2 the matched pair already gives 6.4/3.6.
**P2 agents** (class-decision rate ; mean posterior mass on the truth):
| σ | truth set | passive | random-amplitude probe | active EIG |
|---|---|---|---|---|
| 0.05 | identifiable truths (5) | 1.00 ; 1.00 | 0.93 ; 0.87 | 1.00 ; 1.00 |
| 0.2 | identifiable truths (5) | 0.96 ; 0.93 | 0.79 ; 0.64 | **1.00 ; 1.00** |
| **0.8** | identifiable truths (5) | **0.64 ; 0.45** | 0.47 ; 0.22 | **0.93 ; 0.86** |
| 3.2 | identifiable truths (5) | 0.42 ; 0.17 | 0.40 ; 0.15 | 0.53 ; 0.38 |
| 0.05–0.8 | interface-limited pair (quant 0.4, stiff 0.2) | 0.68–0.76 | 0.42–0.55 | 0.74–0.81 |
(Chance for a three-class decision is 0.33; the "identifiable" set excludes the equivalence pair.) At σ = 0.8 the planner raises the class-decision rate from 0.64 to 0.93 and the posterior mass on the truth from 0.45 to 0.86; per truth (σ = 0.8, passive → active class-decision): cont 0.33 → 1.00; quant(0.2) 0.85 → 0.97; stiff(0.1) 0.82 → 1.00; stiff(0.05) 0.60 → 0.85; quant(0.1) 0.60 → 0.82; **stiff(0.2) 0.90 → 0.62** (the planner is *worse* at the class decision there; exact-hypothesis decision 0.45 → 0.62 — the pair-confusion cell).
**Predictive accuracy** of the posterior-mean predictor on a fresh passive episode, RMSE/σ: 0.984–0.995 for passive and active at every σ (1.06 for probe at σ = 0.2): **equal predictive accuracy, structurally different knowledge** (H1 supported). The random-amplitude `probe` policy is worse than passive everywhere — naive exploration is not discovery-oriented.
**P3 MLP predictor** (σ = 0.05; passive training, 150 episodes): passive-test RMSE 0.069 (cont, = the noise floor of predicting from a noisy input), **0.089 (quant), 0.077 (stiff)** — above the floor, i.e. the unfiltered MLP does not fit the lattice/dead-zone transitions; probe RMSE (x = 0, u ∈ {0.02, 0.05, 0.1}) 0.006/0.016/0.017 vs 0.05 noise: the one-step probe differences are far below the observation noise, so **this probe cannot show a structural gap** (design weakness). Training on random-amplitude data *raises* passive RMSE (0.097/0.138/0.142). No structural claim is extracted from the MLP.

# 3. Verdicts on the pre-declared hypotheses
H1 **supported** (predictive RMSE within 1.1 % across passive/active; structural class-decision 0.64 vs 0.93 at σ = 0.8). H2 **supported only in the informative regime** (σ ≥ 0.2); at σ ≤ 0.05 passive is at ceiling, so the first run's design was uninformative. H3 **supported**: the interface-limited pair stays at ≤ 0.81 for every policy; note the class-decision metric *rewards guessing* in this cell (quant(0.4) is decided correctly ≈ 1.0, stiff(0.2) ≈ 0.5 because of prior bookkeeping) — for unidentifiable cells the correct output is abstention/set-valued, and these cells are reported separately and are not counted as discoveries.

# 4. Controls and what they do and do not show
- *Matched predictive accuracy:* yes (RMSE/σ). *Matched observation/intervention access and budget:* yes among Bayesian agents. *Hidden labels:* yes. *Negative control with observational equivalence:* the interface-limited pair (exact by Prop A, tested). *Positive controls with analytic identifiability:* cont vs quant at σ ≤ 0.2 (KL ≫ 3 nats/episode). *Ablations:* planner ablated (passive/probe/active). *Generator-family holdouts, structural-parameter holdouts, transfer:* **not done**. *Artefact tests:* the agent's hypothesis class contains the truth and the physics is known — a strong simplification.
- *What the result shows.* In a well-specified 1-D toy, an information-gain planner recovers a precision property that passive large-control data identify only slowly at high noise, at equal predictive accuracy. This **is the Chernoff/KL prediction** (best vs random program KL ≈ 31× at σ = 0.8); it is an instance of known design theory, not a discovery. What it does *not* show: that learned world models (Dreamer-class) behave likewise, that discovery policies transfer, or anything about nesting.

# 5. Relation to Bostrom's argument
Suppose an agent identified a finite-precision signature (quant(q) with posterior ≈ 1 against all alternatives in ℋ).
1. *What that establishes (L4, restricted):* the generator is better explained by lattice-valued state than by the continuous or stiction hypotheses in ℋ — **given** σ ≪ q, actuator reach above the dead zone, and a hypothesis class that excludes lattice-valued physical mechanisms.
2. *Does it identify a generator family?* Only the class "lattice-state dynamics with spacing q"; many implementations share it.
3. *Could an alternative physical mechanism produce it?* Yes outside ℋ: a physical lattice (a fundamental discreteness) is observationally identical to a simulated lattice; Prop A and Prop C show equivalences already inside simple classes.
4. *Does it imply computational implementation?* No: a physical lattice is a mechanism, not a computation by an agent; "computational" is a description (Chalmers), not a discovery.
5. *Does it imply simulation by an external civilisation (L5)?* No. It would affect Bostrom's proposition (3) only through a likelihood ratio P(E | simulated)/P(E | base), requiring premises about simulator behaviour (do simulators choose lattices with inhabitant-visible spacing? Bostrom's own editing assumption suggests detectable artefacts are removed, making P(E | simulated) small) and about base physics (is fundamental discreteness plausible?). **Neither likelihood is available; no numerical probability is offered.**
6. *Bayesian framework (not numerically instantiated):* hypothesis space {base reality with continuous/discrete physics} ∪ {simulation with simulator-policy variants}; priors from (1)–(2); likelihoods of signature evidence under each; reference-class assumptions as in Bostrom's observer counting. Without elicited likelihoods the framework yields no number; it clarifies *which* premises carry the inference.
**Conclusion permitted:** these methods can test restricted simulator/implementation hypotheses (type A/B) at a stated interface; the trilemma itself is not empirically testable by them.

# 6. Limitations and confounders
One-dimensional linear toy; well-specified hypothesis class; known physics; 40 draws per cell with no independent structures (only b and noise vary); σ grid selected after a failed first run (disclosed); planner is greedy EIG over a hand-made menu; MLP probe design uninformative; no learned-model discovery objective evaluated; no generalisation or transfer; no nested worlds; development only.
