---
id: pub-03-ltkm-zotero-workflow
title: "Zotero workflow — Publication 03"
type: research-notes
status: provisional
created: 2026-07-31
updated: 2026-07-31
---

# Zotero workflow — Publication 03

**Repo evidence:** Lab uses one shared BibTeX library at `references/bib/library.bib` with key pattern `authorYearShortTitle` ([`docs/writing-guidelines.md`](../../../docs/writing-guidelines.md)). No Pub-03-specific Zotero collection is documented yet.

## Recommended setup

### 1. One shared Zotero collection

- Name: `Publication 03 — ICLR LTKM` (exact name TBD by collection owner).
- Group library preferred if coauthors are multi-institution; otherwise shared collection under one owner with coauthor access.
- **Owner (conflict resolution / deduplication):** TBD — must be named in open questions.

### 2. Subcollections or tags (align to sections)

Use **tags** (portable) plus optional subcollections:

| Tag / subcollection | Use |
|---|---|
| `pub03` | All Pub 03 items |
| `pub03/intro` | Motivation / gap cites |
| `pub03/agent-memory` | Agent memory systems |
| `pub03/lifelong` | Lifelong / continual knowledge |
| `pub03/conflict-temporal` | Conflicting / temporal / multi-hop QA |
| `pub03/benchmarks` | Agent / memory benchmarks |
| `pub03/baselines` | Systems actually compared |
| `pub03/methods` | Lifecycle / hierarchical memory methods |
| `pub03/must-cite` | Coauthor-required |

### 3. Better BibTeX citation keys

- Prefer lab convention: `authorYearShortTitle` (e.g. `packer2023memgpt`).
- If Better BibTeX auto-keys differ, set citekey pin on import and **do not** let auto-rename after export into the repo.
- One item → one citekey across Zotero, `library.bib`, and Overleaf.

### 4. Canonical `.bib` path in this repository

- **Canonical lab bibliography:** `references/bib/library.bib`
- Optional paper-local export (if Overleaf needs a slim file):  
  `publications/03-iclr-long-term-knowledge-memory/references/pub03.bib`  
  — **only** as an export from the shared collection, regenerated; do not hand-edit divergent copies.

**Rule:** New cites added for Pub 03 are added to Zotero first, then exported into `library.bib` (and regenerated `pub03.bib` if used).

### 5. Conflict resolution

- Collection owner merges duplicates (DOI/ISBN match).
- Do not keep two BibTeX entries for the same paper with different keys.
- Monika proposes keys for conceptual cites; owner arbitrates collisions.

### 6. Path into Overleaf without divergent copies

1. Maintain Zotero as bibliographic **entry** source.
2. Export Better BibTeX → update `references/bib/library.bib` in git.
3. Overleaf either:
   - **A (preferred with git sync):** pulls `library.bib` or `pub03.bib` from the repo; or
   - **B:** receives a dated export uploaded by the bib owner only (log date in `planning/project-status.md`).

**Forbidden:** Each author maintaining a private `.bib` inside Overleaf that is never exported back.

### 7. Reading notes

Optional literature notes under a future `topics/<ltkm-slug>/literature/` once a topic is declared. Until then, short notes may live in Zotero “Notes” or in `planning/literature-scratch.md` (create only if needed).
