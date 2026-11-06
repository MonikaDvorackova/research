---
id: topic-bostrom-world-models-phase7-prereg
title: "Preregistration X1 (frozen before confirmatory data)"
topic: bostrom-world-models
type: note
status: frozen
created: 2026-11-03
tags: [preregistration, X1]
---

# Preregistration: X1 — detecting hypothesis-class inadequacy

**Frozen at the commit that contains this file; the confirmatory run is executed only afterwards.** The commit hash is recorded in `04-results-X1.md`. Analysis code `src/eid/analyze_x1.py` and `configs/x1_confirm.yaml` are frozen in the same commit; neither may change after confirmatory outcomes exist.

## Changes from the Phase 6 proposal (all made after development runs on seeds 500–505, before any confirmatory data)
(1) Alternative family W is action-structured; class M has four members (no t.02 member). (2) Test statistic is a Bayes-mixture alternative over M ∪ W instead of a saturated order-2 predictor (D1.1). (3) Added P5, within-class EIG over M ∪ W, because P4 and P3 differ in information (D1.3). (4) Effect size is restricted mean time (D1.4). (5) N = 3000, 30 seeds, R = 20 (D1 §6). (6) Hypothesis set reorganised: H1–H3, H4a/b/c, H5. (7) The Phase 6 prediction "unanticipated deviations are undetectable" is withdrawn (D1.5). **Dev exposure:** I have seen development results (seeds 500–505): P4 and P5 are faster than random on anticipated deviations; **P5 ≥ P4 on anticipated deviations**; P3 (member EIG on M only) is slower than random on pc1/pc2; t10 detected 70% by random. Predictions below are informed by that exposure and are labelled.

## Setting
Finite POMDP (4 hidden states, 3 observations, 3 actions; action 2 reveals hidden state 0 vs 1), episodes of T = 4 steps, N = 3000 episodes maximum, exact filtering. Null class M = {E0, emission-noise 0.05, 0.10, 0.20}. Observer's wide family W: 42 members (3 action groups × 14), each E0 with the transition rows of **one action** perturbed (Dirichlet mixing, λ = 0.2 for 7, 0.5 for 7). K = 46. Test: E_t = (K⁻¹ Σ_k p_k(D_t)) / max_{m∈M} p_m(D_t), reject at first E_t ≥ 20 (α = 0.05), checked after every observation. Validity proven in `02-design-review-D1.md` §1.

**Truths** (`truths_for`): null: E0, split (bisimilar, S = 5), n10, n20 (members). Unanticipated: t05, t10 (action-2 rows of states 0, 1 swapped with weight 0.5, 1.0; not in W). Anticipated: pc0, pc1, pc2 (the median-distance member of W's action-0/1/2 group; exact rule in `x1_exact.pc_member_index`). Exploratory: "shift" (E0 for the first third of the budget, then n20).
**Policies**: P0 never action 2 (negative control); P1 passive (action 2 w.p. 0.02); P2 random wide; P3 within-class EIG over M (member identity); P4 class-level EIG (JS divergence between posterior-predictives of M and W); P5 within-class EIG over M ∪ W.
**Seeds**: confirmatory 600–629 (30). R = 20 runs per (seed, truth, policy). Unit of analysis for efficiency ratios: seed. Dev seeds 500–505 used for implementation validation only. Config: `configs/x1_confirm.yaml`.

## Hypotheses and decision rules (primary)
- **H1 (validity).** Under each null truth and each of the 6 policies, the rejection rate is ≤ α. *Supported* if every cell's 95% Clopper–Pearson upper bound ≤ 0.07 and the pooled rate ≤ 0.05; *contradicted* if the pooled lower bound > 0.05; else inconclusive. (Cells are pooled over runs within seeds; this ignores within-seed dependence; reported.)
- **H2 (barrier).** Under P0, truths t05, t10, pc2 are rejected at ≤ α (CP upper bound ≤ 0.07 each): without action 2 they are indistinguishable from a member's law.
- **H3 (power).** Under P2, rejection within 1500 episodes ≥ 0.8 for pc0, pc1, pc2.
- **H4a (design benefit, anticipated).** RMST(P2)/RMST(P4) has bootstrap lower 95% bound ≥ 1.5 for **all** of pc0, pc1, pc2. *Contradicted* if any upper bound < 1.5; else inconclusive. Dev expectation: borderline (point estimates 1.4–2.0).
- **H4b (design benefit, unanticipated).** Same for t05 and t10. Dev expectation: **not met** (t10 ratio ≈ 1.05; t05 mostly censored).
- **H4c (criticism target vs identification target, same information).** RMST(P5)/RMST(P4) lower 95% bound ≥ 1.5 for all of pc0–pc2. Dev expectation: **contradicted** (P5 ≥ P4 on anticipated truths).
- **H5 (within-class EIG on M is not an efficient criticism design).** RMST(P2)/RMST(P3) upper bound < 1.5 for pc0, pc1, pc2 ⇒ supported; any lower bound ≥ 1.5 ⇒ contradicted. Dev expectation: supported (P3 slower than random on pc1/pc2).

**Effect size.** RMST = mean over runs of min(episodes to rejection, N) per seed; ratio per seed; geometric mean across seeds; percentile bootstrap over seeds, 10 000 resamples, seed 20261103. The threshold 1.5 was set in Phase 6 and is **not changed**.

## Secondary and exploratory (not decision-bearing)
Rejection rates by budget {100, 200, 400, 800, 1500, 3000}; median time; the "shift" control; per-policy computational cost; exact feasibility table for each confirmatory seed (exact calculation, no outcomes).

## Controls
Negative: null truths (all policies), split-state equivalence, P0. Positive: pc truths under P2. No privileged information: observers get only actions and observations (source-inspection test). Leakage: seeds disjoint; streams from integer keys.

## Outcome classification (before seeing results)
- **Success of the X1 design hypothesis:** H1, H2, H3 supported **and** H4a supported **and** H4c supported.
- **Informative failure:** H1–H3 supported and H4c contradicted ⇒ the apparent advantage of "criticism design" is access to the alternative family, not the criticism target. This is preserved and reported as a negative result about the target variable.
- **Invalid:** H1 or H2 contradicted ⇒ implementation or proof error; results withheld, correction logged, no confirmatory re-run without a new preregistration.
- **Inconclusive:** otherwise.

## What a negative result would rule out
H4a contradicted: with the alternative family given, criticism-oriented sampling brings no ≥ 1.5× benefit over random in this benchmark. H4c contradicted: class-level targeting is not what produces the gain.

## Limits
One environment family, oracle likelihoods, hand-built classes, α = 0.05, T = 4. Bears on nothing physical. Detection of class inadequacy ≠ identification of a better mechanism ≠ simulation.
