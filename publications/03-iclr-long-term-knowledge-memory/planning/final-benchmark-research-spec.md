---
id: pub-03-final-benchmark-research-spec
title: "Final benchmark research specification — WorldConsistMem"
type: research-notes
status: frozen
created: 2026-08-04
updated: 2026-08-04
---

# Final benchmark research specification

## Paper shape

**BENCHMARK ONLY**

Central contribution: cross-query consistency exposes failures that isolated per-query accuracy does not characterize.

Not central: hierarchical LTKM / H0 architecture superiority.

## Final research question

**RQ.** Under evolving synthetic worlds with dependent query bundles and machine-checkable cross-query constraints, do memory systems that achieve non-trivial per-query accuracy also produce jointly consistent answer sets—and what complementary partial-consistency diagnostics remain informative when strict bundle consistency floors?

## Objects

- Evolving deterministic gold world histories.  
- Dependent query bundles (current / historical / transition / relational / provenance / multi-hop / conflict views).  
- Machine-derived constraint set \(\mathcal{C}\) scored jointly over predicted answers.  
- Strict metrics: Acc, BCR, ConsAcc, Gap_query, Gap_bundle.  
- Complementary metrics: CSR, violations/bundle, PConsAcc grid (Acc τ ∈ {0.5, 0.8}, CSR τ_c ∈ {0.8, 0.9}).

## Closed experiments

See `experiments/worldconsistmem/outputs/scaled/FINAL_EXPERIMENT_STATUS.md`.

## H0 role

H0 / LTKM is a **structured reference baseline** in “Evaluated Memory Systems,” not the central method. Symbolic gains may be reported; Qwen H4 is a **negative architecture result** under BCR.

## Non-goals

- No Phi run.  
- No further architecture redesign.  
- No new topic search.  
- No SOTA / real-world generality claims.
