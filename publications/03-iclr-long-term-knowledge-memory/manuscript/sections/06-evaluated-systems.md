---
id: pub-03-sec-06-evaluated-systems
title: "Evaluated Memory Systems"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 6. Evaluated Memory Systems

Systems are **reference implementations** for evaluation. We describe them factually. We do not claim architectural superiority for any design, including the structured hierarchical reference.

## 6.1 Oracle and flat stores

- **Oracle / gold.** Predictions equal gold answers (validation upper bound; Acc = BCR = 1 on well-formed bundles).  
- **Flat append-only (unconstrained).** All observations retained; reader consults the full store.  
- **Latest-only.** Retain only the most recent observation(s) under a simple currency rule; older evidence is discarded.  
- **Capacity-limited flat.** Fixed logical-record budget with eviction: **recency**, **compact padding** (drop low-priority padding/status noise first), or **reservoir** sampling.

## 6.2 Retrieval baselines

- **Recency-\(k\).** Retrieve the \(k\) most recent observations.  
- **BM25-\(k\).** Lexical retrieval of top-\(k\) observations for the query text.  

Reported operating points include \(k\in\{3,8\}\) under the frozen scaled protocol.

## 6.3 Structured hierarchical reference (H0)

H0 is a structured lifecycle-aware store with multiple internal components (working/session-style buffers, long-term assertions with validity, graph edges, provenance, archive/conflict bookkeeping, as implemented in the frozen experiment). At query time it returns an evidence pack under a retrieval budget (e.g., `ret8` at capacity 150).

**Role in the paper.** H0 is a **reproducible structured baseline**, not presented as a superior architecture. Symbolic matched-budget comparisons and the Qwen reader study report Acc and consistency for H0 under the WorldConsistMem metrics. Completed Qwen results do **not** support a consistency advantage for H0 (Section 8).

## 6.4 Readers

- **Symbolic / deterministic reader.** Exact structured matching over retrieved or stored records (primary scaled symbolic tables).  
- **Local LLM reader.** `mlx-community/Qwen2.5-3B-Instruct-4bit` with frozen prompt, temperature 0, max tokens, JSON early-stop, and parser (H4 subset).  

Evidence packs are isolated per query under the frozen H4 protocol so that cross-query leakage through the prompt is not an uncontrolled confound.

## 6.5 Fairness limitations (explicit)

Comparisons are informative but not perfectly matched:

- **Internal structure differs** (flat list vs multi-store H0).  
- **Capacity accounting** charges H0 metadata (graph, provenance, indices) against the same logical-record budgets used for flat stores; absolute budgets therefore tax structured metadata.  
- **Retrieval budgets** (\(k\) vs store-routed packs) are matched numerically where stated, but lexical BM25 is not identical to H0’s routing.  
- **Deterministic vs LLM readers** are separate conditions; symbolic Acc/BCR must not be pooled with Qwen Acc/BCR.  
- **Compact flat** can retain focal lifecycle events by dropping padding, which can yield very high symbolic Acc/BCR at medium budgets; this is a fairness caveat for matched-budget interpretation, not a general ranking of store designs.

These limits bound interpretation: gaps support metric claims; they do not license claims of architectural superiority.
