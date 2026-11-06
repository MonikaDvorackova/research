## E1. Optimiser gap: best-of-R EM against the likelihood at the TRUE parameters (40 independent small HMMs, S in {2,3}, 800 training episodes)

| restarts R | iteration budget | tolerance | fraction with ll below the true-parameter ll by > 0.5 nats (invalid denominator) | median shortfall vs true (nats) | 90th pct shortfall | median shortfall vs 20x1000 reference | median seconds |
|---|---|---|---|---|---|---|---|
| 1 | 20 | 1e-06 | 0.82 (33/40) | 13.9 | 38.5 | 22.1 | 0.01 |
| 1 | 60 | 1e-06 | 0.35 (14/40) | -1.4 | 12.4 | 9.5 | 0.05 |
| 1 | 300 | 1e-06 | 0.07 (3/40) | -6.1 | -1.8 | 0.8 | 0.22 |
| 1 | 1000 | 1e-06 | 0.03 (1/40) | -7.6 | -2.4 | 0.2 | 0.39 |
| 5 | 20 | 1e-06 | 0.62 (25/40) | 2.3 | 14.8 | 11.4 | 0.08 |
| 5 | 60 | 1e-06 | 0.07 (3/40) | -4.1 | -1.3 | 2.9 | 0.23 |
| 5 | 300 | 1e-06 | 0.00 (0/40) | -7.4 | -2.4 | 0.2 | 1.05 |
| 5 | 300 | 0.001 | 0.62 (25/40) | 1.8 | 8.8 | 10.4 | 0.05 |
| 5 | 1000 | 1e-06 | 0.00 (0/40) | -8.0 | -2.5 | 0.0 | 1.96 |
| 5 | 1000 | 0.001 | 0.55 (22/40) | 0.9 | 7.5 | 9.1 | 0.06 |
| 20 | 20 | 1e-06 | 0.30 (12/40) | -1.4 | 4.3 | 8.1 | 0.31 |
| 20 | 60 | 1e-06 | 0.03 (1/40) | -5.2 | -1.8 | 1.5 | 0.89 |
| 20 | 300 | 1e-06 | 0.00 (0/40) | -7.6 | -2.6 | 0.0 | 4.18 |
| 20 | 1000 | 1e-06 | 0.00 (0/40) | -8.1 | -2.5 | 0.0 | 7.99 |

## E2. Type-I of an e-process with an EM denominator, truth in the class, S known (40 structures x 3 data sets; blocks 100,100,200,400 episodes; checkpoints after every block; threshold 1/alpha = 20)

| denominator | rejections / runs | structures with >= 1 | median optimisation shortfall at the last checkpoint (nats) | median numerator deficit  log q - log p_true (nats) | max (shortfall + numerator gap) |
|---|---|---|---|---|---|
| true | 0/120 (UB 0.025) | 0/40 | 0.0 | -115.1 | -20.6 |
| sym(R5,B300) | 0/120 (UB 0.025) | 0/40 | -7.2 | -115.1 | -28.1 |
| best(R10,B600) | 0/120 (UB 0.025) | 0/40 | -7.7 | -115.1 | -28.1 |
| asym(R1,B60) | 0/120 (UB 0.025) | 0/40 | -1.4 | -115.1 | -19.5 |
| asym(R1,B20) | 5/120 (UB 0.086) | 4/40 | 10.1 | -115.1 | 70.9 |

log E = (log q - log p_true) + (log p_true - log p_den) = (numerator deficit, <= 0 on average: the price of learning) + (optimisation shortfall of the denominator). Rejection requires the shortfall to exceed the numerator deficit by ln 20 = 3.0 nats.

## E3. Same denominators with a GOOD fixed alternative (true parameters mixed 10 % with random rows; deficit ll_alt - ll_true small): type-I under the correctly specified null

| denominator | rejections / runs | structures with >= 1 | median optimisation shortfall (nats) | median alternative deficit (nats) | share of runs with shortfall > deficit + ln 20 |
|---|---|---|---|---|---|
| true | 0/120 (LB 0.000) | 0/40 | 0.0 | -16.9 | 0.00 |
| sym(R5,B300) | 0/120 (LB 0.000) | 0/40 | -7.2 | -16.9 | 0.00 |
| best(R10,B600) | 0/120 (LB 0.000) | 0/40 | -7.7 | -16.9 | 0.00 |
| asym(R1,B60) | 18/120 (LB 0.099) | 10/40 | -1.4 | -16.9 | 0.09 |
| asym(R1,B20) | 53/120 (LB 0.365) | 27/40 | 10.1 | -16.9 | 0.31 |
