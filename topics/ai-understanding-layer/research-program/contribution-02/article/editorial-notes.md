---
id: note-contribution-02-article-editorial-notes
title: "Article 2 — Editorial Notes (draft-v1)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, editorial-notes]
refs: [draft-v1.md, ../drafting-readiness/VERDICT.md, ../drafting-readiness/claim-ledger.md]
---

## Editorial Notes — draft-v1

Items in this file are deliberately **not** silently resolved. Each
needs a human decision before this draft can move toward publication.

## Unresolved citation issues

No external citation is placed inline in draft-v1's body — the draft
currently names mechanisms (W3C PROV, event sourcing, bitemporal
databases, distributed tracing, audit logs, lineage tools) without
footnoted sources, matching `article-01-decision-level-control/draft-v1.md`'s
own style (that draft also carries no inline citations in its body). This
needs an explicit decision:

- **If the target venue expects citations** (an academic-adjacent or
  O'Reilly-Radar-with-references style): add footnotes/endnotes using the
  exact sources already gathered and verified in
  `../prior-art-audit.md` and listed in `../drafting-readiness/VERDICT.md`'s
  "Required external citations" section (W3C PROV-DM 2013; Snodgrass
  TSQL2 / SQL:2011; Fowler, "Event Sourcing," 2005; in-toto spec; SLSA
  v1.0; Sigstore/Rekor docs; OpenTelemetry Specification; NIST SP 800-92;
  EU AI Act Art. 12; ACM Artifact Review and Badging v1.1; MLflow docs).
- **If the target venue is citation-light** (matching Article 1's own
  practitioner style): leave as-is.
- **One citation was not independently re-verified in this session**:
  OASIS XACML 3.0, added to `../drafting-readiness/prior-art-matrix.md`
  but not mentioned in draft-v1's body at all (it didn't make the cut for
  the article's tighter mechanism list). If a future revision adds it,
  re-fetch the primary spec before citing.

## Claims deliberately softened

Per `../drafting-readiness/claim-ledger.md`, every place a stronger
absolute claim was available and was not used:

- "Bitemporal databases... solve it completely — for exactly the cases
  without retroactive correction" — deliberately not "bitemporal
  databases are insufficient," which would misstate the actual,
  conditional result.
- "Event sourcing... is exactly the negative control's mechanism" is
  immediately qualified by "The catch is the qualifier" — deliberately
  not left as an unqualified endorsement.
- The False Historical Confidence section explicitly disclaims
  prevalence ("This is a result from one synthetic testbed... not a
  claim about how often this happens anywhere else") immediately
  adjacent to the strongest-sounding sentence in that section, per the
  claim ledger's requirement that scope statements accompany each result
  rather than being stated once and dropped.
- No sentence anywhere in the draft asserts that explicit binding is
  required, that provenance/event sourcing/PROV "cannot" solve the
  problem, that this proves compliance or trustworthiness benefits, or
  that the findings generalize to production systems — verified in
  `draft-v1-audit.md`.

## Places requiring human judgment

- **Tone of the closing bridge sentence.** The draft ends with: "Historical
  reconstructability is only one dimension of what it means to preserve
  understanding of a system over time." This is the one permitted
  Contribution-3 gesture per the authorizing brief, deliberately left
  undeveloped. A human editor may prefer to cut it entirely for a
  tighter, more self-contained ending — both options are defensible; this
  session did not choose between them beyond following the brief's
  explicit instruction to include exactly one such sentence.
- **Whether to name the synthetic system's domain.** The draft never says
  "Tier-2 Access Advisor" (the experiment design's actual name for the
  testbed) — it describes the scenario generically ("a risk score, a
  policy threshold, an approver role, a watchlist check") to keep the
  article's own voice rather than importing the experiment design
  documents' internal name. A human editor may prefer either choice.
- **Level of formality of the `R(D, x)` notation.** Used once, briefly, in
  "What a Historical Decision Actually Depends On," per
  `../drafting-readiness/formalization.md`'s recommendation to keep any
  formal notation minimal and optional. An editor uncomfortable with any
  notation in a practitioner piece could cut this single occurrence
  without losing any claim — the surrounding prose already states the
  same content.

## Diagram production requirements

Per `../drafting-readiness/diagram-plan.md`, three diagrams were planned;
none are rendered as images in draft-v1 — the repository has no Mermaid
usage anywhere in `topics/ai-understanding-layer/` and Article 1's own
diagram (`article-01-decision-level-control/diagram-spec.md`) was
likewise never rendered, only specified, so this draft follows the same
convention. The draft's two fenced code blocks under "Two Ways to
Preserve It" are the closest it comes to Diagram 1/2's content, rendered
as text rather than as a figure. If this article proceeds toward
publication, three figures should be produced:

1. **Versioned but unbound** — decision D, four parallel version
   histories, no arrows connecting D to any specific version (see
   `../drafting-readiness/diagram-plan.md` Diagram 1 for exact
   specification).
2. **Preserved causal context** — identical to (1) with arrows added from
   D to exactly one version per history, captioned to note the arrows are
   "reference only, no new facts" (Diagram 2).
3. **Temporal failure** — a timeline showing the same query, run before
   and after a backdated correction, returning different answers
   (Diagram 3).

None of the three are essential for a text-only publication; the prose
in "Experiment 1" and "Two Ways to Preserve It" carries the same content
without them.

## Publication venue questions

- This draft is written as an independent technical/practitioner article,
  per the authorizing brief, not yet adapted for any specific venue
  (O'Reilly Radar, a conference-adjacent blog, a standalone report). No
  venue-specific formatting (word-count caps, required abstract, required
  bio section) has been applied.
- Whether this becomes an O'Reilly piece is an explicit, separate,
  not-yet-made decision per `../../CHECKPOINT-2026-08-23.md`'s "O'Reilly
  Status" section and the authorizing brief's explicit instruction not to
  adapt it for O'Reilly in this pass.
- The article currently stands alone (no cross-reference to Article 1 or
  a not-yet-written Article 3). Whether a published version should
  cross-link to Article 1 (`article-01-decision-level-control/`) is an
  open editorial question, not resolved here — the authorizing brief did
  not ask for that linkage, and adding it risks implying a stricter
  dependency between the two contributions than `../../CHECKPOINT-2026-08-23.md`'s
  publication architecture actually specifies (a shared root premise, not
  a linear chain).

## Anything else that should not be silently resolved

- **Numbers are exact, not rounded for readability**, quoted directly
  from `../experiment/results/` and `../experiment/followup-case10/results/`
  (verified against the committed CSVs immediately before drafting — see
  `draft-v1-audit.md`'s evidence-traceability section for the specific
  figures and their source rows). Do not adjust these numbers in a later
  revision without re-checking them against the same files.
- **The "~60 seconds apart" framing of the original Case 10** is a plain-
  language restatement of the primary experiment's actual timestamps
  (11:59:00 and 12:01:00 around a 12:00:00 boundary) — accurate, but
  phrased for readability rather than quoted as raw timestamps; a
  reviewer wanting the exact figures should check
  `../experiment/results/case_level_results.csv` (Case 10 rows) directly.
