---
id: note-oreilly-article-title-review
title: "O'Reilly Article draft-v1 — Title Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, article, review, title]
refs: [../draft-v1.md, claim-review.md]
---

## Current title

**"What Your AI Audit Trail Is Missing: The Relations, Not the Records"**

Dek: *"Why approving an AI decision and explaining it later are two
different engineering problems."*

## Attack

- **Is "audit trail" the right object?** Partially — the article is
  about decision records specifically, not audit trails generally (audit
  trails can include model-level and infrastructure-level artifacts the
  article explicitly says are out of scope, e.g., model cards,
  evaluation reports as such). "Audit trail" is close enough to be
  recognizable but slightly broader than what the article actually
  addresses.
- **Does "missing" imply empirical prevalence evidence?** Yes, and this
  is a real problem — "what your... audit trail **is** missing" reads as
  a diagnosis of the reader's actual system, which implies the article
  has evidence about what audit trails typically lack. No prevalence
  evidence exists in this research programme (matching the "most ML
  pipelines" finding in `claim-review.md`). The title makes the same
  category of claim the body text is being asked to remove.
- **Does "the relations, not the records" falsely imply records don't
  matter?** **Yes — this is a genuine false dichotomy, confirmed on
  inspection (Section 17 of the review task).** A consumption relation,
  once captured, *is itself a record* — a row, a field, a log entry. The
  article's actual distinction (Section 4) is between records of what
  *existed* (artifacts) and records of what was *used* (relations) — not
  between relations and records as separate categories. "Records" and
  "relations" are not opposed in the article's own argument; the title's
  dichotomy misstates the article's own technical content. **This
  requires a title change even independent of whether the article body
  survives.**
- **Is "AI" necessary?** Marginally — the article's own Section 6
  concedes the underlying principle isn't AI-specific, but "AI" earns
  its place in the title as the article's stated domain of application,
  consistent with `OREILLY-FINAL-BRIEF.md`'s AI-specificity guidance.
  Not a problem on its own.
- **Does the title cover authorization as well as reconstruction?** No —
  "audit trail" and "relations vs. records" both point toward the
  reconstruction half only (Section 4/5/7); nothing in the title signals
  Section 3's authorization material, even though the article spends
  roughly a third of its length there and Section 3 is where the
  synthesis moment (`reviewer-report.md` §13) actually begins. This is
  the title's second structural problem, independent of the false
  dichotomy above.

**Verdict: the current title has two independent problems** — a false
technical dichotomy ("relations, not records") and a coverage gap (it
represents only the reconstruction half of a two-part article) — plus a
milder prevalence-implication risk from "missing." **Retitle
recommended**, even though the article body itself survives review.

## Eight candidates (required set, improved)

Required candidates from the review task, tested and improved, plus
additional coverage:

1. **"Building AI Systems That Can Be Authorized Now and Reconstructed
   Later"** *(required candidate, improved: "Explained" → "Reconstructed"
   per the terminology verdict below)* — directly covers both halves,
   active voice, no false dichotomy, uses the article's own precise term
   rather than the XAI-risky one.
2. **"The Decision, Not Only the Model"** *(required candidate, as
   given)* — carries the qualifier already built in; strong technical
   framing but covers only Section 2's premise, not the authorization/
   reconstruction duality that is the article's actual payload.
3. **"Approved Doesn't Reconstructable" → "Approved Doesn't Mean
   Reconstructable"** *(required candidate, corrected grammar,
   "Explainable" → "Reconstructable")* — punchy, accurate, avoids XAI
   confusion entirely; slightly less descriptive of *what* the article
   covers (relations, checklist) than titles 1 or 4.
4. **"The Record That Authorized It May Not Reconstruct It"** *(required
   candidate, as given — "Explain" already reads as "Reconstruct" here,
   no change needed)* — vivid, concrete, and correctly frames this as a
   *records* problem (two different records, not "relations vs.
   records"), fixing the false-dichotomy issue directly.
5. *(current title, retained for comparison)* **"What Your AI Audit
   Trail Is Missing: The Relations, Not the Records"** — kept as the
   baseline; see Attack above for why it is not recommended as-is.
6. **"Authorized Now, Reconstructable Later"** — the cleanest possible
   compression of the actual thesis into a title; conservative, precise,
   no false dichotomy, covers both halves explicitly.
7. **"Two Records Every AI Decision Needs — and Most Systems Only
   Keep One"** — vivid, covers both halves via "two records," but
   reintroduces a prevalence claim ("most systems only keep one") this
   review just flagged as unsupported elsewhere in the article; not
   recommended unless paired with real evidence.
8. **"Passing Review Isn't the Same as Being Reconstructable"** —
   plain-language, decision-neutral (works even for a reader who hasn't
   yet absorbed "authorization" as a term), correctly uses
   "reconstructable."

## Ranking

1. **#6 — "Authorized Now, Reconstructable Later"** — most accurate,
   covers both halves, zero false dichotomy, zero prevalence claim,
   uses the article's own precise terminology throughout. Recommended
   primary.
2. **#4 — "The Record That Authorized It May Not Reconstruct It"** —
   nearly as accurate, more vivid/narrative, correctly reframes
   "records" as the shared object (two different records) rather than
   opposing records to relations. Strong runner-up, especially if an
   editor wants more narrative pull than #6's flatter construction.
3. **#1 — "Building AI Systems That Can Be Authorized Now and
   Reconstructed Later"** — accurate and complete but longer; better
   suited as a subtitle/dek than a main title if #6 or #4 is used as the
   headline.
4. **#3 — "Approved Doesn't Mean Reconstructable"** — strong pull-quote
   candidate, pairs well with #6 as a dek.
5. **#8 — "Passing Review Isn't the Same as Being Reconstructable"** —
   solid, plain-language alternative if the editorial voice wants to
   avoid "authorized" as jargon.

**Not recommended:** #2 (covers only one section), #5/current (false
dichotomy + coverage gap, see Attack), #7 (reintroduces an unsupported
prevalence claim).

## Recommended dek pairing

If title #6 is adopted: *"Authorization and reconstruction are separate
engineering properties for a production AI decision — and most systems
are built to guarantee only one of them."* — **flagged**: this dek
itself contains "most systems," the same unsupported-prevalence pattern
found elsewhere in the article (`claim-review.md`). Recommended
dek instead: *"Passing review and being reconstructable later are
separate engineering properties — and neither follows automatically
from the other."* — accurate, no prevalence claim, mirrors the article's
own correctly-hedged closing line.
