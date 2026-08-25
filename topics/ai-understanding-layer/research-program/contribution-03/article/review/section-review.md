---
id: note-contribution-03-article-section-review
title: "Contribution 3 Article draft-v1 — Section-by-Section Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, sections]
refs: [../draft-v1.md, reviewer-report.md]
---

Aggressive pass. A 3,257-word article built on a structurally simple
central mechanism (§4/§5 of `reviewer-report.md`) should compress, not
merely be polished.

## "Every Decision Is Reconstructable. The System Still Isn't." (opening)

- **Purpose:** state the paradox concretely before any abstraction.
- **Strength:** genuinely effective — the D1→D2→D3→D4 walkthrough is
  the article's best piece of writing and does real work making the
  distinction legible before it's named.
- **Weakness:** "The System Still Isn't" (both here and in the title)
  overclaims scope — the experiment measures trajectory-level
  dependency-edge identifiability, not any broader notion of "system"
  (state, deployment, configuration). See `title-review.md`.
- **Prior-art vulnerability:** none directly — this is scene-setting.
- **Empirical vulnerability:** none — no numbers claimed yet.
- **Redundancy:** none.
- **KEEP / REVISE / CUT / MERGE: REVISE** — keep the walkthrough, retitle
  the heading away from "System."

## "Local Reconstruction Is Not Trajectory Reconstruction"

- **Purpose:** define the two questions being conflated.
- **Strength:** the timestamp-vs-dependency distinction (line 23) is a
  genuinely useful, non-obvious clarification worth keeping intact.
- **Weakness:** none major.
- **Prior-art vulnerability:** low.
- **Empirical vulnerability:** none, purely definitional.
- **Redundancy:** low overlap with "What Has to Compose" below —
  consider merging the two definitional sections into one.
- **KEEP / REVISE / CUT / MERGE: MERGE** with "What Has to Compose."

## "What Has to Compose"

- **Purpose:** state Contribution 2's premise and formalize the
  composition question.
- **Strength:** correctly scoped summary of Contribution 2 (two
  sentences, not a re-argument) — satisfies the Article 2 boundary
  requirement cleanly.
- **Weakness:** houses the ∀i identifiable(C(di)) ⇏ identifiable(E)
  formalization, found in `reviewer-report.md` §17 to be close to
  tautological and possibly worth cutting.
- **Prior-art vulnerability:** the composition framing invites
  Objection 1 (triviality) without naming or answering it.
- **Empirical vulnerability:** none directly.
- **Redundancy:** with the prior section, per above.
- **KEEP / REVISE / CUT / MERGE: REVISE** — merge with the prior
  section; cut or relabel the formalization; add an explicit sentence
  naming and provisionally answering Objection 1.

## "The Experiment"

- **Purpose:** describe T1/T2 and the six cases.
- **Strength:** the local-equivalence enforcement claim ("that check
  re-runs automatically before every execution... it never failed," line
  49) is a real, verifiable methodological strength and should stay
  prominent.
- **Weakness:** does not disclose that `DecisionRecordT1` structurally
  lacks any field for E (Objection 6) — the paragraph describing T1
  (line 45) says "no field... stores any relation... structurally not
  there" but frames this as a regime design choice without acknowledging
  it also guarantees the headline result.
- **Prior-art vulnerability:** moderate — a reader familiar with
  provenance formalisms will recognize T1/T2 as PROV's own
  entity-attributes-vs-derivation-edges split before the article says so
  three sections later; earlier signposting would pre-empt rather than
  invite the objection.
- **Empirical vulnerability:** does not disclose the construct-validity
  gap (`reviewer-report.md` §5 — root decisions never scored for
  false-edge invention).
- **Redundancy:** low.
- **KEEP / REVISE / CUT / MERGE: REVISE** — add the Objection 6
  disclosure and the construct-validity caveat.

## "Perfect Local Records, Ambiguous Global History"

- **Purpose:** report the headline TI numbers.
- **Strength:** numbers are accurate and traceable (see
  `empirical-traceability.md`).
- **Weakness:** this is the section title doing the most overclaiming in
  the piece — "Ambiguous Global History" reads as a discovery, when per
  Objection 6 the *direction* of this result was guaranteed at design
  time. The section does not distinguish "this had to happen given the
  schema" from "this is what we measured."
- **Prior-art vulnerability:** high, exactly here — this is where a
  systems-theory reviewer will first object "well, of course."
- **Empirical vulnerability:** the 0.33/1.00 contrast is correct but
  under-qualified as a "finding."
- **Redundancy:** none.
- **KEEP / REVISE / CUT / MERGE: REVISE, substantially** — shrink this
  section's rhetorical weight; move the "this is a manipulation check,
  not a surprise" concession here, immediately before the real finding
  in the next section.

## "Ambiguous Is Better Than Wrong"

- **Purpose:** report DEA=1.00/FGC=0.00, the honest-ambiguity finding.
- **Strength:** this is, per `reviewer-report.md` §2/§4, **the strongest
  material in the article** — genuinely non-guaranteed, well-explained,
  well-traced.
- **Weakness:** under-weighted relative to the previous section; does
  not use the three-way taxonomy from `reviewer-report.md` §6
  (ambiguous record vs. weak algorithm vs. false confidence) explicitly.
- **Prior-art vulnerability:** low — this is the article's least
  prior-art-vulnerable material.
- **Empirical vulnerability:** low, well-traced.
- **Redundancy:** none.
- **KEEP / REVISE / CUT / MERGE: KEEP, and promote** — this should
  arguably be the article's headline result, not its second act. Add the
  three-way taxonomy.

## "The Relation That Resolves the Ambiguity" (negative control)

- **Purpose:** present C3-6, rule out "new architecture required."
- **Strength:** correctly central per the authorizing task's own
  instruction; well-argued.
- **Weakness:** none major.
- **Prior-art vulnerability:** low — this section itself pre-empts
  overclaiming rather than inviting attack.
- **Empirical vulnerability:** none, numbers check out.
- **Redundancy:** overlaps partly with "This Is Not a New Provenance
  System" (both argue "no new mechanism needed") — could be tightened
  into one continuous argument.
- **KEEP / REVISE / CUT / MERGE: KEEP**, consider tightening the
  transition into the next section.

## "This Is Not a New Provenance System"

- **Purpose:** address the strongest prior-art objection directly.
- **Strength:** the direct, named-objection format ("isn't this just
  workflow provenance?") is exactly right and should be the model for
  how Objections 1, 5, and 6 are handled elsewhere (currently they are
  not named at all).
- **Weakness:** citation base incomplete — Buneman/why-provenance (ICDT
  2001) not cited despite being the programme's own strongest-identified
  provenance source; Dapper (Sigelman et al. 2010, already verified as
  S4 in `../../source-ledger.md`) not cited despite being the
  foundational tracing paper behind the OpenTelemetry citation used
  instead. See `prior-art-review.md`.
- **Prior-art vulnerability:** this section is the article's defense
  against prior-art attack, not a vulnerability itself, apart from the
  citation gap above.
- **Empirical vulnerability:** none.
- **Redundancy:** with the negative-control section, as above.
- **KEEP / REVISE / CUT / MERGE: REVISE** — add the two missing
  citations; otherwise keep intact, this is the article's strongest
  section for honesty.

## "What to Preserve Across Decisions" (engineering takeaway)

- **Purpose:** give a concrete, practitioner-facing design question.
- **Strength:** genuinely actionable, correctly declines to prescribe
  one schema.
- **Weakness:** none major.
- **Prior-art vulnerability:** low.
- **Empirical vulnerability:** none, this is prescriptive, not
  empirical.
- **Redundancy:** low.
- **KEEP / REVISE / CUT / MERGE: KEEP.**

## "What the Experiment Does Not Show" (limitations)

- **Purpose:** disclose scope limits.
- **Strength:** thorough — sample-size discipline, mechanism-count
  limits, dependency-definition specificity, and the human-understanding
  disclaimer are all present and accurate.
- **Weakness:** does **not** include the Objection 6 disclosure (the
  guaranteed-by-construction nature of the headline result) or the
  construct-validity gap (root decisions never scored) — both belong
  here and are currently absent from the entire article.
- **Prior-art vulnerability:** none, this section only concedes.
- **Empirical vulnerability:** the section this review would most expect
  to catch Objection 6 and the construct-validity gap, and doesn't.
- **Redundancy:** none.
- **KEEP / REVISE / CUT / MERGE: REVISE** — add both missing
  disclosures; this is the natural home for them.

## "The Composition Question" (closing)

- **Purpose:** restate the thesis without embellishment.
- **Strength:** correctly hedged ("not necessarily," line 107); the
  AI-generality admission (line 109) is honest and creditable.
- **Weakness:** restates P3/P4 as the headline one more time rather than
  leading with P5, compounding the over-weighting problem identified
  above.
- **Prior-art vulnerability:** low, this section is mostly summary.
- **Empirical vulnerability:** none new.
- **Redundancy:** significant overlap with "Perfect Local Records,
  Ambiguous Global History" — two sections making substantially the same
  claim.
- **KEEP / REVISE / CUT / MERGE: REVISE** — rebalance toward P5 in the
  closing paragraph, per `reviewer-report.md` §2's proposition ledger.

## Net compression assessment

Given the central mechanism is structurally simple (§4/§5 of
`reviewer-report.md`), and at least two clear merge opportunities exist
("Local Reconstruction Is Not Trajectory Reconstruction" + "What Has to
Compose"; the redundant restatement between "Perfect Local Records..."
and "The Composition Question"), a v2 built around this review's
findings should target roughly **1,800–2,400 words**, not 2,500–3,300 —
see `revision-plan-v2.md` for the specific target and rationale.
