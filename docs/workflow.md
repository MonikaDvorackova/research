---
id: docs-workflow
title: Research Workflow
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
---

# Research Workflow

Day-to-day operating model for this workspace.

## Design decision

Work advances **inside a topic** through knowledge stages. Publications branch off after research is strong enough to narrate — they do not replace earlier stages.

```text
Capture → Topic → Ideas → Notes + Literature → Architecture → Specifications
                                                      ↓
                                              Publications (derived)
```

**Why this order:** Publishing before specification freezes invites rewriting “truth” to fit a word limit. Specs and ADRs keep claims stable across venues.

## 1. Capture (`inbox/`)

- Drop raw thoughts as `YYYY-MM-DD-<slug>.md`.
- Triage within about a week: promote into a topic, merge into an existing note, or delete noise.

**Decision:** Inbox is deliberately shallow so capture stays frictionless without polluting `topics/`.

## 2. Charter a topic

1. Copy `docs/templates/topic/` → `topics/<slug>/`.
2. Fill `charter.md` (purpose, scope, non-goals).
3. Fill `meta.yaml` (status, tags, related topics).
4. Register in `catalog/topics.yaml`.

**Decision:** A charter is mandatory. Topics without scope become dumping grounds within months.

## 3. Ideas → notes → literature

| Stage | Folder | Goal |
|---|---|---|
| Ideas | `ideas/` | Half-formed claims; no normative language |
| Notes | `notes/` | Working knowledge and claim inventories |
| Literature | `literature/` | Source summaries with `cite_key` |

Add bibliographic entries to `references/bib/library.bib` (one shared library).

**Decision:** Literature notes are first-class Markdown summaries, not PDF filenames. Lab memory must survive without opening binaries.

## 4. Architecture

Record durable decisions in `architecture/` (ADRs, views, trade-offs). Keep editable diagram sources beside SVG exports.

**Decision:** Architecture is separate from specifications so rationale (why) does not get mixed with normative text (what shall be).

## 5. Specifications

Promote stable, citeable rules into `specifications/` with semantic versions and clear status (`draft` → `review` → `accepted`).

Tag releases: `spec/<topic>/<name>@vX.Y.Z`.

**Decision:** Only specifications are normative. Notes may be wrong; specs are what publications pin.

## 6. Reviews and future work

- External/internal feedback → `reviews/YYYY-MM-DD-<context>.md` (append decisions).
- Deferred threads → `future-work/` (do not delete unresolved questions from notes without a pointer).

## 7. Derive publications

When claims are evidence-backed and specs are frozen enough:

1. Follow [publication-workflow.md](publication-workflow.md).
2. Copy a venue template from `docs/templates/publications/`.
3. Keep inventing claims in the topic, not in the draft.

## Status vocabulary

| Status | Typical use |
|---|---|
| `inbox` | Unowned capture |
| `active` | Topic work in progress |
| `draft` | Spec or publication under revision |
| `review` | Review in flight |
| `submitted` / `accepted` | Publication venue states |
| `published` | Released artifact |
| `archived` | Topic moved under `archive/` |

## Weekly rhythm (recommended)

1. Empty or triage `inbox/`.
2. Update claim inventories in active topics.
3. Advance at least one note toward architecture or specification when claims stabilize.
4. Sync `catalog/*.yaml` with reality.

## What not to do

- Start an article folder without a topic.
- Put venue prose in `notes/`.
- Rewrite accepted ADRs in place (supersede instead).
- Use Overleaf as the only copy of prose.
