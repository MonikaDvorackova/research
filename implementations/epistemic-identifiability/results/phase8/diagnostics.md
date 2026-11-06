## D2 Stationarity e-process (changepoint mixture / stationary-MLE), alpha = 0.05, N = 3000 episodes x 4 steps, R = 100 streams per scenario

| scenario | rejection within N | median rejection episode among rejected | rejections before episode 1500 |
|---|---|---|---|
| S0 Markov, stationary, wide (epistemic only) | 0/100 | – | 0 |
| S1 Markov, stationary, policy shift narrow->wide (C) | 0/100 | – | 0 |
| S2 Markov, kernel change at ep 1500, wide (D) | 100/100 | 1775.0 | 0 |
| S3 Markov, kernel change at ep 1500, narrow (D, low coverage) | 0/100 | – | 0 |
| S4 hidden-state POMDP, stationary, wide (B: order-1 class misspecified) | 0/100 | – | 0 |
| S5 hidden-state POMDP, stationary, policy shift (B+C) | 0/100 | – | 0 |
| S6 hidden-state POMDP, kernel change at ep 1500, wide (B+D) | 0/100 | – | 0 |

## D4a Frozen learned null (count model trained once on a narrow policy, p(action 2) = 0.02) tested on a WIDE-policy stream from the SAME Markov kernel (no change of mechanism)

| training episodes | false-alarm rate within N = 3000 | median rejection episode |
|---|---|---|
| 100 | 100/100 | 115.0 |
| 1000 | 98/100 | 807.5 |
| 10000 | 3/100 | 2.0 |
| 100000 | 2/100 | 1.0 |

For comparison the stationarity e-process on the same wide stream (S0 above) has the rejection rate shown there.

## D3 Learning curves of Dirichlet(1/2) count learners (uniform actions, T = 4); excess held-out log-loss in nats per episode, mean over R = 40 training sets (+- s.e.)

**Markov truth**: entropy of the truth H = 3.3314; exact misspecification plateau of the best order-1 kernel d1 = -4.44e-16, of the best order-2 kernel d2 = -4.44e-16

| n | order-1 excess loss | order-2 excess loss | comparator gap L1 − L2 |
|---|---|---|---|
| 10 | 6.67e-01 ± 2.5e-02 | 9.61e-01 ± 1.9e-02 | -2.95e-01 |
| 30 | 3.49e-01 ± 2.1e-02 | 7.11e-01 ± 1.7e-02 | -3.63e-01 |
| 100 | 1.14e-01 ± 6.4e-03 | 3.07e-01 ± 8.4e-03 | -1.93e-01 |
| 300 | 3.74e-02 ± 1.7e-03 | 1.13e-01 ± 2.9e-03 | -7.57e-02 |
| 1000 | 1.17e-02 ± 5.5e-04 | 3.67e-02 ± 9.2e-04 | -2.50e-02 |
| 3000 | 4.04e-03 ± 2.0e-04 | 1.31e-02 ± 3.9e-04 | -9.02e-03 |
| 10000 | 1.24e-03 ± 4.9e-05 | 3.94e-03 ± 1.1e-04 | -2.71e-03 |

**hidden-state truth E0**: entropy of the truth H = 4.0039; exact misspecification plateau of the best order-1 kernel d1 = 5.54e-02, of the best order-2 kernel d2 = 4.95e-02

| n | order-1 excess loss | order-2 excess loss | comparator gap L1 − L2 |
|---|---|---|---|
| 10 | 7.10e-01 ± 2.8e-02 | 5.69e-01 ± 2.0e-02 | +1.40e-01 |
| 30 | 4.06e-01 ± 1.8e-02 | 5.83e-01 ± 1.1e-02 | -1.76e-01 |
| 100 | 1.80e-01 ± 6.4e-03 | 3.91e-01 ± 9.0e-03 | -2.11e-01 |
| 300 | 9.69e-02 ± 1.7e-03 | 1.78e-01 ± 3.7e-03 | -8.13e-02 |
| 1000 | 6.79e-02 ± 4.9e-04 | 8.98e-02 ± 1.1e-03 | -2.19e-02 |
| 3000 | 5.96e-02 ± 2.0e-04 | 6.24e-02 ± 3.4e-04 | -2.80e-03 |
| 10000 | 5.65e-02 ± 4.8e-05 | 5.32e-02 ± 7.8e-05 | +3.32e-03 |

## D4b Approximate maximiser: truth = member n10 of the true class; denominator maximises over a coarse subset (n10 omitted) while the numerator mixture contains the full class

| denominator | rejection within 3000 episodes (R = 40, random wide policy) |
|---|---|
| exact maximiser over the true class (valid) | 0/40 |
| coarse maximiser, true member missed | 39/40 |
