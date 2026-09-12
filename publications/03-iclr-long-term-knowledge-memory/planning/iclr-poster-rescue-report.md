---
id: pub-03-iclr-poster-rescue-report
title: "ICLR 2027 poster rescue report — WorldConsistMem"
type: planning
status: final
created: 2026-09-07
updated: 2026-09-07
---

# ICLR 2027 poster rescue report — WorldConsistMem

**Plan:** [`iclr-poster-rescue-plan.md`](iclr-poster-rescue-plan.md)  
**PDF:** `submission/worldconsistmem.pdf` (12 pages total; Conclusion on p.7; References from p.8 → **main text ≤9**)  
**Deadlines:** abstract 2026-09-18 AOE; paper 2026-09-25 AOE.

---

## Changes made

### Packaging / venue
- Switched style from ICLR 2026 → **ICLR 2027** (`iclr2027_conference.sty` / `.bst`).
- Header now reads “Under review as a conference paper at ICLR 2027”.
- Added mandatory **AI Use Statement** (outside page limit).
- Kept Ethics + Reproducibility; acknowledgements omitted for double-blind.
- Refreshed OpenReview source zip: `submission/package/worldconsistmem-openreview.zip`.

### Page-budget / presentation (P0)
- Compressed §§1–10 aggressively; merged Systems+Setup; shortened Related Work / Metrics / Failures / Discussion.
- Results now begin by page 4 (was ~9).
- Main scientific body through Conclusion fits in **7 pages** (desk-reject risk from overlength removed).
- Figure captions state takeaways (pipeline; inconsistency example; Acc/BCR/CSR divergence; family heatmap).

### Scientific hygiene (P0; no invented numbers)
- Audited headline Acc/BCR/CSR/Abs/Mal against frozen CSVs in `/Users/monikadvorackova/worldconsistmem-experiments/results/scaled/` (half-up 3-decimal display rule preserved: B3 BCR **0.063**, H0 Abs **0.483**).
- Synced markdown tables `t3` / `t4` to the same display rule.
- Surfaced world-level bootstrap CIs for BCR/CSR (symbolic + Qwen) from frozen CSVs; avoided juxtaposing query-pooled Acc with world-Acc CIs that do not contain the pooled point.
- Strengthened BCR-floor defense: gold/symbolic satisfiability + Qwen multi-violation + transition 192/192 + labelled H4 gold re-eval.
- Surfaced frozen tier (history-length proxy) Acc–BCR divergence in Results.
- Removed internal filename leak (`difficulty_results.csv`) from PDF prose.
- Preserved explicit “architecture superiority not supported”; conclusion is measurement-first.

### Experiment repo note
- Research tree `experiments/worldconsistmem/` is **empty**; runnable code + freeze live in `~/worldconsistmem-experiments/`. Reproducibility depends on packaging that external repo as anonymized supplementary.

---

## Experiments run

### Frozen (not re-run; audited only)
- Smoke corruption suite; symbolic scaled 102/1088/7140; Qwen H4 Option A; partial consistency recompute; difficulty/tier stratification; world bootstrap CIs.
- Pytest in experiment repo: **92 passed**.

### NEW labelled runs (not mixed with Option A freeze)
Artefacts: `planning/rescue_p1_artifacts/`

| ID | Command / protocol | Result |
|---|---|---|
| `rescue_p1_h4_gold_sanity` | Regenerate H4 subset (seed 100; first 6 worlds/tier); gold `Prediction`s; `evaluate_predictions` | Acc=1.0, BCR=1.0, ConsAcc=1.0, violations=0 |
| `rescue_p1_alt_seed_symbolic_mini` | Symbolic B3/B4 k8; `worlds_per_tier=6`; seeds 100/101/102 | Acc–BCR gaps persist (B3 Gap≈0.504; B4 Gap≈0.336–0.338) |

Exact gold command pattern (research workspace):

```bash
PYTHONPATH=$HOME/worldconsistmem-experiments/src python3 - <<'PY'
# see planning/rescue_p1_artifacts/RESCUE_P1_EXPERIMENT_STATUS.md
PY
```

Seed mini JSON: `planning/rescue_p1_artifacts/alt_seed_symbolic_mini.json`.

**Not run (deferred / unsafe for deadline):** Phi or larger LLM readers; full multi-seed 34-world/tier regeneration; relation-density generator sweeps requiring new knobs; external transfer benchmarks.

---

## Validation performed
- Tectonic compile of `submission/latex/worldconsistmem.tex` (ICLR 2027).
- Page map: Conclusion p.7; References p.8; appendix p.9–12.
- Anonymity scan: no `/Users/`, no author name, no experiment-repo path, no `planning/` paths in PDF.
- Numeric audit vs frozen CSVs: PASS under declared rounding rule.
- Citations render in References (natbib resolved under tectonic).

---

## Remaining risks

| Risk | Status |
|---|---|
| Incremental novelty vs SetCons/LogicVault + LTM Acc suites | Residual is sharp but still **incremental**; reviewers may want a stronger LLM reader. |
| Weak 3B Qwen + high abstention | Scoped honestly; still a credibility hit for poster vs oral. |
| Empty `experiments/worldconsistmem/` in research git | Must upload anonymized code/data zip from experiment repo. |
| Seed mini-study nearly identical across seeds | Suggests limited seed diversity at wpt=6; do not overclaim seed robustness. |
| Compact-flat symbolic saturation | Fairness caveat remains; some reviewers will dislike BCR=1 at cap150. |
| AI-use statement is honest but generic | Authors should edit to match actual coauthor AI practices before abstract deadline. |
| Reciprocal reviewing / author quotas (ICLR 2027) | Process risk outside the manuscript. |

---

## Reviewer objections still unresolved
1. “Consistency benchmarks already exist” — rebutted by residual, but not eliminated.
2. “Synthetic worlds only” — correctly scoped; no external validation yet.
3. “BCR=0 means nothing works / metric broken” — substantially mitigated by gold H4 BCR=1 + multi-violation diagnostics; still needs careful reading.
4. “Only a 3B reader” — unresolved without optional P2 model.
5. “Why is compact flat perfect symbolically?” — caveat present; may still draw fire.

---

## Updated subjective acceptance assessment

| Track | Assessment |
|---|---|
| Desk-reject (format/page/anonymity) | **Likely avoided** if OpenReview upload uses the new PDF + 2027 checklist items. |
| Poster | **Borderline but plausible** if reviewers accept a clean measurement contribution with honest negative architecture result and defended BCR floor. |
| Oral | **Unlikely** without stronger readers / broader validation. |
| Reject (scientific) | Still possible on novelty + synthetic + weak LLM grounds. |

**Probability mass (subjective, not a forecast):** poster-or-better ~25–40% if supplementary code is solid; reject ~60–75%. Up from near-certain desk-reject/overlength before this rescue.

---

## Final recommendation

### **Submit** (with conditions) — do **not** delay solely for more models.

Conditions before abstract/paper deadlines:
1. Upload anonymized experiment code+data supplementary (from `worldconsistmem-experiments`), not an empty research path.
2. Coauthors review AI Use Statement and author-list / reciprocal-reviewing compliance.
3. Do **not** revive architecture superiority; keep BCR=0 + CSR diagnostics foregrounded.
4. Optional if time: one stronger local reader as clearly labelled appendix — only if complete before 2026-09-25.

**Delay** only if supplementary artefacts cannot be anonymized in time, or if coauthors require a larger LLM study before standing behind the Qwen floor narrative.

**Redirect** (workshop / extended tech report) if the team cannot defend synthetic-only + 3B-reader scope at ICLR; the measurement object remains publishable elsewhere.

---

## Changed files (this rescue)
- `planning/iclr-poster-rescue-plan.md` (new)
- `planning/iclr-poster-rescue-report.md` (this file)
- `planning/rescue_p1_artifacts/*` (new labelled experiment outputs)
- `submission/latex/worldconsistmem.tex` + `sec_*.tex` (compressed rewrite; ICLR 2027)
- `submission/latex/iclr2027_conference.sty/.bst` (added)
- `submission/worldconsistmem.pdf` (rebuilt)
- `submission/package/worldconsistmem-openreview.zip` (refreshed)
- `manuscript/tables/t3-symbolic-system-results.md`, `t4-qwen-system-results.md` (rounding sync)

No commits created. JURIX and other publications untouched.
