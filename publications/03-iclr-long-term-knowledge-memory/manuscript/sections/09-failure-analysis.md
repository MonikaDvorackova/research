---
id: pub-03-sec-09-failure-analysis
title: "Consistency Failure Analysis"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 9. Consistency Failure Analysis

This section localizes failures under the frozen Qwen condition and contrasts them with symbolic error patterns. Counts refer to bundles with at least one violation in a family unless noted.

## 9.1 Qwen: widespread multiple violations

For all four Qwen systems, **transition** constraints fail on **192/192** bundles in the H4 subset. Failures are not explained by a single rare constraint on an otherwise consistent bundle:

| System | Mean viol./bundle | Frac. exactly one viol. | Frac. multiple viol. |
|---|---:|---:|---:|
| B1 compact | 3.59 | 0.031 | 0.969 |
| B3 recency | 3.59 | 0.031 | 0.969 |
| B4 BM25 | 3.33 | 0.177 | 0.823 |
| H0 reference | 3.50 | 0.000 | 1.000 |

**BCR = 0** under Qwen therefore reflects **widespread multi-constraint inconsistency**, not one recurring isolated miss.

## 9.2 Constraint families (Qwen)

Approximate family hit counts (bundles with ≥1 failure; frozen diagnostics):

| Family | B1 / B3 | B4 | H0 |
|---|---:|---:|---:|
| transition | 192 | 192 | 192 |
| provenance | 180 | 139 | 192 |
| relational | 120 | 120 | 120 |
| multi-hop | 78 | 78 | 78 |
| temporal | 68 | 62 | 54 |
| uniqueness | 42 | 34 | 0 |
| contradiction | 10 | 14 | 36 |

Transition and provenance dominate. H0 reduces uniqueness hits to zero in this snapshot but **increases** contradiction hits and still fails every transition constraint. B4 reduces provenance hits relative to B1/B3, aligning with its higher CSR.

## 9.3 Abstention and malformed output

Qwen abstention is high for B1/B3 (0.728), lower for B4 (0.579) and H0 (0.483). Malformed rates remain low for flats/BM25 (≤0.007) and higher for H0 (0.029). Lower abstention with higher Acc under H0 does not restore BCR; some additional answered queries still violate joint constraints (near-zero Acc–CSR correlation).

## 9.4 Evidence availability versus reader composition

Symbolic BM25 and H0 can place correct evidence in scope and still show Acc–BCR gaps; under Qwen, error decomposition emphasizes **reader composition** failures even when retrieval improves Acc. Frozen H4 notes include non-zero reader-failure-on-correct-evidence rates. The methodological implication suggested by the decomposition is consistent with the observed pattern that improving evidence can shift Acc without necessarily restoring \(\Phi=1\) under this frozen evaluation pipeline.

## 9.5 Symbolic contrast (brief)

Under the deterministic reader, family Acc and BCR are much higher; gaps concentrate on retrieval/capacity regimes (e.g., recency) rather than universal transition collapse. Ablations link archive/temporal/graph components to family Acc drops. This contrast indicates that Qwen BCR flooring is reader-regime-specific, not a claim that the constraint suite is unsatisfiable in principle (gold and strong symbolic systems achieve BCR = 1).
