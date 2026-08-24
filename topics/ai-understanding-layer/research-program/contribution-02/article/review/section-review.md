---
id: note-contribution-02-article-review-section-review
title: "Contribution 2 Article — Section-by-Section Editorial Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, section-review]
refs: [../draft-v1.md, reviewer-report.md]
---

## Section-by-Section Review

Target for v2: **tighter than v1**, not longer. Only one section
genuinely needs new material (the transaction-time nuance); every other
change is a cut, merge, or precision fix.

### Title + dek

**Purpose:** set expectations. **Works:** dek ("Retained is not
consumed...") is precise. **Redundant:** none. **Unsupported:** the main
title's "AI Decision" framing, per `reviewer-report.md`'s AI-specificity
finding. **Vulnerable:** "explain" risks XAI/explainability association
(see `title-review.md`). **Verdict: REVISE.** Target: resolve per
`title-review.md`'s recommendation.

### Opening (untitled, paragraphs 1–4)

**Purpose:** ground the paradox concretely before jargon. **Works:** the
paradox lands by paragraph 4; no prevalence claim. **Redundant:** none.
**Unsupported:** none — this section makes no empirical claim yet.
**Vulnerable:** genericness of the artifact list (see
`reviewer-report.md`'s opening review — "specific model version... specific
policy..." reads as a list, not a scene). **Verdict: REVISE** (light —
add one concrete illustrative value, per P2 in `revision-plan-v2.md`).

### Version History Is Not Decision History

**Purpose:** pre-empt the "we already have versioning" objection fairly.
**Works:** genuinely does not strawman — names six real mechanisms
before pivoting. **Redundant:** the closing sentence ("That distinction
sounds abstract until it's made concrete...") is a pure transition with
no content; could merge into the next section's opening. **Unsupported:**
none. **Vulnerable:** this section is where Objection 1
(`reviewer-report.md`) should eventually be pre-empted, but currently
isn't — the transaction-time nuance belongs in Experiment 1's section,
not here, since this section makes no bitemporal-specific claim yet.
**Verdict: KEEP**, minor trim only (P3).

### What a Historical Decision Actually Depends On

**Purpose:** define consumed context and decision-context
identifiability. **Works:** the formal notation is minimal, used once,
and matches `../../drafting-readiness/formalization.md`'s
recommendation not to overbuild it. **Redundant:** none. **Unsupported:**
none — this is a definitional section. **Vulnerable:** Objection 5
(`reviewer-report.md`: "isn't this just referential integrity?") is not
pre-empted here, where it would most naturally fit. **Verdict: REVISE**
(add one sentence distinguishing the property from referential
integrity — P2).

### Experiment 1: When History Changes After the Decision

**Purpose:** report the primary experiment's retroactive-correction
result. **Works:** the numbers are exact and traceable
(`empirical-traceability.md`); the forward-drift control comparison
(both at 1.00) is included, which is good practice against strawmanning.
**Redundant:** none. **Unsupported:** none — the numbers are correct.
**Vulnerable:** this is the section carrying `reviewer-report.md`'s
headline finding. As written, it asserts "no amount of additional
bitemporal completeness fixes this" — **this specific sentence is not
supported** by the review's independent inspection and is the draft's
single highest-priority required change. **Verdict: REVISE (P0)** — add
the transaction-time-query nuance; do not remove the section, since the
underlying result (this specific algorithm failed, and the metric is
real) remains true and worth reporting, just not with the current
unqualified framing.

### The More Dangerous Failure: A Wrong Answer That Looks Right

**Purpose:** introduce False Historical Confidence. **Works:**
well-written, correctly scoped ("a result from one synthetic testbed, not
a claim about how often this happens anywhere else"), correctly
distinguishes honest-abstention from confident-wrongness in the abstract.
**Redundant:** none. **Unsupported:** none in isolation — but this
section's *example* is the same retroactive-correction case Experiment
1's section uses, so it inherits that section's P0 issue by reference.
**Vulnerable:** per `reviewer-report.md`'s FHC deep-dive, this section
should eventually note (once Experiment 1's section is fixed) that the
confident-wrongness here is specifically an artifact of *which* query
was run, not evidence that confident-wrongness is unavoidable given
Regime B's data. **Verdict: KEEP structurally, REVISE for one added
sentence once Experiment 1's fix lands (P0, dependent on that fix).**

### Experiment 2: When Time Does Not Identify a Unique Context

**Purpose:** report the follow-up's precision-loss result. **Works:**
fully — this is the strongest experiment-reporting section in the draft,
survives independent inspection without modification
(`reviewer-report.md`). Correctly explains why the original Case 10
didn't work, correctly frames B's `AMBIGUOUS` result as not the dangerous
failure mode. **Redundant:** none. **Unsupported:** none. **Vulnerable:**
none identified. **Verdict: KEEP, no changes required.**

### The Negative Control That Changed the Thesis

**Purpose:** report F10-6 and narrow the thesis. **Works:** fully —
`reviewer-report.md` calls this "the strongest-executed section in the
draft." Prominent placement, correct framing, correctly forecloses the
"proprietary binding architecture" misreading. **Redundant:** none.
**Unsupported:** none. **Vulnerable:** none identified. **Verdict: KEEP,
no changes required.**

### This Is Not a New Provenance System

**Purpose:** revisit prior art honestly after the experiments.
**Works:** four of five sub-claims (PROV, event sourcing, tracing/logs/
lineage) survive independent inspection unmodified. **Redundant:** none.
**Unsupported:** the bitemporal-databases paragraph's claim ("solve it
completely — for exactly the cases without retroactive correction") is
the article's one factually incomplete claim, per `reviewer-report.md`.
**Vulnerable:** same paragraph. **Verdict: REVISE (P0)** — this paragraph
must be corrected in the same pass as Experiment 1's section, since both
draw on the same underlying fact.

### The Property to Design For

**Purpose:** give a practical design test. **Works:** the boxed question
is genuinely reusable and well-phrased. **Redundant:** partially restates
"What a Historical Decision Actually Depends On" — acceptable repetition
for a practitioner takeaway, but could be tightened. **Unsupported:**
none. **Vulnerable:** none. **Verdict: KEEP, minor tightening only (P3)**
— consider whether this section and "What a Historical Decision Actually
Depends On" could merge; recommend against merging (the first is
definitional, this one is actionable — different reader jobs), but flag
for editorial judgment.

### Two Ways to Preserve It

**Purpose:** show two non-exclusive implementations. **Works:** the two
code blocks are genuinely illustrative and short. **Redundant:** none.
**Unsupported:** none — explicitly hedged ("Neither is presented here as
the correct one"). **Vulnerable:** none. **Verdict: KEEP, no changes
required.**

### What the Experiments Do — and Do Not — Show

**Purpose:** limitations. **Works:** thorough, five distinct points, not
buried in a single footnote sentence — matches the authorizing brief's
requirement for both draft-v1 and this review. **Redundant:** none.
**Unsupported:** none — this section is entirely negative claims
(disclaimers), which by construction cannot be overstated. **Vulnerable:**
should gain one more bullet once Experiment 1 is corrected: "the
retroactive-correction result specifically reflects one query algorithm's
behavior, not a proof that bitemporal completeness cannot solve
retroactive correction" — this is a natural home for a compressed version
of the P0 fix. **Verdict: REVISE (P1)** — add one bullet, once Experiment
1's section is fixed, cross-referencing it.

### The Question to Ask (+ closing bridge sentence)

**Purpose:** land the practical takeaway; one permitted Contribution-3
gesture. **Works:** the reframed question is a strong, quotable closing
line. **Redundant:** none. **Unsupported:** none. **Vulnerable:** none —
the bridge sentence is appropriately undeveloped, matching
`../../drafting-readiness/contribution-boundary-check.md`'s requirement.
**Verdict: KEEP, no changes required** — this is an editorial-taste
question (`../editorial-notes.md` already flags whether to keep or cut
the bridge sentence), not a correctness issue.

---

## Aggregate verdict

| Section | Verdict | Priority |
|---|---|---|
| Title + dek | REVISE | P1 |
| Opening | REVISE (light) | P2 |
| Version History Is Not Decision History | KEEP | P3 |
| What a Historical Decision Actually Depends On | REVISE | P2 |
| Experiment 1 | REVISE | **P0** |
| The More Dangerous Failure | REVISE (dependent) | **P0** |
| Experiment 2 | KEEP | — |
| The Negative Control | KEEP | — |
| This Is Not a New Provenance System | REVISE | **P0** |
| The Property to Design For | KEEP | P3 |
| Two Ways to Preserve It | KEEP | — |
| What the Experiments Do/Do Not Show | REVISE | P1 |
| The Question to Ask | KEEP | — |

**No section merits CUT.** No section requires expansion beyond the P0
fix and its dependents. Three sections carry the same underlying P0 issue
and should be revised together, in one pass, for consistency.
