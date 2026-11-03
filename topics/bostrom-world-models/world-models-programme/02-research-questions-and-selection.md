---
id: topic-bostrom-world-models-wm-questions
title: "Candidate research questions, scoring and selection"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-05
tags: [questions, selection]
---

# Eight candidate questions
Fields: (1) formulation; (2) matters because; (3) known; (4) unknown; (5) hypothesis; (6) environment; (7) world model; (8) intervention; (9) baseline; (10) confounders; (11) negative result; (12) feasibility; (13) contribution. Scores 1–5 (qualitative, my judgement; a high score does not establish novelty).
| ID | Question | Known (what blocks novelty) | Unknown / candidate hypothesis | Falsified / negative outcome | Scores: Orig / Imp / Math / WM / Bos / Feas / Triv-risk(↓) / Unident-risk(↓) / Gen |
|---|---|---|---|---|---|
| Q1 | **Direction A.** Can an agent infer membership in a *class of computational generators* from interaction alone? | observational equivalence; Chalmers; Bostrom's editing assumption | which computational-class properties have identifiable signatures at a given interface (precision, resolution) and which are equivalent to physical mechanisms | all candidate properties equivalent to a physical alternative at every realistic interface | 3/5/3/3/5/3/3/4/3 |
| Q2 | **Direction B.** Finite-precision/discretisation signatures: identifiable when, and against which physical alternatives? | modified equations (NA); KL thresholds elementary | the identifiability map over (σ/q, actuator reach, law-class prior) and whether *learned* models recover it | the map is fully explained by two-line KL calculations (it largely is) | 3/4/3/4/4/5/4/3/3 |
| Q3 | **Direction D.** Does the training objective matter: prediction-oriented vs discovery-oriented world models at matched predictive accuracy? | BOED, curiosity, MuZero value-equivalence (AB) | magnitude of the dissociation for *learned* (not Bayesian-over-given-hypotheses) models | no dissociation, or it vanishes with matched coverage | 3/5/3/5/3/4/3/2/4 |
| Q4 | **Direction C.** Does nesting change identifiability after controlling budget/interface? | composition closure (trivial) | only through an observable resource channel | no effect once the channel is removed (expected) | 2/3/2/3/4/3/5/3/2 |
| Q5 | **Direction F.** Detecting observer-dependent (adaptive) dynamics vs hidden-state dynamics | persistence ≡ random-time change (own, Phase 9); Choi et al. | whether interventions that *change the observer's own strategy* break the equivalence | equivalence persists for all admissible strategies | 3/4/4/3/3/3/3/4/3 |
| Q6 | **Direction E.** A theory of what each class of test/learned model can license about generative structure | Phases 5–10 | an organised map is not a theorem | everything is a corollary of known results (largely true) | 2/4/3/3/3/4/4/2/3 |
| Q7 | Transfer of discovery skill across generator families (meta-learned discovery) | meta-RL; causal discovery transfer (not reviewed) | whether discovery *policies* transfer to unseen mechanisms | no transfer beyond training families | 4/4/2/5/2/2/2/3/5 |
| Q8 | **Direction F′.** Can a learned world model *detect its own coverage limits* (know what it cannot predict), distinguishing "not yet learned" from "different mechanism"? | uncertainty quantification (ensembles contested), Phase 9–10 results | calibrated structural-uncertainty signals under intervention | ensemble disagreement uncorrelated with the exact epistemic gap | 3/5/3/5/3/3/3/3/4 |
Full field-by-field entries for the three selected questions are in `03` and `05`.

# Selection
**Selected for preliminary investigation:** **Q2** (precision signatures; the cleanest exactly analysable case that connects to Bostrom's "resolution of the simulation" question), **Q3** (prediction vs discovery at matched predictive accuracy; the central world-model question), and—as a thin extension only—**Q8** (coverage-awareness), which was *not* run.
**Rejected/deferred.** Q4 (nesting): trivial without a resource channel; deferred until a formal channel is specified. Q6: already largely done (Phases 8–10). Q5: persistence equivalence is established; the remaining question requires an agent whose strategy alters the generator, not yet designed. Q7: needs a family of generators and a meta-learner; far beyond the current evidence base. Q1 is the umbrella for Q2.
**Honest assessment.** Q2 and Q3 both have elementary Bayesian analogues (KL maps, Chernoff design). The only way they become more than illustrations is if *learned* world models behave differently from the Bayesian ideal in a way theory does not predict; the pilot tests the Bayesian side first and shows what the learned side must be compared against.
