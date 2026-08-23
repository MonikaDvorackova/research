---
id: note-contribution-02-drafting-thesis-and-titles
title: "Contribution 2 Drafting Readiness — Does 'State Is Not Knowledge' Survive, and Titles"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, titles, thesis]
refs: [non-obvious-result.md, ../prior-art-audit.md, ../novelty-verdict.md]
---

## Does "State Is Not Knowledge" Survive?

**No — confirmed, not merely carried over.** This was already decided
before either experiment ran (`../prior-art-audit.md` Task 2: the
dichotomy is imprecise because several things Source A implicitly treats
as "mere state" — logs, traces, provenance graphs, attestations — are
already historical, append-only records, not snapshots) and
`../novelty-verdict.md`'s original post-audit thesis already replaced it
with a binding-centric formulation. The two experiments narrow that
formulation further (to a causal-relation formulation) but do not revive
"knowledge" as a term — nothing in either experiment's results depends on
or supports the word.

Testing the specific alternatives the review requires:

- **"Is it technically precise?"** No. "Knowledge" is not a property
  either experiment measured; both measured whether a specific relation
  (decision → consumed version) was recoverable, a narrower and checkable
  claim.
- **"Is 'knowledge' too philosophical?"** Yes, and it also collides with
  Contribution 3's reserved vocabulary (`../deferred-contribution-03.md`
  already flags this collision risk explicitly).
- **"Does it overreach the empirical result?"** Yes — "knowledge" implies
  a general epistemic property; the experiments measured two specific,
  named mechanisms, not knowledge in general.
- **"State Is Not Context"?** Better than "knowledge," but "context" is
  ambiguous with `../problem-formalization.md`'s own sub-problem F
  ("context reconstruction," the deliberately bounded residual category)
  — using "context" in the title risks a reader conflating the title's
  claim with the F sub-problem specifically, when the actual claim spans
  C/D/E. Rejected for collision risk.
- **"Version History Is Not Decision History"?** Directionally right and
  memorable, but imprecise: the experiments never showed "decision
  history" (the log of decisions) was itself deficient — Regime
  B/C both always answer Q1 (what decision occurred) correctly. The
  deficiency is specifically about *which versions* a decision used, not
  about the decision record itself. Close, but not the sharpest available
  phrase.
- **"Preserving State Is Not Preserving Decisions"?** Same imprecision as
  above — decisions themselves are not what goes unpreserved.
- **"The Missing Link in Historical AI Decisions"?** Thematically exact
  (a causal *link* is precisely what both experiments show is missing)
  but reads as a headline, not a technical thesis statement — better
  suited to the practitioner/provocative title than the technical one.

## Recommended titles

**Technical working title:**

> **"Retained Is Not Consumed: A Measured Causal Gap in AI Decision
> Reconstruction"**

Why: "retained" and "consumed" are exactly the two properties the
experiments distinguish (`non-obvious-result.md`'s formulation C) — a
version being *retained* somewhere in history is not the same as a
decision having *consumed* a specific, identifiable one of those
versions. It preserves the rhythm and memorability of "State Is Not
Knowledge" without inheriting its imprecision, and "measured" signals
this is now an empirical claim, not a purely conceptual one.

**Publication / practitioner title:**

> **"Why Keeping Every Version Still Isn't Enough to Explain an AI
> Decision"**

Why: states the non-obvious result (`non-obvious-result.md`'s Formulation
B) directly, in plain language, with no jargon and no unearned claim
about AI systems in general — "isn't enough" is precise (not "is
impossible"), matching the claim ledger's requirement that no absolute
quantifier appear unqualified.

**Optional provocative title:**

> **"Your System Remembers Everything. It Still Can't Tell You Why."**

Why: provocative without overclaiming — "your system" is addressed to a
practitioner reader about their own system, not a claim about "all AI
systems"; "remembers everything" is the reader's own assumption being
challenged, not an assertion the article makes about the world; "can't
tell you why" is exactly sub-problem G, the article's actual target.
Should be used only where the venue's register tolerates a rhetorical
title, with the technical working title as the actual paper/section
title underneath it.

**Not recommended, and why:** any title using "knowledge" (imprecise,
Contribution-3-colliding), "understanding" (same collision, reserved for
Contribution 3 by `../deferred-contribution-03.md`), or "binding" alone
without qualification (narrowed away by F10-6 — a title built around
"binding" would misrepresent the surviving thesis before the reader even
reaches the abstract).
