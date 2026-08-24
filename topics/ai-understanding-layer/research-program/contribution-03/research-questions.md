---
id: note-contribution-03-research-questions
title: "Contribution 3 — Research Questions Blocking Article 3"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, research-questions]
refs: [residual-gap-analysis.md, novelty-verdict.md]
---

## Minimum questions blocking Article 3

Derived directly from this review, not from the brief's illustrative
examples (though they overlap in substance).

1. **Can "system-level understanding" — across a multi-component AI
   decision pipeline, not a single model or a single decision — be
   operationalized as a measurable property, distinct from observability,
   provenance, and interpretability individually?** (`residual-gap-analysis.md`
   option D). Without an answer, Article 3 has no way to state its
   central claim as anything other than a metaphor, per
   `novelty-verdict.md`'s "Understanding Layer" disposition.
2. **Beyond the AI-agent-observability-tooling-specific "depth without
   integration" finding already confirmed (`ai-systems-review.md`),
   is there real evidence that explainability, provenance, governance,
   and auditability *as research communities* fail to coordinate — or
   does the fragmentation claim only hold at the narrower, already-
   confirmed tooling-integration scope?**
3. **Does Contribution 2's decision-specific consumption-relation
   finding generalize to Level 5 (behavioral envelope) or Level 6
   (human/operator knowledge), or does it remain scoped to individual
   decisions?** This is `../recommended-program.md`'s own flagged Q3 gap,
   still unresolved after this review — this review narrows the
   question (by locating exactly where existing fields already operate,
   `residual-gap-analysis.md`'s level table) but does not answer it.
4. **Would better integration of existing mechanisms (observability +
   provenance + assurance-case structuring) suffice, or is there a
   specific, nameable reason existing mechanisms cannot be composed
   without a new abstraction?** This is the direct test between residual-
   gap options B (integration) and E (architecture) — this review found
   strong evidence for B and none for E, but did not exhaustively rule
   out E; a more adversarial pass specifically on composability would be
   needed before claiming E is fully closed.
5. **Can a capability metric and an understanding metric be defined for
   the same system such that their relative rates of change are even in
   principle comparable — and if not, should the capability-vs-
   understanding framing be dropped from Article 3 entirely rather than
   merely softened?** Per `novelty-verdict.md`'s classification
   (untested conjecture, bordering unfalsifiable), this question's answer
   may simply be "no, and the framing should be dropped" — but that
   determination itself should be made deliberately, not by default.

## Not included as blocking (explicitly, to prevent scope creep)

Per the authorizing task's Section 29 instruction not to generate
questions merely because more are answerable: whether Git's history
"really" supports or undermines the historical-pattern claim in more
detail than `historical-literature-review.md` already establishes;
whether every individual XAI method aggregates to system understanding
(already answered narrowly, `ai-systems-review.md`); and any question
about real-production-system prevalence (explicitly out of scope for
this entire research programme, per Contribution 2's own repeated
disclaimers, reused here).
