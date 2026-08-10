---
id: pub-03-final-claim-evidence-map
title: "Final claim–evidence map — WorldConsistMem"
type: research-notes
status: frozen
created: 2026-08-04
updated: 2026-08-04
---

# Final claim–evidence map

No claim may enter the manuscript without a row here.

## Claim 1 — Acc ≠ consistency

| Field | Content |
|---|---|
| Exact wording | Per-query accuracy and global cross-query consistency are empirically distinct. |
| Experiments | Smoke corruption suite; symbolic scaled Acc–BCR gaps; Qwen H4 Acc>0 with BCR=0 |
| Tables/figures | Corruption validation table; symbolic system table; Qwen system table; Fig. Acc vs BCR/CSR |
| Statistics | Gap_query > 0 where Acc > BCR; world-level bootstrap CIs on Acc/BCR |
| Limitations | Synthetic worlds; exact-match Acc; Qwen-only LLM reader for final H4 |
| Prohibited stronger wording | “Accuracy is meaningless”; “all systems are inconsistent in the wild” |

## Claim 2 — Constraint failures under strong retrieval / Acc

| Field | Content |
|---|---|
| Exact wording | High-retrieval and high-answer-accuracy systems can still violate temporal, relational, transition, and provenance constraints across dependent queries. |
| Experiments | Symbolic B4/H0 constraint-family rates; Qwen constraint-family + CSR family rows |
| Tables/figures | Constraint-family tables; Fig. violation heatmap |
| Statistics | Per-family violation rates; CSR-by-family means |
| Limitations | Constraint library is synthetic and incomplete vs real legal/world constraints |
| Prohibited stronger wording | “Retrieval cannot help consistency”; “BM25 is inconsistent by design” |

## Claim 3 — BCR floor + partial diagnostics

| Field | Content |
|---|---|
| Exact wording | Strict bundle consistency can exhibit floor effects under weaker readers; partial constraint satisfaction (CSR) and thresholded partial ConsAcc provide complementary diagnostic resolution without replacing BCR. |
| Experiments | Qwen BCR=0 for all four systems; CSR/PConsacc recomputation; corruption CSR checks |
| Tables/figures | Partial consistency tables; PConsAcc grid; BCR-floor diagnostics |
| Statistics | mean/median CSR; violation distributions; Acc–CSR correlation; world CSR CIs |
| Limitations | Partial thresholds are predeclared but still convention-dependent; not a single headline score |
| Prohibited stronger wording | “CSR replaces BCR”; “pick the best PConsAcc cell as the main result” |

## Claim 4 — Architecture limitation (not headline)

| Field | Content |
|---|---|
| Exact wording | Structured lifecycle-aware memory improves evidence availability and symbolic consistency under matched budgets in the completed symbolic study, but architecture superiority does not survive the completed Qwen reader evaluation (BCR=0 for H0 and baselines). |
| Experiments | Symbolic capacity-matched H0 vs compact/recency; Qwen H4 finalize |
| Tables/figures | Symbolic capacity table; Qwen table; limitations section |
| Statistics | Symbolic BCR lifts where present; Qwen BCR all zero; Acc/abs shifts are not BCR wins |
| Limitations | Single small local LLM; no Phi; no cloud models; H4 subset of scaled worlds |
| Prohibited stronger wording | “H0 is superior”; “hierarchy is necessary”; “five layers are required”; “LLM-independent architecture gains” |

## Explicitly rejected claims

| Rejected | Why |
|---|---|
| H0 superiority (headline) | Qwen BCR=0; decision rule fails |
| Necessity of hierarchical memory | Not evidenced |
| SOTA | Not evaluated against published leaderboards |
| General real-world validity | Synthetic benchmark only |
| LLM-independent architecture gains on H4 | Contradicted by Qwen BCR floor |

## Residual novelty (conservative)

Dependent query bundles; one shared gold world history; machine-derived cross-query constraints; strict **and** partial consistency metrics; explicit Acc vs coherent world-model distinction.  
Do **not** claim that no prior benchmark studies consistency at all.
