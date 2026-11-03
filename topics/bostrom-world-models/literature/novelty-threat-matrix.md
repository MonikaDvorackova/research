---
id: topic-bostrom-world-models-novelty-threat-matrix
title: "Novelty threat matrix"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [novelty, literature, audit]
---

## Novelty threat matrix (Phase 5)

Purpose: for every component of the proposed contribution, the closest prior work, the strongest argument that the component is already known, and an honest assessment of whether that argument succeeds. Reading levels: **Full** (text read), **Summary** (read through a fetch summary of the page), **Abstract** (abstract or search description only), **None** (inaccessible). "Threat" is the risk that the component is already known: High, Medium, Low.

### Verified metadata and exact theses of the central works

| Work | Verified metadata | Exact thesis (as read) | Reading |
|---|---|---|---|
| Bostrom, "Are You Living in a Computer Simulation?" | *Phil. Quarterly* 53(211):243–255 (2003); DOI 10.1111/1467-9213.00309 | At least one of: (1) humanity very likely goes extinct before a posthuman stage; (2) posthuman civilisations very rarely run ancestor simulations; (3) we are almost certainly in a simulation. Credence step by a "very weak indifference principle" for observers with no information distinguishing their experiences. Simulators can edit anomalies noticed by simulated minds or rerun, so simulations are "indistinguishable from physical reality for human minds". Assumes substrate-independence. | Full |
| Bostrom and Kulczycki, "A Patch for the Simulation Argument" | *Analysis* 71(1):54–61 (2011) | A mathematical non sequitur in the formula for the fraction of simulated observers; two patches, one needing "empirical indexical evidence" satisfying stated conditions; discusses what would count as evidence against the hypothesis (a defeater based on computer-age birth rank). | Full |
| Chalmers, "Taking the simulation hypothesis seriously" | *PPR* (2024); DOI 10.1111/phpr.13122 | We cannot rule the hypothesis out; a perfect simulation is not a sceptical scenario (most beliefs remain true); per Schneider and Schwitzgebel imperfect versions may be sceptical; "a low-grade model would be pretty easily detectable". | Full |
| Chalmers, "The Simulation Hypothesis: Metaphysics, Epistemology, Value" | *Oxford Studies in Philosophy of Mind* 4 (2024); DOI 10.1093/9780198924159.003.0017 | Objects in a simulation are real; we cannot know we are not in one; defeat of external evidence by indifference over observers with matching experiences (Weatherson 2003 on externalism). | Full |
| Chalmers, "The Matrix as Metaphysics" | Chalmers in Grau (ed.), *Philosophers Explore the Matrix*, OUP 2005 | The Matrix Hypothesis is metaphysical, not sceptical; "from the inside there is no way to tell for sure"; cites Bostrom. | Summary |
| Weatherson, "Are You a Sim?" | *Phil. Quarterly* 53(212):425–431 (2003); DOI 10.1111/1467-9213.00323 (Crossref) | Per Chalmers and secondary descriptions: an objection from externalism about evidence and a "grue"-style worry about the principles Bostrom needs. Not read. | None (metadata verified) |
| Stanford, "Underdetermination of Scientific Theory" (SEP) | rev. 4 April 2023 | Holist (Duhem–Quine) and contrastive underdetermination; Laudan and Leplin: "any judgment of empirical equivalence is both defeasible and relativized to a particular state of science"; Earman's Bayesian response. | Summary |
| Douven, "Abduction" (SEP) | rev. 18 June 2025 | IBE as a reply to underdetermination and to brain-in-a-vat scepticism; the "bad lot" objection; adding a catch-all hypothesis "gives little assurance, because that hypothesis is usually uninformative". | Summary |
| Schulte, "Formal Learning Theory" (SEP) | rev. June 2026 | Verifiable, refutable, identifiable in the limit; hypotheses that no evidence separates cannot be reliably identified. | Summary (about 90%) |
| Catanach and Das, "Metrics for Bayesian Optimal Experiment Design under Model Misspecification" | arXiv:2304.07949 (2023) | Introduces an expected generalised information gain relative to a true model when the design model has discrepancy, and a measure of how well an experiment can detect discrepancy. | Abstract |
| Nalisnick et al. (ICLR 2019); Ren et al. (NeurIPS 2019) | arXiv:1810.09136; arXiv:1906.02845 | Deep generative models can assign higher likelihood to out-of-distribution data than to training data; likelihood ratios against a background model correct part of it. | Abstract |
| Berk (1966); Kleijn and van der Vaart (2006) | *Ann. Math. Statist.* 37(1):51–58; *Ann. Statist.* 34(2):837–877 | Posteriors under misspecification concentrate on the KL-closest model (finite-dimensional; infinite-dimensional extension). | Abstract |
| Castro, Panangaden and Precup (2009); Armstrong (2018); Weinstein and LaValle (2024) | IJCAI 2009 pp. 1653–1658; arXiv:1801.03737; arXiv:2402.18323 | Exact equivalence notions in (PO)MDPs and robot environments (bisimulation, trace equivalence, counterfactual equivalence, covering maps). | Abstract |
| Thomas and Didierjean (2026) | *Psychon. Bull. Rev.* 33(3); DOI 10.3758/s13423-026-02867-x | Humans often fail to notice a logical impossibility in an experienced event ("inattentional incoherence blindness"). | Abstract (PubMed) |
| Brogioli (2019) | PhilSci Archive preprint | Empirical equivalence via simulated systems and an experimenting robot; complexity-theoretic sufficient condition. | Abstract (search snippet; **no full text**) |
| Ikram et al. (2026) | TMLR | Anomaly handling for generated latent states in model-based RL (linear latent prior). | Abstract (via summary; **no full text**) |

### Threat matrix

| # | Component of the contribution | Closest prior work | Strongest argument that it is already known | Does the argument succeed? | What remains | Threat |
|---|---|---|---|---|---|---|
| N1 | The unrestricted simulation claim is not decidable by observation; only fidelity-indexed hypotheses can be tested (T1) | Bostrom (builds in indistinguishability); Chalmers (explicit); formal learning theory | Bostrom assumes simulations indistinguishable for their inhabitants; Chalmers says we cannot know; learning theory says indistinguishable hypotheses cannot be identified. | **Yes, fully.** | Nothing beyond a formal restatement (Props. 1, 4). | High |
| N2 | Detection claims are relative to the observer's theory and its coverage (T4) | Duhem–Quine (SEP, Summary); Laudan–Leplin ("defeasible and relativized"); statistical misspecification theory | Every test confronts a hypothesis together with auxiliaries (here, the observer's theory); empirical equivalence is relative to the state of knowledge. | **Yes for the qualitative thesis.** The quantified interventional instance (coverage, inversion across nine observer types, exact bounds) was not found. | A quantified, experimentally controlled instance for learned observers. | High (qualitative), Medium (instance) |
| N3 | A learned likelihood can rate an unfamiliar environment as more normal than reality (inversion) | Nalisnick et al.; Ren et al. | Known for deep generative models on static data. | **Yes for the phenomenon.** The interventional, sequential and Bayesian-observer instance was not found. | An instance with exact explanation (Prop. 7b) and mechanism check. | High (phenomenon) |
| N4 | Updating on the environment under test absorbs the anomaly (T6; Prop. 8c) | Posterior consistency (Doob, Schwartz, Berk); learning theory | An observer that fits the data it faces will fit it; basic Bayesian consistency. | **Yes for the statistics.** Application to simulation detection and the finding that a Bayesian observer with a *learned-likelihood* class is overconfident not rescued by active design: not found. | Application plus empirical findings (confirmatory D1–D7). | Medium–High |
| N5 | EIG design is only optimal relative to the hypothesis class and can avoid the very place where truth deviates; a catch-all class helps only non-myopically (Prop. 10) | Catanach and Das (abstract); "Improving Robustness to Model Misspecification in BED" (abstract); Douven on catch-all hypotheses being uninformative; Rainforth et al. (review) | Misspecification in BED is an acknowledged problem with dedicated metrics; a misspecification indicator or auxiliary model is already proposed; the "catch-all is uninformative" point is made in the abduction literature. | **Largely yes.** My result is an exact elementary illustration, including a refuted conjecture and a one-step-versus-two-step distinction; its exact form was not found in the abstracts read. | An exact toy illustration; I do not claim a result. | High |
| N6 | How much discriminating evidence defeats the indifference proviso (T7; Corollary) | Bostrom (proviso, full text); Bostrom–Kulczycki (indexical evidence, full text); Wald | The proviso says evidence that distinguishes would defeat the credence step; Wald's identity gives the expected cost. | **Partly.** The proviso is Bostrom's own, and indexical evidence is discussed in the patch; the detection-evidence quantification ln ω / KL was not found. Weatherson, Bostrom's replies and Brueckner are unread. | A quantified application of an elementary bound to Bostrom's proviso. | Medium |
| N7 | Exact finite-state demonstration that observational equivalence is relative to an intervention class (hidden-state control with TV = 0 without action 2) | Castro et al. (bisimulation under partial observability); Armstrong; Weinstein and LaValle | Equivalence relative to action sets is the standard notion (equivalence under all policies versus a policy class). | **Yes.** | A benchmark instance with exact tables. | High |
| N8 | Experiments with learned world models and Bayesian observers on observer-side limits of simulation detection | Searches of the technical and philosophical literature found none; closest are the inversion literature (static), BED misspecification, and "evaluation awareness" in language models (Needham et al., abstract) | No paper joins these in the sources I could reach. | **Not established.** Absence of discovered work from a limited search; Brogioli, Edge, Weatherson, Norton unread. | The empirical programme itself. | Low–Medium (unverified) |

### The strongest single argument that the contribution is already known

*Every component is a corollary of something established: indistinguishability (Bostrom, Chalmers, learning theory), theory-relativity of testing (Duhem–Quine, Laudan–Leplin), absorption by learning (posterior consistency), likelihood inversion (Nalisnick et al.), and design under misspecification (Catanach and Das). What is called a contribution is the conjunction applied to learned observers.*

**Assessment.** The argument succeeds for every component taken separately. It does not by itself show that the conjunction yields nothing new, but the brief asks that integration not be presented as discovery unless it produces a clearly specified new result. The candidate new results are **empirical regularities, not theorems**: (i) with learned likelihoods a Bayesian model-selection observer is overconfident and mislabels the true reference most of the time even under informative interventions, while still separating a learned world model from non-learned alternatives (confirmatory: D1–D7); (ii) in these systems information-gain design did not help and was worse than random wide interventions in the learned regime (post hoc reading of E1); (iii) the ratio of realised to expected information gain separates correct from misspecified observers (exploratory). Their novelty cannot be asserted until the unread sources have been read, and they concern toy systems.

### What remains inaccessible, and the limit it imposes

Brogioli (no full text), Ikram et al. (abstract only), Edge (no access), Norton (certificate error), Laudan and Leplin (primary text), Weatherson (primary text), Bostrom's 2005 and 2009 replies, Brueckner, *Reality+*, Schneider and Schwitzgebel. For N6 and N8 in particular the conclusion "not found" is limited to the sources listed as read. No access restriction was bypassed; Semantic Scholar returned HTTP 429 and was not worked around.

## Phase 6 additions (2026-11-03; search-description level only — see `phase6/03-literature-search-log.md`)
| # | Component | Closest prior work | Strongest "already known" argument | Threat |
|---|---|---|---|---|
| N9 | Distinguishing updating from hypothesis discovery; model criticism outside Bayesian updating | Gelman and Shalizi (2013) | Their central thesis is that model checking and revision lie outside Bayesian confirmation | High (concept) |
| N10 | A finite-sample valid test that the truth lies in a finite model class | Wasserman, Ramdas, Balakrishnan, PNAS 2020 (universal inference, sequential use) | Split likelihood-ratio / sequential version gives anytime-valid tests without regularity | High (test); design for the test: not found |
| N11 | Predictive accuracy without mechanism identification | Hyvärinen–Pajunen; Locatello et al.; Khemakhem et al.; causal hierarchy theorem | Nonidentifiability of latent models and of higher causal layers from lower-layer data is established | High (qualitative) |
| N12 | Limits to inference by embedded observers | Wolpert, "Physical limits of inference" | Impossibility results for inference devices embedded in the universe, independent of physical laws | Medium (abstract-level; scope differs) |

## Phase 7 additions (2026-11-03; after partial full-text reading of three sources via extracted PDF text — see `phase7/01-literature-gate-L1.md`)
| # | Component | Closest prior work | Assessment after reading | Threat |
|---|---|---|---|---|
| N10′ | Anytime-valid test under adaptive hidden-state data | Wasserman et al. Thm 9 (i.i.d.; read) | Same argument holds with conditional likelihoods; extension elementary, proved in D1 | High |
| N13 | Criticism-oriented design | Catanach–Das EDI = KL(p(Y\|d,M\*)‖p(Y\|d,M)) (read) | EDI already targets detection of modeling failures with a specified alternative | High |
| N14 | Criticism target brings no advantage over identity-EIG under equal information (when the alternative contains the truth) | Not found in what was read | A negative result in one benchmark; generality untested | Medium (unknown) |
| N15 | Anticipated vs unanticipated structure of inadequacy detection (margin law) | Laudan–Leplin (summary), Gelman–Shalizi (partly read), Wald-type rates | Quantified instance only | High |

## Phase 8 additions (search-description level except where stated; see `phase8/03-literature-and-novelty.md`)
N16 relative taxonomy (Medium-High); N17 absorption of non-stationarity (High; Choi et al. 1999); N18 Le Cam finite-data ambiguity (High; memory); N19 Occam dissociation (High; Jeffreys–Lindley); N20 approximate-maximiser invalidity (Medium-High; universal-inference text read: EM convergence assumed); N21 stationarity e-process (High; e-detectors); N22 persistent hidden regime fools change detection (Medium); N23 mechanism-shift identifiability needs modularity (High; sparse mechanism shift); N24 policy shift misread by frozen learned null (High). No theorem claimed.

## Phase 9 additions
N26–N35 in `phase9/03-literature-and-novelty.md` (adaptive e-process validity = Emmenegger et al. Thm 1 / Wasserman et al.; episode-level e-process = Shin et al. with i.i.d. class; predictive-comparison CS = Choe–Ramdas family (not read); Occam window = Jeffreys–Lindley; Chernoff-normalised design comparison; EM approximate maximiser audit; reset taxonomy). **No component is new.**
