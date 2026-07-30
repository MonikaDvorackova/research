# Build instructions — JAIR submission package

## Prerequisites

- [Tectonic](https://tectonic-typesetting.github.io/) (`brew install tectonic`)
- [Graphviz](https://graphviz.org/) (`dot`) for figure regeneration
- System fonts: Times New Roman (macOS Supplemental fonts used in this build)

## Regenerate figures

```bash
cd publications/01-jair/figures
for f in fig{1,2,3,4,5}-*.dot; do
  base=$(basename "$f" .dot)
  dot -Tpdf -Gsize="6.5,9!" -o "${base}.pdf" "$f"
  dot -Tsvg -Gsize="6.5,9!" -o "${base}.svg" "$f"
done
cp fig{1,2,3,4,5}-*.{pdf,svg,dot,mmd} ../submission/figures/
```

Editable sources: `.mmd` (Mermaid) and `.dot` (Graphviz) under `publications/01-jair/figures/`. Rendered submission assets: `.pdf` / `.svg` (also mirrored under `submission/figures/` for a self-contained build).

## Compile manuscript PDF

```bash
cd publications/01-jair/submission
tectonic -X compile paper.tex --keep-logs
```

Output: `paper.pdf`.

## Important: official JAIR format

JAIR requires the official Author Kit (ACM-based) for portal submission:

- <https://www.jair.org/index.php/jair/formatting>
- Overleaf: <https://www.overleaf.com/read/hycbzkdksrzz#8106d4>

Before portal upload:

1. Copy content into the JAIR Author Kit template.
2. Merge the official reproducibility checklist (replace Appendix A draft).
3. Recompile and verify cross-references.

This package provides a complete journal-neutral LaTeX+PDF build suitable for content review and as the content source for the Author Kit migration.

## Source of truth

- Narrative Markdown (preserved): `../manuscript/paper-v1.md`
- Canonical figure sources: `../figures/`
- Research artefacts: `../../../topics/ai-infrastructure-gap/`
- Shared bibliography: `../../../references/bib/library.bib` (submission copy may coerce `@legislation` → `@misc` for BibTeX)
