---
id: pub-03-appendix-a-reproducibility
title: "Appendix A — Reproducibility checklist"
type: appendix
status: camera-ready
---

# Appendix A. Reproducibility checklist

Paper: WorldConsistMem (ICLR target). Evidence freeze: `experiments/worldconsistmem/outputs/scaled/FINAL_EXPERIMENT_STATUS.md`.

## A.1 Data

- [x] Scaled dataset generated with seed **100**
- [x] Scale: **102** worlds / **1,088** bundles / **7,140** queries
- [x] H4 LLM subset: **18** worlds / **192** bundles / **1,260** queries
- [x] Smoke checksum SHA-256 prefix: `3aa67ed1…` (full hash in freeze doc)
- [x] Manifest hash recorded in freeze doc (`37aa8604…`)

## A.2 Metrics (frozen definitions)

- [x] Acc = mean per-query exact-match accuracy
- [x] BCR = fraction of bundles with \(\Phi=1\) (all applicable constraints satisfied)
- [x] CSR = mean fraction of satisfied constraints per bundle (partial; complementary)
- [x] \(\mathrm{Gap}_{\mathrm{query}} = \mathrm{Acc} - \mathrm{BCR}\)
- [x] ConsAcc / PConsAcc grid reported; PConsAcc cells are 0 under Qwen H4
- [x] World-level bootstrap CIs where present in CSV outputs

## A.3 Readers and systems

- [x] Symbolic exact-match reader on full scaled set
- [x] LLM reader: `mlx-community/Qwen2.5-3B-Instruct-4bit` with frozen decoding (`prompt_v3_k3_mt48`)
- [x] Systems under Qwen: B1 compact, B3 recency k8, B4 BM25 k8, H0 LTKM cap150 ret8
- [x] Phi **not** run for Option A (do not add)

## A.4 Computation integrity

- [x] Symbolic `system_results.csv` checksum `70b5ce4f…`
- [x] Run1 Qwen cache checksum `9bb7cfb1…`
- [x] H4-Run2 Option A complete: 2734/2734 queries
- [x] Partial consistency recomputed offline from frozen predictions (no new inference)
- [x] Paper shape gate: `"paper": "BENCHMARK ONLY"`

## A.5 Forbidden post-freeze actions

- [ ] Rerun / optimize completed experiments — **forbidden**
- [ ] Revive architecture-superiority claims — **forbidden**
- [ ] Modify frozen numbers — **forbidden**
- [ ] Run Phi for Option A — **forbidden**
