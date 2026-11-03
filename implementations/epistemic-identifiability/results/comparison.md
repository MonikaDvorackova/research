# Cross-condition comparison (quality 3, 12,500 training transitions for W; mean over seeds with bootstrap 95% CI)

## FPR (alpha=0.05)

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.070 [0.056, 0.084] | 0.883 [0.868, 0.897] | 1.000 [0.999, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A1: ReLU-128x3 ensemble theory | 0.092 [0.074, 0.112] | 0.974 [0.967, 0.981] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A2: cubic-polynomial theory (different model class) | 0.052 [0.048, 0.057] | 0.579 [0.355, 0.786] | 0.747 [0.489, 0.995] | 0.832 [0.597, 1.000] | 0.900 [0.700, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.082 [0.063, 0.101] | 0.050 [0.044, 0.055] | 0.071 [0.061, 0.081] | 0.065 [0.057, 0.073] | 0.198 [0.132, 0.274] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.050 [0.045, 0.054] | 0.049 [0.042, 0.056] | 0.049 [0.044, 0.055] | 0.055 [0.050, 0.060] | 0.048 [0.040, 0.055] |
| independently trained theory (fresh E0 sample), same architecture | 0.064 [0.054, 0.074] | 0.865 [0.815, 0.902] | 1.000 [0.999, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.070 [0.056, 0.084] | 0.883 [0.868, 0.897] | 1.000 [0.999, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.092 [0.074, 0.112] | 0.974 [0.967, 0.981] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.055 [0.049, 0.061] | 0.055 [0.048, 0.063] | 0.093 [0.081, 0.107] | 0.137 [0.074, 0.202] | 0.468 [0.296, 0.654] |

## FNR on W (1 - TPR)

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.908 [0.857, 0.945] | 0.930 [0.919, 0.941] | 0.861 [0.790, 0.920] | 0.877 [0.809, 0.921] | 0.587 [0.389, 0.768] |
| A1: ReLU-128x3 ensemble theory | 0.748 [0.655, 0.826] | 0.264 [0.207, 0.319] | 0.001 [0.000, 0.002] | 0.230 [0.059, 0.432] | 0.142 [0.026, 0.283] |
| A2: cubic-polynomial theory (different model class) | 0.838 [0.743, 0.905] | 0.026 [0.011, 0.046] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.901 [0.852, 0.939] | 0.033 [0.027, 0.039] | 0.000 [0.000, 0.000] | 0.021 [0.000, 0.049] | 0.000 [0.000, 0.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.848 [0.763, 0.911] | 0.029 [0.022, 0.036] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| independently trained theory (fresh E0 sample), same architecture | 0.905 [0.861, 0.940] | 0.916 [0.904, 0.927] | 0.857 [0.819, 0.894] | 0.915 [0.887, 0.936] | 0.814 [0.695, 0.909] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.892 [0.855, 0.924] | 0.896 [0.854, 0.935] | 0.647 [0.493, 0.800] | 0.681 [0.534, 0.827] | 0.408 [0.223, 0.604] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.793 [0.724, 0.858] | 0.718 [0.651, 0.786] | 0.336 [0.176, 0.513] | 0.387 [0.212, 0.571] | 0.281 [0.015, 0.547] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.918 [0.891, 0.941] | 0.940 [0.929, 0.951] | 0.928 [0.910, 0.945] | 0.911 [0.869, 0.945] | 0.737 [0.553, 0.878] |

## TPR on W

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.092 [0.055, 0.143] | 0.070 [0.059, 0.081] | 0.139 [0.080, 0.210] | 0.123 [0.079, 0.191] | 0.413 [0.232, 0.611] |
| A1: ReLU-128x3 ensemble theory | 0.252 [0.174, 0.345] | 0.736 [0.681, 0.793] | 1.000 [0.998, 1.000] | 0.770 [0.568, 0.941] | 0.858 [0.717, 0.975] |
| A2: cubic-polynomial theory (different model class) | 0.163 [0.095, 0.258] | 0.974 [0.955, 0.989] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.099 [0.061, 0.148] | 0.968 [0.962, 0.973] | 1.000 [1.000, 1.000] | 0.979 [0.951, 1.000] | 1.000 [1.000, 1.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.151 [0.089, 0.237] | 0.972 [0.964, 0.979] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| independently trained theory (fresh E0 sample), same architecture | 0.095 [0.060, 0.139] | 0.084 [0.073, 0.096] | 0.143 [0.106, 0.181] | 0.085 [0.063, 0.113] | 0.186 [0.091, 0.305] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.108 [0.076, 0.146] | 0.103 [0.065, 0.146] | 0.353 [0.200, 0.507] | 0.319 [0.173, 0.467] | 0.592 [0.396, 0.777] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.207 [0.142, 0.276] | 0.282 [0.214, 0.349] | 0.664 [0.487, 0.824] | 0.613 [0.429, 0.788] | 0.719 [0.453, 0.986] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.082 [0.059, 0.109] | 0.060 [0.049, 0.071] | 0.072 [0.056, 0.090] | 0.089 [0.055, 0.131] | 0.263 [0.122, 0.447] |

## balanced accuracy (TPR on W and 1 - FPR)

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.511 [0.492, 0.538] | 0.093 [0.084, 0.103] | 0.070 [0.040, 0.105] | 0.062 [0.040, 0.096] | 0.206 [0.116, 0.306] |
| A1: ReLU-128x3 ensemble theory | 0.580 [0.541, 0.626] | 0.381 [0.354, 0.408] | 0.500 [0.499, 0.500] | 0.385 [0.284, 0.470] | 0.429 [0.358, 0.487] |
| A2: cubic-polynomial theory (different model class) | 0.555 [0.521, 0.603] | 0.698 [0.600, 0.804] | 0.626 [0.502, 0.756] | 0.584 [0.500, 0.701] | 0.550 [0.500, 0.650] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.509 [0.486, 0.536] | 0.959 [0.955, 0.963] | 0.964 [0.959, 0.969] | 0.957 [0.945, 0.967] | 0.901 [0.863, 0.934] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.551 [0.519, 0.594] | 0.961 [0.957, 0.965] | 0.975 [0.972, 0.978] | 0.973 [0.970, 0.975] | 0.976 [0.973, 0.980] |
| independently trained theory (fresh E0 sample), same architecture | 0.515 [0.499, 0.535] | 0.109 [0.095, 0.130] | 0.071 [0.053, 0.090] | 0.042 [0.032, 0.056] | 0.093 [0.046, 0.152] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.519 [0.503, 0.539] | 0.110 [0.088, 0.132] | 0.177 [0.100, 0.253] | 0.160 [0.086, 0.233] | 0.296 [0.198, 0.389] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.557 [0.523, 0.594] | 0.154 [0.119, 0.187] | 0.332 [0.244, 0.412] | 0.307 [0.215, 0.394] | 0.360 [0.226, 0.493] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.514 [0.500, 0.529] | 0.503 [0.496, 0.509] | 0.489 [0.477, 0.503] | 0.476 [0.438, 0.513] | 0.397 [0.305, 0.503] |

## AUROC W vs controls

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.516 [0.479, 0.567] | 0.056 [0.049, 0.064] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| A1: ReLU-128x3 ensemble theory | 0.619 [0.569, 0.681] | 0.114 [0.092, 0.139] | 0.012 [0.006, 0.019] | 0.010 [0.001, 0.026] | 0.000 [0.000, 0.000] |
| A2: cubic-polynomial theory (different model class) | 0.592 [0.533, 0.661] | 0.948 [0.924, 0.968] | 0.999 [0.998, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.507 [0.452, 0.564] | 0.985 [0.981, 0.989] | 1.000 [1.000, 1.000] | 0.989 [0.975, 1.000] | 1.000 [1.000, 1.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.591 [0.537, 0.652] | 0.989 [0.985, 0.992] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| independently trained theory (fresh E0 sample), same architecture | 0.532 [0.497, 0.577] | 0.064 [0.045, 0.092] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.536 [0.508, 0.569] | 0.086 [0.063, 0.111] | 0.002 [0.000, 0.004] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.598 [0.546, 0.649] | 0.026 [0.019, 0.033] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.538 [0.510, 0.573] | 0.491 [0.473, 0.508] | 0.458 [0.437, 0.482] | 0.432 [0.369, 0.497] | 0.329 [0.195, 0.488] |

## ECE (Platt-scaled)

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.015 [0.005, 0.027] | 0.037 [0.033, 0.042] | 0.003 [0.002, 0.004] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| A1: ReLU-128x3 ensemble theory | 0.026 [0.015, 0.036] | 0.050 [0.042, 0.062] | 0.022 [0.017, 0.027] | 0.010 [0.002, 0.022] | 0.001 [0.000, 0.001] |
| A2: cubic-polynomial theory (different model class) | 0.015 [0.006, 0.023] | 0.040 [0.027, 0.057] | 0.004 [0.001, 0.008] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.025 [0.013, 0.037] | 0.017 [0.014, 0.020] | 0.000 [0.000, 0.001] | 0.008 [0.001, 0.015] | 0.001 [0.000, 0.001] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.016 [0.007, 0.026] | 0.016 [0.013, 0.019] | 0.000 [0.000, 0.001] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| independently trained theory (fresh E0 sample), same architecture | 0.015 [0.006, 0.026] | 0.036 [0.032, 0.041] | 0.004 [0.002, 0.006] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.010 [0.004, 0.019] | 0.038 [0.031, 0.045] | 0.007 [0.003, 0.011] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.023 [0.012, 0.033] | 0.024 [0.020, 0.028] | 0.003 [0.001, 0.004] | 0.001 [0.000, 0.002] | 0.000 [0.000, 0.001] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.011 [0.003, 0.022] | 0.013 [0.005, 0.023] | 0.016 [0.008, 0.024] | 0.037 [0.022, 0.054] | 0.036 [0.023, 0.051] |

## Brier score (0.25 = uninformative)

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.219 [0.213, 0.223] | 0.085 [0.079, 0.092] | 0.002 [0.001, 0.003] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| A1: ReLU-128x3 ensemble theory | 0.206 [0.190, 0.218] | 0.126 [0.113, 0.140] | 0.032 [0.021, 0.043] | 0.013 [0.002, 0.031] | 0.000 [0.000, 0.000] |
| A2: cubic-polynomial theory (different model class) | 0.209 [0.191, 0.220] | 0.064 [0.047, 0.084] | 0.003 [0.000, 0.006] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.217 [0.212, 0.222] | 0.031 [0.026, 0.035] | 0.000 [0.000, 0.000] | 0.013 [0.001, 0.026] | 0.001 [0.000, 0.001] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.211 [0.196, 0.221] | 0.024 [0.020, 0.028] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| independently trained theory (fresh E0 sample), same architecture | 0.220 [0.215, 0.222] | 0.091 [0.076, 0.110] | 0.003 [0.001, 0.006] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.220 [0.217, 0.222] | 0.106 [0.089, 0.123] | 0.009 [0.002, 0.016] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.211 [0.202, 0.218] | 0.054 [0.045, 0.063] | 0.002 [0.001, 0.004] | 0.001 [0.000, 0.002] | 0.000 [0.000, 0.000] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.220 [0.216, 0.222] | 0.223 [0.222, 0.224] | 0.220 [0.219, 0.222] | 0.212 [0.205, 0.218] | 0.162 [0.127, 0.196] |

## oracle AUROC

| condition | passive T=50 | wide T=10 | wide T=50 | active T=10 | active T=50 |
|---|---|---|---|---|---|
| baseline: tanh-64 ensemble theory, trained on a in [-1,1] | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A1: ReLU-128x3 ensemble theory | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| A2: cubic-polynomial theory (different model class) | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| C: tanh-64 theory trained on a in [-3,3] (coverage) | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 0.999 [0.998, 1.000] | 1.000 [1.000, 1.000] |
| B: analytic true-law theory; actions chosen by learned-ensemble disagreement | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| independently trained theory (fresh E0 sample), same architecture | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| W = ReLU-128x3, theory = tanh-64 (architectures differ) | 0.904 [0.882, 0.926] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| W = ReLU-128x3, theory = ReLU-128x3 (architectures shared) | 0.904 [0.882, 0.926] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
| adaptive observer: fine-tunes the tanh theory on its own interaction before testing | 0.884 [0.858, 0.910] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] | 1.000 [1.000, 1.000] |
