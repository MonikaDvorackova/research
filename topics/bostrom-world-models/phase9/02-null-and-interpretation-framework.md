---
id: topic-bostrom-world-models-phase9-framework
title: "Corrected formal-null and interpretation framework"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [framework, semantics]
---

# Formal nulls, false positives and interpretation

## 1. Seven notions that must not be conflated
1. **Predictive accuracy**: expected score of the observer's forecasts (e.g. Brier, log loss) on the interaction process.
2. **Statistical distinguishability**: TV(P_E^π, P_{E′}^π) > 0 for some admissible π.
3. **Model-class adequacy**: inf over the class of a divergence to the truth on the probed interventions — **always relative to a comparator or to the truth**; one learning curve cannot separate entropy from misspecification (T3, D3 of Phase 8).
4. **Parameter / mechanism identifiability**: identification of the *minimal* realisation of the observable law. For HMMs this is generic up to label swapping (Allman et al. Thm 6; Petrie): non-identifiability is non-generic, non-minimal (bisimilar representations), or due to unprobed interventions.
5. **Computational tractability**: ability to compute the test statistic with a guarantee (certified suprema; approximate EM maximisers void the guarantee, `07-…` E).
6. **Epistemic justification**: which premises license a step from a statistical conclusion to a claim about mechanism.
7. **Metaphysical conclusions about simulation**: not licensed by any item above. Rejecting an observer's model class says nothing about whether its environment is simulated; it is at most a fact about the pair (observer's class, environment) on the probed interventions.

## 2. Three-way separation of what a rejection can mean
For a procedure φ with formal null 𝒩 (a set of laws of the data) and level α:
- **Statistical type-I error** exists only when the truth ∈ 𝒩 and P(reject) > α. This is a statement about 𝒩 and nothing else.
- **Model misspecification** is truth ∉ 𝒩. Then rejection is **correct** with respect to 𝒩. It may be informative ("the observer's class is inadequate") — this is the purpose of an adequacy test.
- **False attribution** is the inference "the physical mechanism changed" (or "the environment is different from before") from a rejection of 𝒩. It is valid only if 𝒩 contains *every* stationary generator the observer considers possible — i.e. 𝒩 ⊇ 𝒢_stat. If 𝒩 ⊊ 𝒢_stat, a rejection can come from a stationary generator outside 𝒩.
- **Failure of the observer's semantic interpretation** is a further error: reading a rejection in a vocabulary (mechanism, simulation) the test does not speak.
Also distinguish **kernel change** (the observable conditional law changes over time — what any test can address) from **generator change** (the underlying physical mechanism changes). A persistent latent regime produces genuine *kernel* change with an *unchanged generator*; by T4 the two descriptions are observationally equivalent in a single trajectory.

## 3. Reanalysis of the Phase 8 counterexample (as required)
| Phase 8 observation | Formal null | Truth in null? | Correct description |
|---|---|---|---|
| D2b: stationary hidden regime, order-1 stationarity e-process rejects 40/40 (also from a stationary start) | N_ctx: conditional law of o_t given the entire past = ν(·|x_t), time-invariant | **No** (regime persistence makes the conditional law depend on the past beyond x_t, and it is not time-invariant locally) | Not a type-I violation. Correct rejection of N_ctx under misspecification; **would be a false attribution if read as "mechanism change"**. The stationary-start control shows the cause is regime persistence, not an initial transient. |
| D4a: frozen learned null rejects 98–100 % under pure policy shift | simple null "environment kernel = p̂" | **No** (p̂ ≠ ν\*) | Correct rejection; the observer's epistemic gap (p̂ estimated on a narrow policy) is mistaken for "change"; the *intended* null (kernel unchanged since training) is composite and requires a denominator dominating ν\*'s likelihood (T6d). |
| D4b: approximate maximiser, 39/40 vs 0/40 | the searched subclass | **No** (the omitted member is the truth) | Correct rejection of the subclass. Silent mismatch between the class the observer *intends* (full M) and the class it *searched*; a guarantee for M is voided. |
| S4/S5 "0/100" | N_ctx | No | Low power, not robustness (A2). |

## 4. Corrected inference ladder with the formal object at each rung
| Rung | Statement | Formal object | Extra premises needed |
|---|---|---|---|
| 1 | Rejection | φ rejects 𝒩 at level α | truth-agnostic if 𝒩 is the declared null |
| 2 | Class inadequacy relative to a comparator | predictive-score gap (Prop D) or LR margin (X1) | the comparator is predictable and declared before the data |
| 3 | Kernel change | rejection of "one time-invariant kernel" with 𝒩 ⊇ all stationary kernels in the class | the class contains the stationary truth (Prop B) |
| 4 | Generator/mechanism change | 𝒩 ⊇ 𝒢_stat | resets that redraw the regime, observed context, or modularity (T4, R-series) |
| 5 | Implementation / simulation | – | substrate premises; outside the data |

## 5. Does the research question stay coherent?
Provisional wording: *"Under what assumptions can an embedded observer, equipped with an imperfect learned model of its environment, distinguish prediction error, model-class inadequacy, distribution shift and genuine changes in the generating mechanism?"*
Verdict: **coherent only after the following revision.** (i) Two of the four items (shift vs generator change) are not properties of the observable law (T4), so "distinguish" must be phrased as "under which declared structure is each distinction identifiable"; (ii) "prediction error" splits into epistemic gap (resolves with data) and class inadequacy (plateau), which are separable only relative to a comparator and above a scale n·ε ≳ 1; (iii) the question is a question about **epistemic limitations of learned world models**, with Bostrom/Chalmers only as motivation for why "mechanism" and "simulation" labels are not warranted by data. The more productive contribution, if any, is therefore a theory (or at least a quantified map) of what each class of tests can license, not simulation detection.
