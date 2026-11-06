---
id: topic-bostrom-world-models-phase6-baseline
title: "Research-state baseline (authoritative, as of commit 7ec3d70)"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [baseline, inventory]
---

# Research-state baseline

Authoritative inventory at the start of Phase 6. Source: Phases 1–5 notes (`notes/formal-framework.md`, `results.md`, `results-phase5.md`, `claim-evidence-assumption-matrix.md` v2, `corrections-log.md`, `literature/*`, `reviews/*`) and commit `7ec3d70` (draft PR #10, open, not merged). Working tree clean; no experiment running at the time of writing. Nothing here supersedes an earlier file; it indexes them. Where a statement rests on toy systems it says so.

**Standing evidence labels.** M = mathematically established (finite proofs checked by exact enumeration and 129 adversarial cases); C = confirmatory empirical (pre-specified, held-out seeds, frozen analysis code); X = exploratory; L = known from prior literature (reproduced, not claimed); P = philosophical interpretation; U = unverified; Q = open question.

## 1. Established mathematical results (M)
All elementary; none is claimed as a new theorem.
| ID | Statement (qualified) | Status |
|---|---|---|
| P1, P1′ | Observational equivalence of two controlled processes ⇔ identical interventional kernels on reachable histories; equivalence is *relative to an intervention class*. | M; L (bisimulation/trace equivalence, Castro et al., Armstrong) |
| P2–P3 | Neyman–Pearson/Le Cam, Pinsker, chain-rule bounds; policy-ratio (coverage) bound c^t and impossibility when the probed class has zero mass on the discriminating set. | M; L for ingredients |
| P4–P6 | Evidence screens off; bounded likelihood ratio of one outcome; a misspecified reference null inflates false alarms by up to the TV distance. | M |
| P7a–c | AUROC ceiling ½+TV; cross-entropy identity; score inversion under a learned reference. | M; L for the phenomenon (Nalisnick et al.) |
| P8 | Finite-class posterior consistency, KL concentration, absorption; absorbing an anomaly by updating. | M; L (Doob, Berk) |
| P9 | Adaptivity cannot beat the oracle ceiling; existence of cases where active selection helps/hurts (exact enumeration). | M |
| P10 | EIG design is optimal only relative to the hypothesis class; zero information where members agree; myopic EIG with a catch-all does not explore the untried action (exact DP), two-step does. | M for the finite example; Medium–High novelty threat (Catanach & Das) |
| Cor. | Expected episodes to overturn prior odds ω is **at least** ln ω / KL (Wald). Earlier wording "equals" was false; corrected. | M |

## 2. Empirically supported findings (C)
Env 1: fully observed 2-D Gaussian dynamics, MLP world models. Env 2: finite POMDP (4 hidden / 3 obs / 3 actions), GRU world model. Pre-specified, 12 held-out seeds each (run A primary; run B deterministic re-run).
1. **Oracle vs observer gap.** Oracle-likelihood Bayesian observers separate H0/H1/H2 with budget-increasing, calibrated accuracy (env 2, two-step design 0.60→0.92; ECE 0.037 at step 100). Learned-likelihood and model-averaging observers stay at 0.31–0.45 accuracy, ECE 0.26–0.57. (8/8 directional claims in each env.)
2. **Likelihood inversion** under misspecification: learned reference mislabels the true reference as non-reference (false-identification rate 0.35 in env 1; below chance on H1-vs-H0 in env 2).
3. **Design does not rescue learned observers**: EIG worse than random wide in 11/12 seeds (env 1, confirmatory); no benefit in env 2 (−0.025 [−0.047, −0.008]).
4. **Intervention coverage is decisive**: hidden-state mechanism control has TV 0 and posterior odds exactly unchanged without action 2 (M + C); accuracy 0.116 → 0.705 → 0.950 as action 2 is introduced (random → two-step design).
5. **Equivalence controls**: 5 of 6 pre-specified equivalence claims established; **E3b (env 1) not established in run A** (established in run B); not claimed.

## 3. Exploratory observations (X)
Winner's-curse effect in recorded EIG (fixed); information-gain-ratio diagnostic separated correct from misspecified observers in env 1 (0.97 vs 5.0) but **did not replicate** in env 2; stress tests (coverage, fidelity 500/2500, incomplete hypothesis class, misleading prior; 6 seeds) — incompleteness gives confident misclassification even for the oracle (ECE 0.33); H1-vs-H2 separability environment-specific (0.93 vs 0.57); post hoc equivalence tests on Phase 4 data.

## 4. Known results reproduced from prior literature (L)
Observational equivalence/bisimulation; underdetermination (Duhem–Quine; Laudan–Leplin relativisation); posterior consistency under misspecification (Berk; Kleijn–van der Vaart); likelihood inversion in deep generative models (Nalisnick; Ren); Wald identity; EIG design (Lindley; Rainforth et al.). Reading level of each source is recorded in `literature/novelty-threat-matrix.md`; several are abstract-only and the ones inaccessible are listed there.

## 5. Philosophical interpretations (P)
Bostrom's indifference-principle proviso and anomaly-editing assumption insulate the simulation argument from detection evidence; Chalmers: perfect simulation is not sceptical; inference ladder anomaly → model discrepancy → mechanism → implementation → simulation → ancestor simulation, each rung needing premises. These are interpretive readings supported by full-text reading of Bostrom, Bostrom–Kulczycki and Chalmers (two papers) only.

## 6. Unverified claims (U) — must not be cited as findings
Anything about Brogioli (2019), Weatherson (2003), Edge, Norton, Ikram et al. beyond abstracts; novelty of the *conjunction* of components (absence-of-evidence from a limited search); generality beyond two toy environments and one learner family per environment; any bearing on the physical universe.

## 7. Robust vs assumption-dependent
| Finding | Robust across | Depends on |
|---|---|---|
| Oracle ≫ learned-likelihood observer | both envs, both learners, stress tests | learners trained on a narrow policy; one learner family per env; no ensembles/calibration fixes tested |
| Likelihood inversion | env 1 (nine observer types), env 2 | coverage gap in training; vanishes when training covers the probed range (stress) |
| EIG ≤ random for learned observers | env 1 (11/12), env 2 | EIG computed from the learned likelihood; no misspecification-aware design |
| Coverage decisive | exact (M) + both envs | by construction — it is a theorem for the toy; the empirical question is how often real coverage gaps occur (U) |
| H1 vs H2 separable | env 1 (0.93) | env 2 only 0.57; mechanism-specific |
| Info-gain ratio diagnostic | **not robust** | env 1 only |
| Run reproducibility | one machine; run B deterministic | stream-seeding bug fixed after run A |

## 8. Weakest existing assumptions
(i) Hypothesis class is *given* to the observer (members hand-built); (ii) oracle likelihoods are assumed to exist, which is exactly the object an embedded observer lacks; (iii) intervention class and "reference" environment are defined by the experimenter, so "detection" is detection of a specified perturbation, not of simulation; (iv) two toy environments, one learner family each, 12 (6) seeds; (v) Bayesian observer only — no frequentist/e-value or criticism-based observer was tested; (vi) the original headline ("learned world models cannot detect simulation") is not what the experiments test.

## 9. Findings on the six requested topics (revisited)
1. *Oracle–observer gap*: real, large, confirmatory in both envs, driven by learned-likelihood quality and coverage — not by the information in the environment.
2. *Likelihood inversion*: an instance of a known phenomenon; the interventional-Bayesian instance with exact explanation (P7b) is the only added value.
3. *Failure of the original adaptive observer*: it failed because it adapted to the environment under test (absorption, P8c); not evidence about any real system.
4. *Role of coverage*: the single most important variable; both the exact barrier and the empirical failure vanish when the probed range is covered.
5. *Equivalence controls*: exact in the finite POMDP (TV 0, odds unchanged); statistical elsewhere (one of three env-1 claims unresolved).
6. *Limits of inferring simulation from anomalies*: anomaly → model discrepancy is the most an observer can claim without extra premises (see Direction F map).

## 10. Open research questions carried forward
See `02-open-question-map.md`.
