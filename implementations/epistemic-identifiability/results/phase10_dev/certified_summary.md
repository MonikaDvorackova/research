## A. Confidence-set coverage

LR confidence set (delta = 0.05), time-uniform over 200 training checkpoints, 60 independent Markov structures x 5 training streams (5000 episodes, uniform policy): true kernel excluded at some checkpoint in **0/300** streams (guarantee: <= 5 %; one-sided CP upper bound 0.010).

Adversarial optional stopping (Bernoulli(1/2), 2000 observations, check every n): fixed-n Clopper-Pearson interval (95 %) excludes the truth at SOME n in **468/1000** runs; the LR confidence sequence (delta = 0.05) in **32/1000**.

## B. Type-I under the intended null (kernel unchanged), 60 independent structures x 30 runs per condition (1500 test episodes)

| training policy | training episodes | certified: rejections/runs | structures with >= 1 | oracle (true kernel known) | frozen point null (simple null 'kernel = estimate') |
|---|---|---|---|---|---|
| narrow | 1000 | 0/1800 (UB 0.0017) | 0/60 | 0/1800 | 1335/1800 |
| narrow | 10000 | 0/1800 (UB 0.0017) | 0/60 | 0/1800 | 1/1800 |
| uniform | 1000 | 0/1800 (UB 0.0017) | 0/60 | 0/1800 | 0/1800 |
| uniform | 10000 | 0/1800 (UB 0.0017) | 0/60 | 0/1800 | 0/1800 |

## C. Detection after a change in action-2 rows (post-change stream of 3000 episodes), delay in episodes (censored at 3000), median over structures; price = exponent ratio

| training policy | training episodes | oracle detected | certified detected | frozen detected | median delay oracle | median delay certified | median certified/oracle delay | median predicted exponent ratio (oracle/certified) |
|---|---|---|---|---|---|---|---|---|
| narrow | 1000 | 480/480 | 107/480 | 480/480 | 25 | 3001 | 60.02 | 1649.02 |
| narrow | 10000 | 480/480 | 462/480 | 480/480 | 25 | 225 | 5.50 | 4.09 |
| uniform | 1000 | 480/480 | 479/480 | 480/480 | 25 | 125 | 2.92 | 2.40 |
| uniform | 10000 | 480/480 | 480/480 | 480/480 | 25 | 50 | 1.42 | 1.38 |

Spearman correlation between predicted exponent ratio and observed delay ratio (uniform training, 10000 episodes; 480 runs): 0.16

## D. Adversarial adaptive test policy (chooses contexts to maximise the numerator's advantage), 30 structures x 10 runs, alpha = delta = 0.05: rejections **0/300** (guarantee <= 0.10)
