---
id: pub-03-sec-10-discussion-limitations
title: "Discussion and Limitations"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 10. Discussion and Limitations

## 10.1 What the residual supports

WorldConsistMem’s residual is methodological: dependent bundles over one gold evolving world, machine-checkable cross-query constraints, BCR, and CSR make Acc and joint world-answer consistency separately measurable for memory systems. Completed evidence is consistent with these quantities diverging under corruption, symbolic retrieval baselines, and a local Qwen reader.

## 10.2 Strict versus partial consistency

BCR is the right strict rate for “fully coherent bundle.” When BCR floors, CSR and violation distributions remain informative and should be reported. Partial ConsAcc grids should be reported in full; they are not a license to replace BCR with a favorable threshold cell.

## 10.3 Synthetic-world and template limits

Worlds are synthetic; observations are templated; ecological validity for open-domain conversation is **not** claimed. Difficulty labels are structural. Results characterize controlled WorldConsistMem regimes, not production assistants.

## 10.4 Reader limits

The LLM condition uses a single local 3B-class Qwen model with frozen short-form JSON decoding. Stronger models, cloud APIs, and Phi were not part of the frozen Option A decision. Low Acc and high abstention limit how far Qwen tables can speak to “human-level” memory behavior; they remain valid for the Acc≠consistency and BCR-floor/CSR questions under this reader.

## 10.5 Compact-flat strength and fairness

Under symbolic matched budgets, compact flat can match or exceed H0 on BCR by discarding padding while retaining focal events; capacity accounting taxes H0 metadata (Section 6.5). Structure is a reference design under test, not a proven necessity.

## 10.6 Negative architecture result under Qwen

The hierarchical reference does **not** earn a consistency win under Qwen (BCR = 0 for all; CSR highest for BM25). Within the frozen Qwen evaluation, Acc improvements and structural memory do not reliably yield joint coherence. This negative result is reported as a limitation of architecture claims under WorldConsistMem, not as a contribution headline.

## 10.7 Adjacent logical-consistency literature

As discussed in Section 2.4, cross-query logical consistency work [@salla2026crossQueryContradictions; @chaudhry2026logicVault] already separates Acc from global coherence for multi-query reasoning, but not for persistent memory systems over evolving multi-entity gold worlds with world-history-derived constraints.

## 10.8 Proper scope of conclusions

Safe conclusions: Acc≠consistency for this benchmark; BCR can floor; CSR can still separate systems; architecture superiority is unsupported under the frozen Qwen protocol.  
Unsafe conclusions: real-world generality; state-of-the-art rankings; necessity of hierarchy; BCR sufficiency alone in low-Acc regimes without CSR.
