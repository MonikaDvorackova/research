---
id: topic-bostrom-world-models-phase9-literature
title: "Phase 9 literature gate: source-verification log and novelty-threat matrix"
topic: bostrom-world-models
type: literature
status: active
created: 2026-11-04
tags: [literature, novelty, verification-log]
---

# Source-verification log (Phase 9)

Method: arXiv/NeurIPS PDFs downloaded with `curl` into an isolated scratch directory and converted with `pdftotext`; text passages read directly. Access levels: **FT** full text examined (stated sections); **TH** relevant theorem/section examined; **AB** abstract/introduction only; **SD** secondary description only (search-result text); **NA** not accessible. Search date 2026-11-04 (web search, standard mode, 3 queries) plus the Phase 6–8 searches.

| Source | Exact identification | Level | What was examined | Relevance and assumptions found |
|---|---|---|---|---|
| Wasserman, Ramdas, Balakrishnan, "Universal inference" | PNAS 117(29):16880–16890 (2020); arXiv 1912.11436 | **TH** | §2 (split LRT, Thm 1), §8 (running-MLE sequential LRT, Thms 9–11, Ville), EM remark | Thm 9 **i.i.d.**; null MLE in the denominator; "EM … we assume converges"; local/global EM convergence declared out of scope |
| Emmenegger, Mutný, Krause, "Likelihood Ratio Confidence Sets for Sequential Decision Making" | NeurIPS 2023; arXiv 2311.04402 | **TH** | §1–2, Theorem 1 | R_t(θ⋆) nonnegative supermartingale with **adaptively chosen** x_s, ŵ_s, θ̂_s (F_{s−1}-measurable); C_t = {θ: R_t(θ) ≤ 1/α}; coverage via Ville; **requires well-specified likelihood**; notes non-identifiability inflates sets |
| Shin, Ramdas, Rinaldo, "E-detectors: a nonparametric framework for sequential change detection" | arXiv 2203.03532 (50 pp.); published in a journal per search descriptions (not verified) | **TH** | §2.1–2.2, Remark 2.1, Def. 2.2, Prop. 2.3 | pre-change class P is a set of laws over **infinite, not necessarily i.i.d.** sequences; e-detector defined by E[M_τ] ≤ E[τ]; ARL control without assumptions on change point |
| Arnold, Gavrilopoulos, Schulz, Ziegel, "Sequential model confidence sets" | arXiv 2404.18678v4 (22 Jan 2026) | **AB** | abstract; introduction passages | e-processes and confidence sequences for sequential model comparison via "best model" defined by predictive loss; cites Choe–Ramdas (2023), Henzi–Ziegel (2022) for sequential forecast comparison |
| Allman, Matias, Rhodes, "Identifiability of parameters in latent structure models with many observed variables" | Ann. Statist. 37(6A):3099–3132 (2009); arXiv 0809.5032 | **TH** | §6.1, Theorem 6, Petrie's conditions | HMM parameters **generically** identifiable up to label swapping from the marginal of 2k+1 consecutive variables with C(k+κ−1,κ−1) ≥ r; Petrie's explicit non-identifiable subvariety (non-regular HMMs, repeated emission entries, singular A) |
| Choi, Yeung, Zhang, "An environment model for nonstationary reinforcement learning" | NeurIPS 1999 | **TH** | abstract; HM-MDP passages | "HM-MDP is a subclass of POMDP … ordered pair of any mode and observable state as a hidden state" |
| Ramdas, Ruf, Larsson, Koolen, "Admissible anytime-valid sequential inference must rely on nonnegative martingales" | arXiv 2009.03167v3 (5 Nov 2022) | **AB (header only)** | title/authors | not used for any statement beyond the title |
| Ramdas, Grünwald, Vovk, Shafer, "Game-theoretic statistics and safe anytime-valid inference" | arXiv 2210.01948 (Statistical Science submission) | **AB (downloaded; not read)** | – | not used |
| Gelman, Shalizi, "Philosophy and the practice of Bayesian statistics" | BJMSP 66(1):8–38 (2013); arXiv 1006.3868 | **TH (Phase 7)** | §4 passages | model checking as hypothetico-deductive "error probes" |
| Catanach, Das, "Metrics for Bayesian optimal experiment design under model misspecification" | arXiv 2304.07949 | **TH (Phase 7)** | EGIG, EDI definitions | EDI = KL(p(Y|d,M⋆)‖p(Y|d,M)) |
| Choe, Ramdas "Comparing sequential forecasters"; Henzi, Ziegel | as cited in Arnold et al. | **SD** (only their citation context) | – | basis of Prop D is **their** construction (not read) |
| Berbee (1979); Yu (1994, Ann. Probab. 22(1):94–116) | blocking / β-mixing coupling | **SD** | search descriptions | used only for the mixing remark in PO-10 (tagged unverified) |
| Gama et al. (concept drift survey), Hüllermeier–Waegeman, Wimmer et al., Locatello et al., Hyvärinen–Pajunen, Khemakhem et al., Bareinboim et al., Wolpert, Schölkopf et al., Perry et al., Chen et al. | various | **SD** (Phases 6, 8) | – | unchanged; no new access |
| Bostrom 2003; Bostrom–Kulczycki 2011; Chalmers (2024 ×2; 2005) | – | **FT/TH (Phases 1–3)** | – | unchanged |
| Brogioli (2019), Ikram et al. (2026 full text), Edge, Norton, Weatherson (text) | – | **NA** | – | still inaccessible; no bypass |

# Novelty-threat matrix (Phase 9)
Questions: (1) established? (2) immediate corollary? (3) reproduces a known phenomenon? (4) adds a new assumption/theorem/algorithm/empirical characterisation? (5) what would a sceptical specialist say is missing?
| # | Potential contribution | (1) | (2) | (3) | (4) | (5) Sceptic |
|---|---|---|---|---|---|---|
| N26 | Adaptive-policy anytime validity of the mixture-LR e-process (X1-V) | yes (Emmenegger Thm 1; Wasserman Thm 9/11) | yes | yes | no; only the POMDP bookkeeping (episode reset, filter) | "This is Theorem 1." |
| N27 | Three-way separation: type-I / misspecification / false attribution; kernel change vs generator change | in spirit (Gelman–Shalizi; standard misspecification) | – | yes | an explicit, tested semantics for sequential tests with a table of cells | "Textbook distinctions." |
| N28 | Episode-level saturated e-process valid for any stationary hidden-state generator under perfect resets | yes (Shin et al. with P = i.i.d. class; Prop A) | yes | yes | no | "It is the categorical case of e-detectors; power is hopeless (alphabet 2187)." (confirmed: 0 rejections in dev) |
| N29 | Predictive-comparison confidence sequence for adequacy relative to a comparator under dependence | yes (Choe–Ramdas, Henzi–Ziegel, Arnold et al.) | yes | yes | no | "Known; and yours has no power at N = 3000 (dev)." |
| N30 | Reset taxonomy R1–R5; persistent regime ≡ random-time change | not found in sources read; elementary (de Finetti / non-ergodicity; HM-MDP) | yes | partly | a clarifying taxonomy with exact checks | "Folklore of POMDPs and exchangeability." |
| N31 | Occam window for mechanism identification | yes (Jeffreys–Lindley; local alternatives) | yes | yes | no | "Known paradox." |
| N32 | Chernoff-normalised comparison of designs; observed gains 72–93 % of the optimum | method yes (Chernoff 1959 `[memory]`, unverified here) | yes | – | an instance | "Routine LP." |
| N33 | Approximate-maximiser audit: EM starts below the true-parameter likelihood 62 % (60 it) / 15 % (300 it) | EM local optima known | – | yes | restricted-setting measurement | "Universal inference already flags this as out of scope." |
| N34 | Relative identifiability map for the four explanations (N16) | partly | – | – | organisation + exact checks | "Consolidation." |
| N35 | Robustness–power trade-off: broader null ⇒ regret ∝ dimension/2·ln n | yes (minimax testing folklore) | yes | yes | dev numbers: E_ctx 30/30 (in-class) vs E_ep 0/30 at N = 3000 | "Known." |
**Net.** No component is new. Nothing is claimed as a theorem. The possibly useful residue is an organised, exactly checked map plus quantified instances for learned observers (classes B/C of `phase7/08`), not a discovery.
