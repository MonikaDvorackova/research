---
id: note-contribution-02-article-review-bitemporal-verdict
title: "Contribution 2 Article — Bitemporal Finding Verification Verdict"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, verification, verdict]
refs: [bitemporal-verification.md, reviewer-report.md]
---

## Reviewer finding

**PARTIALLY CONFIRMED.**

The specific mechanism `reviewer-report.md` proposed — a transaction-
time-anchored (`SYSTEM_TIME AS OF t0`) bitemporal query recovering the
correct answer from information Regime B already retains — is
**REJECTED**, empirically, for the system as actually implemented: direct
inspection of the executed fixtures (`bitemporal-verification.md`,
Sections 1–3) shows the specific fact such a query needs (the original,
pre-correction `recorded_at` on the closed policy/authority row) was not
retained — both remaining rows carry the correction's own transaction
time. A semantically-derived version of the proposed query, run against
the actual data, returns nothing, not the correct answer.

The underlying **concern** that motivated the finding — that the primary
experiment's retroactive-correction result might be an artifact of the
specific reconstruction algorithm rather than an information-architecture
property of Regime B — is **confirmed, via a different mechanism**, for
two of the three affected cases (3 and 9): a raw, immutable value already
captured in Regime B's event trace (`threshold_value_read = 0.50`)
uniquely and correctly identifies the historically valid policy version
among the two retained rows, if an investigator cross-references it —
which the tested algorithm does not do. This mechanism is real but
narrow: fixture-specific (works only because the pre/post-correction
threshold values differ), and does not extend to Case 8's authority
dimension, which has no analogous raw-identity field and remains a clean
information gap.

## Primary experiment classification

**B — VALID BUT OVERINTERPRETED**, as a whole-experiment characterization
— with the explicit caveat that this is a **mixed, case-dependent**
result, not uniform across the three affected cases. Evaluated in
isolation, Case 8 alone would warrant **A**; Cases 3 and 9 warrant **B**.
No case supports **C**, and the evidence is specific and confident enough
to rule out **D**.

## Cases 3 / 8 / 9

- **Case 3 (isolated retroactive policy drift): B — overinterpreted.**
  Regime B's retained data (specifically, the event trace's raw
  `threshold_value_read = 0.50`, cross-referenced against all retained
  policy rows including the closed one) is sufficient to recover the
  correct answer ("v1"); the tested algorithm does not perform this
  cross-reference and therefore reports the wrong answer confidently. The
  reported TC=0.00/FHC=0.50 result reflects the tested algorithm's
  limitation, not an inherent property of Regime B's retained information.
- **Case 8 (combined retroactive policy + authority): A — valid as
  originally interpreted.** The policy dimension has the same escape
  hatch as Case 3, but Temporal Correctness on this case requires *both*
  policy and authority correct. The authority dimension has no
  analogous raw-identity field anywhere in Regime B's retained data
  (`approver_check_result` is a boolean, never an agent ID) — the
  information genuinely does not exist, under any query strategy. Case
  8's TC=0.00/FHC=1.00 result stands as valid, undiminished evidence.
- **Case 9 (retroactive policy + forward authority + other forward
  drift): B — overinterpreted**, structurally identical to Case 3's
  reasoning — the escape hatch applies to the same policy mechanism; the
  authority dimension in Case 9 is forward-drift (not retroactive) and
  already resolves correctly under the existing algorithm, so it needs no
  escape hatch.

## False Historical Confidence

**Does not survive as originally stated, for Cases 3 and 9 specifically;
survives fully and without qualification for Case 8.** FHC's definition
and measurement procedure are unaffected (the metric itself is sound —
`reviewer-report.md`'s FHC review, unchanged). What must change is the
claim drawn from it: the confident-wrong answers on Cases 3 and 9 are a
demonstrated property of the **specific reconstruction algorithm tested**
(it does not cross-reference retained raw values against superseded
version rows), not a demonstrated property of "versioned-but-unbound
histories" as a category. Case 8's FHC=1.00 result requires no such
qualification — it is a genuine, unrescuable false-confidence failure
given Regime B's actual retained information.

## Follow-up Case 10

**NO, unaffected.** Verified directly: the follow-up's domain model
(`experiment/followup-case10/src/domain.py`, `src/reconstruction.py`)
has no `recorded_at`/transaction-time field anywhere, no retroactive
correction of any kind, and no closed/reopened rows — the mechanism this
verification investigated (transaction-time information loss during row
closure) does not exist in that codebase. The follow-up's own mechanism
(observational timestamp-precision loss) and its results stand exactly
as reported.

## F10-6

**NO, unaffected as a result — but conceptually connected, worth noting.**
F10-6 remains exactly as reported: a deliberately-added, explicitly
negative-control causal-consumption event resolves the follow-up's
ambiguity. This verification's Case 3/9 escape hatch is a **structurally
similar but independently-discovered, coincidental** instance of the same
underlying pattern (an ordinary, already-retained signal — a captured
value, not a formal binding — resolving what version-identity-only
querying cannot) arising unplanned in the primary experiment, rather than
by deliberate design as in F10-6. This strengthens the programme's
overall thesis about causal/value signals being the operative mechanism,
but it does not change F10-6's own reported numbers or role.

## Contribution 2

**SURVIVES NARROWED.**

**Exact surviving empirical claim:** under retroactive correction where
the corrected dimension has no independently-captured, uniquely-
identifying raw value available for cross-reference (demonstrated
concretely by Case 8's authority dimension), and under observational
timestamp-precision loss with no causal-consumption signal present
(demonstrated by the follow-up's F10-2 through F10-5), retained version
history is not sufficient for unique, correct decision-context
reconstruction — and closing the gap requires some preserved relation
connecting the decision to its consumed context, which can take the form
of an explicit binding, a captured raw value later cross-referenced
against version history, or an ordinary causal-consumption event.

**Exact claim that must be removed:** that Regime B's retroactive-
correction failure, reported in aggregate across Cases 3, 8, and 9 (or
via the primary experiment's summary TC 1.00→0.00 figure), demonstrates
an unqualified information-architecture insufficiency of "versioned but
unbound" histories as a general category — this claim is true only for
Case 8 among the three, not for Cases 3 and 9, whose reported failures
reflect the specific tested algorithm's choice not to cross-reference
captured values against superseded records.

## Is draft-v2 now safe to authorize?

**YES, conceptually** — the correction required is now fully specified,
narrow, and well-evidenced (`bitemporal-verification.md`,
`revision-plan-v2.md`'s updated P0 items). Actual authorization to write
draft-v2 remains a separate, explicit human decision this task does not
make, per its own hard stop.
