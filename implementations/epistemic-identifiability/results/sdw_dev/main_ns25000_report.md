# SDW development evaluation (ns 25000): 360 instances (40 per family), paired; 95% bootstrap CIs over instances (10000 resamples)

Primary outcome: functional recovery = RMSE of predicted x3 on 24 fresh admissible programmes <= tau=0.05. Agent rows use the agent's best hypothesis irrespective of abstention (that is the *nocrit* claim); abstention outcomes are in section 3.

## 1. Functional recovery rate (ok)  — groups: known / unfamiliar-in-language / osc / unreach

### B=3

| method | known | unfamiliar | all in-language | osc | unreach |
|---|---|---|---|---|---|
| agent[falsify] | 0.80 [0.72,0.87] | 0.64 [0.56,0.71] | 0.71 [0.65,0.76] | 0.28 [0.15,0.42] | 0.97 [0.93,1.00] |
| agent[sweepA] | 0.70 [0.62,0.78] | 0.59 [0.51,0.66] | 0.64 [0.58,0.69] | 0.15 [0.05,0.28] | 1.00 [1.00,1.00] |
| agent[sweepB] | 0.70 [0.62,0.78] | 0.59 [0.51,0.66] | 0.64 [0.58,0.69] | 0.15 [0.05,0.28] | 1.00 [1.00,1.00] |
| agent[random] | 0.89 [0.83,0.94] | 0.64 [0.57,0.72] | 0.75 [0.70,0.80] | 0.25 [0.12,0.38] | 1.00 [1.00,1.00] |
| agent[ens] | 0.62 [0.54,0.71] | 0.39 [0.31,0.46] | 0.49 [0.43,0.55] | 0.23 [0.10,0.35] | 1.00 [1.00,1.00] |
| agent[eig] | 0.80 [0.72,0.87] | 0.64 [0.57,0.72] | 0.71 [0.66,0.76] | 0.17 [0.07,0.30] | 0.97 [0.93,1.00] |
| agent[declared_eig] | 0.93 [0.88,0.97] | 0.22 [0.16,0.28] | 0.53 [0.46,0.58] | 0.80 [0.68,0.93] | 1.00 [1.00,1.00] |
| agent[falsify_nou2] | 0.72 [0.64,0.80] | 0.62 [0.54,0.69] | 0.66 [0.61,0.72] | 0.23 [0.10,0.35] | 1.00 [1.00,1.00] |
| baseline[bayes_declared] | 0.87 [0.80,0.93] | 0.21 [0.15,0.28] | 0.49 [0.44,0.55] | 0.68 [0.53,0.82] | 1.00 [1.00,1.00] |
| baseline[grammar_sweep] | 0.70 [0.62,0.78] | 0.59 [0.51,0.66] | 0.64 [0.58,0.69] | 0.15 [0.05,0.28] | 1.00 [1.00,1.00] |
| baseline[narx] | 0.07 [0.03,0.12] | 0.01 [0.00,0.03] | 0.04 [0.02,0.06] | 0.00 [0.00,0.00] | 0.20 [0.07,0.33] |
| baseline[hammerstein] | 0.13 [0.07,0.19] | 0.19 [0.13,0.26] | 0.17 [0.12,0.21] | 0.00 [0.00,0.00] | 0.25 [0.12,0.40] |
| baseline[sindyc_raw] | 0.24 [0.17,0.32] | 0.07 [0.04,0.12] | 0.15 [0.11,0.19] | 0.12 [0.03,0.23] | 0.07 [0.00,0.17] |
| baseline[sindyc_embed] | 0.02 [0.00,0.04] | 0.02 [0.00,0.04] | 0.02 [0.00,0.04] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] |
| baseline[sindyc_learned] | 0.56 [0.47,0.65] | 0.18 [0.12,0.24] | 0.34 [0.29,0.40] | 0.50 [0.35,0.65] | 0.30 [0.15,0.45] |
| baseline[sindyc_oracle] (ORACLE state, privileged) | 0.58 [0.49,0.68] | 0.18 [0.12,0.24] | 0.35 [0.30,0.41] | 0.33 [0.17,0.47] | 0.78 [0.65,0.90] |
| baseline[sindyc_dict_raw] | 0.00 [0.00,0.00] | 0.01 [0.00,0.02] | 0.00 [0.00,0.01] | 0.00 [0.00,0.00] | 0.12 [0.03,0.23] |
| baseline[sindyc_dict_learned] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.07 [0.00,0.17] |
| baseline[sindyc_dict_oracle] (ORACLE state, privileged) | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.03 [0.00,0.07] |

### B=5

| method | known | unfamiliar | all in-language | osc | unreach |
|---|---|---|---|---|---|
| agent[falsify] | 1.00 [1.00,1.00] | 0.87 [0.81,0.92] | 0.93 [0.89,0.95] | 0.70 [0.55,0.82] | 1.00 [1.00,1.00] |
| agent[sweepA] | 1.00 [1.00,1.00] | 0.96 [0.92,0.99] | 0.97 [0.96,0.99] | 0.65 [0.50,0.80] | 1.00 [1.00,1.00] |
| agent[sweepB] | 1.00 [1.00,1.00] | 0.81 [0.74,0.86] | 0.89 [0.85,0.93] | 0.88 [0.75,0.97] | 1.00 [1.00,1.00] |
| agent[random] | 0.98 [0.96,1.00] | 0.88 [0.82,0.93] | 0.92 [0.89,0.95] | 0.72 [0.57,0.85] | 1.00 [1.00,1.00] |
| agent[ens] | 0.92 [0.87,0.97] | 0.69 [0.62,0.76] | 0.79 [0.74,0.84] | 0.45 [0.30,0.60] | 1.00 [1.00,1.00] |
| agent[eig] | 1.00 [1.00,1.00] | 0.86 [0.80,0.91] | 0.92 [0.89,0.95] | 0.68 [0.53,0.82] | 1.00 [1.00,1.00] |
| agent[declared_eig] | 1.00 [1.00,1.00] | 0.23 [0.17,0.30] | 0.56 [0.50,0.62] | 0.72 [0.57,0.85] | 1.00 [1.00,1.00] |
| agent[falsify_nou2] | 1.00 [1.00,1.00] | 0.89 [0.84,0.94] | 0.94 [0.91,0.96] | 0.45 [0.30,0.60] | 1.00 [1.00,1.00] |
| baseline[bayes_declared] | 1.00 [1.00,1.00] | 0.24 [0.17,0.31] | 0.57 [0.51,0.62] | 0.70 [0.55,0.82] | 1.00 [1.00,1.00] |
| baseline[grammar_sweep] | 1.00 [1.00,1.00] | 0.81 [0.74,0.86] | 0.89 [0.85,0.93] | 0.88 [0.75,0.97] | 1.00 [1.00,1.00] |
| baseline[narx] | 0.05 [0.02,0.09] | 0.01 [0.00,0.03] | 0.03 [0.01,0.05] | 0.00 [0.00,0.00] | 0.15 [0.05,0.28] |
| baseline[hammerstein] | 0.50 [0.41,0.59] | 0.38 [0.31,0.46] | 0.43 [0.38,0.49] | 0.00 [0.00,0.00] | 0.65 [0.50,0.80] |
| baseline[sindyc_raw] | 0.42 [0.33,0.52] | 0.17 [0.11,0.23] | 0.28 [0.23,0.33] | 0.28 [0.15,0.42] | 1.00 [1.00,1.00] |
| baseline[sindyc_embed] | 0.09 [0.04,0.15] | 0.03 [0.01,0.05] | 0.05 [0.03,0.08] | 0.05 [0.00,0.12] | 0.17 [0.07,0.30] |
| baseline[sindyc_learned] | 0.67 [0.58,0.75] | 0.19 [0.14,0.26] | 0.40 [0.34,0.45] | 0.42 [0.28,0.57] | 1.00 [1.00,1.00] |
| baseline[sindyc_oracle] (ORACLE state, privileged) | 0.58 [0.49,0.67] | 0.21 [0.15,0.28] | 0.37 [0.31,0.43] | 0.33 [0.17,0.47] | 1.00 [1.00,1.00] |
| baseline[sindyc_dict_raw] | 0.00 [0.00,0.00] | 0.01 [0.00,0.02] | 0.00 [0.00,0.01] | 0.00 [0.00,0.00] | 0.15 [0.05,0.28] |
| baseline[sindyc_dict_learned] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 0.15 [0.05,0.28] |
| baseline[sindyc_dict_oracle] (ORACLE state, privileged) | 0.01 [0.00,0.03] | 0.01 [0.00,0.03] | 0.01 [0.00,0.03] | 0.00 [0.00,0.00] | 0.12 [0.03,0.23] |

### B=8

| method | known | unfamiliar | all in-language | osc | unreach |
|---|---|---|---|---|---|
| agent[falsify] | 1.00 [1.00,1.00] | 0.95 [0.91,0.98] | 0.97 [0.95,0.99] | 0.78 [0.65,0.90] | 1.00 [1.00,1.00] |
| agent[sweepA] | 1.00 [1.00,1.00] | 0.99 [0.97,1.00] | 0.99 [0.98,1.00] | 0.45 [0.30,0.60] | 1.00 [1.00,1.00] |
| agent[sweepB] | 1.00 [1.00,1.00] | 0.95 [0.91,0.98] | 0.97 [0.95,0.99] | 0.88 [0.78,0.97] | 1.00 [1.00,1.00] |
| agent[random] | 1.00 [1.00,1.00] | 0.98 [0.96,1.00] | 0.99 [0.97,1.00] | 0.80 [0.68,0.93] | 1.00 [1.00,1.00] |
| agent[ens] | 0.97 [0.93,0.99] | 0.88 [0.82,0.93] | 0.91 [0.88,0.95] | 0.45 [0.30,0.60] | 1.00 [1.00,1.00] |
| agent[eig] | 1.00 [1.00,1.00] | 0.96 [0.93,0.99] | 0.98 [0.96,0.99] | 0.60 [0.45,0.75] | 1.00 [1.00,1.00] |
| agent[declared_eig] | 1.00 [1.00,1.00] | 0.25 [0.18,0.32] | 0.57 [0.51,0.63] | 0.60 [0.45,0.75] | 1.00 [1.00,1.00] |
| agent[falsify_nou2] | 1.00 [1.00,1.00] | 0.98 [0.96,1.00] | 0.99 [0.97,1.00] | 0.53 [0.38,0.68] | 1.00 [1.00,1.00] |
| baseline[bayes_declared] | 1.00 [1.00,1.00] | 0.25 [0.18,0.32] | 0.57 [0.51,0.63] | 0.68 [0.53,0.82] | 1.00 [1.00,1.00] |
| baseline[grammar_sweep] | 1.00 [1.00,1.00] | 0.95 [0.91,0.98] | 0.97 [0.95,0.99] | 0.88 [0.78,0.97] | 1.00 [1.00,1.00] |
| baseline[narx] | 0.27 [0.19,0.35] | 0.11 [0.06,0.16] | 0.17 [0.13,0.22] | 0.10 [0.03,0.20] | 0.23 [0.10,0.35] |
| baseline[hammerstein] | 0.53 [0.43,0.62] | 0.44 [0.37,0.52] | 0.48 [0.42,0.54] | 0.00 [0.00,0.00] | 0.72 [0.57,0.85] |
| baseline[sindyc_raw] | 0.45 [0.36,0.53] | 0.17 [0.11,0.23] | 0.29 [0.24,0.34] | 0.30 [0.17,0.45] | 1.00 [1.00,1.00] |
| baseline[sindyc_embed] | 0.28 [0.20,0.37] | 0.07 [0.03,0.11] | 0.16 [0.12,0.20] | 0.07 [0.00,0.17] | 0.57 [0.42,0.72] |
| baseline[sindyc_learned] | 0.68 [0.59,0.76] | 0.17 [0.12,0.24] | 0.39 [0.33,0.45] | 0.60 [0.45,0.75] | 1.00 [1.00,1.00] |
| baseline[sindyc_oracle] (ORACLE state, privileged) | 0.62 [0.54,0.71] | 0.20 [0.14,0.26] | 0.38 [0.33,0.44] | 0.50 [0.35,0.65] | 1.00 [1.00,1.00] |
| baseline[sindyc_dict_raw] | 0.00 [0.00,0.00] | 0.01 [0.00,0.02] | 0.00 [0.00,0.01] | 0.00 [0.00,0.00] | 0.15 [0.05,0.28] |
| baseline[sindyc_dict_learned] | 0.17 [0.11,0.25] | 0.09 [0.04,0.13] | 0.12 [0.09,0.16] | 0.03 [0.00,0.07] | 0.35 [0.20,0.50] |
| baseline[sindyc_dict_oracle] (ORACLE state, privileged) | 0.07 [0.03,0.12] | 0.05 [0.02,0.09] | 0.06 [0.03,0.09] | 0.00 [0.00,0.00] | 0.50 [0.35,0.65] |

### Per-family recovery, B=5 (agent[falsify] | agent[sweepB] | grammar | bayes_declared | narx | hammerstein | sindyc_dict_raw | sindyc_raw)

| family | falsify | sweepB | grammar | bayes | narx | hammer | dict_raw | raw |
|---|---|---|---|---|---|---|---|
| lin | 1.00 | 1.00 | 1.00 | 1.00 | 0.15 | 0.62 | 0.00 | 0.90 |
| sat | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 0.88 | 0.00 | 0.00 |
| delay | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 | 0.38 |
| quad | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.75 | 0.00 | 0.00 |
| gate | 0.62 | 0.80 | 0.80 | 0.00 | 0.00 | 0.23 | 0.03 | 0.00 |
| backlash | 0.85 | 0.42 | 0.42 | 0.00 | 0.00 | 0.03 | 0.00 | 0.00 |
| fb | 1.00 | 1.00 | 1.00 | 0.97 | 0.05 | 0.53 | 0.00 | 0.68 |
| osc | 0.70 | 0.88 | 0.88 | 0.70 | 0.00 | 0.00 | 0.00 | 0.28 |
| unreach | 1.00 | 1.00 | 1.00 | 1.00 | 0.15 | 0.65 | 0.15 | 1.00 |

Median test RMSE (B=5) in-language: bayes_declared=0.027, grammar_sweep=0.007, narx=0.108, hammerstein=0.059, sindyc_raw=0.082, sindyc_embed=0.321, sindyc_learned=0.079, sindyc_oracle=0.080, sindyc_dict_raw=0.317, sindyc_dict_learned=0.407, sindyc_dict_oracle=0.192, agent[falsify]=0.008

## 2. Pre-fixed decision rules (paired risk differences in recovery rate)

**H1** (grammar search vs best baseline; agent[falsify] without criticism minus each baseline; unfamiliar in-language families)

| B | baseline | difference |
|---|---|---|
| 5 | bayes_declared | 0.62 [0.55,0.70] |
| 5 | narx | 0.86 [0.80,0.91] |
| 5 | hammerstein | 0.49 [0.41,0.57] |
| 5 | sindyc_raw | 0.70 [0.63,0.77] |
| 5 | sindyc_embed | 0.84 [0.79,0.90] |
| 5 | sindyc_learned | 0.68 [0.60,0.74] |
| 5 | sindyc_oracle (oracle) | 0.66 [0.58,0.73] |
| 5 | sindyc_dict_raw | 0.86 [0.81,0.91] |
| 5 | sindyc_dict_learned | 0.87 [0.81,0.92] |
| 5 | sindyc_dict_oracle (oracle) | 0.86 [0.80,0.91] |
| 8 | bayes_declared | 0.70 [0.63,0.77] |
| 8 | narx | 0.84 [0.79,0.90] |
| 8 | hammerstein | 0.51 [0.42,0.59] |
| 8 | sindyc_raw | 0.78 [0.72,0.84] |
| 8 | sindyc_embed | 0.88 [0.83,0.93] |
| 8 | sindyc_learned | 0.78 [0.71,0.84] |
| 8 | sindyc_oracle (oracle) | 0.75 [0.68,0.82] |
| 8 | sindyc_dict_raw | 0.94 [0.91,0.97] |
| 8 | sindyc_dict_learned | 0.86 [0.81,0.91] |
| 8 | sindyc_dict_oracle (oracle) | 0.90 [0.85,0.94] |

Best baseline (by point estimate): B=5: hammerstein diff 0.49 [0.41,0.57]; B=8: hammerstein diff 0.51 [0.42,0.59]

**H1 SUPPORTED** against the best non-oracle baseline at both budgets: B=5: hammerstein 0.49 [0.41,0.57]; B=8: hammerstein 0.51 [0.42,0.59]

**H2** (falsification design vs alternatives; risk difference in recovery rate, agent[falsify] minus X; groups unfamiliar / in-language)

| B | X | unfamiliar | all in-language |
|---|---|---|---|
| 3 | sweepA | 0.05 [0.00,0.11] | 0.07 [0.03,0.11] |
| 3 | sweepB | 0.05 [0.00,0.11] | 0.07 [0.03,0.11] |
| 3 | random | -0.01 [-0.09,0.08] | -0.04 [-0.10,0.01] |
| 3 | ens | 0.25 [0.16,0.34] | 0.22 [0.15,0.29] |
| 3 | eig | -0.01 [-0.07,0.05] | -0.00 [-0.05,0.05] |
| 3 | falsify_nou2 | 0.02 [-0.02,0.06] | 0.04 [0.01,0.08] |
| 5 | sweepA | -0.09 [-0.15,-0.03] | -0.05 [-0.09,-0.02] |
| 5 | sweepB | 0.06 [-0.01,0.13] | 0.04 [-0.00,0.07] |
| 5 | random | -0.01 [-0.08,0.06] | 0.00 [-0.04,0.05] |
| 5 | ens | 0.17 [0.09,0.26] | 0.14 [0.09,0.19] |
| 5 | eig | 0.01 [-0.05,0.07] | 0.01 [-0.03,0.04] |
| 5 | falsify_nou2 | -0.03 [-0.08,0.03] | -0.01 [-0.05,0.02] |
| 8 | sweepA | -0.04 [-0.07,-0.01] | -0.02 [-0.04,-0.00] |
| 8 | sweepB | 0.00 [-0.04,0.04] | 0.00 [-0.03,0.03] |
| 8 | random | -0.03 [-0.07,0.01] | -0.02 [-0.04,0.00] |
| 8 | ens | 0.07 [0.03,0.13] | 0.06 [0.03,0.09] |
| 8 | eig | -0.01 [-0.05,0.03] | -0.01 [-0.03,0.01] |
| 8 | falsify_nou2 | -0.03 [-0.07,0.01] | -0.02 [-0.04,0.00] |

Decisive comparison (vs the better fixed sweep, all in-language): B=3: 0.07 [0.03,0.11]; B=5: -0.05 [-0.09,-0.02]; B=8: -0.02 [-0.04,-0.00]

**H2 NOT SUPPORTED** (CI>0 against the better fixed sweep at 1 of 3 budgets; rule: >=2 budgets and CI>0 against every alternative listed in the protocol).

Median RMSE by design (all in-language, B=3 / 5 / 8): falsify: 0.022 / 0.008 / 0.005; sweepA: 0.030 / 0.010 / 0.009; sweepB: 0.030 / 0.007 / 0.004; random: 0.018 / 0.010 / 0.006; ens: 0.054 / 0.012 / 0.006; eig: 0.021 / 0.011 / 0.009

## 3. Criticism and abstention (agent[falsify]; modes: full = in-sample + out-of-sample chi-square + ambiguity; crit_in = in-sample + ambiguity; nocrit)

| B | mode | coverage (in-lang) | precision P(ok given claim) | in-lang false rejection (abstain_ool) | in-lang abstain_amb | osc claim rate | osc claim with RMSE>tau | unreach claim&ok | decision accuracy (all 9 families) |
|---|---|---|---|---|---|---|---|---|---|
| 3 | full | 0.10 [0.06,0.13] | 0.85 | 0.62 [0.57,0.68] | 0.28 [0.23,0.33] | 0.05 [0.00,0.12] | 0.05 [0.00,0.12] | 0.17 [0.07,0.30] | 0.19 |
| 3 | crit_in | 0.25 [0.20,0.31] | 0.86 | 0.12 [0.08,0.16] | 0.63 [0.57,0.69] | 0.05 [0.00,0.12] | 0.05 [0.00,0.12] | 0.85 [0.72,0.95] | 0.37 |
| 3 | nocrit | 1.00 [1.00,1.00] | 0.71 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 1.00 [1.00,1.00] | 0.72 [0.57,0.85] | 0.97 [0.93,1.00] | 0.66 |
| 5 | full | 0.42 [0.36,0.47] | 0.91 | 0.47 [0.41,0.53] | 0.11 [0.07,0.14] | 0.05 [0.00,0.12] | 0.00 [0.00,0.00] | 0.80 [0.68,0.93] | 0.49 |
| 5 | crit_in | 0.61 [0.56,0.67] | 0.92 | 0.12 [0.09,0.16] | 0.26 [0.21,0.31] | 0.12 [0.03,0.25] | 0.00 [0.00,0.00] | 0.88 [0.78,0.97] | 0.64 |
| 5 | nocrit | 1.00 [1.00,1.00] | 0.93 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 1.00 [1.00,1.00] | 0.30 [0.17,0.45] | 1.00 [1.00,1.00] | 0.83 |
| 8 | full | 0.70 [0.65,0.76] | 0.97 | 0.26 [0.21,0.31] | 0.03 [0.01,0.05] | 0.03 [0.00,0.07] | 0.00 [0.00,0.00] | 0.90 [0.80,0.97] | 0.74 |
| 8 | crit_in | 0.80 [0.76,0.85] | 0.97 | 0.15 [0.11,0.19] | 0.05 [0.03,0.07] | 0.03 [0.00,0.07] | 0.00 [0.00,0.00] | 0.93 [0.82,1.00] | 0.82 |
| 8 | nocrit | 1.00 [1.00,1.00] | 0.97 | 0.00 [0.00,0.00] | 0.00 [0.00,0.00] | 1.00 [1.00,1.00] | 0.23 [0.10,0.35] | 1.00 [1.00,1.00] | 0.87 |

**Per-family outcome shares, B=8, mode full** (claim / abstain_ool / abstain_amb):

| family | claim | abstain_ool | abstain_amb |
|---|---|---|---|
| lin | 0.70 | 0.28 | 0.03 |
| sat | 0.78 | 0.17 | 0.05 |
| delay | 0.80 | 0.15 | 0.05 |
| quad | 0.90 | 0.10 | 0.00 |
| gate | 0.62 | 0.38 | 0.00 |
| backlash | 0.62 | 0.38 | 0.00 |
| fb | 0.50 | 0.40 | 0.10 |
| osc | 0.03 | 0.97 | 0.00 |
| unreach | 0.90 | 0.07 | 0.03 |

**AUROC of the in-sample misfit statistic (-log10 min p) for osc vs in-language truth** (higher = better flag)

| B | agent[falsify] | agent[sweepB] | grammar_sweep | bayes_declared (GOF, declared class) |
|---|---|---|---|---|
| 3 | 0.87 | 0.81 | 0.81 | 0.68 |
| 5 | 0.94 | 0.86 | 0.86 | 0.47 |
| 8 | 0.98 | 0.98 | 0.98 | 0.55 |

**epsilon sensitivity (analysis only; primary eps=0.5 sigma-hat)**, agent[falsify], B=8, mode full: coverage / precision / decision accuracy

* eps=0.25: coverage 0.55, precision 0.96, accuracy 0.62
* eps=0.5: coverage 0.70, precision 0.97, accuracy 0.74
* eps=1.0: coverage 0.72, precision 0.97, accuracy 0.76
* eps=2.0: coverage 0.73, precision 0.97, accuracy 0.76

## 4. Representation role (H4)

**Proposal recall@3** (true primitive among the 3 best-scoring primitives by BIC-penalised equation-error regression on the reconstructed hidden state; sweep-B data, 6 episodes; in-language families):

| state | known | unfamiliar | all in-language |
|---|---|---|---|
| oracle (privileged) | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] |
| analytic | 0.87 [0.80,0.93] | 0.87 [0.81,0.92] | 0.87 [0.83,0.91] |
| learned | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] | 1.00 [1.00,1.00] |

learned minus analytic recall@3: in-language 0.13 [0.09,0.17], unfamiliar 0.13 [0.08,0.19]; oracle minus analytic: 0.13 [0.09,0.17]

**SINDYc recovery by state set (B=8, in-language, library degree-1 tuned / dictionary):**

| state set | linear library | dictionary library |
|---|---|---|
| raw | 0.29 [0.24,0.34] | 0.00 [0.00,0.01] |
| embed | 0.16 [0.12,0.20] | – |
| learned | 0.39 [0.33,0.45] | 0.12 [0.09,0.16] |
| oracle (ORACLE) | 0.38 [0.33,0.44] | 0.06 [0.03,0.09] |

SINDYc learned minus embed (B=8): 0.23 [0.18,0.28]; learned minus raw: 0.10 [0.06,0.14].

## 5. Decision accuracy (synergy and ablations, all 9 families; right = correct claim for in-language/unreach, abstention for osc)

| variant | B=3 | B=5 | B=8 |
|---|---|---|---|
| full agent (falsify, criticism full) | 0.19 | 0.49 | 0.74 |
| no criticism | 0.66 | 0.83 | 0.87 |
| in-sample criticism only | 0.37 | 0.64 | 0.82 |
| no active design: sweep B | 0.41 | 0.59 | 0.70 |
| no active design: sweep A | 0.41 | 0.61 | 0.71 |
| random design | 0.30 | 0.45 | 0.63 |
| generic ensemble-variance design | 0.15 | 0.29 | 0.56 |
| declared-class EIG design (structure search kept) | 0.24 | 0.50 | 0.61 |
| no structure generation (declared class + EIG) | 0.24 | 0.42 | 0.49 |
| no u2 interventions in pool | 0.28 | 0.54 | 0.73 |

Paired decision-accuracy difference, full agent minus variant (all 9 families pooled; CI over instances):

* no criticism: B=3 -0.47 [-0.54,-0.40] | B=5 -0.34 [-0.41,-0.28] | B=8 -0.13 [-0.19,-0.07]
* in-sample criticism only: B=3 -0.18 [-0.22,-0.14] | B=5 -0.15 [-0.19,-0.11] | B=8 -0.08 [-0.11,-0.05]
* no active design: sweep B: B=3 -0.22 [-0.27,-0.18] | B=5 -0.10 [-0.15,-0.04] | B=8 0.04 [-0.02,0.09]
* no active design: sweep A: B=3 -0.22 [-0.27,-0.18] | B=5 -0.12 [-0.18,-0.07] | B=8 0.03 [-0.02,0.08]
* random design: B=3 -0.11 [-0.16,-0.06] | B=5 0.04 [-0.02,0.10] | B=8 0.11 [0.05,0.17]
* generic ensemble-variance design: B=3 0.04 [0.01,0.07] | B=5 0.20 [0.14,0.26] | B=8 0.18 [0.12,0.24]
* declared-class EIG design (structure search kept): B=3 -0.06 [-0.09,-0.02] | B=5 -0.01 [-0.07,0.05] | B=8 0.12 [0.07,0.19]
* no structure generation (declared class + EIG): B=3 -0.05 [-0.10,-0.00] | B=5 0.06 [0.00,0.13] | B=8 0.25 [0.19,0.31]
* no u2 interventions in pool: B=3 -0.09 [-0.12,-0.06] | B=5 -0.05 [-0.10,0.00] | B=8 0.01 [-0.04,0.06]