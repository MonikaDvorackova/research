## A. Bayesian-Occam dissociation: truth at psi0 (E[P(true mechanism m2 | data)]; E[predictive KL])

| n | psi0 = 0.50 (non-generic) | 0.52 | 0.55 | 0.60 |
|---|---|---|---|---|
| 10 | 0.374 (KL 1.4e-02) | 0.375 (KL 1.4e-02) | 0.383 (KL 1.6e-02) | 0.410 (KL 2.3e-02) |
| 30 | 0.277 (KL 4.2e-03) | 0.282 (KL 4.7e-03) | 0.306 (KL 7.1e-03) | 0.390 (KL 1.5e-02) |
| 100 | 0.186 (KL 9.0e-04) | 0.200 (KL 1.5e-03) | 0.275 (KL 4.1e-03) | 0.521 (KL 9.3e-03) |
| 300 | 0.124 (KL 2.0e-04) | 0.161 (KL 8.1e-04) | 0.361 (KL 3.0e-03) | 0.846 (KL 3.4e-03) |
| 1000 | 0.077 (KL 3.8e-05) | 0.181 (KL 6.3e-04) | 0.714 (KL 1.3e-03) | 0.999 (KL 5.0e-04) |
| 3000 | 0.048 (KL 8.1e-06) | 0.340 (KL 4.8e-04) | 0.991 (KL 1.9e-04) | 1.000 (KL 1.7e-04) |
| 10000 | 0.029 (KL 1.4e-06) | 0.825 (KL 1.4e-04) | 1.000 (KL 5.0e-05) | 1.000 (KL 5.0e-05) |
| 30000 | 0.018 (KL 3.0e-07) | 1.000 (KL 1.7e-05) | 1.000 (KL 1.7e-05) | 1.000 (KL 1.7e-05) |

## B. Chernoff design exponent vs uniform and passive designs (X1 benchmark, seed 500, episodes as actions; truth vs the null class M)

| truth | exponent, uniform actions | exponent, passive (P(a=2)=0.02) | Chernoff-optimal | optimal / uniform | observed X1 speed-up of P4 over P2 (confirmatory) |
|---|---|---|---|---|---|
| pc0 | 1.71e-02 | 2.00e-02 | 3.71e-02 | 2.17 | 2.01 |
| pc1 | 2.39e-02 | 2.80e-02 | 5.69e-02 | 2.39 | 1.74 |
| pc2 | 2.37e-02 | 1.24e-03 | 6.10e-02 | 2.57 | 1.85 |
| t10 | 3.33e-02 | 2.99e-03 | 1.69e-01 | 5.08 | – |
| t05 | 8.61e-03 | 7.68e-04 | 4.83e-02 | 5.61 | – |

For pc0–pc2 (truth inside the alternative family) the oracle exponent is the relevant rate; for t05, t10 the e-process rate is the margin d_M − d_A, so the table gives only an upper bound.

## C. Statistical audit of binomial and clustered claims

- Zero rejections certify rate ≤ 0.07 at one-sided 95 % only with n ≥ 42 runs, rate ≤ 0.05 with n ≥ 59; 20 runs per structure give a bound of 0.139.

Probability that a pooled claim 'rate ≤ threshold' is demonstrated (one-sided CP, i.i.d. runs):

| runs n | true rate | threshold | level | P(claim demonstrated) |
|---|---|---|---|---|
| 200 | 0.02 | 0.05 | 0.05 | 0.629 |
| 200 | 0.02 | 0.05 | 0.05/24 (Bonferroni) | 0.089 |
| 200 | 0.02 | 0.07 | 0.05 | 0.951 |
| 200 | 0.02 | 0.07 | 0.05/24 (Bonferroni) | 0.629 |
| 200 | 0.05 | 0.05 | 0.05 | 0.026 |
| 200 | 0.05 | 0.05 | 0.05/24 (Bonferroni) | 0.000 |
| 200 | 0.05 | 0.07 | 0.05 | 0.213 |
| 200 | 0.05 | 0.07 | 0.05/24 (Bonferroni) | 0.026 |
| 600 | 0.02 | 0.05 | 0.05 | 0.989 |
| 600 | 0.02 | 0.05 | 0.05/24 (Bonferroni) | 0.847 |
| 600 | 0.02 | 0.07 | 0.05 | 1.000 |
| 600 | 0.02 | 0.07 | 0.05/24 (Bonferroni) | 0.999 |
| 600 | 0.05 | 0.05 | 0.05 | 0.032 |
| 600 | 0.05 | 0.05 | 0.05/24 (Bonferroni) | 0.002 |
| 600 | 0.05 | 0.07 | 0.05 | 0.620 |
| 600 | 0.05 | 0.07 | 0.05/24 (Bonferroni) | 0.151 |
| 1800 | 0.02 | 0.05 | 0.05 | 1.000 |
| 1800 | 0.02 | 0.05 | 0.05/24 (Bonferroni) | 1.000 |
| 1800 | 0.02 | 0.07 | 0.05 | 1.000 |
| 1800 | 0.02 | 0.07 | 0.05/24 (Bonferroni) | 1.000 |
| 1800 | 0.05 | 0.05 | 0.05 | 0.044 |
| 1800 | 0.05 | 0.05 | 0.05/24 (Bonferroni) | 0.002 |
| 1800 | 0.05 | 0.07 | 0.05 | 0.968 |
| 1800 | 0.05 | 0.07 | 0.05/24 (Bonferroni) | 0.728 |

X1 re-evaluated: 24 cells, max rejections 18/600; max 95 % UB = 0.0442; max UB at Bonferroni level 0.05/24 = 0.0558 (threshold used in the preregistration: 0.07; nominal alpha: 0.05).

Coverage of 95 % one-sided upper bounds for a boundary mean rate 0.05, m = 30 structures x R = 20 runs, 300 simulated datasets:

| intra-structure correlation | pooled Clopper-Pearson coverage | cluster-bootstrap coverage | cluster-level t bound coverage |
|---|---|---|---|
| 0.0 | 0.970 | 0.947 | 0.947 |
| 0.05 | 0.923 | 0.920 | 0.917 |
| 0.2 | 0.807 | 0.890 | 0.880 |
| 0.5 | 0.627 | 0.767 | 0.747 |

Number of structures m needed (R = 20 runs each, boundary mean 0.05, intra-structure correlation 0.2):

| m structures | pooled CP | cluster bootstrap | cluster t |
|---|---|---|---|
| 30 | 0.760 | 0.863 | 0.850 |
| 60 | 0.797 | 0.930 | 0.913 |
| 120 | 0.733 | 0.897 | 0.883 |
| 240 | 0.787 | 0.923 | 0.923 |

Power to REFUTE validity: true rate 0.10, pooled n=600, P(CP lower bound at 95 % > 0.05) = 0.998; at true rate 0.07: 0.648.

## D. Pure policy shift under a misspecified order-1 class: exact discrepancy E_ctx~pi2 KL(k1||k2) per hidden-state instance (mechanism fixed)

| instance | S | order-1 plateau (misspecification) | discrepancy uniform -> extreme(0.9 on action 2) | discrepancy no-action-2 -> uniform |
|---|---|---|---|---|
| 0 | 5 | 3.83e-03 | 4.65e-04 | 1.31e-04 |
| 1 | 4 | 3.40e-02 | 1.85e-03 | 2.54e-03 |
| 2 | 5 | 9.52e-03 | 6.38e-04 | 2.33e-04 |
| 3 | 5 | 2.43e-03 | 3.71e-04 | 8.83e-05 |
| 4 | 6 | 1.17e-02 | 5.06e-04 | 4.74e-04 |
| 5 | 6 | 2.41e-02 | 1.25e-03 | 1.89e-04 |
| 6 | 6 | 5.55e-03 | 8.58e-04 | 1.75e-04 |
| 7 | 5 | 9.61e-03 | 3.97e-04 | 1.13e-04 |
| 8 | 3 | 7.85e-03 | 1.09e-04 | 2.23e-05 |
| 9 | 6 | 4.89e-03 | 8.27e-06 | 4.56e-06 |
