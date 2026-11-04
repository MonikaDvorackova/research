# 13 — Reassessment: diagnosis of the programme, primary-literature log, novelty-threat matrix, programme comparison, selection

Written before building the selected prototype (§6 gate). Nothing earlier is rewritten; this document supersedes earlier *selection* decisions only where stated.

## 1. Audit of the record (independently verified this session)
Branch `research/bostrom-world-models` at `d02e02a`; PR #10 open/draft; 334 tests pass (65 s); `git log` contains the full phase history (d4cc9e7 → 0df5186 → c68b378 → a8bc0f1 → d02e02a). Exposed evaluation namespaces (not usable as untouched tests): 9001–9304, 9777, 11000–11200, 12000, 13000. No confirmatory seed range (600–629, 700–719, 800–829) has ever been used.

## 2. Scientific diagnosis (classification of each limitation; "main" marks what I judge decisive)
| # | Finding / limitation | Type | Judgement |
|---|---|---|---|
| 1 | Latents contain mechanism information | empirical | expected: meta-trained sequence models approximate Bayes filters (Ortega 2019; Mikulik 2020, AB) — known |
| 2 | Better prediction ≠ better structure | conceptual + experimental | partly an artefact: the RSSM was *defective* (see §3), so the "predictive gap" is not a clean variable |
| 3 | Discovery objective (ICI) no robust gain | experimental/statistical | 3 seeds, one objective; inconclusive |
| 4 | Simple intervention policies beat learned planner | benchmark design **(main)** | the generators were designed by me; a sweep matched to the dead-zone mechanism is a hand-coded oracle for the answer |
| 5 | Confident claims on equivalent worlds | mathematical | forced by Le Cam two-point (known); not a finding about learned models |
| 6 | Ambiguity exposure does not transfer | conceptual/benchmark | eqA/eqB/eqD share the "pure noise" signature; one genuine held-out source |
| 7 | Oracle works only inside its class | mathematical (known) | standard misspecification |
| 8 | Learned simulators extrapolate arbitrarily | architectural | expected for any non-structured regressor |
| 9 | Math already known | literature | yes (E1–E4 are textbook flavours) |
| 10 | Environments too simple | benchmark design **(main)** | 1-D, closed six-class hypothesis set, designed-in answers |
**Strongest reason a serious venue would reject the current programme:** it demonstrates, in a closed-set toy where the answer is designed in, phenomena that follow from known statistical decision theory (Le Cam, misspecification, covariate shift); the learned-model component adds no mechanism or theory, and "discovery" is six-way classification. A contribution must therefore come from (i) a question the theory does not already answer, (ii) a setting where the answer is not designed in, or (iii) a sharp formal separation that connects to world models.

## 3. Diagnostic of the RSSM-vs-GRU predictive gap (Section 9 requirement)
Primary-source comparison (DreamerV3 full text, `pdftotext`, **TH-level for the points below**): β_pred=1, β_dyn=1, β_rep=0.1, free bits clip at **1 nat**, symlog on vector inputs, **categorical** latents with unimix; the decoder reconstructs the input from (z,h); there is no prior-predictive head. My RSSM: Gaussian latents, free bits 0.1, balance 0.8/0.2 (β_rep=0.2), no symlog/unimix, plus an *added* prior-predictive head — i.e. several deviations, one of which (the first version without prior-loss) autoencoded noise. Controlled diagnostics: `scripts/gwb_rssm_diag.sh` (8 variants incl. decode-from-h-only, Dreamer-style free-bits/balance, β=5, no-prior-loss, H=256, deterministic GRU) — results in `14-…`.

## 4. Primary-literature log (access level per source; TH = text passages read via pdftotext, AB = abstract, SD = search description, NA = not accessed)
| Source | Level | Used for |
|---|---|---|
| Bostrom 2003 *Phil. Q.* 53(211):243–255; "first version: May 2001" (simulation-argument.com PDF header + Oxford ORA record) | AB/SD (earlier: full text read, Phase 1) | trilemma; bibliographic history. The page header gives 2001 as first version; the journal title in print: "Are You Living…", running header "Are We Living…" |
| Beane–Davoudi–Savage 1210.1847 | AB | lattice-artifact signature (type-A, architecture-specific) |
| Campbell et al. 1703.00058 | SD | proposes wave/particle-duality tests premised on finite-resource "rendering on demand" |
| Vazza 2504.08461 (Front. Phys. 2025) | SD | energy-budget argument against full-universe simulation (opinion-quality responses discarded) |
| Birch (critique of the simulation argument) | SD (paywalled) | selective-scepticism critique |
| DreamerV3 2301.04104 | **TH** | loss weights, free bits, symlog, categorical latents |
| TD-MPC2 2310.16828 | **TH** | decoder-free implicit world model: joint-embedding prediction + reward + value, SimNorm, MPPI planning, Q-ensemble |
| Schölkopf et al. 2102.11107 | **TH** | Table I: statistical models predict i.i.d. but not under shift/intervention; causal/mechanistic models do; ICM principle |
| Tao et al. 2502.10390 (ICML 2025) | AB | transformers predict LCG sequences in context (moduli up to 2^32 fixed-modulus; unseen moduli to 2^16); learn digit-wise representations/factorisation; sharp transition at depth 3 — **direct novelty threat for "learned models predict PRNG output"** |
| Learning PCGs with transformers 2510.26792 | SD | harder generator family (shifts/XOR/rotation/truncation) |
| Boancă (SciTePress 2025) | SD | neural nets vs LFSR incl. degree ≥100 |
| Gohr, CRYPTO 2019 (ePrint 2019/037) | SD | neural *distinguishers* of round-reduced Speck outperform classical DDT distinguisher — learned detection of non-randomness is established in cryptanalysis |
| Yao 1982 / Blum–Micali 1984: next-bit unpredictability ⇔ indistinguishability | SD (lecture notes; attribution to Yao 1982 disputed in Reyzin's notes) | the formal backbone of "predictability = detectability" — **already known** |
| Wagenmaker–Jamieson 2002.00495; Mania–Jordan–Recht 2006.10277; Lundby et al. 2302.12667; Chatzikiriakos–Jamieson (AISTATS 2026) | SD | active system identification with guarantees/ensemble acquisition — baseline machinery for experiment design |
| Toth et al. 2206.02063 | SD | active Bayesian causal inference; class assumed to contain truth |
| Angelopoulos–Bates; Geifman–El-Yaniv; Lakshminarayanan; Ovadia; Hüllermeier–Waegeman; Tibshirani et al. | AB/SD (Phase 12) | selective/conformal/ensemble baselines |
| Le Cam; Blackwell; Manski/Tamer; Bahadur–Savage; Solomonoff/Martin-Löf; Goldwasser–Micali; SQ learning lower bounds (Kearns; Blum et al.); Chalmers *Reality+* | **NA** | background only; **no claim relies on having read them** |
Honest summary: full-text reading achieved for 3 world-model/causal papers; everything on active discovery, Blackwell/Le Cam, computational indistinguishability and Chalmers is SD/NA.

## 5. Novelty-threat matrix
| Candidate contribution | Closest existing result | Difference | Verdict |
|---|---|---|---|
| Learned latent models contain mechanism info | Ortega 2019; Mikulik 2020 (AB) | none | known |
| Predictive ≠ structural sufficiency | value-equivalent models (MuZero AB); Schölkopf Table I (TH) | counterexample style only | known |
| Learned models overconfident on non-identifiable worlds | Le Cam two-point; Ovadia (AB) | none | known |
| Hypothesis class determines abstention | misspecification theory (NA) | none | known |
| **Deterministic structure in an environment's stochasticity is learnable by sequence models up to resource-dependent limits** | Tao et al. 2025 (LCG, AB); Boancă (LFSR, SD); Gohr (SD); SQ/parity hardness (NA) | the cited works study *abstract sequence prediction*, not an embedded agent with actions in a partially observed dynamical environment | **high threat; measured-phenomenon unlikely to be new** |
| Predictability ⇔ detectability | Yao/Blum–Micali (SD) | none | known |
| **Interface asymmetry:** a reset/replay intervention on the hidden seed detects determinism of *any* generator with 2 episodes, whereas without it detection is bounded by the observer's computational power | folklore (two-sample test; derandomisation arguments); I found no source stating it for embedded observers | formulation for embedded observers and quantification via a learned world model | possibly new framing, almost surely known in components; **no claim without reading cryptography/learning-theory sources** |
| Valid, agent-computable certificate of discovered mechanism (frozen predictor on fresh data; exact recurrence verification on m bits, error ≤ 2^{-m}) | held-out testing; e-value/test martingales (NA) | assembly | engineering, not theory |
| Nested worlds | – | – | see Programme C below: reduces to hidden-state augmentation |
**Decision on originality:** no original contribution is currently identified. The best candidate is the *combined* statement (embedded learned observer + interface asymmetry + certificates + quantified practical-vs-fundamental gap), whose originality is unverified and probably modest.

## 6. The three programmes compared
| Item | A: world models as instruments of discovery | B: computationally bounded embedded observers | C: recursive / nested worlds |
|---|---|---|---|
| 1 Question | do prediction-trained latents preserve information for scientific inference? | how do environment/observer compute limits and interface access shape discoverability of generative structure? | what changes when a world-model agent's world contains another world-model agent? |
| 2 Closest literature | MuZero/value equivalence; causal repr. learning; Schölkopf | Yao/Blum–Micali; Tao et al. 2025; Gohr; SQ hardness | recursive Bayesian/game-theoretic modelling (NA) |
| 3 Theory | sufficiency hierarchy (done, known) | information-theoretic vs computational identifiability; replay-vs-prediction separation | composition of kernels: a nested world is a controlled process with larger hidden state — **no new identifiability phenomenon found** |
| 4 Empirical | structure-readout curves (done at toy scale) | detection/explanation thresholds vs state size, capacity, data, interface | cosmetic unless resource propagation matters |
| 5 Models | RSSM/Dreamer/TD-MPC2 | GRU/RSSM/Transformer sequence models + exact algebraic baseline | same |
| 6 Env complexity | needs causal/multi-dim worlds | needs a hidden *computational* generator in a dynamical world | needs matched non-nested controls |
| 7 Baselines | probes, GBM, oracle | Berlekamp–Massey, replay test, n-gram/XOR-regression | – |
| 8 Confounders | benchmark designed-in answers | extractability of the bit channel; data leakage via period | – |
| 9 Compute | local | local for n ≤ ~20 bits; larger needs GPU | local |
| 10 Meaningful negative | no divergence between predictive and causal sufficiency | learned model never beats chance at n where BM succeeds with 2n bits; replay unavailable | no new phenomenon |
| 11 P(already known) | ~0.8 | ~0.7 for the phenomenon, ~0.5 for the framing | ~0.5 (but little to know) |
| 12 Philosophy | what prediction can justify | what *kind* of evidence about the generator an embedded observer can ever get; resets/replays are interventions unavailable to us | detectability of nesting |
**Selection (scientific value over convenience):** Programme B, in the narrow form that links directly to Bostrom's detectability question — *the determinism/computational origin of the environment's stochasticity* — because (a) it admits a clean separation between three facts (information-theoretic identifiability, interface-dependent test power, computational accessibility), (b) the learned-model component then matters (it *is* the bounded observer: capacity, data, architecture define its resources), (c) it avoids hand-designed answer classes (the detector is a prediction-residual test and the explainer proposes a recurrence extracted from the model, not a label), (d) the strongest baselines (Berlekamp–Massey, replay) are exact and well understood, so negative results are interpretable. Programme A is retained only as the diagnostic of predictive-vs-structural readouts already done; Programme C is rejected as a primary direction (reduction to hidden-state augmentation; revisit only if resource-propagation yields a new proposition).
**Honest expectation:** the phenomenon (learned sequence models learn small linear recurrences; fail at larger state / sparse-parity-hard cases) is largely predicted; the experiment serves as a quantified foundation and as a test of the world-model-in-the-loop framing. A GO would require evidence of something not already in Tao et al./SQ theory.

## 7. Quality gate for the selected experiment (§16 questions)
1. Exact unknown: for an embedded learned world model that observes a partially observed dynamical world whose hidden shocks are generated by an n-bit deterministic generator, at what (n, capacity, data) does it (i) statistically detect that the shocks are predictable and (ii) extract a verified mechanism, compared with exact algebraic observers and with the replay test?
2. Known: LCG/LFSR prediction by networks in abstract streams; unpredictability ⇔ indistinguishability; BM solves LFSR with 2n bits.
3. Closest competing result: Tao et al. 2025.
4. Why necessary: to measure the embedded-agent version, including the quality of the bit channel and the effect of actions, and to quantify the learned-vs-exact gap on which the "practical vs fundamental" claim rests.
5. Supports: learned detection frontier shifts with capacity/data, with valid false-positive control; verified extraction of taps for some n.
6. Falsifies: no detection above chance at any n≥… where BM works; or detection reached only via a period-memorisation artefact; or replay-free detection tracks no resource.
7. Simpler baseline: BM on extracted bits (structured, declared class), logistic regression on lags; the replay test.
8. Negative result teaches: where learned world models cannot supply evidence about generator determinism even though it is information-theoretically identifiable.
9. World-model link: the learned model is the bounded observer.
10. Bostrom link: a PRNG-driven simulation vs true randomness is the standard "computational signature" intuition; the experiment makes the interface- and resource-dependence of that signature precise without claiming anything about our universe.
