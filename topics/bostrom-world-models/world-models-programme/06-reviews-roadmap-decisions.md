---
id: topic-bostrom-world-models-wm-roadmap
title: "Adversarial reviews, multi-month roadmap, decision log and verdict for the world-models programme"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-05
tags: [review, roadmap, decisions]
---

# 1. Six internal reviews (same agent; not external peer review)
| Reviewer | Strongest objection | Evidence in this repository | What would answer it | Blocks next step? |
|---|---|---|---|---|
| World-models researcher | "Your 'world model' that discovers structure is a Bayesian comparer over a hand-written hypothesis class that contains the truth; the learned model (MLP) was never evaluated on a structural question. Dreamer/TD-MPC were not even trained." | `04` §3: only an MLP was trained; P3's probe was uninformative | a learned latent model whose structural claims are scored against the exact hypothesis posterior on the same data (Q3 proper); a coverage-awareness test (Q8) | **Yes** for any claim about *learned* world models |
| Model-based RL researcher | "Equal one-step prediction error is a weak notion of matched predictive accuracy; multi-step rollouts and control performance are what matter. Your task has no reward." | P2 uses one-step RMSE/σ only | multi-step rollout error and a control task in which the dead zone matters | Yes for H1 as a world-model statement |
| Causal representation learning researcher | "L3 is claimed in the hierarchy but nothing causal is learned or tested; the 'structure' is a precision flag, not a causal variable." | Prop H(c) is the only L3 statement; pilot has no latent causal variables | E5-type environment with latent causal variables and interventions | Yes for the causal part; not for the precision pilot |
| Mathematical statistician | "Every result is Gaussian KL plus Chernoff design; the 31× ratio is arithmetic; 40 draws per cell with the same b-distribution are not independent structures; the class-decision metric rewards guessing in unidentifiable cells." | `05` §3–4 (disclosed) | independent structures, set-valued scoring throughout, preregistered thresholds | Blocks any confirmatory claim |
| Philosopher of science | "'Computational signature' conflates a description with a discovery. A lattice is a mechanism; whether it is 'computational' or 'simulated' is not something the data can say. Your Bostrom inference ends with 'no number', which is the honest part, but then what is the contribution?" | `05` §5 | a defended account of what, if anything, a precision signature adds to the evidential bearing on Bostrom's (3) beyond restricting simulator-hypothesis space | Does not block experiments; blocks the interdisciplinary framing |
| Theoretical computer scientist | "Finite precision is the wrong abstraction for a simulator's resource bounds; resource-bounded generators are about computational *complexity* (e.g. pseudorandomness), where indistinguishability for bounded observers is a cryptographic statement, not a KL map. Nesting is trivial composition." | Prop D; Phase 8 (computational indistinguishability noted, not tested) | a complexity-theoretic formulation (bounded observers vs bounded generators) with a concrete separation | Yes for any claim beyond precision-type signatures |
**Disagreements retained.** The RL and world-model reviewers want learned models in the loop; the statistician and philosopher think that without independent structures and a defended inferential bridge more models add nothing; the complexity-theory reviewer questions the precision abstraction itself.

# 2. Multi-month roadmap (evidence gates, not dates)
| Milestone | Required evidence | Failure criterion | Cost | Decision rule |
|---|---|---|---|---|
| M1 verified literature and gap | full reading of: TD-MPC2, DreamerV3 text, active causal discovery, backward error analysis (Hairer et al.), Ziv, Chalmers *Reality+*; novelty ledger updated | a source already contains the dissociation/identifiability map for learned world models | days | continue / pivot |
| M2 formal problem | definitions of discovery, identifiability, budget for *learned* models with a stated hypothesis-free variant | no formulation beyond the Bayesian one | days | continue / reformulate |
| M3 identifiable vs non-identifiable generator classes | exact map for ≥ 3 property families (precision, resolution allocation, resource-bounded randomness) incl. complexity-theoretic one | all reduce to the KL map (then stop at a note) | 1–3 weeks | continue / stop |
| M4 benchmark | ≥ 30 independently generated structures, set-valued scoring, observation/interface variants | pilot platform fails the leak tests | 2–4 weeks | continue |
| M5 strong baselines | structured Bayesian oracle, passive/active, learned latent model (RSSM-class) with filtered inputs | learned model matches oracle trivially, or fails for trivial reasons | 2–3 weeks (GPU optional) | continue |
| M6 adversarial pilots | matched predictive accuracy, coverage-awareness (Q8), transfer to held-out generator families | no dissociation at matched coverage | 2–4 weeks | continue / stop |
| M7 theory or informative negative | a non-elementary statement (e.g. resource-bounded identifiability) or a documented negative | everything is a corollary | parallel | decide at gate |
| M8 external expert review | at least one world-models and one philosophy reader | fatal objections | – | revise |
| M9 confirmatory design | frozen preregistration with independent structures and structure-level inference | M6 negative | – | proceed / stop |
| M10 manuscript | only after M6–M9 | – | – | – |
No preregistration is frozen now.

# 3. Decision log
| Date | Decision | Reason |
|---|---|---|
| 2026-11-05 | Phase 11 closed; prototype kept as infrastructure; K-ratio claim restricted to the unconstrained family | `00` |
| 2026-11-05 | Selected Q2 (precision signatures) and Q3 (prediction vs discovery) for pilot; Q8 deferred; Q4, Q5, Q6, Q7 rejected/deferred | `02` |
| 2026-11-05 | First pilot σ grid was uninformative and is retained; re-run on a grid chosen from the exact KL map | `05` §1 |
| 2026-11-05 | No world model other than an MLP trained; Dreamer/TD-MPC not trained | no question they could answer that exact baselines cannot |
| 2026-11-05 | No novelty claimed | `01` matrix |

# 4. Verdict
**REVISE** the selected direction. The pilot established the *platform logic* and two exact facts (interface-limited equivalence; quantisation ≡ stiction under noise ≥ q/2), and reproduced the classical advantage of information-gain design at matched predictive accuracy; it did **not** test any learned world model on a structural question, and the Bostrom bridge remains premise-bound. The programme should continue only if M3 produces a property family whose identifiability is **not** a one-line KL calculation (candidate: resource-bounded/pseudorandom generators and bounded observers) or M6 shows a dissociation for learned models at matched coverage that exact theory does not predict. Otherwise: NO-GO and archive as a methodological note.
**The single most important question for the next milestone:** *Does a learned latent world model, trained for prediction, differ from the structured Bayesian oracle in what it can tell us about hidden computational structure at matched predictive accuracy and matched coverage — and can it tell when it cannot know?*
