---
id: pub-03-table-t5-query-family
title: "Query-family accuracy (headline)"
type: table
status: camera-ready
---

# Table 5. Query-family Acc under Qwen (H4; frozen)

| Family | B1 compact | B3 recency | B4 BM25 | H0 |
|---|---:|---:|---:|---:|
| current_state | 0.010 | 0.010 | 0.083 | 0.542 |
| historical_state | 0.162 | 0.162 | 0.089 | 0.547 |
| transition | 0.000 | 0.000 | 0.000 | 0.000 |
| multi_hop | 0.000 | 0.000 | 0.052 | 0.000 |
| provenance | 0.188 | 0.167 | 0.417 | 0.000 |
| temporal_order | 0.128 | 0.128 | 0.205 | 0.308 |
| contradiction | 0.083 | 0.083 | 0.167 | 0.000 |
| counterfactual | 0.000 | 0.000 | 0.000 | 0.000 |
| conflict_validity | 0.462 | 0.462 | 0.462 | 0.000 |

Source: `qwen_system_results.csv` family_accuracy fields.
