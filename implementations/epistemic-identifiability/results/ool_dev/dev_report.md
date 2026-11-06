# OOL development run (namespace 30000)

Manifest sha256: `f8a09dea01ca1d3807237bd4b041d8ab354c5a78378758a62cbaf40ccbced1d2`; instances: 60; families: bilin, leak, lin, rectsq, sin, thresh. Cal thresholds: c_in={'5': 2.9211034554667945, '8': 2.959068486815061, '12': 3.469841235022011}, c_oos={'5': 10.465359921980648, '8': 4.515395951854984, '12': 2.5431422533663137}.

## 1. Per-family recovery (L1 predictive = RMSE<=0.05; L2 structural = signature match), B=8 and 12

### B=8

| method | bilin L1/L2 | leak L1/L2 | lin L1/L2 | rectsq L1/L2 | sin L1/L2 | thresh L1/L2 |
|---|---|---|---|---|---|---|
| adapt_sweepB | 0.9/0.9 | 1.0/0.9 | 1.0/0.7 | 0.9/0.0 | 0.9/0.0 | 1.0/0.9 |
| adapt_falsify | 0.7/0.7 | 1.0/0.8 | 1.0/0.5 | 1.0/0.0 | 1.0/0.1 | 1.0/1.0 |
| L0_sweepB | 0.4/0.0 | 1.0/0.0 | 1.0/0.7 | 0.0/0.0 | 0.9/0.0 | 1.0/0.9 |
| all_sweepB | 0.7/0.6 | 1.0/0.9 | 1.0/0.7 | 0.9/0.3 | 0.9/0.3 | 1.0/0.9 |
| oracle_struct | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 |
| pysr_fixed_kalman | 0.2/0.6 | 0.0/ | 0.6/ | 0.0/0.0 | 0.0/0.0 | 0.9/0.0 |
| pysr_expanded_kalman | 0.2/0.6 | 0.0/ | 0.6/ | 0.0/0.0 | 0.1/0.3 | 0.8/0.0 |
| pysr_expanded_learned | 0.0/0.2 | 0.0/ | 0.5/ | 0.4/0.1 | 0.0/0.7 | 0.6/0.0 |
| pysr_expanded_oracle | 0.9/0.7 | 0.1/ | 1.0/ | 0.9/0.0 | 0.5/0.5 | 1.0/0.0 |
| pysr_expanded_raw | 0.0/0.0 | 0.3/ | 0.1/ | 0.0/0.0 | 0.0/0.4 | 0.1/1.0 |
| sindyc_kalman | 0.5/ | 0.0/ | 0.7/ | 0.3/ | 0.0/ | 0.9/ |
| sindyc_oracle | 0.4/ | 0.0/ | 0.5/ | 0.1/ | 0.0/ | 0.7/ |
| weak_kalman | 0.5/ | 0.0/ | 0.8/ | 0.2/ | 0.0/ | 1.0/ |
| implicit_kalman | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| narx | 0.5/ | 0.2/ | 0.8/ | 0.1/ | 0.0/ | 0.0/ |
| hammerstein | 0.1/ | 0.0/ | 0.9/ | 0.8/ | 0.7/ | 0.7/ |

### B=12

| method | bilin L1/L2 | leak L1/L2 | lin L1/L2 | rectsq L1/L2 | sin L1/L2 | thresh L1/L2 |
|---|---|---|---|---|---|---|
| adapt_sweepB | 0.9/0.9 | 1.0/0.9 | 1.0/0.5 | 1.0/0.4 | 1.0/0.0 | 1.0/0.9 |
| adapt_falsify | 0.9/0.9 | 1.0/0.7 | 1.0/0.6 | 1.0/0.3 | 1.0/0.2 | 1.0/0.9 |
| L0_sweepB | 0.5/0.0 | 1.0/0.0 | 1.0/0.5 | 0.3/0.0 | 1.0/0.0 | 1.0/0.9 |
| all_sweepB | 0.8/0.5 | 1.0/1.0 | 1.0/0.5 | 1.0/0.4 | 1.0/0.6 | 1.0/1.0 |
| oracle_struct | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 | 1.0/1.0 |
| pysr_fixed_kalman | 0.1/0.5 | 0.0/ | 0.6/ | 0.0/0.0 | 0.1/0.0 | 0.5/0.0 |
| pysr_expanded_kalman | 0.0/0.6 | 0.0/ | 0.5/ | 0.0/0.0 | 0.1/0.1 | 0.9/0.0 |
| pysr_expanded_learned | 0.2/0.3 | 0.0/ | 0.5/ | 0.5/0.1 | 0.1/0.8 | 0.5/0.0 |
| pysr_expanded_oracle | 1.0/0.7 | 0.0/ | 1.0/ | 1.0/0.0 | 0.6/0.5 | 1.0/0.0 |
| pysr_expanded_raw | 0.0/0.0 | 0.1/ | 0.2/ | 0.0/0.0 | 0.0/0.3 | 0.1/1.0 |
| sindyc_kalman | 0.8/ | 0.0/ | 1.0/ | 0.2/ | 0.0/ | 0.9/ |
| sindyc_oracle | 0.4/ | 0.0/ | 0.5/ | 0.2/ | 0.0/ | 0.7/ |
| weak_kalman | 0.6/ | 0.0/ | 0.9/ | 0.2/ | 0.0/ | 0.8/ |
| implicit_kalman | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ | 0.0/ |
| narx | 0.7/ | 0.1/ | 0.9/ | 0.1/ | 0.0/ | 0.0/ |
| hammerstein | 0.4/ | 0.6/ | 1.0/ | 1.0/ | 0.9/ | 1.0/ |

## 2. Pooled over identifiable out-of-L0 mechanisms (95% stratified bootstrap over instances)

| method | B=5 L1 | B=5 L2 | B=8 L1 | B=8 L2 | B=12 L1 | B=12 L2 |
|---|---|---|---|---|---|---|
| adapt_sweepB | 0.65 [0.55,0.78] | 0.28 [0.17,0.38] | 0.93 [0.82,1.00] | 0.45 [0.38,0.50] | 0.97 [0.93,1.00] | 0.55 [0.45,0.65] |
| adapt_falsify | 0.68 [0.55,0.80] | 0.25 [0.15,0.35] | 0.93 [0.85,1.00] | 0.40 [0.30,0.50] | 0.97 [0.93,1.00] | 0.53 [0.40,0.65] |
| L0_sweepB | 0.42 [0.33,0.53] | 0.00 [0.00,0.00] | 0.57 [0.47,0.68] | 0.00 [0.00,0.00] | 0.70 [0.60,0.80] | 0.00 [0.00,0.00] |
| all_sweepB | 0.70 [0.57,0.82] | 0.28 [0.17,0.38] | 0.88 [0.78,0.97] | 0.53 [0.38,0.65] | 0.95 [0.88,1.00] | 0.62 [0.50,0.75] |
| oracle_struct | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] |
| pysr_fixed_kalman | n/a | n/a | 0.05 [0.00,0.12] | nan [nan,nan] | 0.05 [0.00,0.12] | nan [nan,nan] |
| pysr_expanded_kalman | n/a | n/a | 0.07 [0.00,0.15] | nan [nan,nan] | 0.03 [0.00,0.07] | nan [nan,nan] |
| pysr_expanded_learned | n/a | n/a | 0.10 [0.03,0.17] | nan [nan,nan] | 0.20 [0.10,0.30] | nan [nan,nan] |
| pysr_expanded_oracle | n/a | n/a | 0.60 [0.47,0.70] | nan [nan,nan] | 0.65 [0.57,0.72] | nan [nan,nan] |
| pysr_expanded_raw | n/a | n/a | 0.07 [0.00,0.15] | nan [nan,nan] | 0.03 [0.00,0.07] | nan [nan,nan] |
| sindyc_kalman | 0.05 [0.00,0.12] | n/a | 0.20 [0.10,0.30] | n/a | 0.25 [0.17,0.33] | n/a |
| sindyc_oracle | 0.10 [0.03,0.20] | n/a | 0.12 [0.05,0.23] | n/a | 0.15 [0.05,0.25] | n/a |
| weak_kalman | 0.03 [0.00,0.07] | n/a | 0.17 [0.07,0.28] | n/a | 0.20 [0.10,0.30] | n/a |
| implicit_kalman | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a | 0.00 [0.00,0.00] | n/a |
| narx | 0.03 [0.00,0.07] | n/a | 0.20 [0.10,0.30] | n/a | 0.23 [0.12,0.33] | n/a |
| hammerstein | 0.33 [0.20,0.45] | n/a | 0.40 [0.28,0.50] | n/a | 0.72 [0.60,0.85] | n/a |

## 3. H1 - paired differences, adapt_sweepB minus competitor (identifiable out-of-L0 pooled)

| competitor | B | dL1 | dL2 (competitor L2 only where defined) | n |
|---|---|---|---|---|
| adapt_falsify | 8 | 0.00 [-0.10,0.07] | 0.05 [-0.07,0.15] | 40 |
| adapt_falsify | 12 | 0.00 [0.00,0.00] | 0.03 [-0.10,0.15] | 40 |
| L0_sweepB | 8 | 0.35 [0.25,0.42] | 0.45 [0.38,0.50] | 40 |
| L0_sweepB | 12 | 0.28 [0.17,0.38] | 0.55 [0.45,0.65] | 40 |
| all_sweepB | 8 | 0.05 [-0.05,0.15] | -0.07 [-0.20,0.05] | 40 |
| all_sweepB | 12 | 0.03 [0.00,0.07] | -0.07 [-0.20,0.05] | 40 |
| oracle_struct | 8 | -0.07 [-0.17,0.00] | -0.55 [-0.62,-0.50] | 40 |
| oracle_struct | 12 | -0.03 [-0.07,0.00] | -0.45 [-0.55,-0.35] | 40 |
| pysr_fixed_kalman | 8 | 0.88 [0.78,0.95] | 0.10 [-0.03,0.23] | 40 |
| pysr_fixed_kalman | 12 | 0.93 [0.85,1.00] | 0.27 [0.10,0.43] | 40 |
| pysr_expanded_kalman | 8 | 0.85 [0.75,0.95] | 0.00 [-0.17,0.17] | 40 |
| pysr_expanded_kalman | 12 | 0.95 [0.88,1.00] | 0.20 [0.03,0.37] | 40 |
| pysr_expanded_learned | 8 | 0.82 [0.72,0.93] | -0.03 [-0.20,0.13] | 40 |
| pysr_expanded_learned | 12 | 0.78 [0.65,0.88] | 0.03 [-0.17,0.20] | 40 |
| pysr_expanded_oracle | 8 | 0.33 [0.23,0.40] | -0.10 [-0.27,0.07] | 40 |
| pysr_expanded_oracle | 12 | 0.33 [0.25,0.42] | 0.03 [-0.17,0.23] | 40 |
| pysr_expanded_raw | 8 | 0.85 [0.72,0.95] | 0.17 [0.03,0.27] | 40 |
| pysr_expanded_raw | 12 | 0.95 [0.88,1.00] | 0.33 [0.17,0.47] | 40 |
| sindyc_kalman | 8 | 0.72 [0.60,0.85] | n/a | 40 |
| sindyc_kalman | 12 | 0.72 [0.65,0.80] | n/a | 40 |
| sindyc_oracle | 8 | 0.80 [0.70,0.90] | n/a | 40 |
| sindyc_oracle | 12 | 0.82 [0.72,0.93] | n/a | 40 |
| weak_kalman | 8 | 0.75 [0.62,0.85] | n/a | 40 |
| weak_kalman | 12 | 0.78 [0.68,0.88] | n/a | 40 |
| implicit_kalman | 8 | 0.93 [0.82,1.00] | n/a | 40 |
| implicit_kalman | 12 | 0.97 [0.93,1.00] | n/a | 40 |
| narx | 8 | 0.72 [0.60,0.85] | n/a | 40 |
| narx | 12 | 0.75 [0.65,0.82] | n/a | 40 |
| hammerstein | 8 | 0.53 [0.42,0.62] | n/a | 40 |
| hammerstein | 12 | 0.25 [0.12,0.38] | n/a | 40 |

## 4. Cost per instance (median) at B=12: candidate columns evaluated (cumulative over all revisions) and wall-clock of the fit (agent: cumulative discovery time; baselines: fit+rollout time)

| method | candidates | wall s |
|---|---|---|
| adapt_sweepB | 1830 | 14.0 |
| adapt_falsify | 7161 | 54.9 |
| L0_sweepB | 540 | 5.4 |
| all_sweepB | 3522 | 6.8 |
| oracle_struct | nan | nan |
| pysr_fixed_kalman | nan | 6.0 |
| pysr_expanded_kalman | nan | 9.2 |
| pysr_expanded_learned | nan | 9.8 |
| pysr_expanded_oracle | nan | 9.8 |
| pysr_expanded_raw | nan | 11.5 |
| sindyc_kalman | nan | 0.1 |
| sindyc_oracle | nan | 0.1 |
| weak_kalman | nan | 0.3 |
| implicit_kalman | nan | 0.0 |
| narx | nan | 0.0 |
| hammerstein | nan | 0.0 |

## 5. Model criticism (H4)

False rejection of a correct L0 explanation on dev controls (lin) and power against out-of-L0 (L0_sweepB, c_in threshold; statistic = best-L0 s_in)

| B | false rejection (lin) | power out-of-L0 | median s_in lin | median s_in out-of-L0 | AUROC |
|---|---|---|---|---|---|
| 5 | 0.00 | 0.75 | 1.03 | 27.27 | 0.90 |
| 8 | 0.00 | 0.75 | 1.35 | 40.92 | 0.92 |
| 12 | 0.00 | 0.78 | 1.48 | 54.44 | 0.94 |

Per-family L0 rejection rate at c_in:

| B | bilin | leak | lin | rectsq | sin | thresh |
|---|---|---|---|---|---|---|
| 5 | 0.90 | 1.00 | 0.00 | 1.00 | 0.10 | 0.00 |
| 8 | 1.00 | 1.00 | 0.00 | 1.00 | 0.00 | 0.00 |
| 12 | 1.00 | 1.00 | 0.00 | 1.00 | 0.10 | 0.00 |

## 6. Epistemic decisions of the full agent (adapt_falsify, calibrated criticism): counts of claim / abstain_amb / abstain_ool, with claim correctness (L2) and false-discovery rate

| family | B | claim_correct | claim_wrong | abstain_amb | abstain_ool |
|---|---|---|---|---|---|
| bilin | 5 | 1 | 2 | 0 | 7 |
| bilin | 8 | 6 | 0 | 0 | 4 |
| bilin | 12 | 9 | 0 | 0 | 1 |
| leak | 5 | 5 | 0 | 3 | 2 |
| leak | 8 | 8 | 2 | 0 | 0 |
| leak | 12 | 7 | 3 | 0 | 0 |
| lin | 5 | 6 | 3 | 1 | 0 |
| lin | 8 | 5 | 5 | 0 | 0 |
| lin | 12 | 6 | 4 | 0 | 0 |
| rectsq | 5 | 0 | 5 | 1 | 4 |
| rectsq | 8 | 0 | 7 | 0 | 3 |
| rectsq | 12 | 2 | 6 | 1 | 1 |
| sin | 5 | 0 | 2 | 3 | 5 |
| sin | 8 | 0 | 4 | 1 | 5 |
| sin | 12 | 0 | 8 | 0 | 2 |
| thresh | 5 | 10 | 0 | 0 | 0 |
| thresh | 8 | 9 | 0 | 0 | 1 |
| thresh | 12 | 9 | 1 | 0 | 0 |

Pooled false-discovery rate among claims (wrong-structure claims / all claims): B=5: 12/34, B=8: 18/46, B=12: 22/55

## 7. H3 - first budget at which the agent holds a correct claim (claim and L2; 16 if never), identifiable out-of-L0, mean over instances

| design | mean first-correct B | paired diff vs falsify [95%] |
|---|---|---|
| adapt_falsify | 11.85 | - |
| adapt_sweepB | 11.07 | 0.78 [0.12,1.43] (falsify minus adapt_sweepB; negative favours falsify) |
| adapt_random | 11.38 | 0.47 [-0.88,1.85] (falsify minus adapt_random; negative favours falsify) |
| adapt_ens | 12.95 | -1.10 [-1.80,-0.40] (falsify minus adapt_ens; negative favours falsify) |

## 8. Learned world model (H2)

| comparison | B | dL1 [95%] | dL2 [95%] |
|---|---|---|---|
| pysr_expanded_learned - pysr_expanded_kalman | 8 | 0.03 [-0.07,0.12] | nan [nan,nan] |
| pysr_expanded_learned - pysr_expanded_kalman | 12 | 0.17 [0.05,0.30] | nan [nan,nan] |
| pysr_fixed_learned - pysr_fixed_kalman | 8 | 0.07 [-0.05,0.20] | nan [nan,nan] |
| pysr_fixed_learned - pysr_fixed_kalman | 12 | 0.07 [-0.05,0.20] | nan [nan,nan] |
| sindyc_learned - sindyc_kalman | 8 | -0.10 [-0.20,0.00] | n/a |
| sindyc_learned - sindyc_kalman | 12 | -0.15 [-0.25,-0.05] | n/a |
| weak_learned - weak_kalman | 8 | -0.07 [-0.17,0.03] | n/a |
| weak_learned - weak_kalman | 12 | -0.10 [-0.20,0.00] | n/a |
| ord_learned_sweepB - adapt_sweepB | 8 | 0.00 [0.00,0.00] | 0.03 [-0.07,0.12] |
| ord_learned_sweepB - adapt_sweepB | 12 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_kalman_sweepB - adapt_sweepB | 8 | 0.00 [0.00,0.00] | 0.05 [-0.03,0.12] |
| ord_kalman_sweepB - adapt_sweepB | 12 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| ord_learned_sweepB - ord_kalman_sweepB | 8 | 0.00 [0.00,0.00] | -0.03 [-0.10,0.05] |
| ord_learned_sweepB - ord_kalman_sweepB | 12 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| pysr_expanded_kalman - pysr_expanded_raw | 8 | 0.00 [-0.10,0.10] | nan [nan,nan] |
| pysr_expanded_kalman - pysr_expanded_raw | 12 | 0.00 [-0.07,0.07] | nan [nan,nan] |
| pysr_expanded_oracle - pysr_expanded_kalman | 8 | 0.53 [0.40,0.65] | nan [nan,nan] |
| pysr_expanded_oracle - pysr_expanded_kalman | 12 | 0.62 [0.55,0.70] | nan [nan,nan] |

Stage ordering by equation-error evidence (candidates evaluated, median, B=12, identifiable out-of-L0): adapt_sweepB: 1830, ord_kalman_sweepB: 3264, ord_learned_sweepB: 3264, all_sweepB: 3522

## 9. Levels of success for the full agent (adapt_sweepB, identifiable out-of-L0 pooled)

| B | L1 predictive | L2 structural | L3 mechanistic | predictive-but-not-structural |
|---|---|---|---|---|
| 5 | 0.65 [0.55,0.75] | 0.28 [0.17,0.38] | 0.28 [0.17,0.38] | 0.38 |
| 8 | 0.93 [0.82,1.00] | 0.45 [0.38,0.50] | 0.45 [0.38,0.50] | 0.47 |
| 12 | 0.97 [0.93,1.00] | 0.55 [0.45,0.65] | 0.55 [0.45,0.65] | 0.42 |

Baseline divergence flags (fraction of rollouts flagged diverged): sindyc_kalman: 0.00, weak_kalman: 0.00, implicit_kalman: 0.00

## 10. Fixed-language search vs adaptive expansion (same data, B=12): RMSE medians

| family | L0_sweepB | adapt_sweepB | all_sweepB | expansion stage used (adapt_sweepB, mode) |
|---|---|---|---|---|
| bilin | 0.047 | 0.002 | 0.010 | 4 |
| leak | 0.024 | 0.003 | 0.002 | 2 |
| lin | 0.003 | 0.003 | 0.003 | 0 |
| rectsq | 0.062 | 0.012 | 0.003 | 1 |
| sin | 0.016 | 0.016 | 0.004 | 0 |
| thresh | 0.002 | 0.002 | 0.002 | 0 |