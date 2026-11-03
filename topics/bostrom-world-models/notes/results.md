---
id: topic-bostrom-world-models-results
title: "Proof-of-concept results and limits"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [results, evaluation]
---

## Proof-of-concept results

Everything here comes from executed runs in `implementations/epistemic-identifiability/results/` (`poc_v1`, `poc_v2`; 10 seeds each; 41 automated tests pass; v2 reproduces all 720 v1 rows exactly in the shared columns). Full tables are in each `summary.md`. Numbers below are means over seeds with the bootstrap 95% interval over seeds in brackets, copied from those tables. This is a **small toy study**; it is not evidence about the physical universe, about consciousness, or about Bostrom's trilemma.

### Status of the run history

- `poc_v1` was run first with controls E0, E0split, Ealt.
- Reading it showed that Ealt did not test the intended point (its discrepancy profile differs from W's: it deviates in-distribution, W mainly outside it). The control `AltOOD` (real, non-learned mismatch that vanishes for |a| ≤ 1, matched to W's KL under wide interventions) was then added **post hoc** and the whole configuration re-run as `poc_v2`. v1 is kept unchanged. The AltOOD results are therefore exploratory.

### Findings

**F1. In-distribution (passive) interventions: calibrated test, no power.** The α = 0.05 test of consistency with the agent's theory Q has false-positive rate 0.050 [0.043, 0.055] at T = 2 and 0.070 [0.056, 0.084] at T = 50 on the negative controls. For W trained on at least 500 transitions its power is close to the nominal level: for quality 3 (12,500 transitions) TPR is 0.056 at T = 2 and 0.092 [0.055, 0.143] at T = 50, and AUROC ≈ 0.5 (0.516 [0.479, 0.567] at T = 50). The oracle likelihood-ratio AUROC for the same trajectories is 0.884 [0.858, 0.910] at T = 50. So the information to discriminate exists, but the agent's test, which has only its own estimated theory, cannot use it. Only the poorest model (quality 0, 100 transitions, true in-distribution KL ≈ 9 nats/step) is detected: AUROC 0.750 [0.646, 0.859] at T = 50; 5 of 10 seeds reach AUROC 0.8 within T ≤ 50 (median T = 20).

**F2. Out-of-distribution interventions invert the test.** Under `wide` interventions the false-positive rate on the *true* environment rises from 0.443 at T = 2 to 0.883 at T = 10 and 1.000 at T = 50; under `active` interventions it is 1.000 at every horizon. At the same time W is rejected rarely (quality 3, wide, T = 10: TPR 0.070, vs 0.883 for E0 and E0split and 0.862 for AltOOD). AUROC of W vs the negative controls therefore falls to 0.056 [0.049, 0.064] at T = 10 (quality 3, wide) and to about 0 at larger T: the agent treats the learned model as *more* consistent with its theory than the real environment. This is the behaviour Proposition 6 allows (false alarms bounded by α + TV(E0, Q)) and the situation of Proposition 3(b).

**F3. The information is available to an oracle.** Oracle AUROC is 1.000 for `wide` and `active` at T ≥ 10 for all qualities. Oracle information gain per step (mean log-likelihood ratio on W trajectories) is 0.03–0.15 nats under passive, 5.5–6.5 under wide, and 32–42 under active for qualities 1–3. Active selection (maximum ensemble disagreement) thus finds interventions with very large true divergence, and does not help the agent's own test, because its null model is misspecified exactly there.

**F4. No implementation artifact is exploited.** AUROC between E0 and E0split (identical law, different noise mechanism) is between 0.49 and 0.51 in every cell, with every interval containing 0.5 at T ≥ 5 (checked by reading the `poc_v1` `summary.md` table). The negative control is observationally equivalent (Proposition 1) and the statistic does not separate it.

**F5. The score tracks the size of the divergence in the probed region, not the provenance of the discrepancy.** Under `wide` and `active` interventions the baseline statistic flags the real, non-learned mismatches Ealt and AltOOD as readily as, or more readily than, W (quality 3, wide, T = 10: TPR 0.862 for AltOOD, 0.070 for W). Under passive interventions at qualities ≥ 1, W and AltOOD both coincide with E0 and are not separated (AUROC W vs AltOOD 0.505 [0.487, 0.521] at T = 2, quality 3; 0.519 [0.485, 0.566] at T = 50). The Phase 3 ablations (below) show that with a well-specified theory the statistic *does* rank W above AltOOD under adaptive probing. That ranking is not identification of a learned model: the controls were matched only in mean KL under uniform wide actions, and an adaptive policy probes exactly where W's error is largest. The experiment cannot test identification of a mechanism, and this study does not claim to (see Proposition 1, Corollary 1).

**F6. Calibration is not informative here.** ECE after Platt scaling is small (mostly below 0.07; up to 0.13 for the smallest model under active interventions), but the Brier score under passive interventions at quality 3, T = 50 is 0.219, near the uninformative value 0.25. Low ECE here reflects scores that carry little information, not useful probabilities.

### Pre-stated expectations (from `experiment-design.md`) against outcomes

| # | Expectation | Outcome |
|---|---|---|
| 1 | Power rises with worse W and longer T | Supported for passive and for quality 0; not for quality ≥ 1 under OOD (inverted) |
| 2 | FPR above 0.05 for OOD interventions | Supported, strongly (up to 1.000) |
| 3 | E0 vs E0split AUROC ≈ 0.5 | Supported |
| 4 | W vs matched real mismatch may be near 0.5 | Not supported for Ealt (separated, but in the "W looks less anomalous" direction); supported only under passive interventions for AltOOD (a trivial case, since both match E0 there) |
| 5 | Active may or may not beat wide | Active gives far more oracle information but does not improve the agent's detection; it raises FPR to 1.000 |

### Hypothesis from Phase 2, now tested in part

Phase 2 conjectured that the inversion arises because W and Q are learned from similar data with the same architecture. The ablations below test this (see "Phase 3 ablations").

### Limitations

- Toy, fully observed, low-dimensional environment; no partial observability (POMDP) and no learned latent states.
- Q and W share architecture and training distribution (one family), and Q is trained on the reference. The agent has a theory built from the reference, which a real embedded agent would not.
- The test uses only squared standardised residuals; no tuned detector, no other statistic, no hyperparameter search, no architecture ablation. Ablations are limited to quality levels, policies, and horizons.
- "Active" is an uncertainty-based proxy for expected information gain, not an exact EIG policy.
- Ealt and AltOOD are matched in mean KL under wide interventions only; AltOOD was added after seeing v1.
- Ten seeds; intervals are bootstrap over seeds and ignore episode-level variance within a seed. KL values for the smallest model are heavy-tailed.
- Calibration uses labelled episodes on the experimenter side.
- The results illustrate Propositions 3(b) and 6 and do not validate them (they are proved separately); nothing here supports or tests thesis T1–T3 beyond illustration.


## Phase 3 ablations

Configurations: `configs/abl_*.yaml`; outputs `results/abl_*/` (10 seeds each, quality levels and horizons as in the baseline). W, the controls, the seeds and all random streams are identical across conditions (the `quality.csv` files are identical), so only the agent's theory differs. Full cross-condition tables: `implementations/epistemic-identifiability/results/comparison.md` (generated by `python -m eid.compare`). The table below is quality 3 (W trained on 12,500 transitions). Mean over seeds [bootstrap 95% CI over seeds].

| Condition | FPR passive T=50 | FPR wide T=10 | FPR wide T=50 | FPR active T=50 | TPR on W, wide T=10 | AUROC W vs controls, wide T=10 | AUROC, active T=10 |
|---|---|---|---|---|---|---|---|
| Baseline: tanh-64 ensemble trained on a ∈ [−1, 1] | 0.070 | 0.883 | 1.000 | 1.000 | 0.070 | 0.056 [0.049, 0.064] | 0.000 |
| A1: ReLU-128×3 ensemble, same data | 0.092 [0.074, 0.112] | 0.974 [0.967, 0.981] | 1.000 | 1.000 | 0.736 [0.681, 0.793] | 0.114 [0.092, 0.139] | 0.010 [0.001, 0.026] |
| A2: cubic polynomial (different model class) | 0.052 [0.048, 0.057] | 0.579 [0.355, 0.786] | 0.747 [0.489, 0.995] | 0.900 [0.700, 1.000] | 0.974 [0.955, 0.989] | 0.948 [0.924, 0.968] | 1.000 |
| C: tanh-64 ensemble trained on a ∈ [−3, 3] | 0.082 [0.063, 0.101] | 0.050 [0.044, 0.055] | 0.071 [0.061, 0.081] | 0.198 [0.132, 0.274] | 0.968 [0.962, 0.973] | 0.985 [0.981, 0.989] | 0.989 [0.975, 1.000] |
| B: analytic true law (actions chosen by learned-ensemble disagreement) | 0.050 [0.045, 0.054] | 0.049 [0.042, 0.056] | 0.049 [0.044, 0.055] | 0.048 [0.040, 0.055] | 0.972 [0.964, 0.979] | 0.989 [0.985, 0.992] | 1.000 |

### Findings from the ablations

**G1. Active detection is not intrinsically defective; the failure comes from the agent's theory outside its training coverage.** With the exact law as the agent's theory (B), the test is calibrated for every policy and horizon (FPR 0.048–0.055 in the cells shown; 0.042–0.056 across all 36 quality-0 and quality-3 cells of the summary) and active interventions detect W perfectly from T = 5 (AUROC 1.000 for quality 3, and for quality 0). The same is true when the theory is learned with actions covering the probed range (C): FPR 0.050 [0.044, 0.055] under wide interventions at T = 10, AUROC 0.985. Calibration under C degrades for the longest active horizon (FPR 0.198 [0.132, 0.274] at T = 50), which I attribute to residual extrapolation error at the extremes of the range; I did not test this.

**G2. The inversion is not an artifact of sharing one architecture.** A ReLU, deeper, wider theory trained on the same in-distribution data (A1) reproduces the failure: FPR 0.974 [0.967, 0.981] under wide interventions at T = 10 and AUROC against the negative controls 0.114 [0.092, 0.139], falling to about 0 at longer horizons.

**G3. A different model class removes the inversion but not the false alarms.** The polynomial theory (A2) ranks W far above the negative controls (AUROC 0.948 [0.924, 0.968] at wide T = 10; 1.000 under active) while still rejecting the *true* environment in 58% to 90% of episodes (wide T = 10 and active T = 50 respectively), with large seed-to-seed spread (per-seed FPR at wide T = 10, quality 3: 0.03 to 0.97). Ranking and calibration come apart: the score can order environments correctly while the α = 0.05 test is unusable.

**G4. In-distribution (passive) detection is limited by information, not by the theory.** Even with the exact theory (B) the passive AUROC of W (quality 3) at T = 50 is only 0.591 [0.537, 0.652] (TPR 0.151 [0.089, 0.237]); the oracle on the same trajectories reaches 0.884. All conditions agree to within noise on the oracle (it does not depend on the theory).

**G5. Probable cause, with limits.** Taken together: what restores detection is that the agent's theory is correct (B) or has been trained over the intervention range later used (C); changing architecture inside the neural family (A1) does not help; changing model class (A2) helps ranking only. Training-range coverage is therefore the best-supported explanation of the failure (consistent with Proposition 3(b) and Proposition 6). The evidence is for one environment, one learned-world-model architecture for W, and 10 seeds; the shared-inductive-bias explanation for the *size* of the inversion in the neural conditions is untested directly because W's architecture was not varied.

**G6. Reading of the AltOOD control under better theories.** With theories that work (B, C, A2), the statistic ranks W above AltOOD under adaptive probing (quality 3, active T = 10: AUROC W vs AltOOD 1.000 under B, 0.886 under C, 1.000 under A2; wide T = 10: 0.785, 0.772, 0.860). As noted under F5 this reflects larger divergence in the probed region, not recognition of a learned model.

**G7. Negative control.** In all five conditions the seed-averaged AUROC between E0 and E0split lies in [0.482, 0.513] (per-seed values reach ±0.09 with 400 episodes, as expected from sampling noise; the standard error of one AUROC is roughly 0.03).

### Reproducibility checks

- 45 automated tests pass (including a golden-output test that the refactor for ablations leaves the default path bit-identical).
- `scripts/reproduce_check.py` re-ran seed 0 of all five conditions at full configuration: 72 rows each, 0 mismatches (tolerance 1e-9) against the stored CSVs.
- v2 reproduces v1 exactly in all shared columns (0 of 720 rows differ).

### Additional limitations from the ablations

- One environment family and one W architecture. Whether the pattern holds for partially observed, high-dimensional, or discrete worlds is not tested.
- Condition C gives the agent experience (training data) in the very regime it later probes. For an embedded observer this corresponds to having already experienced the reference regime; that is the "reference premise" and is precisely what an observer lacks for regimes it has never visited.
- Condition B gives the agent the true law; this is an upper bound, not a realistic observer.
- Condition A2's FPR has very wide intervals; ten seeds do not characterise its variance well.
