---
id: pub-03-iclr-hostile-reviewer-audit-v2
title: "ICLR hostile-reviewer audit and prioritized rescue plan v2"
type: planning
status: active
created: 2026-09-07
updated: 2026-09-07
---

# Hostile-reviewer audit + prioritized rescue plan (v2)

**Target:** maximize ICLR 2027 poster acceptance probability.  
**Constraint:** Option A freeze immutable; new runs labelled separately.  
**Environment blocker:** stronger local LLM readers require `mlx_lm` + model weights; currently unavailable (`ModuleNotFoundError: mlx_lm`) and disk ≈2.1 GiB free. Phi was listed in code (`H4_MODELS`) but **not** executed for Option A and **cannot** be executed in this environment now.

---

## Number provenance (current PDF)

| Claim / number | Source | Status |
|---|---|---|
| 102 / 1,088 / 7,140 | freeze `FINAL_EXPERIMENT_STATUS.md`, `dataset_statistics.json` | Frozen |
| Corruption Acc/BCR | `results/corruption_metrics.csv` | Frozen |
| Symbolic Acc/BCR/CSR + CIs | `system_results.csv`, `partial_consistency_results.csv` | Frozen |
| Qwen Acc/BCR/CSR/Abs/Mal | `run2/qwen_system_results.csv`, partial CSR | Frozen Option A |
| Transition 192/192; viol. multiplicity | `partial_consistency_findings.md` | Frozen |
| H0 ablations Acc/BCR | `ablation_results.csv` / statistical_analysis | Frozen; **under-surfaced in PDF** |
| Tier Acc/BCR | `difficulty_results.csv` | Frozen |
| H4 gold Acc=BCR=1 | `planning/rescue_p1_artifacts/h4_gold_sanity.json` | Labelled NEW |
| Seed mini 100–102 | `planning/rescue_p1_artifacts/alt_seed_symbolic_mini.json` | Labelled NEW |

---

## Reviewer 1 — novelty / significance

**Likely attack:** BCR is Acc rebranded; consistency already studied (SetCons/LogicVault); synthetic diagnostic is not significant.

**Current defense strength:** Medium. Residual is precise (memory + evolving gold world + world-history Φ) but incremental.

**Must tighten:** One failure-mode sentence as the spine; Acc vs Φ as different mathematical objects; synthetic framed as diagnostic instrument.

---

## Reviewer 2 — methodology / validity

**Likely attack:** Gap from generator shortcuts, distractors, density, prompt, leakage, weak reader, compact-flat artifact.

**Evidence already available:** corruption suite Acc≠BCR; gold BCR=1; `assert_no_gold_leakage`; frozen H0 component ablations; tier stratification.

**Missing / blocked:** stronger reader; controlled density/distractor/contradiction sweeps (code knobs exist; not yet reported); empty-evidence / prior baselines.

---

## Reviewer 3 — reproducibility / empirical strength

**Likely attack:** cannot reproduce; empty research `experiments/`; only 3B Qwen; seed mini too small/identical.

**Defense:** experiment repo exists off-tree; 92 tests pass; freeze checksums documented. **Upload anonymized code is mandatory.**

---

## Prioritized plan

### A. Must-fix before submission
1. Rewrite abstract/intro around one Acc–BCR failure mode.
2. Explicit Acc vs Φ math + evaluation object.
3. Threat-to-validity + reproducibility subsections.
4. Robustness subsection for labelled NEW experiments (separate tables).
5. Surface frozen H0 ablations (archive/temporal/graph/conflict).
6. Leakage/shortcut controls (empty evidence; no-distractor; majority/prior if feasible).
7. Generator robustness sweeps (density, distractors, seeds) as labelled NEW.
8. Keep page budget ≤9 main; anonymized code zip reminder.
9. Honest statement: stronger LLM reader **not completed** in this environment.

### B. High-value if feasible
1. Phi / larger Qwen H4 as labelled NEW (blocked now).
2. Broader seeds with world CIs (partially doable symbolically).
3. Contradiction-depth / dependency-depth sweeps (needs generator surgery → only if cheap).

### C. Nice-to-have (do not delay)
1. External transfer to another Acc suite.
2. Figure redesign for poster.
3. Effect-size tables beyond existing CIs.

---

## Per-change ledger (implementation targets)

| Change | Risk addressed | Evidence | Edit target | Affects freeze? | New compute? |
|---|---|---|---|---|---|
| Abstract/intro rewrite | R1 significance | existing | `worldconsistmem.tex`, `sec_intro.tex` | No | No |
| Acc vs Φ formal contrast | R1/R2 | metrics defs | `sec_object.tex`, `sec_metrics.tex` | No | No |
| Threat-to-validity | R2 | audit | `sec_discussion.tex` | No | No |
| Robustness subsection + table | R2/R3 | NEW runs | `sec_results.tex`, appendix | No | Yes (symbolic) |
| Surface ablations | R2 causal | `ablation_results.csv` | results/appendix | No | No |
| Density/distractor/seed sweeps | R2 generator | NEW | labelled artefacts | No | Yes |
| Empty-evidence baseline | R2 leakage | NEW | labelled + results | No | Yes |
| Stronger reader | R3 model dep. | blocked | N/A | No | **Impossible now** |
| Anonymized code package note | R3 repro | env | checklist/report | No | Manual |
