---
id: topic-bostrom-world-models-phase6-reviews
title: "Three adversarial reviewer assessments (written by the author; not independent)"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-03
tags: [review, adversarial]
---

# Adversarial reviews

Caveat: all three reviews are written by the same agent that produced the work, so they simulate, not replace, independent review. Disagreements between reviewers are kept.

## Reviewer 1 — Philosophy of science
- **A:** "Prediction ≠ identification is the underdetermination thesis in new clothes." *Addressable?* Only by a narrower claim: quantified, interventional version for learned observers (empirical), not a philosophical thesis.
- **B/E:** "Observational equivalence relative to an intervention class is textbook; hidden-state quotient is bisimulation." Not addressable; report as known.
- **C:** "Discovering that your hypothesis space is inadequate is Kuhnian anomaly/crisis plus Gelman–Shalizi model-checking. The `updating vs discovery' distinction is not new." *Narrower claim:* provide operational definitions with measurable separation (X1/X4) and cite openly.
- **D:** "Nested simulation is hand-waving; there is no formal bridge." Agree; deferred.
- **F:** "Your ladder merges epistemic and metaphysical steps; rung 3→4 depends on substrate-independence, which Bostrom assumes and Chalmers treats differently." Partly agree: the ladder is a bookkeeping device. Reviewer also doubts any link to Bostrom survives once the experiments concern toy environments: "Your results are about learned-model evaluation, not the simulation argument." *Response:* the link is only the indifference proviso and the anomaly-editing assumption; do not claim more.

## Reviewer 2 — Mathematical statistics and learning theory
- **A:** "Frontier = data-processing inequality; the amplification factor is the likelihood-ratio bound." Likely correct; X2 exists to test whether anything beyond that exists.
- **B:** "ε-equivalence is meaningless without a loss; TV vs KL give different frontiers; define it." Required in X2 (both reported).
- **C:** "Your anytime-valid test is the universal-inference e-process; Ville's inequality gives validity; with adaptive designs the policy factors cancel only if the policy is predictable and the observation model does not depend on unobserved policy randomisation." Accepted; add exact enumeration check of type-I error at small horizon.
- **C′:** "sup over θ in the denominator is conservative and the saturated alternative's regret grows with context order; power may be poor." Accepted as failure mode.
- **E:** "No identifiability notion is stated for the POMDP beyond equivalence of observation laws; state the equivalence class precisely (minimal PSR dimension)." Add to X2.
- **General:** "Wald lower bound ln ω / KL requires i.i.d. increments; with adaptive design use the expected KL under the design." Accepted.

## Reviewer 3 — Machine learning and experimental methodology
- "Two environments, toy sizes, one learner family each, 12 seeds: nothing generalises." → X3.
- "The oracle observer uses ground-truth likelihoods, so `oracle succeeds' is a tautology; the interesting regime is learned likelihoods, and there you only tried narrow-trained learners without ensembles or calibration." → X3 includes ensembles, temperature scaling.
- "Environment designer controls which interventions are `informative'; the result `coverage matters' is built in." Agree; the empirical question is conditional (how often real learners are narrow).
- "Reference is defined as the training environment, so inversion is just OOD detection." Agree, partly; that is why the claim is limited to observers.
- "Run A was not deterministic; one machine." Accepted; run B fixes; repeat on another machine is a roadmap item (Gate R2).
- "E3b non-replication shows your equivalence claims are fragile." Accepted; do not claim.
- "Hyperparameters for GRU tuned on dev seed." Pre-specify in X3.

## Which criticisms are addressable
| Criticism | Experimentally | Theoretically | Narrower claim |
|---|---|---|---|
| Generality (R3) | X3 | – | claim only for covered learner families |
| Known theory (R1, R2) | – | X2 | cite and restate as known |
| Updating vs discovery (R1) | X1/X4 | operational definitions | distinguish by measurable criteria |
| Validity of test (R2) | exact enumeration | proof via Ville | limit to predictable designs |
| Connection to Bostrom (R1) | – | – | restrict to proviso/anomaly-editing; no empirical bearing |
