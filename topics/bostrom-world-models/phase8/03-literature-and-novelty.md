---
id: topic-bostrom-world-models-phase8-novelty
title: "Phase 8 adversarial literature review and novelty-threat matrix"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-03
tags: [literature, novelty]
---

# Adversarial literature and novelty assessment (Phase 8)

## Access and reading levels (stated first)
- **Partly read from extracted full text (Phase 7):** Wasserman–Ramdas–Balakrishnan (universal inference: split LRT, Thm 1, sequential Thm 9–11; they write that the MLE "is obtained by the EM algorithm, which we assume converges" and that local/global EM convergence "is beyond the scope"); Gelman–Shalizi (model checking section outline and key passages); Catanach–Das (EDI definition).
- **Search-description level only (Phase 6, 8):** Gama et al. concept-drift survey (via secondary descriptions: real drift = change of P(y|x), virtual = change of P(x)); Choi–Yeung–Zhang hidden-mode MDPs (NeurIPS 1999); Allman–Matias–Rhodes (Ann. Stat. 2009, HMM/latent-structure identifiability, generic identifiability via Kruskal); Shin–Ramdas–Rinaldo e-detectors; Wimmer et al. and follow-ups on aleatoric/epistemic disentanglement; Jeffreys–Lindley paradox literature; Perry et al., Schölkopf et al., Chen et al. on sparse mechanism shifts; Locatello, Khemakhem, Hyvärinen–Pajunen, Bareinboim et al. (Phase 6); Wolpert (Phase 6).
- **From memory, not verified here:** Le Cam two-point method / Pinsker; Wald; Ville; AIC/BIC; Berk. **Not found:** Grünwald–van Ommen on Bayesian misspecification (search returned nothing relevant).
- **Inaccessible (earlier phases, not bypassed):** Brogioli, Ikram et al. full text, Edge, Norton, Weatherson text, Semantic Scholar (429), PhilPapers/PhilArchive.
No new full text was read in Phase 8. "Not found" means not found in what I reached.

## Searches (2026-11-03, standard web search, 9 queries in Phase 8)
concept drift real/virtual; HMM identifiability; hidden-mode MDP / non-stationary RL as POMDP; aleatoric–epistemic disentanglement critique; Lindley/Jeffreys paradox and misspecified Bayes; e-detectors; unified taxonomy of predictive-failure causes; sparse mechanism shift identifiability. Plus reading of the universal-inference text for approximate maximisers.

## Is the four-way distinction formalised already?
- *Pieces:* real vs virtual drift (change in P(y|x) vs P(x)); covariate/concept/label shift taxonomies; epistemic vs aleatoric uncertainty (with the literature on whether they are separable at all); misspecification as a part of epistemic uncertainty (2022 UQ paper; 2026 taxonomy paper separating model bias from domain-shift uncertainty, snippet-level).
- *What the searches did not return:* a formal **identifiability** treatment of the combined distinctions among estimation uncertainty, class inadequacy, shift, and mechanism change — the 2026 taxonomy is "a conceptual aid, not a strict partition" per its description; none gave non-identifiability results for the combination. This is "not found in the results reached," not an established gap.
- *Where an identifying premise is already known:* sparse/modular mechanism shifts (Schölkopf et al., Perry et al., Chen et al.) provide assumptions under which shifted mechanisms can be identified.

## Novelty-threat matrix
| # | Component | Closest prior work | Strongest "already known" argument | Verdict | Threat |
|---|---|---|---|---|---|
| N16 | Relative taxonomy: labels defined from (E, M, Π, n, structure) and not intrinsic | real/virtual drift; UQ taxonomies; ICM/SMS | Everyone knows the labels depend on the model and assumptions | The explicit non-identifiability (T1/T4) combined across the four causes with exact verification was not found, but is largely a consolidation | Medium-High |
| N17 | Non-stationary/shifting kernel ≡ stationary model with larger latent state | Choi et al. HM-MDP (1999); POMDP augmentation | Textbook | Known | **High** |
| N18 | Finite-data ambiguity A vs B (Le Cam / n·ε) | Le Cam; AIC/BIC; bias–variance | Textbook | Known | **High** |
| N19 | Prediction improves while mechanism posterior mass falls (Occam dissociation) | Jeffreys–Lindley paradox | Textbook | Known; our framing (identification of an unprobed mechanism) is an application | **High** |
| N20 | Validity of e-processes needs the denominator to dominate the true likelihood; approximate maximisers void it | universal inference (requires the exact MLE; EM convergence assumed) | The proof makes this evident | Known; the quantified sequential false-alarm onset and the policy-shift framing are an instance | Medium-High |
| N21 | Sequential stationarity/changepoint e-process | e-detectors (Shin–Ramdas–Rinaldo); mixture SR/CUSUM | Standard | Known | **High** |
| N22 | Hidden stationary regimes with persistence fool changepoint detectors | HMM/regime-switching and change-point literature | Obvious | Known qualitatively; our quantified false-alarm instance with the stationary-start control | Medium |
| N23 | Mechanism shift identifiable only with modularity/sparsity | SMS, ICM | It is exactly their premise | Known premise | **High** |
| N24 | Policy-shift misread as mechanism change by a frozen learned null | covariate-shift/OOD literature | Known (OOD detection with learned models) | Instance | High |
| N25 | Existing Bostrom-linked claim (X1/Phase 5): limits of inference about simulation from observation | Chalmers, Bostrom; Duhem–Quine | Established | No new claim | – |

**Net assessment.** Every component is known or elementary. The only possibly new contribution is an *organised, exactly verified map* of which of the four distinctions are identifiable under which premises, plus quantified instances for learned observers. This is an integrative/methodological contribution at best and is not claimed as novel. No theorem is claimed.
**Gate C verdict:** the *question* as stated goes beyond any single known result only through the integration; the narrower unresolved problem that survives is **PO-10** (what mixing/reset premise makes sequential adequacy/stationarity e-processes robustly valid when the model class is misspecified, and how do learned, certified nulls trade power for validity).
