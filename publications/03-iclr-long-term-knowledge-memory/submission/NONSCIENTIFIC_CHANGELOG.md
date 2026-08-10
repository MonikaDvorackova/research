---
id: pub-03-openreview-nonscience-changelog
title: "Non-scientific changes for OpenReview package"
type: planning
status: final
created: 2026-08-04
updated: 2026-08-04
---

# List of every non-scientific change

Scientific content (RQ, benchmark, experiments, metrics definitions, conclusions, claims) was **not** modified. Below are packaging-only changes.

## Format / scaffolding removal

1. Converted Markdown assembly to ICLR 2026 LaTeX (`iclr2026_conference`).
2. Removed YAML frontmatter, Contents TOC, freeze meta-headers, “Final figure/table list”, process notes.
3. Removed internal paths (`planning/…`, `experiments/…`, `FINAL_EXPERIMENT_STATUS.md`, CSV source lines).
4. Removed `mlx-community/` prefix from model string in submission text (model identity unchanged: Qwen2.5-3B-Instruct-4bit).
5. Cleaned bibliography note field for LogicVault (removed internal “bot wall” audit wording).

## Numeric display synchronization (round half-up to 3 decimals)

Canonical display rule applied wherever the same frozen value appeared multiple times:

| Quantity | Frozen raw | Display |
|---|---:|---:|
| B3 BCR (symbolic) | 0.0625 | **0.063** (was also 0.062) |
| H0 Acc (Qwen) | 0.1849 | 0.185 |
| H0 Abs (Qwen) | 0.4825 | **0.483** (was also 0.482) |
| B3 Acc (symbolic) | 0.5669 | 0.567 |
| H0 BCR (symbolic) | 0.8438 | 0.844 |
| Other Acc/BCR/CSR/Abs/Mal | as frozen | 3-decimal half-up |

No underlying CSV values were altered.

## Deduplication / float placement

6. Removed duplicated inline result tables; kept single publication tables.
7. Moved closest-work comparison table to appendix.
8. Moved detailed related-work subsections to appendix; left a short residual paragraph in main text (same citations/claims).
9. Moved difficulty figure, constraint-family table, query-family table, coverage table, and full fairness bullet list to appendix (main text retains claims + references).
10. Compressed experimental-setup section to a short protocol summary; details retained in appendix reproducibility section.

## Figures

11. Converted SVG figures to PDF for LaTeX inclusion.
12. Ensured appearance order: Fig.~1 pipeline, Fig.~2 inconsistency, Fig.~3 Acc–BCR/CSR, Fig.~4 constraint heatmap (main), Fig.~5 difficulty (appendix).

## OpenReview statements

13. Added Ethics Statement (synthetic; no human subjects).
14. Added Reproducibility Statement (anonymous; no identifying URLs).
15. Acknowledgements omitted for double-blind (`\iclrfinalcopy` commented out).

## Build artefacts produced

16. `submission/worldconsistmem.pdf`
17. `submission/package/worldconsistmem-openreview.zip`
18. `submission/logs/compile.log`
19. `submission/SUBMISSION_CHECKLIST.md`
20. This changelog
