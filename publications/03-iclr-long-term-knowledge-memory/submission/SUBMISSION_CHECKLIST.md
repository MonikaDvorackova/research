---
id: pub-03-openreview-submission-checklist
title: "OpenReview submission checklist"
type: planning
status: active
created: 2026-08-04
updated: 2026-09-07
---

# OpenReview submission checklist — WorldConsistMem (ICLR 2027)

**PDF:** `publications/03-iclr-long-term-knowledge-memory/submission/worldconsistmem.pdf`  
**Source zip:** `publications/03-iclr-long-term-knowledge-memory/submission/package/worldconsistmem-openreview.zip`  
**Compile log:** `publications/03-iclr-long-term-knowledge-memory/submission/logs/compile_rescue.log`  
**Rescue plan/report:** `planning/iclr-poster-rescue-plan.md`, `planning/iclr-poster-rescue-report.md`

## Venue / format

- [x] Official ICLR **2027** style (`iclr2027_conference.sty` / `.bst`)
- [x] Anonymous authors (`%\iclrfinalcopy` remains commented)
- [x] Compiles with tectonic (BibTeX + PDF)
- [x] Bibliography rendered
- [x] Mandatory **AI Use Statement** present (outside page limit)
- [x] Ethics statement present
- [x] Reproducibility statement present
- [x] Acknowledgements omitted for double-blind
- [x] Appendix present

## Page budget (ICLR main text ≤ 9 pages)

| Marker | Page (current PDF) |
|---|---|
| Results start | 4 |
| Discussion | 5 |
| Conclusion | 7 |
| References start | 8 |
| Appendix | 9–12 |

- [x] Main text through Conclusion is within 9 pages (currently ends p.7)

## Content hygiene

- [x] No author-identifying local paths in PDF
- [x] Numeric display synced (half-up 3 decimals)
- [x] Architecture superiority not claimed
- [x] BCR=0 defended with gold H4 sanity + multi-violation diagnostics
- [x] New rescue experiments labelled separately from Option A freeze

## Still manual before upload

- [ ] Anonymized code/data zip from `~/worldconsistmem-experiments` (research `experiments/worldconsistmem/` is empty)
- [ ] Coauthor edit of AI Use Statement to match actual practice
- [ ] OpenReview abstract by 2026-09-18 AOE; full paper by 2026-09-25 AOE
- [ ] Confirm reciprocal-reviewing / author-quota rules for all coauthors

## Scientific freeze

Option A Qwen/symbolic freeze remains authoritative. Rescue P1 outputs in `planning/rescue_p1_artifacts/` are labelled NEW and must not silently replace freeze tables.
