## X. Exact checks

### X1. Certified test, exhaustive enumeration (2 contexts, binary outcomes, adaptive context rule c_{t+1} = o_t, 4 training + 5 test observations, alpha = 0.4, delta = 0.3)

| true kernel (P(o=1|c=0), P(o=1|c=1)) | P(truth outside C at some training prefix) [<= delta] | P(reject) [<= alpha+delta] | P(reject and truth in C) [<= alpha] |
|---|---|---|---|
| (0.1, 0.1) | 0.1252 | 0.0000 | 0.0000 |
| (0.1, 0.5) | 0.1045 | 0.0000 | 0.0000 |
| (0.1, 0.9) | 0.1171 | 0.0000 | 0.0000 |
| (0.5, 0.1) | 0.1150 | 0.0000 | 0.0000 |
| (0.5, 0.5) | 0.0625 | 0.0000 | 0.0000 |
| (0.5, 0.9) | 0.1125 | 0.0000 | 0.0000 |
| (0.9, 0.1) | 0.1171 | 0.0000 | 0.0000 |
| (0.9, 0.5) | 0.1045 | 0.0000 | 0.0000 |
| (0.9, 0.9) | 0.1171 | 0.0000 | 0.0000 |

Maxima over the grid: 0.1252 (<= 0.3), 0.0000 (<= 0.7), 0.0000 (<= 0.4).

### X2. Bernoulli stream, null interval [0.3, 0.7]; denominator = marginal likelihood under the uniform prior on [0.3, 0.7] (no supremum): rejection probability by true p (N = 400, alpha = 0.05)

| true p | P(reject by N=400) |
|---|---|
| 0.3 | 0.1468 |
| 0.35 | 0.0369 |
| 0.4 | 0.0140 |
| 0.5 | 0.0043 |
| 0.6 | 0.0140 |
| 0.7 | 0.1468 |

Average over the prior (9-point quadrature): 0.0458 (<= alpha = 0.05 by Ville under the Bayes mixture); maximum pointwise value in the table: 0.1468.

### X3. Exact expected e-value E[E_N] of the certified test (N = 8 test observations), by dynamic programming; training counts enumerated (4 training observations, adaptive rule c_{t+1}=o_t); delta = 0.3

| true kernel | training count states with truth in C: max E[E_N] (<= 1 required) | training count states with truth NOT in C: max E[E_N] (no guarantee) |
|---|---|---|
| (0.5, 0.5) | 0.2044 (10 states) | 0.2761 (1 states) |
| (0.2, 0.8) | 0.1899 (8 states) | 0.6217 (3 states) |
| (0.1, 0.9) | 0.2122 (6 states) | 0.9335 (5 states) |
| (0.8, 0.3) | 0.2275 (8 states) | 0.8337 (3 states) |
