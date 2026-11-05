# Research synthesis and evidence audit (Bostrom / world-models programme, phases 1–22)

Status: theoretical synthesis; **no new experiment, training run or implementation was done** for this document. Internal analysis; not peer review. Companion files: `identifiability-and-embedded-observers.md` (framework), `literature-and-novelty-map.md` (sources, gap matrix), `research-direction-decision.md` (decision). Older documents are preserved unchanged.

## 1. Verification performed and discrepancies found
Repository `MonikaDvorackova/research`, branch `research/bostrom-world-models`, HEAD `d019dd6`, draft PR #10 open and unmerged — verified by `git`/`gh` at the start. I did **not** re-run the test suite (368 passed at `d019dd6`, as last recorded); I re-read stored artifacts only.
Spot-checks of headline claims against raw artifacts:
| claim | artifact | outcome |
|---|---|---|
| X1 confirmatory type-I 244/14 400 = 0.0169, all cell upper bounds ≤ 0.07 | `results/x1_confirm/analysis.md`, `runs.jsonl` (36 000 rows) | **confirmed** |
| SDW: unfamiliar-mechanism recovery 0.95 [0.91,0.98] at B = 8, best baseline (Hammerstein) 0.44 | `results/sdw_dev/main_ns25000_report.md` | **confirmed**. The recent brief's "≈ 0.81 at B = 8" is wrong: 0.81 is the sweepB agent at **B = 5** (falsify 0.87); B = 8 is 0.95 for both |
| MDW: direct probing 0.09/0.16 vs world-model 2.6/1.3 error at B = 4 (held-out gate/backlash) | `17-…md` (table), `results/mdw_dev/` | **consistent with doc 17** (not re-derived from raw JSON) |
| OOL holdout, B = 12, identifiable out-of-L0: agent L1 1.00 / L2 0.38; static-grammar L1 1.00 / L2 0.70; L0 0.90 / 0.00; PySR-oracle-state L1 0.80 | `results/ool_dev/holdout_report_long.pkl` | **confirmed** (L2 of PySR rows is a coarse token heuristic: 0.40 oracle, 0.05 Kalman) |
**Namespace discrepancy (a correction to my own earlier statements).** The standing constraints recited in later briefs list seeds 600–629 as untouched. They are not: `results/x1_confirm/` is the **preregistered confirmatory run of X1 (seeds 600–629)**, executed in phase 7 after a preregistration commit (`README_phase7.md`). Only 700–719 and 800–829 (the E6/E6′ confirmatory ranges) have no result directories. Nothing in the later phases ran in 600–629, so no harm was done, but the later "untouched" recitations were inaccurate for that range.
**Provenance caveat.** Every review in the programme ("adversarial reviewers", "independent audit") was written by the same agent that produced the work; none is external. Most literature was read at abstract/search level until phase 18, and several phase-9/10 claims cite sources "from memory". These are marked in the novelty map.

## 2. Reconstruction of the intellectual development
| phase | question (as stated then) | what was done | verdict recorded then | assessment now |
|---|---|---|---|---|
| 1–3 | Can an agent embedded in an environment tell a learned world model E1 from the reference E0? Reframed: what may it infer from a detected discrepancy, and which premises reach "simulated"? | formal framework (props 1–6), small PyTorch proof of concept, ablations | REVISE (philosophical content anticipated by Chalmers, Duhem–Quine, Laudan–Leplin; maths elementary) | correct: the narrowed question is a quantified instance of known points |
| 4–5 | Do learned-likelihood observers detect mismatch? | preregistered phase-5 study | learned observers overconfident, invert out of coverage; theory-relativity of detection | informative methodological negative; coverage dependence is known (Wald/Chernoff; offline-RL coverage) |
| 6 | How does prediction error amplify under shifted policies? | exact diagnostics | amplification ≈ 1/q (coverage) | known fact reproduced exactly |
| 7 | Anytime-valid test of class adequacy under adaptive interventions (X1) | proof, preregistration, confirmatory run 600–629 | H1 supported (type-I 0.0169); design benefit (H4c) falsified under equal information | A-class: elementary extension of universal inference/Ville to POMDP with actions; null design result is a genuine, modest negative |
| 8 | Which of four explanations (state, regime, mechanism, shift) are identifiable under declared structure? | taxonomy, T1–T6, gates | "which distinctions are identifiable under which declared structure" | **the right question**; gates A–C: conceptually relative, novelty failed for every component |
| 9–10 | Price of validity: power lost by a guaranteed, learned-null observer | E6′ development, certified null, EM-denominator study | confirmatory not authorised; proofs reduced to known (T1 = Wald-type lower bound); explicit counterexample: approximate maximisers void validity | informative negative/clarificatory; nothing new mathematically |
| 11 | Certified HMM likelihood bounds | interval/type-class code | closed; interval B&B already published (Montanher; Gormley–Eisner), K-ratio claim false for constrained families | archive: infrastructure, off the central question |
| docs 00–12 | Do learned latent world models (GRU/RSSM) recover mechanism? epistemic abstention states | gwb benchmark, abstention benchmark | predictive models fine in family, fail on unfamiliar structure; abstention framework | methodological negative; conceptual framework (claim / abstain-ambiguous / abstain-out-of-class) is sound but standard in spirit |
| 13–15 | Programme comparison; kick-world (deterministic vs random shocks) | prototype, RSSM diagnostics | REVISE; "no original contribution identified" | the determinism / computational-origin-of-randomness question was the most Bostrom-relevant idea and was never developed theoretically |
| 16–17 | Active discovery with a meta-trained world model | MDW, planners, baselines | NO-GO for world-model advantage | negative result, benchmark-limited |
| 18–21 | Structure search with calibrated criticism | SDW environment, grammar search | H1 only with a grammar aligned to the generator | the alignment caveat is decisive |
| 22–25 | Discovery outside the hypothesis language | independent manifest, staged expansion, PySR/SINDy | NO-GO for adaptive expansion + learned latents + falsification design | always-on search ≥ adaptive loop; equation-error pipelines limited by state error |
Pattern across 25 documents: each phase narrowed the claim, each audit classified the mathematics as "known or elementary" and the empirical effect as benchmark-dependent, and each implementation phase added tooling around a question that the preceding theory phase had already answered. **The experimental programme drifted from the original question (what can an *embedded* observer identify about a generative system?) to engineering questions about agents that fit equations in toy simulators.** Phases 8–10 were the closest to the original question and are the most valuable part.

## 3. Mathematical results: what exists and its status
All were classified by the programme itself as known or elementary; I agree and add primary sources where I accessed them (see the novelty map).
| result | statement (short) | status |
|---|---|---|
| Prop 1′ / T3a (barrier) | mechanisms differing only on histories unreachable under the interface are indistinguishable by any procedure | elementary; instance of behavioural/bisimulation equivalence |
| T1 | valid sequential test needs E_P[τ] ≥ ln(1/α)/min κ (KL data-processing at a stopping time) | proved; known form (Wald; Chernoff; Le Cam family) |
| T4 | coverage q of discriminating histories multiplies cost by 1/q | proved; elementary corollary of T1 |
| T2 | certified exponent Λ_cert = min over confidence set; Gaussian illustration (1−ρ/μ)² | proved; elementary |
| T3c / Prop F | persistent hidden regime ≡ random-time change in a single trajectory; no mixing-free guarantee | proved; known in spirit (ergodicity cannot be certified from one trajectory) |
| T5 | approximate maximiser in the e-process denominator can void type-I control; exact DP counterexample (P(reject) → 1 for a grid omitting the truth) | proved/constructed; practical caution, no new theory |
| SDW S1–S5, OOL P1–P3 | interface-limited exact equivalence; pairwise-disagreement elimination; Le Cam score; EIG pathology under misspecification; predictive ≠ structural | elementary or known |
**No theorem in the programme is, to my assessment, new.** The strongest unresolved items the programme itself recorded: a non-asymptotic minimax delay bound with unknown pre/post-change laws (T1 obstacle), a rate for retained exponent in the training size (T2), a certified HMM-likelihood price (phase 11).

## 4. Empirical findings that stand
1. **Coverage dominates** (verified, repeatedly): detection and generalisation fail where training/interaction never reached; effect size follows 1/q. Known theory, confirmed in several toy settings.
2. **Learned predictors are architecture-and-coverage-limited**: GRU/RSSM/meta-trained models predicted in-family and failed out of family; more training did not repair it (doc 17: v2 no improvement). This is evidence about those architectures at that scale, not about a limit of embedded observers.
3. **Predictive adequacy ≠ structural recovery** (OOL: 0.42–0.62 of agent successes predictive without structure; ~40 % of claims wrong-structured). Known phenomenon (non-identifiability/misspecification); the quantification in a self-built benchmark is of low evidential value for any general claim.
4. **Calibration matters**: nominal χ² thresholds over-rejected valid models 15–62 %; empirical calibration fixed it (doc 20/24). A calibrated misfit test cannot see mechanisms that a wrong-structured model already predicts within noise (OOL blind spot).
5. **Hidden-state reconstruction error, not operator-library size, limited equation-error discovery** (PySR with privileged state 0.65–0.80 vs 0.03–0.28).
6. **Design and latent components gave no robust benefit**: falsification design, ensemble-variance design, learned latent state, latent-ordered expansion (docs 17, 20, 24).
Items that must **not** be cited as findings: "structural recovery 0.95" without the grammar-alignment caveat; any statement that the learned world model was "necessary" or "sufficient" for discovery; any inference toward simulation.

## 5. Methodological weaknesses (programme-wide)
1. **Self-built benchmarks with shared authorship** (benchmark, agent vocabularies, baselines, reviews). Closure alignment was measured in phase 22 only as a caveat; the decisive remedy (independent generator) was never done.
2. **Lab observer, not embedded observer.** Nearly every experiment lets the observer reset the world, replay episodes, choose arbitrary admissible programmes and run many i.i.d. episodes. An embedded observer has one trajectory, no reset, causal restrictions and memory limits. The central object of the original question was therefore **never tested**; the theory (Prop F, reachability) says these restrictions change identifiability qualitatively.
3. **Baselines are my configurations** (SINDy/PySR pipelines; equation-error rather than simulation-based).
4. **Repeated REVISE/NO-GO cycles with new tooling each time**, which produced code volume (1 013 lines for `sdw` plus 1 089 for `ool`, source and scripts, in two consecutive phases) but no new knowledge about the central question.
5. **Many bootstrap CIs resample instances of one generator family**; generality across structures is untested.
6. **Literature access was mostly abstract-level** for the identifiability, causal-representation, learning-theory and philosophy strands until this synthesis; several "novelty not found" statements therefore carry little weight.

## 6. Decision per experimental line
| line | decision | reason |
|---|---|---|
| Phase 1–5 proof of concept and learned-likelihood observers | **Retain as methodological negative** | clean demonstration that theory-relativity and coverage determine what a detected discrepancy licenses |
| X1 (anytime-valid class-adequacy test, 600–629) | **Retain as useful evidence** | verified type-I control; documents an elementary theory-conform result and a null design result; exhausts seed range 600–629 |
| Phase 6 exact diagnostics (1/q) | **Retain** | exact instance of coverage amplification |
| Phases 8–10 taxonomy, T1–T6, price of validity, certified null | **Retain** (theory) | the part closest to the original question; proofs and counterexamples are checkable |
| Phase 11 HMM bounds | **Archive as inconclusive** (infrastructure) | closed by its own note; known methods |
| gwb GRU/RSSM benchmarks, abstention study | **Retain as methodological negative** (+ framework retained) | evidence on architectures; abstention states reusable as vocabulary |
| kick-world prototype | **Archive as inconclusive** | the question (determinism of environment randomness) is worth theory, not this prototype |
| MDW active discovery (docs 16–17) | **Retain as methodological negative**; **discontinue** the line | design/WM advantage absent; benchmark-limited |
| SDW structure search (docs 18–21) | **Retain as methodological negative** (grammar alignment); **discontinue** | shows selection among supplied primitives, not discovery |
| OOL adaptive expansion (docs 22–25) | **Retain as negative result and as an instance of known non-identifiability**; **discontinue** | always-on search ≥ loop; blind spot; shared authorship |
| Any further agent/benchmark/neural/symbolic-regression pipeline | **Discontinue as irrelevant to the central question** | the open issues are theoretical; implementation cannot resolve them |

## 7. What should guide future work
The theory-phase outputs (interface-relative equivalence, reachability barrier, coverage lower bounds, validity-vs-power, approximate-maximiser failure) and the programme's own list of "what is identifiable under which declared structure". The implementation phases should not guide future work except as negative evidence. See `research-direction-decision.md`.
