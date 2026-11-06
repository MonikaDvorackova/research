---
id: topic-bostrom-world-models-phase9-reviews
title: "Phase 9 adversarial reviews (internal; not external peer review)"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-04
tags: [review, adversarial]
---

# Three internal adversarial reviews
Written by the same agent that produced the work; disagreements and unresolved objections are retained.

## Reviewer A — mathematical statistician
**Attacks.**
1. *Null definitions.* "Every procedure here is valid iff the truth is in its null — a tautology. The audit just states what validity means." **Response:** agreed; the content is that Phase 8 mislabelled out-of-class rejections (A1) and over-read non-rejections (A2); nothing beyond textbook semantics is claimed.
2. *Novelty.* X1-V is Emmenegger et al. Theorem 1; Prop C is the categorical case of Shin et al.; Prop D is Choe–Ramdas/Robbins. **Response:** accepted; `03-…` classifies them as corollaries.
3. *Sequential validity of the dev CS-repair.* "Your CP boxes are fixed-n applied to data-dependent counts; coverage is unproven." **Accepted** (A4); replaced by LR confidence sequences in E6′.
4. *Proof of Prop D uses Hoeffding conditionally and a Gaussian mixture over both signs — the boundary is two-sided and conservative; is `ρ = 2000` tuned?* ρ was fixed before the run; two-sidedness costs power (the dev E_comp had zero power). Open: a one-sided/stitched boundary.
5. *Clustering and multiplicity.* Corrected in `06-…`; the objection that even cluster-level intervals undercover at R = 20 is **confirmed** by the audit (0.85–0.93).
6. *Prop 5 exact-size requirement* — accepted (A5).
**Unresolved:** a non-trivial theorem about minimax detection time as a function of null-class complexity (the robustness–power frontier) is neither proved nor excluded as known (Le Cam/Ingster-type results `[memory]`, not read).

## Reviewer B — machine learning researcher
**Attacks.**
1. *Generalisation.* "A = 3, O = 3, T = 4, hand-structured hidden-state chains; the learned-observer story (count tables, EM) is not the neural world-model story that motivated the project." **Accepted**; GRU/ensemble are deferred and flagged.
2. *Power.* "Your valid procedures have zero power at N = 3000; the experiment will return nulls for the robust procedures and you will call it a 'frontier'." **Response:** the dev run already shows this; the proposed experiment measures *how large N must be* relative to the Chernoff bound. A result of "no power at feasible N across all independent generators" would be reported as the finding, but Reviewer B holds that this is a statement about toy alphabets rather than learned models.
3. *Leakage.* "P4/P5 and the e-process mixtures used the alternative family W; E6′ ladder rungs use comparators declared in advance." The dev runs use comparators fixed before the run; no truth information reaches any procedure (source/signature inspection test added: `test_procedures_receive_only_data_arrays_no_environment_objects`).
4. *Architectural confound.* EM restarts and budgets are tuned ad hoc (60/300 iterations); the 62 %/15 % figures depend on this.
5. *Distribution-shift artefacts.* "H2's null result is because your policy shift is mild; engineered shifts would produce false D attributions." **Agreed** (exact discrepancy ≤ 2.5×10⁻³); an engineered case should be added as a *positive control for false attribution*.
**Unresolved:** no non-toy test; no check that the order-1/2 count learners are representative.

## Reviewer C — philosopher of science
**Attacks.**
1. *Prediction vs mechanism.* "Your 'mechanism' is the minimal realisation of the observable law. For HMMs it is generically identifiable up to labels (Allman et al.), so the supposed gap between prediction and identification is a gap between a model class and a coverage condition, not an epistemic gap about the world." **Accepted**: with the corrected T5 and the R-series, non-identifiability is (i) non-generic, (ii) non-minimal representation, (iii) unprobed interventions, (iv) persistence/regime equivalence — all assumptions about interface and class.
2. *Underdetermination.* "Persistent regime ≡ random-time change is the Duhem–Quine point with a probability measure." **Accepted**; the contribution is the exact check and the reset taxonomy, not a thesis.
3. *Theory-ladenness.* "Declaring 𝒩 ⊇ 𝒢_stat requires deciding which generators count as 'stationary' — a theory-laden choice the observer must make *before* data." **Accepted** and now explicit in `02-…` §2.
4. *Metaphysics.* "Nothing licenses simulation talk." **Agreed**; Bostrom/Chalmers remain motivation (anomaly editing builds KL → 0 into the hypothesis).
**Unresolved:** whether the project's remaining question is philosophically interesting beyond a clarification of what statistical tests can license. Reviewer C is not convinced that it is.

## Disagreements retained
- A would pursue the minimax frontier theorem; B would pursue a non-toy empirical test; C would pursue neither as philosophy. 
- A and B disagree on whether zero power of robust procedures is a finding (A: it is the regret scaling; B: a toy artefact).
