---
id: tpl-topic-root-readme
title: Topic template
type: governance
status: active
---

## Topic template

Copy this entire directory to create a new topic:

```bash
cp -R docs/templates/topic topics/<slug>
```

Then:

1. Edit `charter.md` and `meta.yaml`.
2. Replace `<slug>` placeholders.
3. Add an entry to `catalog/topics.yaml`.

### Layout

| Path | Role |
|---|---|
| `charter.md` | Purpose, scope, non-goals |
| `meta.yaml` | Status, tags, relations |
| `ideas/` | Raw speculation |
| `notes/` | Working research |
| `literature/` | Source summaries |
| `architecture/` | Decisions and views |
| `specifications/` | Versioned normative text |
| `reviews/` | Review trails |
| `future-work/` | Deferred threads |

Do not add venue articles under a topic folder. Publications live in `publications/` and point here via `source_topics`.
