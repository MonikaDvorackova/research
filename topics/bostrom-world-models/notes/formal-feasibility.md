---
id: topic-bostrom-world-models-formal-feasibility
title: "Formal feasibility: status of candidate propositions"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [formal, proof-obligations]
---

## Formal feasibility

> Superseded by [formal-framework.md](formal-framework.md), which gives the statements and proofs. Kept for the Phase 1 record; the numbering P5–P8 there maps to Propositions 1, 3, 4 and 5.

Setting: E0 and E1 are controlled stochastic processes with kernels p_i(o_t | h_{t-1}, a_t) over a shared action and observation space. A policy π maps histories to action distributions. P_i^π is the law of the T-step history. H0: data from P_0^π; H1: data from P_1^π. Nothing below is proved yet; the table separates what is known from what must be shown.

| Proposition | Status | Notes / proof obligation |
|---|---|---|
| P1. Chain rule: KL(P_0^π ‖ P_1^π) = E_{P_0^π} Σ_t KL(p_0(·\|h,a) ‖ p_1(·\|h,a)) | Known (standard) | Policy terms cancel. Cite, do not claim. |
| P2. Optimal total test error = 1 − TV(P_0^π, P_1^π) (equal priors, summed errors); TV ≤ √(KL/2) | Known (Neyman–Pearson/Le Cam, Pinsker) | Gives a necessary KL for detection at error δ. |
| P3. Stein/Chernoff exponents for repeated testing | Known | Applies per episode if episodes are i.i.d. under fixed π. |
| P4. Value of adaptivity: active policies can improve the sequential-testing exponent | Known (Chernoff; Naghshvar and Javidi 2013) | Do not present as new. Check the exact conditions of their theorems before citing. |
| P5. Exact observational equivalence under all policies iff conditional observation kernels agree on all action-observation sequences | Believed known (observable-operator / predictive-state literature; relation to Armstrong and Castro et al.) | **Literature check needed**; sources not yet searched or verified. |
| P6. Coverage proposition (C2): for any ε>0 and M>0 there exist E0, E1, policy μ with training-distribution per-step KL ≤ ε and a policy π with KL(P_0^π ‖ P_1^π) ≥ M; under a bounded occupancy ratio C, KL_π ≤ C·(training error) per step | Candidate; expected easy | Construction by a rarely visited branch; bound by change of measure. Relate to simulation lemma and compounding-error results (sources to verify). |
| P7. Non-identifiability of "simulated": if two mechanisms with different simulated status induce the same observation law under all policies, no observation-based test separates them, and the posterior on "simulated" depends only on the prior over mechanisms within that fibre | Candidate; elementary | Frames C1. Value is in stating the bridge premises (artifact premise; fidelity premise; reference-status premise), not in difficulty. |
| P8. Bayes-factor form of the null result: the evidential force of "no anomaly detected" for "simulated" is P(no detection \| sim) / P(no detection \| not sim); it is near 1 whenever the simulation hypothesis predicts high fidelity | Candidate; elementary | Duhem–Quine-style point made quantitative; connects to Bostrom's own fidelity assumption. |

### Feasibility judgement

Technically feasible and low-risk. The formal part is a careful application of established results plus two or three elementary propositions (P6–P8). Its honest status is a framework with one useful new quantitative observation (P6), not a major theorem. A reviewer at *Minds and Machines* would weigh the philosophical analysis (C1, P7, P8) more than the mathematics, provided the mathematics is correct and clearly credited.
