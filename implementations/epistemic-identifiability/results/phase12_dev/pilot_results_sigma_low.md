## P1. Exact identifiability map: per-episode KL (nats) between hypothesis pairs, for the best program in the menu and for a random large-control program (mean of 200)

| sigma | pair | best menu program KL | random large-control KL | episodes to reach 3 nats (best) | episodes (random) |
|---|---|---|---|---|---|
| 0.005 | cont vs quant(0.2) | 2.95e+05 | 9.46e+03 | 1e-05 | 0.00032 |
| 0.005 | cont vs stiff(0.1) | 2.37e+05 | 4.6e+03 | 1.3e-05 | 0.00065 |
| 0.005 | quant(0.2) vs stiff(0.1) [matched dead zone] | 1.03e+04 | 5.82e+03 | 0.00029 | 0.00052 |
| 0.05 | cont vs quant(0.2) | 2.95e+03 | 94.6 | 0.001 | 0.032 |
| 0.05 | cont vs stiff(0.1) | 2.37e+03 | 46 | 0.0013 | 0.065 |
| 0.05 | quant(0.2) vs stiff(0.1) [matched dead zone] | 103 | 58.2 | 0.029 | 0.052 |
| 0.2 | cont vs quant(0.2) | 184 | 5.91 | 0.016 | 0.51 |
| 0.2 | cont vs stiff(0.1) | 148 | 2.87 | 0.02 | 1 |
| 0.2 | quant(0.2) vs stiff(0.1) [matched dead zone] | 6.44 | 3.64 | 0.47 | 0.82 |

## P2. Structural hypothesis agents, 12 episodes of 20 steps, 40 replicate noise/physics draws per cell (no independent structures beyond b ~ U[0.7, 1.3])

Entry: posterior mass on the true hypothesis (mean) / correct-class decision rate / exact-hypothesis decision rate.

| truth | sigma | passive (large random controls) | random-amplitude probe | active EIG planner |
|---|---|---|---|---|
| cont(0.0) | 0.005 | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 |
| cont(0.0) | 0.05 | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 |
| cont(0.0) | 0.2 | 0.81 / 0.82 / 0.82 | 0.81 / 0.85 / 0.85 | 1.00 / 1.00 / 1.00 |
| quant(0.1) | 0.005 | 1.00 / 1.00 / 1.00 | 0.98 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 |
| quant(0.1) | 0.05 | 1.00 / 1.00 / 1.00 | 0.97 / 1.00 / 1.00 | 1.00 / 1.00 / 1.00 |
| quant(0.1) | 0.2 | 0.96 / 0.97 / 0.97 | 0.68 / 0.82 / 0.80 | 1.00 / 1.00 / 1.00 |
| quant(0.2) | 0.005 | 1.00 / 1.00 / 1.00 | 0.87 / 1.00 / 0.97 | 1.00 / 1.00 / 1.00 |
| quant(0.2) | 0.05 | 1.00 / 1.00 / 1.00 | 0.67 / 0.78 / 0.93 | 1.00 / 1.00 / 1.00 |
| quant(0.2) | 0.2 | 1.00 / 1.00 / 1.00 | 0.65 / 0.65 / 0.88 | 1.00 / 1.00 / 1.00 |
| quant(0.4) | 0.005 | 0.74 / 1.00 / 1.00 | 0.48 / 1.00 / 0.75 | 0.71 / 1.00 / 1.00 |
| quant(0.4) | 0.05 | 0.70 / 1.00 / 1.00 | 0.47 / 0.78 / 0.70 | 0.72 / 1.00 / 1.00 |
| quant(0.4) | 0.2 | 0.74 / 1.00 / 1.00 | 0.43 / 0.10 / 0.65 | 0.77 / 0.97 / 0.97 |
| stiff(0.05) | 0.005 | 1.00 / 1.00 / 1.00 | 0.98 / 0.97 / 0.97 | 1.00 / 1.00 / 1.00 |
| stiff(0.05) | 0.05 | 1.00 / 1.00 / 1.00 | 0.95 / 0.95 / 0.95 | 1.00 / 1.00 / 1.00 |
| stiff(0.05) | 0.2 | 0.85 / 0.88 / 0.88 | 0.54 / 0.78 / 0.70 | 1.00 / 1.00 / 1.00 |
| stiff(0.1) | 0.005 | 1.00 / 1.00 / 1.00 | 0.77 / 0.70 / 0.70 | 1.00 / 1.00 / 1.00 |
| stiff(0.1) | 0.05 | 1.00 / 1.00 / 1.00 | 0.75 / 0.90 / 0.68 | 1.00 / 1.00 / 1.00 |
| stiff(0.1) | 0.2 | 1.00 / 1.00 / 1.00 | 0.52 / 0.75 / 0.53 | 1.00 / 1.00 / 1.00 |
| stiff(0.2) | 0.005 | 0.76 / 0.53 / 0.53 | 0.49 / 0.10 / 0.10 | 0.74 / 0.47 / 0.47 |
| stiff(0.2) | 0.05 | 0.76 / 0.53 / 0.53 | 0.51 / 0.28 / 0.15 | 0.81 / 0.62 / 0.62 |
| stiff(0.2) | 0.2 | 0.76 / 0.53 / 0.53 | 0.42 / 0.75 / 0.10 | 0.74 / 0.50 / 0.50 |

Predictive accuracy of the posterior-mean predictor on a fresh passive episode relative to the noise floor (RMSE / sigma), mean over truths and replicates:

| sigma | passive | probe | active |
|---|---|---|---|
| 0.005 | 0.992 | 5.133 | 0.994 |
| 0.05 | 0.983 | 1.423 | 0.991 |
| 0.2 | 0.995 | 1.028 | 0.986 |

## P3. Prediction-oriented learned world model (MLP one-step predictor, 64-64 tanh), sigma = 0.05; 5 seeds per generator; RMSE in observation units

| generator | training data | passive-test RMSE | probe RMSE (x = 0, u in {0.02, 0.05, 0.1}) | probe RMSE of the TRUE noise-free map = 0 | passive RMSE noise floor |
|---|---|---|---|---|---|
| cont(0.0) | passive | 0.0693 ± 0.0007 | 0.0056 ± 0.0028 | 0 | 0.05 |
| cont(0.0) | probe+active-style | 0.0972 ± 0.0054 | 0.0041 ± 0.0018 | 0 | 0.05 |
| quant(0.2) | passive | 0.0891 ± 0.0015 | 0.0156 ± 0.0023 | 0 | 0.05 |
| quant(0.2) | probe+active-style | 0.1379 ± 0.0050 | 0.0136 ± 0.0037 | 0 | 0.05 |
| stiff(0.1) | passive | 0.0769 ± 0.0013 | 0.0171 ± 0.0028 | 0 | 0.05 |
| stiff(0.1) | probe+active-style | 0.1423 ± 0.0093 | 0.0055 ± 0.0020 | 0 | 0.05 |
