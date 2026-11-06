# 24 — Out-of-language discovery experiments (Phase 22)

Protocol: doc 23 (committed as `bcf9c9c` before the calibration, development and holdout runs). Internal analysis; development-stage evidence only; no confirmatory run. Raw results: `implementations/epistemic-identifiability/results/ool_dev/` (`*_report.md` carry every table; `*_long.pkl` the per-instance rows). Manifest sha256 `f8a09dea01ca1d3807237bd4b041d8ab354c5a78378758a62cbaf40ccbced1d2`.

## 1. What was run
| step | namespace / seeds | content | size |
|---|---|---|---|
| baseline tuning | instance seeds 310–312 | SINDYc, weak-SINDy, implicit-SINDy grids (library × threshold × variable set); Kalman q | 33 instances |
| calibration | 29000 | L0 agent (falsify design) on 5 correctly specified families, B ∈ {5,8,12} | 60 instances |
| development | 30000 | 6 families × 10; 9 agent variants, oracle-structure, 11 cheap baselines at B ∈ {5,8,12}; PySR (6 fits × B ∈ {8,12}) | 60 instances (PySR: 58; thresh 0 and thresh 3 hung Julia and are missing) |
| frozen holdout | 31000 | 7 families × 10, same conditions, run **once** after freezing agent/thresholds/baselines | 70 instances (PySR: 69; saw 9 missing) |
| stress tests | 32000 | noise ×1/×2/×3, no-u2 pool; 5 families × 6; 4 agent variants | 4 × 30 instances |
Every instance uses ≤ 12 episodes of T = 80 steps; test = 24 fresh programmes. No new neural training: the biGRU state estimator of doc 20 (3 seeds) was reused unchanged. PySR: 696 + 828 fits. Wall-clock (shared, heavily loaded M4 Pro): dev agents 1 050 s, holdout agents 2 472 s, PySR ≈ 18 + 25 min with 7–8 workers.

## 2. Calibrated criticism (H4)
Thresholds c_in(B) = 2.92 / 2.96 / 3.47 (−log₁₀ p) and c_oos(B) = 10.5 / 4.5 / 2.5 at B = 5/8/12, from 60 valid fits per B. Per-family false rejection of the correct L0 explanation on the calibration namespace: 0–0.17 (delay 0.08/0.08/0.17, gate 0.08/0.08/0.08, lin 0.08/0.08/0.0, quad 0, sat 0). On the dev control `lin` (n = 10): false rejection **0.00** at all B. Power against out-of-L0 mechanisms: dev 0.75 / 0.75 / 0.78, holdout 0.42 / 0.60 / 0.60 (AUROC dev 0.90 / 0.92 / 0.94). **The ≥ 0.8 power criterion of doc 23 fails.** The shortfall is structural: calibrated criticism never fires on mechanisms that a two-term L0 hypothesis already predicts within noise — `sin` (L0 rejection 0.0–0.1), `bump` (0.0), `sqrtabs` (0.0) — while it always fires on `rectsq`, `leak`, `bilin`, `quadlag`, `rate` (B ≥ 8) and `gdelay`. High AUROC and good calibration therefore coexist with a blind spot defined by predictive near-equivalence, which no goodness-of-fit test can remove.

## 3. Primary results (identifiable out-of-L0 mechanisms; 95 % stratified bootstrap over instances)
L1 = predictive (RMSE ≤ 0.05 on 24 fresh programmes); L2 = structural (term set equals the manifest signature); L3 = L2 with parameter tolerance (L3 = L2 everywhere here).
| | dev B=8 L1 | dev B=12 L1 | dev B=12 L2 | holdout B=8 L1 | holdout B=12 L1 | holdout B=8 L2 | holdout B=12 L2 |
|---|---|---|---|---|---|---|---|
| adaptive agent (`adapt_sweepB`) | 0.93 [0.82,1.00] | 0.97 [0.93,1.00] | 0.55 [0.45,0.65] | 0.94 [0.88,1.00] | 1.00 [1.00,1.00] | 0.44 [0.38,0.50] | 0.38 [0.32,0.44] |
| agent + falsify design | 0.93 | 0.97 | 0.53 | 0.90 | 0.98 | 0.50 | 0.50 |
| fixed-language search (L0) | 0.57 | 0.70 | 0.00 | 0.80 | 0.90 | 0.00 | 0.00 |
| **static broad grammar** (`all_sweepB`) | 0.88 | 0.95 | **0.62** [0.50,0.75] | 0.90 | 1.00 | **0.78** [0.70,0.86] | **0.70** [0.60,0.78] |
| oracle structure (privileged) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| PySR fixed, Kalman state | 0.05 | 0.05 | – | 0.30 | 0.28 | – | – |
| PySR expanded, Kalman state | 0.07 | 0.03 | – | 0.20 | 0.24 | – | – |
| PySR expanded, learned state | 0.10 | 0.20 | – | 0.24 | 0.28 | – | – |
| PySR expanded, **oracle state** (privileged) | 0.60 | 0.65 | – | 0.38 | 0.80 | – | – |
| PySR expanded, raw observations (role A) | 0.07 | 0.03 | – | 0.02 | 0.00 | – | – |
| SINDYc (Kalman / oracle state) | 0.20 / 0.12 | 0.25 / 0.15 | – | 0.02 / 0.00 | 0.00 / 0.00 | – | – |
| weak-SINDy / implicit-SINDy | 0.17 / 0.00 | 0.20 / 0.00 | – | 0.00 / 0.00 | 0.00 / 0.00 | – | – |
| ridge NARX | 0.20 | 0.23 | – | 0.02 | 0.10 | – | – |
| Hammerstein static map | 0.40 | 0.72 | – | 0.26 | 0.40 | – | – |
Paired L1 differences (agent − competitor), holdout B=12: PySR-fixed/Kalman +0.72 [0.62,0.80], PySR-expanded/Kalman +0.76 [0.66,0.86], PySR-expanded/learned +0.72 [0.62,0.82], PySR-expanded/oracle state +0.20 [0.14,0.26], Hammerstein +0.60 [0.54,0.68]; dev B=12: PySR-expanded/Kalman +0.95 [0.88,1.00], Hammerstein +0.25 [0.12,0.38]. Paired L2 differences against `static_all`: dev −0.07 [−0.20,0.05], **holdout −0.34 [−0.40,−0.28] (B=8), −0.32 [−0.38,−0.24] (B=12)**; against PySR's coarse token signature (families where definable) holdout +0.30 [0.23,0.38] / +0.17 [0.05,0.28] (Kalman state), +0.05 [−0.07,0.17] (learned, B=12), −0.17 [−0.28,−0.07] (oracle state, B=12).
Per-family (holdout, B=12, L1/L2 of the agent / of `static_all`): bump 1.0/0.0 vs 1.0/0.9; sqrtabs 1.0/0.0 vs 1.0/0.7; rate 1.0/0.8 vs 1.0/0.8; gdelay 1.0/0.1 vs 1.0/0.1; quadlag 1.0/1.0 vs 1.0/1.0; dev: sin 1.0/0.0 vs 1.0/0.6; rectsq 1.0/0.4 vs 1.0/0.4; leak 1.0/0.9 vs 1.0/1.0; bilin 0.9/0.9 vs 0.8/0.5.
**Predictive vs structural**: the agent's L1 − L2 gap (predictive but not structural) is 0.42 (dev, B=12) and 0.62 (holdout, B=12); typical wrong structures are `abs(id)+sq(id)` for `rectsq`, `dz+tanh` for `sin`/`bump`/`sqrtabs` — the counterexample class of P2 in doc 23, observed.

## 4. Decisions, abstention, non-identifiable and beyond-closure cases (full agent, calibrated, falsify design)
* `saw` (outside every stage vocabulary): calibrated criticism rejected L0 in 10/10 and the agent output **abstain_ool in 10/10 at B = 5, 8 and 12** (also reported: its best-BIC surrogate has L1 = 0, RMSE ≈ 0.27, so nothing was falsely claimed). Abstention accuracy on this family 1.0 (n = 10 per B).
* Non-identifiable (`thresh`, `bumpfar`): the null (empty-structure) explanation was claimed in 0.8–1.0 of instances (adapt_sweepB L2: thresh 0.9 at B=8; bumpfar 0.8); no spurious structure was claimed otherwise except 1–2 of 10 per B.
* **False discovery among claims** (wrong-structure claims / claims, all families): dev B=5/8/12: 12/34, 18/46, 22/55; holdout 13/34, 20/49, 21/51 — about 0.40 at B=12, far above the 0.10 target of the informal acceptance criterion; the dominant source is mechanisms that L0 approximates (the claim is made from L0 and is wrong-structured), plus `rectsq` and `bump`/`sqrtabs` ambiguity.
* The `lin` control: L2 is only 0.5–0.7 (L0 often prefers `tanh` or a spurious second term, nearly equivalent within the actuator range) — an over-strict equivalence relation, reported as is.

## 5. Intervention efficiency (H3) and world-model contribution (H2)
* **H3 not supported.** Mean first budget with a correct claim (16 if never): dev falsify 11.85 vs sweepB 11.07 (falsify − sweepB +0.78 [0.12,1.43], i.e. *worse*), vs random 11.38 (+0.47 [−0.88,1.85]); holdout falsify 11.28 vs sweepB 11.88 (−0.60 [−1.42,0.22]) and random 12.18 (−0.90 [−1.96,0.14]); versus the NARX-ensemble-variance design falsify is better in both (−1.10 [−1.80,−0.40], −1.92 [−2.72,−1.20]). The sign of the falsify-vs-sweep difference reverses between dev and holdout; no consistent efficiency advantage. Falsify costs 4–5× the wall-clock (55–89 s vs 14–20 s per instance).
* **H2 not supported; the learned world model is removed from the recommended architecture.** Learned vs classically reconstructed state, paired L1: PySR-expanded B=12 dev +0.17 [0.05,0.30], holdout +0.04 [−0.10,0.16]; SINDYc dev −0.15 [−0.25,−0.05], holdout 0.00; weak-SINDy ≤ 0. Stage ordering by learned-latent (or Kalman) equation-error evidence leaves L1 and L2 **identical** to the default order on both splits (differences 0.00 [0.00,0.00]) and changes candidates evaluated inconsistently (dev 3 264 vs 1 830 for the default order; holdout 936 vs 1 400), with learned = Kalman. Role A (PySR on raw observations): Kalman-state PySR beats it by +0.18 [0.08,0.28] / +0.24 [0.14,0.34] on the holdout and ties on dev; a hidden-state reconstruction therefore helps equation discovery, but the privileged oracle state helps far more (+0.56 [0.44,0.66] at B=12 holdout), i.e. reconstruction error, not the missing operator library, is the PySR bottleneck. The GRU reconstruction is better than the tuned Kalman smoother in state error (0.11 vs 0.21 relative RMSE on 18 tuning instances) but not reliably better downstream. Role of neural intervention prediction (`adapt_ens`): worst design in both splits.

## 6. Cost of discovery (median per instance at B = 12)
| method | candidates evaluated | fit wall s (dev / holdout) |
|---|---|---|
| fixed-language L0 | 540 | 5 / 12 |
| adaptive (sweep design) | 1 830 / 1 400 | 14 / 20 |
| adaptive + falsify | 7 161 / 5 850 | 55 / 89 |
| static broad grammar | 3 522 | 7 / 8 |
| PySR fixed / expanded | – | 6–10 / 10–17 (per fit, 40 iterations, serial) |
| SINDYc / weak / NARX / Hammerstein | – | ≤ 0.6 |
Adaptive expansion evaluates fewer candidate columns than the static grammar (0.4–0.5×) but takes *longer* wall-clock because each staged revision repeats the search (14–20 s vs 7–8 s); there is no efficiency advantage in time, only in candidate count, and the accuracy is lower. The 'candidate' metric favours the adaptive loop; wall-clock does not.

## 7. Failure boundary (doc 23 §9; development families, 6 instances per family, no CIs: 24 instances per cell)
Agent `adapt_sweepB` / `static_all` at B=12, L1 / L2: noise ×1 1.00/0.54 vs 0.96/0.54; ×2 0.96/0.46 vs 1.00/0.71; ×3 0.96/0.25 vs 0.96/0.58; no-u2 pool 1.00/0.38 vs 1.00/0.46. L0-rejection (power) falls with noise: 0.79 → 0.71 → 0.50. Predictive recovery degrades slowly; structure recovery of the criticism-triggered loop collapses faster than that of the static grammar (0.25 vs 0.58 at ×3). Untested or not implemented, per the brief's list: stiff dynamics, stacked/higher-complexity mechanisms, reconstruction-error injection beyond the front-end comparison, incorrect-threshold sweeps (decisions can be recomputed from stored statistics; not done), strongly correlated rivals beyond the observed `rectsq` vs `abs+sq` confusion (L2 0.4).

## 8. Failures, negative findings, caveats (not removed)
1. Pre-registered **H1's adaptive clause failed**: `static_all` matches (dev) or beats (holdout, +0.32–0.34 L2) the adaptive loop; the always-on BIC comparison across languages, not criticism-triggered expansion, drives structure recovery.
2. **H3, H2 and H4-power failed** as stated in doc 23.
3. The criticism trigger is blind to mechanisms predictively imitated by L0 (`sin`, `bump`, `sqrtabs`).
4. Joint maximum-likelihood fitting of the Kalman model collapsed to a degenerate solution (§ doc 22).
5. Weak-SINDy first crashed (pysindy 2.1.0 one-column state; AxesArray matmul) and was fixed before the final tuning run; the first tuning table with weak = 99.0 (= exception) was superseded and rerun (same command, same code after the fix). The background tuning job ran twice (a duplicated launch); the surviving file is from the final run.
6. PySR/Julia hung on three instances (thresh 0, thresh 3, saw 9) even with a 60 s fit timeout; they are missing from the PySR comparisons (pairing is by instance), not imputed.
7. Honest limits: the agent's stage vocabularies were written by the benchmark's author, so `sin`, `bump`, `sqrtabs`, `relu∘sq`, `gate∘delay`, `sq∘lp`, `lp`, `rate`, `x₁x₂` are *in the closure by construction*; only `saw` and the two non-identifiable families lie outside. PySR/SINDy results use my pipelines (equation-error on a reconstructed state with a tapped delay line); an output-error (simulation-based) PySR variant does not exist off the shelf and would be a fairer, much stronger comparator. The holdout namespace 31000 and dev namespaces 29000–32000 are consumed; the holdout was run once but both agent and benchmark share an author, so it is not an independent confirmation. The structural check for PySR is a coarse token heuristic. 10 instances per family give wide family-level intervals; pooled CIs resample instances only (no seed-level variance for the GRU).
8. Code changes after the protocol commit `bcf9c9c` and before any calibration/dev/holdout run: baseline module fixes and additions (weak-SINDy predictor, role-A raw PySR, profiled Kalman, `simulate`), `propose_order`/callable stage order and `sweep_ids` in `loop.py`, and the run/report scripts. The agent's search, criticism and decision logic and the manifest were not changed after the protocol commit; the PySR runner was changed once more after the first (hung) dev attempt (incremental saving, executor), with no change to what is fitted.
