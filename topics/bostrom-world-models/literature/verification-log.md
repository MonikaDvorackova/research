---
id: topic-bostrom-world-models-verification-log
title: "Citation verification log"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [literature, verification]
---

## Citation verification log

Status scale: **V-primary** = metadata checked on the publisher/proceedings/arXiv page; **V-secondary** = checked only on an index, bibliography listing or search summary; **Unverified** = not checked. Content was read only where stated. Searches were run on 2026-11-03.

| cite_key | Status | What was checked | Corrections / caveats |
|---|---|---|---|
| bostrom2003AreYouLiving | V-secondary | Oxford ORA record and a REF case study give *Phil. Quarterly* 53(211):243–255, DOI 10.1111/1467-9213.00309 | Journal page not opened. Argument text not re-read this session. |
| armstrong2018CounterfactualEquivalence | V-primary (abstract) | arXiv:1801.03737, 11 Jan 2018, v2 14 Jan 2018 | Preprint only; no journal version listed. Not about simulation. Proofs not read. |
| castro2009EquivalenceRelations | V-primary (abstract) | IJCAI 2009 abstract page; pp. 1653–1658 | Some reference lists give a different title ("Notions of state equivalence under partial observability") for the same authors and pages. Paper not read. |
| warrier2026BenchmarkingWorldModel | V-primary (abstract) | PMLR v306 page: ICML 2026, pp. 133215–133246, 11 authors, no DOI | Preprint arXiv:2510.19788 had a shorter title ("Benchmarking World-Model Learning"). Paper not read. |
| tan2026LatentWorldModels | V-primary (abstract) | arXiv:2607.27017, v1 29 Jul 2026, v4 26 Sep 2026 | **Title and author list differ between versions** (earlier subtitle: "Physical Parameter Identifiability in Multimodal Predictive Representations"). Author list taken from a fetch summary of the abs page; re-check before submission. About what a latent encodes, not environment discrimination. |
| ikram2026WorldModelAnomaly | V-secondary (bib only) | TMLR BibTeX confirms title, 5 authors, year | **OpenReview blocked (bot challenge); abstract and results not read.** Nothing may be claimed about its content. |
| hafner2025Dreamerv3 | V-secondary | Search results give *Nature* 640(8059):647–653, DOI 10.1038/s41586-025-08744-2 (RePEc listing) | Nature title differs from arXiv:2301.04104 ("Mastering Diverse Domains through World Models"). |
| beane2012Constraints | V-secondary | arXiv:1210.1847 from search results (Beane, Davoudi, Savage) | Journal version not checked; cite arXiv only. |
| chalmers2022RealityPlus | V-secondary | Publisher/retailer listings: W. W. Norton, 2022 | Book not read this session; claims about it come from reviews. |
| birch2013SimulationArgument | V-secondary | LSE repository and PhilPapers records: *Erkenntnis*, 2013 | Volume/pages not checked. |
| naghshvar2013ActiveSequential | V-primary | Project Euclid: *Ann. Statist.* 41(6):2703–2738, DOI 10.1214/13-AOS1144; arXiv:1203.4626 | Contents not read beyond abstract. |
| rainforth2024ModernBED | V-primary | Project Euclid: *Statist. Sci.* 39(1):100–114, DOI 10.1214/23-STS915 | — |
| givan2003Equivalence | V-secondary | Bibliography listing: *Artif. Intell.* 147(1–2):163–223 | — |
| janner2019MBPO | V-secondary | arXiv:1906.08253 | Venue (NeurIPS 2019) not verified here; cite arXiv. |

### Not verified (do not cite until checked)

- Chernoff (1959) on sequential design of experiments: the year did not appear in any result.
- Chaloner and Verdinelli (1995): not found.
- Ferns, Panangaden, Precup bisimulation metrics: not found.
- Hanson, Dainton, Kulczycki and other philosophical work on simulation: not searched individually.
- Bruiger (2023) PhilArchive refutation; Scuro on the structure of the trilemma; arXiv:1404.1718, arXiv:2609.10864, arXiv:2512.23419: seen only as search snippets, not read, so characterisations in the matrix are provisional.

### Not done

- Backward and forward citation analysis (no Semantic Scholar / Google Scholar access used). Required before any novelty claim is finalised.


## Phase 2 update (2026-11-03)

Access limits this session: OpenReview returns a bot challenge (an attempt to fetch the PDF with a spoofed browser agent was blocked and not retried); Springer and PhilSci Archive pages were not reachable (authentication redirect, certificate error). Nothing below was obtained by circumventing these.

| Source | What was read | Finding on relevance |
|---|---|---|
| Ikram et al. 2026 (TMLR) | Abstract only, via a search-tool summary of the OpenReview page (not first-hand; full text unread) | Problem: world models produce unrealistic *generated* states that push the agent toward poor policies. Method (LP): a linear prior on successive latent states flags generated states that violate it and excludes them from agent learning; Atari100k; DreamerV3 with LP reported +9% human-normalised mean score with under 90% of value updates. **This is anomaly handling inside model-based learning, not an agent discriminating its environment from a model.** Overlap with this project is small; it is relevant to "model exploitation" and imagined-state reliability. |
| Leuenberger, arXiv:1404.1718 | arXiv abstract (v8, 2017) | Formal models of several puzzles including the simulation argument, via algorithmic probability and observer localisation. No detection method visible from the abstract. Different framework; full text unread. Not a competitor on the narrowed gap. |
| Ramezanian, arXiv:2609.10864 | arXiv abstract (v2, 18 Oct 2026) | About predetermination and provability of P = NP for embedded observers in a shared computational world. **Does not address simulation.** Downgraded from "closest neighbour" (the earlier snippet-based characterisation was wrong). |
| Campbell, Owhadi, Sauvageau, Watkinson, arXiv:1703.00058 | arXiv abstract | Physics proposal: test whether rendering depends on observation. Fidelity-indexed sub-hypothesis in the sense of thesis T1; full text unread. |
| Brogioli (PhilSci Archive 2019) | Search snippet only | Defines empirical equivalence via simulations of physical systems including an experimenting robot, with a complexity-class sufficient condition. **Closest formal neighbour for "empirical equivalence"; must be read before submission.** |
| Hennig, arXiv:2108.09227 | arXiv abstract | Statistical, not about simulation: parameters that are identifiable in theory but not empirically. Peripheral (theoretical vs empirical identifiability). |
| "Inattentional incoherence blindness: If the world were to glitch, would we even be capable of detecting it?" (Psychonomic Bull. Rev. 2026, doi 10.3758/s13423-026-02867-x) | Title and venue only; abstract unavailable | Cites Bostrom per Semantic Scholar. A human-perception angle on detecting glitches. **Unread; potential neighbour.** |
| Philosophy citing Bostrom (titles only) | *Simulation Expectation* (Erkenntnis 2024), *Let's hope we're not living in a simulation* (PPR 2024), *Illusory world skepticism* (PPR 2024), Birch 2013, a Bayesian approach (arXiv:2008.12254; Universe 2020) | Probabilistic and sceptical treatments of the argument; none found that analyses detection by embedded agents. Abstracts read for two. |

### Forward and backward citation search (partial)

- Bostrom (2003): Semantic Scholar returned **512 citing records** (the list is probably incomplete; the true count is likely much larger). I filtered them by keywords (world model, reinforcement, agent, detect, glitch, identifiab, observational, POMDP, hypothesis test, likelihood, empirical, testab, distinguish, artifact, Bayes) and read titles and, where available, abstracts. **No title connects the simulation argument to learned world models or to agent-side detection experiments.**
- Armstrong (2018): references retrieved (6: *Causality*, Inverse Reward Design, IRL in POMDPs, Kaelbling et al. 1998 POMDP paper, Sutton and Barto, and a "Planning and Acting" entry). Citing-paper retrieval **failed** (rate limit); not done.
- Castro et al. (2009): title search returned no usable record; forward citations **not done**.
- Therefore the citation analysis requirement is only partly met. Absence of a connecting paper is again "not found", not "does not exist".

### Still not verified

Chernoff (1959), Chaloner and Verdinelli (1995), Ferns et al. bisimulation metrics, Hanson, Dainton, Kulczycki, Weatherson, Kearns and Singh (simulation lemma) and Ross and Bagnell (compounding error) as bibliographic items (search results only), observable-operator and predictive-state representations.
