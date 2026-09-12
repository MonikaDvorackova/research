# ICLR Scientific Audit — WorldConsistMem

Date: 2026-09-08  
Authoritative manuscript: `submission/latex/worldconsistmem.tex` (ICLR 2027 style)  
Compiled PDF: `submission/latex/worldconsistmem.pdf` → `submission/worldconsistmem.pdf`  
Stale/duplicate sources (do not edit as primary): `manuscript/*.md` (draft markdown); `submission/package/worldconsistmem-openreview/` (packaging snapshot).

## Baseline compile (pre-revision)

| Item | Status |
|------|--------|
| Style | `iclr2027_conference` |
| Anonymity | Anonymous authors; no identity strings in prior PDF text extract |
| Main text | Conclusion ~p.8; References start ~p.8; Appendix from ~p.9 (≤9 main) |
| Total PDF pages | ~13 (incl. appendix) |
| Option A hashes | `system_results.csv` `eb5bd5fa…`; manifest `37aa8604…` (verified separately) |

## Reviewer-style issue table

| Issue | Severity | Location | Likely objection | Available evidence | Required correction | New experiment? |
|-------|----------|----------|------------------|--------------------|---------------------|-----------------|
| Central claim slightly diffuse (“benchmark + results”) | Major | Abstract/Intro/Conclusion | Incremental benchmark only | Acc≠BCR formalization; B2/B3-k3; B4 gap; corruption | Unify one falsifiable claim across Abs/Intro/Results/Conclusion | No |
| Residual novelty vs SetCons/LogicVault undersold in first 2 pages | Major | Intro/Related | Distinction unclear | Related § + App Table closest | Explicit evaluation-object residual early; what BCR detects that Acc/LTM Acc miss | No |
| “Retrieval difficulty, not consistency” not preempted | Major | Results/Discussion | Gap is just hard retrieval | Identical Acc different BCR; shortcuts majority Acc>0 BCR=0; consistent_wrong_world Acc low BCR=1; gold H4 BCR=1 | Dedicated paragraph + discussion alternative explanations | No |
| BCR edge cases / scope underspecified | Moderate | Object/Metrics | Metric ill-motivated | Code: empty C → CSR=1; Φ joint ∀c | State range, empty-C, what Gapq means/doesn’t mean | No |
| Single 3B Qwen + BCR=0 floor | Major | Results/Limitations | Empirical evaluation too limited | Explicit limitation; gold sanity NEW; CSR | Keep visible; do not overclaim; no fake stronger-reader results | Yes for scale (not performed) |
| B3 seed identical outcomes | Moderate | Robustness | Robustness overclaimed | Already narrowed in text | Keep; do not present as replication | Yes for diverse generators (not performed) |
| B1 compact Acc=BCR=1 may look unfair | Moderate | Systems/Results | Unfair comparison | App fairness caveats | One main-text sentence pointing to caveat | No |
| Alternative explanations thin | Major | Discussion | Conclusions exceed evidence / confounders | Tiers, density null, distractors null, shortcuts, retrieval budget | Expand Discussion: alternative explanations subsection | No |
| Qualitative real prediction example weak | Moderate | Failures | Can’t see failure concretely | Fig2 schematic; Qwen transition 192/192; violation tables | Add compact real-data-backed example table if extractable; else strengthen Fig2 linkage + Qwen transition fact | Prefer extract from frozen preds |
| Synthetic scope | Major | Benchmark/Limitations | No transfer | Synthetic-why § | Keep; sharpen transfer vs non-transfer | Yes for NL transfer (not performed) |
| Consistency ≠ factual correctness | Moderate | Discussion | Metric confusion | Corruption consistent_wrong_world | Explicit sentence | No |
| Packaging/repro in abstract | Minor | Abstract | Noise | — | Keep scientific; repro in statement only | No |
| Figure generators missing | Minor | Figures | Repro of art | FIGURE_REPRODUCIBILITY.md | Do not claim bit-exact redraw | No |
| Incremental vs LTM Acc suites | Major | Related | Incremental | Closest-work table | Keep Acc+BCR+CSR primary metric framing | No |

## Dimensions (summary verdicts)

### A. Central claim
**Present but needs tighter unification.** Strongest accurate claim:  
*Under known gold evolving histories, per-query Acc can materially overstate whether dependent answers jointly satisfy world-history constraints; BCR and Gapq = Acc−BCR measure that discrepancy, and Acc-only ranking can mis-order systems.*

### B. Novelty
**Defensible residual, not “first consistency metric.”** Residual = memory systems + evolving multi-entity gold worlds + world-history-derived Φ (validity/transition/provenance/relations), jointly scored. Must stay explicit vs SetCons/LogicVault and vs LTM Acc.

### C. BCR
**Formally defined; needs edge cases + interpretation bounds.** Implementation aligns with Φ=∀c, BCR=mean_b Φ_b.

### D. Leakage / construction
**Controls exist** (no gold to systems; gold-only scoring; distractor flags; corruption suite; shortcuts). Must surface “not retrieval-only” more clearly.

### E. Fairness
**Documented caveats** (capacity metadata tax; compact padding; symbolic≠Qwen pooling). Main text must flag B1 saturation.

### F. Statistics
**World CIs exist for BCR/CSR**; identical-Acc example is strongest robustness-independent finding. Seed diversity weak (honest). Model scale weak (honest).

### G. Alternatives
**Partially addressed** by corruption + shortcuts + budget; needs dedicated discussion.

### H. Qualitative
**Schematic Fig2 strong;** need tighter tie to empirical Qwen transition failure / symbolic transition families.

### I. Limitations
**Mostly good;** add consistency≠factual correctness; ontology dependence; prompt sensitivity.

### J. Writing
**First two pages mostly work;** Results still a bit inventory-like—reframe as RQs.

## Experiments explicitly NOT performed this round
- Stronger LLM readers / Qwen re-inference  
- Alternate natural-language generator  
- Full `run_scaled_study` regeneration  
- Bit-exact figure redraw  

## Priority edit plan (implemented)
1. Unify central claim wording Abs/Intro/Conclusion — done  
2. Intro: novelty residual + “not just retrieval” preview — done  
3. Object: Gapq interpretation; empty-C; scope — done  
4. Results: RQ framing; fairness callout — done  
5. Discussion: alternatives + threats — done  
6. Conclusion: demonstrated / bounded significance / next step — done  

## Post-revision compile (2026-09-08)

| Item | Status |
|------|--------|
| Compile | `tectonic` OK → 14 pages |
| Main text | Conclusion ends p.8 (≤9) |
| AI Use + References | start p.9 |
| Appendix | start p.10 |
| Anonymity | Pass (no identity strings in PDF text extract) |
| Undefined citations (final) | None |
| Option A hashes | Unchanged (`37aa8604…`, `eb5bd5fa…`) |
| Result consistency | `RESULT_CONSISTENCY_REPORT.json` `n_fail=0` |
| B2 vignette | Implemented main-text Table `tab:b2vignette`; Acc=0.75 / Φ=0 from frozen B2 preds (6/8; not 3/4) |
| Extraction utility | `scripts/extract_b2_vignette.py` exit 0; `tests/test_extract_b2_vignette.py` 2 passed |
| ICLR 2027 page limit | Main text ends on p.9 (≤9); refs p.9+; appendix p.10+ |
| AI Use Statement | Present p.9; excluded from page limit per official guidelines |
## Post-confirmatory status (2026-09-08)

Executed: $\Acc^{n}$ diagnostic; naturalistic transfer $n{=}36$; Qwen parser sensitivity; Phi blocker documented.  
Manuscript updated (RQ1–RQ4); main text ends p.6–7 (≤9).  
Option A hashes unchanged.  
Stronger LLM inference **not** completed (environment blocker).  
See `ICLR_ACCEPTANCE_ACTION_PLAN.md`, `ICLR_FINAL_READINESS.md`, `ICLR_SIMULATED_REVIEWS.md`.

## Honesty pass (2026-09-09)

**Finding:** Confirmatory NL transfer and Qwen parser studies were at risk of overclaim. Audited artefacts (`results/confirmatory/naturalistic_transfer/analysis/claim_audit_report.json`) show:

- Transfer = 36 scenarios × 4 queries = 144; gold Acc=BCR=1; last-event Acc=0.208 BCR=0 with Acc CI [0.174,0.236].
- No LLM on NL scenarios; stronger reader blocked (API estimate only).
- Qwen Acc ≈0.075–0.187 under all parsers with BCR=0 → **difficulty floor**, not high-Acc divergence.
- Last-event BCR=0 ≈ independence reference under low $p$ (role-product = 0).

**MS correction:** Abstract/Intro/RQ4/Conclusion/Discussion narrowed to bounded conclusions; compact Table `tab:confirmatory`; parser/role details moved to App `app:parser` / `app:transfer`.

**Verdict:** Primary frozen symbolic Acc–BCR case intact. Confirmatory evidence does **not** upgrade the paper to multi-model/NL Acc–BCR confirmation. Strongest remaining rejection risk: missing meaningful-Acc stronger/NL reader.
