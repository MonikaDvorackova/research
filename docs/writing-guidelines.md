---
id: docs-writing-guidelines
title: Writing Guidelines
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
---

## Writing Guidelines

How to write inside this repository so work stays reviewable, citable, and reusable across venues.

### Design decision: one prose medium

All durable prose is **Markdown with YAML frontmatter**. Diagrams prefer text sources (Mermaid, PlantUML, Excalidraw) plus SVG export. Bibliography lives in BibTeX.

**Why:** Git diffs, Astro content collections, and Pandoc exports share one pipeline. Venue-specific formatting is applied at export time.

### Frontmatter (minimum)

```yaml
---
id: note-example-claim-inventory
title: Example claim inventory
topic: example-topic
type: note
status: active
created: 2026-07-28
updated: 2026-07-28
tags: []
refs: []
---
```

| Field | Notes |
|---|---|
| `id` | Stable key: `<type>-<short-slug>` |
| `type` | `idea` \| `note` \| `literature` \| `architecture` \| `spec` \| `review` \| `publication` \| `chapter` \| `governance` |
| `status` | See [workflow.md](workflow.md) |
| `topic` | Topic slug (omit only for pure inbox items) |
| `refs` | Citation keys from `references/bib/library.bib` |

### Naming files

- kebab-case only
- Inbox and reviews: `YYYY-MM-DD-<slug>.md`
- Figures: `<topic>--<diagram>.svg` (and matching source file)
- No venue names in research filenames (`ieee-draft.md` belongs under `publications/`)

### Voice by folder

| Location | Voice |
|---|---|
| `ideas/` | Tentative; questions welcome |
| `notes/` | Analytical; label assumptions |
| `literature/` | Descriptive + critique; always `cite_key` |
| `architecture/` | Decision-focused; alternatives considered |
| `specifications/` | Normative where intended; versioned |
| `publications/` | Audience-shaped narrative; no new orphan claims |

### Claims and evidence

- State claims explicitly.
- Link each claim to literature, data, an implementation, or a labeled assumption.
- Prefer short notes that compose over long undifferentiated essays in `notes/`.

### Specifications

- Use semantic versioning in frontmatter (`version: X.Y.Z`).
- Mark normative statements clearly.
- Record `supersedes` when replacing an older accepted version.
- Publications must pin the version they rely on.

### Citations

- One library: `references/bib/library.bib`.
- Key pattern: `authorYearShortTitle` (e.g. `bass2021softwareArch`).
- Literature notes summarize relevance in 5–10 sentences; do not rely on PDF alone.

### Diagrams

1. Commit editable source (`.mmd`, `.puml`, `.excalidraw`, …).
2. Commit SVG (or PDF for camera-ready) beside it.
3. Keep topic-local figures with the topic; promote to `figures/shared/` only when reused.

### Drafts vs published

- Research: use `status` in frontmatter (no parallel shadow tree).
- Publications: `status: draft` until release; after `published`, prefer errata or a new version over silent rewrites of DOI’d text.

### Style constraints

- Prefer precise technical language over marketing tone in `topics/`.
- Keep paragraphs short enough to review in a pull request.
- Do not embed secrets, credentials, or private personal data.

### Anti-patterns

- Article-first writing with research backfilled later
- Binary-only figures
- Per-topic bibliographies that drift from `library.bib`
- Copy-pasting the same claim into three venue drafts without a topic home
