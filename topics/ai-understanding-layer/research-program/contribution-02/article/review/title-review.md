---
id: note-contribution-02-article-review-title-review
title: "Contribution 2 Article — Title Attack and Alternatives"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, title]
refs: [../draft-v1.md, reviewer-report.md]
---

## Title Attack

**Current title:** "Why Keeping Every Version Still Isn't Enough to
Explain an AI Decision"

### Attack, point by point

- **"Every version" — too absolute?** Low risk. Read in context, it
  restates the opening scenario's own premise ("nothing was deleted...
  every version exists") rather than asserting a universal claim about
  real systems. Not a required fix, but the word choice invites a
  literalist misreading ("nobody keeps literally every version") that a
  slightly softer phrase avoids for free.
- **"Explain" — confused with XAI/explainability?** **Real risk, and the
  strongest single objection to the current title.** "Explain an AI
  decision" is exactly the phrase used for model explainability
  (feature attribution, SHAP/LIME-style methods, interpretability). This
  article is not about explaining *model behavior* — it is about
  reconstructing *which historical context a decision used*. A reader
  arriving via this title expecting an explainability piece will be
  confused for the first several paragraphs, and a reader who skips the
  article based on the title (assuming "another XAI piece") is a real
  loss. This must be fixed.
- **"AI decision" — too broad?** Real risk, consistent with
  `reviewer-report.md`'s AI-specificity finding: the mechanism tested is
  substrate-independent (the "model" in the testbed is a fixed linear
  function). "AI decision" implies the finding is specifically about AI
  systems' behavior, when the more honest framing is "a decision made by
  any versioned, automated system, illustrated in an AI-shaped testbed."
- **Does the article reconstruct decision context rather than explain
  model behavior?** Yes, exactly — this is the clearest, most precise way
  to state what the title should actually promise, and it is not what
  "explain... decision" currently promises.
- **Is the title clickier than the evidence permits?** Mildly. Not
  dishonest, but "AI Decision" borrows more urgency from the current AI
  discourse than the substrate-independent finding underneath it
  justifies. A title that would work equally well with "AI" struck out
  entirely is a useful test — the current title fails that test; several
  alternatives below pass it.

## Alternatives (ranked)

| Rank | Title | Type | Why |
|---|---|---|---|
| 1 | **"Retained Is Not Consumed: Why Version History Doesn't Guarantee Decision Reconstruction"** | Precise technical | Uses the article's own strongest, already-approved technical phrase (`../../drafting-readiness/thesis-and-titles.md`) as the lead, avoids "explain" entirely, avoids "AI" entirely (honest about substrate-independence), states the actual finding precisely. Best default choice for a technical/practitioner venue. |
| 2 | **"Your Audit Trail Has Every Version. It Still Can't Tell You Which One Was Used."** | Strong practitioner | Concrete, addresses a practitioner's own system directly ("your"), avoids "explain"/XAI confusion, avoids "AI decision" overclaim by naming "audit trail" instead, states the paradox in the reader's own vocabulary. Strong hook, no accuracy risk identified. |
| 3 | **"Why Versioning Isn't Enough to Reconstruct a Decision"** | O'Reilly-style | Short, punchy, matches Article 1's own title register ("Model Outputs Are Not Decisions"), replaces "explain" with "reconstruct" (accurate to the actual claim), drops "AI" (can be reintroduced in a subtitle/dek if the venue wants AI-specific framing, e.g., "...in AI-mediated systems" as a subordinate clause rather than the main claim). |
| 4 | **"Preserving Consumed Context: An Empirical Study of Decision Reconstruction Under Version Drift"** | Conservative research | Most hedged option; names the actual technical object (consumed context), frames the piece honestly as an empirical study rather than a general lesson, appropriate if the venue is closer to a workshop-paper register than a practitioner blog. |
| 5 | "Why Keeping Every Version Still Isn't Enough to Reconstruct an Automated Decision" | Minimal edit of current title | Fixes both flagged risks with the smallest possible change from the current title (swap "explain"→"reconstruct", "AI"→"automated") — useful if editorial preference is to preserve as much of the current title's cadence as possible rather than replace it outright. |
| 6 | "Everything Was Versioned. Nobody Could Say Why It Happened." | Provocative / narrative | Strong hook, present-tense drama; risk: "why it happened" edges back toward explainability-adjacent language and is slightly less precise than options 1–3 about what's actually being claimed (reconstruction of *context*, not causal explanation of *behavior*). Usable if the venue wants maximum narrative pull and a precise dek immediately underneath to disambiguate. |
| 7 | "The Reconstruction Gap: What Version History Doesn't Tell You" | Generic conceptual | Serviceable but the least distinctive of the set — "the X gap" is an overused essay-title pattern, and it drops the concrete "decision" framing entirely, weakening the hook. Lowest-ranked; include only for completeness. |

## Recommendation

**Primary recommendation: Rank 1** ("Retained Is Not Consumed: Why
Version History Doesn't Guarantee Decision Reconstruction") as the
working/technical title, with **Rank 2** ("Your Audit Trail Has Every
Version...") as the practitioner-venue alternative if a punchier hook is
wanted. Both independently resolve every risk identified in the attack
above. **Do not carry the current title forward unmodified** — the
"explain an AI decision" phrasing is the review's clearest, lowest-risk-
to-fix, highest-value title-level correction.

This section does **not** rename `../draft-v1.md`, per the authorizing
brief's explicit instruction. The recommendation is recorded here for
`revision-plan-v2.md` and human decision.
