---
id: topic-bostrom-world-models-wm-literature
title: "Bostrom's argument reconstructed; world-model, causal-discovery and simulation-signature literature; novelty-threat matrix"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-05
tags: [Bostrom, world-models, literature, novelty]
---

# 1. Bostrom's argument, reconstructed (full text read in Phase 1; bibliographic history re-checked)
**Reference.** N. Bostrom, "Are You Living in a Computer Simulation?", *Philosophical Quarterly* 53(211):243–255, April 2003, DOI 10.1111/1467-9213.00309 (Oxford ORA record via search; full text read earlier). Bostrom's own PDF header gives "First version: 2001" (search description of the PDF header; the 2001 text itself was not examined). The 2003 article is the published formulation; 2001 is the first version, not an interchangeable date. Related: Bostrom–Kulczycki, "A Patch for the Simulation Argument", *Analysis* 71(1), 2011 (read earlier); Bostrom's reply to Weatherson, *Phil. Quarterly* 55(218), 2005 (listed, not read); Weatherson, "Are You a Sim?", *Phil. Quarterly* 53(212) (metadata only).
**Logical structure.** A trilemma (a disjunction): at least one of (1) the human species is very likely to go extinct before reaching a "posthuman" stage; (2) posthuman civilisations are extremely unlikely to run a significant number of ancestor simulations; (3) we are almost certainly living in a computer simulation. It is **not** a proof of (3).
**Probabilistic step.** If (1) and (2) are false, a large fraction of observers with human-type experiences are simulated; a "very weak indifference principle" (credence equals the simulated fraction when one has no information distinguishing one's experiences) yields (3).
**Assumptions kept apart.** *Substrate independence* (mental states can supervene on computation, not only on biology); *technological capability* (posthuman computing sufficient for ancestor simulations); *observer counting/reference class* (which observers count, how simulated ones are weighted); *simulated observers vs simulated environments* (the argument concerns simulated minds; how much of the environment must be simulated, and at what resolution, is a separate engineering question); the text assumes simulators could **edit or rerun** anomalies noticed by simulated minds.
**What it implies about empirical detectability.** The indifference step is stated for the case of *no distinguishing information*; evidence that discriminates would defeat that step. Bostrom's own editing assumption builds indistinguishability for inhabitants into the premise. Hence the trilemma does not by itself predict artefacts; any empirical test addresses a *specific simulator hypothesis*, not the trilemma.
**Critiques in the record (Phases 1–3; levels in earlier logs).** Chalmers: a perfect simulation is not a sceptical scenario (read); indifference defeat (read); Weatherson (metadata only); underdetermination (Stanford SEP, summary).

# 2. Sources examined in this programme step (access levels)
Levels: **TH** theorem/section read; **AB** abstract (+ first page) read; **SD** search description; **NA** not accessed. PDFs obtained with `curl` and converted with `pdftotext`; passages read directly.
| Source | Identification | Level | What was verified |
|---|---|---|---|
| Ha & Schmidhuber, *World Models* | arXiv 1803.10122v4 | **AB** | generative models of RL environments; compressed spatial/temporal representation; agent trained inside its own "dream" and transferred back |
| Hafner et al., PlaNet | arXiv 1811.04551v5 | **AB** | latent-dynamics model + online planning in latent space; names model inaccuracy, compounding multi-step error, overconfidence outside the training distribution as key difficulties |
| Hafner et al., Dreamer | arXiv 1912.01603v3 (ICLR 2020) | **AB** | behaviours learned by latent imagination, analytic gradients through imagined trajectories |
| Hafner et al., DreamerV2 | arXiv 2010.02193 (ICLR 2021) | **AB (introduction)** | learns purely within a world model; human-level Atari |
| Hafner et al., DreamerV3 | arXiv 2301.04104v2 | **AB** | single configuration across > 150 tasks; Minecraft diamonds without human data |
| Hansen et al., TD-MPC2 | arXiv 2310.16828 | **NA for content** (downloaded; abstract extraction failed) | only the identifier was verified |
| Schrittwieser et al., MuZero | arXiv 1911.08265 | **AB** | learns a model that predicts only reward, policy and value ("quantities most directly relevant to planning") — an explicit example of a world model not trained to reconstruct the environment |
| Assran et al., I-JEPA | arXiv 2301.08243 | **AB** | predicts target-block *representations* from a context block (non-generative) |
| Schölkopf et al., "Toward Causal Representation Learning" | arXiv 2102.11107v1 (Proc. IEEE) | **AB** | "most work in causality starts from the premise that the causal variables are given"; the central problem is the discovery of high-level causal variables from low-level observations |
| Beane, Davoudi, Savage, "Constraints on the Universe as a Numerical Simulation" | arXiv 1210.1847v2 | **AB** | assumes a cubic space-time lattice with unimproved Wilson fermions; derives a bound on the inverse lattice spacing (≳ 10¹¹ GeV, from the cosmic-ray cutoff) and predicts rotational-symmetry breaking in the highest-energy cosmic rays |
| Chalmers, *Reality+* (2022); "The Matrix as Metaphysics" (2005) | – | **NA** (book); summary-level (Phase 3) for the essay | not re-read |
| Phase 5–10 sources (Wasserman et al.; Emmenegger et al.; Choe–Ramdas; Howard et al.; Allman et al.; Choi et al.; Catanach–Das; Gelman–Shalizi) | see earlier logs | TH/AB as recorded | – |
**Not performed, stated plainly:** no systematic review of AI-scientist/automated-discovery systems, active causal discovery (Murphy; Eberhardt), object-centric world models, TD-MPC2's content, foundation/generative environment models, SLAC/latent-state identifiability beyond Allman; Brogioli, Ikram et al. (full text), Edge, Norton, Weatherson (text) remain inaccessible. The syntheses below are therefore **provisional and restricted to what was read**.

# 3. Synthesis
**World models.** The reviewed systems learn latent dynamics *for control or representation*: PlaNet/Dreamer(V2/V3) via reconstruction + reward/value; MuZero by predicting only planning-relevant quantities; I-JEPA by predicting representations; none of the abstracts read claims identification of the generating mechanism. Predictive adequacy is the training signal everywhere; structural identification is not an objective. Most relevant to discovery: MuZero's *value-equivalent* models are by design indifferent to any mechanism detail that does not change planning-relevant predictions — the formal analogue of observational equivalence.
**Causal world models.** Schölkopf et al. state the open problem we need — discovering causal variables from low-level observations — and note that standard causal inference assumes the variables. Identifiability results are sparse (Locatello et al., Khemakhem et al. [SD]): useful embeddings need not be identified states.
**Active discovery.** The relevant machinery is Bayesian experimental design/Chernoff-type active hypothesis testing (Phases 6–10); under a *given* hypothesis class its behaviour is classical.
**Computational signatures.** The one concrete proposal read (Beane et al.) is **type A**: a consequence of a particular simulator architecture (cubic lattice, specific discretisation), not of simulation in general. Generalising from A to "any simulation" (type C) is unjustified; finite precision/discretisation as a *broad class* (type B) is where our pilot sits, and there the central question is observational equivalence with physical mechanisms (see 03).

# 4. Novelty-threat matrix (for the candidate contributions)
| # | Candidate | Closest prior (level) | Strongest "already known" argument | Threat |
|---|---|---|---|---|
| W1 | Equivalence of a quantised (finite-precision) world with a continuous stiction mechanism under a bounded interface | Prop 1′ (own); observational equivalence; modified-equation/backward-error analysis `[memory]` | restricted-intervention equivalence is textbook | High |
| W2 | Quantitative identifiability map for a precision signature (KL in σ/q and actuator reach) | exact Gaussian KL; Chernoff design | elementary computation | High |
| W3 | Prediction-vs-structure dissociation under matched predictive accuracy; EIG planner vs passive | BOED/Chernoff; curiosity/exploration literature (not reviewed) | known design theory | High |
| W4 | Nested simulation adds no identifiability without an observable resource channel | composition closure (trivial) | trivial | High |
| W5 | Discretisation signatures need a prior on law class (Euler ≡ sampled non-conservative flow) | Hairer–Lubich–Wanner backward error analysis `[memory]` (NA) | standard numerical analysis | High |
| W6 | A benchmark platform that separates generator / interface / world model / hypothesis system / planner / evaluator | benchmark design practice | engineering | Medium |
| W7 | A premise-by-premise inference chain from a detected signature to Bostrom's (3) | Bostrom–Kulczycki, Chalmers (read earlier) | philosophical commonplace | High |
**No component is claimed to be new.**
