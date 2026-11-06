## K1. Regret scaling of a broad (saturated iid) null: evidence needed to detect a change of fixed size (KL = 0.1 nats/observation), pre-change law unknown

| cells K | detected within 12000 post-change obs | median delay (obs) | median delay x KL (nats of evidence) | (K-1)/2 | ratio evidence/((K-1)/2) |
|---|---|---|---|---|---|
| 2 | 12/12 | 170 | 17.0 | 0.5 | 34.00 |
| 4 | 12/12 | 300 | 30.0 | 1.5 | 20.00 |
| 8 | 12/12 | 480 | 48.0 | 3.5 | 13.71 |
| 16 | 12/12 | 1220 | 122.0 | 7.5 | 16.27 |
| 32 | 12/12 | 2950 | 295.0 | 15.5 | 19.03 |
| 64 | 1/12 | 12000 | 1200.0 | 31.5 | 38.10 |
| 128 | 0/12 | 12000 | 1200.0 | 63.5 | 18.90 |

Measured slope of evidence needed versus K (detected cases K = 8, 16, 32): 10.4 nats per cell (naive Krichevsky-Trofimov redundancy would be (1/2) ln n per cell, about 4-5 nats).
Extrapolation (beyond the measured range, indicative only) to the episode-level saturated model of Phases 7/9 (2160 free cells; change of 0.01 nats/episode): evidence ~ 22391 nats, i.e. about 2.2e+06 episodes, versus N = 3000 in the dev run.
