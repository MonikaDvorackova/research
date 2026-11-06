# Seed-paired comparison against the baseline fixed observer (quality 3)

Difference = condition minus baseline, mean over seeds [bootstrap 95% CI]. Practical threshold: 0.10 for AUROC, 0.05 for rates.
Holm-adjusted Wilcoxon p-values within each metric family (all conditions x cells). With 10 seeds the smallest attainable two-sided p is 0.002.

## FPR (alpha=0.05)

| condition | cell | difference | Holm p | statistically significant (p<0.05) | practically significant | reading |
|---|---|---|---|---|---|---|
| independently trained theory (fresh E0 sample) | passive T=50 | -0.006 [-0.014, +0.003] | 1.000 | no | no | neither |
| independently trained theory (fresh E0 sample) | wide T=10 | -0.018 [-0.065, +0.018] | 1.000 | no | no | neither |
| independently trained theory (fresh E0 sample) | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| ReLU theory | passive T=50 | +0.023 [+0.004, +0.047] | 0.844 | no | no | neither |
| ReLU theory | wide T=10 | +0.091 [+0.077, +0.105] | 0.047 | yes | yes | both |
| ReLU theory | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| polynomial theory | passive T=50 | -0.017 [-0.031, -0.004] | 0.586 | no | no | neither |
| polynomial theory | wide T=10 | -0.304 [-0.537, -0.091] | 0.684 | no | yes | practical only (not established by 10 seeds) |
| polynomial theory | active T=10 | -0.168 [-0.403, +0.000] | 1.000 | no | yes | practical only (not established by 10 seeds) |
| theory trained over probed range | passive T=50 | +0.012 [-0.002, +0.028] | 1.000 | no | no | neither |
| theory trained over probed range | wide T=10 | -0.833 [-0.846, -0.817] | 0.047 | yes | yes | both |
| theory trained over probed range | active T=10 | -0.935 [-0.943, -0.927] | 0.047 | yes | yes | both |
| analytic true-law theory | passive T=50 | -0.020 [-0.033, -0.008] | 0.219 | no | no | neither |
| analytic true-law theory | wide T=10 | -0.835 [-0.849, -0.818] | 0.047 | yes | yes | both |
| analytic true-law theory | active T=10 | -0.945 [-0.951, -0.940] | 0.047 | yes | yes | both |
| W=ReLU, theory=tanh (architectures differ) | passive T=50 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | wide T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| W=ReLU, theory=ReLU (architectures shared) | passive T=50 | +0.023 [+0.004, +0.047] | 0.844 | no | no | neither |
| W=ReLU, theory=ReLU (architectures shared) | wide T=10 | +0.091 [+0.077, +0.105] | 0.047 | yes | yes | both |
| W=ReLU, theory=ReLU (architectures shared) | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | passive T=50 | -0.015 [-0.028, -0.002] | 0.711 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | wide T=10 | -0.829 [-0.844, -0.811] | 0.047 | yes | yes | both |
| adaptive observer (fine-tunes on interaction) | active T=10 | -0.863 [-0.926, -0.798] | 0.047 | yes | yes | both |

## TPR on W

| condition | cell | difference | Holm p | statistically significant (p<0.05) | practically significant | reading |
|---|---|---|---|---|---|---|
| independently trained theory (fresh E0 sample) | passive T=50 | +0.003 [-0.012, +0.021] | 1.000 | no | no | neither |
| independently trained theory (fresh E0 sample) | wide T=10 | +0.014 [+0.001, +0.030] | 0.742 | no | no | neither |
| independently trained theory (fresh E0 sample) | active T=10 | -0.038 [-0.109, +0.014] | 1.000 | no | no | neither |
| ReLU theory | passive T=50 | +0.160 [+0.108, +0.212] | 0.047 | yes | yes | both |
| ReLU theory | wide T=10 | +0.666 [+0.616, +0.719] | 0.047 | yes | yes | both |
| ReLU theory | active T=10 | +0.647 [+0.457, +0.812] | 0.047 | yes | yes | both |
| polynomial theory | passive T=50 | +0.071 [+0.032, +0.117] | 0.102 | no | yes | practical only (not established by 10 seeds) |
| polynomial theory | wide T=10 | +0.904 [+0.891, +0.917] | 0.047 | yes | yes | both |
| polynomial theory | active T=10 | +0.877 [+0.809, +0.921] | 0.047 | yes | yes | both |
| theory trained over probed range | passive T=50 | +0.007 [-0.019, +0.040] | 1.000 | no | no | neither |
| theory trained over probed range | wide T=10 | +0.897 [+0.887, +0.907] | 0.047 | yes | yes | both |
| theory trained over probed range | active T=10 | +0.855 [+0.787, +0.913] | 0.047 | yes | yes | both |
| analytic true-law theory | passive T=50 | +0.059 [+0.027, +0.098] | 0.164 | no | yes | practical only (not established by 10 seeds) |
| analytic true-law theory | wide T=10 | +0.901 [+0.891, +0.913] | 0.047 | yes | yes | both |
| analytic true-law theory | active T=10 | +0.877 [+0.809, +0.921] | 0.047 | yes | yes | both |
| W=ReLU, theory=tanh (architectures differ) | passive T=50 | +0.016 [-0.049, +0.071] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | wide T=10 | +0.033 [-0.010, +0.078] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | active T=10 | +0.195 [+0.048, +0.356] | 0.742 | no | yes | practical only (not established by 10 seeds) |
| W=ReLU, theory=ReLU (architectures shared) | passive T=50 | +0.115 [+0.040, +0.196] | 0.193 | no | yes | practical only (not established by 10 seeds) |
| W=ReLU, theory=ReLU (architectures shared) | wide T=10 | +0.212 [+0.144, +0.279] | 0.047 | yes | yes | both |
| W=ReLU, theory=ReLU (architectures shared) | active T=10 | +0.490 [+0.306, +0.665] | 0.047 | yes | yes | both |
| adaptive observer (fine-tunes on interaction) | passive T=50 | -0.010 [-0.040, +0.016] | 1.000 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | wide T=10 | -0.010 [-0.020, +0.001] | 0.742 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | active T=10 | -0.034 [-0.113, +0.031] | 1.000 | no | no | neither |

## AUROC W vs controls

| condition | cell | difference | Holm p | statistically significant (p<0.05) | practically significant | reading |
|---|---|---|---|---|---|---|
| independently trained theory (fresh E0 sample) | passive T=50 | +0.016 [-0.001, +0.035] | 1.000 | no | no | neither |
| independently trained theory (fresh E0 sample) | wide T=10 | +0.008 [-0.010, +0.033] | 1.000 | no | no | neither |
| independently trained theory (fresh E0 sample) | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| ReLU theory | passive T=50 | +0.103 [+0.067, +0.140] | 0.047 | yes | yes | both |
| ReLU theory | wide T=10 | +0.058 [+0.033, +0.085] | 0.047 | yes | no | statistical only (small effect) |
| ReLU theory | active T=10 | +0.010 [+0.001, +0.026] | 0.312 | no | no | neither |
| polynomial theory | passive T=50 | +0.076 [+0.042, +0.111] | 0.047 | yes | no | statistical only (small effect) |
| polynomial theory | wide T=10 | +0.892 [+0.862, +0.916] | 0.047 | yes | yes | both |
| polynomial theory | active T=10 | +1.000 [+1.000, +1.000] | 0.047 | yes | yes | both |
| theory trained over probed range | passive T=50 | -0.010 [-0.044, +0.028] | 1.000 | no | no | neither |
| theory trained over probed range | wide T=10 | +0.929 [+0.919, +0.938] | 0.047 | yes | yes | both |
| theory trained over probed range | active T=10 | +0.989 [+0.975, +1.000] | 0.047 | yes | yes | both |
| analytic true-law theory | passive T=50 | +0.074 [+0.043, +0.107] | 0.047 | yes | no | statistical only (small effect) |
| analytic true-law theory | wide T=10 | +0.932 [+0.923, +0.941] | 0.047 | yes | yes | both |
| analytic true-law theory | active T=10 | +1.000 [+1.000, +1.000] | 0.047 | yes | yes | both |
| W=ReLU, theory=tanh (architectures differ) | passive T=50 | +0.020 [-0.043, +0.071] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | wide T=10 | +0.030 [+0.009, +0.051] | 0.301 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| W=ReLU, theory=ReLU (architectures shared) | passive T=50 | +0.082 [+0.022, +0.141] | 0.439 | no | no | neither |
| W=ReLU, theory=ReLU (architectures shared) | wide T=10 | -0.030 [-0.040, -0.019] | 0.047 | yes | no | statistical only (small effect) |
| W=ReLU, theory=ReLU (architectures shared) | active T=10 | +0.000 [+0.000, +0.000] | 1.000 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | passive T=50 | +0.022 [-0.001, +0.044] | 0.672 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | wide T=10 | +0.435 [+0.419, +0.450] | 0.047 | yes | yes | both |
| adaptive observer (fine-tunes on interaction) | active T=10 | +0.432 [+0.369, +0.497] | 0.047 | yes | yes | both |

## balanced accuracy

| condition | cell | difference | Holm p | statistically significant (p<0.05) | practically significant | reading |
|---|---|---|---|---|---|---|
| independently trained theory (fresh E0 sample) | passive T=50 | +0.004 [-0.006, +0.014] | 1.000 | no | no | neither |
| independently trained theory (fresh E0 sample) | wide T=10 | +0.016 [-0.002, +0.039] | 0.957 | no | no | neither |
| independently trained theory (fresh E0 sample) | active T=10 | -0.019 [-0.055, +0.007] | 1.000 | no | no | neither |
| ReLU theory | passive T=50 | +0.068 [+0.043, +0.095] | 0.047 | yes | yes | both |
| ReLU theory | wide T=10 | +0.288 [+0.264, +0.313] | 0.047 | yes | yes | both |
| ReLU theory | active T=10 | +0.323 [+0.228, +0.406] | 0.047 | yes | yes | both |
| polynomial theory | passive T=50 | +0.044 [+0.023, +0.069] | 0.047 | yes | no | statistical only (small effect) |
| polynomial theory | wide T=10 | +0.604 [+0.501, +0.718] | 0.047 | yes | yes | both |
| polynomial theory | active T=10 | +0.522 [+0.425, +0.649] | 0.047 | yes | yes | both |
| theory trained over probed range | passive T=50 | -0.003 [-0.021, +0.018] | 1.000 | no | no | neither |
| theory trained over probed range | wide T=10 | +0.865 [+0.855, +0.874] | 0.047 | yes | yes | both |
| theory trained over probed range | active T=10 | +0.895 [+0.861, +0.923] | 0.047 | yes | yes | both |
| analytic true-law theory | passive T=50 | +0.040 [+0.020, +0.061] | 0.195 | no | no | neither |
| analytic true-law theory | wide T=10 | +0.868 [+0.857, +0.878] | 0.047 | yes | yes | both |
| analytic true-law theory | active T=10 | +0.911 [+0.878, +0.934] | 0.047 | yes | yes | both |
| W=ReLU, theory=tanh (architectures differ) | passive T=50 | +0.008 [-0.025, +0.035] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | wide T=10 | +0.017 [-0.005, +0.039] | 1.000 | no | no | neither |
| W=ReLU, theory=tanh (architectures differ) | active T=10 | +0.098 [+0.024, +0.178] | 0.594 | no | yes | practical only (not established by 10 seeds) |
| W=ReLU, theory=ReLU (architectures shared) | passive T=50 | +0.046 [+0.011, +0.087] | 0.580 | no | no | neither |
| W=ReLU, theory=ReLU (architectures shared) | wide T=10 | +0.061 [+0.027, +0.093] | 0.107 | no | yes | practical only (not established by 10 seeds) |
| W=ReLU, theory=ReLU (architectures shared) | active T=10 | +0.245 [+0.153, +0.332] | 0.047 | yes | yes | both |
| adaptive observer (fine-tunes on interaction) | passive T=50 | +0.002 [-0.012, +0.015] | 1.000 | no | no | neither |
| adaptive observer (fine-tunes on interaction) | wide T=10 | +0.409 [+0.401, +0.418] | 0.047 | yes | yes | both |
| adaptive observer (fine-tunes on interaction) | active T=10 | +0.414 [+0.366, +0.460] | 0.047 | yes | yes | both |
