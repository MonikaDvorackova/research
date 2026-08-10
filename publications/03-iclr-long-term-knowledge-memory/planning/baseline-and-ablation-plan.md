---
id: pub-03-baseline-and-ablation-plan
title: "Baseline and ablation plan"
type: research-notes
status: draft-spec
created: 2026-08-02
updated: 2026-08-02
---

# Baseline and ablation plan

Compare **system families** under matched reader model, retrieval budget \(k\), and (where applicable) storage token budget \(B\).

## Baselines

| # | Family | Instantiation notes |
|---|---|---|
| 1 | Full-context / long-context | Concatenate observation stream (truncate if needed with fixed policy) |
| 2 | Flat vector memory | Chunk embed + top-\(k\) similarity |
| 3 | Recency-weighted vector | Similarity × recency decay |
| 4 | Temporal RAG | Time-aware index / filter for historical queries |
| 5 | Graph memory | Entity-relation store + path retrieval (lightweight) |
| 6 | Profile / summary memory | Running summary or profile buffer |
| 7 | Existing agent-memory frameworks | Mem0, A-Mem, LangGraph memory, AutoGen memory, MemoryOS — **if runnable and fair**; document adapters |
| 8 | Proposed hierarchical LTKM | Full five-component system |

Do **not** list “OpenAI” as a baseline without a defined memory configuration (e.g., long-context only vs tool memory).

## Ablations (proposed system)

| Ablation | Predicted hit dimension |
|---|---|
| Without hierarchy (flat unified store, same \(B\)) | Bundle ConsAcc / Gap |
| Without archive | Historical + transition consistency |
| Without graph | Relational + multi-hop |
| Without temporal validity metadata | Conflict-validity / temporal |
| Without provenance | Provenance consistency |
| Without conflict resolution | Contradiction consistency |
| Without lifecycle promotion (session-only) | Evolution under long \(T\) |
| Flat unified store, same total storage | H3 control |
| Oracle retrieval (gold evidence) | Separates retrieval vs consistency assembly |

## Controls

- Same backbone reader for all systems in a comparison wave.  
- Matched \(k\) and \(B\) when comparing hierarchical vs flat.  
- Report Acc, BCR, ConsAcc, Gap, and per-family violation rates.
