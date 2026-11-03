---
id: topic-bostrom-world-models-claim-matrix
title: "Claim–evidence–assumption matrix"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [audit, claims]
---

## Claim–evidence–assumption matrix

Version 1 was written at the start of Phase 5, **before** any new experiment, from the stored Phase 1–4 material. Status classes: **Math** (mathematically established), **Emp** (empirically supported), **Expl** (exploratory), **Phil** (philosophically argued), **Unver** (unverified), **Contra** (contradicted). A claim is promoted only by new evidence recorded in a later version; the section "Version history" at the end lists every change.

### Reconstructed relationship between the six quantities

Fix an intervention policy π and horizon T. Let P_E^π denote the law of the interaction history.

1. **Environmental distinguishability** of a reference E₀ and a candidate E₁: D(π) = TV(P_{E₀}^π, P_{E₁}^π). It is a *ceiling*: no score computed from the history has AUROC above ½ + D(π) (Prop. 7a), and the best test has total error 1 − D(π) (Prop. 2a). It depends on the intervention class: kernels that agree where the observer probes give D = 0 there (Prop. 1).
2. **Observer misspecification** m(π) = TV(P_{E₀}^π, P_Q^π) for the observer's theory Q. A level-α test against Q rejects the true E₀ with probability at most α + m(π) (Prop. 6). The direction of a likelihood score is set by which environment is nearer the theory in cross-entropy (Prop. 7b).
3. **Intervention coverage** determines m(π): a theory estimated on interventions μ has small error under μ but unbounded error outside its support (Prop. 3b); under a bounded policy ratio c the error is bounded by powers of c (Prop. 3a).
4. **Model adaptation**: updating the theory on the environment under test drives P_{Q_n} toward P_E, so the residuals that carried the discrepancy vanish (Prop. 8c). Information then lives in the posterior over hypotheses, not in the residuals.
5. **Hypothesis identification** is relative to the observer's class M: with E ∈ M and distinguishability D > 0 the posterior identifies E at exponent KL; with E ∉ M it concentrates on the KL-closest member and is blind to deviations where all members agree (Props. 8, 10). Active design by expected information gain optimises *within* M (Prop. 10).
6. **Justified inference about simulation** adds premises that observation cannot supply (artifact, reference, bridge to Bostrom's assumptions): rungs 3–5 of the ladder in `philosophical-analysis.md`.

Composite: achievable detection ≤ ceiling set by (1) at the probed regime; realised detection = ceiling reduced or inverted by (2), (3); adaptation (4) trades false alarms against power; identification (5) is class-relative; (6) is not reachable from (1)–(5) alone.

### Matrix

| # | Claim | Status | Evidence | Assumptions that could invalidate it | Scope / caveat |
|---|---|---|---|---|---|
| F1 | Observational equivalence under all policies ⇔ equal kernels on reachable histories (Prop. 1) | Math | Proof; exact enumeration; randomised audit with unreachable histories | Finite A, O; policies are all history-dependent randomised policies; equality of *interventional* laws | Known in spirit; continuous spaces unverified (O1); relation to Armstrong/Castro unverified (O4) |
| F2 | Min total error = 1 − TV; TV ≤ √(KL/2); chain rule (Prop. 2) | Math | Standard theorems; exhaustive 2⁸-region check | Fixed π, T | Known |
| F3 | Coverage: bounded policy ratio ⇒ bounded KL; without it unbounded (Prop. 3) | Math | Proof; enumeration; audit incl. infinite KL | Occupancy ratio c^t; tightness unknown (O3) | Elementary |
| F4 | Evidence screens off only the kernel (Prop. 4) | Math | Tower property | Countable M; likelihood depends on m only via κ(m) | Elementary; close to Chalmers's defeat argument |
| F5 | One test outcome has bounded likelihood ratio (Prop. 5) | Math | TV definition; all-regions check | **Simple** hypothesis S = "E₁" against E₀; not the composite "some simulation" | Elementary |
| F6 | Misspecified null inflates false alarms (Prop. 6) | Math | Event bound; all-regions check | Test level α under Q; test data independent of any adaptation of Q | Elementary |
| F7 | AUROC ceiling ½ + TV; cross-entropy identity; inversion exists (Prop. 7) | Math | Proof; ties and exhaustive-ordering checks | Continuous-score argument via tie-breaking | Elementary; ½ + TV/2 is false (counterexample) |
| F8 | Finite-class posterior consistency / KL concentration; absorption (Prop. 8) | Math (finite classes) | SLLN proof; simulation | Finite class; i.i.d. episodes; sample splitting for (c) | Known (Berk; Doob–Schwartz); general classes unverified |
| F9 | Adaptivity: no KL gain for memoryless kernels; strict gain exists (Prop. 9) | Math | Exhaustive 2-step enumeration | KL and fixed-size tests for (a) | General characterisation of when adaptivity helps: Unver (O6) |
| F10 | Evidence needed to overturn prior odds ω: E[τ] ≥ ln ω / KL | Math | Wald identity; simulation | Independent episodes; E₀ true; simple S | Earlier wording "expected number = ln ω / KL" **Contra** (corrected) |
| F11 | EIG design is blind to deviations outside the members' disagreement set; can manufacture equivalence (Prop. 10a,b) | Math (finite example; (a) in general) | Exact DP over all outcome sequences | The specific kernel values in the example | Generality beyond the example: Unver |
| F12 | A catch-all class makes *myopic* EIG explore | Contra | Exact counterexample (EIG at the untried action is 0) | — | Refuted conjecture; non-myopic (2-step) EIG with catch-all succeeds (Math, finite example) |
| E1 | In-distribution-trained neural theories invert under out-of-distribution interventions (AUROC ≪ 0.5, FPR → 1) | Emp | 9 observer conditions, 10 seeds, paired statistics, oracle AUROC 1.0 | Fully observed 2-D Gaussian toy; χ² residual statistic; α = 0.05; W trained on 12,500 transitions; narrow range [−1,1] | One environment; not yet tested under partial observability or other statistics |
| E2 | The inversion does not depend on theory architecture, training sample, or W architecture | Emp (weak) | ReLU, independent sample, W ReLU/tanh grid: differences < practical threshold | Same environment and statistic | "No dependence" rests on non-significance; **no equivalence test yet** (Phase 5) |
| E3 | Exact or range-covering theories detect (AUROC ≥ 0.985, FPR ≈ 0.05) | Emp | Conditions B, C | Condition C hands the agent coverage; B hands it the law | Upper bounds, not realistic observers |
| E4 | A fine-tuning adaptive observer loses false alarms and power (chance) | Emp (one protocol) | `adaptive_tanh`, 10 seeds | Batch fine-tuning of a tanh ensemble; 1,000 adaptation transitions | Not a Bayesian observer; Prop. 8(a) says a class-complete Bayesian observer would differ: **untested** |
| E5 | The inversion is a cross-entropy-nearness effect | Expl (+ Math for 7b) | Mechanism check: 10/10 seeds each direction | Exploratory; −log Q score, not the χ² statistic | Direction only |
| E6 | In-distribution detection is limited by information, not by the theory | Emp | Exact theory AUROC 0.59 vs oracle 0.88 at passive T = 50 | Chi-square test vs composite alternative | Also reflects the composite alternative |
| E7 | The score tracks divergence size, not provenance (learned vs non-learned) | Expl | AltOOD post hoc; matching only in mean KL under uniform wide actions | Control matching on one summary | Cannot test mechanism identification |
| E8 | The equivalent negative control is not exploited | Emp (weak) | Seed-averaged AUROC 0.482–0.513 over all cells | Same | No equivalence test; margin not pre-specified (Phase 5) |
| E9 | Results reproduce | Emp (seed 0 only) | `reproduce_check`: 0 mismatches for seed 0 of 9 conditions | One machine and library version | Other seeds not re-run |
| E10 | No leakage or stream coupling | Emp | Tests and audit | Checks enumerated in the audit | Absence of detected issues, not a proof |
| P1 | T1–T3 (untestability of the unrestricted hypothesis; refutation only of fidelity-indexed ones; insulation of Bostrom) | Phil | Argument; Bostrom (full text), Chalmers (full text), formal learning theory (summaries) | — | **Established in the literature**: clarifications, not contributions |
| P2 | T4: anomaly detection is theory-relative; coverage matters | Phil + Emp | E1–E3 | Toy; interpretation of E1 | Duhem–Quine qualitatively; static-model inversion known; novelty of interventional instance Unver |
| P3 | T6: learning from the environment under test cannot supply the reference | Phil + Emp (E4) | Prop. 8c; E4 | One protocol; no Bayesian observer | Over-general until a Bayesian observer is tested |
| P4 | T7: discriminating evidence needed to defeat the indifference proviso ≈ ln ω / KL | Phil + Math | F10 | Simple S; independent episodes | Application possibly new; elementary |
| P5 | T5: testability of fidelity-indexed hypotheses is bounded by the observer's coverage | Phil | Interpretation of C, B conditions | — | **Unver** for physical regimes |
| P6 | The experiments say nothing about the physical universe or about Bostrom's trilemma | Phil (by construction) | Design | — | — |
| P7 | The contribution is novel relative to the literature | Unver | Partial: Bostrom, Chalmers read; others abstracts | Brogioli, Weatherson, Norton, Laudan–Leplin, Edge, *Reality+* unread | See novelty threat matrix (Phase 5) |

### Assumptions that could invalidate the current interpretation

1. **Single environment**: fully observed, Markov, Gaussian noise, smooth nonlinearity, 2-D state. Partial observability could create identifiability barriers that this environment cannot show (Phase 5, Part D).
2. **Single detector**: χ² of standardised residuals. A likelihood-ratio or Bayesian detector might behave differently (Phase 5, Part B).
3. **Learned world model is a Gaussian MLP**, not a latent-state model of the DreamerV3 type.
4. **The reference is stipulated non-simulated**, so the "reference premise" holds by construction.
5. **AltOOD and Ealt are matched on one divergence summary**; conclusions about provenance are limited accordingly.
6. **Ten seeds; no external pre-registration**; all Phase 1–4 analyses are partly exploratory because designs were refined after seeing results (the post hoc AltOOD control; the adaptive observer was specified after Phase 3 results).
7. **Non-significance is not equivalence**: E2 and E8 are stated without equivalence tests.
8. **Platt-based calibration metrics are experimenter-side** and meaningless for inverted scores.
9. **The adaptive observer is one protocol**, not "the" adaptive observer.

### Version history

- v1 (Phase 5 start): created.
- v2 (Phase 5 end): status changes and new claims below; no claim was promoted from exploratory to confirmatory without a pre-specified test.


## Version 2 (end of Phase 5)

### Status changes to v1 claims

| v1 id | Claim | v1 status | v2 status | Reason |
|---|---|---|---|---|
| F10 | E[τ] ≥ ln ω / KL (Bostrom corollary) | Math | Math | Unchanged after audit; the earlier wording was already marked Contra and corrected. |
| F11 | EIG design blind to deviations outside the members' disagreement set (Prop. 10a,b) | Math (finite example) | Math (finite example); **novelty threatened** | Catanach and Das and related BED-misspecification work (abstracts) cover the phenomenon; only the exact illustration is ours. |
| F12 | A catch-all makes myopic EIG explore | Contra | Contra | Unchanged; non-myopic design with a catch-all succeeds in the exact example (Math). |
| E2 | Inversion independent of architecture, sample, W architecture | Emp (weak) | **Emp (post hoc equivalence-tested; 12/12 contrasts within ±0.10 AUROC)** | Post hoc TOST, margins fixed beforehand; many cells at the AUROC floor, so equivalence partly reflects a shared floor. |
| E4 | Fine-tuning adaptive observer absorbs the anomaly | Emp (one protocol) | Emp (one protocol); **scope narrowed** | A Bayesian observer whose class contains the truth identifies it (oracle, both environments); one whose class is learned does not (D1, G2). Absorption is a property of the fine-tuning protocol, not of learning from the environment in general. |
| E8 | Equivalent control not exploited | Emp (weak) | **Emp**: environment 1 TOST 25/27 (post hoc); confirmatory E3a,c yes, E3b **not established**; environment 2 E1a–c yes | Equivalence now tested. |
| E9 | Reproducibility | Emp (seed 0 only) | Emp for Phase 1–4; **Phase 5 run A not bit-reproducible (defect found and fixed)**; run B deterministic | See corrections log #14. |
| P3 | T6: learning from the environment under test cannot supply the reference | Phil + Emp (one protocol) | Phil + Emp (scope narrowed as for E4) | Same. |
| P7 | Novelty | Unver | Unver; novelty threat matrix completed | Components anticipated; conjunction not found in the sources reached. |

### New claims

| # | Claim | Status | Evidence | Assumptions / scope |
|---|---|---|---|---|
| B1 | A Bayesian observer with learned likelihoods is far less accurate and far worse calibrated than the oracle under informative interventions, and mislabels the reference (environment 1) | **Emp (confirmatory, D1–D4, D7)** | 12 held-out seeds, pre-specified, Holm-adjusted | Gaussian toy; theories trained on a narrow range; one world-model architecture |
| B2 | The same holds in a partially observed POMDP with GRU learners (G2, G3) | **Emp (confirmatory)** | 12 held-out seeds | One POMDP family; GRU only |
| B3 | In the POMDP the correctly specified observer's accuracy rises with budget (finite-sample) while learned observers stay flat (G1, flat curves) | **Emp (confirmatory G1; flat curves exploratory)** | as above | 200-step horizon |
| B4 | Equivalence relative to an intervention class is exact: with no use of action 2 the transition-perturbed mechanism is unidentifiable by any observer; with action 2 the oracle identifies it (0.116 versus 0.705 versus 0.950) | **Math (exact) + Emp (confirmatory G7)** | exact enumeration; posterior odds unchanged to 0.00e+00 | Specific POMDP; exact kernels |
| B5 | Information-gain design helps a correctly specified observer (G4: +0.176) and does not help learned observers (G5: −0.025; environment 1 E1/E2 not established, EIG worse in 11/12 and 9/12 seeds) | **Emp (confirmatory G4, G5)**; env-1 reading **Expl** | | Myopic EIG in environment 1; two-step in environment 2 |
| B6 | The learned observer separates a learned world model from non-learned alternatives well in environment 1 (D6: 0.928) but not in the POMDP (G6: 0.569) | **Emp (confirmatory both)**; the contrast is a **robustness limit** | | Environment-specific |
| B7 | The failure of learned observers is coverage-dependent: training the observer's theories over the probed range removes it | **Expl** (stress seeds 400–405, n = 6) | acc3 0.983, ECE 0.011 | Environment 1 only |
| B8 | Incomplete hypothesis spaces yield confident misclassification even for an oracle | **Math (Props. 8b, 10a) + Expl (stress)** | ECE 0.33 for the oracle with a class absent | |
| B9 | Oracle observers are insensitive to misleading priors; learned observers are sensitive | **Expl** | stress | |
| B10 | The realised/expected information-gain ratio diagnoses misspecification | **Contra (not replicated)** | environment 1: 0.97 versus 5.0; environment 2: 0.94, 1.00, 0.97 | Exploratory finding withdrawn as a general claim |
| B11 | The inversion mechanism (the environment nearer the theory in cross-entropy looks normal) holds for Bayesian observers too | **Expl** | environment 1: H0 accuracy 0.31–0.37 for learned and bma; environment 2: H1-vs-H0 AUROC 0.44–0.49 | Direction only; no mechanism check for the Bayesian observers |
| B12 | The confirmatory conclusions hold in a bit-reproducible rerun | **Emp**: environment 1, 12 of 13 decisions identical (E3b differs: not claimed); environment 2, 11 of 11 identical; stress accuracies within 0.018 | `results/compare_runs_bayes*.md`; exact re-run of one seed per environment: 0 mismatching arrays | One machine; run B shares observer materials and truths with run A, so it replicates the interaction randomness and the code path, not the training randomness |
