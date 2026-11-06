## E. Approximate maximiser: multi-start EM (10 random starts) against the likelihood at the TRUE parameters (hidden-state instances with S <= 4, uniform actions, T = 4)

| instance | hidden states | training episodes | EM iterations | starts below the true-parameter log-likelihood by > 0.5 nats | worst shortfall (nats) | best start − true (nats) | seconds for 10 starts |
|---|---|---|---|---|---|---|---|
| 1 | 4 | 500 | 60 | 1/10 | -4.6 | +19.99 | 0 |
| 1 | 4 | 500 | 300 | 0/10 | 8.3 | +28.57 | 2 |
| 1 | 4 | 5000 | 60 | 10/10 | -132.9 | -4.69 | 3 |
| 1 | 4 | 5000 | 300 | 2/10 | -116.2 | +20.23 | 12 |
| 8 | 3 | 500 | 60 | 9/10 | -8.4 | +3.65 | 0 |
| 8 | 3 | 500 | 300 | 1/10 | -2.4 | +11.34 | 1 |
| 8 | 3 | 5000 | 60 | 10/10 | -132.4 | -52.69 | 2 |
| 8 | 3 | 5000 | 300 | 5/10 | -24.4 | +5.88 | 10 |
| 11 | 4 | 500 | 60 | 0/10 | 3.9 | +16.07 | 0 |
| 11 | 4 | 500 | 300 | 0/10 | 18.2 | +28.56 | 2 |
| 11 | 4 | 5000 | 60 | 10/10 | -80.9 | -13.26 | 3 |
| 11 | 4 | 5000 | 300 | 0/10 | -0.4 | +13.88 | 12 |
| 13 | 4 | 500 | 60 | 0/10 | 0.6 | +22.12 | 0 |
| 13 | 4 | 500 | 300 | 0/10 | 22.3 | +29.30 | 2 |
| 13 | 4 | 5000 | 60 | 10/10 | -64.8 | -8.89 | 3 |
| 13 | 4 | 5000 | 300 | 4/10 | -15.7 | +13.01 | 11 |

EM budget 60 iterations: 50/80 starts ended below the true-parameter likelihood by > 0.5 nats; a denominator built from any such start is NOT an upper bound on the true null likelihood.

EM budget 300 iterations: 12/80 starts ended below the true-parameter likelihood by > 0.5 nats; a denominator built from any such start is NOT an upper bound on the true null likelihood.

## F. Confidence-set denominator (T6d): rejection rate within 1500 test episodes (wide policy); Markov instances (10), 2 reps; level alpha = 0.05, alpha1 = 0.05

| training policy | training episodes | unchanged kernel (type-I; guarantee <= 0.10) | kernel change in action-2 rows at episode 500 | median seconds per run |
|---|---|---|---|---|
| narrow | 100 | 0/20 | 0/20 | 0.3 |
| narrow | 1000 | 0/20 | 3/20 | 0.3 |
| narrow | 10000 | 0/20 | 20/20 | 0.2 |
| uniform | 100 | 0/20 | 11/20 | 0.3 |
| uniform | 1000 | 0/20 | 19/20 | 0.2 |
| uniform | 10000 | 0/20 | 20/20 | 0.2 |
