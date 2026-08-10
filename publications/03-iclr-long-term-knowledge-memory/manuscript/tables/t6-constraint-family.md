---
id: pub-03-table-t6-constraints
title: "Constraint-family violation rates"
type: table
status: camera-ready
---

# Table 6. Constraint-family violation rates (headline systems)

**Symbolic** (fraction of bundles with ≥1 failure):

| Family | B3 recency | B4 BM25 | B1 compact | H0 |
|---|---:|---:|---:|---:|
| uniqueness | 0.156 | 0.000 | 0.000 | 0.000 |
| temporal | 0.406 | 0.000 | 0.000 | 0.156 |
| transition | 0.375 | 0.120 | 0.000 | 0.000 |
| relational | 0.562 | 0.343 | 0.000 | 0.000 |
| provenance | 0.625 | 0.057 | 0.000 | 0.000 |
| multi_hop | 0.344 | 0.124 | 0.000 | 0.000 |
| contradiction | 0.000 | 0.000 | 0.000 | 0.000 |

**Qwen** (same systems):

| Family | B1 / B3 | B4 | H0 |
|---|---:|---:|---:|
| transition | 1.000 | 1.000 | 1.000 |
| provenance | 0.938 | 0.724 | 1.000 |
| relational | 0.625 | 0.625 | 0.625 |
| multi_hop | 0.406 | 0.406 | 0.406 |
| temporal | 0.354 | 0.323 | 0.281 |
| uniqueness | 0.219 | 0.177 | 0.000 |
| contradiction | 0.052 | 0.073 | 0.188 |
