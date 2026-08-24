---
id: note-contribution-02-article-review-bitemporal-verification
title: "Contribution 2 Article — Bitemporal Finding Verification"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-02, article, review, verification, bitemporal]
refs: [reviewer-report.md, ../../experiment/src/reconstruction.py, ../../experiment/src/cases.py]
---

## Purpose

`reviewer-report.md`'s headline finding claimed that a transaction-time-
anchored bitemporal query, using only information already retained by
Regime B, could avoid the primary experiment's retroactive-correction
failure. This document verifies that claim **against the actual
implementation and fixtures**, not against the abstract design
description, per this task's explicit instruction not to reason from
prose alone.

**Result, stated up front: the claim, as literally stated, is
REJECTED for the system as actually implemented and executed** — the
specific fact a transaction-time-anchored query would need was not, in
fact, retained. A different, narrower, and partially-valid finding
survives in its place (see Section 6).

---

## 1. What Regime B retains — inspected directly, not from prose

Verified against `experiment/src/domain.py` (schema) and
`experiment/src/cases.py` (fixture construction), by direct Python
inspection of the actual constructed `World` objects for Cases 3, 8, 9
(not by reading `preservation-regimes.md`'s prose description of what
Regime B is *intended* to be).

| Information | Available to B? | Precision | Used by investigator (`reconstruction.py`)? |
|---|---|---|---|
| Policy valid-time interval (`valid_from`/`valid_to`) | Yes | Exact | Yes — sole basis for policy resolution |
| Policy transaction time (`recorded_at`) | **Yes as a schema field, but see Section 2 — its value is overwritten on correction, destroying the pre-correction fact** | Exact, but factually stale after correction | Read, but never bounded by `t0` (compares rows to each other only) |
| Authority valid-time interval | Yes | Exact | Yes |
| Authority transaction time (`recorded_at`) | Same caveat as policy | Same caveat | Same as policy |
| Model version history (`valid_from`/`valid_to`) | Yes | Exact | Yes |
| Model transaction time | **No such field exists in the schema** (`ModelVersion` has no `recorded_at`, confirmed in `domain.py`) | N/A | N/A |
| Decision timestamp (`t0`) | Yes, in every regime's `DecisionOutcomeLog`/view | Exact | Yes — the valid-time query point |
| Raw evidence values read at t0 (`DecisionEventTrace.evidence_attributes_read`) | Yes | Exact, immutable, authored at t0 | Yes — used directly for evidence |
| **Raw policy threshold value read at t0** (`DecisionEventTrace.threshold_value_read`) | **Yes, immutable, authored at t0, unaffected by later correction** | Exact | **No — never read by `_reconstruct_b`** |
| Raw approver-check result at t0 (`DecisionEventTrace.approver_check_result`) | Yes, boolean only | Exact but **not an identity** (no agent ID captured) | Yes, but only as a boolean gate, never for identity disambiguation |
| Any direct decision → specific-version reference | **No** (that is exactly Regime C's one addition) | — | — |
| Event/row ordering beyond valid-time and (nominal) transaction-time fields | No separate ordering mechanism | — | — |

**Key finding from this table alone:** Regime B's schema *does* include a
transaction-time field for policy and authority (`recorded_at`), matching
the design's stated bitemporal intent. Whether that field actually
*preserves* pre-correction transaction-time information, however, is a
fixture-construction question, answered in Section 2 — not something
determinable from the schema or design prose alone.

---

## 2. Reconstructing Cases 3, 8, 9 exactly — from live fixture inspection

Directly executed `experiment/src/cases.py`'s case builders and printed
the resulting `World` objects (not estimated, not read from documentation)
to obtain the following, for all three cases:

```
t0 = 2026-03-01T00:00:00
query_time (t1) = 2026-05-01T00:00:00  (= RETRO_RECORDED_AT)

Case 3 / Case 8 / Case 9 policy_history (identical across all three):
  PolicyVersion(version_id='v1',    threshold=0.50, valid_from=2026-01-01,
                 valid_to=2026-02-01, recorded_at=2026-05-01)
  PolicyVersion(version_id='v1bis', threshold=0.45, valid_from=2026-02-01,
                 valid_to=None,       recorded_at=2026-05-01)

Case 8 authority_history:
  AuthorityAssignment(agent_id='Agent-1', valid_from=2025-11-01,
                       valid_to=2026-02-15, recorded_at=2026-05-01)
  AuthorityAssignment(agent_id='Agent-3', valid_from=2026-02-15,
                       valid_to=None,       recorded_at=2026-05-01)

Case 3 / Case 8 / Case 9 event_trace.threshold_value_read = 0.50
Case 3 / Case 8 / Case 9 event_trace.approver_check_result = True
                          (no agent identity captured)

Ground truth (all three): true_policy_version_id='v1',
                           true_authority_agent_id='Agent-1'
```

**The decisive fact:** in every one of the three cases, **both retained
policy rows carry the identical `recorded_at = 2026-05-01`** — the
correction's own transaction time. The original row's true transaction
time (`2026-01-01`, when policy v1 was actually first recorded, well
before t0) does not appear anywhere in the final, retained `policy_history`.
The same holds for Case 8's authority rows (original `recorded_at =
2025-11-01` does not survive; both final rows read `2026-05-01`).

**Why:** `experiment/src/cases.py::_close_and_append` (lines ~216–245)
implements "closing" a superseded row by **slicing the original row out
of the list and replacing it with a new row object that shares the
original's `valid_from` but is assigned the *closing* operation's
`recorded_at`, not the original's**:

```python
old = history[index]
closed = PolicyVersion(old.version_id, old.threshold, old.valid_from,
                        closed_valid_to, closed_recorded_at)   # <-- new recorded_at, not old.recorded_at
...
return history[:index] + history[index + 1:] + [closed, new_row]
```

This is a genuine implementation property, confirmed by direct execution,
not an inference from the surrounding comment. The surrounding comment in
the code (written during the original implementation session) states this
"never changes any query result" — true only for the specific algorithm
that was in fact implemented (which never bounds its transaction-time
comparison by `t0` — see Section 3), not true in general.

### A. Information absent from B, vs. B. information present but unused

Per this task's required distinction:

- **Policy dimension, Cases 3/9:** **borderline — see Section 5's escape
  hatch.** The *version-identity* fact ("v1 was recorded at 2026-01-01,
  before t0") is genuinely **absent (Category A)** from the retained
  `policy_history`. However, the *value* that was actually read at t0
  (`threshold_value_read = 0.50`) **is present and unused (Category B)**
  by the tested algorithm — and, in this specific fixture, that value
  happens to uniquely identify "v1" among the two retained policy rows
  (0.50 vs. 0.45). This is a real escape hatch, but a narrow and
  fixture-specific one (Section 5).
- **Authority dimension, Case 8:** **Category A, cleanly, with no escape
  hatch.** The version-identity fact is absent from `authority_history`
  for the same reason as policy. Unlike policy, no analogous raw *value*
  exists in the retained data that could disambiguate "Agent-1" from
  "Agent-3" — `DecisionEventTrace.approver_check_result` is a boolean
  ("an approver existed"), never an identity. There is no information in
  Regime B, used or unused, that resolves this.

---

## 3. Semantic counterfactual, derived (not assumed) first

**The question:** at t1, given only what Regime B retains, could an
investigator issue the logical equivalent of "which record was visible to
the system at transaction time t0, and valid for valid-time t0?"

**Derivation:** such a query requires, for each identity, selecting the
row with the **greatest `recorded_at` not exceeding t0**, then checking
valid-time containment. Semantically: `argmax_{row.recorded_at <= t0}
(row.recorded_at)`, filtered by `row.valid_from <= t0 < row.valid_to`.

**Applying this to the actual Case 3 data:** for identity `v1`, the only
retained row has `recorded_at = 2026-05-01`, which is **not** `<= t0
(2026-03-01)`. For identity `v1bis`, same: `recorded_at = 2026-05-01 >
t0`. **No row satisfies `recorded_at <= t0` for either identity.** The
semantically-derived query returns **the empty set — not "v1," not
"v1bis," nothing** — which would score as `UNDETERMINED`, not as a
correct answer.

**Conclusion: NO.** Given only the information Regime B actually retains
in this implementation, an investigator cannot issue a transaction-time-
anchored query that resolves to the correct answer, because the fact such
a query needs (the original row's true, pre-correction `recorded_at`) was
not retained. `reviewer-report.md`'s specific counterfactual is
**semantically well-formed but empirically inapplicable to this fixture.**

---

## 4. Primary-source verification

Live-searched and fetched during this verification (not sourced from
memory or unverified prior claims):

- **SQL:2011's system-versioning model exists and defines `FOR SYSTEM_TIME
  AS OF <datetime>`**, confirmed via web search returning consistent
  descriptions across MariaDB, Microsoft, and general references: "System-
  versioned tables were first introduced in the SQL:2011 standard... SQL:2011
  provides three syntactic extensions: AS OF is used to see the table as it
  was at a specific point in time in the past."
- **Microsoft Learn, "Query Data in a System-Versioned Temporal Table"**
  (SQL Server documentation implementing the SQL:2011 model),
  <https://learn.microsoft.com/en-us/sql/relational-databases/tables/querying-data-in-a-system-versioned-temporal-table>,
  fetched directly in this session: *"Use the `AS OF` subclause to
  reconstruct the state of data as it was at any specific time in the
  past."*
- **The decisive cross-check, confirmed by direct fetch of MariaDB's
  documentation**, <https://mariadb.com/docs/server/reference/sql-structure/temporal-tables/system-versioned-tables>:
  *"When an `UPDATE` statement modifies a row in a system-versioned table,
  the server writes a new history row capturing the previous state of the
  row. The original row's `ROW_START` timestamp remains fixed in the
  historical record. Instead of modifying that timestamp, the system
  creates a new history entry with the current timestamp and sets the
  original row's `ROW_END` to the current time... The new current row
  then receives a fresh `ROW_START` value."*

**This is the decisive, citable fact:** a genuine SQL:2011-conformant
system-versioned table **never overwrites a superseded row's original
start-of-validity system time** — only its end-of-validity system time is
set, and the original start time is permanently preserved in the history
table by construction. **This experiment's `_close_and_append` does the
opposite for its `recorded_at` field: it reassigns the closed row's
transaction time to the closing operation's own time, discarding the
original.** This is a genuine, citable, and material divergence between
this experiment's Regime B implementation and the bitemporal storage
discipline `preservation-regimes.md` (the design document) explicitly
claims Regime B embodies ("genuinely bitemporal... never mutates or
removes the original row").

**Remaining verification gap:** none identified for the specific claim
checked (system-versioned tables preserve original start times) — two
independent, authoritative vendor sources agree, both implementing the
same SQL:2011 model. A full read of the ISO/IEC 9075-2:2011 standard text
itself was not performed (paywalled primary text); the vendor
documentation is treated as authoritative secondary confirmation of
publicly-summarized standard behavior, consistent with how
`../../prior-art-audit.md` itself cites SQL:2011 via secondary sources
(Kulkarni & Michels 2012) rather than the paywalled standard text.

---

## 5. Question A vs. Question B

- **Question A:** "What did the database/system record say at t0?"
- **Question B:** "What did decision D actually consume at t0?"

In **this specific synthetic testbed**, Question A and Question B are
equal by construction: ground truth is built by reading the live,
"current-as-of-t0" values directly (`experiment/src/cases.py::_build_ground_truth`,
called before any perturbation is applied), and no caching, replication
lag, or concurrent-writer scenario is modeled anywhere in this
experiment. **None of the five caveats this task lists (D used state
visible at exactly that timestamp; sufficient precision; no concurrent
ambiguity; the queried system was the actual source; no caching/
replication lag) is violated in this testbed — all five hold trivially by
construction.** This means: *if* a transaction-time-anchored query
against Regime B's data had correctly answered Question A for this
testbed, it would also have correctly answered Question B. The reason it
does not is not a Question-A-vs-B gap — it is that **Regime B, as
implemented, does not correctly answer Question A either**, because the
fact needed to answer it was not retained (Section 2).

---

## 6. The escape hatch, precisely bounded

Section 2 identified that `DecisionEventTrace.threshold_value_read =
0.50` is retained, immutable, and — in this fixture's specific numbers —
uniquely matches only the "v1" policy row (`threshold = 0.50`) among the
two retained rows (the other, "v1bis," has `threshold = 0.45`). An
investigator algorithm that cross-referenced this raw captured value
against *every* retained policy row's `threshold` field (not just the
valid-time-matching one) could, in this specific instance, uniquely
identify "v1" — using only information Regime B already retains, no
binding required.

**This is real, but narrow, in three specific ways:**

1. **It is a value-triangulation heuristic, not transaction-time
   reasoning.** It has nothing to do with the `SYSTEM_TIME AS OF`
   mechanism `reviewer-report.md` proposed — that mechanism is rejected
   (Sections 2–3). This is a structurally different mechanism: cross-
   checking a captured observation against a set of candidate historical
   records by value.
2. **It is not guaranteed to work in general.** It succeeds here only
   because v1's and v1bis's threshold values happen to differ (0.50 vs.
   0.45). Two policy versions with the same threshold value (a
   realistic, unremarkable administrative pattern — e.g., a purely
   procedural backdating that changes nothing substantive) would make
   this heuristic ambiguous or wrong, and no test in this matrix probes
   that boundary case.
3. **It does not generalize to the authority dimension.** `Case 8`'s
   authority failure has no analogous raw-identity field to triangulate
   against (`approver_check_result` is a boolean, not an agent ID) — the
   escape hatch closes entirely for Case 8's authority dimension. Case 8
   remains clean Category A evidence regardless of this finding.

**Where this escape hatch is directionally consistent with existing
programme findings:** it is a second, independently-discovered instance
of the same pattern F10-6 already demonstrated deliberately — an
*ordinary, unlabeled, already-retained signal* (here: a captured
evidence value; there: a causal consumption event) resolving what a
version-identity-only query cannot. It was not designed into the primary
experiment on purpose (unlike F10-6, which was a deliberate negative
control); its presence here is coincidental to this fixture's specific
numbers, not a designed test of the same idea. This distinction matters
for how much weight the finding can bear (see `BITEMPORAL-VERDICT.md`).

---

## Summary

| Case | Retains needed fact? | Escape hatch via retained value? | Classification |
|---|---|---|---|
| 3 (policy only) | No (Category A for version-identity) | **Yes** (threshold value 0.50 uniquely matches v1) | **B** (algorithm-limited; a value-cross-referencing algorithm recovers it from Regime B's own data) |
| 8 (policy + authority) | No | Policy: yes. Authority: **no** — no escape hatch | **A** (authority dimension is a clean, undiminished information gap; dominates this case's TC=0 result) |
| 9 (policy retroactive + authority forward) | No (policy only; authority already resolves correctly via forward-drift logic) | **Yes** (same as Case 3) | **B** (algorithm-limited, same mechanism as Case 3) |
