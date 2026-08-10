---
id: pub-03-sec-08-results
title: "Results"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 8. Results

We organize results around five questions. Symbolic and Qwen conditions are never pooled.

## 8.1 Are accuracy and consistency distinct?

**Corruption suite (smoke).** Gold predictions attain Acc = BCR = ConsAcc = 1. Controlled corruptions separate the metrics. Representative frozen values:

| Corruption | Acc | BCR | Gap_query |
|---|---:|---:|---:|
| high_acc_inconsistent | 0.849 | 0.000 | 0.849 |
| wrong_provenance | 0.849 | 0.000 | 0.849 |
| consistent_wrong_world | 0.394 | 1.000 | −0.606 |
| transition_inconsistency | 0.939 | 0.600 | 0.339 |

High Acc with BCR = 0 and low Acc with BCR = 1 both occur. This supports that \(\Phi\) is not redundant with Acc.

## 8.2 Does the distinction persist at scale?

**Symbolic scaled (102 worlds).** Retrieval baselines show large Acc–BCR gaps. Frozen point estimates:

| System | Acc | BCR | Gap_query | mean CSR (recompute) |
|---|---:|---:|---:|---:|
| B3_recency_k8 | 0.567 | 0.063 | 0.504 | 0.507 |
| B4_bm25_k8 | 0.929 | 0.591 | 0.338 | 0.881 |
| B1_flat_cap150_compact | 1.000 | 1.000 | 0.000 | 1.000 |
| H0_ltkm_cap150_ret8 | 0.976 | 0.844 | 0.132 | 0.973 |

B4 retains high Acc while BCR remains materially lower (\(\mathrm{Gap}_{\mathrm{query}} = 0.338\)). The Acc–consistency distinction survives scaling under the deterministic reader. World-level bootstrap CIs are reported in the frozen statistical analysis artefacts.

## 8.3 Which systems show the largest gaps?

Under the symbolic reader, **recency retrieval** exhibits the largest \(\mathrm{Gap}_{\mathrm{query}}\) among the headline retrieval points (0.504). **BM25** narrows but does not close the gap. **Compact flat at capacity 150** saturates Acc and BCR in this generator regime (fairness caveat: padding eviction can preserve focal lifecycle evidence; Section 6.5). **H0 at cap150/ret8** achieves high Acc and high BCR/CSR, but does **not** beat compact flat on BCR (ΔBCR vs compact = −0.156 at this point; matched lift vs compact fails the frozen gate). H0 does beat matched **recency** flat on BCR in the frozen capacity study; that is a matched-baseline comparison, not a claim of architectural superiority over all flat stores.

Selective ablations (archive, temporal-validity, graph, conflict) produce family-level Acc drops in the frozen ablation table; they are diagnostic of component–family links under the symbolic reader, not evidence that a multi-component store is necessary.

## 8.4 What happens under the Qwen reader?

**H4 subset; frozen Qwen Option A.** All four systems have **BCR = 0**. Acc remains non-trivial and ordered:

| System | Acc | BCR | mean CSR | Abs | Mal |
|---|---:|---:|---:|---:|---:|
| B1_flat_cap150_compact | 0.096 | 0 | 0.258 | 0.728 | 0.007 |
| B3_recency_k8 | 0.093 | 0 | 0.258 | 0.728 | 0.007 |
| B4_bm25_k8 | 0.148 | 0 | **0.329** | 0.579 | 0.001 |
| H0_ltkm_cap150_ret8 | **0.185** | 0 | 0.284 | 0.483 | 0.029 |

Because the constraint suite is satisfiable for gold/oracle predictions and yields non-trivial BCR on the deterministic symbolic reader (see Section 4.5 smoke confirmation and Section 8.2 symbolic results), the Qwen BCR floor reflects difficulty in producing jointly constraint-satisfying answers under this frozen reader/parsing pipeline, not an intrinsically inconsistent constraint definition.

**Reading:**

- In this Qwen setting, H0 has the **highest Acc** and lower abstention than flats/recency.  
- B4 has the **highest CSR**.  
- H0’s CSR is above B1/B3 (+0.026) but **below B4 (−0.045)**.  
- **No architecture consistency advantage is supported** under Qwen: BCR ties at 0; CSR does not rank H0 highest.  
- Acc gains must not be converted into consistency claims.

PConsAcc grid cells at \((\tau,\tau_c)\in\{0.5,0.8\}\times\{0.8,0.9\}\) are all 0 under Qwen: no bundle jointly clears the predeclared Acc and CSR thresholds.

## 8.5 Does CSR provide resolution when BCR floors?

Yes, within limits. With BCR = 0 for all Qwen systems, mean CSR still separates B4 (0.329) from B1/B3 (0.258) and H0 (0.284). Mean violations per bundle remain high (≈3.3–3.6). Acc–CSR Pearson correlation is positive for B1/B3/B4 (≈0.30–0.43) but near zero/slightly negative for H0 (−0.04), consistent with H0 answering more questions without proportional joint constraint satisfaction.

**Conclusion of Section 8.** Acc and consistency are empirically distinct; the distinction persists symbolically at scale; under Qwen, strict BCR floors while CSR remains weakly diagnostic; the structured reference H0 is not supported as a consistency winner under Qwen.
