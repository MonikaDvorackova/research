# Confirmatory analysis, Bayesian observer, environment 1 (confirmatory)

Directory: results/bayes1_confirm_runB; seeds: [300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311] (n = 12); checkpoint: step 40; unit of analysis: seed. Rules fixed in notes/preregistration-phase5.md.

## Directional claims (supported iff the bootstrap 95% CI lower bound of the seed-level statistic exceeds the threshold AND the Holm-adjusted one-sided Wilcoxon p < 0.05)

| id | claim | mean [95% CI] | raw p | Holm p | supported |
|---|---|---|---|---|---|
| D1 | acc3(oracle, wide) - acc3(learned, wide) >= 0.10 | 0.319 [0.260, 0.375] (threshold 0.10) | 0.0005 | 0.0024 | **yes** |
| D2 | acc3(oracle, wide) - acc3(bma, wide) >= 0.10 | 0.409 [0.316, 0.499] (threshold 0.10) | 0.0002 | 0.0020 | **yes** |
| D3 | ECE(learned, wide) - ECE(oracle, wide) >= 0.10 | 0.270 [0.216, 0.324] (threshold 0.10) | 0.0005 | 0.0024 | **yes** |
| D4 | ECE(bma, wide) - ECE(oracle, wide) >= 0.10 | 0.337 [0.246, 0.427] (threshold 0.10) | 0.0007 | 0.0024 | **yes** |
| D5 | acc3(learned, wide) - acc3(learned, passive) >= 0.10 | 0.195 [0.149, 0.243] (threshold 0.10) | 0.0012 | 0.0024 | **yes** |
| D6 | H1-vs-H2 balanced accuracy (learned, wide) >= 0.80 | 0.126 [0.093, 0.158] (threshold 0 on the shifted statistic) | 0.0002 | 0.0020 | **yes** |
| D7 | false-identification rate (learned, wide) >= 0.20 | 0.154 [0.108, 0.199] (threshold 0 on the shifted statistic) | 0.0005 | 0.0024 | **yes** |
| S1 | acc3(oracle, wide) >= 0.95 (sanity gate) | 0.050 [0.050, 0.050] (threshold 0 on the shifted statistic) | 0.0002 | 0.0020 | **yes** |

## Equivalence claims (supported iff Holm-adjusted TOST p < 0.05 at the stated margin; otherwise 'not established', never 'no effect')

| id | claim | mean difference [95% CI] | margin | TOST p | Holm p | supported |
|---|---|---|---|---|---|---|
| E1 | |acc3(eig) - acc3(wide)| < 0.05, learned regime | -0.075 [-0.097, -0.050] | ±0.05 | 0.9612 | 0.9612 | **not established** |
| E2 | |acc3(eig) - acc3(wide)| < 0.05, bma regime | -0.042 [-0.095, +0.014] | ±0.05 | 0.3928 | 0.7856 | **not established** |
| E3a | negative control E0 vs E0split, mass on H0, oracle, wide | -0.000 [-0.000, +0.000] | ±0.05 | 0.0000 | 0.0000 | **yes** |
| E3b | negative control E0 vs E0split, mass on H0, learned, wide | +0.010 [-0.013, +0.034] | ±0.05 | 0.0049 | 0.0197 | **yes** |
| E3c | negative control E0 vs E0split, mass on H0, bma, wide | +0.017 [-0.008, +0.040] | ±0.05 | 0.0137 | 0.0411 | **yes** |

