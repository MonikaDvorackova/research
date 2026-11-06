---
id: topic-bostrom-world-models-phase10-gates
title: "Confirmatory E6′ design proposal (NOT executed) and decision gates G1–G8"
topic: bostrom-world-models
type: note
status: proposal
created: 2026-11-04
tags: [E6prime, design, gates]
---

# Proposed confirmatory E6′ (v2; for review only — not frozen, not authorised)
**Question.** For learned observers with a *certified* null, does the exact price formula predict detection behaviour, and how do uncertified optimisers and assumption-free predictive tests behave across independent structures?
| ID | Hypothesis | Falsified if | Units |
|---|---|---|---|
| H1 | The median delay inflation of the certified procedure relative to the oracle equals the exact exponent ratio within ±30 % in each of four coverage × size conditions | the median ratio (observed/predicted) lies outside [0.7, 1.3] with a cluster-level 95 % interval excluding it | ≥ 130 structures (±10 %) |
| H2 | Type-I of an EM-denominator e-process (good fixed alternative) increases monotonically with (optimisation shortfall − alternative deficit); symmetric ≥ 5 × 300 optimisers show no violation | flat dose–response; or any violation at ≥ 5 × 300, tolerance 10⁻⁶ | ≥ 60 structures × 3 data sets |
| H3 | The predictable-range comparison test detects hidden-state change in ≥ 1.5× the proportion of structures detected by the restricted-kernel test (paired by structure) | ratio < 1.5 (lower cluster bound) or the null-true cells reject above α | ≥ 93 structures, paired |
| H4 | Evidence overhead grows linearly with the number of null cells | non-linear (adjacent-K ratios outside ×2 of linear) | ≥ 3 K values × 12 runs |
Primary outcomes and units: structure-level quantities; detection probability separate from delay; censored delays treated as censored; nested runs averaged within structure. Positive controls: engineered changes with exact exponents; negative controls: unchanged kernel, zero-reach context change, bisimilar twin. **No equivalence claims.** Type-I checks at the nominal 0.05 (+ δ for the certified procedure), cluster-aware bounds, no relaxed threshold.
**Honest value assessment.** H1, H2, H4 test predictions that follow from Props T1–T5 and from the mechanism of `05-…`; a positive result adds measured constants and regimes; a negative result would most likely indicate an implementation or a numerical issue. H3 is the one empirical comparison with a nontrivial outcome. None addresses neural or latent world models.

# Gates
| Gate | Assessment | Evidence |
|---|---|---|
| **G1 mathematical validity** | **Passed** for the procedures that would be run: certified categorical test (proof; exact coverage 0.125 ≤ 0.3; exact E[E] ≤ 0.23; 0/7200; adversary 0/300), predictive-comparison test (Choe–Ramdas Thm 1 + predictable-range derivation; MC 0/300), episode-level test (Prop A). **Not passed, by exclusion:** EM/latent denominators (no certificate; excluded from any validity claim). Caveat: proofs not externally checked | `03`, `04` |
| **G2 literature and novelty adequacy** | **Not passed.** Chernoff 1959 not accessible; Safe Testing, Podkopaev–Ramdas (beyond abstract), Henzi–Ziegel, Naghshvar–Javidi, minimax-testing literature not read in full; no systematic review. **Passes for the narrower claim** "no component is claimed to be new" | `01`, `09` |
| **G3 independent environment diversity** | **Passed with limits**: 60 Markov and 40 small-HMM independent structures, 5 families implemented; A = O = 3, T = 4; ≈ 50× the structural spread of the single jittered template | `06` |
| **G4 statistical design adequacy** | **Passed as a design proposal** (ICC measured 0.37–1.0 for power/detection; coverage audited; structure counts 21–156 per claim); **not passed** for any claim requiring a demonstrated type-I ≤ 0.05 for a non-conservative procedure (undefined ICC; undercoverage near the boundary) | `08` |
| **G5 reproducibility** | **Passed**: namespace/streams, registries, determinism (9 re-executed jobs), tests | `06`, `07` |
| **G6 positive/negative control validity** | **Passed with caveats**: engineered exponents, zero-reach and coverage controls, bisimilar twin, K-scaling with known KL; oracle delays are floored at the 25-episode checkpoint; type-I controls cannot separate validity from conservatism | `07` |
| **G7 scientific value** | **Failed for the confirmatory E6′ as designed** (outcomes largely fixed by theory; no neural/latent coverage); a re-scoped programme on certified/bounded latent nulls (PO-13) would pass | `09`, `10` |
| **G8 feasibility of confirmatory execution** | **Computationally feasible** for the count-table designs (minutes–hours, CPU); **infeasible in a meaningful form** for latent/neural nulls without a certification method | `07` |
# Decision
**NO-GO for confirmatory E6′ as designed. Not authorised and not recommended.** (REVISE: re-scope around the unresolved certification problem for latent nulls.) Nothing was run in confirmatory namespaces (700–719, 800–829).
**Next phase priority: mathematical theory first** — a bounded attempt at a certified (or conservatively bounded) upper bound on the null-likelihood supremum for small latent nulls (PO-13) with explicit accounting of its detection cost, then a small *development* experiment on it; only if that yields a usable procedure should a confirmatory design be reconsidered.
