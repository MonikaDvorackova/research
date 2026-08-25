---
id: note-contribution-03-article-reviewer-report
title: "Contribution 3 Article draft-v1 — Adversarial Reviewer Report"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, adversarial]
refs: [../draft-v1.md, ../../experiment/RESULT.md, ../../composition-review.md]
---

Review-only. `draft-v1.md` not modified. All findings independently
re-derived against `draft-v1.md`, `../../experiment/src/domain.py`,
`../../experiment/src/scoring.py`, `../../experiment/results/*`, and
`../../*.md`, not accepted from `draft-v1-audit.md`'s own self-audit.

## 1. Four reviewer postures

### Reviewer A — distributed systems / provenance expert

**Verdict: article survives, barely, and only because it concedes the
attack rather than contesting it.** "This is just workflow provenance"
is correct as far as it goes — draft-v1 itself says so in Section 8
("This Is Not a New Provenance System," line 83: "The honest answer is
yes, largely"). But the concession is incomplete: the article's citation
base for this collision is W3C PROV [1] plus generic OpenTelemetry [2]
and Fowler [3] — it does not cite the actual database-provenance
literature (Buneman, Khanna, Tan, "Why and Where: A Characterization of
Data Provenance," ICDT 2001) that this programme's own
`../../provenance-review.md` identifies as predating and formally
sharpening exactly the same why/where distinction, twelve years before
PROV. Citing only the newer, more general standard while omitting the
older, more precise formalization this programme already surfaced is a
prior-art-fairness gap, not just an incompleteness. See §9 below.

### Reviewer B — formal methods / systems theory reviewer

**Verdict: the central claim is close to true by construction, and the
article does not disclose this.** `experiment/src/domain.py` defines
`DecisionRecordT1` with **no field capable of encoding a cross-decision
relation at all** (confirmed directly, lines 43–55) and
`DecisionRecordT2` with exactly one such field, authored from ground
truth (lines 58–73). Given that, "T1 cannot always recover the
dependency edge E" is not an empirical discovery so much as a restatement
of the type definition — E was never representable in T1's schema to
begin with. The four failing cases (C3-2/3/4/5) were, by
`case-matrix.md`'s own design notes, deliberately constructed so that no
local fact resolves the ambiguity. This is a legitimate experimental
design (a controlled demonstration is supposed to guarantee its own
mechanism), but the article's prose repeatedly frames the T1 failure as
if it were a finding ("Perfect Local Records, Ambiguous Global History")
rather than a manipulation check. The one genuinely open, non-guaranteed
empirical result is whether T1's *failures* are honest (AMBIGUOUS) or
falsely confident (WRONG_UNIQUE) — nothing in the schema forces that
outcome. See §4, Objection 6, and §17.

### Reviewer C — ML/agent-systems reviewer

**Verdict: honest about not being AI-specific, but leaves real
AI-specific grounding unused.** The article's own closing section states
plainly that "the same composition question applies to any system built
from dependent, individually-auditable steps" (line 109) — a direct,
creditable admission that swapping "AI-mediated trajectory" for
"distributed workflow" leaves the argument intact (confirmed by removal
test, §14). But this programme's own `../../ai-systems-review.md`
already surfaced a concrete, current, AI-specific empirical grounding
for why this gap may matter more in AI-agent tooling than in generic
distributed systems — S13/S23's finding that 2026 AI/agent observability
tooling has "impressive depth at individual layers but limited
integration across them." That finding is a legitimate, non-overclaiming
way to say "here is *why* AI-agent trajectories are a plausible
present-day site for exactly this gap" — and it is not cited or used
anywhere in draft-v1. This is a missed opportunity, not a factual error.

### Reviewer D — skeptical technical editor

**Verdict: does not yet clear the bar for an independent article at this
length.** Article 2 already established the consumption-relation
argument, the honest-ambiguity-vs-false-confidence metric family, the
negative-control pattern, and the "not a new architecture" concession —
all four of Article 3's rhetorical devices are direct reuses of Article
2's own apparatus, one level up. Once the AI framing and the formula are
stripped away (§21), what remains is close to: *"if a system's decision
records don't store which decision fed which, you can't always recover
who-depended-on-whom — but if it does, you can; and a well-built
investigator will at least say so honestly when it can't."* That is a
real point, worth writing down, but it is closer to a tight research
note or a two-paragraph addition to Article 2 than to a free-standing
3,257-word piece. See §15.

## 2. Proposition ledger

| # | Proposition | Type | Notes |
|---|---|---|---|
| P1 | A single decision's consumed context is not automatically reconstructable from retained version history alone (Contribution 2's premise) | EMPIRICAL (already earned elsewhere) | Correctly summarized in two sentences, not re-argued (lines 29). |
| P2 | Decision reconstruction (local) and trajectory reconstruction (global, dependency edges) are distinct questions | DEFINITIONAL | Sound; the article's most durable contribution is stating this distinction cleanly. |
| P3 | ∀i identifiable(C(di)) does not imply identifiable(E) | LOGICAL / near-DEFINITIONAL | **Weakest transition** — see §17. True almost by construction once C(di) is defined not to contain E. |
| P4 | The T1/T2 experiment demonstrates a concrete instance of P3 (LDR=1.00 both regimes; TI=0.33 T1 vs 1.00 T2) | EMPIRICAL, but direction guaranteed by construction | The *magnitude* (4/6, not e.g. 1/6) is a designed number, not a discovered one — see Objection 6. |
| P5 | T1's failures are honest (AMBIGUOUS), never falsely confident (WRONG_UNIQUE): DEA=1.00, FGC=0.00 | EMPIRICAL, genuinely not guaranteed | **The strongest, least-obvious result in the article** — nothing in the schema forces this; a differently built investigator could guess. Under-emphasized relative to P3/P4 in the article's own structure (see §18). |
| P6 | The gap closes completely given one ordinary relation field (negative control, C3-6) | EMPIRICAL, near-definitional | Legitimately narrows the claim; correctly centered by the article. |
| P7 | Workflow provenance, tracing, event sourcing already model this relation | PRIOR-ART SUPPORTED | Correct, but citation base incomplete (missing Buneman; missing Dapper) — see §9. |
| P8 | Therefore no new mechanism is required — only ensuring existing relation-capturing fields are populated | SYNTHESIS | Reasonable, appropriately modest. |
| C | Per-decision reconstructability does not necessarily compose into trajectory-level reconstructability; the fix is preserving cross-decision relations with existing mechanisms | Conclusion | Correctly hedged ("not necessarily," line 107) — see §4 for whether the *hedged* claim is still worth an article. |

**Weakest transition: P2 → P3.** Dressed in formal notation (∀i
identifiable(C(di)) ⇏ identifiable(E)), but the notation encodes a type-
system fact (T1's `DecisionRecordT1` structurally has no field for E)
rather than a result the data could have gone the other way on. See §17
for the recommendation to either cut the formalization or explicitly
label it as restating the design.

## 3. Attack on the central thesis: six objections

### Objection 1 — Triviality: local properties rarely imply global properties without composition conditions

- **Strongest form:** stating "local completeness doesn't imply global
  completeness" for yet another property, after compositional
  verification has already established this for predictability
  (`../../composition-review.md`, citing [S37][S38]), adds nothing by
  itself.
- **Correct?** Yes, as a general principle.
- **Does draft-v1 answer it?** Partially — line 87 concedes "the broader
  caution... is not new either," citing [5]. But the article never names
  this objection directly or explains why *reconstructability
  specifically* (as opposed to predictability, already shown to fail to
  compose) was not a foregone conclusion before the experiment ran.
- **Enough?** No.
- **Threatens publishability?** Yes — this is the core "why does this
  deserve an article" question.
- **v2 must:** name the objection explicitly and make the case that P5
  (honest ambiguity vs. false confidence), not P3/P4, is the part that
  was genuinely open before the experiment ran.

### Objections 2–4 — Workflow provenance / distributed tracing / event sourcing already store the edges

- **Strongest form:** any of the three, correctly instrumented, already
  captures the T2-equivalent relation; T1 is an artificially
  impoverished record no well-built system would ship.
- **Correct?** Yes — confirmed directly by this programme's own
  `../../prior-art-collision-matrix.md` ("W3C PROV / database
  provenance... Dependency relation? Yes, exactly"; "Distributed tracing
  (Dapper-lineage)... Dependency relation? Yes, causal (span graph)").
- **Does draft-v1 answer it?** Yes, directly and honestly (lines 81–89,
  "This Is Not a New Provenance System").
- **Enough?** Yes for honesty. Not enough for publishability on its own
  — leaves open why the piece is worth publishing if the answer to "does
  existing tooling solve this" is simply yes.
- **Threatens publishability?** Moderately — same root issue as
  Objection 1.
- **v2 must:** keep the concession, but pair it with
  `../../provenance-review.md`'s own verdict that provenance theory and
  replay together "cover reconstruction... about as completely as any
  mechanism reviewed in this whole programme — this is not a residual
  gap," and adjust the article's self-positioning from "finding" toward
  "practitioner reminder, quantified."

### Objection 5 — This is merely graph connectivity / provenance completeness

- **Strongest form:** strip the decision vocabulary and this is a DAG
  with unlabeled-edge visibility under two conditions — a restatement of
  reachability/provenance-completeness with new variable names.
- **Correct?** Largely yes.
- **Does draft-v1 answer it?** No — the article never uses "graph
  connectivity" framing or concedes this reading anywhere.
- **Enough?** N/A — unaddressed.
- **Threatens publishability?** Yes — feeds directly into §5's
  obviousness test.
- **v2 must:** name this framing explicitly in the same paragraph as the
  provenance concession, and sharpen the synthesis claim to what
  actually survives it: the demonstration holds *even when every local
  per-node fact is perfect*, which guards against a real, common,
  mistaken engineering intuition (see §5's resolution).

### Objection 6 — The experiment constructs ambiguity by deleting the exact cross-edge later claimed necessary

- **Strongest form:** `DecisionRecordT1` structurally has no field that
  could encode E (`experiment/src/domain.py` lines 43–46); the four
  failing cases were deliberately built (per `case-matrix.md`'s own
  design notes) so no local fact resolves the ambiguity. The result is
  therefore guaranteed before any data is generated — closer to a
  manipulation check than a discovery, and arguably question-begging if
  presented as a finding.
- **Correct?** Yes, substantially — confirmed directly against the
  source files, not merely plausible.
- **Does draft-v1 answer it?** **No.** This objection is not addressed
  anywhere in the article. The closest material is the self-aware
  framing already present in "Ambiguous Is Better Than Wrong" ("a
  differently constructed investigator... could produce false confidence
  instead," line 69), which is adjacent but does not concede that the
  TI=0.33-vs-1.00 headline itself is a designed, not discovered, number.
- **Enough?** Not addressed at all — this is the most dangerous
  unaddressed objection in the piece.
- **Threatens publishability?** **Yes, materially** — an alert reviewer
  who traces `domain.py` will conclude the "experiment" primarily
  illustrates rather than tests H0/H1, since H0 was never at meaningful
  risk given the type design.
- **v2 must:** add an explicit paragraph conceding that the *direction*
  of the T1/T2 gap is guaranteed by construction (this is a manipulation
  check, not a finding), and relocate the article's actual empirical
  claim to where it belongs: P5, the honest-vs-false-confident failure
  mode, which the schema does not force. This is a reconceptualization
  of the article's framing, not a line edit.

## 4. Is the result too obvious? (Section 5 test)

Restated plainly: *"If you do not store graph edges, you cannot always
reconstruct the graph."* Yes — that restatement is accurate, and per
Objection 6, the headline TI numbers are close to guaranteed by how
`DecisionRecordT1` was defined. **This is a genuine, major novelty
threat, and the article does not currently disclose it.**

What survives, without inflation:

1. **The honest-ambiguity vs. false-confidence separation (P5)** is not
   obvious and not guaranteed — DEA=1.00/FGC=0.00 is a property of how
   the investigator was built, and a reasonable, still-not-a-strawman
   investigator could have produced false confidence instead. This is
   real, quantified, and worth keeping.
2. **The demonstration holds while local completeness is perfect
   (LDR=1.00)** — this guards against a genuine, plausible engineering
   mistake (assuming per-decision audit logs are trajectory-sufficient),
   even though the mechanism producing the gap is not itself surprising
   to anyone who has thought about provenance.
3. What does **not** survive as a strong claim: that the T1→T2 gap's
   *existence*, or its *magnitude* (4/6 vs. 2/6), is itself a discovery.
   It is a demonstration of a designed property, correctly quantified,
   not a finding about the world.

**Verdict: PARTIALLY obvious.** The headline framing overclaims; a
narrower framing centered on P5 does not.

## 5. Experimental design review

- **Local equivalence:** PASS. `verify_t1_t2_local_equivalence`
  mechanically checks every local field on every case and re-runs before
  every execution (`src/regimes.py`, `src/run_experiment.py`); this is
  real, not merely asserted.
- **Manipulation validity:** PASS. Regimes differ by exactly one field
  (`consumed_from_decision_id`), confirmed by the type definitions.
- **Construct validity:** PARTIAL. `_dependent_decision_ids`
  (`src/scoring.py` line 44–45) scores **only** decisions with a
  non-None true predecessor — root decisions (D1, D2 in every case) are
  never scored. This means Trajectory Identifiability and Dependency
  Edge Accuracy never test whether an investigator would *falsely invent
  a dependency* for a decision that has none. This is an unflagged
  construct-validity gap: the experiment measures "can you find the true
  edge when one exists," not "can you correctly distinguish 'has a
  dependency' from 'has none,'" which is a real and different failure
  mode a production system could exhibit.
- **Handcrafted cases guaranteed to fail:** YES, by design — see
  Objection 6. Disclosed nowhere in the article; disclosed in
  `case-matrix.md`'s own design notes, which is not equivalent to
  disclosure in the publication.
- **Negative control:** PASS, genuinely narrows the claim, correctly
  centered.
- **Deterministic investigator dependency:** the *existence* of AMBIGUOUS
  outcomes does not depend on a weak investigator (T1's investigator
  actively infers whenever local evidence uniquely determines an edge).
  The *honesty* result (P5) is entirely a property of investigator
  design (never breaks a tie) — correctly self-aware in the article's
  prose (line 69), but this is a design choice being validated, not an
  emergent property of the domain being discovered.
- **Graph definition:** the ground-truth trajectory is well-defined for
  this synthetic testbed; the dependency operationalization (value-match
  or recency) is domain-specific and stipulated, disclosed in the
  article's Limitations.
- **Counterexample nature:** PASS — existence only, not prevalence,
  disclosed clearly and repeatedly (arguably redundantly) in the
  article.

## 6. The "honest ambiguity" claim (Section 8)

This is, correctly, flagged by the authorizing task as potentially the
strongest conceptual point, and the review agrees — but draft-v1 does
not sharpen it as far as it could. The article distinguishes "T1 cannot
uniquely select one trajectory" from "T1 invents wrong trajectories"
(lines 67–69), which is the right distinction, but does not name the
full three-way taxonomy the review requests:

1. **A globally ambiguous retained record** — a property of the regime
   (what was retained), not the algorithm.
2. **A poor reconstruction algorithm** — a property of investigator
   quality, distinct from (1); a weak investigator could fail even where
   the record is not ambiguous.
3. **False confident reconstruction** — a wrong answer stated as fact,
   categorically worse than either (1) or (2), and the one this
   experiment found zero instances of (FGC=0.00).

Draft-v1 conflates (1) into its main narrative and correctly rules out
(3), but never explicitly separates (1) from (2) — a reader could come
away unclear on whether T1's AMBIGUOUS verdicts prove the *record* is
ambiguous or merely that *this particular investigator* couldn't do
better. Given the investigator is not a strawman (it infers wherever
locally determined), the article's own evidence supports (1), but the
article should say so explicitly rather than leaving it implied.

## 7. AI-specificity test (Section 14)

Removal test: replace "AI-mediated trajectory" with "distributed
workflow" throughout — the argument is fully intact; the article's own
closing section admits as much (line 109). **Score: honest, not
overclaiming.**

Legitimate AI-specific value available but unused:
`../../ai-systems-review.md`'s S13/S23 finding that current AI/agent
observability tooling shows "depth without integration" — real,
current, citable, and directly relevant to *why* this gap is a plausible
present-tense concern for AI-agent trajectories specifically, not just a
generic systems-theory footnote. Not cited anywhere in draft-v1. This is
a concrete, low-cost v2 addition that would strengthen AI-relevance
without overclaiming AI uniqueness — the opposite of the risk this
review was asked to check for.

## 8. Formalization review (Section 17)

> ∀i identifiable(C(di)) ⇏ identifiable(E)

- **Is E the dependency edge relation?** Yes, stated as such (line 31).
- **Does the implication capture the experiment?** Loosely. The
  experiment does not actually test identifiability of E as one Boolean
  over the whole relation — it computes a case-level Boolean (Trajectory
  Identifiability) *and* edge-level metrics (Dependency Edge Accuracy,
  False Global Confidence) that carry the article's strongest evidence
  (P5). The single-predicate formalism elides the distinction that
  matters most.
- **Is it trivial?** Yes, substantially — see Objection 6 and P3 above.
  `C(di)` is defined, by the schema, not to contain any information
  about E; "identifiable(C(di)) does not imply identifiable(E)" is close
  to true by definition, not a proposition the data could have
  falsified.
- **Recommendation:** cut it, or replace it with a sentence that
  explicitly labels it as restating the type-level design decision
  rather than a theorem — matching this review's brief that fake
  mathematical sophistication should be removed, not preserved for
  appearance's sake.
