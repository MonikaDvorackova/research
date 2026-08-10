---
id: pub-03-openreview-submission-checklist
title: "OpenReview submission checklist"
type: planning
status: final
created: 2026-08-04
updated: 2026-08-04
---

# OpenReview submission checklist — WorldConsistMem

**PDF:** `publications/03-iclr-long-term-knowledge-memory/submission/worldconsistmem.pdf`  
**Source zip:** `publications/03-iclr-long-term-knowledge-memory/submission/package/worldconsistmem-openreview.zip`  
**Compile log:** `publications/03-iclr-long-term-knowledge-memory/submission/logs/compile.log`

## Venue / format

- [x] Official ICLR 2026 style (`iclr2026_conference.sty` / `.bst` from ICLR Master-Template)
- [x] Anonymous authors (`%\iclrfinalcopy` remains commented)
- [x] Compiles with tectonic (BibTeX + PDF)
- [x] Bibliography rendered (10 keys)
- [x] No undefined citations / references in log
- [x] Ethics statement present (synthetic data; N/A for human subjects)
- [x] Reproducibility statement present
- [x] Acknowledgements omitted for double-blind
- [x] Appendix present (related work detail, fairness, extra tables/figures)

## Content hygiene (packaging)

- [x] YAML / freeze notes / planning paths / experiment paths removed from submission PDF
- [x] Duplicate inline result tables removed (single publication tables)
- [x] Numeric display synced (round half-up to 3 decimals): B3 BCR **0.063**, H0 Abs **0.483**, etc.
- [x] Figures appear in order 1→5 by first reference (difficulty figure in appendix as Fig.~5)
- [x] No author-identifying local paths in PDF

## Page budget (ICLR main text ≤ 9 pages)

| Section | Approx.\ start page (current PDF) |
|---|---|
| Intro | 1 |
| Related (short) | 3 |
| Object | 3 |
| Benchmark | 5 |
| Metrics | 6 |
| Systems | 7 |
| Setup | 8 |
| **Results** | **9** |
| Failures / Discussion / Conclusion | 11–13 |
| Appendix | 15+ |

- [x] Results section begins within the first 9 pages
- [ ] Optional author follow-up: further compress §§3–6 if you want full Qwen tables inside pages 1–9

## Upload steps (manual)

1. OpenReview → ICLR 2026 → Create submission  
2. Upload `worldconsistmem.pdf` as primary PDF  
3. Upload `worldconsistmem-openreview.zip` as supplementary source (if required)  
4. Confirm anonymity checklist on OpenReview  
5. Do **not** uncomment `\iclrfinalcopy` until camera-ready  

## Scientific freeze

No changes to RQ, benchmark, experiments, metrics definitions, conclusions, or scientific claims. Display rounding synchronized only.
