# X1 analysis (results/x1_confirm)

seeds 600..629 (n=30), R=20, N=3000, T=4, alpha=0.05


## H1 Type-I error (truth in M)

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| E0 | 11/600 (UB 0.030) | 8/600 (UB 0.024) | 14/600 (UB 0.036) | 13/600 (UB 0.034) | 10/600 (UB 0.028) | 15/600 (UB 0.038) |
| split | 8/600 (UB 0.024) | 16/600 (UB 0.040) | 9/600 (UB 0.026) | 6/600 (UB 0.020) | 18/600 (UB 0.044) | 8/600 (UB 0.024) |
| n10 | 9/600 (UB 0.026) | 15/600 (UB 0.038) | 8/600 (UB 0.024) | 7/600 (UB 0.022) | 12/600 (UB 0.032) | 15/600 (UB 0.038) |
| n20 | 6/600 (UB 0.020) | 4/600 (UB 0.015) | 6/600 (UB 0.020) | 4/600 (UB 0.015) | 9/600 (UB 0.026) | 13/600 (UB 0.034) |

Pooled 244/14400 = 0.0169 (CP lower 0.0152); all cell UB <= 0.07: True. **H1: supported**

## H2 Barrier (policy P0 never uses action 2; these truths equal a member's law on that class)

t05: 6/600 (UB 0.020); t10: 5/600 (UB 0.017); pc2: 7/600 (UB 0.022). **H2: supported**

## H3 Power of random wide intervention (P2): rejection rate within budget

| truth | 100 | 200 | 400 | 800 | 1500 | 3000 |
|---|---|---|---|---|---|---|
| pc0 | 0.118 | 0.375 | 0.787 | 0.975 | 1.000 | 1.000 |
| pc1 | 0.082 | 0.375 | 0.735 | 0.952 | 1.000 | 1.000 |
| pc2 | 0.185 | 0.517 | 0.878 | 0.997 | 1.000 | 1.000 |
| t05 | 0.013 | 0.018 | 0.035 | 0.083 | 0.193 | 0.412 |
| t10 | 0.030 | 0.113 | 0.242 | 0.517 | 0.803 | 0.943 |

Criterion: P2 rejection within 1500 episodes >= 0.8 for pc0, pc1, pc2. **H3: supported**


## H4 Efficiency of class-level design P4 (primary comparator: random P2)


### H4a anticipated deviations: RMST(P2) / RMST(P4) (restricted at N=3000; >1 means P4 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| pc0 | 2.01 | [1.86, 2.18] |
| pc1 | 1.74 | [1.59, 1.91] |
| pc2 | 1.85 | [1.71, 1.99] |

**H4a (lower CI bound >= 1.5 for all of pc0, pc1, pc2): supported**


### H4b unanticipated deviations: RMST(P2) / RMST(P4) (restricted at N=3000; >1 means P4 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| t05 | 1.24 | [1.13, 1.36] |
| t10 | 1.02 | [0.86, 1.22] |

**H4b (same criterion for t05, t10): contradicted**


## H4c Fair comparator: P5 (within-class EIG over M u W) vs P4 (same information, different target)


### H4c: RMST(P5) / RMST(P4) (restricted at N=3000; >1 means P4 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| pc0 | 1.13 | [1.02, 1.25] |
| pc1 | 0.87 | [0.77, 0.98] |
| pc2 | 0.88 | [0.82, 0.93] |
| t05 | 1.18 | [1.07, 1.31] |
| t10 | 1.29 | [1.08, 1.57] |

**H4c (anticipated truths, lower CI bound >= 1.5): contradicted**


## H5 Within-class EIG over M only (P3) is not faster than random (P2)


### H5: RMST(P2) / RMST(P3) (restricted at N=3000; >1 means P3 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| pc0 | 1.44 | [1.19, 1.74] |
| pc1 | 0.13 | [0.11, 0.16] |
| pc2 | 0.17 | [0.14, 0.22] |
| t05 | 0.81 | [0.76, 0.85] |
| t10 | 0.34 | [0.28, 0.40] |

**H5 (upper CI bound < 1.5 for pc0, pc1, pc2 => supported; any lower bound >= 1.5 => contradicted): inconclusive**


Rate of rejection within the budget, all non-null truths:

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| pc0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| pc1 | 1.000 | 1.000 | 1.000 | 0.318 | 1.000 | 1.000 |
| pc2 | 0.012 | 0.558 | 1.000 | 0.805 | 1.000 | 1.000 |
| t05 | 0.010 | 0.048 | 0.412 | 0.047 | 0.550 | 0.352 |
| t10 | 0.008 | 0.083 | 0.943 | 0.222 | 0.830 | 0.733 |
| shift | 0.023 | 0.025 | 0.017 | 0.017 | 0.037 | 0.025 |

Median episodes-to-reject (N+1 = censored):

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| pc0 | 226 | 219 | 246 | 157 | 110 | 131 |
| pc1 | 196 | 204 | 258 | 3001 | 141 | 132 |
| pc2 | 3001 | 2680 | 194 | 1254 | 98 | 92 |
| t05 | 3001 | 3001 | 3001 | 3001 | 2442 | 3001 |
| t10 | 3001 | 3001 | 760 | 3001 | 609 | 888 |

## Computational cost (run-seconds per policy, summed)

P0: 1572, P1: 1702, P2: 1232, P3: 3951, P4: 3265, P5: 3180


## Summary of decisions

```json
{
 "H1": "supported",
 "H2": "supported",
 "H3": "supported",
 "H4a": "supported",
 "H4b": "contradicted",
 "H4c": "contradicted",
 "H5": "inconclusive"
}
```
