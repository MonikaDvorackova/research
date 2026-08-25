---
id: note-contribution-03-article-2-integration-candidates
title: "Contribution 3 — Article 2 Integration Candidates"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article-2, integration-candidates]
refs: [FINAL-EDITORIAL-DISPOSITION.md, ../contribution-02/article/draft-v2.md, article/review/revision-plan-v2.md]
---

Identification only. **Article 2's frozen `draft-v2.md` is not modified
by this document or by this editorial pass.** Any merge remains a
separate, future, explicitly authorized action.

## Candidate 1 — The honest-ambiguity-vs-false-confidence distinction, generalized one level up

**Where it would fit:** Article 2 already distinguishes AMBIGUOUS
(honest non-answer) from a wrong answer for single-decision
reconstruction. Contribution 3 confirms the same distinction holds at
the trajectory level (Dependency Edge Accuracy = 1.00, False Global
Confidence = 0.00 across all cases). A one-sentence footnote or closing-
paragraph addition to Article 2's "The Question to Ask" section could
note that this principle is not decision-specific.

**Required or optional:** OPTIONAL. Article 2's own claim already stands
without it — Contribution 3 confirms rather than completes it.

**Risk of bloating Article 2:** Low if kept to one sentence; moderate if
expanded to explain the T1/T2 experiment, which would require
introducing new vocabulary (trajectory, dependency edge) Article 2
currently has no need for.

**Risk of weakening Article 2's accepted thesis:** Low — this is
confirmatory, not contradictory. The only risk is diluting Article 2's
tight, already-accepted scope (`FINAL-ACCEPTANCE.md`: "ARTICLE COMPLETE")
by reopening a frozen, ACCEPT-verdict document for a non-essential
addition.

## Candidate 2 — "Preserve cross-decision relations, not just per-decision context"

**Where it would fit:** Article 2's own engineering takeaway ("the
system must preserve enough relation/context to identify the consumed
state") already implies this at the single-decision level. A trajectory-
level extension could sit in the same section as one additional
sentence.

**Required or optional:** OPTIONAL. Per `FINAL-EDITORIAL-DISPOSITION.md`
Reason 4, this is close enough to Article 2's existing takeaway that it
adds marginal value.

**Risk of bloating Article 2:** Moderate — this is the candidate most
likely to require new setup (defining "trajectory," "cross-decision
relation") to land cleanly, which works against Article 2's current
economy of scope.

**Risk of weakening Article 2's thesis:** Low, same reasoning as
Candidate 1.

## Candidate 3 — The negative-control finding ("ordinary relations already fix this")

**Where it would fit:** Could reinforce Article 2's own "not a new
architecture" framing (`FINAL-ACCEPTANCE.md`'s explicit non-claim list)
with a second, independent confirmation at a different scope.

**Required or optional:** OPTIONAL, and lower priority than Candidates 1
and 2 — it reinforces a point Article 2 already makes about itself
without adding new information for Article 2's own reader.

**Risk of bloating Article 2:** Moderate-high — explaining why the
negative control is decisive requires importing case-matrix detail from
a different experiment, which is exactly the "detailed... case
numbering, metric tables" material `FINAL-ACCEPTANCE.md`'s own "Later
O'Reilly synthesis" note already says Article 2 should **not** force
itself to reproduce.

**Risk of weakening Article 2's thesis:** Low.

## Candidate 4 — The full T1/T2 experimental apparatus, cases, or metrics

**Required or optional:** NOT RECOMMENDED for Article 2 at all, at any
priority. This is Contribution 3's own experiment, belongs to the
research note, and would substantially exceed Article 2's scope and
length discipline (2,400–3,000 words, already achieved and frozen).

## Recommendation

**KEEP SEPARATE for now; USE ONLY IN O'REILLY when synthesis drafting is
authorized.**

None of Candidates 1–3 are required — Article 2 stands complete and
ACCEPTED without them (`FINAL-ACCEPTANCE.md`). All three are better
suited to a future O'Reilly synthesis chapter, where the "level-up"
narrative (decision → trajectory) can be told once, cleanly, across both
contributions, rather than retrofitted into a frozen, already-accepted
article as piecemeal additions. Reopening a document with a "ZERO
blocking issues: DO NOT modify" acceptance verdict for optional,
non-essential material carries process risk (per this program's own git-
safety and append-only discipline) disproportionate to the marginal
value gained. If a future editorial pass decides Article 2 should be
revised for other reasons, Candidates 1 and 2 (in that priority order)
are the only ones worth reconsidering at that time.
