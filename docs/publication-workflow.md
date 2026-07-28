---
id: docs-publication-workflow
title: Publication Workflow
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
---

# Publication Workflow

How research becomes website articles, O’Reilly Radar pieces, conference papers, journal articles, whitepapers, and book chapters — without turning publications into the source of truth.

## Design decision: project, do not rewrite

Publications are **derived narratives**. Claims, decisions, and normative text live in `topics/`. Each publication declares `source_topics` and pinned `spec_refs`.

**Why:** One research program yields many venue shapes. If the article is canonical, every reuse is a fork. If the topic is canonical, each venue is an adaptation.

## Prerequisites

Before opening a publication draft:

1. Topic charter exists and scope is clear.
2. Claim inventory in `notes/` is defendable.
3. Relevant specifications are frozen at a citeable version (when the piece depends on normative text).
4. Catalog entry for the topic is up to date.

## Templates

Copy from `docs/templates/publications/`:

| Venue | Template | Destination |
|---|---|---|
| Website article | `website-article.md` | `publications/articles/` |
| O’Reilly Radar | `oreilly-radar.md` | `publications/radar/` |
| Conference paper | `conference-paper.md` | `publications/conference/` |
| Journal paper | `journal-paper.md` | `publications/journal/` |
| Whitepaper | `whitepaper.md` | `publications/whitepapers/` |
| Book chapter | `book-chapter.md` | `publications/books/<book-slug>/chapters/` |

Every template includes a **spine** section (audience, thesis, claim→section map, figures, venue targets). Complete the spine before polishing prose.

## Process

```text
Prepare (internal)          Submit (external)           Release (public)
─────────────────────       ─────────────────────       ─────────────────────
Freeze cited specs          Export venue package        status: published
Complete spine              Tag pub/<id>@v0.x           Tag pub/<id>@v1.0
Register in catalog         Track venue_status          Deploy site if applicable
Open review checklist       Store reviews/              Errata or new version only
```

### Prepare

1. Copy the venue template; set `id`, `source_topics`, `spec_refs`.
2. Fill the spine; refuse sections that lack topic evidence.
3. Add `catalog/publications.yaml` entry.
4. Open a review checklist under the topic `reviews/` folder.

### Submit

1. Export with Pandoc (or venue tooling) from Markdown — do not rewrite in Overleaf as the only copy.
2. Tag a pre-release: `pub/<id>@v0.x`.
3. Update `venue_status` in frontmatter and catalog.
4. File reviewer/editor feedback in `reviews/` (append decisions). Feedback that changes knowledge must update the topic.

### Release

1. Set publication `status: published` and record `doi_or_url` when available.
2. Tag `pub/<id>@v1.0`.
3. For website pieces with `publish: true`, deploy via the Astro site pipeline.
4. After release: substantive advances go to the topic (new spec version if needed). Public text changes via errata or a new publication version.

## Venue adaptation matrix

| Venue | Emphasis | Typical export |
|---|---|---|
| Website | Narrative, links | Astro content collection |
| O’Reilly Radar | Trend + implication | Markdown → Radar template |
| Conference | Academic framing, related work | Pandoc → LaTeX / Overleaf |
| Journal (e.g. IEEE Software) | Practitioner rigor | Pandoc → DOCX / LaTeX |
| Whitepaper | Problem, approach, implications | PDF via Pandoc or site |
| Book chapter | Pedagogical arc | From mature topics/spines |

## Overleaf and camera-ready

Overleaf (or similar) is an **export target** for camera-ready LaTeX. Sync generated `.tex` if useful, but Markdown in this repository remains authoritative.

**Decision:** Treating Overleaf as home creates an unreviewable second truth and breaks the website/Radar pipeline.

## Git branches and tags

| Pattern | Use |
|---|---|
| `pub/<id>` | Drafting and submission packaging |
| `pub/<id>@vX.Y.Z` | Tagged releases |
| `spec/<topic>/<name>@vX.Y.Z` | Spec versions cited by publications |

## Hard rules

1. No publication without `source_topics`.
2. No new research claims only in venue prose.
3. Pin specification versions; do not cite “latest” implicitly.
4. Do not silently rewrite DOI’d or publicly released text.

## Related documents

- [workflow.md](workflow.md) — research lifecycle
- [writing-guidelines.md](writing-guidelines.md) — authoring conventions
- [workspace-architecture.md](workspace-architecture.md) — structural rationale
