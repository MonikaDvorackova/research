---
id: note-contribution-02-experiment-implementation-spec
title: "Contribution 2 Experiment — Implementation Specification (Design Only, No Code)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, implementation-spec]
refs: [preservation-regimes.md, perturbation-matrix.md, reconstruction-task.md, metrics-and-scoring.md]
---

## Purpose and Boundary

This document specifies the experiment precisely enough to implement in a
later session **without reopening any conceptual design decision**. It
contains data schemas, concrete case parameters, and algorithm
descriptions in structured prose/pseudocode. **It contains no executable
source code and no programming-language syntax**, consistent with this
phase's explicit restriction against implementation or execution.

---

## 1. Data schemas (language-neutral)

```
PolicyVersion:       { version_id, threshold, valid_from, valid_to, recorded_at }
AuthorityAssignment: { agent_id, role, valid_from, valid_to, recorded_at }
ModelVersion:        { version_id, weights, valid_from, valid_to }
WatchlistEntry:      { requester_id, on_watchlist, valid_from, valid_to }
DecisionEventTrace:  { decision_id, t0, evidence_attributes_read,
                        score_computed, threshold_value_read,
                        approver_check_result, watchlist_check_result }
DecisionBindingRecord (Regime C only):
                     { decision_id, policy_ref{version_id,valid_from,valid_to},
                       authority_ref{agent_id,valid_from,valid_to},
                       model_ref{version_id},
                       evidence_ref{snapshot_id, values},
                       context_ref{snapshot_id} }
DecisionOutcomeLog (all regimes):
                     { decision_id, t0, requester_id, computed_score, result }
GroundTruth:         { decision_id, t0, true_policy_version_id,
                        true_policy_valid_interval, true_authority_agent_id,
                        true_authority_valid_interval, true_evidence_values,
                        true_model_version_id, true_watchlist_status_at_t0,
                        true_computed_score, true_result, true_justification }
```

`valid_to = null` denotes "still valid as of the latest known state."
`recorded_at` is present only on bitemporal tables (PolicyVersion,
AuthorityAssignment) per `preservation-regimes.md`.

---

## 2. Decision rule (fixed, deterministic)

```
score = w1*evidence.account_age_norm + w2*evidence.prior_incidents_norm
        (weights w1, w2 defined by the active ModelVersion)

result = GRANT  if score < policy.threshold
                AND an agent held role="Approver" at t0
                AND requester NOT on watchlist at t0
         DENY   otherwise
```

Two evidence attributes are sufficient (`account_age_norm`,
`prior_incidents_norm`, each normalized to [0,1]) — no further attributes
are needed per `experimental-system.md`'s minimality requirement.

---

## 3. Case parameter table (concrete values for all 10 cases)

| Case | t0 (illustrative) | Policy at t0 | Approver at t0 | Evidence at t0 | Watchlist at t0 | Model at t0 | True result | Perturbation (recorded at t1) |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-03-01 | v1: θ=0.50, valid 2026-01-01→∞ | Agent-1, valid 2025-11-01→∞ | age=0.3, incidents=0.2 | not listed | m1 | score=0.41 → GRANT | none |
| 2 | 2026-03-01 | v1: θ=0.50 (as above) | Agent-1 (as above) | age=0.3, incidents=0.2 | not listed | m1 | GRANT | v2: θ=0.30, valid_from=2026-04-01 (forward, non-retroactive) |
| 3 | 2026-03-01 | v1: θ=0.50 (as above) | Agent-1 (as above) | age=0.3, incidents=0.2 | not listed | m1 | GRANT | v1bis: θ=0.45, valid_from **backdated to 2026-02-01** (before t0), recorded_at=2026-05-01 |
| 4 | 2026-03-01 | v1: θ=0.50 | Agent-1, valid 2025-11-01→∞ | age=0.3, incidents=0.2 | not listed | m1 | GRANT | Agent-2 becomes Approver, valid_from=2026-04-01 (forward) |
| 5 | 2026-03-01 | v1: θ=0.50 | Agent-1 | age=0.3, **incidents=0.4** | not listed | m1 | score=0.47 → GRANT | Upstream incident record corrected; live profile at t1 shows incidents=0.0 |
| 6 | 2026-03-01 | v1: θ=0.50 | Agent-1 | age=0.3, incidents=0.2 | **not listed** | m1 | GRANT | Requester added to watchlist, valid_from=2026-04-01 (forward) |
| 7 | 2026-03-01 | v1: θ=0.50 | Agent-1 | age=0.3, incidents=0.2 | not listed | m1: w1=0.5,w2=0.5 | GRANT | m2: w1=0.2,w2=0.8, valid_from=2026-04-01 (forward) |
| 8 | 2026-03-01 | v1: θ=0.50 | Agent-1 | age=0.3, incidents=0.2 | not listed | m1 | GRANT | Policy retroactive correction (as Case 3) **and** Agent-1's assignment retroactively corrected to have ended 2026-02-15 (before t0), Agent-3 retroactively inserted as the "true" holder |
| 9 | 2026-03-01 | v1: θ=0.50 | Agent-1 | age=0.3, incidents=0.4 | not listed | m1: w1=0.5,w2=0.5 | GRANT | Combined: policy retroactive (as Case 3) + authority forward reassignment (as Case 4) + evidence supersession (as Case 5) + watchlist forward addition (as Case 6) + model forward drift (as Case 7) |
| 10 | D_x at 2026-03-01T11:59:00; D_y at 2026-03-01T12:01:00 | v1: θ=0.50 valid until 2026-03-01T12:00:00; v2: θ=0.30 valid from 2026-03-01T12:00:00 | Agent-1 | Two distinct requesters, each age=0.3/incidents=0.2 | not listed | m1 | D_x: GRANT (under v1); D_y: DENY (under v2) | None beyond the pre-planned policy boundary — the test is attribution, not further drift |

All numeric values above are illustrative placeholders sufficient to
fully specify each case's ground truth; the implementer may substitute
any concrete values that preserve each case's structural property (e.g.,
"score crosses the threshold under the old policy but not the new one" for
Case 2), without needing to revisit this design.

---

## 4. Per-regime artifact derivation (from a case's ground truth)

- **Regime A:** Emit only `DecisionOutcomeLog` for the decision. At t1,
  the "live" policy/authority/watchlist/model tables reflect only their
  **post-perturbation** values (Regime A retains no history, so whatever
  is live at query time is all that exists).
- **Regime B:** Emit `DecisionOutcomeLog`, `DecisionEventTrace` (with the
  raw values read at t0), plus full `PolicyVersion`/`AuthorityAssignment`/
  `ModelVersion`/`WatchlistEntry` histories reflecting both the t0 state
  and the t1 perturbation as separate, retained rows (never overwritten).
- **Regime C:** Everything in Regime B, plus one `DecisionBindingRecord`
  per decision, populated with the version identifiers that were true at
  t0 per that case's ground truth (i.e., authored using ground truth,
  before any t1 perturbation is applied — reflecting that the binding is
  created at decision time, not retrofitted).

---

## 5. Deterministic reconstruction algorithm (per regime)

```
FUNCTION reconstruct(regime, decision_id, t0):

  IF regime == A:
    outcome  = lookup(DecisionOutcomeLog, decision_id)
    policy   = current_live(PolicyVersion)          # only option available
    auth     = current_live(AuthorityAssignment)     # only option available
    evidence = UNDETERMINED                          # no per-decision trace exists
    RETURN answers_from(outcome, policy, auth, evidence)

  IF regime == B:
    outcome  = lookup(DecisionOutcomeLog, decision_id)
    trace    = lookup(DecisionEventTrace, decision_id)
    evidence = trace.evidence_attributes_read         # directly available
    policy_matches = query(PolicyVersion,
                            WHERE valid_from <= t0 AND (valid_to IS NULL OR valid_to > t0))
    auth_matches   = query(AuthorityAssignment,
                            WHERE valid_from <= t0 AND (valid_to IS NULL OR valid_to > t0)
                            AND role == "Approver")
    IF count(policy_matches) != 1: policy = UNDETERMINED  ELSE policy = policy_matches[0]
    IF count(auth_matches)   != 1: auth   = UNDETERMINED  ELSE auth   = auth_matches[0]
    RETURN answers_from(outcome, policy, auth, evidence)

  IF regime == C:
    outcome = lookup(DecisionOutcomeLog, decision_id)
    binding = lookup(DecisionBindingRecord, decision_id)
    policy  = lookup(PolicyVersion, binding.policy_ref.version_id)
    auth    = lookup(AuthorityAssignment, binding.authority_ref.agent_id)
    evidence = binding.evidence_ref.values
    RETURN answers_from(outcome, policy, auth, evidence)
```

`answers_from(...)` deterministically populates the eight structured
answers (`reconstruction-task.md`) from whichever of `outcome`, `policy`,
`auth`, `evidence` were resolved (or `UNDETERMINED`), and computes Q7
(authorized?) by re-applying the decision rule (Section 2) using whatever
values were resolved — if any required value is `UNDETERMINED`, Q7 is also
`UNDETERMINED`, never guessed.

**Note on Regime B's ambiguity handling:** the `count(...) != 1` check is
the specific, deliberate mechanism by which Case 10 (concurrency) can
produce either an `UNDETERMINED` answer (if the implementation detects the
ambiguity, e.g., via timestamp granularity or boundary-adjacency checks)
or a wrong-but-confident answer (if it does not) — **which of these two
behaviors Regime B's algorithm exhibits on Case 10 is itself part of what
the experiment measures**, not something to be decided in advance by this
spec. The as-of-t0 query as written above will, in fact, deterministically
resolve to exactly one match in Case 10 as long as `valid_to` for v1 is
recorded as strictly less than or equal to D_y's t0 and D_x's t0 is
strictly before that boundary — meaning the real risk in Case 10 is not
query-logic ambiguity but **clock/timestamp-recording granularity in a
real system** (i.e., whether the decision's own recorded t0 is precise
enough relative to the policy boundary). The implementer must decide, at
build time, whether to model this as a genuine boundary-precision fault
injected into Case 10, or whether Case 10 should be reduced to a
documented limitation of this synthetic design (see
`validity-and-confounders.md`) rather than a live test — flagged here as
an open implementation decision, not resolved by this design.

---

## 6. Scoring implementation

For each of the 8 answers, compare against `GroundTruth` per
`metrics-and-scoring.md`'s definitions. Aggregate AIA/TC/AC/JC/FHC per
case, then group by perturbation category (control / forward-drift /
retroactive-drift / combined-drift / concurrency) as defined in
`perturbation-matrix.md`, and report both the per-category table and the
manipulation check (`validity-and-confounders.md`) before any H1/H0
conclusion is drawn.

---

## 7. What remains genuinely open for the implementer

- Whether Case 10's boundary-precision question (Section 5 note) is
  modeled as a fault-injection case or documented as a limitation.
- The exact numeric evidence-weight values (placeholders given in Section
  3 are sufficient but arbitrary).
- The concrete storage technology used to realize the schemas in Section 1
  (any language/database capable of expressing bitemporal queries and
  immutable records suffices; no specific technology is mandated by this
  design).

Nothing else requires returning to `problem-formalization.md`,
`prior-art-audit.md`, `collision-tests.md`, or `temporal-semantics.md` —
this specification, together with the rest of `experiment-design/`, is
intended to be sufficient on its own for implementation.
