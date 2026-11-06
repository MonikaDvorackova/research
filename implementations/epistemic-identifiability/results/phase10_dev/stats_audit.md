## S1. Intra-structure dependence measured on the development runs (60 independent Markov structures)

| outcome | runs per structure | mean | ICC (ANOVA) | design effect 1+(R-1)ICC |
|---|---|---|---|---|
| frozen-null rejection (simple null; semantic false alarm), narrow/1000 | 30 | 0.7417 | 0.007 | 1.2 |
| certified rejection (type-I), narrow/1000 | 30 | 0.0000 | undefined (no variation) | – |
| frozen-null rejection (simple null; semantic false alarm), narrow/10000 | 30 | 0.0006 | 0.000 | 1.0 |
| certified rejection (type-I), narrow/10000 | 30 | 0.0000 | undefined (no variation) | – |
| frozen-null rejection (simple null; semantic false alarm), uniform/1000 | 30 | 0.0000 | undefined (no variation) | – |
| certified rejection (type-I), uniform/1000 | 30 | 0.0000 | undefined (no variation) | – |
| log(certified delay / oracle delay), uniform/10000 | 8 | 0.344 | 0.367 | 3.6 |
| log(certified delay / oracle delay), uniform/1000 | 8 | 1.108 | 0.654 | 5.6 |
| log(certified delay / oracle delay), narrow/10000 | 8 | 1.705 | 0.786 | 6.5 |

## S2. Coverage of one-sided 95 % upper bounds for a rate, m = 60 structures x R = 60 runs, 300 simulated datasets

| true mean rate | ICC | pooled CP | cluster t | cluster bootstrap | design-effect-adjusted CP |
|---|---|---|---|---|---|
| 0.05 | 0.0 | 0.973 | 0.970 | 0.967 | 0.973 |
| 0.05 | 0.05 | 0.773 | 0.927 | 0.923 | 0.947 |
| 0.05 | 0.2 | 0.673 | 0.880 | 0.870 | 0.927 |
| 0.05 | 0.5 | 0.637 | 0.870 | 0.887 | 0.933 |
| 0.02 | 0.0 | 0.963 | 0.937 | 0.940 | 0.967 |
| 0.02 | 0.05 | 0.833 | 0.913 | 0.923 | 0.933 |
| 0.02 | 0.2 | 0.683 | 0.833 | 0.843 | 0.913 |
| 0.02 | 0.5 | 0.550 | 0.770 | 0.783 | 0.843 |

## S3. Sample sizes from measured variability (exact exponents; development runs)

Retained fraction of the oracle exponent, rho_s = Lambda_cert / Lambda_oracle per structure (from the exact information projection onto the LR confidence set):

| training policy | training episodes | mean rho | between-structure SD of rho | structures for a 95 % interval half-width 0.05 on mean rho | structures for half-width 0.02 |
|---|---|---|---|---|---|
| narrow | 1000 | 0.010 | 0.014 | 1 | 2 |
| narrow | 10000 | 0.240 | 0.094 | 14 | 85 |
| uniform | 1000 | 0.395 | 0.103 | 17 | 103 |
| uniform | 10000 | 0.691 | 0.116 | 21 | 129 |

Log delay ratio (certified / oracle), variance components from the 8 runs per structure:

| condition | between-structure SD | within-structure SD | structures m for a 95 % interval of +-10 % on the geometric-mean ratio with R = 8 | with R = 30 |
|---|---|---|---|---|
| uniform/10000 | 0.241 | 0.316 | 30 | 26 |
| uniform/1000 | 0.533 | 0.387 | 128 | 123 |
| narrow/10000 | 0.749 | 0.390 | 246 | 240 |
