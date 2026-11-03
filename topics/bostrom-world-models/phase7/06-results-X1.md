---
id: topic-bostrom-world-models-phase7-results
title: "X1 confirmatory results, statistical analysis and interpretation"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [results, X1]
---

# X1 results

Source: `results/x1_confirm/analysis.md` (frozen primary analysis, unmodified), `results/x1_confirm/supplementary_exploratory.md` (exploratory), `results/x1_audit/independent_audit.txt`. **Units:** 30 independent environment instances (seeds); within a seed, 20 runs per cell share the POMDP, the class and W. Binomial intervals pooled over runs treat runs as independent; seed-cluster intervals are given alongside (S1). Efficiency ratios use the seed as the unit. RMST = restricted mean episodes to rejection, censored at N = 3000; ratio > 1 means the second-named policy is faster.

## Primary preregistered outcomes
| Hypothesis | Result | Decision |
|---|---|---|
| **H1** validity | pooled null rejection 244/14 400 = **1.69 %**; every one of 24 cells' 95 % CP upper bound ≤ 0.044 (≤ 0.07 required); seed-cluster 95 % interval for the overall rate [1.5 %, 1.9 %]; worst policy P5 2.1 % [1.5 %, 2.8 %]; worst seed 6.2 % (80 runs) | **supported** |
| **H2** barrier | under P0, t05 6/600, t10 5/600, pc2 7/600 (UB ≤ 0.022) | **supported** |
| **H3** power | P2 rejection within 1500 episodes: pc0 1.000, pc1 1.000, pc2 1.000 (≥ 0.8) | **supported** |
| **H4a** P4 vs P2, anticipated | pc0 2.01 [1.86, 2.18]; pc1 1.74 [1.59, 1.91]; pc2 1.85 [1.71, 1.99] — all lower bounds ≥ 1.5 | **supported** |
| **H4b** P4 vs P2, unanticipated | t05 1.24 [1.13, 1.36]; t10 1.02 [0.86, 1.22] | **contradicted** (threshold 1.5 not reached) |
| **H4c** fair comparison P5 vs P4 (same information), anticipated | pc0 1.13 [1.02, 1.25]; pc1 0.87 [0.77, 0.98]; pc2 0.88 [0.82, 0.93] | **contradicted** — no ≥ 1.5× advantage for the criticism target; P5 is nominally faster on 2 of 3 |
| **H5** P3 (within-class EIG on M) vs P2 | pc0 1.44 [1.19, 1.74] (P3 faster); pc1 0.13 [0.11, 0.16]; pc2 0.17 [0.14, 0.22] (P3 6–8× **slower**) | **inconclusive by the preregistered rule** (the pc0 interval straddles 1.5); the heterogeneity is reported as found |

**Outcome class (preregistered): "informative failure".** H1–H3 and H4a hold, H4c does not: *the apparent advantage of criticism-oriented design over random intervention is explained by access to the alternative family, not by the criticism target.* The 1.5× threshold was not changed.

## Detection probabilities, times and censoring (S2, exploratory but descriptive of the same data)
Detection probability within 3000 episodes [seed-cluster 95 %]:

| truth | P0 | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|---|
| pc0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| pc1 | 1.000 | 1.000 | 1.000 | **0.318** [0.19, 0.46] | 1.000 | 1.000 |
| pc2 | 0.012 | 0.558 [0.48, 0.63] | 1.000 | 0.805 [0.71, 0.90] | 1.000 | 1.000 |
| t10 | 0.008 | 0.083 | **0.943** [0.90, 0.98] | 0.222 [0.13, 0.33] | 0.830 [0.74, 0.91] | 0.733 [0.62, 0.83] |
| t05 | 0.010 | 0.048 | 0.412 [0.33, 0.49] | 0.047 | 0.550 [0.43, 0.67] | 0.352 [0.24, 0.48] |

Median episodes to rejection (">N" = more than half the runs censored): pc0 P2 246, P4 110, P5 131, P3 157; pc1 P2 258, P4 141, P5 132, P3 >N; pc2 P2 194, P4 98, P5 92, P3 1254; t10 P2 760, P4 609, P5 888, P3 >N; t05 >N for all but P4 (2442). Full quantile tables, censoring rates and conditional means are in S2; conditional means are biased low when detection is rare and are not used for comparisons.

**Probability vs time.** For anticipated truths all non-pathological policies detect with probability 1 within budget, so differences are differences in time. For unanticipated truths differences are in both probability and time, and the ranking changes: on t10 random P2 has the **highest** detection probability (0.943 vs 0.830 P4, 0.733 P5); on t05 P4 is highest (0.55) but censored in 45 % of runs.

## Dependence on budget (S3, exploratory)
P2/P4 on anticipated truths rises with the cap and saturates: pc0 1.60 → 1.90 → 2.01 (caps 250, 500, 1000); pc1 1.43 → 1.65 → 1.73 (at cap 250 the lower bound 1.33 is **below** 1.5); pc2 1.60 → 1.82 → 1.84. At the shortest cap (250) the point estimates exceed 1.5 only for pc0 and pc2 (lower bounds 1.50 and 1.50), not for pc1. P5/P4 stays within 0.87–1.13 at every cap.

## Exact rate versus observed (S5, exploratory)
Predicted episodes ≈ ln(K/α)/(d_M − d_A) with the exact margin at q = 1/3: pc0 306, pc1 314, pc2 255, t10 1089, t05 9874; observed medians under P2: 246, 258, 193, 760, >3000. The formula is a rough guide that over-predicts by 20–30 % on the detectable cases (fluctuations make the crossing earlier than the mean-rate crossing); the **order of magnitude and the ranking are right**, and t05 is correctly predicted to be effectively undetectable within the budget.

## Computational cost
Summed run-seconds over all 6000 runs per policy (30 seeds × 10 truths × 20 runs): P0 1572, P1 1702, P2 1232, P3 3951, P4 3265, P5 3180. P3's total is the largest because it rarely rejects and so runs longer; per step it is cheaper (K = 4 vs 46). Per-step cost was not separately measured.

## Answers to the central question (Part 5), with evidence
1. **Can the embedded agent detect that its class is inadequate?** Yes, in this benchmark, with a test whose type-I error is controlled (1.7 % observed, ≤ 5 % guaranteed), *when* (a) the deviation changes the interaction kernel on actions it actually takes (H2: exactly nothing is detectable otherwise), (b) its alternative family contains something closer to the truth than its class by a margin large enough relative to the mixture regret (H3 and S5), and (c) the budget suffices. Without (b) the test has no power by construction.
2. **Without privileged access to the true environment?** No truth information is given to any policy or test. But the alternative family W is itself prior structure; for anticipated truths W *contains* the truth, which is a strong form of prior knowledge. For unanticipated truths power is limited and graded by the margin (t10 0.94 under random; t05 0.41).
3. **Does model-criticism design outperform ordinary information-gain design?** Against *random* intervention: yes for anticipated deviations (≈ 1.7–2.0×), no for unanticipated (≈ 1.0–1.2×). Against information-gain design **with the same information (P5)**: no — 0.87–1.13 on anticipated; on unanticipated P4 is 1.18–1.29× faster than P5 (t10 lower bound 1.07), below the threshold and exploratory in this role.
4. **Within-class information gain worse than random?** Yes, strongly, for P3 on pc1 (7.7× slower), pc2 (5.9×), t10 (2.9×) and t05 (1.2×); but not on pc0 (1.44× faster). Consistent with Proposition 10: member discrimination within M (members differ only in emission noise) is blind to the action that exposes the deviation.
5. **1.5× threshold:** met by H4a only; not met by H4b or H4c.
6. **Generalisation across environments:** not tested. One environment family, one set of hand-built classes.
7. **Anticipated vs unanticipated dependence:** large (see 1–3).

## Strongest negative finding
Under a fair information comparison, *criticism-oriented design offers no ≥ 1.5× advantage over identity-oriented information gain when the truth lies inside the alternative family*; the headline advantage over random intervention is explained by access to W. Also: for unanticipated deviations nothing designed here beats random intervention by 1.5×, and random is best on t10 in detection probability.

## Strongest positive finding
The sequential class-adequacy test is valid under adaptive intervention (proof + exact enumeration + 1.7 % observed), and its power is predicted, to within about 30 %, by an exact margin computation; the barrier (no action 2 ⇒ no detection) holds to the level of the type-I error; and information-gain design aimed only at identifying members of a class can be **6–8× slower than random** at exposing inadequacy.

## What this does not show
No claim about learned world models (all likelihoods are exact); no claim about simulation or the physical world; detection of class inadequacy is not identification of a better mechanism (no mechanism was identified in this experiment, only rejection of the stationary class M).
