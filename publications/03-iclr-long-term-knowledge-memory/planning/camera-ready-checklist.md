---
id: pub-03-camera-ready-checklist
title: "Camera-ready checklist"
type: planning
status: final
created: 2026-08-04
updated: 2026-08-04
---

# Camera-ready checklist (WorldConsistMem)

## Content freeze

- [x] Research question frozen
- [x] Benchmark / experiments / metrics / results frozen
- [x] Tables and figure *specifications* frozen (SVG rendered from frozen outputs)
- [x] Positioning: benchmark + methodology (not architecture)
- [x] Contribution claims match freeze (no H0 superiority under Qwen)
- [x] Limitations explicit (Section 10 + Table 8)

## Manuscript assembly

- [x] Single coherent `manuscript/paper.md`
- [x] Abstract written from frozen evidence only
- [x] Conclusion written without new claims
- [x] Final title selected (`planning/title-candidates.md`)
- [x] Figures 1–5 present under `manuscript/figures/`
- [x] Tables 1–8 present under `manuscript/tables/` and inlined in `paper.md`
- [x] Appendix A (reproducibility) + Appendix B (artifacts)

## Cross-reference audit

- [x] Every figure referenced in body (Figures 1–5)
- [x] Every table referenced in body (Tables 1–8)
- [x] Section forward references in Introduction (Sections 3–10)
- [x] Acronyms defined on first use: LTM, Acc, BCR, CSR, ConsAcc, Gap_query, H0/B1/B3/B4
- [x] Citation keys listed; entries live in `references/bib/library.bib`
- [ ] Venue LaTeX/PDF compile (Markdown-primary assembly; Overleaf export remaining)

## Scientific claim audit

- [x] Acc–consistency dissociation supported (corruption + symbolic)
- [x] High Acc with constraint violations supported (symbolic B4)
- [x] Qwen BCR = 0 for all four systems; CSR discriminative
- [x] H0 highest Acc, not highest CSR under Qwen
- [x] Architecture superiority explicitly unsupported
- [x] No SOTA / first / only / unprecedented language

## Process

- [x] No commit performed for this assembly pass
- [x] No numbers changed from frozen CSVs beyond display rounding already in camera-ready tables
