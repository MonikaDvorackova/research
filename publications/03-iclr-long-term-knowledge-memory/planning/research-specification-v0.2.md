---
id: pub-03-ltkm-research-specification-v0.2
title: "Research Specification v0.2 — Publication 03"
type: research-notes
status: frozen-benchmark
version: 0.4-benchmark-only
created: 2026-08-01
updated: 2026-08-04
approval: provisional-team
tags: [iclr, publication-03, benchmark, consistency]
---

# Research Specification — WorldConsistMem (BENCHMARK ONLY)

**Status:** Experiments frozen. Paper shape **BENCHMARK ONLY**. Architecture superiority closed.

**Final RQ:** Under evolving synthetic worlds with dependent query bundles and machine-checkable cross-query constraints, do memory systems that achieve non-trivial per-query accuracy also produce jointly consistent answer sets—and what complementary partial-consistency diagnostics remain informative when strict bundle consistency floors?

**Object:** Cross-query consistency (\(\Phi(\hat Y;\mathcal{C})\)) vs per-query accuracy, plus CSR / PConsAcc diagnostics (BCR unchanged).

**Novelty:** INCREMENTAL BUT DEFENSIBLE — residual is dependent bundles + global constraints + Acc–consistency gap + strict/partial metrics + component diagnostics.

**H0 role:** Structured reference baseline / limitation (negative under Qwen BCR), not contribution headline.

Canonical freeze: [`final-benchmark-research-spec.md`](final-benchmark-research-spec.md), experiment status `experiments/worldconsistmem/outputs/scaled/FINAL_EXPERIMENT_STATUS.md`.
