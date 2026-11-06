# 07 — Learned world models: definitions, hypotheses, analysis plan (written BEFORE the final-test evaluation)

Status: development-stage research. No confirmatory seed ranges (600–629, 700–719, 800–829) are used. Nothing here is a frozen preregistration; it is a dated analysis plan so that final-test outcomes are not chosen after seeing them. Instance namespaces: training = `seed*1_000_003+step`; model selection / dev eval = 9001, 9100–9150, 9300+; **final development test = 9200+ (not touched until this plan is committed)**.

## 1. Definitions (benchmark `eid.gwb`)

| Term | Definition in this benchmark |
|---|---|
| True generative mechanism | a tuple (class c ∈ {cont, quant, stiff, delay, lag, reset}, parameters K, b, p, σ); process deterministic, only observation noise random |
| Hidden state | x_t (all families), actuator state z_t (lag), action buffer (delay), clock (reset) — never exposed |
| Observable | y_t = x_t + σ ε_t after action a_t; a_t ∈ [−1,1] |
| Intervention | a chosen open-loop action program on a block (8 steps) or whole episode; the agent may choose any program from its menu |
| Learned latent representation | summary state of a trained recurrent world model after reading (a,y) history (GRU hidden h_L; RSSM also has stochastic z) |
| Predictive world model | model of p(y_t | history, a_t) trained by NLL (RSSM adds KL + prior-predictive loss) |
| Structural hypothesis | the mechanism class label (6-way) |
| Discovery policy | rule choosing interventions given history (passive / uniform / heuristic sweep / random block / exact-Bayes EIG / learned-ensemble disagreement) |
| Structural ground truth | class label of the generator (privileged; used only for scoring). Label −1 for equivalent worlds |
| Identifiability (interface-relative) | two generators g≠g′ are 𝒜-equivalent if P_g^a = P_g′^a for every action program a in the interface 𝒜 = [−1,1]^L. `eqA` (quant/stiff thresholds beyond actuator reach) and `eqB` (delay ≥ horizon vs reset period 1) are exactly equivalent: x ≡ 0 (tested) |
| Discovery success | correct class with calibrated confidence on identifiable instances; **no confident claim** on equivalent ones |
| Epistemic calibration | ECE of class probabilities on identifiable instances; claim rate (max prob ≥ 0.8) on equivalent instances (any such claim is unsupported) |
| Transfer generalisation | probe accuracy on a generator family the world model never saw in training |

Levels: this study addresses inference levels 1–4 only (prediction, interface-relative structure/mechanism class). Level 5 (computational implementation / simulation) is not tested; "quantised"/"reset"/"delay" are mechanisms inside a toy generator, not claims about any real universe.

## 2. Hypotheses and primary outcomes

* **H1** predictive ≠ structural: across all trained models, relate excess one-step NLL (and held-out-intervention NLL) to structural accuracy; report pairs with matched NLL but different accuracy.
* **H2** discovery objective (instance-contrastive invariance, ICI, λ=1) vs prediction-only: 2×2 factorial {RSSM, det-GRU} × {pred, ICI}, equal data (two views per instance in both arms), equal steps, equal parameters. Primary: ID accuracy difference per architecture, pooled over 3 training seeds; effect counted only if CI over test instances excludes 0 AND sign agrees in ≥2/3 seeds.
* **H3** active experimentation: compare conditions passive / uniform / sweep(heuristic) / randblock / oracle_eig / ens_disagree at identical interaction budget (48 steps); same noise realisation per instance across conditions (paired).
* **H4** epistemic limits: claim rates on eqA / eqB for probes trained on identifiable only vs probes trained with eqA labelled as ambiguous; transfer of abstention to eqB (unseen equivalence family). Baselines: oracle, GBM, supervised GRU.
* **H5** family transfer: det-GRU trained on one family only (A or B), probed on the other; compare with model trained on both and with an untrained random-init network (probe control). Single seed per cell → exploratory.

## 3. Pre-stated decision rules

1. A world-model-specific structural claim is retained only if it beats BOTH the untrained-network probe and the hand-feature GBM control under the same condition.
2. "Discovery objective helps" requires H2 primary rule above; otherwise reported as not supported.
3. "Learned planner helps" requires ens_disagree > randblock with non-overlapping 95% CI over instances for ≥2 of the 4 cells; otherwise reported as not supported.
4. Oracle reference: two oracles are reported — broad-grid (knows equivalence structure; misspecified prior) and prior-matched (in-distribution only). Accuracy comparisons against "oracle" use the matched one; the broad one is the epistemic-reliability reference.
5. All dev-stage choices already made from namespace 9300 (λ selection rule, RSSM prior-predictive fix) are disclosed in the results README.

## 4. Known limitations stated in advance

Toy 1-D generators with deterministic latent dynamics; hypothesis classes are shared between train and test (except family/parameter/noise holdouts); only 3 training seeds per cell; instances are the independence unit for test statistics and training seeds are reported separately; MLP/GRU capacity small; no DreamerV3/TD-MPC2 reproduction.
