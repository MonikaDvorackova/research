---
id: topic-bostrom-world-models-comparison-matrix
title: "Comparison matrix"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [literature, novelty]
---

## Comparison matrix

"Read" means the full text was read; everything else rests on abstracts or snippets and is provisional. See [verification-log.md](verification-log.md).

| Publication | Research question | Formal contribution | Experimental contribution | Link to Bostrom | Overlap with this project | Remaining gap |
|---|---|---|---|---|---|---|
| Bostrom 2003 | At least one of three propositions holds about posthuman ancestor simulations | Probabilistic trilemma | None | Is the argument | Defines the target of the epistemic question | Silent on empirical detectability by observers |
| Chalmers 2022 (book; not read) | Are virtual worlds real; can the simulation hypothesis be refuted | Metaphysical arguments | None | Direct engagement | Supports separating ontological from epistemic claims | No formal treatment of detection from interventions |
| Birch 2013 (abstract only) | Does the argument need selective scepticism | Philosophical critique | None | Direct critique | Evidence-limits theme | No learned models or testing theory |
| Beane, Davoudi, Savage 2012 (abstract only) | Could a lattice simulation leave physical signatures | Bounds from cosmic-ray cutoff | None (data comparison) | Motivated by simulation hypothesis | Concrete artifact-detection precedent | Physical signatures, not an agent's inference procedure; no explicit hypothesis-testing formalism assessed |
| Armstrong 2018 (abstract only) | When are POMDPs indistinguishable to agents | Observational vs counterfactual equivalence; deterministic-POMDP result | None | None | Core notion of indistinguishability | No statistical (finite-sample) distinguishability, no learned models |
| Castro et al. 2009 (abstract only) | How do bisimulation and trace equivalence relate under partial observability | Equivalence relations and trajectory characterisation | None | None | Observational-equivalence foundation | Exact, not approximate or statistical |
| Naghshvar and Javidi 2013 (abstract only) | Optimal action choice in sequential testing | Bounds and asymptotically optimal heuristic (Chernoff sense) | None | None | **Known theory for the value of active experimentation; must not be restated as new** | Not applied to world-model error structure |
| Warrier et al. 2026 (abstract only) | Do agents learn models that answer environment-level queries | WorldTest protocol | AutumnBench; humans vs five frontier models | None | Evaluation of learned world knowledge | Tests knowledge, not discrimination between generating processes |
| Tan et al. 2026 (abstract only) | What physical information do latents encode | Training-objective analysis | PokeWorld, RH20T | None | Latent content vs model quality | Not detection by an embedded agent |
| Ikram et al. 2026 (abstract via search summary; full text unread) | Unrealistic generated states in model-based RL | Method: linear latent prior flags generated states | Atari100k; DreamerV3 +9% HNS | None | Small: anomaly handling inside learning, not environment discrimination by an agent | Does not address embedded-agent discrimination or inference from anomalies |
| Hafner et al. 2025 | General model-based RL via learned world models | Method | 150+ tasks | None | Defines the class of learned model E1 | Not about detectability |
| Leuenberger arXiv:1404.1718 (abstract) | Formal models of philosophical puzzles incl. simulation argument | Algorithmic probability, observer localisation | None | Models the argument | Different framework; no detection analysis visible | Full text unread |
| Ramezanian arXiv:2609.10864 (abstract) | Predetermination and P = NP for embedded observers | Observer-relative unprovability | None | None | Not about simulation (earlier characterisation withdrawn) | None |
| Campbell et al. arXiv:1703.00058 (abstract) | Can rendering-on-observation be tested | Physics proposal | Proposed experiments | Motivated by simulation theory | Fidelity-indexed sub-hypothesis example | Full text unread |
| Brogioli 2019 (PhilSci Archive; snippet) | Empirical equivalence via simulated systems and an experimenting robot | Sufficient condition via complexity-class transformation | Numerical simulations | None found | **Closest formal neighbour for empirical equivalence** | Must be read before submission |

| Bostrom 2003 (full text read) | At least one of three propositions holds | Probabilistic trilemma; bland indifference principle conditional on no discriminating information | None | Is the argument; builds in simulators that edit anomalies | Defines both the target and the proviso our Corollary addresses | Silent on how much evidence would defeat the proviso |
| Chalmers 2024 (two papers, full text) and "Matrix as Metaphysics" (summary) | Epistemic and metaphysical status of the simulation hypothesis | Philosophical arguments | None | Direct engagement | Perfect-simulation indistinguishability; defeat by indifference; imperfect sims may be sceptical | No quantitative or experimental treatment |
| SEP Formal Learning Theory; Kelly 1996 (TOC); Genin and Kelly 2017 (abstract) | When can hypotheses be verified, refuted, identified in the limit | Topological and computability characterisations | None | None | Formal home for "indistinguishable hypotheses cannot be identified" | Not applied to simulation or learned observers |
| Berk 1966; Kleijn and van der Vaart 2006 (abstracts) | Posterior behaviour under misspecification | Concentration on the KL minimiser | None | None | Underlies Prop. 8 | Not applied to detection of generated environments |
| Nalisnick et al. 2019; Ren et al. 2019 (abstracts) | Deep generative models assign higher likelihood to OOD data | Empirical and analytical explanation | Image benchmarks | None | Known analogue of the inversion (static, not interventional) | No sequential/interventional setting; no philosophical reading |
| Thomas and Didierjean 2026 (abstract) | Can people detect logical impossibilities they experience | None | Two experiments, N = 44 each | Cites Bostrom per Semantic Scholar | Evidence on human observers' detection limits | Not formal; not about simulation theory; full text unread |
| Weinstein and LaValle 2024 (abstract) | When can robots not tell environments apart | Covering maps (sufficient), bisimulation (necessary) | None | None | Robotics-side formalisation of environment equivalence | Exact, not statistical |

### Result of the novelty search

No publication was found that both (a) connects Bostrom's argument to learned world models and (b) studies detectability by embedded agents with controlled experiments. This is an absence of discovered work from a limited search, not evidence that none exists.
