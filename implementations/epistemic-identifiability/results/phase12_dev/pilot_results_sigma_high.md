## P1. Exact identifiability map: per-episode KL (nats) between hypothesis pairs, for the best program in the menu and for a random large-control program (mean of 200)

| sigma | pair | best menu program KL | random large-control KL | episodes to reach 3 nats (best) | episodes (random) |
|---|---|---|---|---|---|
| 0.2 | cont vs quant(0.2) | 184 | 5.91 | 0.016 | 0.51 |
| 0.2 | cont vs stiff(0.1) | 148 | 2.87 | 0.02 | 1 |
| 0.2 | quant(0.2) vs stiff(0.1) [matched dead zone] | 6.44 | 3.64 | 0.47 | 0.82 |
| 0.8 | cont vs quant(0.2) | 11.5 | 0.369 | 0.26 | 8.1 |
| 0.8 | cont vs stiff(0.1) | 9.24 | 0.18 | 0.32 | 17 |
| 0.8 | quant(0.2) vs stiff(0.1) [matched dead zone] | 0.403 | 0.227 | 7.4 | 13 |
| 3.2 | cont vs quant(0.2) | 0.721 | 0.0231 | 4.2 | 1.3e+02 |
| 3.2 | cont vs stiff(0.1) | 0.578 | 0.0112 | 5.2 | 2.7e+02 |
| 3.2 | quant(0.2) vs stiff(0.1) [matched dead zone] | 0.0252 | 0.0142 | 1.2e+02 | 2.1e+02 |

## P2. Structural hypothesis agents, 12 episodes of 20 steps, 40 replicate noise/physics draws per cell (no independent structures beyond b ~ U[0.7, 1.3])

Entry: posterior mass on the true hypothesis (mean) / correct-class decision rate / exact-hypothesis decision rate.

| truth | sigma | passive (large random controls) | random-amplitude probe | active EIG planner |
|---|---|---|---|---|
| cont(0.0) | 0.2 | 0.85 / 0.95 / 0.95 | 0.76 / 0.80 / 0.85 | 1.00 / 1.00 / 1.00 |
| cont(0.0) | 0.8 | 0.35 / 0.33 / 0.45 | 0.23 / 0.10 / 0.35 | 1.00 / 1.00 / 1.00 |
| cont(0.0) | 3.2 | 0.15 / 0.00 / 0.17 | 0.15 / 0.00 / 0.30 | 0.39 / 0.45 / 0.45 |
| quant(0.1) | 0.2 | 0.98 / 1.00 / 1.00 | 0.67 / 0.82 / 0.82 | 1.00 / 1.00 / 1.00 |
| quant(0.1) | 0.8 | 0.43 / 0.60 / 0.57 | 0.27 / 0.65 / 0.45 | 0.72 / 0.82 / 0.82 |
| quant(0.1) | 3.2 | 0.20 / 0.62 / 0.40 | 0.15 / 0.60 / 0.25 | 0.35 / 0.47 / 0.42 |
| quant(0.2) | 0.2 | 1.00 / 1.00 / 1.00 | 0.61 / 0.72 / 0.75 | 1.00 / 1.00 / 1.00 |
| quant(0.2) | 0.8 | 0.70 / 0.85 / 0.82 | 0.23 / 0.42 / 0.40 | 0.92 / 0.97 / 0.97 |
| quant(0.2) | 3.2 | 0.20 / 0.53 / 0.47 | 0.15 / 0.62 / 0.33 | 0.44 / 0.47 / 0.57 |
| quant(0.4) | 0.2 | 0.74 / 1.00 / 1.00 | 0.43 / 0.20 / 0.68 | 0.71 / 1.00 / 1.00 |
| quant(0.4) | 0.8 | 0.67 / 0.45 / 1.00 | 0.25 / 0.33 / 0.40 | 0.68 / 0.97 / 0.97 |
| quant(0.4) | 3.2 | 0.28 / 0.47 / 0.65 | 0.16 / 0.42 / 0.35 | 0.56 / 0.42 / 0.82 |
| stiff(0.05) | 0.2 | 0.83 / 0.85 / 0.85 | 0.61 / 0.70 / 0.65 | 1.00 / 1.00 / 1.00 |
| stiff(0.05) | 0.8 | 0.30 / 0.60 / 0.42 | 0.20 / 0.45 / 0.17 | 0.76 / 0.85 / 0.85 |
| stiff(0.05) | 3.2 | 0.15 / 0.50 / 0.10 | 0.15 / 0.33 / 0.05 | 0.30 / 0.47 / 0.35 |
| stiff(0.1) | 0.2 | 1.00 / 1.00 / 1.00 | 0.57 / 0.88 / 0.53 | 1.00 / 1.00 / 1.00 |
| stiff(0.1) | 0.8 | 0.49 / 0.82 / 0.72 | 0.20 / 0.70 / 0.23 | 0.93 / 1.00 / 1.00 |
| stiff(0.1) | 3.2 | 0.16 / 0.45 / 0.17 | 0.14 / 0.42 / 0.00 | 0.43 / 0.75 / 0.60 |
| stiff(0.2) | 0.2 | 0.76 / 0.53 / 0.53 | 0.44 / 0.85 / 0.10 | 0.73 / 0.47 / 0.47 |
| stiff(0.2) | 0.8 | 0.67 / 0.90 / 0.45 | 0.27 / 0.70 / 0.07 | 0.74 / 0.62 / 0.62 |
| stiff(0.2) | 3.2 | 0.25 / 0.70 / 0.25 | 0.15 / 0.42 / 0.03 | 0.54 / 0.80 / 0.35 |

Predictive accuracy of the posterior-mean predictor on a fresh passive episode relative to the noise floor (RMSE / sigma), mean over truths and replicates:

| sigma | passive | probe | active |
|---|---|---|---|
| 0.2 | 0.993 | 1.058 | 0.994 |
| 0.8 | 0.984 | 0.996 | 0.991 |
| 3.2 | 0.995 | 0.971 | 0.986 |
