# Cross-condition comparison (quality 3, 12,500 training transitions for W; mean over seeds with bootstrap 95% CI)

## FPR (alpha=0.05)

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.070 [0.056, 0.084] | 0.883 [0.868, 0.897] | 1.000 [0.999, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A1: ReLU-128x3 ensemble theory | 0.092 [0.074, 0.112] | 0.974 [0.967, 0.981] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A2: cubic-polynomial theory (different model class) | 0.052 [0.048, 0.057] | 0.579 [0.355, 0.786] | 0.747 [0.489, 0.995] | 0.832 [0.597, 1.000] | 0.900 [0.700, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.082 [0.063, 0.101] | 0.050 [0.044, 0.055] | 0.071 [0.061, 0.081] | 0.065 [0.057, 0.073] | 0.198 [0.132, 0.274] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.050 [0.045, 0.054] | 0.049 [0.042, 0.056] | 0.049 [0.044, 0.055] | 0.055 [0.050, 0.060] | 0.048 [0.040, 0.055] |

## TPR on W

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.092 [0.055, 0.143] | 0.070 [0.059, 0.081] | 0.139 [0.080, 0.210] | 0.123 [0.079, 0.191] | 0.413 [0.232, 0.611] |
| A1: ReLU-128x3 ensemble theory | 0.252 [0.174, 0.345] | 0.736 [0.681, 0.793] | 1.000 [0.998, 1.000] | 0.770 [0.568, 0.941] | 0.858 [0.717, 0.975] |
| A2: cubic-polynomial theory (different model class) | 0.163 [0.095, 0.258] | 0.974 [0.955, 0.989] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.099 [0.061, 0.148] | 0.968 [0.962, 0.973] | 1.000 [1.000, 1.000] | 0.979 [0.951, 1.000] | 1.000 [1.000, 1.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.151 [0.089, 0.237] | 0.972 [0.964, 0.979] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |

## AUROC W vs controls

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.516 [0.479, 0.567] | 0.056 [0.049, 0.064] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| A1: ReLU-128x3 ensemble theory | 0.619 [0.569, 0.681] | 0.114 [0.092, 0.139] | 0.012 [0.006, 0.019] | 0.010 [0.001, 0.026] | 0.000 [0.000, 0.000] |
| A2: cubic-polynomial theory (different model class) | 0.592 [0.533, 0.661] | 0.948 [0.924, 0.968] | 0.999 [0.998, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.507 [0.452, 0.564] | 0.985 [0.981, 0.989] | 1.000 [1.000, 1.000] | 0.989 [0.975, 1.000] | 1.000 [1.000, 1.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.591 [0.537, 0.652] | 0.989 [0.985, 0.992] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |

## oracle AUROC

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A1: ReLU-128x3 ensemble theory | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A2: cubic-polynomial theory (different model class) | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 0.999 [0.998, 1.000] | 1.000 [1.000, 1.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
