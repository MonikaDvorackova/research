---
id: note-contribution-02-drafting-claim-ledger
title: "Contribution 2 Drafting Readiness — Claim Ledger"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, claim-ledger]
refs: [../experiment/RESULT.md, ../experiment/followup-case10/RESULT.md, novelty-review.md]
---

## Claim Ledger

Classification key:

- **A** — Directly supported by experiment (primary and/or follow-up raw
  results).
- **B** — Supported by prior art (audit/collision-test findings, not the
  experiments).
- **C** — Synthesis / interpretation (a reasonable reading of A/B
  together, not itself a measured or cited fact).
- **D** — Plausible but unsupported (must not appear in the article as
  stated).
- **E** — Contradicted / narrowed by our own results (must not appear in
  the article in its original form).

| # | Claim | Class | Basis / required treatment |
|---|---|---|---|
| 1 | Versioning alone always suffices | **E** | Directly contradicted: primary experiment Cases 3/8/9 (TC: B=0.00) and follow-up Cases F10-2/3/4/5 (B not `CORRECT_UNIQUE`). **Must not appear.** If mentioned at all, only as the null hypothesis (H0) that was rejected on these specific cases. |
| 2 | Versioning alone never suffices | **E** | Equally contradicted, in the other direction: primary Cases 1/2/4/5/6/7 and follow-up F10-1 show B ≈ C exactly when there is no retroactive correction and no observational ambiguity. **Must not appear** as a general statement. Correct, supportable claim: versioning alone suffices *except* under the two tested mechanisms. |
| 3 | Retroactive correction can break historical reconstruction | **A** | Primary experiment, Cases 3/8/9: categorical TC drop (1.00→0.00) with confidently wrong answers (FHC up to 1.00). Directly supported, precisely scoped to this synthetic testbed. |
| 4 | Temporal precision loss can create genuine underdetermination | **A** | Follow-up, Cases F10-2/3/4/5: B honestly reports `AMBIGUOUS` (ADR=1.00) rather than guessing, and cannot uniquely resolve without a causal signal. Directly supported. |
| 5 | Explicit binding resolves these tested cases | **A** | Regime C achieves `CORRECT_UNIQUE`/TC=1/FHC=0.00 on every case in both experiments, no exception. Directly supported. |
| 6 | Causal event linkage can also resolve ambiguity | **A** | F10-6 negative control: a non-binding causal consumption event fully matches Regime C's performance. Directly supported, and this is the specific result that forces claim 7 into class E. |
| 7 | Explicit binding is uniquely necessary | **E** | Directly contradicted by claim 6 / F10-6. **Must not appear.** This was the original (pre-follow-up) formulation; it is superseded. See `../novelty-verdict.md`'s follow-up-dated update. |
| 8 | Causal linkage (in general) is the operative property | **C** | Not itself a single measured data point — it is the synthesis of claims 3, 4, 5, and 6 taken together, consistent with all four and not contradicted by any result. This is the article's central interpretive claim; it must be presented as a synthesis, not as a single experimental finding. |
| 9 | "State is not knowledge" | **B, narrowed to C for the technical thesis** | The phrase itself is Source A's framing (`../../sources/source-a-missing-layer.md`), not an experimental result. `../prior-art-audit.md` Task 2 already found the dichotomy imprecise as literally stated (several "state" examples are already historical, append-only records). Retained only as practitioner-register color per `../novelty-verdict.md`; the technical thesis uses "causal relation," not "knowledge." See `titles-and-terminology` decision in this package. |
| 10 | Provenance (PROV) always solves the problem | **E** | Directly narrowed: PROV solves the follow-up's mechanism (if version-identified) but not the primary experiment's (no valid-time semantics) — see `prior-art-matrix.md`. "Always" **must not appear**; correct form: "PROV can solve one of the two tested mechanisms, conditionally." |
| 11 | Event sourcing always solves the problem | **E** | Same structure as 10: solves it only if deliberately instrumented to capture identifiers rather than values (F10-6 confirms this branch works; the primary experiment's Regime B, a genuine event-sourcing implementation capturing values, confirms the other branch fails). "Always" **must not appear**. |
| 12 | AI systems commonly lack causal decision-context preservation | **D** | Plausible, consistent with the prior-art audit's qualitative findings (prompt/retrieval/policy stores "essentially never built with valid-time semantics by default") — but "commonly" is a prevalence claim, and neither experiment nor the audit measured prevalence in real systems. **Must not appear as stated.** Permissible, narrower form: "the prior-art audit did not find an example of a surveyed mechanism doing this by default" (a claim about the audit's own search, not about the world). |
| 13 | Inability to reconstruct creates governance/compliance risk | **D** | Plausible and intuitively motivating, but neither experiment measured any compliance or governance outcome — this is outside both experiments' scope entirely (`../experiment/experiment-design/validity-and-confounders.md`'s external-validity limitation). **Must not appear as an established claim.** Permissible only as motivating framing in an introduction, explicitly marked as motivation, not as a finding. |
| 14 | The mechanism generalizes to production systems | **D** | Explicitly and repeatedly disclaimed by both experiments' own design docs as out of scope (`../experiment/experiment-design/validity-and-confounders.md`; `../experiment/followup-case10/analysis/experiment-report.md`'s "What the result does NOT support"). **Must not appear.** Required framing: "demonstrated in a controlled, synthetic setting; a real-system follow-up would be required to generalize," stated explicitly wherever the mechanism is discussed. |

## Claims requiring removal or softening — exact instructions

- **Claim 1, 2, 7, 10, 11** (the four "always/never/uniquely" claims):
  remove any absolute quantifier. The article may state the *conditional*
  form only ("X suffices except when...", "Y resolves this if and only
  if..."), never the unconditional form, because the unconditional form
  is directly contradicted by at least one of the two experiments'
  results.
- **Claim 12**: replace any claim about real-world prevalence with a claim
  about the audit's own search result (absence-in-the-surveyed-literature,
  not absence-in-the-world).
- **Claim 13**: may appear only in framing/motivation sections (e.g., "why
  should a reader care"), never adjacent to a results claim, and must be
  clearly marked as motivation rather than finding.
- **Claim 14**: every discussion of either experiment's result must carry
  its own scope statement ("in this synthetic testbed") rather than
  relying on a single disclaimer stated once and then dropped for the
  rest of the article.

## What survives cleanly, unqualified within its own scope

Claims 3, 4, 5, and 6 (class A) are the article's actual empirical
content and may be stated directly, with the scope already attached in
their basis column (specific cases, specific experiment). Claim 8 (class
C) is the article's thesis-level synthesis and must always be presented
as an interpretation of 3–6, not as an additional, independent finding.
