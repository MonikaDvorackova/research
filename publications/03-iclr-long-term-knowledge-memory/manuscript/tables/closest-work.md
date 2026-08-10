---
id: pub-03-table-closest-work
title: "Closest-work comparison table"
type: table
status: draft
created: 2026-08-04
updated: 2026-08-04
---

# Table: Closest related benchmarks and adjacent consistency work

Cells use **Yes** / **Partial** / **No**. Every cell is backed by `planning/final-citation-audit.md` and the novelty audit. Do **not** read “No” as “the work ignores the phenomenon entirely”—it means the feature is not the primary evaluation object as operationalized in WorldConsistMem.

| Benchmark / work | Long-term memory | Evolving state | Dependent query bundles | Shared gold history | Temporal / transition queries | Provenance | Cross-query machine constraints | Strict bundle consistency | Partial constraint satisfaction | Primary metric |
|---|---|---|---|---|---|---|---|---|---|---|
| LongMemEval [@wu2025longMemEval] | Yes | Partial^[a] | No | Partial^[b] | Partial^[c] | No | No | No | No | Ability Acc |
| LongMemEval-V2 [@wu2026longMemEvalV2] | Yes | Yes | No | Partial^[b] | Partial^[c] | No | No | No | No | Acc (+ latency) |
| MemoryAgentBench [@hu2025memoryAgentBench] | Yes | Partial^[a] | No | Partial^[b] | Partial^[c] | No | No | No | No | Competency Acc |
| EverMemBench [@hu2026everMemBench] | Yes | Yes | No | Partial^[b] | Partial^[c] | No | No | No | No | Recall / awareness / profile Acc |
| EvoMemBench [@wang2026evoMemBench] | Yes | Partial^[a] | No | Partial^[b] | No / Partial^[d] | No | No | No | No | Task Acc / success |
| MemConflict [@tao2026memConflict] | Yes | Partial^[a] | No | Partial^[b] | Partial^[c] | Partial^[e] | No / Partial^[f] | No | Partial^[g] | Conflict Acc + retrieval fitness |
| DynamicMem [@xie2026dynamicMem] | Yes | Yes | Partial^[h] | Yes^[i] | Partial^[c] | No | No / Partial^[f] | No | Partial^[g] | Checkpoint / service Acc |
| WorldMemArena [@liu2026worldMemArena] | Yes | Yes | Partial^[h] | Partial^[b] | Partial^[c] | Partial^[e] | No | No | Partial^[g] | Lifecycle Acc / faithfulness |
| SetCons metrics [@salla2026crossQueryContradictions] | No | No | Yes | Partial^[j] | Partial^[k] | No | Yes^[l] | Yes^[m] | Partial^[n] | SetCons / case satisfiability |
| LogicVault / LogicBench-Cross [@chaudhry2026logicVault] | No | No | Yes | Partial^[j] | Partial^[k] | No | Yes^[l] | Yes^[m] | Partial^[n] | Logical / SMT consistency |
| **WorldConsistMem (this work)** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes (BCR)** | **Yes (CSR)** | **Acc + BCR + CSR** |

### Footnotes

^[a]: Evolving knowledge appears as updates, long sessions, or competency settings, not as a multi-entity gold world timeline scored by joint \(\Phi\).

^[b]: Histories or sessions provide shared context for questions, but scoring remains primarily per-query Acc rather than joint constraints over one retained gold world state sequence.

^[c]: Temporal or update abilities / questions exist; explicit *transition* queries jointly constrained with current/historical/provenance answers are not the primary object.

^[d]: Self-evolving taxonomy emphasizes scope×content mechanisms; temporal-transition bundles are not evidenced as a primary consistency suite (conservative Partial/No).

^[e]: Conflict or evidence diagnostics may touch support relations; provenance is not a first-class jointly constrained query family as in WorldConsistMem.

^[f]: May expose divergence between retrieval fitness and answer correctness, or checkpoint reconstruction error—adjacent to, but not identical with, machine-checkable cross-query world constraints \(\mathcal{C}_b\).

^[g]: Partial diagnostics exist (e.g., retrieval fitness, checkpoint completeness, stage metrics) but not CSR-style fraction of satisfied world-history constraints over dependent answer sets.

^[h]: Related probes or multi-stage evaluations can couple questions about one trajectory; not WorldConsistMem-style dependent bundles spanning current/historical/transition/provenance under shared \(\mathcal{C}_b\).

^[i]: DynamicMem retains evolving profile ground truth for checkpoint evaluation (user-centric gold state), distinct from multi-entity world-history bundles.

^[j]: Case-file or belief-state ground truth supports logical satisfiability; not an evolving multi-entity agent-memory world history.

^[k]: Logical entailment / contradiction structure may be temporal in content; not world-event transition constraints derived from a memory observation stream.

^[l]: SMT / set-level logical constraints over commitments—not world-history-derived temporal/transition/provenance/relational memory constraints.

^[m]: Global case satisfiability / SetCons-style strict coherence over multi-query instances.

^[n]: Contradiction density, revision cost, or related graded diagnostics exist; not WorldConsistMem CSR over world-history constraint families.

**Reading rule.** Columns “cross-query machine constraints,” “strict bundle consistency,” and “partial constraint satisfaction” are **Yes** for SetCons/LogicVault because those works evaluate multi-query logical coherence; WorldConsistMem’s residual is the *memory + evolving gold world* instantiation (Section 2.4), not inventing Acc–consistency separation.
