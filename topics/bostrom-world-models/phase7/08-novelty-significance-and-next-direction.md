---
id: topic-bostrom-world-models-phase7-next
title: "Novelty and significance assessment; decision on the next research direction"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [novelty, decision, X1, X2, X3]
---

# Novelty, significance and the next direction

Classes: **A** known theoretical result reproduced experimentally; **B** new empirical observation in a restricted setting; **C** potentially generalisable phenomenon requiring further testing; **D** genuinely new formal result; **E** philosophical interpretation requiring extra premises. Reading limits: L1 (partial full-text reading of three sources; everything else search-description level). "Not found" is not "absent".

## Findings classified
| Finding | Class | Closest prior work | Precise difference | Residual threat |
|---|---|---|---|---|
| Anytime-valid, type-I-controlled test of "truth ∈ finite hidden-state class" under adaptive interventions (proof, exact enumeration, 1.7 % observed) | **A** | Wasserman–Ramdas–Balakrishnan (Thm 9, i.i.d., read) | Same martingale argument for conditional likelihoods with adaptively chosen actions in a POMDP; the extension is elementary and proved here (D1 §1) | High: not a new result |
| Zero detectability without the revealing action (barrier) | **A** | bisimulation/trace equivalence (Castro et al., Armstrong); our Prop. 1′ | Exact benchmark instance, validated by type-I-level rejection | High |
| Detection time follows the exact margin KL(truth‖M) − KL(truth‖M∪W) (S5) | **A** | Wald, Neyman–Pearson, Chernoff–Stein rates | Quantified in the benchmark; ±30 % | High |
| Detection of unanticipated deviations is possible but graded by the margin (t10 0.94, t05 0.41) | **B** | Laudan–Leplin relativity of empirical judgments; misspecification-detection literature (abstract level) | Quantified instance | Medium |
| Member-identity EIG over the class can be 6–8× slower than random at exposing inadequacy (pc1, pc2) | **A/B** | Our Prop. 10; Catanach–Das (EGIG/EDI: designs differ in robustness vs detection, read) | Exact discrete hidden-state instance with a measured factor | High (qualitatively anticipated by Catanach–Das' motivation and by P10) |
| Under equal information, class-level (criticism) targeting gives no ≥ 1.5× benefit over member-identity EIG when the truth is in the alternative family (H4c) | **B**, possibly **C** | Catanach–Das EDI = KL(p(Y|d,M\*)‖p(Y|d,M)) (read) | EDI presupposes a specified alternative M\*; when the alternative mixture contains the truth, discriminating "class vs alternative" and identifying the member coincide in effect; **not tested beyond this benchmark** | Medium: negative result in one setting |
| Class-level targeting is mildly (1.2–1.3×) faster than identity-EIG for unanticipated deviations | **B** (exploratory) | as above | Secondary, under threshold | Medium |
| Anticipated vs unanticipated deviation structure of inadequacy detection | **A + E** | Duhem–Quine, Laudan–Leplin, Gelman–Shalizi | Formalised through the margin | High |
| Detection of inadequacy bears on the mechanism or on simulation | **E** only | Chalmers, Bostrom | Not supported: M's rejection leaves "auxiliary assumptions vs class" undecided | – |
| A **D** (new formal result) | none | — | None established. A candidate (adaptive minimax statement for the margin law) is not proved | – |

**Updated novelty-threat matrix** (`literature/novelty-threat-matrix.md` Phase 7 additions): N10 (universal inference) partly read — adaptive extension is elementary; N13 (Catanach–Das EDI) is the closest design precedent; N14 (new): "criticism design equals EDI" — High. The component with the best remaining chance of being new is the **absence of an advantage of the criticism target under equal information**, and it is a negative result in one benchmark.

## Reassessing X1, X2, X3 (and a fourth direction)
Ranking criterion: potential to produce defensible *new* knowledge, not ease.

### X4 (proposed) — Learned-null class-adequacy testing for an embedded observer *(highest potential)*
- **Question.** When the null model must be *learned from the agent's own interaction* (no oracle member likelihoods), does a valid sequential test of class adequacy exist, and how much power does it retain relative to the exact oracle bound ln(1/α)/KL?
- **Existing evidence.** Phase 5: learned-likelihood observers are overconfident and invert; Phase 7: with exact likelihoods the test is valid and power is predictable. The gap between these two results is the genuinely embedded-agent question, and it answers the brief's item "does detection require information unavailable to an embedded observer?" (currently: yes — exact member likelihoods and the family W).
- **Strongest novelty threat.** Universal inference with estimated nulls (split LRT; Wasserman et al.), prequential/plug-in methods, misspecification tests for HMMs. Likely to be a known construction; the novelty would be the quantified power loss for interventional hidden-state learners and its dependence on coverage.
- **Discriminating next step.** Replace M by a parametric hidden-state family with unknown parameters (e.g. emission noise η ∈ [0, 0.4] continuous plus Dirichlet-parametrised transitions) fitted online; test statistic uses a predictable estimator in the alternative and the exact constrained maximiser in the denominator (valid by the same proof); compare with the exact oracle. Proof obligation: validity when the null class is a continuum (supremum over a compact family—holds by the same argument), and power law with the estimator's regret.
- **Falsifier.** Power loss so large that detection within feasible budgets never occurs for deviations the oracle detects; or invalidity (type-I > α) with a naive plug-in null (informative negative control).
- **Complexity.** CPU only; parametric family on a grid or by EM; hours.
- **Expected scientific value.** High relative to the others: it tests the claim that makes the project about *embedded* agents.

### X3 — Generalisation of learned-observer failure across learner families
- **Question.** Is the Phase 5 failure of learned-likelihood observers (overconfidence, inversion) a coverage property independent of the learner? Hypothesis H_cov.
- **Evidence.** Two environments, two learners; stress tests (exploratory). H_cov unresolved.
- **Novelty threat.** Likelihood inversion is known (Nalisnick, Ren); calibration/ensemble fixes exist. Value is in the controlled coverage axis, not the phenomenon.
- **Next experiment.** Count-based, GRU, transformer, ensemble, temperature-scaled learners × two environments, full-coverage control; ≥ 20 seeds, equivalence test for "no failure under full coverage".
- **Falsifier.** Failure persisting under full coverage for some learner family (H_cov false), or disappearance under mild calibration (then the failure is not fundamental).
- **Complexity.** GPU not required; hours to a day.
- **Value.** Medium: solid empirical generalisation of a known phenomenon; becomes important if combined with X4 (use X3's learners as the null in X4).

### X2 — Prediction–identification frontier
- **Question.** Is there a tight general bound on mechanism distance on a policy class Π′ given predictive distance on Π, beyond the per-step coverage amplification (Prop. 3)?
- **Evidence.** Phase 6 exact diagnostic: amplification ≈ 1/q on the benchmark. Phase 7: the margin law is the same quantity seen from the test's side.
- **Novelty threat.** Data-processing inequality; coverage/concentrability in offline RL (unread). High probability the tight statement is a corollary.
- **Next step.** A bounded proof attempt plus exact random-family computation; stop if the frontier equals Prop. 3.
- **Falsifier.** Frontier never approached, or equal to Prop. 3.
- **Complexity.** Light.
- **Value.** Low-to-medium; cheap to settle, good as a clarifying remark. Do not run as a major thread.

### X1 — Class-inadequacy detection (continuation)
- **Status.** The preregistered design-benefit hypothesis is falsified under the fair comparison (H4c). The validity/power/anticipation characterisation is complete in this benchmark. Remaining unresolved question *within* X1: sensitivity of conclusions to the size/geometry of W and to unanticipated truths (A10) — absorbed by X4.
- **Decision.** Do not continue X1 as a separate line.

## Ranking by potential for defensible new knowledge
1. **X4** (learned-null test; includes the interventional-design question with unknown nulls).
2. **X3** (as the supplier of learners and the generalisation test, scheduled before or with X4).
3. **X2** (bounded proof attempt).
4. X1 (closed).

## Recommendation
**X1: NO-GO for the design-benefit hypothesis; keep the characterisation as a documented result (REVISE the programme, not the experiment).** Prioritise **X3 combined with X4** (a justified alternative to both X2 and a pure X3), starting with an exact learned-null pilot before any large run, behind the usual gates (new preregistration; independent review; no execution without your approval).
**Single most important next scientific question:** *Without oracle likelihoods, can an embedded observer run a valid sequential test that its own model class is inadequate, and how much of the oracle detection power survives?*
