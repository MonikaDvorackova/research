---
id: tpl-topic-future-work-readme
title: Future work folder
type: governance
status: active
---

## Future Work

### Purpose

Park deferred questions, follow-on studies, and out-of-scope threads that must not be forgotten — without cluttering active notes.

### What belongs here

- Explicitly deferred research questions
- Ideas that wait on dependencies (data, collaborators, prior specs)
- Spawns from reviews that are not in current scope

### What does not belong here

- Active primary claims (those stay in `notes/` or `ideas/`)
- Normative requirements (`specifications/`)
- Publication TODOs better tracked on the publication spine

### Naming conventions

- `<short-slug>.md` or `YYYY-MM-DD-<short-slug>.md`
- Frontmatter `type: note` or `idea` with `status` reflecting deferral (e.g. tag `future-work`)
- Link back to the originating note, review, or publication spine

### Design note

Archiving a question here is better than deleting it from a note. When work resumes, promote the item back into `ideas/` or `notes/` and mark the future-work file resolved.
