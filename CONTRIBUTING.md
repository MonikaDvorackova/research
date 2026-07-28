---
id: docs-contributing
title: Contributing
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
---

## Contributing

This repository behaves like a small research lab. Contributions should preserve the separation between **research** (canonical) and **publications** (derived).

### Before you write

1. Read [docs/workspace-architecture.md](docs/workspace-architecture.md).
2. Follow [docs/workflow.md](docs/workflow.md) and [docs/writing-guidelines.md](docs/writing-guidelines.md).
3. For anything public-facing, follow [docs/publication-workflow.md](docs/publication-workflow.md).

### Markdown is canonical

- Author and edit **Markdown** (and YAML frontmatter) in this repository.
- Do not treat Overleaf, Google Docs, Word, or the live website as the source of truth.
- Export to LaTeX, DOCX, or HTML when a venue requires it; commit exports only if needed for reproducibility, never instead of Markdown.

**Why:** One source keeps diffs reviewable in Git, feeds Astro and Pandoc from the same files, and prevents venue forks from diverging silently.

### Creating a topic

```bash
cp -R docs/templates/topic topics/<slug>
# Edit topics/<slug>/charter.md and topics/<slug>/meta.yaml
# Add an entry to catalog/topics.yaml
```

`<slug>` is kebab-case and stable (e.g. `ai-system-boundaries`).

### Creating a publication

1. Confirm the topic has defendable claims and, when applicable, a frozen specification version.
2. Copy the matching template from `docs/templates/publications/` into `publications/<venue>/`.
3. Set `source_topics` and pinned `spec_refs` in frontmatter.
4. Register the publication in `catalog/publications.yaml`.

**Hard rule:** never start a publication that invents claims absent from `topics/`. Backfill the topic first.

### Commit messages

Use a short prefix:

| Prefix | Use |
|---|---|
| `research:` | Ideas, notes, literature |
| `arch:` | Architecture decisions and diagrams |
| `spec:` | Specifications |
| `pub:` | Publication drafts and spines |
| `site:` | Astro / deployment |
| `chore:` | Catalog, templates, CI, docs governance |

### Pull requests

- Keep PRs focused (one topic or one publication when practical).
- Update `catalog/*.yaml` when adding or archiving topics/publications.
- Do not commit secrets, proprietary PDFs without license clarity, or generated `node_modules/`.

### Reviews

Store review rounds under the topic’s `reviews/` (and venue notes under the publication folder if needed). Append decisions; do not erase history.

### Questions

If a contribution does not fit the tree, prefer extending documentation over inventing a one-off folder. Structural changes belong in `docs/workspace-architecture.md` first.
