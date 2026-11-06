---
id: topic-bostrom-world-models-phase7-audit
title: "Second-pass mathematical and statistical audit; adversarial reviewers A–C"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-03
tags: [audit, review, X1]
---

# Second-pass audit (Part 6) and adversarial reviews (Part 8)

**Independence caveat.** Everything here was produced by the same agent. "Independent" means: a different code path or exact enumeration, not an external person. Output: `results/x1_audit/independent_audit.txt`; supplementary recomputation: `results/x1_confirm/supplementary_exploratory.md` (S4).

## Checks performed
| Item | Method | Result |
|---|---|---|
| Filtering equations, likelihoods | brute-force sum over all hidden paths (`pomdp.brute_force_obs_law`) vs an explicit-loop forward recursion written for the audit vs the vectorised filter | max |Δ log-likelihood| = 8.9×10⁻¹⁶ over 25 cases — **pass** (the loop filter and the brute force are separate from `x1.run`'s einsum filter; the einsum filter is covered by the unit test that sums to 1 under adaptive rules) |
| Null/alternative definitions | null H₀: the interaction kernel (conditional law of observation given history and action) equals that of some m ∈ M; alternative: not | consistent with the statistic; see D1 §1–2 |
| Supermartingale, optional stopping, adaptivity | **exhaustive enumeration** of the observation tree (2 episodes × 3 steps, 3 observations) under deterministic adaptive rules P3, P4, P5 for truths E0 and n10: total probability 1 (1e-12); E[E_final] ≈ 0.90–0.91 ≤ 1; P(max E ≥ c) for c = 1.2, 1.5, 2, 3 is 0.048–0.084, 0.005–0.014, ≤ 0.002, 0 — all ≤ 1/c by a wide margin | **pass** for these rules and horizon |
| Randomised policies P0–P2 and random tie-breaks | covered by the proof (the action's law depends only on the past); not enumerated | proof only |
| Policy decisions P3/P4/P5 | recomputed with explicit loops from first principles (entropy, mutual information, Jensen–Shannon) on 90 random histories | 0 mismatches |
| Intervention budgets | action-selection spy on a development seed (never-stopping) | matches the information-access matrix |
| Numerical stability | logs, clipping at 1e-300; 0 non-finite values in 36 000 + 7 200 + 6 000 runs; E-process bounded by tests | pass |
| Randomisation / streams | integer-keyed `SeedSequence([seed, truth_id, policy_idx, rep, {1,2}])`; the environment and observer streams are separate | pass; no `hash()` |
| Confidence intervals | primary: percentile bootstrap, seed unit; independent: jackknife SE (reproduces within 0.01–0.02 in log), 99 % bootstrap, different RNG; exact CP via `binomtest` | all primary bounds reproduce (P2/P4 lb: 1.86/1.59/1.71 vs jackknife 1.85/1.58/1.70; 99 %: 1.82/1.54/1.66) |
| Multiple comparisons | The decisions are intersection–union (all of 3 truths must pass), for which no adjustment is needed; H1 uses a per-cell bound with margin (max 0.044 vs 0.07); at 99 % the H4a lower bounds are 1.82, 1.54, 1.66, still ≥ 1.5 (pc1 narrowly) | no change in any decision |
| Counterexample search | exact enumeration for ties and degenerate priors was attempted only through the checks above; none found | no counterexample found |

## Issue register
| ID | Issue | Class | Status |
|---|---|---|---|
| A1 | Phase 6 proposal infeasible (saturated alternative) and confounded (P4 had W, P3 did not) | Major | Resolved before confirmation (D1, preregistration revision) |
| A2 | Positive controls pc0–pc2 are members of W: H4a/H4c are about anticipated deviations; the truth's family is known to the alternative | Major | **Unresolved** by design; limits scope. Mitigated by reporting unanticipated truths separately (t05, t10) |
| A3 | One environment family, hand-built classes, oracle likelihoods, T = 4; no learned model | Major | **Unresolved** (X3) |
| A4 | Seeds = 30 environment instances; run-level pooling overstates independence in binomial bounds | Minor | Resolved by seed-cluster intervals (S1); decisions unchanged |
| A5 | H5 preregistered rule returned "inconclusive" because the effect is heterogeneous across truths (pc0 +1.44×, pc1/pc2 −6–8×) | Minor | Reported as found; the rule not altered. Lesson: a single criterion across heterogeneous truths is a weak design |
| A6 | RMST ratios compress under heavy censoring (t05, t10 for some policies) | Minor | Disclosed; detection probabilities reported alongside |
| A7 | Exact enumeration covers deterministic adaptive rules at 6 steps; the full run uses random tie-breaking and horizon 12 000 steps | Minor | Covered by proof; not enumerated |
| A8 | The proof assumes truth ∈ M with the same protocol and an independent episode reset; the "shift" control violates stationarity and is not covered | Minor | Disclosed; "shift" only exploratory (rejection 1.7–3.7 %) |
| A9 | The same author wrote design, code, audit | Major | **Unresolved**: external review needed |
| A10 | Mixture-alternative regret grows with K; power depends on W's size/shape (not varied) | Minor | Unresolved; sensitivity to W not studied |
| A11 | No test of the exact claim "the policy cannot change type-I error" under policies that adapt using W, beyond the proof and enumeration | Minor | Resolved by enumeration for P4/P5 |

**No critical issue is unresolved.** Major unresolved items (A2, A3, A9) bound the *scope* of the claims; they do not invalidate the confirmatory outcomes of H1–H5.

## Reviewer A — mathematical statistics
*Strongest objection.* "Everything is expected from sequential-testing theory: the e-process is a likelihood-ratio supermartingale; power is the KL margin; EIG with a mis-targeted variable is slow. The 1.5× design benefit is a statement about the choice of target variable, which any decision theorist predicts: if the target is member identity within a class that does not vary on the informative action, information about that target is zero there."
*Evidence offered / still required.* S5 shows that the exact margin predicts the order of magnitude of detection times, i.e. the results *are* an instance of known theory (class A below). Required to answer: a theorem about adaptive design (e.g. minimax over policies) that is not a corollary of Wald/Neyman–Pearson and P10 — not provided.
## Reviewer B — machine learning
*Strongest objection.* "A 4-state POMDP with exact likelihoods and a hand-built W that includes the truth is not an embedded agent. The agent would need to learn the null model; with learned likelihoods your own Phase 5 shows the failure. The comparison P4 vs P5 only says something about two EIG variants once the truth is in W."
*Evidence still required.* Learned-null versions of the test (valid estimators), at least two environment families, and a W built without reference to the truth family. Not provided. Also the sensitivity to |W| and to the geometry of W.
## Reviewer C — philosophy of science
*Strongest objection.* "Detecting that M fails (a rejection of a stationary finite class) says nothing about the true mechanism; it is Duhem–Quine: failure falls on M or on auxiliary assumptions (stationarity, the protocol). Nothing here touches simulation. 'Anticipated vs unanticipated' is just Kuhn/Laudan–Leplin: you can only reject relative to alternatives you can formulate."
*Response/limits.* Agreed on all counts; the result is a quantified, exact instance of 'rejection requires a rival', not a contribution to the simulation debate. What would address it: a premise-by-premise account of what additional assumptions map rejection of M to a claim about the mechanism, which remains pure philosophy and is not supplied by this experiment.
**No consensus is claimed**: Reviewers A and B disagree on what would make the work valuable (a theorem vs a learned-agent demonstration); Reviewer C would count neither as bearing on simulation.
