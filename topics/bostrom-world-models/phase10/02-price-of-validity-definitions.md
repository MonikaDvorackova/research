---
id: topic-bostrom-world-models-phase10-definitions
title: "Price of validity: formal definitions, observer classes, and a critical comparison"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [definitions, price-of-validity]
---

# What "price of validity" means (mathematically)

## 1. Setting and observer classes
Data: a stream of outcomes o_t with predictable contexts x_t. Null 𝒩_𝒯: the set of kernels over which a procedure 𝒯 guarantees P(reject) ≤ α (+ δ). A procedure is an e-process E_t = (numerator q_t) / (denominator D_t). The **numerator** (alternative) is held common (test-stream prequential Dirichlet(½)) so that differences isolate the **null side**.
Observers, with the information each uses (all see the same test stream):
| Observer | Null information | Denominator |
|---|---|---|
| O1 oracle | the true kernel ν\* (simple null) | p_{ν\*}(D) — diagnostic upper bound |
| O2 estimated correctly specified null | training counts; point estimate ν̂ | p_ν̂(D): a test of the **simple** null "ν = ν̂", not of the intended composite null |
| O3 confidence-set null | training stream | sup_{ν∈C} p_ν(D), C an LR confidence set (certified) |
| O4 approximate likelihood | training/test data; EM | p_θ̂(D), θ̂ from an optimiser with no certificate |
| O5 misspecified class | a class that excludes ν\* | formal null false; rejection is not type-I |
| O6 no coverage guarantee | fixed-n boxes, plug-ins, or truncated search | no upper-bound property |
Comparisons are made **only among observers with the same numerator and the same test data**; O4's class differs (HMM) and O5 has no price (its null is false), so those enter as "validity violations", not as prices.

## 2. Definition A — exponent price
For a post-change (alternative) law P let Λ(𝒯; P) = lim_t (1/t) log E_t under P (growth exponent). Λ(oracle; P) = KL(P‖ν\*) (per observation).
 **Π_exp(𝒯; P) = 1 − Λ(𝒯; P)/Λ(oracle; P).**
*Facts.* (i) **Lower bound** (Prop T1): any procedure valid over 𝒩 has Λ ≤ inf_{Q∈𝒩} KL(P‖Q). (ii) For the LR confidence-set test Λ = min_{ν∈C} Σ_c w_c KL(ν₁_c‖ν_c) (exact information projection onto C), computable by the same Lagrangian solver. (iii) For a saturated iid null in change detection with *learned pre-change law* Λ equals the oracle exponent: Π_exp = 0.
## 3. Definition B — delay price
Π_delay(𝒯; P, α, N) = E[τ_𝒯] / E[τ_oracle] (restricted to N, censored). Heuristically E[τ] ≈ (ln(1/α) + Reg_num + Reg_null)/Λ. Reg_null = **null-side evidence overhead**, in nats (what the observer pays before the exponent takes over): dimension of the null class × ½ ln n for a saturated class; 0 for the oracle.
## 4. Definition C — null-side evidence overhead (the residual)
ΔE(𝒯) = (evidence needed by 𝒯) − (evidence needed by the oracle), both at matched numerators; measured as (delay_𝒯 − delay_oracle) × Λ.

## 5. Critical comparison
| Criterion | A (exponent) | B (delay) | C (overhead) |
|---|---|---|---|
| Intrinsic to the validity construction? | **yes** (depends on 𝒩 only) | no (α, N, numerator-dependent) | partly |
| Exactly computable in the benchmark? | **yes** (projection) | only by simulation | only by simulation |
| Explains finite-N zero power? | **no** (exponent = oracle for saturated nulls) | yes | **yes** |
| Monotone in coverage/training size? | yes (verified, `07`) | yes | – |
| Interpretable asymptotically? | yes | needs α→0 | – |
**Choice.** A single number is misleading. The meaningful quantity is the pair **(Π_exp, ΔE)**: Π_exp for *what the guarantee costs asymptotically* (coverage and confidence-set radius), ΔE for *what breadth of the null costs at finite n* (regret). Delay price B is the experimental readout of the pair, not a primitive. Evidence: certified learned null Π_exp = 1 − ρ with ρ = 0.010, 0.240, 0.395, 0.691 (narrow/10³, narrow/10⁴, uniform/10³, uniform/10⁴); saturated null ΔE ≈ 10 nats per cell with Π_exp = 0 (`07`).
## 6. What the price is **not**
It does not compare observers that differ in hypothesis coverage or privileged information: O1 knows ν\*; O3 knows only coverage-limited training data. The "price" of O3 relative to O1 is therefore the price of *not knowing the null*, which equals the price of validity only insofar as validity requires protection over the unknown null — the Gaussian example makes this explicit: efficiency (1 − ρ/μ)² for a confidence half-width ρ and shift μ.
