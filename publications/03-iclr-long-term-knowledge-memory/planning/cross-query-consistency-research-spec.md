---
id: pub-03-cross-query-consistency-research-spec
title: "Research specification — cross-query consistency"
type: research-notes
status: authorized-direction
created: 2026-08-02
updated: 2026-08-02
---

# Research specification — Cross-query consistency in evolving worlds

**Paper type:** Combined benchmark + evaluation methodology + hierarchical agent-memory system.  
**Venue shape:** ICLR (benchmark/system/evaluation).  
**Topic:** Hierarchical Long-Term Knowledge Memory for AI Agents in Evolving Worlds.

## Exact research question

Can long-term memory systems maintain a **globally consistent** representation of an evolving world across current-state, historical-state, conflict-sensitive, multi-hop, temporal, and provenance queries?

## Scientific / evaluation object

**Cross-query consistency of agent memory over an evolving world.**

Not: whether isolated facts can be retrieved.  
Yes: whether answers to related queries jointly correspond to **one valid current state** and **one valid world history**.

## Paper contributions (target shape)

1. Formal evaluation target: cross-query consistency vs per-query accuracy.  
2. Deterministic evolving-world benchmark (**WorldConsistMem**, working alias EvolvingWorldMem).  
3. Constraint-based metric suite with accuracy–consistency gap.  
4. Hierarchical five-component memory system with explicit lifecycle.  
5. Baselines + ablations + diagnostic failure analysis.

## Explicitly not primary claims

Do not revive as primary: CR-Gap, Archive Pareto, AUG, P-Bind/F1×F4, C1 credit identifiability, C4 consolidation collapse, closed learning-centric hypotheses.

Empirical hypotheses H1–H4 are **falsifiable**, not assumed results (see [`benchmark-specification.md`](benchmark-specification.md)).

## Novelty class

**INCREMENTAL BUT DEFENSIBLE** (see [`focused-novelty-positioning.md`](focused-novelty-positioning.md)).

Residual vs closest work: **dependent query bundles + machine-checkable global consistency constraints over one gold world history + component-tied consistency diagnostics.**

## Implementation readiness

**Ready for specification-locked implementation** of the synthetic world generator and constraint checkers. System/baselines after benchmark skeleton exists.

## Related planning docs

- [`benchmark-specification.md`](benchmark-specification.md)  
- [`consistency-metrics.md`](consistency-metrics.md)  
- [`architecture-specification.md`](architecture-specification.md)  
- [`baseline-and-ablation-plan.md`](baseline-and-ablation-plan.md)  
- [`focused-novelty-positioning.md`](focused-novelty-positioning.md)  
- [`manuscript-outline.md`](manuscript-outline.md)
