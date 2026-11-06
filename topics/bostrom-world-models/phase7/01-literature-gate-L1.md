---
id: topic-bostrom-world-models-phase7-L1
title: "Literature gate L1: is X1 a known application?"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-03
tags: [literature, gate, X1]
---

# Literature gate L1

## Access and reading levels (honest)
The fetch tool could not decode the three PDFs, so I saved them locally and extracted text with `pdftotext`. I then read the passages named below **myself from the extracted text**. This is partial full-text reading, not complete reading, and it is stated per source. Items not listed here were **not** read in Phase 7.

| Source | Access | What I actually read |
|---|---|---|
| Wasserman, Ramdas, Balakrishnan, "Universal inference", PNAS 117(29):16880–16890 (2020); arXiv 1912.11436 | arXiv PDF → text | Section 2 (split LRT definition, Theorem 1), Section 8 (running-MLE sequential LRT, Theorem 9, Ville argument, Theorems 10–11). Appendix proofs and the other sections **not read**. |
| Gelman and Shalizi, "Philosophy and the practice of Bayesian statistics", BJMSP 66(1):8–38 (2013); arXiv 1006.3868 | arXiv PDF → text | Abstract, introduction passages on hypothetico-deduction/error probes, Section 4 (model checking, 4.1–4.2) by keyword-located passages (lines around "error probes", "falsif", "model checking"). Sections 5–6 (induction; Popper/Kuhn) **not read**. |
| Catanach and Das, "Metrics for Bayesian Optimal Experiment Design under Model Misspecification", arXiv 2304.07949 | arXiv PDF → text | Abstract, introduction, definitions of EGIG and EDI (eq. 41, 43–44 region), conclusions. Examples (spring-mass-damper, F-16) skimmed only. |
| Wolpert, Locatello et al., Hyvärinen–Pajunen, Khemakhem et al., Barlas et al., Tang et al., Zhang et al., Baisero–Amato, Freeman et al. | Phase 6 search descriptions only | **Not read** in Phase 7. Their conclusions stay at search-description level. |
| Sequential testing, Wald (1945/1947), Ville (1939), formal learning theory (Gold; Schulte SEP summary in Phase 3) | — | Wald and Ville seen only through the universal-inference paper's citations. Learning theory: Phase 3 SEP summary only. Not read in Phase 7. |

## Findings relevant to X1

**1. The test is a known construction; the adaptive extension is not stated there.**
- Universal inference defines the split likelihood-ratio statistic T_n(θ) = L₀(θ̂₁)/L₀(θ) with θ̂₁ any estimator from independent data (Theorem 1), valid in finite samples with no regularity conditions.
- Section 8 gives a sequential version: "the running MLE LRT", M_t = ∏ p_{θ̂_{1,i-1}}(Y_i) / ∏ p_{θ̂_{0,t}}(Y_i), where θ̂_{0,t} is the **null MLE** and θ̂_{1,i-1} is a **non-anticipating** estimator. Theorem 9 states type-I error ≤ α for **i.i.d.** data. The proof uses Ville's inequality on the nonnegative martingale L_t = ∏ p_{θ̂_{i-1}}(Y_i)/p_{θ*}(Y_i), with M_t ≤ L_t under the null because the null MLE maximises the denominator.
- X1's statistic E_t = [K⁻¹ Σ_k p_k(D_t)] / max_{m∈M} p_m(D_t) has this form with a **Bayes-mixture alternative** in place of the plug-in estimator. The paper's construction is stated for i.i.d. observations; X1's data are adaptively collected, non-i.i.d. (hidden-state) interaction histories. The same martingale argument applies, but I had to **prove it for that setting** (see D1); citing Theorem 9 does not suffice.

**2. The design criterion is known.**
Catanach and Das define the Expected Discriminatory Information (eq. 41) EDI(d, M, M*) = D_KL[p(Y|d, M*) ‖ p(Y|d, M)], "to quantify how well an experiment can identify modeling failures," and state that the framework yields "experiments that would detect modeling failures." P4 in X1 (Jensen–Shannon divergence between the class-posterior-predictive and the wide-family posterior-predictive) is a **close relative of EDI with a posterior-predictive mixture playing the role of the alternative M\***. Their examples are linear-Gaussian dynamical systems with designs of a few continuous parameters; I did not find (in the parts read) sequential/closed-loop design for discrete hidden-state systems or a power analysis. Not the same setting, but the **idea of choosing experiments to expose model failure is not new**.

**3. The conceptual framing is known.**
Gelman and Shalizi argue that model checking and revision "fall outside the scope of Bayesian confirmation" (abstract) and that checking is hypothetico-deductive: "model checking can be understood as 'error probes' in Mayo's sense" (introduction), with falsification the logic of checking. They locate this in posterior predictive checks (Section 4). In the passages I read, they do not treat *which experiments to choose* in order to check a model. (Their bibliography cites optimal-design literature near Section 4; I did not read how it is used.) The distinction "updating vs criticism" is theirs.

**4. Open on my side.** I did not find, in what I read, (a) an exact finite hidden-state study showing that **power of class-inadequacy tests is governed by whether the alternative family contains something closer to the truth than the class** (margin KL(truth‖class) − KL(truth‖class∪alternatives), minus mixture regret), (b) a comparison showing that **member-identity EIG can be slower than random** at exposing inadequacy while class-level design is faster. Both are elementary consequences of known theory (Wald-type rates; EIG optimality relative to a target variable). Absence in what I read is not evidence of absence in the literature.

## Gate decision
**L1: PASSED with a downgrade of ambition.** X1 *as a method* is a known application of universal inference (test) plus EDI-style design (criterion). Passing means only that no read source already contains X1's specific *empirical question in the exact discrete setting*; it does **not** establish novelty. What would be needed to make the work original (any one):
1. A **theorem** (not only an application) characterising the detectable set of a class-inadequacy test under adaptive design: power iff margin·N > regret + ln(1/α), with exact minimax statements over adaptive policies; and a proof that member-identity EIG can be arbitrarily worse than random for criticism (a P10-type construction). Currently only the heuristic/rate version exists.
2. A **test with an unspecified alternative** (no pre-declared W) that retains power for unanticipated deviations at a quantifiable price — the real open problem; the present X1 shows the price is paid in regret.
3. A demonstration beyond the toy (learned world models), which Phase 5 learned that coverage can undermine.

## Updated novelty threats
N9 (Gelman–Shalizi): concept, **High**, now partly read. N10 (universal inference): test, **High**, now partly read; adaptive/hidden-state extension is ours but elementary. N13 (new): Catanach–Das EDI = criticism-oriented design criterion, **High** for P4 as an idea, Medium for its discrete hidden-state sequential use.
