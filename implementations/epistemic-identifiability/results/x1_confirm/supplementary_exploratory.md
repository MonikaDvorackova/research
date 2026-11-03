## S1 Type-I error with the seed as the unit (cluster bootstrap over 30 seeds; EXPLORATORY)

| policy | pooled rate over 4 null truths | seed-cluster 95% interval | max over seeds |
|---|---|---|---|
| P0 | 0.0142 | [0.0100, 0.0183] | 0.038 |
| P1 | 0.0179 | [0.0129, 0.0233] | 0.038 |
| P2 | 0.0154 | [0.0108, 0.0200] | 0.050 |
| P3 | 0.0125 | [0.0079, 0.0175] | 0.050 |
| P4 | 0.0204 | [0.0146, 0.0267] | 0.062 |
| P5 | 0.0213 | [0.0154, 0.0275] | 0.062 |

Overall 0.0169, seed-cluster 95% interval [0.0151, 0.0189]. Independent units: 30 environment instances (seeds), each with R=20 runs per cell; runs within a seed share the POMDP, class and W, so the effective sample is closer to 30 than to 600 per cell.

## S2 Detection probability, censoring, conditional detection time and quantiles (EXPLORATORY)

Quantiles are of the time to rejection over ALL runs (censored runs counted at N+1; a quantile above N is reported as '>N').

| truth | policy | P(detect <= 3000) [seed-cluster 95%] | censored | mean episodes given detection | q25 | q50 | q75 |
|---|---|---|---|---|---|---|---|
| pc0 | P0 | 1.000 [1.000, 1.000] | 0.000 | 262 | 155 | 226 | 334 |
| pc0 | P1 | 1.000 [1.000, 1.000] | 0.000 | 258 | 141 | 219 | 330 |
| pc0 | P2 | 1.000 [1.000, 1.000] | 0.000 | 288 | 152 | 246 | 364 |
| pc0 | P3 | 1.000 [1.000, 1.000] | 0.000 | 219 | 90 | 157 | 278 |
| pc0 | P4 | 1.000 [1.000, 1.000] | 0.000 | 143 | 69 | 110 | 185 |
| pc0 | P5 | 1.000 [1.000, 1.000] | 0.000 | 160 | 81 | 131 | 211 |
| pc1 | P0 | 1.000 [1.000, 1.000] | 0.000 | 245 | 116 | 196 | 314 |
| pc1 | P1 | 1.000 [1.000, 1.000] | 0.000 | 255 | 124 | 204 | 344 |
| pc1 | P2 | 1.000 [1.000, 1.000] | 0.000 | 320 | 157 | 258 | 418 |
| pc1 | P3 | 0.318 [0.187, 0.460] | 0.682 | 1368 | 2050 | >N | >N |
| pc1 | P4 | 1.000 [1.000, 1.000] | 0.000 | 185 | 72 | 141 | 235 |
| pc1 | P5 | 1.000 [1.000, 1.000] | 0.000 | 162 | 80 | 132 | 210 |
| pc2 | P0 | 0.012 [0.005, 0.020] | 0.988 | 150 | >N | >N | >N |
| pc2 | P1 | 0.558 [0.483, 0.632] | 0.442 | 1642 | 1412 | 2680 | >N |
| pc2 | P2 | 1.000 [1.000, 1.000] | 0.000 | 227 | 116 | 194 | 295 |
| pc2 | P3 | 0.805 [0.708, 0.898] | 0.195 | 1146 | 679 | 1254 | 2444 |
| pc2 | P4 | 1.000 [1.000, 1.000] | 0.000 | 125 | 53 | 98 | 162 |
| pc2 | P5 | 1.000 [1.000, 1.000] | 0.000 | 108 | 56 | 92 | 142 |
| t10 | P0 | 0.008 [0.002, 0.015] | 0.992 | 458 | >N | >N | >N |
| t10 | P1 | 0.083 [0.057, 0.113] | 0.917 | 1740 | >N | >N | >N |
| t10 | P2 | 0.943 [0.898, 0.980] | 0.057 | 856 | 416 | 760 | 1269 |
| t10 | P3 | 0.222 [0.128, 0.327] | 0.778 | 1582 | >N | >N | >N |
| t10 | P4 | 0.830 [0.742, 0.912] | 0.170 | 666 | 286 | 609 | 1508 |
| t10 | P5 | 0.733 [0.617, 0.833] | 0.267 | 768 | 372 | 888 | >N |
| t05 | P0 | 0.010 [0.003, 0.020] | 0.990 | 862 | >N | >N | >N |
| t05 | P1 | 0.048 [0.030, 0.068] | 0.952 | 1384 | >N | >N | >N |
| t05 | P2 | 0.412 [0.332, 0.493] | 0.588 | 1543 | 1779 | >N | >N |
| t05 | P3 | 0.047 [0.022, 0.080] | 0.953 | 1655 | >N | >N | >N |
| t05 | P4 | 0.550 [0.425, 0.670] | 0.450 | 1231 | 1027 | 2442 | >N |
| t05 | P5 | 0.352 [0.237, 0.477] | 0.648 | 1170 | 1534 | >N | >N |

Note: conditional means are biased low when detection is rare (they condition on the fast tail); use the probabilities and RMST for comparisons.

## S3 Efficiency ratios at different intervention budgets (RMST restricted at cap; geometric mean over seeds, seed-bootstrap 95%; EXPLORATORY)

| comparison | truth | cap=250 | cap=500 | cap=1000 | cap=3000 |
|---|---|---|---|---|---|
| RMST(P2)/RMST(P4) | pc0 | 1.60 [1.50,1.71] | 1.90 [1.77,2.05] | 2.01 [1.85,2.17] | 2.01 [1.86,2.18] |
| RMST(P2)/RMST(P4) | pc1 | 1.43 [1.33,1.53] | 1.65 [1.53,1.79] | 1.73 [1.58,1.91] | 1.74 [1.58,1.90] |
| RMST(P2)/RMST(P4) | pc2 | 1.60 [1.50,1.71] | 1.82 [1.69,1.97] | 1.84 [1.71,2.00] | 1.85 [1.71,1.99] |
| RMST(P2)/RMST(P4) | t05 | 1.01 [1.00,1.03] | 1.03 [1.01,1.05] | 1.07 [1.04,1.10] | 1.24 [1.13,1.36] |
| RMST(P2)/RMST(P4) | t10 | 1.04 [1.01,1.07] | 1.10 [1.03,1.16] | 1.16 [1.05,1.28] | 1.02 [0.86,1.22] |
| RMST(P5)/RMST(P4) | pc0 | 1.13 [1.04,1.24] | 1.13 [1.03,1.25] | 1.13 [1.02,1.25] | 1.13 [1.02,1.26] |
| RMST(P5)/RMST(P4) | pc1 | 0.97 [0.89,1.05] | 0.91 [0.81,1.01] | 0.87 [0.77,0.98] | 0.87 [0.77,0.98] |
| RMST(P5)/RMST(P4) | pc2 | 0.92 [0.86,0.98] | 0.88 [0.83,0.94] | 0.88 [0.82,0.93] | 0.88 [0.82,0.93] |
| RMST(P5)/RMST(P4) | t05 | 1.01 [1.00,1.02] | 1.02 [1.00,1.04] | 1.04 [1.00,1.08] | 1.18 [1.06,1.31] |
| RMST(P5)/RMST(P4) | t10 | 1.03 [0.99,1.06] | 1.06 [1.00,1.13] | 1.14 [1.03,1.28] | 1.29 [1.07,1.55] |
| RMST(P2)/RMST(P5) | pc0 | 1.41 [1.32,1.51] | 1.68 [1.55,1.82] | 1.77 [1.62,1.95] | 1.78 [1.61,1.95] |
| RMST(P2)/RMST(P5) | pc1 | 1.47 [1.37,1.60] | 1.82 [1.66,1.98] | 1.99 [1.83,2.17] | 2.00 [1.83,2.17] |
| RMST(P2)/RMST(P5) | pc2 | 1.74 [1.65,1.86] | 2.06 [1.94,2.19] | 2.10 [1.99,2.23] | 2.11 [1.99,2.23] |
| RMST(P2)/RMST(P5) | t05 | 1.00 [0.99,1.01] | 1.01 [1.00,1.03] | 1.03 [1.01,1.06] | 1.05 [0.97,1.15] |
| RMST(P2)/RMST(P5) | t10 | 1.01 [0.98,1.05] | 1.03 [0.97,1.10] | 1.01 [0.91,1.14] | 0.80 [0.64,1.00] |
| RMST(P2)/RMST(P3) | pc0 | 1.31 [1.17,1.47] | 1.43 [1.21,1.70] | 1.44 [1.19,1.73] | 1.44 [1.18,1.74] |
| RMST(P2)/RMST(P3) | pc1 | 0.81 [0.77,0.84] | 0.55 [0.50,0.60] | 0.32 [0.28,0.36] | 0.13 [0.11,0.16] |
| RMST(P2)/RMST(P3) | pc2 | 0.72 [0.68,0.76] | 0.46 [0.42,0.50] | 0.28 [0.24,0.32] | 0.17 [0.14,0.22] |
| RMST(P2)/RMST(P3) | t05 | 0.99 [0.98,1.00] | 0.98 [0.96,0.99] | 0.95 [0.93,0.97] | 0.81 [0.76,0.85] |
| RMST(P2)/RMST(P3) | t10 | 0.95 [0.93,0.96] | 0.87 [0.84,0.89] | 0.69 [0.64,0.75] | 0.34 [0.28,0.40] |

## S4 Independent recomputation of the primary ratios and robustness (jackknife; 99% bootstrap; different RNG; exact CIs)

| comparison | truth | primary-style estimate | jackknife SE of log ratio | 99% bootstrap lower bound | jackknife-based 95% lower bound |
|---|---|---|---|---|---|
| RMST(P2)/RMST(P4) | pc0 | 2.01 | 0.040 | 1.82 | 1.85 |
| RMST(P2)/RMST(P4) | pc1 | 1.74 | 0.048 | 1.54 | 1.58 |
| RMST(P2)/RMST(P4) | pc2 | 1.85 | 0.041 | 1.66 | 1.70 |
| RMST(P2)/RMST(P4) | t05 | 1.24 | 0.049 | 1.10 | 1.12 |
| RMST(P2)/RMST(P4) | t10 | 1.02 | 0.092 | 0.81 | 0.85 |
| RMST(P5)/RMST(P4) | pc0 | 1.13 | 0.053 | 0.99 | 1.02 |
| RMST(P5)/RMST(P4) | pc1 | 0.87 | 0.063 | 0.74 | 0.77 |
| RMST(P5)/RMST(P4) | pc2 | 0.88 | 0.033 | 0.80 | 0.82 |

(Primary results used lower bounds: P2/P4 pc0 1.86, pc1 1.59, pc2 1.71; P5/P4 upper bounds pc0 1.25, pc1 0.98, pc2 0.93. All reproduce.)

Exact (Clopper–Pearson via scipy.binomtest) upper 95% bounds, null truths pooled per policy: P0: 34/2400 -> 0.0197; P1: 43/2400 -> 0.0241; P2: 37/2400 -> 0.0212; P3: 30/2400 -> 0.0178; P4: 49/2400 -> 0.0269; P5: 51/2400 -> 0.0278

## S5 Exact rate prediction versus observed (EXPLORATORY)

Predicted episodes for E[log E] to reach ln(K/alpha) = ln(46*20) = 6.82 under uniform random actions (q=1/3): 6.82/(d_M − d_A) (approximation: ignores stochastic fluctuation and the policy's non-stationarity). Compared with the observed median of P2.

| truth | median margin d_M − d_A over seeds | predicted episodes (median margin) | observed median episodes, P2 |
|---|---|---|---|
| pc0 | 2.23e-02 | 306 | 246 |
| pc1 | 2.17e-02 | 314 | 258 |
| pc2 | 2.67e-02 | 255 | 193 |
| t10 | 6.26e-03 | 1089 | 760 |
| t05 | 6.91e-04 | 9874 | >3000 |
