---
id: docs-readme
title: Research Workspace
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
---

# Research Workspace

Long-term workspace for independent research in software architecture, AI systems, governance, and distributed systems — and for publications derived from that research.

## Canonical rule

**Markdown research is the source of truth.** Website articles, O’Reilly Radar pieces, conference and journal papers, whitepapers, and book chapters are *projections* of topic research. They are never the place where new knowledge is invented.

```text
Idea → Research → Architecture → Specification → Article → Conference Paper → Book Chapter
```

## Quick start

1. Capture a thought in [`inbox/`](inbox/README.md).
2. Promote it into a topic by copying [`docs/templates/topic/`](docs/templates/topic/) to `topics/<slug>/`.
3. Register the topic in [`catalog/topics.yaml`](catalog/topics.yaml).
4. When ready to publish, copy a template from [`docs/templates/publications/`](docs/templates/publications/) into the matching `publications/` folder and link `source_topics`.

## Documentation

| Document | Purpose |
|---|---|
| [docs/workspace-architecture.md](docs/workspace-architecture.md) | Design decisions and repository model |
| [docs/workflow.md](docs/workflow.md) | Day-to-day research lifecycle |
| [docs/writing-guidelines.md](docs/writing-guidelines.md) | How to write in this repo |
| [docs/publication-workflow.md](docs/publication-workflow.md) | Multi-venue publication process |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Conventions for contributing |

## Layout

| Path | Role |
|---|---|
| `inbox/` | Untriaged capture |
| `topics/` | Canonical research (one folder per topic) |
| `publications/` | Venue-shaped outputs only |
| `references/` | Shared bibliography |
| `figures/` | Shared reusable figures |
| `implementations/` | Minimal reference code |
| `catalog/` | Machine-readable indexes |
| `site/` | Astro research section (public projection) |
| `archive/` | Frozen topics |
| `docs/templates/` | Copy-from templates |

## Architectural decisions (summary)

- **Topic, not article, is the atomic unit** — one research thread can feed many venues over years.
- **Separate knowledge from product** — `topics/` holds durable knowledge; `publications/` holds narratives.
- **Specifications are versioned; notes are not** — cite pinned spec versions from publications.
- **Catalog indexes scale discovery** — do not rely on browsing alone after dozens of topics.
- **Exports are disposable** — Pandoc/Overleaf/HTML builds are derived; edit Markdown here.

This repository is optimized for a 5–10 year program, not a single article.
