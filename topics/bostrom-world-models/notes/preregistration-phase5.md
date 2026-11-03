---
id: topic-bostrom-world-models-preregistration-phase5
title: "Pre-specification of confirmatory analyses, Phase 5"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [preregistration, confirmatory]
---

## Pre-specification of confirmatory analyses (Phase 5)

This is an internal, version-controlled pre-specification, not an external registry entry. Its timestamp is the commit that first contains this file; the confirmatory runs are launched only after that commit exists, and the commit hash is recorded in the results. Nothing here was chosen after looking at confirmatory data, because none exists yet.

### Part 1: Bayesian observer on environment 1

**Development versus confirmation.** Seeds 200–204 were used to build and debug the observer and its analysis (exploratory; results in `results/bayes1_dev/`). Seeds 300–311 are held out and are used once, with the frozen configuration `configs/bayes1_confirm.yaml` (R = 100 independent observers per cell, 80 steps, episodes of length 10, regimes oracle / learned / bma, policies passive / wide / sweep / eig, uniform class prior, complete hypothesis space, observer theories trained on actions in [−1, 1], world model trained on 12,500 transitions). Design changes made after the development run, before freezing: more runs per cell (30 → 100) because the development run could not test equivalence at a margin of 0.05; an unbiased re-estimate of the recorded expected information gain.

**Unit of analysis.** The seed (n = 12). Each seed builds its own observer materials, true world model and alternative mechanisms from independent random streams. Statistics are computed per seed, then compared across seeds.

**Outcome definitions** (all at step 40; class-balanced: H0-true pools E0 and E0split, H1-true is W, H2-true pools AltOOD and Ealt):
acc3 = mean of the three class-conditional accuracies of argmax class posterior; ECE = expected calibration error of the confidence (max class posterior), 10 bins, class-balanced weights; h1v2_bal_acc = balanced accuracy of the pairwise posterior p(H1)/(p(H1)+p(H2)) at 0.5 between W-true and H2-true runs; false_id = fraction of decisions wrong among runs whose posterior reached 0.95 for some class within 80 steps (class-balanced); negative-control statistic = seed-level mean posterior mass on H0 under truth E0 minus under truth E0split.

**Directional claims** (supported iff the bootstrap 95% CI lower bound of the seed-level statistic exceeds the threshold, **and** the Holm-adjusted one-sided exact Wilcoxon signed-rank p < 0.05 across these eight claims):
- D1: acc3(oracle, wide) − acc3(learned, wide) ≥ 0.10.
- D2: acc3(oracle, wide) − acc3(bma, wide) ≥ 0.10.
- D3: ECE(learned, wide) − ECE(oracle, wide) ≥ 0.10.
- D4: ECE(bma, wide) − ECE(oracle, wide) ≥ 0.10.
- D5: acc3(learned, wide) − acc3(learned, passive) ≥ 0.10.
- D6: h1v2_bal_acc(learned, wide) ≥ 0.80.
- D7: false_id(learned, wide) ≥ 0.20.
- S1 (sanity gate): acc3(oracle, wide) ≥ 0.95.

**Equivalence claims** (supported iff the Holm-adjusted paired TOST p < 0.05 across these five at the stated margin; otherwise "not established", never "no effect"):
- E1: |acc3(eig) − acc3(wide)| < 0.05 in the learned regime.
- E2: the same in the bma regime.
- E3a–c: negative control, |mass on H0 under E0 − mass on H0 under E0split| < 0.05, for oracle, learned and bma under wide interventions.

**Practical-significance thresholds** are those stated in each claim (0.10 for accuracy and calibration differences; 0.05 equivalence margin for accuracy and for the negative control). A statistically significant difference below its threshold is reported as "statistical only".

**Everything else is exploratory** and labelled as such: other policies, checkpoints and regimes, pairwise AUROCs, entropy, information-gain comparisons, per-scenario breakdowns, stress tests (Part 3).

**Deviations.** Any deviation from this specification (code error, failed run, changed analysis) will be recorded in `notes/corrections-log.md` with the reason, and affected results reported both ways. No optional stopping; no re-running to obtain a different outcome; if a confirmatory run fails technically it is re-run with identical seeds and configuration and the failure is documented.

**Gate 2 criteria** (experimental validity) for environment 1, to be satisfied before the confirmatory run: posterior normalisation and exact agreement with a direct computation (unit test); simulation-based calibration under truth drawn from the prior (unit test, passive and information-gain policies); observational-equivalence control keeps the prior ratio exactly (unit test); observer uses only `env.step` (unit test); Monte-Carlo EIG agrees with numerical integration (unit test); oracle observer accurate under informative interventions (development run). All were satisfied before this file was committed.

### Part 2: partially observed environment (to be added in a separate commit before its confirmatory run)

The design, outcomes, thresholds and decision rules for the second environment will be added to this file and committed before the confirmatory run on that environment. Until then no confirmatory claim about partial observability exists.

### Part 3: stress tests and adversarial checks

Exploratory by design, on separate seeds (400–405), never combined with confirmatory seeds: varying model fidelity, intervention budget, training coverage of the observer's theories, prior misspecification, hypothesis-space completeness. Results are descriptive and are not promoted to confirmatory claims.
