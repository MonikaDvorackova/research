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

**F5. Detecting a discrepancy does not identify its source.** Under `wide` and `active` interventions the statistic flags the real, non-learned mismatches Ealt and AltOOD as readily as, or more readily than, W (quality 3, wide, T = 10: TPR 0.862 for AltOOD, 0.070 for W). Under passive interventions at qualities ≥ 1, W and AltOOD both coincide with E0 and are not separated (AUROC W vs AltOOD 0.505 [0.487, 0.521] at T = 2, quality 3; 0.519 [0.485, 0.566] at T = 50). The score cannot be read as detecting "a learned model" in either regime. The large departures of W vs Ealt/AltOOD AUROC from 0.5 under OOD interventions run in the direction opposite to "W is more anomalous", so they are not detection of W as a learned model.

**F6. Calibration is not informative here.** ECE after Platt scaling is small (mostly below 0.07; up to 0.13 for the smallest model under active interventions), but the Brier score under passive interventions at quality 3, T = 50 is 0.219, near the uninformative value 0.25. Low ECE here reflects scores that carry little information, not useful probabilities.

### Pre-stated expectations (from `experiment-design.md`) against outcomes

| # | Expectation | Outcome |
|---|---|---|
| 1 | Power rises with worse W and longer T | Supported for passive and for quality 0; not for quality ≥ 1 under OOD (inverted) |
| 2 | FPR above 0.05 for OOD interventions | Supported, strongly (up to 1.000) |
| 3 | E0 vs E0split AUROC ≈ 0.5 | Supported |
| 4 | W vs matched real mismatch may be near 0.5 | Not supported for Ealt (separated, but in the "W looks less anomalous" direction); supported only under passive interventions for AltOOD (a trivial case, since both match E0 there) |
| 5 | Active may or may not beat wide | Active gives far more oracle information but does not improve the agent's detection; it raises FPR to 1.000 |

### Hypothesis (untested)

W is more consistent with Q under OOD interventions than E0 is, plausibly because both are learned from similar data with the same architecture and extrapolate alike. If so, an observer whose theory belongs to the same model class would find a learned environment *more* congenial than reality. This is a conjecture; the study did not vary Q's architecture or training data, so it cannot be distinguished from other explanations.

### Limitations

- Toy, fully observed, low-dimensional environment; no partial observability (POMDP) and no learned latent states.
- Q and W share architecture and training distribution (one family), and Q is trained on the reference. The agent has a theory built from the reference, which a real embedded agent would not.
- The test uses only squared standardised residuals; no tuned detector, no other statistic, no hyperparameter search, no architecture ablation. Ablations are limited to quality levels, policies, and horizons.
- "Active" is an uncertainty-based proxy for expected information gain, not an exact EIG policy.
- Ealt and AltOOD are matched in mean KL under wide interventions only; AltOOD was added after seeing v1.
- Ten seeds; intervals are bootstrap over seeds and ignore episode-level variance within a seed. KL values for the smallest model are heavy-tailed.
- Calibration uses labelled episodes on the experimenter side.
- The results illustrate Propositions 3(b) and 6 and do not validate them (they are proved separately); nothing here supports or tests thesis T1–T3 beyond illustration.
