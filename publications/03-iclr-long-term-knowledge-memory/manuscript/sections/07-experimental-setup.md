---
id: pub-03-sec-07-experimental-setup
title: "Experimental Setup"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 7. Experimental Setup

All results in Sections 8–9 use **frozen** artefacts. No weights, prompts, metrics, or datasets were altered for this manuscript.

## 7.1 Conditions

**Symbolic reader condition.** Full scaled WorldConsistMem (102 worlds, 1,088 bundles, 7,140 queries). Systems include flat, latest-only, recency/BM25 retrieval, reservoir, capacity-matched flats, H0 capacity/retrieval points, and selective ablations. Predictions are stored under `outputs/scaled/predictions/`.

**Qwen reader condition (H4 Option A).** Model `mlx-community/Qwen2.5-3B-Instruct-4bit`. Subset: 18 worlds, 192 bundles, 1,260 queries. Systems: `B1_flat_cap150_compact`, `B3_recency_k8`, `B4_bm25_k8`, `H0_ltkm_cap150_ret8`. Run1+Run2 caches are frozen; Phi was not used for the final Option A decision.

## 7.2 Evidence isolation and decoding freeze

For H4, each query receives an isolated evidence pack produced by the system under its retrieval/budget rules; prompts, temperature (0), max tokens (48), evidence item cap, JSON early-stop via streaming generation, and parser are frozen (`prompt_v3_k3_mt48`). Cache keys embed model, system, query, and decoding tag. Integrity hashes for smoke, Run1 Qwen cache, and symbolic `system_results.csv` are recorded in `FINAL_EXPERIMENT_STATUS.md`.

## 7.3 Budgets and strata

Logical-record capacities include 60 / 150 / 400 (and unconstrained). Retrieval \(k\in\{3,8\}\). We stratify by world tier (small/medium/large) and bundle difficulty where reported. Constraint-family violation rates and CSR-by-family are computed from the same evaluator path as BCR.

## 7.4 Corruption validation

On smoke, controlled corruptions (single-answer edits, entity swaps, temporal mismatches, wrong provenance, transition/multihop inconsistencies, high-Acc inconsistent, consistent-wrong-world) confirm that Acc and \(\Phi\) can move in opposite directions (Section 8.1). Gold predictions achieve Acc = BCR = 1.

## 7.5 Statistics

World-level bootstrap 95% CIs; no query-level independence assumption. Symbolic and Qwen tables are reported **separately**.

## 7.6 Partial consistency recompute

CSR, violations, and PConsAcc grids are recomputed offline from frozen predictions (`partial_consistency_*.csv`). This step does not regenerate answers.
