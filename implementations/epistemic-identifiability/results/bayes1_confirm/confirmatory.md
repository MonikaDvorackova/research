# Confirmatory analysis, Bayesian observer, environment 1 (confirmatory)

Directory: results/bayes1_confirm; seeds: [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311] (n = 12); checkpoint: step 40; unit of analysis: seed. Rules fixed in notes/preregistration-phase5.md.

## Directional claims (supported iff the bootstrap 95% CI lower bound of the seed-level statistic exceeds the threshold AND the Holm-adjusted one-sided Wilcoxon p < 0.05)

| id | claim | mean [95% CI] | raw p | Holm p | supported |
|---|---|---|---|---|---|
| D1 | acc3(oracle, wide) - acc3(learned, wide) >= 0.10 | 0.314 [0.259, 0.367] (threshold 0.10) | 0.0005 | 0.0020 | **yes** |
| D2 | acc3(oracle, wide) - acc3(bma, wide) >= 0.10 | 0.391 [0.297, 0.483] (threshold 0.10) | 0.0002 | 0.0020 | **yes** |
| D3 | ECE(learned, wide) - ECE(oracle, wide) >= 0.10 | 0.260 [0.208, 0.316] (threshold 0.10) | 0.0005 | 0.0020 | **yes** |
| D4 | ECE(bma, wide) - ECE(oracle, wide) >= 0.10 | 0.323 [0.232, 0.414] (threshold 0.10) | 0.0012 | 0.0024 | **yes** |
| D5 | acc3(learned, wide) - acc3(learned, passive) >= 0.10 | 0.197 [0.151, 0.247] (threshold 0.10) | 0.0012 | 0.0024 | **yes** |
| D6 | H1-vs-H2 balanced accuracy (learned, wide) >= 0.80 | 0.128 [0.096, 0.160] (threshold 0 on the shifted statistic) | 0.0002 | 0.0020 | **yes** |
| D7 | false-identification rate (learned, wide) >= 0.20 | 0.147 [0.107, 0.186] (threshold 0 on the shifted statistic) | 0.0002 | 0.0020 | **yes** |
| S1 | acc3(oracle, wide) >= 0.95 (sanity gate) | 0.050 [0.050, 0.050] (threshold 0 on the shifted statistic) | 0.0002 | 0.0020 | **yes** |

## Equivalence claims (supported iff Holm-adjusted TOST p < 0.05 at the stated margin; otherwise 'not established', never 'no effect')

| id | claim | mean difference [95% CI] | margin | TOST p | Holm p | supported |
|---|---|---|---|---|---|---|
| E1 | |acc3(eig) - acc3(wide)| < 0.05, learned regime | -0.080 [-0.111, -0.048] | ±0.05 | 0.9493 | 1.0000 | **not established** |
| E2 | |acc3(eig) - acc3(wide)| < 0.05, bma regime | -0.056 [-0.104, -0.008] | ±0.05 | 0.5949 | 1.0000 | **not established** |
| E3a | negative control E0 vs E0split, mass on H0, oracle, wide | +0.000 [-0.000, +0.000] | ±0.05 | 0.0000 | 0.0000 | **yes** |
| E3b | negative control E0 vs E0split, mass on H0, learned, wide | -0.018 [-0.043, +0.008] | ±0.05 | 0.0196 | 0.0589 | **not established** |
| E3c | negative control E0 vs E0split, mass on H0, bma, wide | +0.007 [-0.011, +0.024] | ±0.05 | 0.0003 | 0.0012 | **yes** |

