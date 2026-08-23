---
id: topic-ai-understanding-layer-charter
title: "Capability vs. Understanding: From Evidence-Gated AI to an Understanding Layer"
topic: ai-understanding-layer
type: governance
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [architecture, conceptual, ai-systems, understanding, decision-provenance]
---

## Topic: Capability vs. Understanding

**Slug:** `ai-understanding-layer`
**Status:** `active`
**Owner:** Monika Dvořáčková

### 1. What this topic is

This topic captures and analyzes two source documents that represent different
stages of the same broader line of thinking:

- **Source A** — a conceptual article draft, *"The Missing Layer in the AI
  Stack: Why Capability Is Advancing Faster Than Understanding."*
- **Source B** — the original O'Reilly book proposal, *"Auditable AI: Building
  Evidence-Based Systems That Can Be Trusted."*

Both are stored verbatim under `sources/`. The working question for this topic
is **not** "how do we draft the next article" but **"does the intellectual
path from Source B to Source A contain several independently valuable
articles, and if so, what are they and in what order should they be
argued?"** This is a research-architecture task, not a drafting task.

### 2. Explicit independence from other work in this repository

This topic is a **new, independent publication line**. It must not be treated
as a continuation, restatement, or sibling of `topics/ai-infrastructure-gap`
or of the JAIR/JURIX manuscripts under `publications/01-jair` and
`publications/02-jurix2026`, even where vocabulary overlaps (e.g.
"reconstruction," "decision," "provenance," "AIGov Core").

- No file under this topic references, cites, or builds on those manuscripts.
- No connection to them is inferred, asserted, or implied anywhere in this
  topic's analysis.
- Those manuscripts and that topic are not modified as part of this work.

Any future decision to relate this line to that other work is a deliberate
human decision, not a byproduct of shared terminology.

### 3. Scope of this initialization

#### In scope

- Verbatim preservation of Source A and Source B.
- Reconstruction of Source B's deepest engineering claim, on its own terms.
- Identification of the conceptual step Source A adds on top of Source B.
- Construction of the intellectual argument chain connecting the two sources.
- Identification of natural article-level boundaries within that chain.
- Identification of the terminal/deepest thesis and protection of that thesis
  from being spent prematurely by earlier articles.
- Placement of the original Evidence-Gated AI / decision-level enforcement
  idea within the deeper model.
- Separation of candidate empirical/research questions by evidence type
  (repository audit, controlled failure experiment, AIGov Core demonstration,
  conceptual argument, legal analysis).
- A minimal candidate intellectual decomposition into article-level
  arguments, in recommended argument order.

#### Explicitly out of scope for this initialization

- Drafting any article (O'Reilly, SCRIPTed, journal, conference, or
  otherwise).
- Assigning venues to any candidate article.
- Producing or inventing empirical evidence (repository audit results,
  controlled failure experiment results, legal findings). Only candidate
  *questions* are recorded.
- Treating AIGov Core as proof of any general claim beyond what the sources
  themselves state (Source A explicitly hedges: "Whether this approach
  represents the right abstraction remains an open question").
- Any connection to JAIR/JURIX manuscripts or to `ai-infrastructure-gap`.

### 4. Central tension the sources describe

- **Source B** is centered on production AI, the distinction between model
  outputs and decisions, decision-level auditability, evidence as a
  first-class concept, enforcement, CI gates, controlled approval, and
  production governance.
- **Source A** appears to move one level deeper: capability → increasing
  system complexity → loss of reconstructable context → current state
  becoming insufficient → preservation of system knowledge → understanding as
  a first-class engineering concern, generalized beyond governance to
  explainability, interpretability, observability, provenance, and safety.

### 5. Entry points

| Kind | Path |
|---|---|
| Source A (verbatim) | `sources/source-a-missing-layer.md` |
| Source B (verbatim) | `sources/source-b-original-book-proposal.md` |
| Intellectual progression analysis (Tasks 2, 3, 4, 6, 7, 8) | `notes/intellectual-progression.md` |
| Candidate article decomposition (Tasks 5, 9) | `notes/candidate-articles.md` |

### 6. Related topics

None. Deliberately left empty — see §2.
