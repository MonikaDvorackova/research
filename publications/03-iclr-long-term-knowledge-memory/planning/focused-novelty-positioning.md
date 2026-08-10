---
id: pub-03-focused-novelty-positioning
title: "Focused novelty positioning — WorldConsistMem"
type: research-notes
status: audit
created: 2026-08-02
updated: 2026-08-02
---

# Focused novelty positioning

**Question asked:** Do closest benchmarks evaluate dependent query bundles, global consistency constraints, joint agreement across current/historical/transition/relational/provenance answers, constraint-based scoring over one gold world history, and component-tied consistency diagnostics?

**Not asked:** Whether any paper also contains evolving facts.

## Comparison matrix

| Benchmark | Evolving facts? | Isolated Q→A primary? | Dependent query bundles? | Global answer-set constraints? | Joint current/hist/trans/rel/prov? | Constraint scoring from gold history? | Component↔consistency diagnosis? |
|---|---|---|---|---|---|---|---|
| LongMemEval | Yes (updates) | Yes | No | No | Ability-factorized, not joint constraints | No | No |
| LongMemEval-V2 | Env dynamics | Yes (abilities) | No | No | Different ability set (workflow/gotchas) | No | AgentRunbook pools ≠ our C suite |
| MemoryAgentBench | Incremental | Yes | No | No | Partial abilities | No | No |
| MemConflict | Conflicts | Yes (per conflict query) | No | Retrieval/ranking fitness, not multi-query \(\Phi\) | Conflict types, not full joint bundle | Partial (profiles) | White-box retrieval, not H4 map |
| EverMemBench | Multi-party | Yes | No | No | Recall/awareness/profile | No | No |
| DynamicMem | Profile evolution | Checkpoint profile/act | No multi-view world bundles | Profile coherence ≠ relational world \(\mathcal{C}\) | Profile-centric | Profile gold | Limited |
| MemoryArena | Multi-session action | Task success | No | No | Action-oriented | No | No |
| EvoMemBench | Knowledge/execution evolution | Task/episode metrics | No | No | Scope×content axes | No | Mechanism taxonomy, not \(\Phi\) |
| Mem2ActBench | Tool constraints | Inference→tool | No | Task constraints ≠ world-history \(\mathcal{C}\) | Tool grounding | No | Utilization, not consistency suite |
| WorldMemArena | World/action | Typically task/world metrics | Not as our joint \(\Phi\) | Unclear / not our residual | Multimodal world | Varies | Varies |

## Classification

### **INCREMENTAL BUT DEFENSIBLE**

Not OCCUPIED: no inspected benchmark’s primary evaluation target is **cross-query consistency** as \(\Phi(\hat Y;\mathcal{C})\) over **dependent bundles** spanning current, historical, transition, relational, and provenance views of **one deterministic gold world history**, with **accuracy–consistency gap** and **component-level consistency diagnostics**.

Closest neighbors:

- **MemConflict** — conflict validity / retrieval fitness per query (complementary, not duplicate).  
- **LongMemEval / LME-V2** — ability-wise Acc under evolution (complementary).  
- **DynamicMem** — temporal checkpoint profile consistency (different object: user profile, not multi-entity world constraint bundles).

Direct duplicate: **none identified**.

## Residual (one sentence)

WorldConsistMem evaluates whether a memory system’s answers to **interdependent** queries jointly describe **one coherent evolving world**, not whether each query can be answered in isolation.
