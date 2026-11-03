## C. Predictive-comparison procedures: worst-case Hoeffding boundary (rho = 2000, sigma = 2) vs predictable-range boundary; 10 instances x 3 runs per scenario, N = 3000 episodes

| scenario | physical mechanism changed | Hoeffding / forgetting | adaptive / forgetting | Hoeffding / order-2 | adaptive / order-2 | mean conditional range R | sd of Brier difference | formal null (forgetting) approx. |
|---|---|---|---|---|---|---|---|---|
| M1 Markov, stationary | no | 0/30 | 0/30 | 0/30 | 0/30 | 0.083 | 0.042 | true |
| M2 Markov, pure policy shift (C) | no | 0/30 | 0/30 | 0/30 | 0/30 | 0.086 | 0.044 | true |
| M3 Markov, mechanism change, changed action played (D) | yes | 0/30 | 30/30 | 0/30 | 0/30 | 0.203 | 0.156 | false |
| M4 Markov, mechanism change, changed action never played | yes | 0/30 | 0/30 | 0/30 | 0/30 | 0.091 | 0.046 | true |
| H1 hidden-state, stationary, resets | no | 0/30 | 0/30 | 0/30 | 0/30 | 0.091 | 0.047 | true |
| H2 hidden-state, extreme policy shift (B+C) | no | 0/30 | 0/30 | 0/30 | 0/30 | 0.094 | 0.049 | false |
| H3 hidden-state, mechanism change, played (B+D) | yes | 0/30 | 12/30 | 0/30 | 0/30 | 0.117 | 0.067 | false |
| H4 hidden-state, change in an action never played | yes | 0/30 | 0/30 | 0/30 | 0/30 | 0.099 | 0.050 | true |
| H5 hidden-state, switch to bisimilar split-state twin | no | 0/30 | 0/30 | 0/30 | 0/30 | 0.092 | 0.047 | true |
| R1 persistent latent regime, stationary | no | 0/30 | 16/30 | 0/30 | 0/30 | 0.144 | 0.077 | false |
