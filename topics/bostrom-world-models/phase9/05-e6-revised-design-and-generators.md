---
id: topic-bostrom-world-models-phase9-e6
title: "Revised E6 design (E6′) and independent environment-generator specification"
topic: bostrom-world-models
type: note
status: proposal
created: 2026-11-04
tags: [E6, design, generators]
---

# E6′: what survives of the E6 validity map, and what the experiment should be

## 1. Reassessment (Gate G7 first)
The Phase 8 E6 proposed to "map validity". The audit shows that **most of the validity map is settled by theory**: each procedure is valid exactly when the truth lies in its formal null (Props A–D); rejections outside the null are misspecification; a frozen estimated null tests a simple null; approximate maximisers test a smaller class. Running a 90-structure grid to confirm "validity holds iff the null is true" would mostly confirm known facts (A-class). The preregistered question would not be informative on a positive outcome and nearly uninformative on a negative one (a violation would be a bug, not a finding).
**What remains empirically open — and informative either way — is the price of validity under model uncertainty**: how much detection power an embedded learned observer must give up to keep a guarantee when its class may be wrong. Dev evidence: the only procedure with power at N = 3000 (E_ctx) has a null that fails for hidden-state truths (power 5/30 where it matters), while the procedures valid under any hidden-state generator (E_ep, E_comp) had **zero** rejections at N = 3000 even for a large kernel change (0/30). This is a *robustness–power frontier*; quantifying it across independent generators is the proposed experiment.

## 2. E6′ hypotheses (proposals; not frozen)
| ID | Hypothesis | Falsified if |
|---|---|---|
| H-A (null ladder) | Along a ladder of nested nulls — saturated episode model (27×81 cells) ⊃ coarse episode model (action-count × observation histogram, 5×15) ⊃ order-2 ⊃ order-1 contexts — the sample size needed to detect a fixed kernel change **decreases** as the null shrinks, and adjacent rungs differ by a factor within ×3 of the parameter-count ratio (regret scaling) | non-monotone, or ratio off by more than ×3, in ≥ 30 % of structures |
| H-B (validity) | Every (procedure, structure) cell whose formal null is true has type-I ≤ 0.05 | any family with cluster-level lower bound > 0.05 (a bug or a proof error) |
| H-C (false attribution) | For restricted-kernel procedures, the rate of "rejection with an unchanged generator" is ≤ 0.05 under episodic resets of both state and regime, and > 0.5 when the regime dwell time exceeds the checkpoint span | outside these bounds in the pre-specified families |
| H-D (learned null with certified denominator) | An LR-confidence-sequence denominator built from independent training data retains ≥ 50 % of the oracle log-odds growth when training covers the probed contexts and n_train ≥ 10⁴, and has no power on contexts absent from training | retained fraction < 50 % at full coverage, or power on uncovered contexts |
| H-E (approximate maximiser) | The type-I error of an e-process whose denominator comes from multi-start EM exceeds 0.05 in ≥ 50 % of structures at a 60-iteration budget and in ≥ 10 % at 300 iterations (consistent with the 62 %/15 % of starts below the true likelihood measured in dev; the type-I effect itself has **not** been measured yet) | fractions below these |
| H-F (observer disagreement) *(optional stage 2)* | Bootstrap-ensemble disagreement tracks the exact epistemic gap on fully observed Markov environments, and does not track class inadequacy on hidden-state environments | disagreement tracks both, or neither |
Effect sizes are normalised to the **Chernoff-optimal exponent** of the same truth–null pair (Prop E), not to an arbitrary multiple.

## 3. Observer variants and what each tests
| Observer | Why it is in the design |
|---|---|
| Exact likelihood oracle (X1 e-process) | diagnostic upper bound (oracle exponent); never counted as an embedded observer |
| Count-based Markov learner, orders 1–2 | closed-form likelihoods; tests H-A, H-C, H-D without optimisation error |
| Learned IO-HMM (EM, small S) | tests H-E (optimisation gap) and the cost of learning a latent null |
| Bootstrap ensemble of count learners | tests H-F only; ensemble disagreement is **not** assumed to measure epistemic uncertainty |
| Confidence-set / robust sequential procedure (LR confidence sequence) | the certified-denominator repair for H-D |
| GRU world model (exists from Phase 5) | **deferred**: would test whether H-E transfers to a neural null; added only if H-E is supported for HMMs |
No transformer. Neural models are not added for complexity.

## 4. Controls (all with experimenter-side exact flags)
well-specified stationary nulls (M1); misspecified but physically stationary (H1, H5); pure policy shift (M2, H2); genuine mechanism change with and without coverage (M3, M4, H3, H4); latent-context shift; observationally equivalent mechanisms (H5, bisimilar twin; TV = 0); no-discriminating-intervention runs (M4, H4); explicit reset variants (observation, memory, state, regime, full — R1–R5); coverage-limited vs high-coverage training for learned nulls.
**Matching.** Predictive difficulty is matched through the experimenter-side descriptor "order-1 plateau" (exact), and budgets (N, T, policy mixture) are common to all procedures. No procedure sees the alternative's identity; E_comp and the ladder rungs use comparators declared before data.

## 5. Independent environment generators (specification; `src/eid/e6gen.py`)
Interface constraints (stated limitation): 3 actions, 3 observation symbols, episodic T = 4 (so exact enumeration is available). Everything else is sampled per instance from `SeedSequence([9000, family, index])`.
| Family | Structure sampled per instance | Experimenter-side descriptors (never given to the observer) |
|---|---|---|
| `markov` | transition rows ~ Dirichlet(c) with c log-uniform in [0.2, 3]; random initial law | concentration |
| `hmm` | S ∈ {3,…,6}; T rows ~ Dirichlet(c_T), emission rows ~ Dirichlet(c_Z), c's log-uniform in [0.2, 2]; random b₀ | S, c_T, c_Z, exact order-1 misspecification plateau (2.4×10⁻³–3.4×10⁻² nats/episode over the first 10 instances), second-largest eigenvalue modulus of mean T, mean row entropy |
| `controlled` | an hmm instance whose designated action sends each hidden state to a fixed partner state | revealing action |
| `regime` | two independently drawn hmm kernels K₀, K₁; regime flips between episodes with probability ε log-uniform in [10⁻³, 0.2] | ε |
| `changing` | an hmm instance and a second kernel with the rows of one random action redrawn | changed action |
| `equivalent_pair` | an hmm instance and its bisimilar state-split twin (S+1 states) | exact TV = 0 (tested) |
**Independence audit** (`tests/test_e6gen.py`, dev): mean pairwise KL between observation laws of independent `hmm` draws = **0.63** nats vs **0.013** for the jittered copies of the single hand-built POMDP used in X1 (≈ 50×). Seed namespace 9000 does not intersect any earlier seed (200, 300–311, 400–405, 500–505, 600–629) nor the reserved E6 ranges (700–719, 800–829).

## 6. What is known to whom
Experimenter: the generator, the exact law, the descriptors, the flags (null true? mechanism changed? kernel changed?). Observer: its own actions and observations; for variants V-c (observed context) and V-r (reset semantics) the extra information is stated per variant. No observer receives labels or likelihoods of the true generator, except the oracle diagnostic.

## 7. Computational budget (measured in dev, seconds per run, N = 3000 episodes)
E_ctx 0.05; E_comp (two comparators) 0.07; **E_ep 3.3** (naive implementation; needs incremental statistics before a 3600-run cell is feasible); CS-repair 0.2–0.3; multi-start EM, 10 starts: 0.1–12 s depending on budget and size.

## 8. Not yet resolved before a preregistration can be frozen
(i) the LR-confidence-sequence implementation for H-D (the dev CP-box version does not control coverage for data-dependent counts, A4); (ii) a fast E_ep; (iii) a dev measurement of the EM-denominator type-I (H-E); (iv) read Choe–Ramdas / Henzi–Ziegel / Chernoff (Prop D, Prop E are reduced to sources not read); (v) external design review.
