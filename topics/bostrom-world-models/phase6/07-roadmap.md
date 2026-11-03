---
id: topic-bostrom-world-models-phase6-roadmap
title: "Adaptive research roadmap (indicative 4–6 months; gates, not deadlines)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [roadmap, gates]
---

# Adaptive roadmap

Indicative horizon only. **This document does not authorise executing the stages automatically**: every gate needs a review and your go-ahead before the next stage starts. No manuscript title, thesis, or venue is fixed.

| Gate | Focus | Required evidence | Proceed if | Revise the question if | Abandon the hypothesis if | Deliverables |
|---|---|---|---|---|---|---|
| **L1** (weeks 1–3) | Read primary sources: Gelman–Shalizi, Wasserman et al., Catanach–Das, Wolpert, Locatello, Castro, Brogioli (needs your help), Weatherson | Full-text notes with reading level; updated N-matrix | No source already contains X1's design comparison result | A source contains it → drop X1 as contribution, keep as method | – | Verification log update; N-matrix v3 |
| **T1** (weeks 2–5) | X2 theory: frontier statement, proof attempt, exact random-family check | Proof or counterexample; exact computation | A statement strictly stronger than Prop. 3 holds with proof | Statement equals Prop. 3 → Direction A becomes a remark | Frontier is never approached → bound not tight; report | Proof-obligation register entry |
| **D1** (week 3) | Experiment design review for X1, X3 | Pre-specification committed before data; independent reviewer read | Falsifiers and metrics fixed; code frozen | Review finds ill-posed metric | – | Pre-registration files |
| **E1** (weeks 4–8) | X1 development (seeds 500–), then confirmatory (held-out) | Type-I ≤ α by exact check; confirmatory H_a result | H_a supported with CI lower bound ≥ 1.5× | Detection power too low to compare policies | H_a falsified (≤ 1.5×) → report negative | results + README_phase6 |
| **E2** (weeks 6–12) | X3 generalisation (≥ 20 seeds, 3+ learner families, 2 envs) | Confirmatory result on coverage hypothesis | H_cov survives or characterised exception | Failure under full coverage in some family → new question: what in the learner causes it | H_cov falsified broadly → drop “coverage” story | results; mixed-effects analysis |
| **P1** (week 10) | Proof audit of anything claimed | Exact enumeration + adversarial cases for new statements | All claimed statements pass | A claim fails → correct visibly | – | Updated audit tables |
| **G2** (week 12) | Decide whether to build X4 | X1 passed | Updating/criticism/expansion distinction measurable | X1 mixed | X1 negative | X4 prereg or closure note |
| **R2** (weeks 12–16) | Independent replication (another machine/OS; ideally a human collaborator re-running) | Same hashes or documented tolerance | Decisions replicate | Differences → investigate nondeterminism | – | replication note |
| **N1** (weeks 14–18) | Negative-result analysis | Register complete | – | – | – | negative-results register |
| **Q1** (weeks 16–24) | Publication-readiness review (venue open) | A result that survives L1, T1, E1, E2, R2 | Contribution is more than integration | Only methodological note possible | Nothing survives → publish as null/negative report or stop | readiness review; **decision by you** |

## Standing rules at every gate
Exploratory vs confirmatory separated; hypotheses frozen before data; results hash manifests; corrections logged; no submission or merge without your explicit approval.
