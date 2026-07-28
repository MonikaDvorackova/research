---
id: tpl-topic-reviews-readme
title: Reviews folder
type: governance
status: active
---

## Reviews

### Purpose

Preserve review rounds, editorial feedback, and the decisions taken in response — for both research and publications tied to this topic.

### What belongs here

- Dated review notes (internal or external)
- Decision logs: what changed in the topic or publication as a result
- Checklists used before submission

### What does not belong here

- The research content itself (update `notes/`, `architecture/`, or `specifications/`)
- Secrets, private reviewer identities if policy forbids them (redact as needed)
- Disposable chat logs with no decisions captured

### Naming conventions

- `YYYY-MM-DD-<venue-or-context>.md`
- kebab-case; frontmatter `type: review`
- Append outcomes; do not delete prior review history

### Design note

Reviewer feedback is first-class research input. If it opens a new thread, also add an item under `future-work/`.
