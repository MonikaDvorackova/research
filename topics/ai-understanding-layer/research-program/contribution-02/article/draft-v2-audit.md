---
id: note-contribution-02-article-draft-v2-audit
title: "Article 2 — Self-Audit (draft-v2)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, self-audit, v2]
refs: [draft-v2.md, ../review/VERDICT.md, ../review/BITEMPORAL-VERDICT.md]
---

## Self-Audit — draft-v2

Performed against the eight dimensions required for this revision,
re-checking against the review package's specific findings rather than
re-trusting draft-v1's own prior self-audit.

### Technical correctness (especially bitemporal claims)

**PASS.** The overstated claim from v1 ("No amount of additional
bitemporal completeness fixes this") is removed — confirmed absent by
grep. The corrected claim ("it is not true that no bitemporal
implementation could have avoided this failure... the test system's
retained history did not fully implement that discipline for the
corrected records") matches `../review/BITEMPORAL-VERDICT.md` exactly:
authoritative system-versioned database implementations preserve
original system time on correction; this experiment's fixture did not.
The prior-art section's bitemporal paragraph states the mechanism is
solved "directly" by correctly-implemented system-versioning, with the
disclosed caveat that AI-relevant dependency stores typically aren't
built this way — matches `../review/revision-plan-v2.md`'s revised P0-1
requirement precisely.

### Primary experiment honesty (Cases 3/9 narrowed, Case 8 emphasized)

**PASS.** "Experiment: When History Changes After the Decision" leads
with Case 8 ("the clean, unqualified case is the one involving a
retroactive authority correction") as the primary illustration, exactly
as `../review/BITEMPORAL-VERDICT.md` requires. Cases 3/9 are explicitly
named as weaker ("turned out to be weaker than they first appeared...
demonstrate a limitation of the specific reconstruction procedure that
was run, not a clean information gap"), with the specific mechanism (raw
threshold value in the event trace, uncross-referenced by the tested
algorithm) stated precisely, matching `../review/bitemporal-verification.md`
Section 6.

### Follow-up interpretation (is AMBIGUOUS represented as correct behavior?)

**PASS.** Stated explicitly and prominently: "AMBIGUOUS is not the
failure mode to worry about... an honest non-answer, not a wrong one."
This is not merely present but given its own emphasized sentence,
matching the authorizing brief's requirement that this distinction be
one of the article's strongest ideas, not a buried caveat.

### Negative control (is binding uniqueness explicitly rejected?)

**PASS.** "The Negative Control That Reframes the Thesis" states
directly: "The stronger, more architecturally specific claim — that an
explicit, decision-time-authored binding record is what's required —
does not survive this case." No hedging, no burying — this is the
section's opening argumentative move, matching `../review/reviewer-report.md`'s
assessment that this was already draft-v1's strongest-executed section,
now carried forward with equal prominence and placed earlier in the
argument per the restructure.

### Prior-art fairness (can existing mechanisms implement the property?)

**PASS.** "Prior Art, Revisited Honestly" opens with "each can supply a
consumption relation. Whether a given deployment actually does is a
separate, checkable question, not something the mechanism guarantees by
existing" — conditional framing applied consistently across PROV, event
sourcing, tracing, and bitemporal databases, with the bitemporal entry
specifically corrected per the technical-correctness check above. No
mechanism is characterized as inherently solving or inherently failing —
matches the authorizing brief's explicit requirement.

### AI specificity (no claim that this is uniquely an AI phenomenon?)

**PASS.** Stated as directly as the brief requires, in the opening
itself: "This is a general systems and provenance problem, not something
unique to AI... Nothing below claims AI creates this problem. It claims
AI decisions are a dense, realistic setting to measure it in." This is
placed in the third paragraph of the article, before any experiment is
introduced — the earliest point it could credibly appear — directly
addressing `../review/reviewer-report.md`'s 2/5 AI-specific-relevance
score and `../review/VERDICT.md`'s required correction.

### Citations (are all externally sourced technical claims supported?)

**PASS**, after one fix applied during drafting (see
`editorial-notes-v2.md`). All five references are cited inline at least
once (verified by grep: `[1]` x2, `[2]` x3, `[3]` x3, `[4]` x2, `[5]` x1
— re-confirmed after the dangling-reference fix). Every citation maps to
a source already verified via live fetch in this programme (`[1]`, `[4]`
from the original prior-art audit; `[2]`, `[3]` from the dedicated
bitemporal-verification pass; `[5]` from `../review/citation-plan.md`'s
existing REQUIRED list) — no fabricated metadata, matching this task's
explicit prohibition.

### Article 3 boundary (no leakage?)

**PASS.** Grepped for "understanding layer," "capability... understanding,"
"epistemic debt," "fragmentation" — zero matches. Grepped bare
"understanding" — exactly one occurrence, the same permitted, undeveloped
closing bridge sentence carried over from draft-v1 verbatim ("Historical
reconstructability is only one dimension of what it means to preserve
understanding of a system over time"). No expansion, no new development.

---

## Additional checks beyond the required eight

- **Empirical traceability of new/changed numeric claims:** the two
  numbers added during drafting (Ambiguity Detection Rate 1.00; False
  Historical Confidence 0.00 "throughout the entire experiment, for both
  investigators, on every case") were checked directly against
  `../../experiment/followup-case10/results/case_level_results.csv`
  before being added — `adr=1.0000` on all four ambiguous cases;
  `fhc_rate=0.0000` on all twelve rows (both regimes, all six cases),
  confirmed by re-inspection during this audit, not merely asserted.
- **Word count discipline:** 2,519 words, within the 2,400–3,000 target,
  tighter than draft-v1's 2,723 — matches the authorizing brief's
  expectation without requiring padding to reach a floor.
- **Terminology discipline:** "consumption relation" introduced once,
  explicitly defined, and used consistently thereafter as the primary
  term for the general property; "causal" appears exactly twice, both
  uses checked — the first explicitly disclaims the statistical-causal-
  inference reading at first use (matching the authorizing brief's
  Section 6 instruction precisely), the second is a standard, narrow
  technical description of OpenTelemetry span relationships, not a claim
  about this article's own central property. "State Is Not Knowledge"
  and bare "knowledge": zero occurrences, confirmed by grep.
  "Decision-context identifiability": not used at all in v2 — a
  legitimate simplification per the authorizing brief's "use only if it
  materially clarifies" instruction; the property is fully explained in
  prose without needing the term.

## Summary

| Dimension | Verdict |
|---|---|
| Technical correctness (bitemporal) | PASS |
| Primary experiment honesty | PASS |
| Follow-up interpretation | PASS |
| Negative control | PASS |
| Prior-art fairness | PASS |
| AI specificity | PASS |
| Citations | PASS (one dangling-reference fix applied during drafting) |
| Article 3 boundary | PASS |

No violation required correction after this audit was performed — the
one fix identified (the dangling `[5]` reference) was caught and applied
during the drafting pass itself, before this audit document was written,
consistent with this task's instruction to "fix problems before
finalizing."
