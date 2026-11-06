---
id: topic-bostrom-world-models-novelty-and-gap
title: "Novelty and research-gap assessment (Phase 1)"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [novelty, gap]
---

## Novelty and research-gap assessment

Evidence base: [verification-log.md](../literature/verification-log.md) and [comparison-matrix.md](../literature/comparison-matrix.md). Most sources were read at abstract level only, so this assessment is provisional.

### What is not novel

- That a simulation may or may not be detectable from inside (Bostrom's own discussion; Beane et al.; Birch; Chalmers).
- Observational and counterfactual equivalence of POMDPs (Armstrong; Castro et al.; Givan et al.).
- Error exponents, Le Cam and Pinsker bounds, and the benefit of adaptive experiment choice in sequential testing (Chernoff-line results; Naghshvar and Javidi).
- Anomaly detection with world models (Ikram et al. and earlier work; content not yet read).

### The gap that survives the search

1. **No bridge between detection theory and the simulation-inference question.** The literature treats "is the world a simulation" metaphysically (Chalmers, Birch) or physically (Beane et al.). Nothing found analyses what a statistical discrepancy between an environment and a model class licenses an embedded agent to infer.
2. **No controlled study of passive vs active detection against learned world models with equivalent negative controls**, framed around embedded agents rather than sim-to-real transfer. (Absence of discovered work only.)

### Strongest defensible claims (to be tested, not asserted)

- **C1 (conceptual, philosophical).** Three claims come apart: discrepancy detected, generating process identified, "simulated" concluded. Moving between them needs explicit bridge premises, and the premises needed to reach "simulated" are not supplied by any observational test.
- **C2 (formal, elementary but useful).** Detectability is governed by interventional coverage, not in-distribution fit: a model with arbitrarily small training-distribution error can have arbitrarily large KL under an intervention policy outside the training support. Under a bounded density ratio, detectability is bounded by that ratio times the training error. Expected to be easy to prove and close to existing simulation-lemma and compounding-error arguments; its value is the application to detection and the measurement in C3.
- **C3 (empirical).** On a small benchmark, active intervention selection reaches a given detection error with fewer samples than passive or random policies, and the advantage grows as model quality improves, with equivalent negative controls giving chance-level detection.

C1 carries the philosophical contribution. C2 and C3 supply technical credibility. No claim of a new theorem about active testing is made.

### Required fix to the design

A likelihood-ratio test between E0 and E1 needs both likelihoods. An embedded agent has neither. The experiments must therefore include (a) an oracle-likelihood upper bound, (b) an agent with access to samples from E0 only (the realistic "reference" condition), and (c) an agent with only a learned density. Otherwise the result is the trivial statement that an oracle test works.
