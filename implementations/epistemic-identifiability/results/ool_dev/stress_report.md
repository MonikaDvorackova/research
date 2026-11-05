# Stress tests (development families sin, rectsq, leak, bilin, thresh; 6 instances each; namespace 32000)

L1 = RMSE<=0.05, L2 = signature match; pooled over the four identifiable families (n=24 per cell, no CI: 24 instances); thresh = fraction claiming the null/null-equivalent explanation; L0 reject = fraction of identifiable instances on which calibrated criticism rejects L0.

| condition | B | method | L1 | L2 | thresh null-claim | L0 reject |
|---|---|---|---|---|---|---|
| noise1 | 8 | adapt_sweepB | 1.00 | 0.50 | 0.83 | |
| noise1 | 8 | all_sweepB | 0.92 | 0.62 | 0.83 | |
| noise1 | 8 | L0_sweepB | 0.67 | 0.00 | 0.83 | 0.75 |
| noise1 | 8 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| noise1 | 12 | adapt_sweepB | 1.00 | 0.54 | 0.83 | |
| noise1 | 12 | all_sweepB | 0.96 | 0.54 | 0.83 | |
| noise1 | 12 | L0_sweepB | 0.71 | 0.00 | 0.83 | 0.79 |
| noise1 | 12 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| noise2 | 8 | adapt_sweepB | 0.96 | 0.42 | 0.83 | |
| noise2 | 8 | all_sweepB | 0.92 | 0.54 | 0.83 | |
| noise2 | 8 | L0_sweepB | 0.67 | 0.00 | 0.83 | 0.71 |
| noise2 | 8 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| noise2 | 12 | adapt_sweepB | 0.96 | 0.46 | 0.83 | |
| noise2 | 12 | all_sweepB | 1.00 | 0.71 | 0.83 | |
| noise2 | 12 | L0_sweepB | 0.67 | 0.00 | 0.83 | 0.71 |
| noise2 | 12 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| noise3 | 8 | adapt_sweepB | 0.83 | 0.25 | 0.83 | |
| noise3 | 8 | all_sweepB | 0.92 | 0.50 | 0.83 | |
| noise3 | 8 | L0_sweepB | 0.50 | 0.00 | 0.83 | 0.54 |
| noise3 | 8 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| noise3 | 12 | adapt_sweepB | 0.96 | 0.25 | 0.83 | |
| noise3 | 12 | all_sweepB | 0.96 | 0.58 | 0.83 | |
| noise3 | 12 | L0_sweepB | 0.62 | 0.00 | 0.83 | 0.50 |
| noise3 | 12 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| nou2 | 8 | adapt_sweepB | 1.00 | 0.33 | 1.00 | |
| nou2 | 8 | all_sweepB | 0.92 | 0.50 | 1.00 | |
| nou2 | 8 | L0_sweepB | 0.71 | 0.00 | 1.00 | 0.58 |
| nou2 | 8 | oracle_struct | 1.00 | 1.00 | 1.00 | |
| nou2 | 12 | adapt_sweepB | 1.00 | 0.38 | 0.83 | |
| nou2 | 12 | all_sweepB | 1.00 | 0.46 | 0.83 | |
| nou2 | 12 | L0_sweepB | 0.79 | 0.00 | 0.83 | 0.54 |
| nou2 | 12 | oracle_struct | 1.00 | 1.00 | 1.00 | |