---
id: topic-bostrom-world-models-wm-platform
title: "Experimental platform architecture, generative-environment taxonomy, world-model architecture comparison"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-05
tags: [platform, environments, architectures]
---

# 1. Platform architecture (implemented in `src/eid/worldgen_pilot.py`; the layering is the design contract)
| Component | Role | Knows the generator? |
|---|---|---|
| World generator | the mechanism producing the environment (`step`, hidden `PilotEnv` state) | yes (privileged) |
| Observation interface | y = x + N(0, σ²) | – |
| Action interface | bounded control u ∈ [−2, 2] per step; episodes of 20 steps from x₀ = 0 | – |
| Learned world model | any predictor of y_{t+1} from (history, u) (MLP in the pilot) | no |
| Hypothesis system | structured explanations {cont, quant(q), stiff(δ)} with likelihoods; physics (k, b, dt, σ) known | no |
| Experiment planner | `passive` / `probe` / `active` (EIG over hypothesis identity) | no |
| Evaluator | compares agent posterior with the generator's identity; scores abstention separately on equivalence classes | yes |
**Leak controls:** the agent entry point (`run_agent`) takes only `env.act`, public constants and a random stream; a unit test inspects its source for generator attributes; the evaluator never feeds back into the agent; hypothesis identity enters the agent only as its own prior.
**Known weaknesses of the pilot platform:** 1-D linear physics known to the agent; deterministic latent dynamics; hypotheses enumerate the truth (well-specified hypothesis class); only one structural property (precision/dead zone); no object structure; no partial observability beyond observation noise.

# 2. Generative-environment taxonomy (scientific purpose and identifiability conditions)
| Family | Purpose | Identifiable when | Matched alternative (negative control) | Status |
|---|---|---|---|---|
| E1 continuous physical-like dynamics, controlled discretisation | does a resolution limit leave a signature? | the law class is constrained (conservation, symmetry) so Prop C does not apply | continuous non-conservative flow with the modified equation | design only (linear Prop C verified) |
| E2 resource-bounded generators (finite precision, truncated state) | finite-precision signatures | σ ≪ q, actuator reach > dead zone, no stiction in the prior | **stiction/dead-zone mechanism** | **pilot implemented (quant vs stiff)** |
| E3 adaptive-resolution worlds | does computation allocation leave state-dependent artefacts? | artefact visible at the interface resolution | ordinary state-dependent noise | design only |
| E4 nested generators | does depth add identifiability? | only through an observable resource channel (Prop D) | flat world with the same law | design only; no experiment justified yet |
| E5 hidden causal mechanisms | causal identification through intervention | interventions reach the latent variable; modularity premises | observationally equivalent causal graph | design only (Phase 6–10 POMDP controls are the finite instance) |
| E6 adversarially equivalent worlds | essential negative controls | never identifiable (by construction) | – | partially realised (Prop A pair; Phase 9 bisimilar twin; persistent regime ≡ random-time change) |

# 3. World-model architectures: comparison and selection
| Architecture | Learning objective | Relevance to structure discovery | Used? |
|---|---|---|---|
| RSSM / Dreamer family (read at AB level) | reconstruction + reward/value in latent space | latent need not equal physical state; no structural objective | **not trained** (cost, and no hypothesis it could test that the MLP + Bayesian controls do not) |
| MuZero-style value-equivalent models (AB) | predict reward, policy, value only | indifferent to mechanism detail by design: the formal analogue of observational equivalence | discussed; not trained |
| JEPA (AB) | predict representations | representation, not mechanism | not trained |
| TD-MPC(2) | – (content unread) | – | not assessed |
| MLP one-step predictor | squared prediction error | the simplest *prediction-oriented* world model | **yes** (P3) |
| Bayesian hypothesis comparer (structured, oracle hypothesis class) | marginal likelihood + EIG planning | the *discovery-oriented* agent; equals the strong non-neural baseline and the oracle structural model | **yes** (P2) |
**Fairness of comparison.** Same interface, episodes, noise and horizon; discovery agent and passive baseline see identical numbers of episodes; the MLP receives 150 episodes (3000 transitions) — **not equalised to the Bayesian agents' 12 episodes** and trained on noisy observations without a filter, so P3 is a probe of what prediction training yields, not a head-to-head. Parameter count is not treated as a proxy for sophistication.
**Why not train Dreamer/TD-MPC now:** the pilot shows that the decisive quantities (interface-limited equivalence, σ/q thresholds) are exactly computable; a large model adds nothing until a question exists that the exact baselines cannot answer (e.g. coverage awareness, Q8).
