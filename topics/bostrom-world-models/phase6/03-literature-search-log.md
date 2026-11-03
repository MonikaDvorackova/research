---
id: topic-bostrom-world-models-phase6-literature
title: "Phase 6 literature search log and research-opportunity matrix"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-03
tags: [literature, novelty, search-log]
---

# Phase 6 search log and opportunity matrix

**Limits, stated first.** The only search tool was a web search that returns result lists with short descriptions, plus page fetches. Every item below is therefore verified at the **search-description/abstract level at best**; **no new full text was read in Phase 6**. This is not a systematic review (no database queries to Web of Science/Scopus/PhilPapers, no screening protocol, no forward/backward citation traversal — Semantic Scholar was rate-limited and PhilPapers/PhilArchive blocked in earlier phases and not worked around). It is a *targeted novelty scan*. A real systematic review is a roadmap task (Gate L2). Nothing is claimed to be a literature gap.

## Searches run (date 2026-11-03, web search, standard mode)
| # | Query (abridged) | Target direction | Result used |
|---|---|---|---|
| S1 | prediction vs identification, observational equivalence, world models | A | Freeman, Ha, Metz, NeurIPS 2019 (arXiv 1910.13038): world models without forward prediction — off-target for identification |
| S2 | agent detects inadequate hypothesis space; posterior predictive check; BED misspecification | C | PPC/misspecification-measure literature (Schmitt–Bürkner SBI; gravitational-wave PPC review) |
| S3 | POMDP identifiability, observational equivalence, PSR | E | Zhang et al. arXiv 1906.10437 (causal states, behavioural equivalence); Baisero–Amato IJCAI 2021 (PSRs); hindsight-observability paper arXiv 2301.13857; PAC survey arXiv 2603.01309 |
| S4 | nested simulation, computational constraints, lattice cutoff | D | Beane–Davoudi–Savage (press coverage only; primary arXiv not reached) |
| S5 | Wolpert, physical limits of inference | D | arXiv 0708.1362 (abstract/secondary descriptions) |
| S6 | nonidentifiability of latent-variable models / nonlinear ICA | A | Hyvärinen–Pajunen 1999, Locatello et al. arXiv 1811.12359, Khemakhem et al. 2020 (descriptions via review snippets) |
| S7 | BOED under model misspecification | C | Catanach–Das arXiv 2304.07949; Barlas–Sloman–Kaski arXiv 2511.07671; Tang et al. arXiv 2506.07805; Abdulsamad et al. arXiv 2603.14094; Go et al. arXiv 2205.09914 |
| S8 | causal hierarchy theorem / counterfactual realizability | A,F | Bareinboim–Correa technical reports; Raghavan–Bareinboim ICLR 2025 |
| S9 | universal inference (split LRT) | C | Wasserman–Ramdas–Balakrishnan, PNAS 117(29):16880–16890 (2020), arXiv 1912.11436: finite-sample valid, regularity-free tests; sequential/anytime-valid use |
| S10 | Bahadur–Savage; Gelman–Shalizi | C | Gelman–Shalizi, BJMSP 66(1):8–38 (2013), arXiv 1006.3868: model checking as hypothetico-deductive step outside Bayesian updating. **Bahadur–Savage: search returned nothing; I do not cite its content.** |

**Inclusion criteria.** Directly states an identifiability, equivalence, misspecification-robust design, or model-checking result for sequential/interventional or Bayesian settings; or a philosophical account of simulation hypotheses. **Exclusion.** Pure application papers; press items except as pointers; anything whose content I could not confirm.

## Items I know from memory but have **not verified** here (do not cite until checked)
Bahadur–Savage 1956; Lindley 1956 (information-gain design); Wald's identity (standard); Ville's inequality (standard); Kleijn–van der Vaart; Doob; the e-value literature beyond universal inference.

## Research-opportunity matrix
Score scale: High / Medium / Low, qualitative. "Closest" are those listed above.
| Dir. | Closest existing papers | Known theorems | Established empirics | Unresolved (as far as reached) | Potential original contribution | Strongest novelty objection |
|---|---|---|---|---|---|---|
| A | Locatello 2019; Khemakhem 2020; CHT (Bareinboim); Zhang 2019 | Nonidentifiability of unconstrained latent models; CHT; bisimulation | Disentanglement failure studies | A tight, general frontier between predictive and mechanism distance on policy classes; finite-sample certificate cost | Frontier characterisation + exact benchmark | "This is data-processing / observational equivalence"; per-step amplification is Prop. 3 |
| B | Brogioli 2019 (abstract); Armstrong 2018; Castro 2009; Weinstein–LaValle 2024 | Le Cam; cryptographic PRG indistinguishability | — | Measured gap bounded vs unbounded learners | A map, not a result | Standard complexity theory |
| C | Gelman–Shalizi 2013; Catanach–Das 2023; Wasserman et al. 2020; Barlas et al. 2025; Schmitt–Bürkner | Universal-inference validity; posterior concentration | PPC in applied fields; BED misspecification case studies | Design policies for *detecting inadequacy* with exact power analysis in hidden-state equivalence structure; updating vs discovery separation in a controlled agent | Controlled comparison + bounds; possibly a P10-type theorem for criticism design | "Misspecification-robust BED already exists; model criticism is standard" |
| D | Wolpert 2008; Beane et al. 2012 (press) | Halting-type limits (Wolpert) | none (cosmic-ray constraints) | Any formal mechanism by which nesting informs about the parent | None identified | No discriminating experiment; may be vacuous |
| E | Zhang 2019; Baisero–Amato 2021; PAC survey 2026; hindsight observability | Observability conditions for sample-efficient POMDP learning | RL benchmarks | Nonstationary/observer-effect mechanisms; quotient-vs-parameter nonidentifiability for learned models | Instance-level benchmark | Known POMDP observability theory |
| F | Bostrom 2003; Bostrom–Kulczycki 2011; Chalmers 2024/2005; Stanford SEP; Douven SEP | Underdetermination arguments | — | Premise-by-premise ladder with formal handles | Integrative clarification | "Every rung is in Chalmers/Duhem–Quine" |

## Updates to the novelty-threat matrix (see `literature/novelty-threat-matrix.md`)
Added: N9 (Gelman–Shalizi, model checking outside Bayesian updating: threat to any "updating vs discovery" distinction — High for the concept); N10 (Wasserman et al. universal inference: removes novelty of the validity of an anytime test of "truth ∈ class" — High for the test, not for its use as a design target); N11 (Locatello/Khemakhem/CHT: nonidentifiability of latent models — High for Direction A's qualitative claim); N12 (Wolpert: physical limits of inference — Medium for any claim about embedded observers' limits, abstract-level).
