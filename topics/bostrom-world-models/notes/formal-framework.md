---
id: topic-bostrom-world-models-formal-framework
title: "Formal framework, propositions and proofs"
topic: bostrom-world-models
type: notes
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [formal, proofs]
---

## Formal framework, propositions and proofs

Provenance labels: **Known** (standard result, cited and not claimed); **Elementary** (short proof from standard facts; no novelty claimed as a theorem); **Obligation** (not proved). The finite cases are checked numerically in `implementations/epistemic-identifiability/tests/test_propositions.py` by exact enumeration. That is a sanity check, not a proof.

### 1. Problem statement

Fix finite action set A and finite observation set O (continuous spaces: see obligation O1). A history of length t is h_t = (a_1, o_1, …, a_t, o_t). An **environment** E is a family of kernels p_E(· | h_{t-1}, a_t) over O. A **policy** π gives probabilities π(· | h_{t-1}) over A. Together they induce a law P_E^π on T-step histories:

P_E^π(h_T) = ∏_{t≤T} π(a_t | h_{t-1}) · p_E(o_t | h_{t-1}, a_t).

An embedded agent observes only histories and chooses π (possibly adaptively, which is already covered by history-dependence). Let E0 be the reference environment and E1 a learned world model, both with the same A and O.

**Detection problem.** H0: the history is drawn from P_{E0}^π. H1: from P_{E1}^π. The agent chooses π and a test φ: H_T → {0,1} (reject H0 if 1) with size α = P_{E0}^π(φ=1) and type-II error β = P_{E1}^π(φ=0).

A **mechanism** is any implementation m (a POMDP with latent state, a program, a neural network plus sampler) with an observable kernel κ(m), the environment it presents to an agent. S ⊂ M is a predicate on mechanisms ("simulated"); it is not a property of κ(m).

### 2. Propositions

**Definition (observational equivalence).** E ≈ E′ iff P_E^π = P_{E′}^π for every T and every policy π.

**Proposition 1 (kernel characterisation). Known in spirit; Elementary proof.** Call h_{t-1} *reachable* in E if q_E(h_{t-1}) := ∏_{s<t} p_E(o_s | h_{s-1}, a_s) > 0. Then E ≈ E′ iff E and E′ have the same reachable histories and p_E(· | h, a) = p_{E′}(· | h, a) for every reachable h and every a.

*Proof.* (⇐) By induction on T, using the product formula: P_E^π(h_T) = P_E^π(h_{T-1}) · π(a_T | h_{T-1}) p_E(o_T | h_{T-1}, a_T); equal prefixes and kernels (on reachable prefixes; unreachable prefixes have probability 0 under both) give equal laws.
(⇒) Let h = (a_1,o_1,…,a_{t-1},o_{t-1}) and let π_{h,a} be the deterministic policy that plays a_1,…,a_{t-1} along h and then a. Then P_E^{π_{h,a}}(h, a, o) = q_E(h) p_E(o | h, a). Equality with E′ for all o gives q_E(h) = q_{E′}(h) (sum over o), so the reachable sets coincide, and for q_E(h) > 0 dividing gives equal kernels. ∎

Relation to the literature: this is the statement that a controlled process is identified by its conditional kernels. Its relation to Armstrong's (2018) "equivalent" and "counterfactually equivalent" POMDPs and to trace equivalence (Castro et al. 2009) must be checked against the full texts; I read only abstracts (obligation O4). Predictive-state and observable-operator representations are the relevant adjacent literature and are unverified.

**Corollary 1 (mechanism non-identifiability). Elementary.** If κ(m) = κ(m′), no policy and no test distinguishes m from m′. In particular, if S contains m and not m′, no observation-based test separates them.

**Proposition 2 (limits of distinguishability). Known (Neyman–Pearson/Le Cam; chain rule; Pinsker).** For fixed π and T:
(a) min over tests of (α + β) = 1 − TV(P_{E0}^π, P_{E1}^π).
(b) KL(P_{E0}^π ‖ P_{E1}^π) = E_{P_{E0}^π} Σ_t δ_t(h_{t-1}, a_t), where δ_t(h,a) = KL(p_{E0}(·|h,a) ‖ p_{E1}(·|h,a)).
(c) TV ≤ √(KL/2), for KL in either direction. Hence a test with α, β ≤ δ < 1/2 requires TV ≥ 1 − 2δ and therefore KL ≥ 2(1 − 2δ)².
Active choice of π can improve the sequential-testing error exponent (Chernoff; Naghshvar and Javidi 2013). Not claimed as new.

**Proposition 3 (interventional coverage). Elementary; the application is the point.** Let μ be a training policy and ε_t := E_{d_t^μ}[δ_t], where d_t^π(h,a) := P_{E0}^π(H_{t-1} = h, A_t = a).
(a) If π(a|h) ≤ c·μ(a|h) for all h, a (c ≥ 1), then KL(P_{E0}^π ‖ P_{E1}^π) ≤ Σ_{t≤T} c^t ε_t.
(b) For every ε > 0 and M > 0 there exist E0, E1, μ and π with ε_1 ≤ ε and KL(P_{E0}^π ‖ P_{E1}^π) ≥ M. So no bound in terms of in-distribution error alone holds without a coverage condition such as the one in (a).

*Proof.* (a) d_t^π(h,a) = ∏_{s<t} π(a_s|h_{s-1}) p_{E0}(o_s|h_{s-1},a_s) · π(a|h) ≤ c^t ∏_{s<t} μ(a_s|h_{s-1}) p_{E0}(o_s|h_{s-1},a_s) · μ(a|h) = c^t d_t^μ(h,a), the E0 kernel factors being common. Since δ_t ≥ 0, Σ d_t^π δ_t ≤ c^t Σ d_t^μ δ_t = c^t ε_t. Sum over t and use Proposition 2(b). (If E1 gives probability 0 to an observation that E0 can produce at a history in the support of d_t^π, then δ_t = ∞ there; the same inequality then forces ε_t = ∞, so the statement remains true and vacuous.)
(b) Take T = 1, A = O = {0,1}. E0: p(o=1|a) = 1/2 for both actions. E1: same for a=0; p(o=1 | a=1) = q. Let k(q) := KL(Ber(1/2) ‖ Ber(q)) = ½ ln(1/(2q)) + ½ ln(1/(2(1−q))), which tends to ∞ as q → 0. Choose q with k(q) ≥ M. Let μ play a=1 with probability w := min(1, ε/k(q)) and π play a=1 with probability 1. Then ε_1 = w k(q) ≤ ε and KL under π equals k(q) ≥ M. For T > 1, pad with identical kernels. ∎

Remark: the bound in (a) grows geometrically in T when c > 1; I do not know whether this is tight (obligation O3). Part (a) is a change-of-measure argument of the kind used in simulation-lemma and compounding-error analyses (sources to be verified before citing).

**Proposition 4 (evidence screens off only the kernel). Elementary.** Let ν be a prior on a countable mechanism set M, D the observed history under π, and assume the likelihood of D depends on m only through κ(m). Then
P(S | D) = Σ_k ν(S | κ = k) · λ_D(k),
where λ_D is the posterior over kernels. In particular, if ν(S | κ = k) is the same constant c for all k, then P(S | D) = c for every D.

*Proof.* D is independent of m given κ(m), so P(S | D) = Σ_k P(S | κ=k, D) λ_D(k) = Σ_k P(S | κ=k) λ_D(k). ∎ (General measurable spaces need regular conditional probabilities; obligation O1.)

Reading: data move credence in "simulated" only through how the prior links observable signatures to simulation status (the *artifact premise*). That link is not supplied by the data.

**Proposition 5 (bounded evidential force of one test outcome). Elementary.** Here S denotes the *fidelity-indexed* simple hypothesis "the environment is E1" (a particular simulator with a particular kernel), against ¬S: "the environment is E0". It does not apply to the unrestricted, composite claim "the world is some simulation", for which no such bound exists (see Proposition 4). Let τ = TV(P_{E0}^π, P_{E1}^π), and let N be the non-rejection event with P_{E0}(N) = 1 − α. Then
|P_{E1}(N) − P_{E0}(N)| ≤ τ, so P_{E1}(N)/P_{E0}(N) ∈ [1 − τ/(1−α), 1 + τ/(1−α)],
and for the rejection event R, P_{E1}(R)/P_{E0}(R) ≤ 1 + τ/α. By Proposition 2(c), τ ≤ √(KL/2).

*Proof.* For any event A, |P_{E1}(A) − P_{E0}(A)| ≤ TV by definition; divide by P_{E0}(N) = 1−α or P_{E0}(R) = α. ∎

Reading: when the simulator is faithful under the interventions the agent can perform (τ small), a null result carries almost no evidence against S, and this holds for every test, not just the one used.

**Proposition 6 (agent-side misspecification inflates false alarms). Elementary.** Let the agent test against its own model Q (null law P_Q^π) with a level-α test, P_Q^π(R) ≤ α, while the environment is E0. Then P_{E0}^π(R) ≤ α + TV(P_{E0}^π, P_Q^π).

*Proof.* Same event bound. ∎

Reading: a rejection is a statement about the pair (environment, agent's theory). With out-of-distribution interventions TV(P_{E0}, P_Q) grows (Proposition 3(b) applies to Q as well), so false positives against a perfectly faithful environment are expected. The experiment measures this.

### 3. What is and is not claimed

- No new theorem about active hypothesis testing is claimed.
- Propositions 3–6 are elementary; their value is that, together, they turn the philosophical claims (see `philosophical-analysis.md`) into precise statements about what detection can license.
- A reviewer may reasonably regard the mathematics as a careful framing rather than a contribution. The assessment in `reviews/` addresses this.

### 4. Open proof obligations

| Id | Obligation |
|---|---|
| O1 | Extend Propositions 1, 3, 4 to continuous spaces (measurability, absolute continuity, regular conditional probabilities). |
| O2 | Connect ε_t to a generalisation guarantee for a learned model class (not attempted). |
| O3 | Tightness of the c^t factor in Proposition 3(a): find a lower-bound construction or a better bound. |
| O4 | Verify Proposition 1 against Armstrong (2018) and Castro et al. (2009) full texts and the predictive-state/observable-operator literature; update provenance labels. |
| O5 | Composite-null and adaptive-sequential version of Proposition 5 (optional stopping, unknown E0), citing Wald and Chernoff after verifying the sources. |


### 5. Review of correctness, originality and dependence (Phase 3)

Each proposition was re-derived from its statement, its edge cases were checked (infinite KL, unreachable histories, deterministic versus randomised policies, simple versus composite hypotheses), and the finite cases were checked numerically by exact enumeration (`tests/test_propositions.py`, 36 parametrised cases).

| Prop. | Correct as stated? | Originality | Depends on | Change made |
|---|---|---|---|---|
| 1 | Yes. The reverse direction needs the deterministic steering policy and the equality of prefix probabilities, which the proof supplies. Unreachable histories are unconstrained, as stated. | Known in spirit (a controlled process is identified by its conditional kernels; adjacent to observable-operator and predictive-state equivalence, and to Armstrong's equivalence). Not claimed. | Product formula for histories. | None. |
| 2 | Yes. (c) holds in either KL direction; the necessity bound uses TV ≥ 1 − 2δ. | Known (Neyman–Pearson, Le Cam, Pinsker, chain rule). | Standard results; the numerical test checks all four relations on random finite processes. | Clarified the KL direction and the step TV ≥ 1 − 2δ. |
| 3(a) | Yes. The occupancy ratio is c^t because t policy factors appear (t − 1 earlier steps plus the current action). | Elementary change of measure of the kind used in simulation-lemma and compounding-error arguments (sources unverified); not new. Tightness open. | δ_t ≥ 0; chain rule. | Added the infinite-KL remark. |
| 3(b) | Yes. For T > 1 the padding steps contribute zero. The test uses q = ¼e^(−2M), for which k(q) ≥ M (the second logarithm is at least −½ ln 2). | Elementary; the "no bound without coverage" message is standard in distribution-shift analyses. | Explicit Bernoulli KL. | None. |
| 4 | Yes for countable M. Requires that D depend on m only through κ(m), which holds by the definition of κ for any (possibly adaptive) policy. | Elementary conditional independence. Close in spirit to Chalmers's defeat argument by indifference (read in full); the formal statement is not claimed as new. | Tower property. | None. |
| 5 | Yes, but only for the simple hypothesis E1 against E0. The earlier wording could be read as covering "simulation" in general. | Elementary (definition of TV). | |P(A) − Q(A)| ≤ TV. | Wording restricted to the fidelity-indexed simple hypothesis; composite case excluded explicitly. |
| 6 | Yes. | Elementary. | Same event bound. | None. |

**Overall.** No proposition is original as a theorem. Propositions 2 and 1 are established results; Propositions 3–6 are short corollaries of the TV bound and a change of measure. Their only role is to state, precisely and with proofs, the conditions under which each of the three inferences (discrepancy, mechanism, simulation) is warranted. A mathematically trained referee will not regard them as a contribution in themselves.

### 6. New remark: connection to Armstrong (2018), not yet verified

Armstrong's abstract states that any POMDP is counterfactually equivalent, for any finite number of turns, to a deterministic POMDP with all uncertainty in the initial state. A computer simulation driven by a pseudorandom generator seeded once is such a deterministic process. If the statement carries over as the abstract suggests, then "stochastic world" and "deterministic simulation with a random seed" are indistinguishable over finite horizons by any observer. I have read only the abstract; the precise definitions and the range of the result (finite horizon, finite spaces) must be checked in the full text before the remark is used (obligation O4).


## Phase 4 additions: observer model quality, adaptation, active selection

All proofs below are complete for the stated finite settings. Exact-enumeration checks are in `tests/test_propositions_phase4.py` (37 cases). **None of the statements is claimed as a new theorem**; provenance is given for each. "I have not found this exact statement in the sources I read" is not evidence of novelty, and each statement is elementary enough to be known.

Notation as in section 1. P_i := P_{E_i}^π. For a score s of the history, AUROC(s) := P(s(X_1) > s(X_0)) + ½ P(s(X_1) = s(X_0)) with X_0 ~ P_0 and X_1 ~ P_1 independent.

### Proposition 7 (observer-relative separation). Elementary.

(a) *Ceiling.* For every score s, AUROC(s) ≤ ½ + TV(P_0, P_1). The likelihood-ratio ordering attains the maximum AUROC over all scores.

(b) *Cross-entropy identity.* For the observer's theory Q (a history law) and the anomaly score s_Q(h) = −log Q(h), when the quantities are finite,
E_{P_1}[s_Q] − E_{P_0}[s_Q] = [H(P_1) − H(P_0)] + [KL(P_1‖Q) − KL(P_0‖Q)].

(c) *Inversion.* There exist E_0, E_1 with TV(P_0, P_1) = 1 and a theory Q such that AUROC(s_Q) = 0 for E_1 as the positive class, while the likelihood-ratio score has AUROC 1.

*Proof.* (a) Break ties with independent uniform noise added to the score; this leaves AUROC (with the ½-tie convention) unchanged and makes the score distributions continuous, with CDFs F_0, F_1. Then AUROC = ∫ F_0 dF_1 and ∫ F_1 dF_1 = ½, so AUROC − ½ = ∫ (F_0 − F_1) dF_1 ≤ sup_t |F_0(t) − F_1(t)| ≤ TV of the score laws ≤ TV(P_0, P_1) (data processing). The statement about the likelihood-ratio ordering is the Neyman–Pearson lemma applied at every false-positive rate (its ROC curve dominates every other ROC curve pointwise, hence in area).
(b) E_P[−log Q] = H(P) + KL(P‖Q); subtract the two instances.
(c) Let E_0 deliver the observation 0 with probability 1 and E_1 the observation 1, so TV = 1; let Q = E_1. Then s_Q = 0 on E_1 histories and +∞ on E_0 histories, so the E_1 score never exceeds the E_0 score: AUROC(s_Q) = 0. ∎

*Remarks.* The bound ½ + TV/2 is false (a three-outcome counterexample is in the tests), so (a) cannot be tightened to that form. Part (b) says that, up to the entropy offset, **whichever of the two environments is closer in cross-entropy to the observer's theory looks less anomalous**; detecting E_1 requires E_1 to be farther from the theory than reality E_0 is. This explains the direction of the experimental results (inversion when the theory is closer to W than to E_0 outside its training range; correct sign when the theory is exact or covers the range). The experimental statistic is a chi-square of standardised residuals, not −log Q, so (b) explains the direction qualitatively and does not predict the statistic exactly.

### Proposition 8 (adaptation and hypothesis classes; finite classes). Known (Doob/Schwartz consistency; Berk 1966 for misspecified classes); elementary finite proof.

Let M be a finite class of environments, ν a prior with full support, π a fixed policy, and let n i.i.d. episodes be drawn from the true environment E (possibly not in M). Write ν_n for the posterior.
(a) If E ∈ M and P_m ≠ P_E for all m ≠ E, then ν_n(E) → 1 almost surely, and (1/n) log[ν_n(m)/ν_n(E)] → −KL(P_E‖P_m).
(b) If E ∉ M and KL(P_E‖P_m) has a unique minimiser m*, then ν_n(m*) → 1 almost surely, with log-odds rate KL(P_E‖P_m) − KL(P_E‖P_{m*}).
(c) *Absorption.* Let Q_n := Σ_m ν_n(m) P_m be the posterior-predictive theory. Under (a), TV(P_E, Q_n) → 0 almost surely; hence by Proposition 6, any level-α consistency test against Q_n has asymptotic size at most α **whichever member of M is true**, and so cannot distinguish members of M. The information separating them sits in the posterior ν_n, not in the residuals.

*Proof.* By the strong law, (1/n) Σ_i log[P_m(h_i)/P_E(h_i)] → −KL(P_E‖P_m) almost surely (if P_m(h) = 0 for some h with P_E(h) > 0, then m is eliminated almost surely). The posterior log-odds of m against m′ equal the prior log-odds plus the difference of these sums, which gives the rates in (a) and (b) and the concentration statements. (c) follows because Q_n → P_E on a finite history space, and Proposition 6. ∎

*Reading.* An observer that updates on interventions in the environment under test **absorbs the anomaly**: its refreshed theory fits whatever it is facing. What it can still do is **model selection**: if both E_0 and E_1 are in its hypothesis class and are distinguishable under π, the posterior identifies which one it faces at exponent KL; if E_1 is not in its class, the posterior concentrates on the KL-closest member and only goodness of fit can reveal misspecification. Identification of a generated environment therefore depends on the hypothesis class the observer entertains. The numerical checks use a finite class on a three-outcome space, with exact posterior computation.

### Proposition 9 (active selection and distinguishability). Elementary; (b) is an existence example by exact enumeration.

(a) *No gain without state dependence.* If every kernel depends on the history only through the current action, then sup_π KL(P_0^π‖P_1^π) = T max_a KL_a, attained by the constant policy that plays the best action. Adaptivity gives no gain in KL, hence none in the Stein exponent.
(b) *Gain with state dependence.* Let A = O = {0,1}, T = 2. E_0: both observations are fair coins whatever the action. E_1: as E_0 except that the second observation is Bernoulli(½ + δ) when the second action equals the first observation. Over deterministic policies, sup TV is δ/2 for open-loop policies and δ for history-dependent policies: adaptivity strictly helps, by a factor 2.
(c) *Never hurts.* The history-dependent supremum is at least the open-loop supremum, and no policy exceeds the ceiling of Proposition 7(a).

*Proof.* (a) By the chain rule (Proposition 2(b)) KL(P_0^π‖P_1^π) = E Σ_t KL_{a_t} ≤ T max_a KL_a; the constant policy attains it. (b) The two laws differ only on histories with a_2 = o_1. Where they differ, p_1 − p_0 = ±δ on the two values of o_2, so TV = δ · P(a_2 = o_1). First observations are fair coins independent of a_1. An open-loop policy plays a_2 independently of o_1, giving P(a_2 = o_1) = ½, hence TV = δ/2. The policy a_2 = o_1 gives P = 1, hence TV = δ. (c) Inclusion. ∎

*Reading.* Active intervention helps exactly when the discrepancy is **state-dependent and observable**, so that an observation tells the observer where to look next. In the experiment, adaptive probing finds large oracle divergence (32–42 nats per step under active selection), but this advantage reaches the observer only if its theory is good enough to turn the divergence into a detection (Proposition 6, Proposition 7(b)).

### Corollary (evidence needed to overturn an indifference prior). Elementary; an application of Propositions 2, 5 and 8.

Let S be a fidelity-indexed simulation hypothesis (the environment is E_1), with prior odds ω = ν(S)/ν(¬S) against ¬S (the environment is E_0). In Bostrom's argument the indifference principle assigns credence x = f_sim to "I am in a simulation" when one lacks information distinguishing one's own experience; if (3) holds, ω can be very large. Suppose the observer then performs n independent intervention episodes under π, and E_0 is true.
(i) In expectation, ln(posterior odds of S) = ln ω − n KL(P_0‖P_1). The expected number of episodes needed to bring the odds to 1 is n* = ln ω / KL(P_0‖P_1).
(ii) No single test outcome can do it: a non-rejection has likelihood ratio at least 1 − τ/(1 − α) (Proposition 5), so one null result lowers the odds by at most that factor.

*Proof.* (i) The expected log-likelihood ratio per episode under E_0 is −KL(P_0‖P_1); exact identity checked by enumeration. (ii) Proposition 5. ∎

*Reading and limits.* This quantifies how much discriminating information it takes to defeat the *no-distinguishing-information* proviso of Bostrom's indifference principle (his text states the principle conditional on having no such information). It concerns a **specific** hypothesis S, not the composite claim "some simulation"; for the composite claim Proposition 4 applies and no such bound exists. Bostrom's own text lets simulators edit or rerun away anomalies noticed by simulated minds, which builds KL → 0 along the observer's interventions into the hypothesis, so that n* is unbounded. The corollary is a statement about the argument's applicability condition, not about the trilemma.

### Review of the six original propositions after Phase 4

No changes. Dependencies and provenance: see section 5.

### Open proof obligations (updated)

| Id | Obligation |
|---|---|
| O1 | Extend Propositions 1, 3, 4, 7, 8 to continuous spaces (measurability, absolute continuity; infinite-dimensional posterior consistency needs the Kleijn–van der Vaart type conditions). |
| O2 | Connect ε_t to a generalisation guarantee for a learned model class. |
| O3 | Tightness of the c^t factor in Proposition 3(a). |
| O4 | Verify Proposition 1 against Armstrong (2018), Castro et al. (2009), the observable-operator literature; and the Armstrong/pseudorandom-seed remark. |
| O5 | Composite-null and optional-stopping versions of Proposition 5. |
| O6 | A theorem, not an example, characterising when adaptivity strictly increases sup TV (Proposition 9(b) is existence only). |
| O7 | A finite-sample version of the absorption statement (Proposition 8(c)): how many adaptation episodes make the updated theory absorb a given discrepancy, as a function of model class capacity. |
