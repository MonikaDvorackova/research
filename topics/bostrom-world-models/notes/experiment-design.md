---
id: topic-bostrom-world-models-experiment-design
title: "Minimal experiment: design and information-access constraints"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [experiment, design]
---

## Minimal experiment

Code: [`implementations/epistemic-identifiability`](../../../implementations/epistemic-identifiability/README.md). Executed results and limits are in [`results.md`](results.md).

### Environments

- **E0**: 2-D state, 1-D action, fully observed. Nonlinear stochastic dynamics with Gaussian noise (σ = 0.1) and a sinusoidal action effect, so that actions outside [−1, 1] probe a region where a learned model must extrapolate.
- **E0split**: negative control, observationally equivalent to E0 (Prop. 1): the Gaussian noise is generated as a sum of two independent half-variance Gaussians. A unit test checks the law equality (KS test and variance).
- **W**: learned world model (Gaussian MLP) trained on E0 trajectories under actions in [−1, 1], with 100, 500, 2500, 12500 training transitions (quality levels 0–3). Quality is measured by the true per-step KL(E0 ‖ W) in-distribution and with actions in [−3, 3].
- **Ealt**: E0 with a perturbed coupling constant, with the shift chosen so that KL(E0 ‖ Ealt) matches KL(E0 ‖ W) under wide interventions. A real mismatch that is not a learned model.

### Information-access constraints for the embedded agent

| Item | Agent has | Agent does not have |
|---|---|---|
| Interaction | Its own actions and the observed states | Environment label, parameters, source, noise seed |
| Prior knowledge | An ensemble Q of 5 dynamics models trained on independent E0 data with in-distribution actions | Any E0 data under out-of-distribution actions; W's weights or training data |
| Test | A calibrated chi-square test of Q-standardised residuals (exact under Q even for adaptive actions) | Likelihood of E0 or W |
| Calibration (experimenter side) | Platt scaling fitted on separate labelled episodes, used only to report ECE and Brier | Not available to the agent |
| Oracle (experimenter side) | Log-likelihood ratio W vs E0 on the observed trajectory, reported as an upper bound and as "information gain" | Not available to the agent |

**Limitation of this constraint set.** Giving the agent a Q trained on the reference is a stand-in for prior experience; a real embedded agent has no labelled reference. The experiment therefore measures detection of a discrepancy relative to a theory, which is exactly the L1 inference of the philosophical analysis.

### Intervention policies

- `passive`: actions uniform in [−1, 1] (training-like).
- `wide`: random actions uniform in [−3, 3] (out-of-distribution; baseline for exploration).
- `active`: at each step choose, among 64 random candidate actions in [−3, 3], the one maximising the ensemble's epistemic variance of the predicted next state (an uncertainty-based proxy for expected information gain).

### Metrics

AUROC (W vs {E0, E0split}); AUROC E0 vs E0split (should be 0.5); AUROC W vs Ealt (0.5 means the score does not identify a learned model); TPR/FPR of the α = 0.05 test; oracle AUROC; information gain per step; ECE and Brier; horizon at which AUROC reaches 0.8. Ten independent seeds; each seed trains its own Q and W's on independent data streams; evaluation episodes use separate random streams. Intervals are bootstrap 95% intervals over seeds.

### Pre-stated expectations (written before the full run)

1. Detection power increases with W quality being worse and with horizon T.
2. FPR on negative controls exceeds the nominal 0.05 for out-of-distribution interventions (Prop. 6).
3. AUROC E0 vs E0split ≈ 0.5.
4. AUROC W vs Ealt may be near 0.5 at matched divergence, supporting the claim that detection does not identify the mechanism. Not guaranteed, because W's discrepancy is state-dependent and Ealt's is not.
5. Active selection may or may not beat `wide`: it concentrates on regions where Q is uncertain, which inflates false alarms and also widens the null (Q's variance includes epistemic spread). No direction is pre-committed.
