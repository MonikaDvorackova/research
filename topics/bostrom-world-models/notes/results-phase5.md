---
id: topic-bostrom-world-models-results-phase5
title: "Phase 5 results: Bayesian observers, partial observability, stress tests"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [results, confirmatory, bayesian]
---

## Phase 5 results

Status labels: **CONFIRMATORY** = specified in `preregistration-phase5.md` before the data existed and analysed by the committed script (run A); **EXPLORATORY** = everything else. Raw posteriors: `implementations/epistemic-identifiability/results/bayes1_confirm/`, `bayes2_confirm/` (run A) and `*_runB/` (deterministic repeat). All numbers are means over seeds with bootstrap 95% intervals over seeds unless stated. These are toy systems; nothing here is a statement about the physical universe or about Bostrom's trilemma.

### What was built

- **Bayesian model-selection observer** with three classes: H0 the reference environment, H1 a learned computational world model, H2 a non-learned alternative mechanism (optionally H3, a catch-all). Each class is a finite set of members with explicit Gaussian (environment 1) or autoregressive categorical (environment 2) kernels; member log-weights are updated by the exact log-likelihood of every observed transition; class posteriors are sums of member posteriors. Priors uniform over classes unless stated; within-class weights uniform; decision rule: stop when a class posterior reaches 0.95; model uncertainty enters through Bayesian model averaging over heterogeneous learners.
- **Information regimes:** *oracle* (true kernels), *learned* (one plug-in learned kernel per class, trained on narrow in-distribution reference data), *bma* (model averaging over ReLU/tanh/GRU learners, world models of several sizes, deviation families). The observer never receives the environment's identity.
- **Intervention policies:** passive (training-like), random/wide, fixed sweep, myopic expected information gain (EIG about the class index; Monte-Carlo in environment 1, exact in environment 2), non-myopic two-step EIG (environment 2, exact), and, in environment 2, `no2` (never uses the informative action).
- **Environment 2:** a finite POMDP (4 hidden states, 3 observations, 3 actions) with a GRU world model, an exactly observationally equivalent split-state control, a mechanism-distinct transition-perturbed control (identical to the reference unless action 2 is used) and an emission-noise control.
- **Exact finite-state checks:** forward algorithm versus brute-force hidden-path summation; chain rule; one- and two-step EIG versus brute-force mutual information; simulation-based calibration; exact equivalence; Proposition 10 by dynamic programming.

### CONFIRMATORY results, environment 1 (12 held-out seeds, run A)

| id | claim | result | supported |
|---|---|---|---|
| D1 | acc3(oracle, wide) − acc3(learned, wide) ≥ 0.10 | 0.314 [0.259, 0.367] | yes |
| D2 | same for bma | 0.391 [0.297, 0.483] | yes |
| D3 | ECE(learned) − ECE(oracle) ≥ 0.10 | 0.260 [0.208, 0.316] | yes |
| D4 | same for bma | 0.323 [0.232, 0.414] | yes |
| D5 | wide − passive acc3 (learned) ≥ 0.10 | 0.197 [0.151, 0.247] | yes |
| D6 | H1-vs-H2 balanced accuracy (learned, wide) ≥ 0.80 | 0.928 [0.896, 0.960] | yes |
| D7 | false-identification rate (learned, wide) ≥ 0.20 | 0.347 [0.307, 0.386] | yes |
| S1 | acc3(oracle, wide) ≥ 0.95 | 1.000 | yes |
| E1 | \|acc3(eig) − acc3(wide)\| < 0.05, learned | −0.080 [−0.111, −0.048] | **not established** |
| E2 | same, bma | −0.056 [−0.104, −0.008] | **not established** |
| E3a | negative control (E0 vs E0split), oracle | +0.000 | yes |
| E3b | negative control, learned | −0.018 [−0.043, +0.008]; TOST raw p 0.0196, Holm p 0.0589 | **not established** (the interval lies inside ±0.05, but the pre-specified Holm rule is not met) |
| E3c | negative control, bma | +0.007 [−0.011, +0.024] | yes |

Directional claims: Holm-adjusted one-sided exact Wilcoxon p between 0.0020 and 0.0024 (n = 12).

### CONFIRMATORY results, environment 2 (12 held-out seeds, run A)

| id | claim | result | supported |
|---|---|---|---|
| G1 | oracle acc3 (eig2) step 200 − step 25 ≥ 0.10 | 0.315 [0.297, 0.332] | yes |
| G2 | acc3(oracle, random) − acc3(learned, random) at step 100 ≥ 0.10 | 0.259 [0.236, 0.283] | yes |
| G3 | ECE(learned) − ECE(oracle) at step 100 ≥ 0.10 | 0.336 [0.312, 0.359] | yes |
| G4 | acc3(oracle, eig2) − acc3(oracle, random) ≥ 0.05 | 0.176 [0.161, 0.193] | yes |
| G5 | acc3(learned, eig2) − acc3(learned, random) < 0.05 | −0.025 [−0.047, −0.008] | yes (no benefit; slightly worse) |
| G6 | H1-vs-H2 AUROC (learned, random) < 0.65 | 0.569 [0.530, 0.608] | yes |
| G7 | oracle accuracy on the transition-perturbed truth, random minus no2, step 200 ≥ 0.20 | 0.589 [0.552, 0.630] | yes |
| S1 | ECE(oracle, random) at step 100 < 0.10 | 0.037 [0.031, 0.042] | yes |
| E1a–c | negative control (reference vs bisimilar copy), oracle / learned / bma | +0.006, −0.002, −0.004; all intervals inside ±0.05 | yes (all three; Holm p ≤ 0.0003) |

Directional claims: Holm-adjusted p between 0.0020 and 0.0034.

### EXPLORATORY results

**Environment 1 (confirmatory seeds, step 40).** Oracle: perfect under wide, sweep and EIG (acc3 1.000); passive oracle accuracy on the OOD-localised alternative is exactly 0.500 because that mechanism equals the reference for in-distribution actions. Learned, wide: acc3 0.686 (H0 0.368, H1 0.769, H2 0.921), H1-vs-H2 AUROC 0.970, H1-vs-H0 AUROC 0.696, ECE 0.260, mean entropy 0.136 (overconfident). BMA, wide: acc3 0.609, H1-vs-H2 AUROC 0.900, H1-vs-H0 AUROC 0.525, ECE 0.323. EIG design was worse than wide in 11 of 12 seeds (learned: −0.080) and 9 of 12 (bma: −0.056). The learned observers separate the learned world model from non-learned alternatives well, yet label the true reference as the reference only 31–37% of the time.

**Environment 2 (confirmatory seeds).** Accuracy against budget (steps 25, 50, 100, 200), 3-class:

| regime, policy | 25 | 50 | 100 | 200 | ECE at 200 |
|---|---|---|---|---|---|
| oracle, random | 0.489 | 0.562 | 0.645 | 0.771 | 0.037 |
| oracle, two-step EIG | 0.603 | 0.703 | 0.821 | 0.918 | 0.023 |
| oracle, no action 2 | 0.427 | 0.453 | 0.495 | 0.552 | 0.037 |
| learned, random | 0.360 | 0.369 | 0.386 | 0.387 | 0.461 |
| learned, two-step EIG | 0.351 | 0.354 | 0.361 | 0.368 | 0.566 |
| bma, random | 0.371 | 0.381 | 0.396 | 0.398 | 0.361 |

H1-vs-H2 AUROC at step 200: oracle 0.967 (random), 0.998 (two-step EIG); learned 0.611, 0.604; bma 0.615, 0.619. H1-vs-H0 AUROC at step 200: oracle 0.950 / 0.997; learned 0.490 / 0.436; bma 0.464 / 0.445. Accuracy of the oracle on the transition-perturbed truth at step 200: no action 2 0.116 [0.095, 0.136]; random 0.705 [0.679, 0.732]; two-step EIG 0.950 [0.935, 0.964].

**Exact distinguishability (confirmatory seeds, mean total variation of the 6-step observation laws).** Reference versus its split-state copy: 0.0000 under every intervention class. Reference versus transition-perturbed: 0.0078 (training policy), **0.0000 (no action 2)**, 0.0892 (uniform), 0.0818 (action-2-heavy). Reference versus the GRU world model: 0.057 (training), 0.054 (no action 2), 0.127 (uniform), 0.244 (action-2-heavy). The world model is close to the reference where it was trained and far where it was not.

**Information-gain ratio diagnostic (exploratory in environment 1; failed to replicate in environment 2).** In environment 1 the ratio of realised to expected information gain under EIG design was 0.97 [0.96, 0.98] for the oracle and 5.00 [3.85, 6.26] and 4.05 [3.38, 4.77] for learned and bma; the learned observer was unsurprised by the learned world model (realised 1.25 versus expected 1.49) and surprised by the reference (5.63 versus 0.90). In environment 2 the ratio is 0.94, 1.00 and 0.97 for oracle, learned and bma: **no separation**. The diagnostic is not robust and should not be offered as a general finding.

### EXPLORATORY stress tests (environment 1, seeds 400–405, n = 6; `results/stress_summary.md`)

- **Coverage.** Training the observer's theories over the probed range (a ∈ [−3, 3]) turns the failure into success: learned, wide, acc3 0.983, ECE 0.011; EIG 0.991, ECE 0.009; bma 0.984 and 0.991. (Baseline learned wide: 0.686, ECE 0.260.) With adequate coverage, information-gain design matches or slightly exceeds random wide interventions.
- **Fidelity.** Lower-fidelity world models make learned observers worse: learned, wide acc3 0.540 (500 transitions), 0.513 (2,500), 0.686 (12,500); EIG design 0.437, 0.387, 0.606. The oracle is unaffected (1.000).
- **Incomplete hypothesis spaces.** When the true class is absent from the space the observer classifies the truth confidently into a wrong class, even in the oracle regime (oracle, class H1 absent: the learned-world-model truth is misassigned, ECE 0.332; class H2 absent: the alternative truths are misassigned, ECE 0.332; only one deviation shape present: accuracy on H2 about 0.50, ECE 0.166). Posterior probabilities are relative to the class (Propositions 8(b), 10).
- **Misleading priors.** The oracle is insensitive to priors (data overwhelm them); learned observers lose accuracy (for example no H2, learned, wide: 0.367 with a uniform prior, 0.235 when the prior favours H0).

### Post hoc equivalence tests on the frozen Phase 4 results (`results/phase4_equivalence_posthoc.md`)

Margins fixed before running: 12 of 12 contrasts (independent sample, ReLU theory, ReLU world model with either theory architecture, at three cells) are equivalent to the baseline within ±0.10 AUROC; the negative control (AUROC E0 vs E0split within ±0.05 of 0.5) is equivalent in 25 of 27 cells, the two exceptions being the noisy adaptive observer (intervals including 0). Many cells sit at the AUROC floor (about 0), so part of that equivalence reflects a shared floor.

### Where the limits of detection come from (answer from these experiments)

1. **Fundamental, relative to an intervention class (exact):** with no use of action 2 the transition-perturbed mechanism is indistinguishable from the reference by *any* observer (TV 0.0000, posterior odds unchanged to 0.00e+00); no budget helps.
2. **Finite-sample:** the correctly specified observer's accuracy rises steadily with budget (0.49 → 0.77 random; 0.60 → 0.92 two-step EIG), with calibrated uncertainty (ECE 0.02–0.04).
3. **Misspecification:** learned-likelihood observers stay near chance (0.36–0.45 in the POMDP) or are overconfident and mislabel the reference (environment 1), independent of budget; the failure disappears when the theories cover the probed regime (stress, environment 1) and is not removed by model averaging or information-gain design.
4. **Hypothesis-space incompleteness:** confident misclassification of out-of-class truths even for an oracle.

### Where the confirmatory claims do not reach (robustness limits)

- The learned observer's ability to separate H1 from H2 is **environment-specific**: AUROC 0.97 in environment 1 (D6) but 0.57–0.61 in the POMDP (G6).
- The information-gain ratio diagnostic did not replicate.
- Coverage is decisive; the central failure is not a property of learned observers as such.
- One architecture family per environment for the world model (Gaussian MLP; GRU); two environments only; ten to twelve seeds; toy dimensions.
- The equivalence claim E3b (environment 1, learned regime) was not established by the pre-specified rule.

### Run B: bit-reproducible replication (after the reproducibility defect was fixed)

The first Phase 5 runs (run A) used a randomised stream index (see `corrections-log.md` #14). After the fix, the confirmatory and stress experiments were repeated with identical configurations and seeds (run B). **The primary pre-specified analysis is run A;** run B is a replication of the same analysis with fresh interaction randomness (the observer materials, world models and truths are identical).

- **Environment 1, confirmatory** (`results/compare_runs_bayes1.md`): all eight directional claims have the same decision and nearly identical estimates (for example D1 0.314 versus 0.319, D2 0.391 versus 0.409, D6 0.128 versus 0.126). E1 and E2 are not established in both runs. **E3b differs**: not established in run A (the primary result, Holm p 0.0589) and established in run B (difference +0.010 [−0.013, +0.034]). In both runs the estimated difference lies well inside ±0.05, but the pre-specified rule gives different decisions; E3b is therefore **not claimed**.
- **Environment 2, confirmatory** (`results/compare_runs_bayes2.md`): all eleven claims have the same decision in both runs (for example G2 0.259 versus 0.283, G4 0.176 versus 0.160, G7 0.589 versus 0.607).
- **Stress tests** (exploratory): across all 16 learned/bma × wide/eig cells in the four stress sets, run A and run B accuracies differ by at most 0.018 (`results/stress_summary.md` and `results/stress_summary_runB.md`).
- **Exact reproduction of run B:** one full confirmatory seed per environment was re-run in a fresh process and compared array by array with the stored run B output (`scripts/reproduce_bayes.py`; results in `results/repro_bayes1_seed300.txt` and `results/repro_bayes2_seed300.txt`): **environment 1 seed 300: 300 arrays compared, 0 mismatching; environment 2 seed 300: 450 arrays compared, 0 mismatching.** Bit-identity is shown on one machine and library version only.
