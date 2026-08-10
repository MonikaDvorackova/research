---
id: pub-03-final-positioning-lock
title: "Final positioning lock — WorldConsistMem"
type: research-notes
status: locked
created: 2026-08-04
updated: 2026-08-04
---

# Final positioning lock

**Paper shape:** benchmark + evaluation methodology (**not** architecture).  
**Verdict after novelty audit:** residual defensible once Intro/Related Work apply the dual contrast below.

## Central contribution (locked)

Cross-query consistency evaluation for long-term memory systems in evolving worlds, using dependent query bundles, machine-checkable world-history constraints, strict bundle consistency (BCR), and partial constraint satisfaction (CSR).

## Dual neighbor contrast (mandatory in Intro + Related Work)

### A. Long-term memory benchmarks

Already cover long-term interaction, evolving knowledge, retrieval, lifecycle, conflict, temporal facts, profile consistency, and answer accuracy.  
**Residual vs them:** dependent bundles; one shared evolving gold world; machine-checkable cross-query world constraints; BCR; CSR; Acc vs jointly coherent world-model answers.

### B. Cross-query logical consistency

Already cover multi-answer agreement, global logical coherence, constraint satisfaction, Acc–consistency separation.  
**Residual vs them:** application to **persistent memory systems** over **evolving multi-entity worlds** with current/historical/transition/temporal/provenance/relational/multi-hop world-history constraints—not SMT/case-file logical SAT alone.

## Frozen RQ

Under evolving synthetic worlds with dependent query bundles and machine-checkable cross-query constraints, do long-term memory systems that achieve non-trivial per-query accuracy also produce jointly consistent answer sets, and which partial-consistency diagnostics remain informative when strict bundle consistency floors?

## Frozen contribution classes

1. Evaluation methodology  
2. Benchmark (WorldConsistMem)  
3. Metrics (BCR, CSR, ConsAcc, gaps, diagnostics)  
4. Empirical analysis (corruption, symbolic, Qwen)  
5. Reference systems (including structured hierarchical baseline; **not** claimed superior)

## Forbidden claims

No “first consistency / first evolving-memory”; no “no prior consistency work”; no H0/hierarchy superiority; no five-layer necessity; no SOTA; no real-world generality; no architecture gains surviving LLM evaluation; no claim that BCR alone suffices under floor effects.

## Evidence freeze

See `experiments/worldconsistmem/outputs/scaled/FINAL_EXPERIMENT_STATUS.md`. Do not mutate.
