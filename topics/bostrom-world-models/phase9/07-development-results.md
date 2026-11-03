---
id: topic-bostrom-world-models-phase9-dev
title: "Phase 9 development results (exploratory; includes negative findings)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [development, results, negative]
---

# Development results (all exploratory; namespace 9000; not confirmatory)

Artifacts: `results/phase9_dev/` (`runs.jsonl`, `semantics_table.md`, `audit_dev.md`, `em_cs_dev.md`, `tradeoff_dev.md`); code `src/eid/{e6gen,e6proc,iohmm,phase9_audit}.py`, `scripts/phase9_*.py`; tests `tests/test_{e6gen,e6proc,phase9_audit}.py` (290 tests pass in total). Reproducibility: 30 stored runs re-executed with identical rejection times (0 mismatches); seed namespace disjoint from all earlier and reserved seeds. Data sizes are small by design (10 instances × 3 runs per scenario, 30 runs per cell); intervals are Clopper–Pearson on pooled runs and **not clustering-aware**, so they are indicative only.

## 1. Formal-null semantics across independent generators (10 scenarios × 4 procedures; N = 3000 episodes × 4 steps)
Full table: `results/phase9_dev/semantics_table.md`. Rejections / 30 runs (instances with ≥ 1 rejection / 10):
| scenario | physical mechanism changed | E_ctx (null?) | E_ep (null?) | E_comp (forgetting) | E_comp (order-2) |
|---|---|---|---|---|---|
| M1 Markov, stationary | no | 0/30 (T) | 0/30 (T) | 0/30 | 0/30 |
| M2 Markov, pure policy shift | no | 0/30 (T) | 0/30 (T) | 0/30 | 0/30 |
| M3 Markov, mechanism change, changed action played | yes | **30/30** (F; 10/10) | 0/30 (F) | 0/30 | 0/30 |
| M4 Markov, change in an action never played | yes (unobservable) | 0/30 (T) | 0/30 (T) | 0/30 | 0/30 |
| H1 hidden-state, stationary, resets | no | 0/30 (F) | 0/30 (T) | 0/30 | 0/30 |
| H2 hidden-state, extreme policy shift | no | 0/30 (F) | 0/30 (T) | 0/30 | 0/30 |
| H3 hidden-state, change played | yes | 5/30 (F; 2/10) | 0/30 (F) | 0/30 | 0/30 |
| H4 hidden-state, change in an unplayed action | yes (unobservable) | 0/30 (F) | 0/30 (T) | 0/30 | 0/30 |
| H5 hidden-state, switch to bisimilar twin | no (TV = 0) | 0/30 (F) | 0/30 (T) | 0/30 | 0/30 |
| R1 persistent latent regime, stationary generator | no | **8/30** (F; 3/10) | 0/30 (F) | 0/30 | 0/30 |
(T)/(F): whether the procedure's **formal null** holds. E_comp nulls are approximate (asymptotic sign).

**Findings.**
1. **No null-true cell produced a rejection** (E_ctx 0/90 in M1, M2, M4; E_ep 0/180 in its null-true cells M1, M2, M4, H1, H2, H4, H5). With 30 runs per cell the bound is 0.095; the data check for gross failure only.
2. **False-attribution events** (rejection with an unchanged physical generator): only **R1** (8/30). Hidden-state stationarity (H1), policy shift under misspecification (H2) and the bisimilar twin (H5) produced none for E_ctx despite the null being false. Exact reason for H2: the policy-induced movement of the pooled order-1 kernel is ≤ 2.5×10⁻³ nats/observation in the ten random instances (`audit_dev.md` D), far below the regret scale (≈ 36 parameters × ln N / 2); detection would need ≈ 5×10⁴ post-shift observations. The risk is real in principle but small unless a policy contrast is engineered.
3. **Power is where the null is true or nearly so**: E_ctx detects M3 in 30/30 (the change is inside its class) and H3 in only 5/30 (misspecification masks change).
4. **Robust-valid procedures were powerless at N = 3000**: E_ep (valid under any hidden-state generator with perfect resets) rejected 0/30 even for M3; E_comp rejected 0/30 in every scenario with either comparator, including M3. Cost: E_ep 3.3 s/run (50× E_ctx).
5. **Negative findings preserved**: the predictive-comparison procedure (ρ = 2000, comparators chosen before the run) did not detect any change; the dev data cannot say whether a better-tuned boundary or comparator would.

## 2. Corrected Occam dissociation (exact)
See `01-…` §3. Identification of the true mechanism dips and recovers for every ψ₀ ≠ ½; window ≈ c/(ψ₀ − ½)².

## 3. Chernoff reconciliation (exact; X1 benchmark seed 500)
| truth | uniform | passive | Chernoff-optimal | optimal/uniform | observed X1 gain of P4 over P2 | observed/optimal |
|---|---|---|---|---|---|---|
| pc0 | 1.71e-2 | 2.00e-2 | 3.71e-2 | 2.17 | 2.01 | 0.93 |
| pc1 | 2.39e-2 | 2.80e-2 | 5.69e-2 | 2.39 | 1.74 | 0.73 |
| pc2 | 2.37e-2 | 1.24e-3 | 6.10e-2 | 2.57 | 1.85 | 0.72 |
For t10, t05 the oracle exponents (optimal/uniform 5.1, 5.6) are only upper bounds because the e-process rate there is the margin d_M − d_A. **Consequence:** the design headroom over uniform was 2.2–2.6×; P4 and P5 both captured most of it, so a ≥ 1.5× separation between them was close to impossible. The X1 negative result on H4c is therefore partly a statement about headroom, not only about the criticism target.

## 4. Approximate maximisers and confidence-set denominators (Markov and hidden-state instances)
- **EM against the true-parameter likelihood** (hidden-state instances with S ≤ 4; 10 starts; training 500 or 5000 episodes): **50/80** starts end below the true-parameter likelihood by > 0.5 nats at a 60-iteration budget; **12/80** at 300 iterations; the worst shortfall is 132 nats at 5000 episodes/60 iterations. A denominator from such a start is not an upper bound on the true null likelihood, so the T6b mechanism is realistic for latent-variable nulls. (The type-I rate of an e-process built on these denominators was **not** measured — H-E.)
- **Confidence-set denominator** (CP-box on independent training data; Markov instances; 1500 test episodes; α = α₁ = 0.05; `em_cs_dev.md`):
| training policy | training episodes | unchanged kernel | change in action-2 rows |
|---|---|---|---|
| narrow (p(a=2)=0.02) | 100 | 0/20 | 0/20 |
| narrow | 1000 | 0/20 | 3/20 |
| narrow | 10 000 | 0/20 | 20/20 |
| uniform | 100 | 0/20 | 11/20 |
| uniform | 1000 | 0/20 | 19/20 |
| uniform | 10 000 | 0/20 | 20/20 |
Type-I 0/120. Power requires training that covers the changed contexts: with narrow training and 100 episodes the box for action-2 contexts is [0, 1] (vacuous, 0/20). **Caveat (A4):** CP boxes are fixed-n intervals applied to data-dependent counts, so coverage is not guaranteed by theory; E6′ uses LR confidence sequences.

## 5. Target trade-off (exact; `tradeoff_dev.md`)
As the probability q of the revealing action goes 0 → 1: adequacy exponent 0 → 4.4×10⁻² (37×); member-identification exponent 1.18×10⁻³ → 0.99×10⁻³ (−17 %). The targets are almost non-conflicting here; identifying a member is ≈ 40× slower than detecting a gross inadequacy.

## 6. Independence of generators, determinism, feasibility
Independent hmm draws: mean pairwise KL 0.63 vs 0.013 for jitters; order-1 plateau spans 2.4×10⁻³–3.4×10⁻² (14×); S ∈ {3,…,6}; mixing (slem) 0.09–0.27 over the first four instances. Re-run determinism 30/30. Costs per run: see `05-…` §7.

## 7. What the development phase did not show
No type-I certification (too few runs); no clustering-aware inference; no GRU or ensemble; no learned HMM null inside a sequential test (only the EM likelihood gap); no reset-variant experiment beyond the exact R2/R4 checks; no evidence on non-toy environments.
