# Confirmatory analysis, Bayesian observer, partially observed benchmark (confirmatory)

Directory: results/bayes2_confirm; seeds [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311] (n = 12); unit of analysis: seed. Rules fixed in notes/preregistration-phase5.md, Part 2.

## Directional claims (supported iff the bootstrap 95% CI bound lies on the claimed side of the threshold AND the Holm-adjusted one-sided Wilcoxon p < 0.05)

| id | claim | mean [95% CI] | threshold | raw p | Holm p | supported |
|---|---|---|---|---|---|---|
| G1 | oracle acc3, eig2: step 200 minus step 25 >= 0.10 (finite-sample, not fundamental) | 0.315 [0.297, 0.332] | >= 0.1 | 0.0002 | 0.0020 | **yes** |
| G2 | acc3(oracle, random) - acc3(learned, random) at step 100 >= 0.10 (misspecification-limited) | 0.259 [0.236, 0.283] | >= 0.1 | 0.0002 | 0.0020 | **yes** |
| G3 | ECE(learned, random) - ECE(oracle, random) at step 100 >= 0.10 | 0.336 [0.312, 0.359] | >= 0.1 | 0.0002 | 0.0020 | **yes** |
| G4 | acc3(oracle, eig2) - acc3(oracle, random) at step 100 >= 0.05 (active design helps under correct specification) | 0.176 [0.161, 0.193] | >= 0.05 | 0.0002 | 0.0020 | **yes** |
| G5 | acc3(learned, eig2) - acc3(learned, random) at step 100 < 0.05 (no practically significant benefit under learned likelihoods) | -0.025 [-0.047, -0.008] | < 0.05 | 0.0002 | 0.0020 | **yes** |
| G6 | H1-vs-H2 AUROC (learned, random) at step 100 < 0.65 (learned observer cannot separate learned from non-learned mechanisms) | 0.569 [0.530, 0.608] | < 0.65 | 0.0034 | 0.0034 | **yes** |
| G7 | accuracy on the transition-perturbed truth: random minus no-action-2, oracle, step 200 >= 0.20 (equivalence relative to an intervention class) | 0.589 [0.552, 0.630] | >= 0.2 | 0.0002 | 0.0020 | **yes** |
| S1 | ECE(oracle, random) at step 100 < 0.10 (oracle uncertainty is calibrated; sanity gate) | 0.037 [0.031, 0.042] | < 0.1 | 0.0002 | 0.0020 | **yes** |

## Equivalence claims (supported iff Holm-adjusted TOST p < 0.05; otherwise 'not established', never 'no effect')

| id | claim | mean difference [95% CI] | margin | TOST p | Holm p | supported |
|---|---|---|---|---|---|---|
| E1a | negative control, mass on H0 under reference vs bisimilar copy, oracle, random, step 100 | +0.006 [-0.013, +0.023] | ±0.05 | 0.0003 | 0.0003 | **yes** |
| E1b | same, learned | -0.002 [-0.016, +0.011] | ±0.05 | 0.0000 | 0.0000 | **yes** |
| E1c | same, bma | -0.004 [-0.013, +0.006] | ±0.05 | 0.0000 | 0.0000 | **yes** |
