---
id: topic-bostrom-world-models-phase9-audit
title: "Phase 9 mathematical audit: statements, proofs, verification, classification, errors found"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-04
tags: [audit, proofs, errors]
---

# Mathematical audit (Phase 9)

**Independence caveat.** Same-agent audit; "independent verification" means a separate implementation or exhaustive enumeration, not an external person. Source files: `src/eid/phase9_audit.py`, `src/eid/e6proc.py`, `tests/test_phase9_audit.py`, `tests/test_e6proc.py`, `results/phase9_dev/`.
Classification: **T** established theorem (known, elementary proof given); **C** straightforward corollary; **R** restricted instance; **E** empirical observation; **U** unresolved conjecture. "Closest known" names what I actually read (level in `03-…`) or marks `[memory]`.

## 1. Errors and corrections discovered in this audit
| # | Where | Error | Severity | Correction |
|---|---|---|---|---|
| A1 | Phase 8 T4 "counterexample", T6a, T6b, negative-results #18, hypothesis registry | Rejections under an **out-of-class truth** were called "false alarms" / "invalid"/"fails". With the formal nulls (Markov-in-context for E_stat; the simple null "environment = p̂" for the frozen test; the searched subclass for the approximate maximiser) those truths lie **outside the null**, so a rejection is a correct rejection of a false null, not a type-I error. What is wrong is the *interpretation* ("mechanism changed"). | **Major (semantic)** | Three-way separation in `02-…`: formal type-I / misspecification / false attribution. Phase 8 files preserved; erratum appended. |
| A2 | Phase 8 T4′ evidence, "0/100 in S4, S5 shows robustness with resets" | With a hidden-state truth the Markov-in-context null is false; absence of rejection is **low power**, not robustness. Dev run: E_ctx 0/30 in H1, H2, H5 (null false) and 0/30 for E_ep and E_comp in nearly all cells. | **Major** | Claim withdrawn; only in-class validity is claimed for E_ctx. |
| A3 | Phase 8 T5 (Bayesian-Occam dissociation) | Stated as "identification of the true mechanism decreases while prediction improves". True only at the **non-generic** truth ψ₀ = ½. For any fixed ψ₀ ≠ ½ identification recovers; the dissociation is a **window** of length ≈ c/(ψ₀ − ½)² (exact table). Generic identifiability of HMM parameters up to label swapping (Allman–Matias–Rhodes Thm 6; Petrie) says exactly this kind of coincidence is non-generic. | **Major** | Restated as local-alternative window; table below. |
| A4 | Phase 8 T6d (confidence-set repair) | Assumptions were not stated: (i) training data independent of test data; (ii) coverage **on all test-relevant contexts** — a context unseen in training forces the set to be vacuous (verified: no power); (iii) adaptive training requires a **time-uniform** (adaptive-valid) set, not a fixed-n Clopper–Pearson box; the dev implementation uses fixed-n CP boxes with data-dependent counts, so its coverage is **not guaranteed** (empirically 0/120 type-I). | Minor–Major | Assumptions stated; implementation flagged as non-rigorous; E6 design uses LR confidence sequences (Emmenegger et al. Thm 1) instead. |
| A5 | Prop 5 | Rejection-event bound P₁(R)/P₀(R) ≤ 1 + τ/α uses P₀(R) = α. For a **conservative** test (size < α; e.g. the X1 e-process, 1.7 %) it must use the exact size. | Minor | Scope note; no earlier numeric claim depends on it. |
| A6 | E6 analysis plan (Phase 8) | Rate claims used "CP upper bound ≤ 0.07" per cell. (a) 0.07 is not the nominal 0.05 (it demonstrates a weaker claim); (b) 24 cells without multiplicity control; (c) pooled run-level CP **undercovers under clustering** (coverage 0.81 at ICC 0.2); (d) 20 runs per structure cannot certify any per-structure bound ≤ 0.13; (e) 30 structures give cluster-interval coverage 0.85–0.89 at ICC 0.2. | **Major (design)** | Corrected plan in `06-…`. |
| A7 | PO-2 (Wald, adaptive designs) | Listed as open. | – | **PROVED** (below). |
| A8 | T4′ statement | "Null: o_t | x_t has a time-invariant law" is imprecise. The proof needs the **conditional law given the entire past** to equal ν(·|x_t). | Minor | Restated (Prop B). |
| A9 | X1 effect-size design (preregistered 1.5×) | Not a mathematical error: the Chernoff-optimal gain over uniform design is 2.2–2.6× on anticipated truths and the observed gains are 72–93 % of it. A ≥ 1.5× separation of two *near-optimal* designs was nearly unreachable; the threshold should be normalised to the optimal exponent. | Design | Used in E6 design. |
| A10 | X1 H1 text | "supported" meant per-cell 95 % upper bounds ≤ 0.07. Re-evaluated: max per-cell bound 0.0442 (≤ 0.05); at Bonferroni level 0.05/24 the max is 0.0558 (> 0.05, ≤ 0.07). So "no violation up to 0.07, FWER-adjusted" is supported; "all 24 cells ≤ 0.05 at FWER 5 %" is **not** demonstrated. | Minor | Stated precisely; X1 record unchanged. |
No earlier proposition was refuted by the audit; the corrections concern interpretation, scope, assumptions and design.

## 2. Audit register
| ID | Exact statement (compressed) | Assumptions and quantifiers | Proof / verification | Class | Closest known | Fails when |
|---|---|---|---|---|---|---|
| P1 | E ≈ E′ ⇔ same reachable histories and equal kernels on them | ∀ policies, finite A, O, every finite T | proof in `formal-framework.md`; `test_propositions` (36 cases) + new exact split-state equality (`test_time_varying…`) | T | trace/bisimulation equivalence (Castro et al.; Armstrong — abstract); PSR `[memory]` | continuous spaces (O1); equality only on reachable histories |
| P1′ | E ≈_Π E′ ⇔ kernels agree on Π-reachable (h, a) | Π closed under the steering policies used | same proof; `test_class_relative_equivalence`; X1 barrier (H2: ≤ 2.2 % rejection) | T | same | Π not closed under steering |
| P2 | min(α+β) = 1 − TV; KL chain rule E Σδ_t; TV ≤ √(KL/2) | any policy incl. adaptive | **new independent enumeration** of an adaptive policy: |KL − chain| < 10⁻¹² (`test_chain_rule…`) | T | Neyman–Pearson, Pinsker `[memory]`; Chernoff/Naghshvar–Javidi `[memory]` | KL infinite (bound vacuous but true) |
| P3(a) | KL(P_E0^π‖P_E1^π) ≤ Σ c^t ε_t if π ≤ cμ | finite spaces; c ≥ 1 | proof; 129 audit cases | T | change of measure / simulation lemma `[memory]` | c unbounded; tightness open (O3) |
| P3(b) | no bound without coverage | ∀ε, M ∃ E0, E1, μ, π | explicit Bernoulli construction | T | standard | – |
| P4 | P(S|D) = Σ_k ν(S|κ=k) λ_D(k) | countable mechanism set; D depends on m only through κ(m) | tower property | T | – | agent's policy depends on m |
| P5 | |P₁(N) − P₀(N)| ≤ TV | simple hypotheses; **exact** size α for the rejection-event ratio | definition of TV | T | – | composite claim; conservative tests (A5) |
| P6 | P_E0(R) ≤ α + TV(P_E0, P_Q) | level-α under Q | event bound | T | – | – |
| P7a | AUROC ≤ ½ + TV | any score; ties ½ | proof; tie tests | T | Neyman–Pearson | – |
| P7b,c | cross-entropy identity; inversion example | finite quantities | identity; example | T/R | likelihood inversion in generative models (Nalisnick et al. — abstract) | – |
| P8 | posterior concentration/absorption | finite M, i.i.d. episodes, prior full support, test episodes independent of adaptation | proof; tests | T | Doob/Berk `[memory]` | infinite classes (O1) |
| P9 | (a) no gain without state dependence; (b) adaptivity doubles TV in an example | exhaustive 2-step | enumeration | T/R | – | other criteria |
| P10 | EIG over a class is blind where members agree; myopic EIG + catch-all does not explore; two-step does | finite exact DP, T = 40 | `test_proposition10_exact` | R | Catanach–Das (EGIG/EDI — read), BOED misspecification literature (abstracts) | other priors/horizons |
| Cor. | E[τ] ≥ ln ω/KL (i.i.d. episodes) | E[τ] < ∞ | Wald; test | T | Wald `[memory]` | adaptive designs: see PO-2 |
| PO-2 | **Adaptive** version: E[τ] ≥ ln ω / δ_max, δ_max = sup_{h,a} KL(p₀(·|h,a)‖p₁(·|h,a)) | predictable adaptive design, E[τ] < ∞, δ_max < ∞ | S_t = Σ log LR; M_t = S_t − Σ_{s≤t} (−δ_s) is a martingale; optional stopping gives E[Σ_{s≤τ} δ_s] = −E[S_τ] ≥ ln ω; δ_s ≤ δ_max. Monte-Carlo sanity test | T (corollary of optional stopping) | Wald's identity `[memory]` | δ_max = ∞ (vacuous) |
| X1-V | E_t = q(D_t)/max_{m∈M} p_m(D_t) is anytime valid under adaptive predictable policies | truth ∈ M **with the same interaction protocol (reset)**; q predictable, normalised; denominator exact | proof (D1 §1); exhaustive tree enumeration (3 deterministic adaptive rules) | **C** of Emmenegger et al. Thm 1 and Wasserman et al. Thm 9/11 | **read**: Emmenegger–Mutný–Krause Thm 1 (adaptive x_s, θ̂_s, supermartingale R_t, Ville); Wasserman et al. Thm 9–11 | denominator < true likelihood (approximate maximiser); truth ∉ M; imperfect resets (truth ∉ M) |
| X1-V′ | optional stopping / continuation | – | Ville | T | same | – |
| T3 | β ≤ α + √(½ n ε) | any test, adaptive design, KL_π(E‖m) ≤ ε per episode | Pinsker + chain rule | T | Le Cam `[memory]` | – |
| T4 | finite-horizon time-varying kernel ≡ stationary POMDP with counter | finite T | exact check (2.8×10⁻¹⁷); Choi et al. (read: "HM-MDP is a subclass of POMDP") | T | Choi–Yeung–Zhang 1999 | – |
| T4′ → Prop B | E_ctx valid when the **conditional law of o_t given the entire past equals ν(·|x_t)**, ν time-invariant | predictable x_t; policy predictable | proof (martingale + Ville); `test_generic…`, dev 0/90 in null-true cells | C | Wasserman et al. §8; Shin–Ramdas–Rinaldo Def 2.2 (read) | hidden-state truth (null false); persistent regime |
| T5 | Occam window | see A3 | exact table (`occam_offset`); independent implementation agrees with Phase 8 at ψ₀ = ½ to 10⁻⁹ | R | Jeffreys–Lindley (snippets); Allman et al. Thm 6 (read) | generic truths: recovers |
| T6d | LR/CS-set denominator gives type-I ≤ α + α₁ | A4 assumptions | proof; dev 0/120 type-I; vacuity verified | C | Emmenegger et al. Thm 1; Wasserman et al. | A4 |
| Prop C | E_ep: episode-level changepoint e-process valid for **every** stationary hidden-state generator with perfect resets | episodes independent given action sequences | Prop A on the categorical episode model; `test_episode_level…` (0/12) + dev | C | Shin et al. (P = i.i.d. class, composite) | resets imperfect; regime persists |
| Prop D | E_comp: predictive-comparison confidence sequence valid under **arbitrary dependence/misspecification** | predictable forecasts; bounded score; null Σ E[Δ|F] ≤ 0 | Robbins normal-mixture supermartingale + Hoeffding's lemma (derivation in `04-…`); MC test with dependent noise (0/300) | C | Choe–Ramdas; Henzi–Ziegel; Arnold et al. (abstract/intro read) | forecasts not predictable; comparator chosen post hoc |

## 3. Occam window: exact values (A3)
E[P(true mechanism m₂ | D_n)] for truth m₂ at ψ₀ (m₁ = Bernoulli(½); m₂: ψ ~ U(0,1)):
| n | ψ₀ = 0.50 | 0.52 | 0.55 | 0.60 |
|---|---|---|---|---|
| 10 | 0.374 | 0.375 | 0.383 | 0.410 |
| 100 | 0.186 | 0.200 | 0.275 | 0.521 |
| 300 | 0.124 | 0.161 | 0.361 | 0.846 |
| 1000 | 0.077 | 0.181 | 0.714 | 0.999 |
| 3000 | 0.048 | 0.340 | 0.991 | 1.000 |
| 10 000 | 0.029 | 0.825 | 1.000 | 1.000 |
Only ψ₀ = ½ decays forever (∝ n^{-1/2}); every other truth passes through a minimum and recovers.

## 4. What survives independent audit
- X1-V (adaptive validity), the barrier, the Chernoff-normalised reading of X1 results, T3, T4 (absorption), T6d (with assumptions), PO-2, Props 1–10 (with the Prop 5 scope note).
- Reduced to known results: X1-V, T4′/Prop B, Prop C, Prop D, T6d, T3, T4.
- No new theorem is claimed.
