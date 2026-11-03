---
id: topic-bostrom-world-models-phase8-portfolio
title: "Experimental portfolio E1–E6, gate outcomes, prioritised next experiment, statistical analysis plan"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [experiments, portfolio, SAP]
---

# Portfolio and prioritisation

Gate F asked of each candidate: *would either outcome advance the question?* Experiments whose result the theory already fixes are not run.

| ID | Question | Theory already fixes the answer? | Gate F | Decision |
|---|---|---|---|---|
| E1 | Learning (A) vs misspecification (B): do learning trajectories separate with data? | Largely: plateau ≈ H + δ, crossover n\* ≈ (d_rich − d)/(2δ); D3 gives one exact instance | The open part is transfer to a learned HMM/GRU where d is not countable | **Second priority** (after E6) |
| E2 | Shift vs mechanism change with matched degradation | **Yes**: exact obstruction (T4); distinguishing premises are assumptions, not findings | Fails: a result cannot change the conclusion | **Not run**; obstruction documented |
| E3 | Prediction–identification dissociation | **Yes** for the Bayesian instance (T5 exact) | A neural version has no well-defined "mechanism posterior" | **Not run**; revisit only with X2 |
| E4 | Unknown alternatives | Done in X1 (comparator needed) | Subsumed by E6 | **Folded into E6** |
| E5 | Intervention coverage | Done (X1 H2, S2/S3) | Subsumed | **Folded into E6** |
| E6 | Do the sequential guarantees survive learned/estimated likelihoods, misspecification, and persistence? | **No**: only proved for in-class; counterexamples exist; the *map* is unknown | Both outcomes informative | **First experiment** |

## Candidate experiment E6 ("validity map") — full specification (15 fields)
1. **Question.** For which (observer class, environment, policy, reset structure) do the two sequential procedures — the stationarity e-process E_stat (T4′) and the frozen-learned-null test E_frozen (T6a) — keep type-I ≤ α, and how do detection power and time depend on coverage and class capacity?
2. **Formal hypotheses (to be frozen before confirmatory data).**
   - H1: E_stat has type-I ≤ α when the truth is a stationary categorical kernel in the observer's context class, for open-loop and predictable policies including policy shifts.
   - H2: E_frozen has false-alarm probability → 1 as test length → ∞ under an unchanged kernel; the onset time grows at least proportionally to n_train.
   - H3: E_stat keeps type-I ≤ α for hidden-state truths when each episode redraws the latent state (resets).
   - H4: E_stat has type-I > α for a stationary hidden-regime process whose dwell time exceeds the checkpoint span; false-alarm probability increases with dwell/span.
   - H5: a mechanism change not representable in the observer's class (S6-type) is undetected by order-1 E_stat, and detected by an order-3 comparator class with ≥ 80 % power at N = 3000.
3. **Null/alternative.** H1, H3: null true → rejection ≤ 0.07 (upper 95 % cluster-aware bound). H2, H4: the *invalidity* alternatives; the null is "rejection ≤ 0.07".
4. **Ground truth.** Random observed-state Markov chains (F_M, ≥ 30 independent draws of the transition tensor), random hidden-state POMDPs from a generator with independent structure per instance (F_H, ≥ 30; not jitters of one structure), and hidden-regime processes F_R at dwell times {10, 50, 250, 1250} steps.
5. **Observer information.** (a, o) only, no labels, no kernel. Variants: context observed (V-c), reset with regime redraw (V-r).
6. **Interventions.** Open-loop random policies with p(a=2) ∈ {0.02, 1/3}; a policy shift mid-run; a predictable closed-loop policy (action depends on the previous observation).
7. **Primary outcomes.** Rejection probability within N episodes (detection probability) by cell; time to rejection reported separately with censoring; onset time vs n_train.
8. **Negative controls.** Stationary in-class nulls; the policy-shift-only case; split-state bisimilar variants; no-discriminating-action runs.
9. **Positive controls.** Kernel change with coverage (S2); a mechanism change representable in the class.
10. **Minimum meaningful effect.** Type-I violation: upper bound > 0.07 in any pre-specified cell. Invalidity claims (H2, H4) require ≥ 0.50 false-alarm probability at the pre-specified N. Power claims: ≥ 0.80.
11. **Power considerations.** Resolution of cluster-aware CP bounds with 30 instances × 20 runs: ≈ ±0.02 around 0.02; the effects of interest (≥ 0.5 vs ≤ 0.07) are far larger; the number of independent units is the number of environment *instances*, not runs.
12. **Failure conditions.** H1/H3 fail if any cell exceeds 0.07 (an additional counterexample, itself informative). H2 fails if onset time does not increase with n_train or if false alarms stay ≤ 0.07 at 10× the predicted onset. H4 fails if no false alarms at long dwell. H5 fails if order-1 detects or order-3 does not.
13. **Cost.** CPU only; Phase 8 diagnostics took minutes. The full design (≈ 90 instances × ~20 cells × 20 runs × N = 3000) is a few CPU-hours with 11 workers.
14. **Confounds.** Estimation of d for H2; context-grid coarseness; checkpoint step; stream length; the policy affects visited contexts; hidden-state generator coverage; Python/numpy version (recorded).
15. **Closest prior work.** Universal inference (Wasserman et al.); e-detectors (Shin–Ramdas–Rinaldo); hidden-mode MDPs; covariate-shift OOD detection; Catanach–Das. Most elements are known; the product is a validity *map* for embedded learned observers, not a new method.

## Candidate E1 (second priority) — abbreviated
Question: do learning-trajectory comparisons separate A from B for a learned HMM/GRU null as well as for count learners? H: the comparator gap changes sign near n\* ≈ (d_rich − d)/(2δ) with d estimated as effective parameters. Falsified if the sign change is unrelated to n\* (e.g. off by > ×3). Controls: well-specified Markov truth (gap never positive), hidden truth; learners O1–O4. Prior work: model selection theory. Run only after E6.

## Statistical analysis plan (applies to any confirmatory E6)
- **Units.** Environment instance (independently generated structure). Runs are replicates nested within instances; report the intraclass correlation and design effect for every binomial rate; if design effect > 1.2, use cluster bootstrap over instances as the primary interval, not Clopper–Pearson on pooled runs.
- **Detection vs time.** Report detection probability within each budget (primary) and restricted mean time with censoring (secondary); never report a mean time conditional on detection as a primary effect.
- **Type-I rule.** A cell passes if the cluster-aware 95 % upper bound ≤ 0.07; pooled over cells only as descriptive. Any single violation is reported as a counterexample.
- **Trend (H2, H4).** Spearman correlation plus log–log regression of onset time on n_train (H2) and logistic regression of rejection on log(dwell/span) with cluster-robust SE (H4); pre-specified slope thresholds (H2: slope CI lower bound ≥ 0.5; H4: odds ratio CI excludes 1).
- **Multiplicity.** Hypotheses H1–H5 are separate claims reported individually; secondary contrasts are Holm-adjusted; no composite "success" criterion is used.
- **Seeds/splits.** Development instances (e.g. 700–709) for implementation checks only; confirmatory instances (e.g. 800–829) frozen with the preregistration; analysis code committed with it; no change after outcomes exist.
- **Sample size justification.** 30 instances give a 95 % cluster interval half-width ≈ 0.02–0.03 on rates near 0.02 and ≈ 0.1 on rates near 0.5; effects under test are ≥ 0.5.
- **Integrity.** Hash manifest of raw runs before analysis; exact commit of the preregistration recorded before the run starts; the run is executed once.

## Prioritised next experiment
**E6.** It is the only candidate whose both outcomes change what we may claim about *embedded learned* observers. Recommendation: **GO** to freeze a preregistration after (a) external or independent-agent design review of this section, (b) a development run (instances 700–709) that checks H1–H5 machinery without tuning thresholds, (c) your approval.
