---
id: note-contribution-02-article-draft-v1-audit
title: "Article 2 — Self-Audit (draft-v1)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, self-audit]
refs: [draft-v1.md, ../drafting-readiness/claim-ledger.md, ../drafting-readiness/contribution-boundary-check.md]
---

## Self-Audit — draft-v1

Performed after drafting, against the eight required dimensions. One
precision issue was found and fixed in draft-v1 before this audit was
finalized (noted below); no other violation was found.

### Novelty inflation

**PASS.** No sentence claims a new mechanism or architecture. "This Is
Not a New Provenance System" states directly that no mechanism is
reinvented. "Two Ways to Preserve It" explicitly declines to prescribe a
schema: "Neither is presented here as the correct one." "The Property to
Design For" is framed as a design *question*, not a component to build.
Checked against `../drafting-readiness/claim-ledger.md` claim 7
("explicit binding is uniquely necessary," class E) — the draft states
the opposite directly in "The Negative Control That Changed the Thesis."

### Empirical overreach

**PASS.** "What the Experiments Do — and Do Not — Show" states no-
prevalence, no-universal-mechanism, no-required-binding, and
scope-limited-to-two-mechanisms explicitly, as its own dedicated section
rather than a footnote. The False Historical Confidence section
additionally carries its own inline scope statement ("This is a result
from one synthetic testbed... not a claim about how often this happens
anywhere else") immediately next to its strongest sentence, per
`../drafting-readiness/claim-ledger.md`'s requirement that scope
statements travel with each result rather than being stated once at the
top and forgotten. Grepped for the claim-ledger's specific forbidden
phrases (prevalence, "most AI systems," "production AI commonly,"
"proves compliance/trustworthiness") — zero matches in draft-v1.

### Negative-control honesty

**PASS.** F10-6 has its own section, "The Negative Control That Changed
the Thesis," placed immediately after Experiment 2 and before the
prior-art revisit — not deferred to a footnote or a limitations
aside. The section states plainly that it narrows the thesis ("does not
survive," "smaller than it might have first appeared, and more
defensible for being smaller") rather than minimizing the result's
consequence.

### Prior-art fairness

**PASS.** "This Is Not a New Provenance System" credits PROV, event
sourcing, and bitemporal databases with fully solving the parts of the
problem they are structurally suited to solve, and states the qualifying
condition for each precisely (valid-time interval for PROV; identifiers-
not-values for event sourcing; retroactive-correction as the specific
boundary case for bitemporal databases) rather than asserting a blanket
"these don't work."

### Article 3 leakage

**PASS.** Grepped the full draft for "understanding layer," "capability
vs. understanding," "epistemology," "fragmentation," "industry-wide," and
"paradigm shift" — zero matches. Grepped bare "understanding" — exactly
one occurrence, the single permitted closing bridge sentence ("Historical
reconstructability is only one dimension of what it means to preserve
understanding of a system over time."), left undeveloped, with no
following sentence explaining or expanding it, per the authorizing
brief's explicit instruction to stop there.

### Terminology

**PASS**, after one fix. Grepped for "knowledge" (zero matches — correctly
avoided per `../drafting-readiness/thesis-and-titles.md`'s decision that
the phrase does not survive) and for bare "decision context" (zero
matches — the draft consistently uses the narrower, terminology.md-
approved "consumed context" instead). "Binding" is used consistently to
name Regime C's specific mechanism and the narrowed claim about it, never
as the name of the general required property (that role is filled by
"causal relation" / "preserved relation" / "decision-context
identifiability," matching `../drafting-readiness/terminology.md`'s
recommendations).

One precision issue was found and fixed during this audit, not a
terminology violation but an accuracy one: the original phrasing "the two
decisions were recorded 60 seconds apart around a boundary" could be
misread as a 60-second gap between the two decisions (the actual gap is
120 seconds; each decision sits 60 seconds from the boundary on its own
side). Corrected to "each decision was recorded a full 60 seconds from
the boundary, on its own side" before finalizing this audit.

### Evidence

**PASS.** Every empirical number in the draft was checked directly
against the committed CSVs immediately before drafting and re-verified
during this audit:

| Draft claim | Source | Verified value |
|---|---|---|
| Case 3 (retroactive): B TC 0.00, C TC 1.00 | `../experiment/results/case_level_results.csv`, case_id=3 | B tc=0, C tc=1 ✓ |
| Cases 2, 4 (forward drift): B and C both 1.00 | Same file, case_id=2 and 4 | Both TC=1 for B and C ✓ |
| Cases 8, 9 (combined drift): B TC 0.00, C TC 1.00 | Same file, case_id=8, 9 | B tc=0 both; C tc=1 both ✓ |
| Case 3 FHC: B=0.50 | Same file | fhc_rate=0.5000 ✓ |
| Case 8 FHC: B=1.00 | Same file | fhc_rate=1.0000 ✓ |
| C's FHC=0.00 on every case | Same file, all C rows | Confirmed, no exception ✓ |
| Follow-up F10-2/3/4/5: B ambiguity detection rate 1.00 on the ambiguous dimension | `../experiment/followup-case10/results/case_level_results.csv` | adr=1.0000 on all four ✓ |
| Follow-up: C correct/unique on every case | Same file | All C rows: `CORRECT_UNIQUE` across policy/authority/model ✓ |
| F10-6: B matches C exactly on every metric | Same file, case_id=F10-6 | B and C rows identical: tc=1, urr=1.0000, ac=1, fhc_rate=0.0000 ✓ |
| Original Case 10 timestamps (11:59:00 / 12:01:00 around 12:00:00) | `../experiment/results/case_level_results.csv` + `../experiment/src/cases.py` (case_f10 boundary construction, cross-checked against primary experiment's `case_10()`) | Confirmed via source inspection during this session |

No number in the draft was estimated, rounded beyond the CSVs' own
four-decimal precision, or invented.

### Reader value

**PASS.** The article teaches a transferable engineering distinction
("The Property to Design For" gives a design question a reader can apply
to their own system) and two concrete, non-exclusive implementation
patterns ("Two Ways to Preserve It"), rather than only reporting the
experiment's own results. A reader who skipped both experiment sections
entirely could still extract the core distinction and the design question
from "Version History Is Not Decision History" and "What a Historical
Decision Actually Depends On" alone.

## Summary

| Dimension | Verdict |
|---|---|
| Novelty inflation | PASS |
| Empirical overreach | PASS |
| Negative-control honesty | PASS |
| Prior-art fairness | PASS |
| Article 3 leakage | PASS |
| Terminology | PASS (one accuracy fix applied) |
| Evidence | PASS |
| Reader value | PASS |

One fix was applied to draft-v1 as a direct result of this audit (the
60-seconds phrasing). No other change was required.
