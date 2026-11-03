# X1 analysis (results/x1_dev)

seeds 500..505 (n=6), R=20, N=1500, T=4, alpha=0.05


## H1 Type-I error (truth in M)

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| E0 | 2/120 (UB 0.052) | 0/120 (UB 0.025) | 3/120 (UB 0.063) | 0/120 (UB 0.025) | 5/120 (UB 0.086) | 1/120 (UB 0.039) |
| split | 1/120 (UB 0.039) | 0/120 (UB 0.025) | 3/120 (UB 0.063) | 0/120 (UB 0.025) | 1/120 (UB 0.039) | 0/120 (UB 0.025) |
| n10 | 2/120 (UB 0.052) | 4/120 (UB 0.075) | 2/120 (UB 0.052) | 0/120 (UB 0.025) | 8/120 (UB 0.117) | 4/120 (UB 0.075) |
| n20 | 4/120 (UB 0.075) | 1/120 (UB 0.039) | 2/120 (UB 0.052) | 2/120 (UB 0.052) | 1/120 (UB 0.039) | 1/120 (UB 0.039) |

Pooled 47/2880 = 0.0163 (CP lower 0.0126); all cell UB <= 0.07: False. **H1: inconclusive**

## H2 Barrier (policy P0 never uses action 2; these truths equal a member's law on that class)

t05: 2/120 (UB 0.052); t10: 0/120 (UB 0.025); pc2: 0/120 (UB 0.025). **H2: supported**

## H3 Power of random wide intervention (P2): rejection rate within budget

| truth | 100 | 200 | 400 | 800 | 1500 |
|---|---|---|---|---|---|
| pc0 | 0.033 | 0.250 | 0.617 | 0.950 | 1.000 |
| pc1 | 0.100 | 0.350 | 0.758 | 0.942 | 0.992 |
| pc2 | 0.258 | 0.575 | 0.917 | 0.983 | 1.000 |
| t05 | 0.000 | 0.008 | 0.025 | 0.050 | 0.150 |
| t10 | 0.008 | 0.067 | 0.167 | 0.367 | 0.700 |

Criterion: P2 rejection within 1500 episodes >= 0.8 for pc0, pc1, pc2. **H3: supported**


## H4 Efficiency of class-level design P4 (primary comparator: random P2)


### H4a anticipated deviations: RMST(P2) / RMST(P4) (restricted at N=1500; >1 means P4 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| pc0 | 1.83 | [1.61, 2.17] |
| pc1 | 1.79 | [1.59, 1.98] |
| pc2 | 1.41 | [1.12, 1.71] |

**H4a (lower CI bound >= 1.5 for all of pc0, pc1, pc2): inconclusive**


### H4b unanticipated deviations: RMST(P2) / RMST(P4) (restricted at N=1500; >1 means P4 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| t05 | 1.11 | [1.00, 1.26] |
| t10 | 1.05 | [0.98, 1.15] |

**H4b (same criterion for t05, t10): contradicted**


## H4c Fair comparator: P5 (within-class EIG over M u W) vs P4 (same information, different target)


### H4c: RMST(P5) / RMST(P4) (restricted at N=1500; >1 means P4 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| pc0 | 0.84 | [0.72, 0.95] |
| pc1 | 0.78 | [0.64, 0.94] |
| pc2 | 0.64 | [0.48, 0.81] |
| t05 | 1.15 | [1.02, 1.34] |
| t10 | 1.36 | [1.08, 1.68] |

**H4c (anticipated truths, lower CI bound >= 1.5): contradicted**


## H5 Within-class EIG over M only (P3) is not faster than random (P2)


### H5: RMST(P2) / RMST(P3) (restricted at N=1500; >1 means P3 is faster); bootstrap over seeds

| truth | ratio | 95% CI |
|---|---|---|
| pc0 | 1.14 | [0.70, 1.75] |
| pc1 | 0.23 | [0.16, 0.33] |
| pc2 | 0.20 | [0.14, 0.29] |
| t05 | 0.94 | [0.92, 0.96] |
| t10 | 0.64 | [0.55, 0.77] |

**H5 (upper CI bound < 1.5 for pc0, pc1, pc2 => supported; any lower bound >= 1.5 => contradicted): inconclusive**


Rate of rejection within the budget, all non-null truths:

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| pc0 | 1.000 | 0.992 | 1.000 | 0.925 | 1.000 | 1.000 |
| pc1 | 1.000 | 1.000 | 0.992 | 0.233 | 0.992 | 1.000 |
| pc2 | 0.000 | 0.225 | 1.000 | 0.675 | 0.992 | 1.000 |
| t05 | 0.017 | 0.033 | 0.150 | 0.008 | 0.308 | 0.058 |
| t10 | 0.000 | 0.042 | 0.700 | 0.058 | 0.692 | 0.300 |
| shift | 0.008 | 0.025 | 0.000 | 0.008 | 0.025 | 0.017 |

Median episodes-to-reject (N+1 = censored):

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| pc0 | 270 | 303 | 342 | 272 | 160 | 146 |
| pc1 | 206 | 218 | 245 | 1501 | 130 | 128 |
| pc2 | 1501 | 1501 | 171 | 1148 | 102 | 76 |
| t05 | 1501 | 1501 | 1501 | 1501 | 1501 | 1501 |
| t10 | 1501 | 1501 | 1016 | 1501 | 964 | 1501 |

## Computational cost (run-seconds per policy, summed)

P0: 109, P1: 123, P2: 94, P3: 286, P4: 242, P5: 242


## Summary of decisions

```json
{
 "H1": "inconclusive",
 "H2": "supported",
 "H3": "supported",
 "H4a": "inconclusive",
 "H4b": "contradicted",
 "H4c": "contradicted",
 "H5": "inconclusive"
}
```
