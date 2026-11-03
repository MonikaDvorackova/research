---
id: topic-bostrom-world-models-phase10-novelty
title: "Phase 10 novelty-threat matrix (updated)"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-04
tags: [novelty, threats]
---

# Novelty-threat matrix (Phase 10)
Reading levels as in `01-…`. Columns: closest prior result and its assumptions; whether the claim is established; immediate corollary?; threat.
| # | Candidate | Closest prior / assumptions | Established? | Corollary? | Threat |
|---|---|---|---|---|---|
| N36 | Certified learned-null test (LR set from training, α + δ) | Emmenegger et al. Thm 1 (TH); Wasserman et al. §8 (TH); Podkopaev–Ramdas (AB) | yes | yes | **High** |
| N37 | Exponent price = information projection onto the LR set; coverage impossibility | Stein/Chernoff `[memory]`; GROW/RIPr (SD); Prop 1′ (own) | yes in form | yes | **High** |
| N38 | Evidence overhead ∝ null cells (≈ 10 nats/cell) | KT/Rissanen `[memory]` | yes qualitatively | yes | High |
| N39 | Predictive-comparison test with predictable range (power restored, 30/30 and 12/30) | Choe–Ramdas Thm 1–2 (TH); Henzi–Ziegel (AB) | partially (range variant not found) | yes | Medium–High |
| N40 | EM-denominator e-process invalid under optimiser asymmetry; inflation larger for better alternatives; loose tolerance as dominant failure | Wasserman et al. EM remark (TH) | the mechanism is in the proof; measured dose–response restricted | no (empirical) | **Medium** |
| N41 | Exact DP counterexample (grid maximiser) | – | elementary | yes | High |
| N42 | Fixed-n boxes fail under optional stopping (468/1000) | LIL / sequential analysis `[memory]` | yes | yes | High |
| N43 | ICC/design-effect and coverage audit | survey statistics `[memory]` | yes | yes | High |
| N44 | Persistence ≡ random-time change; reset taxonomy | Choi et al., exchangeability | yes | yes | High |
| N45 | Certification cost for latent nulls (Lipschitz relaxation penalty n_test·L·r) | – | **not found; not analysed** | – | unknown |
## Answers to the Part X questions
1. *Is the validity–efficiency frontier already known?* In form, yes (Prop T1, GROW, redundancy). The benchmark instances are not independent knowledge.
2. *Does partial observability add a genuinely new obstacle?* Two, both reducible: (i) no certified supremum for latent nulls (computational), (ii) persistence equivalence (exchangeability).
3. *Does learned misspecification change the mathematical problem?* Yes in one respect: the null becomes a data-dependent set; the exponent is the projection onto it, with coverage-dependent impossibility. It is a known construction (L1).
4. *Does adaptive intervention interact with validity?* No: policy factors cancel (verified exactly and by an adversary). It interacts with **power** only (Chernoff headroom; coverage).
5. *New impossibility result or lower bound?* Only elementary ones (T1, T3a).
6. *Would an empirical characterisation across learned world models be independently valuable?* Possibly **only for neural/latent nulls**, where no exact exponent or certified denominator exists; not done.
7. *Does the philosophical interpretation add beyond underdetermination?* No.
**Net: E6′ as an empirical programme would mostly confirm quantities the theory already fixes.** The unresolved object is N45.
