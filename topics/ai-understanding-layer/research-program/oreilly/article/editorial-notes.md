---
id: note-oreilly-article-editorial-notes
title: "O'Reilly Article draft-v1 — Editorial Notes"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, editorial-notes]
refs: [draft-v1.md, draft-v1-audit.md, ../../OREILLY-FINAL-BRIEF.md]
---

## Unresolved wording questions

- Section 2's "one model, many decisions" example (fraud-scoring model:
  automatic block above a threshold, human review below it, no action
  outside a category) is illustrative, not drawn from any tested case in
  Contribution 1's own material. It reads as illustrative in context
  ("might authorize... in one context and only... in another") but
  should be checked in adversarial review for whether a reader could
  mistake it for a real, audited scenario.
- Section 3's escalation-path paragraph and Section 4's retroactive-
  correction paragraph were both added during word-count expansion (see
  `draft-v1-audit.md` §12). Both add genuine, load-bearing content, not
  filler — but they are the two most natural candidates to trim first if
  an editor wants a tighter piece closer to the 3,500-word floor rather
  than the 4,000+ actual length.
- "Decision record" is used as the umbrella term for what Section 7's
  checklist populates, but the article never formally defines it as a
  named object the way it formally defines "consumption relation." Worth
  deciding in review whether it needs its own explicit definition
  sentence or whether the checklist context does that work sufficiently.

## Citation verification needed

- [4] Carlan, C. et al., "Dynamic Safety Cases for Frontier AI,"
  arXiv:2412.17618, 2024 — lead author and title confirmed via direct
  search of the arXiv PDF this session; the full co-author list (search
  results indicated approximately seven authors total) was not
  independently enumerated, so the citation uses "et al." rather than a
  complete author list. Before external publication, this should be
  re-fetched directly (not via search-summary) to confirm the complete
  author list and add it, per this programme's established citation-
  hygiene discipline (the same standard applied to Article 2's five
  citations and the research note's Sampath/Bakirtzis citations).
- [1]–[3] (W3C PROV-DM, OpenTelemetry Traces, Fowler's Event Sourcing)
  are reused verbatim from Article 2's already-verified reference list —
  no re-verification needed, but worth a final confirmation that the
  URLs still resolve before publication, since Article 2 was frozen
  earlier in this programme's timeline.

## Diagram production needs

The Section 7 diagram is a plain-text/ASCII block, per this drafting
task's instruction and consistent with Article 2's own unresolved
diagram question (`FINAL-ACCEPTANCE.md`: "none of the three planned
diagrams... are rendered as images... no repository convention for
rendering exists yet"). This article inherits the same open item: if
O'Reilly's actual publishing pipeline expects a rendered figure rather
than a text block, the ASCII diagram in Section 7 will need conversion
to a proper illustration before submission. Flagged here, not resolved.

## Possible cuts

- If the piece needs to shorten toward 3,500 words: the escalation-path
  and retroactive-correction paragraphs (see "Unresolved wording
  questions" above) are the cleanest cuts — each is self-contained and
  removable without breaking the surrounding argument.
- Section 6's fourth paragraph (the "none of this is unique to AI"
  paragraph) is important for the AI-exceptionalism boundary
  (`draft-v1-audit.md` §10) and should not be cut even under length
  pressure — flagging this explicitly so a future edit doesn't remove it
  by accident while looking for space.

## Title/dek questions

- Title is locked per this task's explicit instruction ("What Your AI
  Audit Trail Is Missing: The Relations, Not the Records") and was not
  reopened.
- Dek used: "Why approving an AI decision and explaining it later are
  two different engineering problems." This is close to but not
  identical to the task's suggested conceptual dek ("Why approving an AI
  decision and explaining it later are two different engineering
  problems") — used nearly verbatim as it was already precise. Flag for
  adversarial review only if the word "engineering" reads as too dry for
  an O'Reilly Radar-style dek; no strong alternative was tested in this
  pass.

## Flags for adversarial review

- **Structural question:** Section 6 ("This Isn't a New Mechanism")
  currently arrives after both C1 and C2 have been fully explained
  (Sections 3–4) and after C3's brief appearance (Section 5). An
  adversarial reviewer might ask whether crediting prior art this late
  risks a skeptical reader forming an inflated novelty impression during
  Sections 3–4 that Section 6 only corrects afterward, rather than
  preempting it. This drafting task's locked spine places prior art at
  position 6, and this draft followed that placement without
  relitigating it — worth an explicit editorial decision on whether the
  ordering should move prior-art credit earlier in a future revision.
- **Schema-worship risk:** Section 7's seven-field checklist is
  explicitly disclaimed as non-mandatory ("not a mandatory universal
  schema... a design pattern"), but checklists in practitioner articles
  tend to get treated as prescriptive regardless of disclaimers. Worth
  an adversarial pass specifically testing whether the disclaimer
  language is strong enough or whether the checklist should be
  restructured (e.g., as questions rather than field names) to reduce
  this risk further.
- **The "not only the model" qualifier:** a grep check during this
  audit found one bare "not the model" instance in Section 2 (the
  sentence introducing the decision-as-unit point, before the qualified
  version two sentences later) — corrected in this draft to "not only
  the model" as a mechanical phrasing fix against the brief's explicit,
  locked condition, not a change to any claim or evidence. Recorded here
  rather than left silent, since the audit's own first pass claimed
  (incorrectly) that no bare instance existed. Worth a fresh grep in
  adversarial review to confirm no other instance was missed.
