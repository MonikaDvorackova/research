---
id: note-contribution-02-experiment-regimes
title: "Contribution 2 Experiment — The Three Preservation Regimes, Precisely"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, preservation-regimes, bitemporal, prov, event-sourcing]
refs: [experimental-system.md, ../prior-art-audit.md, ../temporal-semantics.md]
---

## Regime A — Bare

**Retained:** A single decision-outcome log entry per case:
`{decision_id, t0, requester_id, computed_score, result}`. Nothing else.

**Discarded:** All history of policy, authority, evidence, model, and
context. At t1, only the **current, live** values of policy threshold,
Approver assignment, and watchlist are queryable — there is no way to
distinguish "current" from "as it was at t0" because no historical record
of change exists at all.

**Realism check (not sabotage):** This matches a genuinely common,
unremarkable engineering pattern — an application log plus mutable
config/database rows with no history table, no registry, and no audit
trail beyond the outcome itself. It is not artificially crippled; it is
the default absence of any preservation discipline, which is exactly the
condition Regime A is defined to represent.

---

## Regime B — Versioned but unbound (the critical baseline)

**Retained**, all as complete, queryable histories:

- **PolicyVersions**: every policy version ever created, each with
  `{version_id, threshold_value, valid_from, valid_to, recorded_at}` —
  **fully bitemporal**, per the requirement (brief item 13) that Regime B
  must not be strawmanned as a system with poor temporal storage.
  `valid_from`/`valid_to` is the valid-time interval (when the threshold
  was the operative one in reality); `recorded_at` is the transaction time
  (when this row was written).
- **AuthorityAssignments**: every Approver-role assignment, bitemporally,
  as `{agent_id, role, valid_from, valid_to, recorded_at}`.
- **ModelVersions**: every scoring-function version, as
  `{version_id, weights, valid_from, valid_to}`.
- **ContextSnapshots**: watchlist membership history, as
  `{requester_id, on_watchlist, valid_from, valid_to}`.
- **A per-decision request/event trace** (the strong, event-sourced
  component of Regime B, per brief item 15): for every decision, an
  append-only event log entry capturing the **raw values actually read**
  at t0 — `{decision_id, t0, evidence_attributes_read, score_computed,
  threshold_value_read, approver_check_result, watchlist_check_result}`.
  This is what a well-instrumented, competently engineered tracing/logging
  system captures today: the values consulted, timestamped, causally
  linked to the request.

**What is deliberately absent, and only this:** none of the above records
— neither the version histories nor the per-decision event trace —
contains a **version identifier reference** connecting decision_id to a
specific `PolicyVersions.version_id`, `AuthorityAssignments` row, or
`ModelVersions.version_id`. The event trace records *that* the threshold
read was, say, `0.62` — a **value** — not *which policy version* produced
that value. Reconstructing "which version" requires a separate,
inferential step: querying `PolicyVersions` for the row whose
`[valid_from, valid_to)` interval contains t0, and hoping this query
returns a unique, correct answer.

**Why this is the strong, fair version of Regime B:** it is deliberately
*not* "a system with no temporal storage." It has complete bitemporal
history for every dependency and a complete causal event trace of every
value consulted. Its only limitation is the one property under test:
**the absence of an explicit, decision-time-authored reference from D to
the specific version identifiers that applied.**

---

## Regime C — Versioned and bound

**Retained:** Everything in Regime B, unchanged, **plus exactly one
additional artifact per decision**: a `DecisionBindingRecord`, authored
and persisted as part of the decision transaction itself, at t0:

```
DecisionBindingRecord {
  decision_id,
  policy_ref:    { version_id, valid_from, valid_to },
  authority_ref: { agent_id, role, valid_from, valid_to },
  model_ref:     { version_id },
  evidence_ref:  { snapshot_id -> the exact attribute values used },
  context_ref:   { watchlist_check_version_or_snapshot_id }
}
```

This record does not assert any new fact about the world — every value it
references already exists in Regime B's version histories. It asserts
exactly one new thing: **that these specific version identifiers, and no
others, are the ones that applied to this decision**, recorded at the
moment the decision was made rather than inferred afterward.

---

## B-vs-C information-equivalence table

| Information | In B? | In C? | Note |
|---|---|---|---|
| Full bitemporal policy version history | Yes | Yes | Identical in both |
| Full bitemporal authority version history | Yes | Yes | Identical in both |
| Full model version history | Yes | Yes | Identical in both |
| Full watchlist history | Yes | Yes | Identical in both |
| Raw evidence values consulted at t0 | Yes (via event trace) | Yes (via event trace) | Identical in both |
| Raw computed score at t0 | Yes | Yes | Identical in both |
| Final GRANT/DENY outcome | Yes | Yes | Identical in both |
| **Explicit version-identifier reference from D to the policy version applicable at t0** | **No** | **Yes** | The only addition |
| **Explicit version-identifier reference from D to the authority assignment applicable at t0** | **No** | **Yes** | The only addition |
| **Explicit version-identifier reference from D to the model version used** | **No** | **Yes** | The only addition |
| **Explicit reference from D to the exact evidence snapshot used** | **No** | **Yes** | The only addition |
| Any new underlying fact not already derivable from B | No | No | Confirmed: C adds zero new facts about the world |

**Redesign check (per brief item 5):** this table was constructed
specifically to verify that C does not contain materially more underlying
evidence than B. It does not. Every field in `DecisionBindingRecord` is a
reference into data that Regime B already retains in full. If this were
not the case — if, for example, C's evidence_ref pointed to attribute
values not present anywhere in B's event trace — the design would need to
be revised. It does not need revision.

---

## Direct address of the three strongest prior-art collisions

### Bitemporal prior art (brief item 13)

**Question:** Does temporal version history alone (Regime B, as designed
above — genuinely bitemporal, not a strawman) resolve which artifacts were
actually bound to D?

**Answer: No, not in general, for a specific and important reason beyond
"inference is merely inconvenient."** An as-of-t0 valid-time query against
`PolicyVersions` is only guaranteed to return the version the
decision-maker actually relied on when **no retroactive correction ever
occurs** and **no ambiguity in matching a decision's timestamp to an
interval arises**. Both conditions can fail:

1. **Retroactive correction breaks query stability.** If a policy
   correction is recorded at t1 with a backdated `valid_from` before t0, an
   as-of-t0 query run *after* t1 returns a different answer than the same
   query would have returned if run *before* t1 — even though the query
   itself ("what was valid at t0") never changed. The query's answer is
   only as stable as the transaction-time history behind it, and Regime B
   has no way to distinguish "the version I am now being told was valid at
   t0" from "the version that was actually consulted at t0" once these two
   diverge. An explicit binding, authored at t0 and never subsequently
   alterable, does not have this instability by construction — it is fixed
   at the moment of decision, independent of any later correction to the
   historical record.
2. **Interval-matching ambiguity under concurrency.** If two decisions
   occur close enough in time that timestamp-based as-of queries could
   plausibly attribute either to a transitional version near a validity
   boundary, an inferential reconstruction has no way to resolve the
   ambiguity that an explicit per-decision reference resolves trivially.

**If the answer had been "yes, bitemporal history alone resolves it,"**
this would directly weaken the contribution — this is precisely why the
brief requires testing it head-on rather than assuming the conclusion, and
why the experiment (`perturbation-matrix.md`, Cases 3 and 10) is built
specifically to surface exactly these two failure conditions.

### W3C PROV (brief item 14)

**Question:** Is Regime C simply W3C PROV used correctly?

**Answer: Largely yes, and this should be stated plainly rather than
obscured.** `DecisionBindingRecord` is structurally isomorphic to a PROV
graph: D is an Activity; the evidence snapshot, policy version, authority
assignment, and model version are Entities; the record's references are
Usage relations (D used these Entities); the approving agent's role is an
Association/Delegation. If PROV's Entities are extended with the
valid-time attributes Regime B's bitemporal stores already carry, and PROV
is populated **at generation time** rather than reconstructed later, the
result is exactly Regime C. **This experiment does not claim C is a new
representational formalism.** It claims, and is designed to test, that the
specific discipline of populating this structure **at decision time,
referencing specific version identifiers rather than raw values** — a
discipline `../prior-art-audit.md` found is not what PROV's specification
requires or what typical instrumentation practice does by default — is
what produces measurably different reconstruction outcomes under drift.

### Event sourcing (brief item 15)

**Question:** If every relevant event is recorded and causal links are
explicit, does B collapse into C?

**Answer: Yes, exactly at the point where the event log stops recording
raw values and starts recording version identifiers — and this
collapse is the single most important, most honest finding this design
surfaces before any case is run.** Regime B's event trace is already a
strong, causally-linked, append-only record — a genuine event-sourcing
implementation. It fails to be equivalent to Regime C for one precise
reason: it captures **values** (`threshold_value_read: 0.62`) rather than
**version identifiers** (`policy_version_id: v7, valid 2026-01-01 to
present`). If a future revision of Regime B's event trace captured version
identifiers instead of, or in addition to, raw values at the moment of
consultation, **B and C would become definitionally identical** — "explicit
causal event recording of version identifiers at consultation time" and
"explicit decision-time binding" are two descriptions of the same
discipline. This experiment does not claim event sourcing is
insufficient in principle. It claims that **capturing values without
capturing the version identifiers that produced them — which is what most
real tracing/logging practice actually does, per the OpenTelemetry
findings in `../prior-art-audit.md`, where span attributes are
undifferentiated key-value pairs — is the specific, narrow, easy-to-miss
omission this contribution identifies**, and Regime B is deliberately
constructed to embody exactly that omission, and nothing more.

**Consequence for how results should be read:** if the experiment confirms
H1, the honest interpretation is not "a new mechanism was needed" — it is
"the discipline of capturing version identifiers rather than values, at
decision time, is empirically consequential and is not what default
engineering practice (including good event sourcing and good bitemporal
storage) does automatically." This is the precise, narrow claim
`../novelty-verdict.md`'s Verdict B already commits to; the experiment is
designed to test whether that claim has empirical teeth, not to
manufacture a broader one.
