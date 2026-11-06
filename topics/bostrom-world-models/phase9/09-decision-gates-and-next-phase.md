---
id: topic-bostrom-world-models-phase9-gates
title: "Decision gates G1–G7, verdict on confirmatory E6, and the next research phase"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [gates, decision, roadmap]
---

# Gates (before any confirmatory E6/E6′)
| Gate | Requirement | Assessment | Evidence |
|---|---|---|---|
| **G1** mathematical correctness | no unresolved flaw in the procedures being tested | **Partly passed.** E_ctx (in-class), E_ep, E_comp: valid with stated nulls (Props A–D; enumeration; MC). **Not passed for the learned-null repair**: the dev CP-box version has no coverage guarantee for data-dependent counts (A4); the LR-confidence-sequence version is specified but not implemented or verified | `01`, `04` |
| **G2** conceptual clarity | formal rejection separated from mechanism interpretation | **Passed**: three-way separation, kernel vs generator change, corrected ladder | `02` |
| **G3** literature adequacy | closest prior results identified and verified enough to assess originality | **Not passed.** Sources behind Prop D (Choe–Ramdas; Henzi–Ziegel), Prop E (Chernoff; Naghshvar–Javidi), the mixing remark (Berbee; Yu) and minimax testing are unread (secondary description only); two downloaded papers (Ramdas et al.) unread; no systematic review; Brogioli, Weatherson, Edge, Ikram et al. still inaccessible | `03` |
| **G4** experimental identifiability | the benchmark distinguishes the claimed hypotheses or measures an impossibility | **Passed** with a stated limitation (A = O = 3, T = 4): impossibility cells (persistent regime ≡ random-time change; bisimilar twin; unplayed action; latent context) are built in and exactly checked | `04`, `05`, `07` |
| **G5** statistical adequacy | sample sizes, independent units, intervals, thresholds defensible | **Not passed yet.** Corrected plan exists (structures as units, R ≥ 60, margin rules, Holm), but ICCs for the E6′ procedures are unknown, even cluster intervals undercover at R = 20, and the required structure count has not been re-derived per claim | `06` |
| **G6** reproducibility | development experiments and audits pass | **Passed for development**: 291 tests, determinism 30/30, namespace audit. **Feasibility caveat**: E_ep is 50× slower than the others and needs incremental statistics | `07` |
| **G7** scientific value | positive and negative outcome both informative | **Failed for E6 as specified** (its outcome is mostly fixed by theory); **passed for the re-scoped E6′** (robustness–power frontier, H-A…H-F) | `05` |

# Verdict
**REVISE — do not launch confirmatory E6 (or E6′) now.** No preregistration was frozen; no confirmatory data exist; nothing was run in the E6 confirmatory namespaces (700–719, 800–829).

# Recommended next phase (Phase 10: E6′ development completion and literature gate L2)
1. **L2 (literature).** Read in full: Choe–Ramdas (comparing sequential forecasters), Henzi–Ziegel, Chernoff (1959) and Naghshvar–Javidi, the Ramdas et al. admissibility and game-theoretic-statistics papers (already downloaded), minimax testing references (Le Cam; Ingster), Berbee/Yu. Paywalled items: your help.
2. **Development.** (a) implement and verify the LR-confidence-sequence denominator by exact enumeration; (b) a fast, incremental E_ep; (c) measure the **type-I of an e-process built on EM denominators** (H-E; not measured); (d) estimate ICCs from ≥ 60 independent structures for every procedure; (e) engineered shift/regime positive controls for false attribution; (f) optional ensembles (H-F).
3. **Theory.** A bounded attempt at a lower bound for the minimal detection sample size of any valid test over a null class of complexity d (robustness–power frontier). If it is a corollary of known minimax testing results, record that and stop.
4. **Review.** Obtain an external (human) design review of `05`/`06`, then freeze a preregistration.

# Comparison of directions (X1 closed; X2; X3; and the E6′ line)
| Direction | Scientific question | Existing evidence | Strongest novelty threat | Most discriminating next step | Falsifier | Cost | Expected value |
|---|---|---|---|---|---|---|---|
| **E6′** (price of validity) | How much detection power does a guaranteed, learned observer give up when its class may be wrong? | dev: in-class power vs zero power of robust procedures | minimax testing; Prop A–D are known | H-A…H-E on ≥ 60 independent structures per family | rungs non-monotone; robust procedures within ×3 of in-class; EM-denominator type-I ≤ α | CPU hours (after E_ep fix) | medium: an informative measurement; probably not a theorem |
| X2 (frontier theory) | tight predictive-vs-mechanism distance frontier | Prop 3; Chernoff exponents; Phase 6 diagnostic | data-processing; Chernoff | bounded proof attempt | frontier = Prop 3 | light | low–medium |
| X3 (learner generalisation) | does narrow-training failure persist across learners? | Phase 5 (2 learners) | inversion literature | count/HMM/GRU × coverage ladder | failure under full coverage | CPU/GPU hours | medium; supplies learners for E6′ |
Ranked by potential for defensible new knowledge: E6′ (with X3 supplying learners) > X2.

# Alternative question uncovered by the audit
"What can a *comparator-relative* predictive test license about a learned world model, and what cannot be licensed at any budget?" — it merges Props D, F and R1–R5 and is where the philosophy (theory-ladenness of the comparator; premise about resets) and the statistics meet.
