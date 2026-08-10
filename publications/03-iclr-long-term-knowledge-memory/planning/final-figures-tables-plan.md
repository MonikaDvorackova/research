---
id: pub-03-final-figures-tables-plan
title: "Final figures and tables plan — WorldConsistMem"
type: research-notes
status: draft-plan
created: 2026-08-04
updated: 2026-08-04
---

# Figures and tables plan

Do not draw figures yet unless plotting code already exists. Specs only.

## Figure 1 — Pipeline

Evolving world → event/observation stream → memory system → dependent query bundle → constraint evaluator (Φ / CSR).

## Figure 2 — Inconsistency example

One bundle: individually plausible answers that jointly violate ≥1 constraint (prefer temporal or provenance).

## Figure 3 — Acc vs BCR/CSR

Systems on Acc (x) vs BCR and CSR (y or dual panel). Show Qwen BCR floor and CSR separation if present.

## Figure 4 — Constraint-family heatmap

Systems × constraint families: violation rate or 1−family CSR. Separate symbolic vs Qwen panels.

## Figure 5 — Difficulty / world tier

Performance by `difficulty` and `tier` (Acc, BCR, CSR).

## Tables

| ID | Content | Source |
|---|---|---|
| T1 | Benchmark comparison vs closest work | `final-novelty-positioning.md` |
| T2 | Dataset statistics | `dataset_statistics.json` |
| T3 | Symbolic system results (+ CSR) | `system_results.csv` + `partial_consistency_results.csv` |
| T4 | Qwen system results (+ CSR, PConsAcc grid) | `run2/qwen_*.csv` + partial CSV |
| T5 | Query-family results | symbolic + Qwen family CSVs |
| T6 | Constraint-family results | constraint + partial-by-constraint CSVs |
| T7 | Corruption-suite validation | `corruption_metrics.csv` / `benchmark_validation.md` |
| T8 | Limitations and coverage | FINAL_EXPERIMENT_STATUS |
