---
id: pub-03-ltkm-overleaf-workflow
title: "Overleaf workflow — Publication 03"
type: research-notes
status: provisional
created: 2026-07-31
updated: 2026-07-31
---

# Overleaf workflow — Publication 03

## Tension with lab defaults (documented honestly)

This research repository’s default is: **Markdown in git is canonical**; Overleaf is an **export / camera-ready sink** ([`docs/publication-workflow.md`](../../../docs/publication-workflow.md)).

Publication 03 is a **multi-author collaborative** paper whose technical coauthors may already work in LaTeX/Overleaf. No Overleaf URL is recorded in the repository yet.

Therefore the team must pick **one** explicit manuscript source of truth.

## Decision required (open question #20)

Choose **exactly one**:

### Option A — Overleaf is manuscript SOT (recommended if collabs already write LaTeX there)

| Artefact | Source of truth |
|---|---|
| Compiled paper (`.tex`, figures in paper, result tables) | **Overleaf project** (URL TBD) |
| Conceptual drafts before paste | This repo `planning/` + optional `manuscript/` Markdown working copies |
| Bibliography entries | Zotero → export to repo bib → sync into Overleaf |
| Planning, responsibilities, open questions | **This repo** |

**Sync rules (Option A):**

1. Name Overleaf project owner; others comment, not silent fork.
2. Section ownership matches [`author-responsibilities.md`](author-responsibilities.md); use Overleaf comments for review.
3. Monika drafts conceptual sections in Markdown here for versioned review, then ports to Overleaf `\section{...}` (or drafts directly in Overleaf if preferred — pick one per section).
4. After each major Overleaf milestone, export `.tex`/PDF snapshot into  
   `publications/03-iclr-long-term-knowledge-memory/overleaf-snapshots/` (dated), so the lab retains an auditable copy.
5. Result tables and experiment figures are inserted **only** by technical collaborators (or with their approval).
6. No second full manuscript in Google Docs.

### Option B — Repository Markdown is manuscript SOT (lab default)

| Artefact | Source of truth |
|---|---|
| Prose | `publications/03-iclr-long-term-knowledge-memory/manuscript/paper.md` |
| Overleaf | Pandoc/export only for camera-ready |

Use Option B only if all coauthors agree to edit via git/Markdown.

## Until the decision is made

- **Do not** create a competing full manuscript in this repo.
- Keep planning files here (already created).
- Monika may start conceptual drafts as  
  `publications/03-iclr-long-term-knowledge-memory/manuscript/sections/*.md`  
  **after** coauthors acknowledge Option A or B.

## Comment and review workflow (either option)

1. Conceptual claims: Monika opens PR or Overleaf comment thread.
2. Empirical claims: technical collabs own; Monika reviews for claim hygiene / terminology.
3. Freeze terminology glossary before merging Methods and Intro.
4. Double-blind: strip author files per ICLR instructions when preparing submission PDF.

## Figures, bibliography, experiment tables

| Asset | Integration rule |
|---|---|
| Conceptual architecture figure | Monika source (`.mmd`/SVG) in repo; PDF in Overleaf |
| Benchmark / result figures | Collabs; link data path in caption footnote or appendix |
| Bibliography | Single export path per [`zotero-workflow.md`](zotero-workflow.md) |
| Experiment tables | Generated from collab scripts; no hand-typed “placeholder numbers” in submission |

## Anti-patterns

- Divergent Overleaf + Markdown full texts both edited weekly.
- Private `.bib` only inside Overleaf.
- Pasting CR-Gap exploratory findings as Related Work “our prior results.”
