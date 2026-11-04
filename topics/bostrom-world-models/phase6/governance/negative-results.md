---
id: topic-bostrom-world-models-negative-results
title: "Negative-results register"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance, negative]
---

# Negative results and failed hypotheses (preserved)
1. Original adaptive observer (Phase 4) fails to detect AltOOD/imitation: absorption by updating (P8c). Not evidence about real systems.
2. Active (EIG) design under learned likelihoods is not better than random wide intervention; worse in 11/12 seeds (env 1).
3. Conjecture "a catch-all makes myopic EIG explore" refuted by exact computation (Phase 5).
4. Corollary originally worded as an equality; false; corrected (Wald lower bound).
5. Information-gain-ratio diagnostic: env 1 only; no replication in env 2.
6. Equivalence claim E3b (env 1): not established in run A.
7. GRU first dev run too poor (v0 retained for the record).
8. Run A not bit-reproducible (hash() seeding); run B deterministic.
9. Phase 5 recorded access failures: Ikram et al. (OpenReview), Semantic Scholar 429, Springer, PhilSci certificate, PhilPapers/PhilArchive 403 — not bypassed.
10. Phase 6: the exact amplification (≈1/q) in the benchmark is Prop. 3, not a new result.
11. Phase 7: the Phase 6 X1 proposal was infeasible (saturated alternative) and confounded (P4 had W, P3 did not); revised before confirmation (D1).
12. Phase 7: my prediction that unanticipated deviations are undetectable was wrong (dev: t10 detected 70 %); replaced by the margin law.
13. Phase 7 confirmatory: **H4c contradicted** — under equal information, class-level targeting gives no ≥ 1.5× advantage (0.87–1.13 on anticipated truths). The apparent benefit over random is explained by access to W.
14. Phase 7 confirmatory: **H4b contradicted** — for unanticipated deviations P4 vs random 1.24 (t05), 1.02 (t10); random has the highest detection probability on t10.
15. Phase 7 confirmatory: H5 inconclusive by the preregistered rule because the effect is heterogeneous (P3 1.44× faster on pc0, 6–8× slower on pc1/pc2); rule not altered.
16. Phase 7: the test is conservative (1.7 % vs 5 %): validity holds but the e-process wastes power in the null-calibrated sense.
17. Phase 8: the absolute four-way partition (epistemic / misspecification / shift / mechanism change) fails Gate A: C and D are not functions of the observable law (absorption, exact check).
18. Phase 8: the stationarity e-process is **not robust** to persistent hidden regimes (40/40 false alarms, including a stationary start); my initial hypothesis that it was a transient artefact was wrong (control).
19. Phase 8: mechanism change not representable in the observer's class is invisible to its stationarity test (S6, 0/100).
20. Phase 8: E2 and E3 judged not worth running (theory fixes the answer).
21. Phase 9: Phase 8's T4/T6 "false alarm" language was a semantic error (out-of-class truths); T4′ "robustness" and T5 "decays with n" were over-claims (corrected).
22. Phase 9 dev: robust-valid procedures (episode-level saturated e-process; predictive-comparison confidence sequence) had **zero** rejections at N = 3000, including for a large kernel change.
23. Phase 9 dev: restricted-kernel stationarity e-process detected a hidden-state mechanism change in 5/30 runs only (misspecification masks change).
24. Phase 9 dev: policy shift + misspecification produced no false-attribution events in random instances (exact discrepancy ≤ 2.5×10⁻³ nats/observation).
25. Phase 9 audit: pooled run-level binomial bounds undercover under clustering; 20 runs per structure cannot certify a per-structure rate bound; even cluster intervals cover 0.85–0.93 at R = 20.
26. Phase 9: the E6 validity map as specified is mostly fixed by theory (G7 failed); re-scoped to E6′.
27. Phase 10: the certified test never rejected under the null (0/7200): calibration cannot be distinguished from conservatism; exact crossing probabilities at the enumerable horizon were 0.0000 (vacuous).
28. Phase 10: proof attempts that failed or were stopped: minimax delay lower bound with unknown pre-change law (two reductions); robust validity of restricted-kernel stationarity tests under mixing (disproved); "approximate EM preserves validity" (disproved); rate of 1 − ρ̄(n) (not attempted).
29. Phase 10: the confirmatory E6′ as designed would mostly confirm theory-predicted quantities and does not cover latent/neural nulls (G7 failed); not authorised.
30. Phase 10: K = 64, 128 cells not detected within 12 000 observations; the 10.4 nats/cell slope is measured only for K ≤ 32.
31. Phase 10: oracle delays are floored at the first checkpoint (25 episodes), compressing ratios; run-level correlation of predicted vs observed delay ratio is only 0.16.
32. Phase 11 closure: K-ratio claim for the type-class bound is false for constrained families (explicit counterexample); interval branch-and-bound is published (not new).
33. World-models pilot: first σ grid uninformative (passive agents at ceiling); random-amplitude probes worse than passive; an MLP world model's one-step probe cannot show the structural gap; the interface-limited equivalence pair stays at chance for every policy.
34. WM execution: first RSSM (no prior-predictive loss) autoencoded observation noise (excess prior NLL ≈ 390, coverage 7 %); results kept in `gwb_dev/…FIRST…` and `runs/failed_v1/`.
35. WM execution: ICI (instance-contrastive) discovery objective did not improve in-distribution structural accuracy (det −0.008…+0.007; RSSM ≤ +0.038, untested pairwise); learned-ensemble disagreement planner not significantly better than random blocks and far below a simple amplitude-sweep heuristic.
36. WM execution: prediction-trained probes make confident claims on 19–97 % of exactly equivalent worlds; exposure-trained abstention transfers only partially (15–40 % residual claims on an unseen equivalence family).
37. WM execution: untrained random recurrent nets read out mechanism class far above chance (0.66 under sweep); the end-to-end supervised GRU was not an upper bound; the two `ens_disagree[*_untrained]` rows are invalid (ensemble of one).
