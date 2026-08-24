---
id: note-contribution-02-article-review-revision-plan
title: "Contribution 2 Article — Revision Plan for draft-v2"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, revision-plan]
refs: [reviewer-report.md, section-review.md, claim-review.md, title-review.md]
---

## Revision Plan — Implementation-Ready

This is a plan, not a hidden draft-v2 — no replacement paragraphs are
provided except tiny disambiguation examples explicitly marked as such,
per the authorizing brief. Priorities: P0 (correctness / unsupported
claim) > P1 (argument / prior-art defense) > P2 (clarity / structure) >
P3 (polish).

---

### P0-1 — The transaction-time query nuance (the review's central finding)

- **Location:** "Experiment 1: When History Changes After the Decision,"
  final paragraph; "This Is Not a New Provenance System," bitemporal
  databases paragraph; "What the Experiments Do — and Do Not — Show,"
  closing summary sentence.
- **Current problem:** the draft states or implies that no query against
  Regime B's retained data can avoid the retroactive-correction failure
  ("No amount of additional bitemporal completeness fixes this"; "solve
  it completely — for exactly the cases without retroactive correction").
  Independent inspection of `experiment/src/reconstruction.py` shows
  Regime B's query uses "as of the latest known transaction state"
  semantics (unbounded by t0), not "as of transaction time t0" semantics
  — a standard `SYSTEM_TIME AS OF t0` bitemporal query, using only data
  Regime B already retains and t0 (already known from every regime's own
  outcome log), would return the pre-correction value and avoid the
  failure entirely.
- **Required change:** add 2–4 sentences to Experiment 1's final
  paragraph explaining that a transaction-time-anchored query *can* avoid
  this specific failure using Regime B's own data, and that the
  meaningful, defensible distinction is narrower than "Regime B fails":
  Regime C removes the need for the investigator to know, in advance, to
  anchor the transaction-time cutoff to decision time rather than query
  time — a non-default choice ordinary "as of" bitemporal usage does not
  make automatically. Correspondingly soften "No amount of... fixes this"
  to something like (illustrative only, not prescriptive prose): *"A
  naive 'as of now' bitemporal query — the default most tooling
  performs — does not fix this; a query deliberately anchored to
  decision time can, using the same retained data, but requires the
  investigator to know to do that in advance, which is exactly the
  burden Regime C's explicit binding removes."* Apply the parallel fix to
  the bitemporal-databases paragraph in "Not a New Provenance System" and
  the "competently implemented" phrase in the closing summary (see
  claim-review.md claim 25).
- **Reason:** `reviewer-report.md`'s headline finding; `claim-review.md`
  claims 5, 7, 19, 25.
- **Evidence/source:** direct inspection of
  `experiment/src/reconstruction.py::_as_of_valid_time_latest_transaction`
  (line-level: `row.recorded_at > current.recorded_at`, unbounded by
  t0); confirmed absent from the follow-up experiment's code (no
  `recorded_at` field exists there at all), so this fix does not touch
  Experiment 2 or the negative control.
- **Expected effect:** the primary experiment's claim becomes narrower
  and more defensible (about default/naive query practice specifically,
  not about bitemporal completeness as a category) without removing the
  result — Regime B's algorithm, as actually implemented and tested, did
  produce the reported numbers, and reporting that remains valid; only
  the causal interpretation drawn from it changes.
- **Before external citation is added supporting the `SYSTEM_TIME AS OF
  t0` claim itself:** see `citation-plan.md`'s flagged
  EXTERNAL VERIFICATION REQUIRED item.

### P0-2 — Same-root correction in "What the Experiments Do — and Do Not — Show"

- **Location:** closing summary sentence of that section.
- **Current problem:** "complete version history, competently
  implemented, is not sufficient for two independently demonstrated
  reasons" — "competently implemented" is not qualified in a way that
  survives P0-1.
- **Required change:** add a sixth bullet to the existing list,
  cross-referencing the P0-1 fix: something in the register of "the
  retroactive-correction result specifically reflects the behavior of an
  as-of-now bitemporal query, not a proof that no query against
  Regime B's data could succeed — see the qualification in Experiment
  1's section."
- **Reason:** `section-review.md`'s aggregate table; keeps the
  limitations section internally consistent with the P0-1 fix rather
  than silently contradicting it.
- **Evidence/source:** same as P0-1.
- **Expected effect:** limitations section remains the article's most
  reliable section (per `reviewer-report.md`) and stays that way after
  P0-1 is applied elsewhere.

---

### P1-1 — Title change

- **Location:** article title.
- **Current problem:** "Explain an AI Decision" risks XAI/explainability
  confusion; "AI Decision" overstates AI-specificity relative to the
  substrate-independent finding.
- **Required change:** adopt `title-review.md`'s Rank 1 or Rank 2
  recommendation (human choice between them; both resolve the identified
  risks).
- **Reason:** `title-review.md`, `reviewer-report.md`'s AI-specificity
  section.
- **Evidence/source:** substitution test (swap "AI-mediated decision" for
  "deployment configuration decision" — argument unchanged) in
  `reviewer-report.md`.
- **Expected effect:** title accurately signals content; removes the
  single biggest reader-expectation mismatch risk.

### P1-2 — "Causal" terminology audit

- **Location:** all nine occurrences of "causal" in the article body.
- **Current problem:** risk of misreading as statistical/philosophical
  causal inference rather than "consumption reference."
- **Required change:** replace at minimum the first, definitional
  occurrence (in "What a Historical Decision Actually Depends On") with
  "consumption relation" or equivalent; review remaining occurrences
  case by case — retain "causal" only where idiomatic and low-risk (e.g.,
  "causal trail" in the closing line).
- **Reason:** `reviewer-report.md`'s terminology attack.
- **Evidence/source:** `../../drafting-readiness/terminology.md`'s own
  flagged collision risk for "causal linkage/relation."
- **Expected effect:** reduces risk of a statistically sophisticated
  reader (Reviewer A's persona) misreading the central term.

### P1-3 — Pre-empt the referential-integrity objection

- **Location:** "What a Historical Decision Actually Depends On."
- **Current problem:** a reader familiar with database referential
  integrity will draw an unaddressed comparison.
- **Required change:** add one sentence distinguishing the property from
  referential integrity (a reference resolving to *something* vs. a
  reference resolving to the *historically correct* thing).
- **Reason:** `reviewer-report.md` Objection 5.
- **Evidence/source:** none needed beyond the logical distinction itself.
- **Expected effect:** closes an anticipatable objection before a
  sophisticated reader raises it.

### P1-4 — Concede the "not a new intuition" point

- **Location:** "This Is Not a New Provenance System" or the opening.
- **Current problem:** the article implicitly, but never explicitly,
  concedes that "retained ≠ consumed" is an intuition many engineers
  already hold informally.
- **Required change:** one sentence conceding this and stating the
  contribution is measuring/demonstrating it with named failure modes and
  a negative control, not discovering it.
- **Reason:** `reviewer-report.md` Objection 6; matches
  `../../drafting-readiness/novelty-review.md` Objection 10's own
  concession, which draft-v1 does not currently carry forward.
- **Evidence/source:** `../../drafting-readiness/novelty-review.md`.
- **Expected effect:** pre-empts Reviewer C's "is this obvious"
  objection directly rather than leaving it to the experiments alone.

---

### P2-1 — Opening concreteness

- **Location:** opening paragraphs 1–4.
- **Current problem:** the dependency list ("a specific model version, a
  specific policy...") reads as a list, not a scene.
- **Required change:** add one illustrative concrete value (e.g., a named
  policy version or threshold number) to the opening scenario.
- **Reason:** `reviewer-report.md` opening review.
- **Evidence/source:** contrast with Article 1's opening (`accuracy:
  0.913`), cited as a positive style precedent.
- **Expected effect:** stronger, more memorable hook.

### P2-2 — Trim the transition sentence

- **Location:** end of "Version History Is Not Decision History."
- **Current problem:** "That distinction sounds abstract until it's made
  concrete..." is a pure transition, no content.
- **Required change:** cut, or merge into the next section's opening
  clause.
- **Reason:** `section-review.md`.
- **Expected effect:** tightens without losing content — supports the
  authorizing brief's "target v2 tighter than v1" instruction.

### P2-3 — Strengthen the tracing example

- **Location:** "This Is Not a New Provenance System," tracing/logs/
  lineage paragraph.
- **Required change:** optional one-sentence concrete example (a trace
  attribute storing a raw value vs. a version ID).
- **Reason:** `reviewer-report.md` Objection 4.
- **Expected effect:** minor strengthening, not required for correctness.

---

### P3 — Polish (preventive, not corrective)

- Cut "consequential" in the opening (marginal, non-load-bearing).
- If any future revision adds language like "N cases tested" or "across
  dozens of scenarios," it must not imply statistical sampling — the
  current draft already avoids this; this is a constraint to preserve,
  not a current defect.
- Consider whether "decision-context identifiability" (introduced once,
  never reused) earns its place, or whether cutting the term and keeping
  only the prose definition simplifies the article without loss. Human
  editorial judgment, not a required fix.
- Consider whether "The Property to Design For" and "What a Historical
  Decision Actually Depends On" should merge; recommend against, but flag
  for editorial judgment per `section-review.md`.

---

## What must NOT change

- Experiment 2's section and the negative-control section require **no
  changes** — both survive independent adversarial review unmodified
  (`reviewer-report.md`). Do not "fix" what isn't broken while making the
  P0 changes elsewhere.
- No experimental result, case definition, or raw data file may be
  touched by any v2 revision — every P0/P1 item above is a **framing and
  interpretation** correction, never a request to rerun or alter
  anything under `experiment/`.
- Word count: current draft is 2,723 words; the P0/P1 additions above
  are estimated at roughly 150–250 words net (a few additions, offset by
  the P2-2 cut and other trims), keeping v2 within the 2,500–3,500 target
  without padding.
