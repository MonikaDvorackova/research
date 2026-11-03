---
id: topic-bostrom-world-models-proof-obligations
title: "Formal proof-obligation register"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [governance, proofs]
---

# Proof-obligation register
| ID | Obligation | Status |
|---|---|---|
| PO-1 | Props 1–10 correct as qualified | discharged (finite settings; exact enumeration + 129 adversarial cases); `formal-framework.md` |
| PO-2 | Corollary: lower bound ln ω/KL for adaptive designs with non-i.i.d. increments | open — Wald holds under i.i.d. increments; adaptive version requires expected-KL under design (Reviewer 2) |
| PO-3 | General frontier: sup mechanism distance on Π′ given predictive distance on Π (Direction A) | open; T1 |
| PO-4 | Validity of anytime-valid class-adequacy e-process under predictable adaptive designs | open; to be proved (Ville + policy factors cancel) and checked by exact enumeration at small T (X1) |
| PO-5 | Precise equivalence class of POMDPs (minimal PSR dimension) for the benchmark | open |
| PO-6 | Posterior consistency statements for infinite classes | out of scope |
| PO-4 (update, Phase 7) | Validity of the anytime-valid class-adequacy e-process under predictable adaptive designs | **discharged** (elementary): proof in `phase7/02-design-review-D1.md` §1 (supermartingale + Ville, policy factors cancel); exhaustive enumeration for deterministic adaptive rules (P3–P5, 2×3 steps) and empirical 1.69 % type-I; not covered: non-stationary truths, learned (estimated) nulls |
| PO-7 | Validity when the null class is learned/estimated (X4) | open |
| PO-8 | Adaptive-design minimax statement for the margin law (power iff N(d_M − d_A) ≳ ln K + ln(1/α) up to regret) | open; currently heuristic (S5 agreement ±30 %) |
| PO-9 | Minimal latent dimension needed to absorb a deterministic change of known time | open |
| PO-10 | Robust validity of the stationarity e-process under misspecification (which mixing/reset premise suffices?) | open; counterexample for persistent regimes |
| PO-11 | n\* ≈ (d_rich − d)/(2δ) as a theorem | open (folklore; one numerical instance) |
| PO-12 | Reset with a persistent regime does not break the C/D confound | open |
| PO-7 (update, Phase 8) | Confidence-set denominator gives type-I ≤ α + α₁ | **proved** (T6d); power not studied |
| Phase 9 status updates | PO-2 PROVED; PO-7 PROVED under stated assumptions; PO-8 REDUCED TO KNOWN (Chernoff); PO-10 REDUCED TO KNOWN (+ PROVED impossibility for persistent regimes); PO-12 PROVED (R1–R5); O5 REDUCED TO KNOWN; PO-9, PO-11, O1–O4, O6, O7 open | `phase9/04` |
