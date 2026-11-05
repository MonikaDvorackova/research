# OOL frozen holdout (namespace 31000)

Manifest sha256: `f8a09dea01ca1d3807237bd4b041d8ab354c5a78378758a62cbaf40ccbced1d2`; instances: 70; families: bump, bumpfar, gdelay, quadlag, rate, saw, sqrtabs. Cal thresholds: c_in={'5': 2.9211034554667945, '8': 2.959068486815061, '12': 3.469841235022011}, c_oos={'5': 10.465359921980648, '8': 4.515395951854984, '12': 2.5431422533663137}.

## 1. Per-family recovery (L1 predictive = RMSE<=0.05; L2 structural = signature match), B=8 and 12

### B=8

| method | bump L1/L2 | bumpfar L1/L2 | gdelay L1/L2 | quadlag L1/L2 | rate L1/L2 | saw L1/L2 | sqrtabs L1/L2 |
|---|---|---|---|---|---|---|---|
| adapt_sweepB | 1.0/0.0 | 1.0/0.8 | 0.7/0.3 | 1.0/1.0 | 1.0/0.9 | 0.0/0.0 | 1.0/0.0 |
| adapt_falsify | 1.0/0.2 | 1.0/0.8 | 0.5/0.2 | 1.0/1.0 | 1.0/1.0 | 0.0/0.0 | 1.0/0.1 |
| L0_sweepB | 1.0/0.0 | 1.0/0.8 | 0.4/0.0 | 0.6/0.0 | 1.0/0.0 | 0.0/0.0 | 1.0/0.0 |
| all_sweepB | 1.0/1.0 | 1.0/0.8 | 0.7/0.3 | 1.0/1.0 | 1.0/0.9 | 0.0/0.0 | 0.8/0.7 |
| oracle_struct | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 0.0/0.0 | 1.0/1.0 |
| pysr_fixed_kalman | 0.5/0.0 | 1.0/0.0 | 0.1/0.0 | 0.1/ | 0.8/0.0 | 0.0/ | 0.0/0.0 |
| pysr_expanded_kalman | 0.2/0.0 | 0.9/0.0 | 0.1/0.0 | 0.0/ | 0.7/0.0 | 0.0/ | 0.0/0.0 |
| pysr_expanded_learned | 0.3/0.0 | 0.8/0.0 | 0.1/0.5 | 0.1/ | 0.7/0.1 | 0.0/ | 0.0/0.0 |
| pysr_expanded_oracle | 0.1/0.1 | 1.0/0.0 | 0.5/0.7 | 0.1/ | 1.0/1.0 | 0.0/ | 0.2/0.0 |
| pysr_expanded_raw | 0.0/0.0 | 0.3/1.0 | 0.0/0.2 | 0.0/ | 0.1/0.0 | 0.0/ | 0.0/0.1 |
| sindyc_kalman | 0.0/ | 1.0/ | 0.0/ | 0.1/ | 0.0/ | 0.0/ | 0.0/ |
| sindyc_oracle | 0.0/ | 0.9/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| weak_kalman | 0.0/ | 1.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| implicit_kalman | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| narx | 0.0/ | 0.1/ | 0.0/ | 0.0/ | 0.1/ | 0.0/ | 0.0/ |
| hammerstein | 0.7/ | 0.9/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.6/ |

### B=12

| method | bump L1/L2 | bumpfar L1/L2 | gdelay L1/L2 | quadlag L1/L2 | rate L1/L2 | saw L1/L2 | sqrtabs L1/L2 |
|---|---|---|---|---|---|---|---|
| adapt_sweepB | 1.0/0.0 | 1.0/0.8 | 1.0/0.1 | 1.0/1.0 | 1.0/0.8 | 0.0/0.0 | 1.0/0.0 |
| adapt_falsify | 1.0/0.2 | 1.0/0.9 | 0.9/0.5 | 1.0/0.9 | 1.0/0.7 | 0.0/0.0 | 1.0/0.2 |
| L0_sweepB | 1.0/0.0 | 1.0/0.8 | 0.9/0.0 | 0.6/0.0 | 1.0/0.0 | 0.0/0.0 | 1.0/0.0 |
| all_sweepB | 1.0/0.9 | 1.0/0.8 | 1.0/0.1 | 1.0/1.0 | 1.0/0.8 | 0.0/0.0 | 1.0/0.7 |
| oracle_struct | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 0.0/0.0 | 1.0/1.0 |
| pysr_fixed_kalman | 0.2/0.0 | 0.9/0.0 | 0.1/0.0 | 0.2/ | 0.9/0.2 | 0.0/ | 0.0/0.0 |
| pysr_expanded_kalman | 0.3/0.0 | 0.8/0.0 | 0.1/0.0 | 0.1/ | 0.7/0.2 | 0.0/ | 0.0/0.0 |
| pysr_expanded_learned | 0.4/0.1 | 0.8/0.0 | 0.2/0.5 | 0.0/ | 0.7/0.1 | 0.0/ | 0.1/0.0 |
| pysr_expanded_oracle | 1.0/0.0 | 1.0/0.0 | 1.0/0.6 | 0.1/ | 1.0/1.0 | 0.0/ | 0.9/0.0 |
| pysr_expanded_raw | 0.0/0.0 | 0.3/1.0 | 0.0/0.3 | 0.0/ | 0.0/0.0 | 0.0/ | 0.0/0.2 |
| sindyc_kalman | 0.0/ | 1.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| sindyc_oracle | 0.0/ | 0.9/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| weak_kalman | 0.0/ | 1.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| implicit_kalman | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| narx | 0.0/ | 0.1/ | 0.0/ | 0.2/ | 0.3/ | 0.0/ | 0.0/ |
| hammerstein | 1.0/ | 1.0/ | 0.2/ | 0.0/ | 0.0/ | 0.0/ | 0.8/ |

## 2. Pooled over identifiable out-of-L0 mechanisms (95% stratified bootstrap over instances)

| method | B=5 L1 | B=5 L2 | B=8 L1 | B=8 L2 | B=12 L1 | B=12 L2 |
|---|---|---|---|---|---|---|
| adapt_sweepB | 0.86 [0.78,0.92] | 0.22 [0.14,0.30] | 0.94 [0.88,1.00] | 0.44 [0.38,0.50] | 1.00 [1.00,1.00] | 0.38 [0.32,0.44] |
| adapt_falsify | 0.78 [0.70,0.86] | 0.32 [0.24,0.40] | 0.90 [0.84,0.96] | 0.50 [0.42,0.58] | 0.98 [0.94,1.00] | 0.50 [0.38,0.62] |
| L0_sweepB | 0.78 [0.68,0.86] | 0.00 [0.00,0.00] | 0.80 [0.72,0.88] | 0.00 [0.00,0.00] | 0.90 [0.82,0.96] | 0.00 [0.00,0.00] |
| all_sweepB | 0.92 [0.86,0.98] | 0.70 [0.58,0.80] | 0.90 [0.82,0.96] | 0.78 [0.70,0.86] | 1.00 [1.00,1.00] | 0.70 [0.60,0.78] |
| oracle_struct | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] |
| pysr_fixed_kalman | n/a | n/a | 0.30 [0.22,0.40] | nan [nan,nan] | 0.28 [0.20,0.38] | nan [nan,nan] |
| pysr_expanded_kalman | n/a | n/a | 0.20 [0.12,0.28] | nan [nan,nan] | 0.24 [0.14,0.34] | nan [nan,nan] |
| pysr_expanded_learned | n/a | n/a | 0.24 [0.14,0.34] | nan [nan,nan] | 0.28 [0.18,0.38] | nan [nan,nan] |
| pysr_expanded_oracle | n/a | n/a | 0.38 [0.30,0.48] | nan [nan,nan] | 0.80 [0.74,0.86] | nan [nan,nan] |
| pysr_expanded_raw | n/a | n/a | 0.02 [0.00,0.06] | nan [nan,nan] | 0.00 [0.00,0.00] | nan [nan,nan] |
| sindyc_kalman | 0.00 [0.00,0.00] | n/a | 0.02 [0.00,0.06] | n/a | 0.00 [0.00,0.00] | n/a |
| sindyc_oracle | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a |
| weak_kalman | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a |
| implicit_kalman | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a |
| narx | 0.00 [0.00,0.00] | n/a | 0.02 [0.00,0.06] | n/a | 0.10 [0.04,0.18] | n/a |
| hammerstein | 0.26 [0.18,0.34] | n/a | 0.26 [0.18,0.34] | n/a | 0.40 [0.34,0.46] | n/a |

## 3. H1 - paired differences, adapt_sweepB minus competitor (identifiable out-of-L0 pooled)

| competitor | B | dL1 | dL2 (competitor L2 only where defined) | n |
|---|---|---|---|---|
| adapt_falsify | 8 | 0.04 [-0.06,0.12] | -0.06 [-0.16,0.04] | 50 |
| adapt_falsify | 12 | 0.02 [0.00,0.06] | -0.12 [-0.26,0.02] | 50 |
| L0_sweepB | 8 | 0.14 [0.04,0.24] | 0.44 [0.38,0.50] | 50 |
| L0_sweepB | 12 | 0.10 [0.04,0.18] | 0.38 [0.32,0.44] | 50 |
| all_sweepB | 8 | 0.04 [0.00,0.08] | -0.34 [-0.40,-0.28] | 50 |
| all_sweepB | 12 | 0.00 [0.00,0.00] | -0.32 [-0.38,-0.24] | 50 |
| oracle_struct | 8 | -0.06 [-0.12,0.00] | -0.56 [-0.62,-0.50] | 50 |
| oracle_struct | 12 | 0.00 [0.00,0.00] | -0.62 [-0.68,-0.56] | 50 |
| pysr_fixed_kalman | 8 | 0.64 [0.54,0.74] | 0.30 [0.23,0.38] | 50 |
| pysr_fixed_kalman | 12 | 0.72 [0.62,0.80] | 0.17 [0.05,0.28] | 50 |
| pysr_expanded_kalman | 8 | 0.74 [0.64,0.84] | 0.30 [0.23,0.38] | 50 |
| pysr_expanded_kalman | 12 | 0.76 [0.66,0.86] | 0.17 [0.05,0.28] | 50 |
| pysr_expanded_learned | 8 | 0.70 [0.60,0.80] | 0.15 [0.00,0.30] | 50 |
| pysr_expanded_learned | 12 | 0.72 [0.62,0.82] | 0.05 [-0.07,0.17] | 50 |
| pysr_expanded_oracle | 8 | 0.56 [0.46,0.66] | -0.15 [-0.25,-0.05] | 50 |
| pysr_expanded_oracle | 12 | 0.20 [0.14,0.26] | -0.17 [-0.28,-0.07] | 50 |
| pysr_expanded_raw | 8 | 0.92 [0.84,0.98] | 0.23 [0.10,0.35] | 50 |
| pysr_expanded_raw | 12 | 1.00 [1.00,1.00] | 0.10 [-0.00,0.20] | 50 |
| sindyc_kalman | 8 | 0.92 [0.84,0.98] | n/a | 50 |
| sindyc_kalman | 12 | 1.00 [1.00,1.00] | n/a | 50 |
| sindyc_oracle | 8 | 0.94 [0.88,1.00] | n/a | 50 |
| sindyc_oracle | 12 | 1.00 [1.00,1.00] | n/a | 50 |
| weak_kalman | 8 | 0.94 [0.88,1.00] | n/a | 50 |
| weak_kalman | 12 | 1.00 [1.00,1.00] | n/a | 50 |
| implicit_kalman | 8 | 0.94 [0.88,1.00] | n/a | 50 |
| implicit_kalman | 12 | 1.00 [1.00,1.00] | n/a | 50 |
| narx | 8 | 0.92 [0.84,0.98] | n/a | 50 |
| narx | 12 | 0.90 [0.82,0.96] | n/a | 50 |
| hammerstein | 8 | 0.68 [0.58,0.78] | n/a | 50 |
| hammerstein | 12 | 0.60 [0.54,0.68] | n/a | 50 |

## 4. Cost per instance (median) at B=12: candidate columns evaluated (cumulative over all revisions) and wall-clock of the fit (agent: cumulative discovery time; baselines: fit+rollout time)

| method | candidates | wall s |
|---|---|---|
| adapt_sweepB | 1400 | 20.2 |
| adapt_falsify | 5850 | 89.1 |
| L0_sweepB | 540 | 11.6 |
| all_sweepB | 3522 | 7.6 |
| oracle_struct | nan | nan |
| pysr_fixed_kalman | nan | 9.9 |
| pysr_expanded_kalman | nan | 16.2 |
| pysr_expanded_learned | nan | 16.9 |
| pysr_expanded_oracle | nan | 15.2 |
| pysr_expanded_raw | nan | 16.7 |
| sindyc_kalman | nan | 0.1 |
| sindyc_oracle | nan | 0.1 |
| weak_kalman | nan | 0.6 |
| implicit_kalman | nan | 0.0 |
| narx | nan | 0.0 |
| hammerstein | nan | 0.1 |

## 5. Model criticism (H4)

False rejection of a correct L0 explanation on dev controls (lin) and power against out-of-L0 (L0_sweepB, c_in threshold; statistic = best-L0 s_in)

| B | false rejection (lin) | power out-of-L0 | median s_in lin | median s_in out-of-L0 | AUROC |
|---|---|---|---|---|---|
| 5 | nan | 0.42 | nan | 2.66 | nan |
| 8 | nan | 0.60 | nan | 11.34 | nan |
| 12 | nan | 0.60 | nan | 16.93 | nan |

Per-family L0 rejection rate at c_in:

| B | bump | bumpfar | gdelay | quadlag | rate | saw | sqrtabs |
|---|---|---|---|---|---|---|---|
| 5 | 0.00 | 0.10 | 0.70 | 1.00 | 0.40 | 1.00 | 0.00 |
| 8 | 0.00 | 0.20 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| 12 | 0.00 | 0.20 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |

## 6. Epistemic decisions of the full agent (adapt_falsify, calibrated criticism): counts of claim / abstain_amb / abstain_ool, with claim correctness (L2) and false-discovery rate

| family | B | claim_correct | claim_wrong | abstain_amb | abstain_ool |
|---|---|---|---|---|---|
| bump | 5 | 0 | 3 | 3 | 4 |
| bump | 8 | 1 | 7 | 0 | 2 |
| bump | 12 | 0 | 8 | 0 | 2 |
| bumpfar | 5 | 9 | 1 | 0 | 0 |
| bumpfar | 8 | 8 | 2 | 0 | 0 |
| bumpfar | 12 | 9 | 1 | 0 | 0 |
| gdelay | 5 | 0 | 6 | 0 | 4 |
| gdelay | 8 | 0 | 4 | 0 | 6 |
| gdelay | 12 | 4 | 0 | 1 | 5 |
| quadlag | 5 | 7 | 0 | 1 | 2 |
| quadlag | 8 | 10 | 0 | 0 | 0 |
| quadlag | 12 | 9 | 1 | 0 | 0 |
| rate | 5 | 4 | 1 | 1 | 4 |
| rate | 8 | 10 | 0 | 0 | 0 |
| rate | 12 | 6 | 3 | 0 | 1 |
| saw | 5 | 0 | 0 | 0 | 10 |
| saw | 8 | 0 | 0 | 0 | 10 |
| saw | 12 | 0 | 0 | 0 | 10 |
| sqrtabs | 5 | 1 | 2 | 3 | 4 |
| sqrtabs | 8 | 0 | 7 | 1 | 2 |
| sqrtabs | 12 | 2 | 8 | 0 | 0 |

Pooled false-discovery rate among claims (wrong-structure claims / all claims): B=5: 13/34, B=8: 20/49, B=12: 21/51

## 7. H3 - first budget at which the agent holds a correct claim (claim and L2; 16 if never), identifiable out-of-L0, mean over instances

| design | mean first-correct B | paired diff vs falsify [95%] |
|---|---|---|
| adapt_falsify | 11.28 | - |
| adapt_sweepB | 11.88 | -0.60 [-1.42,0.22] (falsify minus adapt_sweepB; negative favours falsify) |
| adapt_random | 12.18 | -0.90 [-1.96,0.14] (falsify minus adapt_random; negative favours falsify) |
| adapt_ens | 13.20 | -1.92 [-2.72,-1.20] (falsify minus adapt_ens; negative favours falsify) |

## 8. Learned world model (H2)

| comparison | B | dL1 [95%] | dL2 [95%] |
|---|---|---|---|
| pysr_expanded_learned - pysr_expanded_kalman | 8 | 0.04 [-0.08,0.16] | nan [nan,nan] |
| pysr_expanded_learned - pysr_expanded_kalman | 12 | 0.04 [-0.10,0.16] | nan [nan,nan] |
| pysr_fixed_learned - pysr_fixed_kalman | 8 | -0.02 [-0.14,0.10] | nan [nan,nan] |
| pysr_fixed_learned - pysr_fixed_kalman | 12 | 0.12 [-0.02,0.26] | nan [nan,nan] |
| sindyc_learned - sindyc_kalman | 8 | -0.02 [-0.06,0.00] | n/a |
| sindyc_learned - sindyc_kalman | 12 | 0.00 [0.00,0.00] | n/a |
| weak_learned - weak_kalman | 8 | 0.00 [0.00,0.00] | n/a |
| weak_learned - weak_kalman | 12 | 0.00 [0.00,0.00] | n/a |
| ord_learned_sweepB - adapt_sweepB | 8 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_learned_sweepB - adapt_sweepB | 12 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_kalman_sweepB - adapt_sweepB | 8 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_kalman_sweepB - adapt_sweepB | 12 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_learned_sweepB - ord_kalman_sweepB | 8 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_learned_sweepB - ord_kalman_sweepB | 12 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| pysr_expanded_kalman - pysr_expanded_raw | 8 | 0.18 [0.08,0.28] | nan [nan,nan] |
| pysr_expanded_kalman - pysr_expanded_raw | 12 | 0.24 [0.14,0.34] | nan [nan,nan] |
| pysr_expanded_oracle - pysr_expanded_kalman | 8 | 0.18 [0.06,0.30] | nan [nan,nan] |
| pysr_expanded_oracle - pysr_expanded_kalman | 12 | 0.56 [0.44,0.66] | nan [nan,nan] |

Stage ordering by equation-error evidence (candidates evaluated, median, B=12, identifiable out-of-L0): adapt_sweepB: 1400, ord_kalman_sweepB: 936, ord_learned_sweepB: 936, all_sweepB: 3522

## 9. Levels of success for the full agent (adapt_sweepB, identifiable out-of-L0 pooled)

| B | L1 predictive | L2 structural | L3 mechanistic | predictive-but-not-structural |
|---|---|---|---|---|
| 5 | 0.86 [0.80,0.92] | 0.22 [0.14,0.30] | 0.22 [0.14,0.30] | 0.64 |
| 8 | 0.94 [0.88,1.00] | 0.44 [0.38,0.50] | 0.44 [0.38,0.50] | 0.50 |
| 12 | 1.00 [1.00,1.00] | 0.38 [0.32,0.44] | 0.38 [0.32,0.44] | 0.62 |

Baseline divergence flags (fraction of rollouts flagged diverged): sindyc_kalman: 0.00, weak_kalman: 0.00, implicit_kalman: 0.00

## 10. Fixed-language search vs adaptive expansion (same data, B=12): RMSE medians

| family | L0_sweepB | adapt_sweepB | all_sweepB | expansion stage used (adapt_sweepB, mode) |
|---|---|---|---|---|
| bump | 0.012 | 0.012 | 0.004 | 0 |
| bumpfar | 0.002 | 0.002 | 0.002 | 0 |
| gdelay | 0.027 | 0.013 | 0.013 | 3 |
| quadlag | 0.045 | 0.002 | 0.002 | 3 |
| rate | 0.027 | 0.002 | 0.002 | 2 |
| saw | 0.266 | 0.268 | 0.262 |  |
| sqrtabs | 0.017 | 0.017 | 0.003 | 0 |