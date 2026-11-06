---
id: topic-bostrom-world-models-phase10-literature
title: "Phase 10 literature verification report and novelty assessment"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-04
tags: [literature, verification, novelty]
---

# Literature verification (Phase 10)

Method: arXiv PDFs downloaded with `curl` into an isolated scratch directory, converted with `pdftotext`, passages read directly. Levels: **TH** theorem/section read; **AB** abstract and first page only; **SD** search-result description only; **NA** not accessed. Searches 2026-11-04 (web search, standard mode). **No systematic review was performed.**

| Source | Identification (as printed in the file) | Level | Statements actually verified |
|---|---|---|---|
| Choe, Ramdas, "Comparing Sequential Forecasters" | arXiv 2110.00115v6 (9 Nov 2023) | **TH** | Game 1 (forecasters; Reality may be adaptive; no distributional assumptions); **Thm 1**: if δ̂_i is c-sub-Gaussian conditionally on G_{i−1}, Δ̂_t ± u(t)/t is a (1−α)-CS for the time-varying mean difference Δ_t; **Thm 2** (empirical-Bernstein CS): |δ̂_i| ≤ 2c, V̂_t = Σ(δ̂_i − γ_i)², γ_i predictable; weak null (average) vs strong null discussed; stitching boundary (their eq. 53) and conjugate-mixture boundaries. Theorem 3 (e-process) statement not read. |
| Howard, Ramdas, McAuliffe, Sekhon, "Time-uniform, nonparametric, nonasymptotic confidence sequences" | arXiv 1810.08240 | **TH** | Lemma 1 (linear boundary), §3.1 stitched boundary S_α(v) = √(k₁² v ℓ(v) + k₂² c² ℓ²(v)) + k₂ c ℓ(v), ℓ(v) = log h(log_η(v/m)) + log(l₀/α), k₁ = (η^{1/4}+η^{-1/4})/√2; eq. (11): for 1-sub-Gaussian zero-mean increments P(∃t: S_t ≥ 1.7√(t(log log 2t + 0.72 log(5.2/α)))) ≤ α. Constants k₂ were cut off in the extracted text and **not verified**; I used none of these boundaries in code (my predictable-range boundary is the normal-mixture boundary of Robbins, derived in `04-…`). |
| Henzi, Ziegel, "Valid sequential inference on probability forecast performance" | arXiv 2103.08402v3 (1 Jul 2022); journal reference not verified from the file | **AB** | e-values for score differences of competing forecasts; finite-sample validity without assumptions on the data-generating process; optional stopping. |
| Naghshvar, Javidi, "Active sequential hypothesis testing" | Ann. Statist. 41(6):2703–2738 (2013), arXiv 1203.4626v4 | **AB** | DP-based lower bounds on optimal cost; two heuristic policies; asymptotic optimality "due to Chernoff". Theorem statements **not** read. |
| Chernoff (1959), "Sequential design of experiments" | – | **NA** (only cited by Naghshvar–Javidi) | – |
| Ruf, Larsson, Koolen, Ramdas, "A composite generalization of Ville's martingale theorem using e-processes" | arXiv 2203.04485v3 | **AB** | composite version of Ville's theorem; e-processes as the composite generalisation of nonnegative martingales. |
| Podkopaev, Ramdas, "Sequential predictive two-sample and independence testing" | arXiv 2305.00143v2 (19 Jul 2023) | **AB** | prediction-based betting tests with sequentially updated predictors; valid beyond i.i.d. data, including drift. |
| Grünwald, de Heide, Koolen, "Safe Testing" | arXiv 1906.07801; JRSS-B (2024) with discussion, per search descriptions | **SD** | GROW/GRO optimal e-values; composite nulls; reverse information projection. Exponent claims below rely on this and on the elementary proof in `03-…`, not on a reading. |
| Modak, "On robust hypothesis testing with respect to Hellinger distance"; Gül–Zoubir; related | arXiv 2510.16750; 1502.00647; 1804.05632 | **SD** | robust testing over Hellinger/f-divergence balls; fixed sample size minimax tests; no explicit sample-complexity lower bound for the sequential composite-null problem found in the descriptions. |
| Wasserman, Ramdas, Balakrishnan (arXiv 1912.11436) | PNAS 117(29):16880–16890 (2020) | **TH** (Phase 7/9) | split LRT; running-MLE sequential LRT (Thm 9, i.i.d.); Thms 10–11; "MLE obtained by EM, which we assume converges"; EM convergence "beyond the scope". |
| Emmenegger, Mutný, Krause (arXiv 2311.04402) | NeurIPS 2023 | **TH** (Phase 9) | Thm 1: R_t(θ⋆) supermartingale with adaptively chosen x_s, θ̂_s (F_{s−1}-measurable); C_t = {θ: R_t(θ) ≤ 1/α}; well-specified likelihood. |
| Shin, Ramdas, Rinaldo (arXiv 2203.03532) | – | **TH** (Phase 9) | pre-change class of laws over infinite sequences, not necessarily i.i.d.; Def 2.2 e-detector. |
| Allman, Matias, Rhodes (Ann. Statist. 37(6A), 2009; arXiv 0809.5032); Choi, Yeung, Zhang (NeurIPS 1999) | – | **TH** (Phase 9) | generic identifiability of HMMs up to label swapping (Thm 6); HM-MDP ⊂ POMDP. |
| Gelman, Shalizi (arXiv 1006.3868); Catanach, Das (arXiv 2304.07949) | – | **TH** (Phase 7) | model checking as error probes; EDI. |
| Berbee (1979), Yu (1994, Ann. Probab. 22(1):94–116) | blocking, β-mixing coupling | **SD** (Phase 9); **no access attempt in Phase 10** | not used for any statement. |
| Le Cam; Ingster–Suslina (minimax testing); Lai, Lai–Xing (change detection with unknown parameters); Rissanen redundancy; Krichevsky–Trofimov | – | **NA** (cited from memory only) | used only to label results "known" with `[memory]`. |
| Brogioli; Ikram et al. (full text); Edge; Norton; Weatherson | – | **NA** (inaccessible, not bypassed) | – |

## Novelty assessment per candidate contribution
(1) established? (2) immediate corollary? (3) closest prior result and its assumptions; (4) verdict; (5) what remains unresolved.
| # | Candidate | Closest prior result (assumptions) | Verdict |
|---|---|---|---|
| L1 | **Certified learned-null test:** LR confidence set from training data, supremum over it as denominator, α + δ guarantee | Emmenegger et al. Thm 1 (adaptive LR confidence sets, well-specified); Wasserman et al. §8; sequential two-sample tests with learned predictors (Podkopaev–Ramdas, AB) | **Immediate corollary** of Thm 1 + Ville; the categorical Lagrangian solver is routine. Not new. |
| L2 | **Price of validity as exponent loss** KL(P‖N) − …, including the information-projection exponent of the confidence set | Stein/Chernoff-type bounds `[memory]`; GROW/RIPr composite-null optimality (Safe Testing, SD) | Known in form; the exact categorical-context projection onto an LR set and its comparison with observed delays is an instance. |
| L3 | **Regret scaling with null breadth** (evidence ≈ 10 nats per cell) | KT/Rissanen redundancy; Lai–Xing `[memory]` | Known qualitatively; measured constant is an empirical instance. |
| L4 | **Predictive-comparison test with predictable conditional range** | Choe–Ramdas Thm 1 (c-sub-Gaussian conditionally), Thm 2 (variance-adaptive) | Elementary corollary (Hoeffding's lemma with a predictable range + Robbins mixture); I did not find this exact range-based variant in the text read (Thm 2 uses the empirical variance). Constant-level difference; not a contribution. |
| L5 | **Optimiser asymmetry makes EM-denominator e-processes invalid; inflation inversely related to the alternative's quality** | Wasserman et al. state EM convergence is assumed and out of scope; the proof needs a denominator ≥ true null likelihood | The mechanism is evident from the proof; the measured dose–response is a restricted-setting empirical characterisation (class B). |
| L6 | **Zero-reach / uncovered contexts make a change unobservable to every valid learned-null procedure** | Proposition 1′ (own); equivalence under restricted interventions (Castro et al.; Armstrong — abstracts) | Elementary; known in spirit. |
| L7 | **Persistent hidden regime ≡ random-time change** | Choi et al. (HM-MDP), exchangeability/non-ergodicity | Elementary; known. |
| L8 | **Coverage audits of cluster-level intervals (ICC, design effect)** | standard survey-statistics design effect `[memory]` | Methodology, not a result. |
**Net.** No new theorem. The only residue with some chance of being useful is (i) the exactly checkable *price formula and its coverage impossibility* for learned nulls (L1, L2, L6) and (ii) the optimiser-asymmetry dose–response (L5), both in restricted settings. Whether either is already in the literature is **not established** because Chernoff 1959, Safe Testing, Podkopaev–Ramdas beyond the abstract, and the minimax-testing literature were not read.
