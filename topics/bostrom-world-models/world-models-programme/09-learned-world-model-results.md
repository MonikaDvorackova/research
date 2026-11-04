# 09 — Learned latent world models and structural discovery: development results

Scope: development experiments only (instance namespace 9200 test, 9300 model-selection; no confirmatory seed range touched). Plan fixed beforehand in `07-…plan.md`. Code: `implementations/epistemic-identifiability/src/eid/gwb/`, scripts `scripts/gwb_*`, results `results/gwb_dev/`, `results/gwb_final/`. Numbers below are copied from `results/gwb_final/eval_main_summary.txt` and the transfer summaries. Unless stated, "±" is the SD over **3 training seeds**; each seed is evaluated on the same 800 identifiable test instances (instance-level 95 % CI for one accuracy ≈ ±0.03). Instances are the independence unit; the seed count is small.

## 1. What was built and trained

* Benchmark `gwb`: families **A** (hidden precision: continuous / quantised / stiction), **B** (hidden memory: pure delay / ordinary actuator lag / periodic reset), **E** (exactly equivalent worlds: `eqA` quant≈stiff beyond actuator reach; `eqB` delay≥horizon vs reset period 1; unit-tested x≡0). Families D (latent causal) and F (nested worlds) **not implemented**.
* Models (CPU, PyTorch 2.15, H=128): **RSSM-style** (GRU deterministic state + 8-d stochastic latent, prior/posterior, KL balancing 0.8/0.2, free bits 0.1, plus a *prior-predictive loss* — a deviation from Dreamer, see §6); **deterministic GRU latent dynamics** (comparator; ablates the stochastic latent); **ICI discovery variant** (instance-contrastive invariance: InfoNCE between end-of-sequence states of two independent interaction sequences/noise of the same generator instance, no class labels, λ=1, both arms use both views for prediction → equal data and steps); supervised GRU classifier (control); untrained random-init nets (control). Not DreamerV3 or TD-MPC2.
* Training: 3000 steps, batch 128 instances × 2 views × 48 steps, Adam 1e-3. 12 factorial runs (2 architectures × {pred, ICI} × seeds 1–3), 4 family-holdout runs, 2 untrained, 1 classifier. Wall-clock under 4 concurrent jobs: det ≈ 240–270 s, RSSM ≈ 460–510 s per run; evaluation 6 conditions ≈ 6 min. All CPU; a GRU microbenchmark showed MPS no faster than CPU at H=64 (≈0.007 s/iter both) and ≈4× faster only at H=256, so MPS was not used.
* Readout: logistic probe on the end-of-sequence summary state, trained per (model, interaction condition) on 1500 labelled instances (probe namespace 9100), tested on held-out instances. Interaction conditions (48 steps, identical noise draw per instance across conditions): passive, uniform random, heuristic **sweep** (amplitude ramp, not in the training action mixture; designed with knowledge of the dead-zone mechanism), random 8-step blocks, **exact-Bayes EIG** planner (oracle), **ensemble-disagreement** planner (learned, 3 seeds).
* Tests: 15 new tests (`tests/test_gwb.py`: equivalence, oracle non-claiming on equivalent worlds, EIG>passive, shared noise, no label leakage through the interface, model shapes/gradients, InfoNCE, deterministic batches, resume-equals-uninterrupted, quiescence counterexample, ECE/probe utilities). Full suite **328 passed** (313 earlier + 15).

## 2. Predictive performance (excess one-step prior-predictive NLL over noise floor; 90 % interval coverage; 16-step rollout RMSE/σ)

| model | uniform excess NLL | sweep (held-out interventions) | cover90 | rollout16/σ (uniform) |
|---|---|---|---|---|
| det-GRU pred | 0.103±0.003 | 0.138±0.003 | 0.905 | 0.41 |
| det-GRU ICI | 0.112±0.005 | 0.162±0.009 | 0.904 | 0.45 |
| RSSM pred | 0.265±0.014 | 0.311±0.010 | 0.771 | 0.44 |
| RSSM ICI | 0.337±0.052 | 0.378±0.059 | 0.744 | 0.41 |
| untrained | ≈1.1–1.2 | ≈1.2–1.25 | ≈1.0 | 1.2–1.3 |

The deterministic GRU is the better, better-calibrated predictor; RSSM intervals are overconfident (coverage 0.74–0.77 vs nominal 0.90). Sweep (held-out intervention programme) costs every model ≈0.04–0.05 nats more than uniform.

## 3. Structural discovery (mechanism-class accuracy, 6-way, identifiable ID test; chance 0.167)

| condition | det pred | det ICI | RSSM pred | RSSM ICI | untrained det | hand-feature GBM | supervised GRU | oracle (broad grid) | oracle (prior-matched) |
|---|---|---|---|---|---|---|---|---|---|
| passive | .565±.017 | .559±.010 | .545±.005 | .557±.002 | .316 | .455 | .601 | .661 | .681 |
| uniform | .596±.008 | .594±.011 | .595±.009 | .606±.006 | .359 | .556 | .660 | .726 | .756 |
| sweep (heuristic) | .845±.003 | .837±.004 | .831±.012 | .847±.007 | .660 | .790 | .777 | .828 | .853 |
| random blocks | .636±.018 | .640±.005 | .622±.014 | .660±.007 | .340 | .618 | .741 | .810 | .835 |
| exact-EIG (oracle planner) | .753±.004 | .760±.012 | .752±.017 | .768±.007 | .455 | .701 | .796 | .920 | .936 |
| ens. disagreement (own ensemble) | .696±.017 | .680±.007 | .672±.002 | .646±.002 | invalid† | .744/.680/.641/.644 | — | ≈.79–.82 | ≈.80–.86 |

† An ensemble of size one has zero variance and degenerates to a constant −1 action; the two `ens_disagree[*_untrained]` rows in the raw file are **not valid** results.

Held-out structure (columns of the raw summaries): held-out parameter ranges (`hoparam`) are read out roughly as well as in-distribution (sweep 0.80–0.82 vs 0.83–0.85); held-out noise (`hosigma`, σ∈[0.3,0.4] vs training [0.08,0.2], ×2.5 for family B) falls to 0.17–0.39 for all learned models (oracle 0.67). Calibration (ECE, identifiable set): 0.02–0.03 under sweep/EIG, 0.05–0.08 under passive/uniform/random; the GBM control is badly miscalibrated (ECE 0.16–0.39).

## 4. Hypothesis-by-hypothesis assessment (against the pre-stated rules)

* **H1 (predictive ≠ structural): partly supported, not cleanly.** (a) det-GRU has 2.5× smaller excess NLL and far better calibration than RSSM, yet structural accuracy is the same in every condition (e.g. uniform .596 vs .595, EIG .753 vs .752) → large predictive differences, no structural difference. (b) ICI costs a little prediction (sweep NLL .162 vs .138 for det) with no ID structural change but a consistent change on shifted noise (below). No pair with *matched* predictive performance and a *large* structural gap was found. Mathematical reading: P3 in `08`.
* **H2 (discovery objective helps): not supported on the pre-stated primary outcome.** ID accuracy differences ICI−pred: det −0.008…+0.007 (no effect); RSSM +0.011…+0.038, positive in all five conditions (largest: random blocks .660 vs .622, ≈1.5 SE of one accuracy estimate). The sign is consistent for RSSM but the magnitude is ≤0.04 and **no paired instance-level test was run**, so the pre-stated rule (CI excluding 0 and sign in ≥2/3 seeds) is not verified; treat as a small, unconfirmed possible RSSM-specific effect. **Post-hoc, exploratory:** held-out-noise accuracy is higher for ICI than pred in all 10 architecture×condition cells with seed-level SDs well below the gap in the larger ones (sweep: RSSM .361±.019 vs .265±.035; det .367±.032 vs .287±.004; EIG: .385 vs .291; the smallest gap is +0.002, det/passive). Not a pre-stated outcome; requires a confirmatory test and a mechanism check (e.g. InfoNCE promotes invariance to the noise level through variation of σ across view pairs — σ is shared within a pair, so this is not trivially explained).
* **H3 (learned active experimentation): not supported against the strong heuristic; weakly above random.** Ensemble disagreement beats random blocks by 0.04–0.06 in 3 of 4 cells (rssm pred .672 vs .622; det pred .696 vs .636; det ICI .680 vs .640; RSSM-ICI −0.014) with overlapping 95 % intervals → pre-stated rule 3 **not met**. It is far below the hand-designed amplitude sweep (.83–.85), and below exact-EIG planning read out by the same models (.75–.77). The data it collects is about as informative to the exact oracle (≈.79–.82) as random blocks (.81). Caveat: the sweep heuristic encodes designer knowledge of the dead-zone mechanism.
* **H4 (recognising epistemic limits): negative for ordinary probes, partial for exposure-trained probes.** On equivalent worlds, probes trained on identifiable instances make a confident claim (max prob ≥ 0.8) on **43–97 % of `eqA`** and **19–73 % of `eqB`** instances (every one unsupported, all conditions); the hand-feature GBM and the supervised GRU claim 71–100 % / 21–94 %. The exact-Bayes oracle claims 0–6 %. Untrained nets also "abstain" (≈0–4 % claims) because their features are uninformative, not because they understand non-identifiability. A probe trained with `eqA` labelled as ambiguous reduces the in-distribution claim rate to ≈0.0–0.01 but on the **unseen equivalence family `eqB` still claims 15–40 %** (best case .15 passive; ≈.30 sweep) — abstention only partly transfers. Exposure to ambiguity is a training-distribution intervention, not evidence of a model of identifiability. P1 (`08`) shows no procedure can exceed accuracy ½ on these pairs.
* **H5 (transfer across families), single seed, exploratory.** Probing family B (delay/lag/reset), uniform actions: trained on A only .69–.70, B only .80–.81, both .78–.80, untrained .49 → a family-A-trained model carries substantial *unseen-family* structure (+0.2 over random weights) but less than a B-trained one (−0.1). Probing family A: A-only .45–.48, B-only .46–.48, both .46–.52, untrained .40; under sweep A-only .77–.79 ≈ B-only .77–.79 > untrained .60 → the benefit is mostly generic input-output system identification, **not family-specific structure**. Families share the same first-order base dynamics and noise, so this is not a test of truly unrelated mechanisms.

## 5. Adversarial controls

* Label leakage: actions-only classifier at chance (0.15–0.19) for non-adaptive policies; 0.41–0.57 for adaptive planners — expected because planner actions depend on beliefs inferred from observations (information, not leakage). Test shows interaction and model signatures are independent of labels/family.
* A simple classifier does **not** solve the task under weak interventions (GBM .46–.62 vs oracle .66–.81) but nearly matches the learned probes under the sweep (.79 vs .83–.85).
* Random-init recurrent nets are non-trivially informative (sweep .66, EIG .46, uniform .36) — the probe must be compared with them; trained gains (det-GRU) are +0.18 (sweep) to +0.30 (random blocks, EIG).
* Predictive accuracy does not explain the effect: models with 2.5× different NLL read out identically.
* Overconfidence on equivalent worlds: confirmed (H4). Benchmark neither trivial (passive oracle .66) nor impossible (EIG oracle .92; sweep .83).
* Supervised end-to-end GRU is **not** an upper bound here (sweep .777 < world-model probe .845): it was trained for 2500 steps on the training action mixture only.

## 6. Failed / revised runs (kept)

* `results/gwb_dev/eval_dev_ns9300_FIRST_rssm_without_prior_loss.json` and `runs/failed_v1/`: first RSSM decoded from the posterior and scored with prior-mean predictions had excess NLL ≈390 and 7 % coverage (it autoencoded noise). Fixed by adding the prior-predictive loss; reported as a model defect, evaluated on predictive metrics, not chosen from structural outcomes. The λ=1.0 choice for ICI was fixed from the first dev run by a stated rule (higher mean accuracy over four conditions than λ=0.3: 0.680 vs 0.667) before the fix and retained.
* A zsh word-splitting bug created a malformed run name in the dev grid (`dev2__s100`); removed before use.
* The `ens_disagree[*_untrained]` rows (ensemble of one) are invalid.
* Initial brief-level σ choices: noise levels were set from the oracle's accuracy table (not from learned-model results).

## 7. What is and is not established

Established (development-level, toy generators): learned recurrent latents trained only on prediction carry mechanism information that a linear probe can read out at the level of a prior-matched Bayesian oracle when the intervention is well chosen (sweep: 0.84 vs 0.85) and well below it when interventions are weak (uniform .60 vs .76) or chosen by an exact planner not matched to the training mixture (.75 vs .94); this is consistent with meta-learning-as-Bayes-filtering (AB-level reading only). Predictive quality and structural readout dissociate. Ordinary learned discovery heads are overconfident on exactly equivalent worlds.
Not established: that the ICI objective helps (primary outcome failed); that learned-ensemble planning beats a simple designed heuristic; any transfer to genuinely independent mechanisms; any statement about Dreamer/TD-MPC at scale, latent causal variables or nested worlds; any link beyond levels 1–4 of the inference hierarchy.
