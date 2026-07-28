---
id: tpl-topic-literature-readme
title: Literature folder
type: governance
status: active
---

## Literature

### Purpose

Summarize and critique sources that inform this topic. Build lab memory that survives without opening PDFs.

### What belongs here

- One Markdown note per important source (or tightly related cluster)
- Required: `cite_key` matching `references/bib/library.bib`
- Short summary: claim, method, relevance, critique (about 5–10 sentences)
- Optional DOI/URL links

### What does not belong here

- PDF binaries as the only artifact (optional files go under `references/sources/` with license care)
- Uncited reading lists with no substance
- Your own architecture decisions (use `architecture/`)
- Publication-related-work sections copied wholesale without a topic home

### Naming conventions

- Prefer `author-year-short-title.md` aligned with the cite key
- kebab-case; frontmatter `type: literature`
- Add or update the BibTeX entry in `references/bib/library.bib` in the same change when possible

### Design note

A single shared `.bib` file avoids per-topic citation drift. Literature notes are the human-readable layer on top of that library.
