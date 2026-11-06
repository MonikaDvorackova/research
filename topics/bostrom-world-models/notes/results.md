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

**F6. Calibration: read the agent-side measure, not the experimenter-side one.** The agent-side measure of calibration is how the realised false-positive rate compares with the nominal α = 0.05 (the tables above). The ECE and Brier values in `summary.md` come from Platt scaling fitted on *labelled* calibration episodes by the experimenter; Platt scaling can learn a negative slope, so where the score is inverted (AUROC about 0) it recalibrates the inversion and reports near-perfect ECE and Brier (for example Brier 0.000 at AUROC 0.000). That recalibration is unavailable to the agent, which has no labels and does not know the sign. ECE and Brier are therefore meaningful only in cells where AUROC is above 0.5; in the passive cells, where they are meaningful, Brier is 0.219 at quality 3, T = 50, near the uninformative 0.25. (The statement in an earlier draft that low ECE reflected uninformative scores was incomplete: in inverted cells it reflects exploited inversion.)

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


## Phase 4: independent observers, adaptive observer, statistics, mechanism

Status of analyses. **Confirmatory in the sense of fixed specification before the new data**: the configurations of `abl_qindep`, `abl_wrelu_qtanh`, `abl_wrelu_qrelu` and `adaptive_tanh`, the practical-significance thresholds (0.10 for AUROC, 0.05 for rates; fixed in `eid/stats.py` before the results of these four conditions were inspected), and the metrics. **Exploratory**: AltOOD (post hoc, Phase 2), the mechanism check, and every reading offered below. No hypothesis in this study was pre-registered externally.

### Conditions

| Condition | Directory | What differs from the baseline |
|---|---|---|
| Independently trained observer | `abl_qindep` | Theory trained on a fresh, independent sample of E0 data (new random stream), same architecture. |
| W = ReLU, theory tanh | `abl_wrelu_qtanh` | World model W is ReLU-128x3 (second W architecture); theory as baseline, so architectures differ. |
| W = ReLU, theory ReLU | `abl_wrelu_qrelu` | Both ReLU-128x3: architectures shared. |
| Adaptive observer | `adaptive_tanh` | Before testing, the observer interacts with the environment under test for 100 episodes of 10 steps with the same policy it will use, then fine-tunes a copy of its theory for 300 steps on those 1,000 transitions plus a 2,000-transition replay of its reference data. It then tests on fresh episodes (adaptation, calibration and test episodes use disjoint random streams). |

Together with the Phase 3 conditions (ReLU theory, polynomial theory, theory trained over the probed range, analytic theory) and the baseline, the grid has nine observers. World-model quality is 3 (12,500 transitions) in the tables below; all four qualities are in the stored `metrics.csv` files and `summary.md`. Figure: `results/figures/observer_comparison.png`. Paired statistics: `results/stats.md`. Full tables: `results/comparison.md`.

**passive interventions, T = 50** (world model quality 3; mean over 10 seeds [bootstrap 95% CI])

| Observer | FPR (alpha=0.05) | FNR on W | Balanced accuracy | AUROC, W vs controls |
|---|---|---|---|---|
| Fixed observer, tanh theory trained on a in [-1,1] (baseline) | 0.070 [0.056, 0.084] | 0.908 [0.857, 0.945] | 0.511 [0.492, 0.538] | 0.516 [0.479, 0.567] |
| Independently trained: fresh E0 sample, same architecture | 0.064 [0.054, 0.074] | 0.905 [0.861, 0.940] | 0.515 [0.499, 0.535] | 0.532 [0.497, 0.577] |
| ReLU-128x3 theory | 0.092 [0.074, 0.112] | 0.748 [0.655, 0.826] | 0.580 [0.541, 0.626] | 0.619 [0.569, 0.681] |
| World model W = ReLU; theory tanh (architectures differ) | 0.070 [0.056, 0.084] | 0.892 [0.855, 0.924] | 0.519 [0.503, 0.539] | 0.536 [0.508, 0.569] |
| World model W = ReLU; theory ReLU (architectures shared) | 0.092 [0.074, 0.112] | 0.793 [0.724, 0.858] | 0.557 [0.523, 0.594] | 0.598 [0.546, 0.649] |
| Cubic-polynomial theory (different model class) | 0.052 [0.048, 0.057] | 0.838 [0.743, 0.905] | 0.555 [0.521, 0.603] | 0.592 [0.533, 0.661] |
| Theory trained over the probed range a in [-3,3] | 0.082 [0.063, 0.101] | 0.901 [0.852, 0.939] | 0.509 [0.486, 0.536] | 0.507 [0.452, 0.564] |
| Analytic true-law theory | 0.050 [0.045, 0.054] | 0.848 [0.763, 0.911] | 0.551 [0.519, 0.594] | 0.591 [0.537, 0.652] |
| Adaptive observer: fine-tunes the tanh theory on 1,000 of its own transitions | 0.055 [0.049, 0.061] | 0.918 [0.891, 0.941] | 0.514 [0.500, 0.529] | 0.538 [0.510, 0.573] |

**wide interventions, T = 10** (world model quality 3; mean over 10 seeds [bootstrap 95% CI])

| Observer | FPR (alpha=0.05) | FNR on W | Balanced accuracy | AUROC, W vs controls |
|---|---|---|---|---|
| Fixed observer, tanh theory trained on a in [-1,1] (baseline) | 0.883 [0.868, 0.897] | 0.930 [0.919, 0.941] | 0.093 [0.084, 0.103] | 0.056 [0.049, 0.064] |
| Independently trained: fresh E0 sample, same architecture | 0.865 [0.815, 0.902] | 0.916 [0.904, 0.927] | 0.109 [0.095, 0.130] | 0.064 [0.045, 0.092] |
| ReLU-128x3 theory | 0.974 [0.967, 0.981] | 0.264 [0.207, 0.319] | 0.381 [0.354, 0.408] | 0.114 [0.092, 0.139] |
| World model W = ReLU; theory tanh (architectures differ) | 0.883 [0.868, 0.897] | 0.896 [0.854, 0.935] | 0.110 [0.088, 0.132] | 0.086 [0.063, 0.111] |
| World model W = ReLU; theory ReLU (architectures shared) | 0.974 [0.967, 0.981] | 0.718 [0.651, 0.786] | 0.154 [0.119, 0.187] | 0.026 [0.019, 0.033] |
| Cubic-polynomial theory (different model class) | 0.579 [0.355, 0.786] | 0.026 [0.011, 0.046] | 0.698 [0.600, 0.804] | 0.948 [0.924, 0.968] |
| Theory trained over the probed range a in [-3,3] | 0.050 [0.044, 0.055] | 0.033 [0.027, 0.039] | 0.959 [0.955, 0.963] | 0.985 [0.981, 0.989] |
| Analytic true-law theory | 0.049 [0.042, 0.056] | 0.029 [0.022, 0.036] | 0.961 [0.957, 0.965] | 0.989 [0.985, 0.992] |
| Adaptive observer: fine-tunes the tanh theory on 1,000 of its own transitions | 0.055 [0.048, 0.063] | 0.940 [0.929, 0.951] | 0.503 [0.496, 0.509] | 0.491 [0.473, 0.508] |

**active interventions, T = 10** (world model quality 3; mean over 10 seeds [bootstrap 95% CI])

| Observer | FPR (alpha=0.05) | FNR on W | Balanced accuracy | AUROC, W vs controls |
|---|---|---|---|---|
| Fixed observer, tanh theory trained on a in [-1,1] (baseline) | 1.000 [1.000, 1.000] | 0.877 [0.809, 0.921] | 0.062 [0.040, 0.096] | 0.000 [0.000, 0.000] |
| Independently trained: fresh E0 sample, same architecture | 1.000 [1.000, 1.000] | 0.915 [0.887, 0.936] | 0.042 [0.032, 0.056] | 0.000 [0.000, 0.000] |
| ReLU-128x3 theory | 1.000 [1.000, 1.000] | 0.230 [0.059, 0.432] | 0.385 [0.284, 0.470] | 0.010 [0.001, 0.026] |
| World model W = ReLU; theory tanh (architectures differ) | 1.000 [1.000, 1.000] | 0.681 [0.534, 0.827] | 0.160 [0.086, 0.233] | 0.000 [0.000, 0.000] |
| World model W = ReLU; theory ReLU (architectures shared) | 1.000 [1.000, 1.000] | 0.387 [0.212, 0.571] | 0.307 [0.215, 0.394] | 0.000 [0.000, 0.000] |
| Cubic-polynomial theory (different model class) | 0.832 [0.597, 1.000] | 0.000 [0.000, 0.000] | 0.584 [0.500, 0.701] | 1.000 [1.000, 1.000] |
| Theory trained over the probed range a in [-3,3] | 0.065 [0.057, 0.073] | 0.021 [0.000, 0.049] | 0.957 [0.945, 0.967] | 0.989 [0.975, 1.000] |
| Analytic true-law theory | 0.055 [0.050, 0.060] | 0.000 [0.000, 0.000] | 0.973 [0.970, 0.975] | 1.000 [1.000, 1.000] |
| Adaptive observer: fine-tunes the tanh theory on 1,000 of its own transitions | 0.137 [0.074, 0.202] | 0.911 [0.869, 0.945] | 0.476 [0.438, 0.513] | 0.432 [0.369, 0.497] |

### Findings

**H1. The central finding survives independent architectures, independent training samples, and a second world-model architecture.** All four in-distribution-trained neural theories fail under out-of-distribution interventions: the baseline, an independent sample of E0 data (AUROC 0.064 at wide T = 10, against 0.056 for the baseline; difference +0.008 [−0.010, +0.033], Holm p = 1.0), the ReLU theory (0.114), and the 2×2 grid of world-model and theory architectures (W tanh/theory tanh 0.056; W tanh/theory ReLU 0.114; W ReLU/theory tanh 0.086; W ReLU/theory ReLU 0.026, all at wide T = 10). Architectures shared or different between W and the theory do not change the outcome: AUROC is far below 0.5 in all four cells, and the differences between cells (at most 0.09) are below the practical threshold of 0.10. The sample of E0 data used to train the theory does not matter. Condition-independent sanity check: the false-positive rates of "W = ReLU, theory tanh" are *identical* to the baseline's, and those of "W = ReLU, theory ReLU" identical to the ReLU-theory condition's, as they must be, because false positives are measured on the negative controls with the theory alone; W cannot influence them, which also shows that W and the control statistics are not coupled.

**H2. Adaptive experimentation does not improve identifiability in this setting; it removes false alarms and the power to detect together.** The adaptive observer's false-positive rate falls to 0.055 [0.048, 0.063] at wide T = 10 (baseline 0.883) and its balanced accuracy is 0.503 [0.496, 0.509]: **chance**. AUROC against the controls is 0.491 [0.473, 0.508] at wide T = 10, 0.432 [0.369, 0.497] at active T = 10, and 0.329 [0.195, 0.488] at active T = 50 (below 0.5 and unstable). The large improvement over the baseline in balanced accuracy (+0.409) and AUROC (+0.435) is an improvement over a *systematically wrong* observer (below chance because inverted); it is not detection. After adaptation, its theory has been fitted to whatever environment it faces, E0 or W, so its residuals no longer separate them. This is what Proposition 8(c) predicts. Under active adaptation the false-positive rate is still elevated (0.137 [0.074, 0.202] at T = 10; 0.468 [0.296, 0.654] at T = 50): 1,000 adaptation transitions did not cover the extremes the active policy probes, so adaptation was incomplete there.

**H3. Observers that detect do so because their theory is correct or covers the probed range.** The analytic theory and the theory trained over the probed range reach AUROC 0.985–1.000 with balanced accuracy 0.96–0.97 in the wide T = 10 and active T = 10 cells shown (0.90–0.98 across the longer-horizon cells in `comparison.md`). The polynomial theory ranks W well (AUROC 0.948 at wide T = 10) but with unusable calibration: balanced accuracy 0.698 [0.600, 0.804] at wide T = 10 because its false-positive rate is 0.579 [0.355, 0.786].

**H4. Passive (in-distribution) interventions detect nothing for any observer at this quality.** Balanced accuracy 0.51–0.58 and AUROC 0.51–0.62 for all nine observers at passive T = 50. With the analytic theory AUROC is 0.591 [0.537, 0.652], against 0.884 for the oracle. Two things limit it: the divergence in-distribution is small (about 0.03 nats per step for quality 3), and the agent does not know W (a composite alternative), whereas the oracle does.

**H5. Where do the limits come from? Both.** (i) *Environment and intervention class set the ceiling*: the oracle AUROC is 0.884 under passive and 1.000 under wide or active interventions, so whether W is detectable depends on where one probes. (ii) *The observer's theory sets how much of the ceiling is realised*: under the same wide interventions the realised AUROC ranges from 0.026 to 0.989 across observers. (iii) *The observer's knowledge of the alternative* matters in the passive regime (exact theory, AUROC 0.59 against the oracle's 0.88). Which factor dominates depends on the regime: in-distribution the limit is the environment (little to detect); out of distribution it is the observer's theory (a great deal to detect, and most observers cannot).

**H6. Statistical and practical significance** (`results/stats.md`; seed-paired Wilcoxon tests, Holm-adjusted over 24 comparisons per metric, so the smallest attainable adjusted p is about 0.047 and significance requires all ten seeds to agree in sign). Reading: the independent-sample condition is neither statistically nor practically different from the baseline in any cell. The ReLU-theory differences are mixed: statistically and practically significant for false positives at wide T = 10 (+0.091), statistically significant but below the practical threshold for AUROC (+0.058). The adaptive observer differs from the baseline both statistically and practically (all cells shown), but differences from a below-chance baseline must be read against chance, not against the baseline. Several differences are "practical only" (not established with ten seeds), for example W ReLU/theory ReLU balanced accuracy at wide T = 10 (+0.061, Holm p = 0.107).

**H7. Mechanism (exploratory, `scripts/mechanism_check.py`, `results/mechanism_check.txt`).** The likelihood anomaly score −log Q behaves as Proposition 7(b) says. Under wide interventions at T = 10, with the baseline learned theory, the *true* environment E0 has higher mean negative log-likelihood than W in all 10 of 10 seeds (mean NLL(W) − NLL(E0) = −2.174; AUROC of the NLL score for W 0.051). With the analytic theory, W is more anomalous in 10 of 10 seeds (+5.881; AUROC 0.993). The inversion is thus a statement about which environment is nearer the theory in cross-entropy. The same phenomenon is known for static deep generative models (Nalisnick et al. 2019; Ren et al. 2019), so it is not a new phenomenon; the interventional instance is the contribution, if any.

### Information-leakage and coupling audit (`notes/leakage-audit.md`)

No leakage or unintended coupling was found. Details, with the tests that enforce each point, are in the audit note. In summary: all random streams are distinct (tested over 357 stream identifiers for two seeds); the agent theory's and the world model's training data share no rows and no sample path; the agent sees only `env.step` (tested with an opaque stub); adaptation episodes are disjoint from calibration and test episodes; the oracle, the AltOOD matching and the Platt scaling are experimenter-side only; conditions share seeds, hence are compared with seed-paired statistics.

### Limitations added in Phase 4

- One environment family, fully observed and low-dimensional; the second environment recommended in Phase 3 has **not** been added.
- The adaptive observer is one protocol (batch fine-tuning, then a consistency test, 1,000 adaptation transitions). Other adaptive observers, in particular a Bayesian model-selection observer whose hypothesis class contains a W-like model, would identify W by Proposition 8(a); that was **not** implemented, so the experiments show absorption for this protocol only.
- The detection statistic is a chi-square test of standardised residuals, not a likelihood ratio; the exact-theory observer does not know W.
- Ten seeds; paired tests have a floor on attainable p-values; bootstrap intervals over seeds ignore within-seed variance.
- The mechanism check and AltOOD are exploratory.
- Platt-based ECE and Brier are experimenter-side and meaningless where the score is inverted.
