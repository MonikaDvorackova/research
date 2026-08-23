---
id: note-contribution-02-experiment-perturbations
title: "Contribution 2 Experiment — Ground Truth and Perturbation Matrix"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, perturbations, ground-truth, case-matrix]
refs: [preservation-regimes.md, ../temporal-semantics.md]
---

## Ground Truth Specification

For every case, ground truth is authored **once**, before any regime's
artifacts are derived from it, and is never exposed to the reconstruction
procedure — it is used exclusively by the scoring rubric in
`metrics-and-scoring.md`. Ground truth for case *i* consists of:

```
GroundTruth_i {
  decision_id,
  t0,
  true_policy_version_id,     true_policy_valid_interval,
  true_authority_agent_id,    true_authority_valid_interval,
  true_evidence_values,
  true_model_version_id,
  true_watchlist_status_at_t0,
  true_computed_score,
  true_result (GRANT/DENY),
  true_justification  // one sentence: "score 0.41 < threshold 0.5 (policy v3,
                       //  valid from 2026-01-01), Approver was Agent-2
                       //  (valid from 2025-11-01), not on watchlist"
}
```

Each regime's artifact set (Regime A/B/C, per `preservation-regimes.md`) is
a strict, derived projection of this ground truth — the regimes never
introduce information the ground truth doesn't already fix, and no regime
is permitted to be internally inconsistent with it.

---

## Perturbation Matrix

Ten cases, chosen to isolate one failure class each before combining them,
per the brief's explicit instruction to avoid combinatorial explosion.
"Difficulty" is stated per regime as an a priori expectation, to be checked
against actual scoring once implemented — not asserted as a foregone
result.

| Case | t0 state | Perturbation (t0→t1) | Type | Expected difficulty | Why B and C might differ |
|---|---|---|---|---|---|
| **1. No-drift control** | Policy v1 (θ=0.5), Agent-1 is Approver, R not on watchlist | None — nothing changes before t1 | Control | All regimes should succeed | Sanity check only — if B or C fail here, the design (not the thesis) has a defect |
| **2. Isolated policy drift (forward)** | Policy v1 (θ=0.5) at t0 | Policy revised to v2 (θ=0.3) at t1, `valid_from` = t1 (a genuine, non-retroactive change) | Forward, non-retroactive | A fails (uses current v2); B and C should both succeed (as-of-t0 query is unambiguous when no retroactive correction exists) | Not expected to differ — this case establishes that B's bitemporal query is sufficient absent retroactive correction, isolating that variable for Case 3 |
| **3. Isolated policy drift (RETROACTIVE)** | Policy v1 (θ=0.5) at t0, decision-maker relied on v1 | At t1, a "correction" is recorded: v1bis (θ=0.45) with `valid_from` backdated to before t0, `recorded_at` = t1, on the theory that v1 was itself an error | **Retroactive** | A fails; **B is expected to fail** (as-of-t0 query now returns v1bis, contradicting what was actually consulted, without any signal that this occurred); **C should succeed** (its binding fixes the reference to whatever was authored at t0, which the ground truth guarantees was based on v1) | **This is the theoretically central case.** It directly tests the transaction-time/valid-time confound identified in `../temporal-semantics.md` and is the case most likely to distinguish B from C. |
| **4. Isolated authority drift** | Agent-1 is Approver at t0 | Approver role reassigned to Agent-2 at t1 (forward, non-retroactive) | Forward, non-retroactive | A fails; B and C both succeed | Structurally parallel to Case 2 — establishes B handles simple authority drift correctly, isolating retroactive authority drift as a distinct future test if extended |
| **5. Isolated evidence supersession** | R's evidence includes "prior incidents: 1" at t0 | The upstream incident record is later "expunged" (corrected) at t1, so a live query of R's profile at t1 shows "prior incidents: 0" | Supersession | A fails (uses current, corrected profile); B succeeds (evidence values were captured in the per-decision event trace at t0, not re-queried live); C succeeds identically to B | **Expected non-difference.** This case tests whether B's strong event-trace design (capturing raw values, not live re-queries) already handles evidence supersession correctly — if so, this confirms evidence capture at the moment of use is less binding-dependent than policy/authority version selection, sharpening exactly where the thesis's advantage is and is not expected to appear. |
| **6. Isolated context drift (watchlist)** | R not on watchlist at t0 | R added to watchlist at t1 | Forward, non-retroactive | A fails; B and C both succeed if watchlist history is bitemporal | Parallel to Cases 2/4 — establishes the baseline non-retroactive case for the context dimension |
| **7. Isolated model/config drift** | Scoring weights v1 at t0 | Weights recalibrated to v2 at t1 | Forward, non-retroactive | A fails; B and C both succeed | Establishes sub-problem B (execution) drift is well-handled by ordinary versioning in both B and C — expected non-difference, confirming the thesis is specifically about D/E (policy/authority), not B (execution) |
| **8. Combined drift (policy + authority, both retroactive)** | Policy v1, Agent-1 Approver at t0 | Both a retroactive policy correction (as Case 3) and a retroactive authority correction (Agent-1's assignment is later "found" to have actually ended before t0, backdated) occur before t1 | Combined, retroactive | A fails; **B expected to fail on both dimensions**; C expected to succeed on both | Tests whether the binding advantage compounds coherently across two simultaneously drifting dependencies, or whether cross-dependency interaction introduces new failure modes not visible in isolated cases |
| **9. Combined drift (all five dimensions, mixed forward/retroactive)** | Baseline t0 state | Policy retroactive correction (as Case 3) + authority forward reassignment (as Case 4) + evidence supersession (as Case 5) + watchlist forward change (as Case 6) + model forward drift (as Case 7), all before t1 | Stress case | A fails entirely; B expected to succeed on the forward-drift dimensions (authority, watchlist, model) and fail specifically on the retroactive policy dimension; C expected to succeed on all | The realistic worst-case scenario — confirms whether the isolated-case pattern (B fails only where retroactive/ambiguous, succeeds elsewhere) holds under combined, more realistic drift, or whether unanticipated interactions appear |
| **10. Concurrency/attribution ambiguity** | Two decisions, D_x (requester R_x) and D_y (requester R_y), occur within the same short window, immediately before a policy version boundary | No content drift — the policy genuinely changes exactly between the two decisions' timestamps, both close to the boundary | Attribution ambiguity | A fails; **B is expected to risk misattribution** (an as-of-timestamp query near a validity boundary, combined with clock/logging granularity, can plausibly attribute the wrong version to one of the two decisions); C is unaffected (each decision's binding is explicit and independent of the other's timing) | Tests the second failure mechanism named in `preservation-regimes.md`'s bitemporal answer (item 13) — interval-matching ambiguity under concurrency — distinct from, and not reducible to, the retroactive-correction mechanism tested in Case 3 |

---

## Design notes

- **Cases 2, 4, 6, 7 are deliberately constructed to be cases where B is
  expected to succeed**, not to fail. Their purpose is to prevent the
  experiment from being read as "B always loses" — if the theory in
  `../temporal-semantics.md` is right, B's failure should be **specific to**
  retroactive correction and concurrency ambiguity (Cases 3, 8, 9, 10), not
  general. Finding B succeeding on Cases 2/4/6/7 and failing only on
  3/8/9/10 would be the cleanest possible confirmation of the mechanism;
  finding B failing broadly and uniformly would suggest either a design
  flaw (B was accidentally weakened) or a broader, less precise version of
  the thesis than currently claimed.
- **No case introduces a perturbation type not already named in the
  brief's candidate list** (policy update, authority reassignment, model
  replacement, evidence supersession, context update) — the concurrency
  case (10) is an elaboration of "external dependency change" applied to
  the decision-attribution problem specifically, not a new perturbation
  category.
- **Ten cases is the deliberate ceiling for the first experiment.** Each
  isolates one mechanism (2, 4, 5, 6, 7), one tests the theoretically
  central mechanism directly (3), two test combinations (8, 9), one tests a
  second, distinct failure mechanism (10), and one is a pure control (1).
  This is judged sufficient to falsify or support H1 without combinatorial
  expansion; `implementation-spec.md` may add minor variations (e.g.,
  different numeric threshold values) without adding new structural cases.
