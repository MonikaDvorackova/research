---
id: topic-bostrom-world-models-phase8-review
title: "Internal cross-check of X1, adversarial reviewers, decision gates, roadmap, decision log"
topic: bostrom-world-models
type: review
status: active
created: 2026-11-03
tags: [review, gates, roadmap]
---

# 1. Internal cross-check of Phase 7B results (not an external replication)

| Check | Method | Outcome |
|---|---|---|
| Headline numbers | recomputed from `results/x1_confirm/runs.jsonl` with a separate script | 244/14 400 = 0.0169; decisions match `analysis.json` |
| Dependence | one-way ANOVA ICC of null rejection by seed (cluster 480 runs) | ICC = −0.0003, design effect 1.00: run-level bounds were adequate for type-I; **independent units for any ratio claim = 30 seeds** |
| Independence of environments | inspection of `make_e0(seed)` | seeds jitter one structure by ±8 %; the number of independent *environment structures* is one. Generality across structures is untested (A3 in the Phase 7B issue register) |
| Likelihoods, adaptive-policy supermartingale, policy scores | Phase 7B independent audit (brute-force path sums; exhaustive tree enumeration; loop-based scores) | pass (artifacts preserved, not rerun) |
| Phase 7B conclusions that need **external** replication | – | (i) the proof of Prop X1-V under adaptivity; (ii) the decision logic of the preregistered analysis; (iii) independent reimplementation of `x1.py` by another person; (iv) a second machine/OS run |

The original confirmatory analysis and hypotheses are unchanged. Nothing in Phase 8 reinterprets them.

# 2. Adversarial reviewers (written by the same agent; disagreements retained)

**Reviewer A — mathematical statistics.** *Strongest objection:* "T1–T6 are textbook: Le Cam, absorption, Lindley, Ville with the MLE in the denominator. The 'map' is a table of corollaries." *Evidence required:* a theorem not implied by these — e.g. a mixing/reset condition under which E_stat is provably valid for a misspecified class (PO-10), or minimax statements for adaptive designs (PO-8). *Status:* not provided; the claim is deliberately only a map.
**Reviewer B — machine learning.** *Strongest objection:* "Count learners on 3-symbol environments say nothing about neural world models; and your dwell-time counterexample is a synthetic chain built to fail." *Evidence required:* E6 with ≥ 30 independent structures, O2 (HMM) and O4 (GRU) nulls, and a hidden-regime generator not tuned to the test. *Concession:* the failure of E_stat under persistence is by construction expected; its value is quantifying how the guarantee depends on an unverifiable premise.
**Reviewer C — philosophy of science.** *Strongest objection:* "That shift vs mechanism change is a matter of the model's boundary is the Duhem–Quine point plus the old observation that any time-dependence can be absorbed in state. You have rediscovered underdetermination with a counter." *Response/limits:* agreed; the contribution, if any, is the exact verification and the list of identifying premises (observed context, resets, modularity, bounded k). **Reviewer C also notes:** nothing here bears on the simulation hypothesis, and the Phase 8 results should not be read as evidence about it.
**No consensus is claimed.** A and C would classify Phase 8 as expository; B would classify it as an incomplete empirical programme.

# 3. Decision gates (Part IX)
| Gate | Question | Outcome | Evidence |
|---|---|---|---|
| **A** conceptual clarity | Can the four explanations be defined without circularity? | **Passed only in relative form; failed in absolute form.** A and B are defined from the law; C and D require a factorisation not determined by the law. *Revision:* the research question becomes "which distinctions are identifiable under which declared structure?" | `01-…` §2, T4 |
| **B** identifiability | Can the distinctions be made from observer-available information? | **Partly.** Impossible: C(latent) vs D; stationary hidden regime vs random-time D (single trajectory); A vs B below n·ε ≈ 1. Possible: C(policy) vs D within a class containing the truth; A vs B with a comparator above n\*; B_Π vs B_Π′ via the discriminating action; C vs D with observed context/reset/modularity premises | T1–T4, D2, D2b, D3 |
| **C** novelty | Does the question go beyond known results? | **Failed for every component; undetermined for the integrated map; one narrower open problem survives (PO-10)** | `03-…` |
| **D** experimental validity | Can a benchmark test claims without leaking? | **Passed** with set-valued scoring and the experimenter-side identifiability partition | `04-…` |
| **E** feasibility | Reproducible within reasonable compute? | **Passed** (CPU, minutes–hours) | diagnostics |
| **F** scientific value | Would either outcome advance the question? | **Passed for E6 and E1; failed for E2, E3 (theory settles them); E4/E5 folded in** | `05-…` |

# 4. Updated roadmap (indicative; gates, not deadlines)
| Gate | Content | Proceed if | Revise/abandon if |
|---|---|---|---|
| R-L (weeks 1–3) | Read primary sources with full text: Choi et al., Allman et al., Shin–Ramdas–Rinaldo, Gama et al., Perry et al.; with your help Brogioli, Weatherson, Edge | No source already contains the validity map for learned/estimated nulls under misspecification and persistence | If found: demote E6 to replication; move to X2 |
| R-D (week 3) | External/independent design review of E6 SAP | Review finds no ill-posed metric | Revise |
| R-E (weeks 4–8) | E6 dev run (instances 700–709), freeze preregistration, confirmatory run once | Frozen before data; machinery validated | Any H1/H3 violation = counterexample paper trail, not a failed run |
| R-T (parallel) | Proof obligations PO-8, PO-10, PO-12; X2 bounded attempt | A statement strictly beyond Props 1–10 and T4′ with proof | If everything is a corollary: close X2 and record |
| R-E2 (weeks 8–14) | E1 with HMM/GRU nulls | E6 supported or characterised | Else stop |
| R-R (weeks 14–18) | Independent replication (another person/machine) of X1 and E6 | Decisions replicate | Investigate nondeterminism |
| R-Q (weeks 18–24) | Publication-readiness review (venue open; paper type chosen by findings: methodological note, philosophical clarification, or negative-results report) | Contribution more than integration | Report as a negative/clarificatory result or stop |
Nothing here authorises executing stages automatically.

# 5. Decision log (additions)
| Date | Decision | Reason |
|---|---|---|
| 2026-11-03 (Ph. 8) | The question "which of four explanations?" is reformulated as "which distinctions are identifiable under declared structure" | Gate A: C and D are factorisation-relative (T4) |
| 2026-11-03 (Ph. 8) | E2, E3 not run; E4, E5 folded into E6 | theory settles E2/E3; Gate F |
| 2026-11-03 (Ph. 8) | First experiment: E6 validity map; GO subject to external design review and a dev run | both outcomes informative; addresses oracle-likelihood gap |
| 2026-11-03 (Ph. 8) | Prioritise formal theory (PO-10, PO-8) alongside E6; do not start neural experiments yet | learned-null results so far needed no neural network |
