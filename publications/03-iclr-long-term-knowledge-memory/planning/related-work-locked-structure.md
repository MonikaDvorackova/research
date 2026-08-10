---
id: pub-03-related-work-locked-structure
title: "Related Work locked structure — WorldConsistMem"
type: research-notes
status: locked-structure
created: 2026-08-04
updated: 2026-08-04
---

# Related Work — locked structure (prose not yet drafted)

Four groups. Use `TODO(cite):` until BibTeX keys exist in `references/bib/library.bib`.

---

## Group 1 — Long-term memory evaluation

| Field | Content |
|---|---|
| Papers | `TODO(cite):` LongMemEval; `TODO(cite):` LongMemEval-V2; `TODO(cite):` MemoryAgentBench; `TODO(cite):` EverMemBench; `TODO(cite):` EvoMemBench |
| What they evaluate | Multi-session / long-horizon Acc; ability factorizations (IE, temporal, updates, abstention, AR/TTL/LRU/SF, recall/awareness/profile, scope×content); sometimes latency |
| What they do not evaluate | Joint Φ over dependent world-answer bundles with BCR/CSR |
| Contrast | Ability Acc ≠ machine-checkable cross-query **world** consistency |
| Safe wording | “Primarily score answer accuracy (or ability Acc) under long histories.” |
| Overclaim | “They ignore consistency entirely”; “we are the first long-term memory benchmark.” |

---

## Group 2 — Dynamic and evolving knowledge

| Field | Content |
|---|---|
| Papers | `TODO(cite):` DynamicMem; `TODO(cite):` WorldMemArena; `TODO(cite):` LongMemEval-V2 (dynamic state) |
| What they evaluate | Evolving user profiles / personal–task states; checkpoint reconstruction; lifecycle write/maintain/retrieve/use; multimodal agent trajectories |
| What they do not evaluate | Multi-entity world bundles with joint current+historical+transition+provenance constraints |
| Contrast | Profile TCE / lifecycle Acc ≠ Φ over interdependent **world-history** queries |
| Safe wording | “Track evolving state under accuracy or stage metrics.” |
| Overclaim | “No prior work studies evolving worlds”; “DynamicMem already evaluates BCR.” |

---

## Group 3 — Conflict and temporal memory

| Field | Content |
|---|---|
| Papers | `TODO(cite):` MemConflict; `TODO(cite):` MemoryAgentBench FactConsolidation; temporal/update abilities in LongMemEval |
| What they evaluate | Conflict fitness-for-use; selective forgetting after edits; knowledge-update Acc; retrieval ranking under conflicts |
| What they do not evaluate | Multi-query answer-set Φ linking transition, provenance, uniqueness, relational constraints in one bundle |
| Contrast | Per-query conflict validity ≠ bundle-level world consistency |
| Safe wording | “Diagnose conflict handling and updates at the query or retrieval level.” |
| Overclaim | “MemConflict already measures cross-query consistency”; “we invent conflict evaluation.” |

---

## Group 4 — Cross-query logical consistency

| Field | Content |
|---|---|
| Papers | `TODO(cite):` SetCons / Quantifying Cross-Query Contradictions; `TODO(cite):` LogicVault; `TODO(cite):` LogicBench-Cross or equivalent |
| What they evaluate | Multi-query bundles; global SAT / SetCons; Acc–consistency separation; solver repair |
| What they do not evaluate | Persistent **memory system** evaluation over evolving multi-entity **gold worlds** with world-history-derived temporal/transition/provenance/relational constraints |
| Contrast | Logical belief SAT ≠ memory Φ over evolving worlds |
| Safe wording | “Separates accuracy from global coherence for multi-query reasoning; we apply related methodology to memory over evolving worlds.” |
| Overclaim | “Cross-query consistency is new”; “no prior Acc–consistency work”; “we invented SetCons-style metrics.” |

---

## Drafting order for §2

1. Paragraph Group 1 → residual Acc suite.  
2. Paragraph Group 2 → residual not “evolution alone.”  
3. Paragraph Group 3 → residual not “conflict Acc alone.”  
4. Paragraph Group 4 → residual application domain (memory + world Φ).  
5. Closing sentence: WorldConsistMem residual package (bundles + gold world + Φ/BCR/CSR).
