---
id: docs-workspace-architecture
title: Research Workspace Architecture
type: governance
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [meta, governance, workflow]
---

# Research Workspace Architecture

This document defines the long-term structure and operating model for an independent research program covering software architecture, AI systems, governance, distributed systems, and multi-venue publication (website, O’Reilly Radar, IEEE Software, ACM, whitepapers, Overleaf, book chapters).

**Horizon:** 5–10 years  
**Canonical format:** Markdown  
**Atomic unit of work:** Topic (not article)  
**Publication model:** Research → derived venue artifacts

Operational docs: [workflow.md](workflow.md) · [writing-guidelines.md](writing-guidelines.md) · [publication-workflow.md](publication-workflow.md) · [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## 1. Design intent

### 1.1 What this is

A research lab / standards-organization workspace: durable knowledge, versioned specifications, review trails, catalogs, and publication projections.

### 1.2 What this is not

- A personal notes dump
- A blog repository where posts are the source of truth
- A single-article project layout
- A LaTeX-first academic folder that cannot feed a website

### 1.3 North-star rule

> Research is canonical. Articles, Radar pieces, IEEE/ACM papers, and book chapters are **projections** of research — never the other way around.

**Why:** One research program yields many derivatives. If the article is the source, every reuse is a rewrite. If the topic is the source, reuse is projection with a story spine.

---

## 2. Core design decisions

| Decision | Choice | Rationale |
|---|---|---|
| Unit of organization | **Topic** (`topics/<slug>/`) | Survives multiple papers, venues, and years; articles do not |
| Source format | **Markdown + YAML frontmatter** | Diffable, Pandoc-friendly, Astro-friendly, GitHub-native |
| Capture path | **`inbox/` → weekly triage** | Low friction capture without polluting topic trees |
| Discoverability | **`catalog/*.yaml`** | Scales past filesystem browsing (~100+ docs) |
| Normative knowledge | **`specifications/` with semver** | Specs are citeable; notes are not |
| Narrative outputs | **`publications/` only** | Hard separation of knowledge vs product |
| Diagrams | **Source + export in-repo** | Editable Mermaid/Excalidraw/PlantUML + SVG; no binary-only figures |
| References | **Shared BibTeX** | One citation key space across topics and venues |
| Website | **Astro content collections from publications** | Research section of existing site; opt-in publish flags |
| Academic PDF | **Export via Pandoc / Overleaf** | Overleaf is a camera-ready sink, not the home of truth |
| Dormant work | **`archive/`** | Keeps `topics/` as the active working set |

---

## 3. Repository tree

```text
research/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── catalog/
│   ├── topics.yaml                 # machine-readable topic index
│   ├── publications.yaml           # publication registry + venue status
│   └── glossary.md                 # shared terminology
├── inbox/
│   └── YYYY-MM-DD-<slug>.md        # untriaged capture
├── topics/
│   └── <topic-slug>/               # copy from docs/templates/topic/
│       ├── charter.md              # purpose, scope, non-goals
│       ├── meta.yaml               # status, owners, tags, related topics
│       ├── ideas/
│       ├── notes/
│       ├── literature/
│       ├── architecture/
│       ├── specifications/         # normative specifications (versioned)
│       ├── reviews/
│       └── future-work/
├── publications/
│   ├── articles/                   # website / long-form narratives
│   ├── radar/                      # O’Reilly Radar adaptations
│   ├── conference/                 # ACM / conference manuscripts
│   ├── journal/                    # IEEE Software and similar
│   ├── whitepapers/
│   └── books/
│       └── <book-slug>/
│           └── chapters/
├── references/
│   ├── bib/
│   │   └── library.bib             # single shared bibliography
│   └── sources/                    # optional PDFs (license-aware)
├── figures/
│   └── shared/                     # cross-topic reusable figures
├── implementations/
│   └── <impl-slug>/                # minimal reference code proving claims
├── archive/
│   └── <topic-slug>/               # frozen topics (pointer remains in catalog)
├── site/                           # Astro app for /research section
│   └── src/content/
├── docs/
│   ├── workspace-architecture.md   # this file
│   ├── templates/
│   └── workflows/
└── .github/
    └── workflows/
        ├── validate.yml
        ├── build-site.yml
        ├── deploy.yml
        └── export-paper.yml
```

### 3.1 Why topic-centric (not stage-centric)

A stage-only tree (`ideas/`, `articles/`, …) scatters related work. At year five you cannot answer “everything we know about AI system boundaries.” Topic folders keep the knowledge graph local; stages are **subfolders inside the topic**.

### 3.2 Why publications are outside topics

Venue prose has different structure, length, tone, and IP constraints. Keeping it under `publications/` prevents research notes from being silently rewritten to please a word limit, and allows one topic to feed many publications.

### 3.3 When to introduce `programs/`

Delay program-level grouping until you have ~30+ topics and natural clusters (e.g. governance, distributed systems). Premature taxonomy creates empty scaffolding and rename churn.

---

## 4. Folder responsibilities

| Path | Responsibility | Must not contain |
|---|---|---|
| `inbox/` | Fast capture; triage within ~7 days | Long-lived research |
| `topics/*/ideas/` | Unvalidated sparks | Normative “shall” language |
| `topics/*/notes/` | Working knowledge, claim lists | Camera-ready venue prose |
| `topics/*/literature/` | Source summaries + critique | Uncited PDF-only “notes” |
| `topics/*/architecture/` | Decisions, views, trade-offs | Submission cover letters |
| `topics/*/specifications/` | Normative, versioned truth | Marketing tone |
| `topics/*/reviews/` | Reviewer/editor feedback + decisions | Deleted history (append) |
| `topics/*/future-work/` | Deferred threads | Active primary claims |
| `publications/**` | Venue-shaped narratives + spines | New research claims without topic backfill |
| `references/` | Shared citation corpus | Topic-private contradictory keys |
| `figures/` | Shared durable assets | One-off scratch sketches (keep those in topic) |
| `implementations/` | Evidence for architectural claims | Production products |
| `catalog/` | Indexes for humans and CI | Duplicate prose |
| `site/` | Public projection | Private notes unless `publish: true` |
| `archive/` | Frozen topics | New active writing |

**Hard rule:** Every file under `publications/` declares `source_topics` in frontmatter pointing at one or more `topics/<slug>/`.

---

## 5. Lifecycle model

```text
Idea → Research → Architecture → Specification → Article → Conference Paper → Book Chapter
```

| Stage | Location | Exit criteria |
|---|---|---|
| Idea | `inbox/` or `topics/*/ideas/` | Claimed by a topic charter |
| Research | `notes/` + `literature/` | Claims backed by sources or explicit assumptions |
| Architecture | `architecture/` | ADRs + diagrams for major decisions |
| Specification | `specifications/` | Normative text + semver + status |
| Article | `publications/articles/` | Spine + draft citing frozen specs |
| Conference | `publications/conference/` | Venue package + Overleaf export if needed |
| Book chapter | `publications/books/...` | Pedagogical arc over mature topics |

**Important:** Later stages do not delete earlier ones. Specifications remain citable after an article ships. Book chapters accumulate from mature topics; they do not invent a parallel knowledge base.

### 5.1 Status vocabulary

| Status | Meaning |
|---|---|
| `inbox` | Captured, unowned |
| `active` | Primary working state for topic docs |
| `draft` | Publication or spec under revision |
| `review` | Internal or external review in flight |
| `submitted` | At a venue (publications only) |
| `accepted` | Venue accepted (publications only) |
| `published` | Released; further change via errata or new version |
| `archived` | Frozen under `archive/` |

---

## 6. Naming conventions

### 6.1 Files and folders

- **kebab-case** everywhere
- **Dates:** `YYYY-MM-DD` prefix for inbox items and review rounds
- **Topic slugs:** short, stable, noun phrases (`ai-system-boundaries`, not `new-ideas-july`)
- **Figures:** `<topic>--<diagram-name>.svg` (double hyphen separates topic from diagram)
- **Implementations:** same slug family as the topic when 1:1
- **No venue names** in research filenames (`ieee-draft.md` belongs under `publications/`, not `notes/`)

### 6.2 Document IDs

Stable IDs in frontmatter, independent of filename:

```yaml
id: note-boundary-threats
```

Pattern: `<type>-<short-slug>` where type ∈ `idea | note | lit | adr | spec | review | pub | chap`.

### 6.3 Citation keys

`authorYearShortTitle` in `references/bib/library.bib`, e.g. `bass2021softwareArch`.

---

## 7. Document metadata

### 7.1 Minimum frontmatter (all Markdown docs)

```yaml
---
id: note-boundary-threats
title: Boundary threat model notes
topic: ai-system-boundaries   # omit only for pure inbox items
type: note                    # idea|note|literature|architecture|spec|review|publication|chapter|governance
status: active
created: 2026-07-28
updated: 2026-07-28
tags: [governance, boundaries]
refs: [bass2021softwareArch]
---
```

### 7.2 Specs (additional)

```yaml
version: 1.2.0
status: draft                 # draft|review|accepted|deprecated
normative: true
supersedes: spec-boundary-model@1.1.0
```

### 7.3 Publications (additional)

```yaml
id: pub-2026-govai-boundaries
source_topics: [ai-system-boundaries]
spec_refs: ["ai-system-boundaries/specifications/boundary-model@1.2.0"]
venues: [website, radar, ieee-software]
venue_status:
  website: draft
  radar: planned
  ieee-software: planned
publish: false                # Astro opt-in
doi_or_url: null
# Spine lives in the publication Markdown (see templates)
```

### 7.4 Catalog entries

`catalog/topics.yaml` and `catalog/publications.yaml` are the **discovery index**. CI should fail PRs that add a topic folder without a catalog entry (and vice versa).

---

## 8. Versioning

| Artifact | Scheme | Mechanism |
|---|---|---|
| Specs | Semantic versioning | Frontmatter `version` + git tag `spec/<topic>/<name>@vX.Y.Z` |
| Architecture ADRs | Immutable once accepted | New ADR supersedes; do not rewrite history |
| Notes / ideas | No semver | `updated` date + git history |
| Publications | Status + optional semver for major revisions | Tag `pub/<id>@vX.Y.Z` at camera-ready / public release |
| Site | Calendar or sha | Tag `site@YYYY.MM.DD` on production deploys |

**Rule:** Articles cite **pinned** spec versions. Updating a spec to 2.0 does not silently change a published article; a new publication version or errata is required.

---

## 9. Diagrams

1. Prefer **text-first** sources: Mermaid (`.mmd`), PlantUML (`.puml`), Excalidraw (`.excalidraw`).
2. Commit **exported SVG** (or PDF for papers) beside the source.
3. Topic-local figures live under `topics/<slug>/architecture/figures/` or `topics/<slug>/figures/`.
4. Promote to `figures/shared/` only when reused across topics or publications.
5. Publications reference figures by path + optional content hash note in the spine, so camera-ready sets do not drift.

**Why not only images:** Binary-only diagrams rot, cannot be reviewed in PRs meaningfully, and block Pandoc/Astro reuse.

---

## 10. References

- Single library: `references/bib/library.bib`
- Every `literature/` note includes `cite_key` and a 5–10 sentence summary (claim, method, relevance, critique)
- Optional PDFs under `references/sources/` only when license permits; never treat PDF as the only artifact
- Literature notes may link out to Zotero/DOI; the Markdown summary remains required for lab memory

---

## 11. Drafts and publication tracking

### 11.1 Drafts

- Research drafts: `status: draft|active` in place (no parallel `drafts/` tree inside topics — status is enough)
- Publication drafts: either `status: draft` on the main file or a `drafts/` subfolder **inside** that publication’s directory for venue experiments
- Never fork research notes into a publication folder “to edit freely”; change claims in the topic, then re-project

### 11.2 Tracking

Register every intended output in `catalog/publications.yaml`:

```yaml
- id: pub-2026-govai-boundaries
  title: Boundaries for Governable AI Systems
  source_topics: [ai-system-boundaries]
  venues:
    website: { status: draft, path: publications/articles/govai-boundaries.md }
    radar: { status: planned, path: null }
    ieee-software: { status: planned, path: null }
  created: 2026-07-28
```

Review rounds: `topics/<slug>/reviews/YYYY-MM-DD-<venue>.md` (append-only decisions). Feedback that changes the research agenda also creates items under `future-work/`.

---

## 12. Writing workflow (multi-venue)

```text
1. Capture          → inbox/ or topics/*/ideas/
2. Charter topic    → topics/<slug>/charter.md + catalog entry
3. Claim inventory  → notes/ (each claim linked to evidence)
4. Literature       → literature/ + library.bib
5. Architecture     → architecture/ ADRs + figures
6. Spec freeze      → specifications/ @ v1.x (tag)
7. Story spine      → section inside the publication Markdown template
8. Venue drafts     → articles/ | radar/ | journal/ | conference/ | whitepapers/ | books/
9. Export           → Pandoc / Overleaf / Astro
10. Review & tag    → reviews/ + pub/<id>@vX.Y.Z
```

### 12.1 Story spine (required before serious drafting)

Each publication template includes a **Spine** section. Complete it before polishing prose. It contains:

- Audience and thesis (one paragraph)
- Claim → section map
- Figure list with source paths
- `source_topics` and pinned `spec_refs`
- Target venues and length budgets
- What is **out of scope** for this narrative (points back to future-work)

### 12.2 Venue adaptation

| Venue | Tone / form | Home | Export |
|---|---|---|---|
| Website (Astro) | Narrative, link-rich | `publications/articles/` | Content collection |
| O’Reilly Radar | Trend + implication | `publications/radar/` | Venue template from Markdown |
| IEEE Software | Practitioner rigor | `publications/journal/` | Pandoc → DOCX/LaTeX |
| ACM | Academic framing | `publications/conference/` or `journal/` | Pandoc → `acmart` / Overleaf |
| Overleaf | Camera-ready | `publications/**/overleaf/` (generated or synced) | Git sync or upload |
| Book chapter | Pedagogical arc | `publications/books/...` | From mature spines |

**Pandoc is the bridge.** Markdown remains canonical; Overleaf is not the research home.

---

## 13. Publication workflow

```text
Prepare (internal)     Submit (external)        Release (public)
─────────────────      ─────────────────        ────────────────
Freeze cited specs          Export venue package        status: published
Complete publication spine  Tag pub/<id>@v0.x           Tag pub/<id>@v1.0
Register in catalog         Track venue_status          Deploy site path
Open review checklist       Store reviews/              Errata or new version only
```

After publication, substantive research advances go into the **topic** (new spec minor/major). Public articles get errata or a new publication version — do not silently rewrite history of a DOI’d artifact.

---

## 14. Git strategy

### 14.1 Branches

| Branch | Purpose |
|---|---|
| `main` | Always valid catalog + buildable site |
| `topic/<slug>` | Research work for one topic |
| `pub/<id>` | Venue drafting and submission packaging |
| `site/<change>` | Astro/layout-only changes |

Prefer short-lived branches and small PRs. Long-running topic branches should rebase/merge from `main` regularly so catalog/CI rules stay current.

### 14.2 Commit prefixes

`research:` · `arch:` · `spec:` · `pub:` · `site:` · `chore:`

### 14.3 Tags

- `spec/<topic>/<name>@vX.Y.Z`
- `pub/<id>@vX.Y.Z`
- `site@YYYY.MM.DD`

### 14.4 What not to do

- Force-push `main`
- Commit secrets or licensed PDFs illegally
- Use Overleaf as the only copy of prose
- Amend published tags

---

## 15. GitHub, Actions, Astro, deployment

### 15.1 Natural integration shape

```text
publications/articles/*.md  ──►  site/src/content/research/  ──►  Astro build  ──►  /research on existing site
catalog/*.yaml              ──►  validation + generated indexes
topics/**                   ──►  private by default (opt-in publish: true)
```

### 15.2 Recommended workflows

| Workflow | Trigger | Job |
|---|---|---|
| `validate` | PR / push `main` | Frontmatter schema, catalog ↔ filesystem consistency, internal links |
| `build-site` | push affecting `site/` or `publications/` | Astro build |
| `deploy` | successful build on `main` | Deploy research section to existing website |
| `export-paper` | manual or `pub/*` tag | Pandoc → LaTeX/DOCX artifacts |
| `link-check` | weekly cron | External URL health for published pages |

### 15.3 Astro content collections

Map `publications/articles` (and optionally radar) to typed collections with a Zod schema matching publication frontmatter. Topic notes stay out of the collection unless explicitly flagged.

---

## 16. Best practices

1. **Triage inbox weekly** — undeleted inbox items older than 14 days are a process smell.
2. **Charter before depth** — a topic without `charter.md` scope will sprawl.
3. **Claims need evidence or labels** — mark assumptions explicitly.
4. **Freeze before submit** — pin spec versions in publication frontmatter.
5. **Append reviews** — do not erase reviewer history.
6. **One BibTeX library** — avoid per-topic bibliographies drifting apart.
7. **Keep implementations minimal** — prove the claim; do not build a product in-tree.
8. **Archive deliberately** — move dormant topics; leave catalog pointers.
9. **Write spines** — never jump from notes to IEEE formatting in one step.
10. **CI as librarian** — humans forget structure; validators enforce it.

### Anti-patterns

- Single global `notes/` dump
- Article folders with no `source_topics`
- Binary-only figures
- Overleaf / Google Docs as source of truth
- Rewriting research inside venue drafts
- Reviewer feedback only in email
- Premature `programs/` taxonomy
- Treating the website as the research archive

---

## 17. Future scalability (hundreds of documents)

| Pressure | Response |
|---|---|
| Too many files to browse | Rely on `catalog/` + generated site indexes + search |
| Topic too large | Split topic; record `related_topics` in both `meta.yaml` files |
| ~30+ topics | Introduce optional `programs/<program-slug>/` grouping **without** moving publication rules |
| Citation growth | Keep one `.bib`; consider `biber`/CSL in export pipeline |
| More collaborators | Add `CODEOWNERS` per program/topic; still trunk-friendly PRs |
| Multi-language later | `lang` frontmatter; do not fork entire tree per language |
| Dataset / large binaries | Git LFS or external object store; link from Markdown |

The structure is intentionally **shallow and repetitive** (same subfolders per topic). Repetition beats clever nesting when the archive spans a decade.

---

## 18. Bootstrap sequence (when you are ready to materialize)

This design document is the first artifact. When initializing the working tree (still not “creating GitHub” as a product goal — just local structure):

1. Keep this file as governance.
2. Add templates under `docs/templates/` (topic + publications — already present).
3. Create topics by copying `docs/templates/topic/` as needed.
4. Add Astro under `site/` when the first article is ready to publish.
5. Add GitHub Actions when collaboration or deployment begins.

**Do not optimize the tree for one article.** Optimize for the claim inventory and first topic charter.

---

## 19. Summary

| Layer | Question it answers |
|---|---|
| `inbox/` | What just occurred to us? |
| `topics/` | What do we know and decide? |
| `specifications/` | What is normative? |
| `publications/` | How do we tell which audience? |
| `catalog/` | How do we find it in year seven? |
| `site/` | What do we show the public? |
| `archive/` | What is frozen but retained? |

This is the operating model of a small research lab: capture → classify → decide → specify → project → review → publish → archive — with Markdown as the durable medium and Git as the long-term memory.
