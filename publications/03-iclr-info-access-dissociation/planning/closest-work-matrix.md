---
id: pub-03-c1-closest-work-matrix
title: "Closest-work matrix — C1 Information-Access Regime Dissociation"
type: research-notes
status: stopped
created: 2026-07-31
updated: 2026-07-31
novelty_verdict: OCCUPIED
---

# Closest-work matrix — C1

| Paper | Venue / year | Identical facts? | Simult. vs seq.? | Length matched? | Tools isolated? | Multi-family? | Overlap with C1 | Residual |
|---|---|---|---|---|---|---|---|---|
| Laban et al. Lost in Conversation | ICLR 2026 Best Paper | Yes | Yes (FULL/CONCAT vs SHARDED) | Partial (CONCAT recovers without pad) | N/A (no tools); RECAP/SNOWBALL agent-style | Yes (15) | **Direct duplicate of core claim** | Surface form only |
| Context Arrives in Pieces | arXiv 2026 | Yes (sharded) | Yes (training setting) | Memory-cap ≠ pad | No | Limited | Occupies mitigation follow-on | Training, not new dissociation |
| Tool-Use Tax | arXiv 2026 | Shared noisy ctx | No | No | Protocol vs CoT factorization | Partial | Orthogonal tool-protocol cost | Different RQ |
| LUMINA | ACL Findings 2026 | Env-dependent | Multi-turn hardness | No | Oracle skills | Yes | Adjacent compounding | Not access-regime |
| Lost in the Middle | TACL 2024 | Position within one ctx | No | N/A | No | Yes | Position bias background | Single-context only |
| Progressive Disclosure study | arXiv 2026 | Document packaging | Disclosure vs raw | Efficiency focus | File/skill tools | Yes | Packaging/efficiency | Not matched decision facts |
| Parallel tool calling (LLMCompiler / W&D / TPS-Bench) | ICML/ACL/arXiv 2024–26 | Often independent calls | Parallel vs sequential *scheduling* | Latency/cost | Scheduling | Yes | Latency, not competence dissociation | Efficiency |
| FH vs SH planning horizon | arXiv 2026 | Tool-calling tasks | Plan horizon, not fact access | Token efficiency reported | Tool selection present | Yes | Scaffolding | Different object |

**Matrix conclusion:** C1 is occupied by Laban et al.; remaining rows are adjacent or orthogonal, not a publishable residual.
