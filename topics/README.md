---
id: area-topics-readme
title: Topics
type: governance
status: active
---

# Topics

Canonical research lives here — one directory per topic.

## Create a topic

```bash
cp -R docs/templates/topic topics/<slug>
```

Edit `charter.md` and `meta.yaml`, then register in `catalog/topics.yaml`.

## Rules

- Do not store venue articles under a topic.
- Publications must reference topics via `source_topics`.
- Archive dormant topics to `archive/` and keep a catalog pointer.

Template: [docs/templates/topic/](../docs/templates/topic/).
