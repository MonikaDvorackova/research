| scenario | physical mechanism changed | procedure | formal null true | rejections / runs | instances with ≥1 rejection | cell category | observed |
|---|---|---|---|---|---|---|---|
| M1 Markov, stationary | no | E_ctx | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M1 Markov, stationary | no | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M1 Markov, stationary | no | E_comp_forget | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M1 Markov, stationary | no | E_comp_ord2 | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M2 Markov, pure policy shift (C) | no | E_ctx | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M2 Markov, pure policy shift (C) | no | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M2 Markov, pure policy shift (C) | no | E_comp_forget | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M2 Markov, pure policy shift (C) | no | E_comp_ord2 | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| M3 Markov, mechanism change, changed action played (D) | yes | E_ctx | no | 30/30 (UB95 1.000) | 10/10 | null false and mechanism changed (power cell) | rejected in some runs |
| M3 Markov, mechanism change, changed action played (D) | yes | E_ep | no | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| M3 Markov, mechanism change, changed action played (D) | yes | E_comp_forget | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| M3 Markov, mechanism change, changed action played (D) | yes | E_comp_ord2 | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| M4 Markov, mechanism change, changed action never played | yes | E_ctx | yes | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| M4 Markov, mechanism change, changed action never played | yes | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| M4 Markov, mechanism change, changed action never played | yes | E_comp_forget | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| M4 Markov, mechanism change, changed action never played | yes | E_comp_ord2 | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| H1 hidden-state, stationary, resets | no | E_ctx | no | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| H1 hidden-state, stationary, resets | no | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| H1 hidden-state, stationary, resets | no | E_comp_forget | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| H1 hidden-state, stationary, resets | no | E_comp_ord2 | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| H2 hidden-state, extreme policy shift (B+C) | no | E_ctx | no | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| H2 hidden-state, extreme policy shift (B+C) | no | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| H2 hidden-state, extreme policy shift (B+C) | no | E_comp_forget | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| H2 hidden-state, extreme policy shift (B+C) | no | E_comp_ord2 | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| H3 hidden-state, mechanism change, played (B+D) | yes | E_ctx | no | 5/30 (UB95 0.319) | 2/10 | null false and mechanism changed (power cell) | rejected in some runs |
| H3 hidden-state, mechanism change, played (B+D) | yes | E_ep | no | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| H3 hidden-state, mechanism change, played (B+D) | yes | E_comp_forget | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| H3 hidden-state, mechanism change, played (B+D) | yes | E_comp_ord2 | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| H4 hidden-state, change in an action never played | yes | E_ctx | no | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| H4 hidden-state, change in an action never played | yes | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| H4 hidden-state, change in an action never played | yes | E_comp_forget | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | mechanism changed but formal null still true (no rejection expected) | no rejection |
| H4 hidden-state, change in an action never played | yes | E_comp_ord2 | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false and mechanism changed (power cell) | no rejection |
| H5 hidden-state, switch to bisimilar split-state twin | no | E_ctx | no | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| H5 hidden-state, switch to bisimilar split-state twin | no | E_ep | yes | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| H5 hidden-state, switch to bisimilar split-state twin | no | E_comp_forget | yes (approx.) | 0/30 (UB95 0.095) | 0/10 | null true, mechanism unchanged (type-I cell) | no rejection |
| H5 hidden-state, switch to bisimilar split-state twin | no | E_comp_ord2 | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| R1 persistent latent regime, stationary | no | E_ctx | no | 8/30 (UB95 0.430) | 3/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | rejected in some runs |
| R1 persistent latent regime, stationary | no | E_ep | no | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| R1 persistent latent regime, stationary | no | E_comp_forget | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |
| R1 persistent latent regime, stationary | no | E_comp_ord2 | no (approx.) | 0/30 (UB95 0.095) | 0/10 | null false, mechanism unchanged (misspecification; rejection risks false attribution) | no rejection |

Cost (summed seconds over 300 runs): t_ctx: 15, t_ep: 976, t_comp: 20
