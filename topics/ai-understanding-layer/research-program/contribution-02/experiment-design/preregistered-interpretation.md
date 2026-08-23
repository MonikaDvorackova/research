---
id: note-contribution-02-experiment-preregistration
title: "Contribution 2 Experiment — Pre-Registered Interpretation"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, pre-registration]
refs: [metrics-and-scoring.md, validity-and-confounders.md]
---

## Pre-Registered Interpretation Table

Written **before** implementation or execution, per the brief's explicit
instruction, to prevent post-hoc narrative adjustment once results exist.
Any future write-up of this experiment must reference which row of this
table the actual result matched, and must not introduce a new
interpretation not anticipated here without explicitly flagging it as
unanticipated.

**Step 0, required first:** run the manipulation check
(`validity-and-confounders.md`) — confirm Regime A fails on Cases 2, 4, 6,
7. If it does not, stop and revise the drift magnitude before interpreting
any other result.

| # | Result pattern | Interpretation |
|---|---|---|
| 1 | C >> B on TC and FHC, concentrated specifically in Cases 3, 8, 9, 10 (retroactive/concurrency); B ≈ C on Cases 1, 2, 4, 5, 6, 7 | **Strong support.** The exact mechanism predicted by `../temporal-semantics.md` is confirmed. Explicit decision-time binding is empirically necessary specifically where bitemporal inference is structurally unstable (retroactive correction) or ambiguous (concurrency) — not more broadly than that. |
| 2 | C >> B on TC/FHC uniformly across all categories, including the simple forward-drift cases (2, 4, 6, 7) where B was expected to succeed | **Support, but broader and less precise than predicted.** Worth investigating whether the as-of-t0 query algorithm specified for Regime B (`implementation-spec.md`) was implemented correctly before concluding the mechanism is broader than theorized — first check for an internal-validity failure (a weak B algorithm), per `validity-and-confounders.md`, before accepting this as a stronger-than-expected true result. |
| 3 | C ≈ B on TC/FHC in all categories, but both >> A | **Thesis not supported as stated.** Versioning (already well-established prior art) is doing the work; explicit binding's specific marginal contribution is not demonstrated. Push toward Verdict C (framing only) in `../novelty-verdict.md` rather than Verdict B. |
| 4 | B >> A but C ≈ B, specifically including on Cases 3 and 10 | **Strongest possible disconfirmation of H1.** The single case the design was built to detect (retroactive correction / concurrency ambiguity) shows no binding advantage. Report exactly as `metrics-and-scoring.md`'s "what would specifically kill the thesis" section anticipates, without softening. |
| 5 | A ≈ B ≈ C across all categories | **Ambiguous between "thesis false" and "design too weak to discriminate."** Run the manipulation check first (Step 0 above). If A genuinely fails to differ from B/C even on Cases 2/4/6/7, the case matrix or drift magnitudes need revision before any thesis conclusion can be drawn — do not report this as thesis falsification without first ruling out a design defect. |
| 6 | C improves JC and AIA over B, but not TC or FHC specifically | **Different mechanism than hypothesized.** Binding improves completeness/traceability (more answers given, more versions correctly named in the *non-drift* sense) without improving temporal correctness under drift specifically. Requires reformulating the thesis around completeness rather than temporal correctness — a real but narrower finding than H1 as stated. |
| 7 | C reduces FHC relative to B without a corresponding improvement in raw AC | **Partial support** (per `metrics-and-scoring.md`). Binding converts silent wrong answers into honest `UNDETERMINED` flags more than it changes the final GRANT/DENY outcome. A genuine, valuable, narrower claim about epistemic honesty rather than bottom-line correctness — reframe the thesis accordingly if this is the observed pattern. |
| 8 | Regime B fails Case 10 (concurrency) but succeeds Case 3 (retroactive), or vice versa | **Partial mechanism confirmation.** One of the two theorized failure mechanisms in `preservation-regimes.md`'s bitemporal analysis (retroactive correction vs. interval-matching ambiguity under concurrency) is empirically real and the other is not, within this design. Report which one, specifically — do not merge them into a single undifferentiated "binding helps" conclusion. |
| 9 | Regime B succeeds on Case 8 (combined retroactive drift) despite failing on Case 3 (isolated retroactive drift) | **Internal inconsistency requiring investigation before any conclusion.** This would suggest a scoring or implementation error (e.g., ground truth or query logic differing unintentionally between the isolated and combined versions of the same mechanism), not a genuine result — must be debugged, not interpreted, if observed. |

---

## Commitment

This table is treated as fixed once implementation begins. If actual
results correspond to a pattern not listed above, that must be reported as
an **unanticipated result** requiring new interpretation, explicitly
labeled as such — it must not be silently mapped onto the nearest listed
row to manufacture a pre-registered appearance it does not have.
