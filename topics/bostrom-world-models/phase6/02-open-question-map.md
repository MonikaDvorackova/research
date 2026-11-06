---
id: topic-bostrom-world-models-phase6-open-questions
title: "Open-question map: six directions"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-03
tags: [directions, open-questions]
---

# Open-question map (Directions A–F)

Evidence level of searches: search-result descriptions and abstracts unless stated (see `03-literature-search-log.md`). "Original?" is a judgement about *my reachable literature only*.

## A. Prediction versus identification
**Question.** Can predictive accuracy improve indefinitely while the generative mechanism stays unidentified?
**Already established.** Yes, trivially, whenever mechanisms are observationally equivalent on the data-generating policy class: nonidentifiability of latent-variable models (Hyvärinen–Pajunen 1999, Locatello et al. 2019, Khemakhem et al. 2020 — abstract-level), the causal hierarchy theorem (interventional data cannot determine counterfactuals; Bareinboim et al.), PSR/bisimulation equivalence in POMDPs (Zhang et al., Baisero–Amato; abstract-level). World-model work uses predictive training with no identification guarantee (Freeman et al. 2019).
**Exact diagnostic (this phase; `results/phase6/prediction_vs_identification.txt`).** In the benchmark POMDP, with training-policy probability q of the informative action, per-episode KL(E0‖Et) is ≈ 0 at q = 0, 1.7e-6 at q = 0.005, 8.2e-5 under the wide policy (eps = 0.05). Predictive error on the training distribution can be driven below any threshold while the mechanism gap on the wide class is larger by a factor that grows like 1/q (49× at q=0.005). This is Prop. 3 (coverage amplification) quantified for one benchmark — **not new**.
**Where a non-trivial question remains.** (a) A *general* frontier: for a finite controlled process and a class Π of policies, the largest mechanism distance on Π′ among models ε-close in prediction on Π, as a function of (Π, Π′, structure) — is there a clean combinatorial characterisation beyond the per-step ratio? (b) Computational version (Direction B). (c) Finite-sample: how many episodes under Π to *certify* predictive closeness vs to certify identification — the latter has an unavoidable factor 1/q. 
**Original?** Per-step amplification: no. A tight general frontier theorem: unknown, plausible but probably a corollary of data-processing for KL. **Risk: rediscovering observational equivalence.** Status: theory candidate, medium priority.

## B. Empirically indistinguishable worlds
Taxonomy (exact definitions): (1) exact observational equivalence (P1); (2) equivalence under restricted interventions (P1′, exact in the benchmark); (3) finite-horizon equivalence (prefix laws equal up to T; exact enumeration feasible); (4) ε-statistical equivalence (TV ≤ ε; sample complexity Θ(1/ε²) per Le Cam); (5) computational indistinguishability (cryptographic; PRF-based emission in the hidden-state mechanism; polynomial-time observers).
**Does capacity/intelligence/budget change the limit?** (1)–(3): no (exact). (4): budget moves the boundary ~ε⁻², capacity does not unless it enables a better *test*, which for finite alphabets is the likelihood ratio. (5): capacity (computation) is the whole story, and the notion is standard cryptography; Brogioli (2019, abstract only) appears to use a complexity-theoretic condition. Possible new empirical content only as a measured gap between a bounded learner and an unbounded one — unlikely to be conceptually new.
**Verdict.** Mostly settled by theory; the research value is as a *map* in the paper, not as an experiment. Low priority except (3) as an exact test bed.

## C. Autonomous scientific discovery / hypothesis-space inadequacy
**Question.** Can an embedded Bayesian agent discover that its class is inadequate, and does the design policy matter?
**Prior art.** Model checking is outside Bayesian updating (Gelman–Shalizi 2013, abstract/summary level); posterior predictive checks, misspecification measures in SBI (Schmitt–Bürkner, abstracts); misspecification-robust BED (Catanach–Das; Barlas et al.; Tang et al.; Go et al.; abstracts); universal inference / split-LRT gives finite-sample valid, anytime-valid tests of a composite null with no regularity (Wasserman–Ramdas–Balakrishnan 2020; abstract level). Formal learning theory: identification in the limit with a catch-all.
**What our own results add.** P10 + Phase 5: *within-class* EIG design is blind where members agree, and detection of inadequacy needs a criticism statistic; our incomplete-class stress test shows confident misclassification without one.
**Open, tractable and testable.** With a valid e-process for "truth ∈ class" (universal-inference construction), (i) what is the power as a function of *design*? (ii) does design that maximises criticism evidence beat random wide and within-class EIG, and by how much (Wald bound: episodes ≥ ln(1/α)/KL)? (iii) what is the cost of *discovery* — proposing a new member — as opposed to rejection of the class? Distinguish: model *updating* (posterior over fixed class), *criticism* (reject class), *expansion* (add member from a proposal family), *discovery* (the added member is better, validated on held-out interventions).
**Original?** The pieces are known; a controlled comparison of designs for detecting class-inadequacy under hidden-state equivalence structure, with exact bounds, I did not find — unverified. **Highest priority.**

## D. Nested simulated environments
**Question.** Can an agent learn about its parent by simulating inside it?
**Prior art.** Wolpert (2008/2010, "Physical limits of inference"; abstract/press level): inference devices embedded in the universe obey Halting-type limits and no universe contains two strong inference devices; Beane–Davoudi–Savage (press-level only) — lattice signatures; Bostrom: nested simulation is part of the argument's structure.
**Formal analysis.** A nested simulation is a program of the parent's own dynamics run on parent resources. Its output is a function of (program, parent resources). Information about the parent arises only via *resource side-channels* (runtime, memory, failure), i.e. via the parent's computational bounds — an observation about the parent's *physics*, which the agent could obtain by running ordinary programs; the nesting adds nothing except possibly (a) a lower bound on parent resources by existence of a child that completes, (b) misleading evidence if the child's rules mimic a parent. No discriminating experiment with a formal mechanism exists yet.
**Decision.** Per the brief, not recommended for implementation. Written test of readiness: a formal model in which nesting depth changes the observer's posterior over a parent parameter *given the same non-nested experiments* — currently none. **Defer.**

## E. Partial observability and hidden mechanisms
**Prior art.** Bisimulation/PSR/causal-state equivalence; POMDP identifiability; learning in POMDPs needs observability conditions (Zhang et al.; PAC survey 2026; abstracts).
**Our finding.** Hidden state yields an exact, intervention-class-relative barrier (TV 0 without action 2) — **strengthens a known barrier; new epistemic kind? No.** What is new relative to fully observed systems is that the *non-identifiable* part is a quotient (state-splitting) rather than a parameter, so predictive risk and mechanism risk can diverge without any estimation error.
**Open.** Nonstationarity (a mechanism that switches when the observer probes the informative action — an "observer effect" that makes the barrier adaptive) and noisy observations (finite-sample cost 1/KL scaling) are the two directions that are not already folded into known notions. A nonstationary variant is cheap to build in the exact framework.
**Verdict.** Use E as the platform for C and A, not as a standalone direction.

## F. Philosophical inference ladder (rungs and required premises)
| Rung | Inference | Extra premises required | Our formal handle |
|---|---|---|---|
| 1→2 | Anomaly ⇒ reject predictive model | Observer's reference model is adequate on the probed regime; anomaly not due to finite sample or misspecification | P6, P7, coverage |
| 2→3 | Rejection ⇒ identify the mechanism | A hypothesis class containing the true mechanism; discriminating interventions reaching the disagreement set | P1′, P8, P10 |
| 3→4 | Mechanism ⇒ computational implementation | A bridge between the physical mechanism and a computation (substrate-independence; no observable difference between implementing programs) | none — pure philosophy |
| 4→5 | Implementation ⇒ "simulated" | An artifact criterion distinguishing simulated from base-level computation; a reference for "unsimulated" | none |
| 5→6 | Simulated ⇒ Bostrom ancestor simulation | The trilemma's premises (posthuman civilisations; interest in ancestor simulations; indifference principle) | Cor. (cost of overturning prior) |
Relation to the literature: rung 1→3 is underdetermination (Duhem–Quine, Laudan–Leplin, Stanford SEP — summary level); 3→5 is Chalmers' "Matrix as Metaphysics" (a simulation is a metaphysical, not sceptical, hypothesis); 5→6 is Bostrom. **None of the observations is presented as new**; the only possibly new element is the quantified rung 1→3 behaviour for learned observers, which is empirical and toy.
