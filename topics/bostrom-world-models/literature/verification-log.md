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


## Phase 3 update (2026-11-03)

- Philosophical sources are catalogued in [philosophical-review.md](philosophical-review.md) with reading level and access outcome for each.
- **Read in full this session:** Chalmers (2024) *PPR* symposium reply (DOI 10.1111/phpr.13122) and Chalmers (2024) *Oxford Studies in Philosophy of Mind* vol. 4 chapter (DOI 10.1093/9780198924159.003.0017), from the author's own PDFs (text extracted locally).
- **Inaccessible (recorded, no workaround attempted):** the 2026 glitch paper (Thomas and Didierjean; abstract withheld by the publisher, Springer authentication redirect); Brogioli (PhilSci Archive certificate error, PhilPapers 403); Edge (PhilArchive 403); Ikram et al. (OpenReview bot challenge). One attempt to fetch the OpenReview PDF with a spoofed browser identity was blocked by the environment and was not retried.
- **Corrections:** Weatherson (2003) details verified from Chalmers's reference list (*Phil. Quarterly* 53(212):425-431; the author is Brian Weatherson). Wolpert's arXiv title at v5 is "Implications of computer science theory for the simulation hypothesis" (a search listing gave a different title). Ramezanian arXiv:2609.10864 remains withdrawn as a neighbour.
- **New neighbours:** Needham et al. (2025) on evaluation awareness (agent-side detection of constructed environments; empirical; no formal analysis in the description read); Kelly (1996) as a candidate formal framework for underdetermination; Laudan and Leplin (1991) for relativity of empirical equivalence.
- **Still unverified as bibliographic items or unread:** Glymour (1977), Malament (1977), Manchak, Norton (venues and years), Hanson (2001; reference-list entry only), Faizal et al. (2025; press-level only), Barrow, Dainton, Schneider, Schwitzgebel, Godfrey-Smith, Horgan, Peacocke, Helton, Brueckner (2008), Chernoff (1959), Chaloner and Verdinelli (1995), Ferns et al., Kearns and Singh, Ross and Bagnell.
- **Citation analysis:** unchanged from Phase 2 (partial).


## Phase 4 update (2026-11-03)

- **Bostrom (2003): now read in full** (14 pages; author's PDF from simulation-argument.com, text extracted locally). Passages used: the three propositions; the substrate-independence assumption (section II); the bland indifference principle (section V); and the passage in which simulators fill in detail on demand and "could easily edit the states of any brains that have become aware of an anomaly" or rerun the simulation (section on computational requirements), which builds undetectability into the argument.
- **Thomas and Didierjean (2026): abstract obtained** from PubMed (PMID 41703184) and Europe PMC (public APIs; no access restrictions bypassed). It is an experimental psychology study (two experiments, N = 44 each) in which a magician's trick produces a logical impossibility that most participants fail to notice unless it is pointed out ("inattentional incoherence blindness"). Full text unread. It concerns human detection limits, not simulation theory or formal identifiability.
- **Chalmers, "The Matrix as Metaphysics":** page read via a fetch summary (not the raw text): defines the Matrix Hypothesis, argues it is metaphysical, not sceptical, states that from the inside "there is no way to tell for sure", and cites Bostrom (2003). Quotations as returned by the fetch tool.
- **Brogioli (PhilSci Archive):** still not read (certificate error, 403 on mirrors). An additional search description says the paper is a thought experiment with no numerical results, derives theorems from computational complexity theory, uses cellular automata as models, and has the robot's experiments discover the rules of the system in which it is simulated. Not read; do not rely on more than this.
- **Genin and Kelly (2017), arXiv:1707.09378:** abstract only. **Kelly (1996):** table of contents only (CMU page). **SEP "Formal Learning Theory":** about 100,000 of 111,000 characters read via a fetch summary; verifiability, refutability and identification in the limit, and the point that hypotheses indistinguishable by evidence cannot be reliably identified (Glymour's architecture example).
- **Norton's observational-indistinguishability paper (sites.pitt.edu):** certificate error; not accessed.
- **Weinstein and LaValle (2024), arXiv:2402.18323:** abstract only; robot-environment equivalence by covering maps (sufficient) and bisimulation (necessary).
- **Verified metadata:** Berk (1966) *Ann. Math. Statist.* 37(1):51-58; Kleijn and van der Vaart (2006) *Ann. Statist.* 34(2):837-877, DOI 10.1214/009053606000000029 (both from Project Euclid / arXiv listings; abstracts only). Nalisnick et al. (ICLR 2019, arXiv:1810.09136) and Ren et al. (NeurIPS 2019, arXiv:1906.02845) from search results.
- **Attempt that was blocked and not retried (Phase 3):** fetching the OpenReview PDF of Ikram et al. with a spoofed browser identity.
- **Still inaccessible or unread:** Ikram et al. (OpenReview), Brogioli, Edge (403), Norton (certificate), Laudan and Leplin (primary text), Weatherson (primary text), Bostrom's replies (2005, 2009), Bostrom and Kulczycki (2011), Chalmers's *Reality+* book, Schneider, Schwitzgebel, Godfrey-Smith, Kelly's book text.

## Phase 5 update (2026-11-03)

**Newly read (full text):** Bostrom and Kulczycki (2011), "A Patch for the Simulation Argument", *Analysis* 71(1):54–61 (author's PDF, 8 pages, text extracted locally). Bostrom (2003) and Chalmers (2024) were read in full in earlier phases.

**Newly read (summary level, via a fetch summary of the page):** Stanford, "Underdetermination of Scientific Theory" (SEP, rev. 4 April 2023); Douven, "Abduction" (SEP, rev. 18 June 2025).

**Metadata verified from Crossref:** Weatherson (2003), "Are You a Sim?", *Phil. Quarterly* 53(212):425–431, DOI 10.1111/1467-9213.00323. Content not read.

**Newly identified neighbours (abstract level only):** Catanach and Das (arXiv:2304.07949), expected information gain under model misspecification and a measure of discrepancy detection; "Improving Robustness to Model Misspecification in Bayesian Experimental Design" (OpenReview; auxiliary model with a misspecification indicator); "On the Misinformation in a Statistical Experiment" (AISTATS 2026 poster); "Robust Experimental Design via Generalised Bayesian Inference" (arXiv:2511.07671). These make Proposition 10 a high novelty threat (see `novelty-threat-matrix.md`).

**Access outcomes this phase (none bypassed):**
- Semantic Scholar API: HTTP 429 (rate limit) on three title searches (Ikram et al., Brogioli, Weatherson); not retried within the phase and not worked around. No abstract for Ikram et al. or Brogioli was obtained from it.
- PhilSci Archive (Brogioli): certificate error; PhilPapers: 403; PhilArchive (Edge): 403; Springer journal-scope pages: authentication redirect; OpenReview (Ikram et al.): bot challenge.
- Consequently Ikram et al. and Brogioli remain **abstract/snippet only**, and conclusions about them are limited accordingly.

**Still unread (limits stated in the novelty threat matrix):** Brogioli, Ikram et al. (full text), Edge, Norton, Laudan and Leplin (primary), Weatherson (primary), Bostrom (2005, 2009 replies), Brueckner (2008), *Reality+* (book), Schneider, Schwitzgebel, Godfrey-Smith, the full texts of Catanach and Das and of Genin and Kelly.

## Phase 6 update (2026-11-03)
Targeted web-search scan (10 queries; see `phase6/03-literature-search-log.md`). Verified at **search-description level only**: Wasserman–Ramdas–Balakrishnan PNAS 117(29):16880–16890 (2020); Gelman–Shalizi BJMSP 66(1):8–38 (2013); Catanach–Das arXiv 2304.07949 (plus four later BOED-misspecification arXiv papers); Wolpert arXiv 0708.1362; Locatello et al. arXiv 1811.12359; Zhang et al. arXiv 1906.10437; Baisero–Amato IJCAI 2021; Freeman–Ha–Metz NeurIPS 2019. Beane–Davoudi–Savage: press coverage only. Bahadur–Savage: not found, not cited. No new full text read.

## Phase 9 update (2026-11-04)
Full source-verification table with access levels in `phase9/03-literature-and-novelty.md`. Read from extracted PDF text (TH level): Wasserman et al. §2/§8; Emmenegger–Mutný–Krause Thm 1 (arXiv 2311.04402); Shin–Ramdas–Rinaldo §2 (arXiv 2203.03532); Allman–Matias–Rhodes §6.1/Thm 6 (arXiv 0809.5032); Choi–Yeung–Zhang (1999). Abstract/intro only: Arnold et al. (arXiv 2404.18678v4). Downloaded, not read: Ramdas et al. 2009.03167, 2210.01948. Not accessible: Brogioli, Ikram et al. (full text), Edge, Norton, Weatherson (text).
