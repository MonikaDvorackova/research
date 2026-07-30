---
id: area-publications-readme
title: Publications
type: governance
status: active
updated: 2026-07-30
---

## Publications

Derived, venue-shaped outputs only. Not the research source of truth.

### Active publication packages (canonical)

Active manuscript projects live in **numbered packages**:

| Package | Publication | Venue |
|---|---|---|
| [`01-jair/`](01-jair/) | Publication 01 | Journal of Artificial Intelligence Research (JAIR) |
| [`02-jurix2026/`](02-jurix2026/) | Publication 02 | JURIX 2026 |

Each package holds its own planning (when present), manuscript, figures, and submission artefacts. Do not place active manuscripts under venue category folders.

### Venue category placeholders

These directories are **category stubs** for future short-form or template-driven pieces. They are **not** the canonical home of active manuscript projects:

| Folder | Venue category |
|---|---|
| `articles/` | Website / long-form |
| `radar/` | O’Reilly Radar |
| `conference/` | Conference manuscripts (category only) |
| `journal/` | Journal articles (category only) |
| `whitepapers/` | Whitepapers |
| `books/` | Book projects and chapters |

Templates: [docs/templates/publications/](../docs/templates/publications/).
Process: [docs/publication-workflow.md](../docs/publication-workflow.md).

### Hard rule

Every publication declares `source_topics` pointing at `topics/<slug>/`.
