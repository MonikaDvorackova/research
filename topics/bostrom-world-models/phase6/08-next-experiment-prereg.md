---
id: topic-bostrom-world-models-phase6-next
title: "Proposed next experiment X1 — hypotheses and falsification criteria (PROPOSAL; not executed)"
topic: bostrom-world-models
type: note
status: proposal
created: 2026-11-03
tags: [preregistration, X1]
---

# Proposed experiment X1: detecting hypothesis-class inadequacy

**Status.** Proposal, written before any X1 data exist. It becomes a pre-registration only when committed in its final form before the development run; the analysis code and thresholds below would then be frozen. No X1 code is written in this phase.

**Setting.** Env 2 (finite POMDP, exact likelihoods). Class M (|M| = 7): reference E0; split-state variants; emission-noise η ∈ {0.05, 0.1, 0.2}; one transition variant with ε = 0.02. Truths: T_in (random member of M, includes the bisimilar split-state control), T_out = Et(ε) with ε ∈ {0.2, 0.5} (outside M), T_deep = Et(ε) mixed with η = 0.1 (outside M).

**Policies.** P1 passive (training policy, q ≈ 0.02); P2 random wide; P3 within-class EIG (exact myopic); P4 criticism-driven design = choose the action maximising expected log E-increment against the saturated order-2 alternative under the current posterior-weighted truth (exact over M ∪ alternative); P5 two-step version of P4 if feasible.

**Test.** E_t = q_t(D_t)/max_{θ∈M} p_θ(D_t) with q_t a prequential Dirichlet(½) predictor on contexts (last action, last observation). Reject the class at the first t with E_t ≥ 1/α, α = 0.05.

**Hypotheses.**
- H1 (validity, exact): under every T_in and every policy, P(reject) ≤ α. *Falsified by any exact or Monte-Carlo estimate with upper 95% bound > 0.05 + 0.02.*
- H2 (barrier, exact): under q = 0 policies the rejection probability is exactly α-bounded for T_out = Et. *Falsified if rejection rate exceeds the H1 bound.*
- H3 (power with coverage): rejection probability of P2 increases with budget and reaches ≥ 0.8 within N_max = 2000 episodes for ε = 0.5. *Falsified otherwise; then X1 lacks power and is revised, not reported as positive.*
- H4 (design): median episodes-to-reject of P4 ≤ P2/1.5 for ε ∈ {0.2, 0.5} (paired bootstrap over seeds, 95% CI lower bound on the ratio ≥ 1.5). *Falsified if CI lower bound < 1.5.*
- H5 (P10 prediction): P3 is not faster than P2 (ratio CI includes 1 or below). *If P3 is faster by ≥ 1.5×, P10's practical relevance for this setting is rejected.*
- H6 (equivalence control): T_in = split-state variant rejected at rate ≤ α under all policies (also covered by H1).

**Seeds and splits.** Development seeds 500–505 (parameters only), confirmatory seeds 600–619, R = 100 episodes-blocks per seed; confirmatory analysis code frozen before running.

**Outcome-metric definitions.** Rejection rate at budget N; episodes-to-reject (censored at 2000, median with censoring-aware bootstrap); share of rejecting evidence attributable to episodes containing action 2.

**Stopping rule for the programme.** If H3 fails the direction X1 is closed and recorded as a negative result (no tuning of the alternative after seeing confirmatory data).

**Known limitations.** Oracle likelihoods; hand-built class; the saturated alternative is a weak order-2 model; results are about a toy POMDP. What would count as a meaningful result: H4 true with H5 true (criticism design helps and within-class EIG does not) — a clean, quantified instance of Prop. 10's lesson for the question "can the agent know its class is inadequate". If H4 fails, the finding is that design does not matter beyond coverage, which collapses X1 into Prop. 3.
