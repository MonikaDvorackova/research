# Post hoc equivalence tests on frozen Phase 4 results

Margins fixed before running: 0.10 (AUROC, architecture/sample claims); 0.05 (negative control around 0.5). Seed-paired TOST (n = 10), Holm-adjusted within each family. 'not established' does not mean 'different'.

## Family A: AUROC (W vs controls) of each condition minus the baseline, quality 3

| condition | cell | difference [95% CI] | TOST p | Holm p | equivalent within ±0.10 |
|---|---|---|---|---|---|
| independent training sample | wide T=10 | +0.008 [-0.010, +0.033] | 0.0000 | 0.0001 | yes |
| independent training sample | wide T=50 | +0.000 [-0.000, +0.000] | 0.0000 | 0.0000 | yes |
| independent training sample | active T=10 | +0.000 [+0.000, +0.000] | 0.0000 | 0.0000 | yes |
| ReLU theory | wide T=10 | +0.058 [+0.033, +0.085] | 0.0074 | 0.0074 | yes |
| ReLU theory | wide T=50 | +0.012 [+0.006, +0.019] | 0.0000 | 0.0000 | yes |
| ReLU theory | active T=10 | +0.010 [+0.001, +0.026] | 0.0000 | 0.0000 | yes |
| W = ReLU, theory tanh | wide T=10 | +0.030 [+0.009, +0.051] | 0.0001 | 0.0002 | yes |
| W = ReLU, theory tanh | wide T=50 | +0.002 [+0.000, +0.004] | 0.0000 | 0.0000 | yes |
| W = ReLU, theory tanh | active T=10 | +0.000 [+0.000, +0.000] | 0.0000 | 0.0000 | yes |
| W = ReLU, theory ReLU | wide T=10 | -0.030 [-0.040, -0.019] | 0.0000 | 0.0000 | yes |
| W = ReLU, theory ReLU | wide T=50 | -0.000 [-0.000, +0.000] | 0.0000 | 0.0000 | yes |
| W = ReLU, theory ReLU | active T=10 | +0.000 [+0.000, +0.000] | 0.0000 | 0.0000 | yes |

## Family B: negative control, AUROC(E0 vs E0split) - 0.5, all nine conditions, quality 3

| condition | cell | deviation from 0.5 [95% CI] | TOST p | Holm p | equivalent within ±0.05 |
|---|---|---|---|---|---|
| poc_v2 | wide T=10 | -0.005 [-0.019, +0.008] | 0.0001 | 0.0016 | yes |
| poc_v2 | wide T=50 | -0.006 [-0.024, +0.013] | 0.0007 | 0.0066 | yes |
| poc_v2 | active T=10 | +0.001 [-0.014, +0.018] | 0.0002 | 0.0029 | yes |
| abl_qindep | wide T=10 | -0.009 [-0.022, +0.004] | 0.0001 | 0.0027 | yes |
| abl_qindep | wide T=50 | -0.006 [-0.023, +0.011] | 0.0005 | 0.0055 | yes |
| abl_qindep | active T=10 | -0.010 [-0.018, -0.003] | 0.0000 | 0.0001 | yes |
| abl_relu128 | wide T=10 | -0.005 [-0.016, +0.003] | 0.0000 | 0.0001 | yes |
| abl_relu128 | wide T=50 | +0.001 [-0.022, +0.025] | 0.0018 | 0.0073 | yes |
| abl_relu128 | active T=10 | -0.004 [-0.019, +0.011] | 0.0002 | 0.0031 | yes |
| abl_wrelu_qtanh | wide T=10 | -0.005 [-0.019, +0.008] | 0.0001 | 0.0016 | yes |
| abl_wrelu_qtanh | wide T=50 | -0.006 [-0.024, +0.013] | 0.0007 | 0.0066 | yes |
| abl_wrelu_qtanh | active T=10 | +0.001 [-0.014, +0.018] | 0.0002 | 0.0029 | yes |
| abl_wrelu_qrelu | wide T=10 | -0.005 [-0.016, +0.003] | 0.0000 | 0.0001 | yes |
| abl_wrelu_qrelu | wide T=50 | +0.001 [-0.022, +0.025] | 0.0018 | 0.0073 | yes |
| abl_wrelu_qrelu | active T=10 | -0.004 [-0.019, +0.011] | 0.0002 | 0.0031 | yes |
| abl_poly3 | wide T=10 | -0.008 [-0.026, +0.010] | 0.0010 | 0.0069 | yes |
| abl_poly3 | wide T=50 | +0.001 [-0.016, +0.021] | 0.0005 | 0.0055 | yes |
| abl_poly3 | active T=10 | -0.010 [-0.026, +0.006] | 0.0006 | 0.0059 | yes |
| abl_qwide | wide T=10 | +0.004 [-0.014, +0.019] | 0.0003 | 0.0040 | yes |
| abl_qwide | wide T=50 | +0.005 [-0.003, +0.014] | 0.0000 | 0.0001 | yes |
| abl_qwide | active T=10 | +0.011 [-0.001, +0.023] | 0.0001 | 0.0026 | yes |
| abl_analytic | wide T=10 | -0.006 [-0.023, +0.009] | 0.0003 | 0.0044 | yes |
| abl_analytic | wide T=50 | -0.015 [-0.030, -0.000] | 0.0012 | 0.0070 | yes |
| abl_analytic | active T=10 | +0.002 [-0.013, +0.018] | 0.0001 | 0.0027 | yes |
| adaptive_tanh | wide T=10 | +0.003 [-0.017, +0.025] | 0.0014 | 0.0071 | yes |
| adaptive_tanh | wide T=50 | +0.017 [-0.021, +0.059] | 0.0818 | 0.1635 | not established |
| adaptive_tanh | active T=10 | +0.011 [-0.118, +0.131] | 0.2912 | 0.2912 | not established |
