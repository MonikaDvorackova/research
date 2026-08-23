---
id: note-contribution-02-experiment-reconstruction-task
title: "Contribution 2 Experiment — Reconstruction Task and Investigator Choice"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, experiment-design, reconstruction-task, investigator]
refs: [preservation-regimes.md, perturbation-matrix.md]
---

## The Reconstruction Task

At t1, the investigator receives **only** the artifacts permitted by the
case's assigned regime (A, B, or C) — never ground truth, never artifacts
from another regime. It must answer eight standardized questions. Each
answer must be given in a **structured format**: either a specific,
concrete value, or the explicit token `UNDETERMINED`. Free-form prose is
not an acceptable substitute for any answer — this is deliberate (see
"Answer format discipline" below).

| # | Question | Answer type |
|---|---|---|
| 1 | What decision occurred? | `{decision_id, requester_id, result}` |
| 2 | Which evidence values supported it? | `{attribute: value, ...}` or `UNDETERMINED` |
| 3 | Which general rule/policy applied? | Free-text label (e.g., "threshold rule") — low-stakes, included mainly for completeness |
| 4 | Which **specific policy version** applied (with its valid-time interval)? | `{version_id, valid_from, valid_to}` or `UNDETERMINED` |
| 5 | Who/what had authority to approve? | `{agent_id, role}` or `UNDETERMINED` |
| 6 | Which **specific authority/role-assignment version** applied? | `{agent_id, valid_from, valid_to}` or `UNDETERMINED` |
| 7 | Was D authorized under the conditions valid at t0? | `GRANT` / `DENY` / `UNDETERMINED` |
| 8 | Why? (structured justification) | `{evidence_ref, policy_ref, authority_ref}` citing the specific values/versions used in the answer, or `UNDETERMINED` |

**Questions removed or added relative to the brief's list:** none removed;
none added as a separate numbered question. The brief's implicit ninth
concern — confidence — is deliberately **not** implemented as a
self-reported field (see below) but is instead derived structurally from
whether each answer is a concrete value or `UNDETERMINED`, combined with
its correctness against ground truth. This is discussed fully in
`metrics-and-scoring.md` under False Historical Confidence.

### Answer format discipline: why `UNDETERMINED` must be a first-class option

If the investigator is forced to always produce a concrete answer, it
becomes impossible to distinguish an **honest gap** (the regime's
information genuinely does not support a confident answer, and the
investigator correctly says so) from a **false-confidence failure** (the
regime's information looks sufficient but actually supports the wrong
answer, and the investigator asserts it anyway). This distinction is the
entire point of the False Historical Confidence metric and must be
structurally possible to produce, not left to chance free-form phrasing.

---

## Choice of Investigator: deterministic reconstruction procedure (primary), not human or LLM

**Decision: the first experiment uses a deterministic, rule-based
reconstruction algorithm, not a human or an LLM.** Three investigator types
were considered:

| Investigator type | Confounders introduced | Verdict |
|---|---|---|
| Human investigator | Domain knowledge, fatigue, inference skill, prior exposure to similar systems, variance across individuals | Rejected for the first experiment — introduces exactly the kind of confound the brief warns against ("test the information architecture, not human memory") |
| LLM-based investigator | Reasoning ability, prompt sensitivity, hallucination risk, training-data leakage about bitemporal reasoning patterns, non-determinism across runs | Rejected for the first experiment — conflates "does the information support reconstruction" with "can this particular model reason about the information," which is a different, legitimate, but separate question |
| **Deterministic / rule-based evaluator** | None of the above — the algorithm is fixed, fully specified in advance, and identical in its reasoning procedure across all cases and regimes (adapted only to the artifacts each regime actually provides) | **Selected** |

**Justification:** The research question (`research-question.md`) is about
whether the **information available** under each regime suffices for
correct reconstruction — not about whether a given reasoning agent is
skilled enough to extract it. A deterministic evaluator that implements the
objectively best-possible reconstruction procedure for each regime's
available data structure functions as an **upper bound** on what that
regime's information content can support. If even the best-possible fixed
algorithm fails under Regime B on the retroactive-correction case, this is
strong, uncontaminated evidence of an information-architecture gap — not a
reasoning failure that a smarter investigator might have avoided. Using a
human or LLM investigator first would leave any observed B-vs-C difference
ambiguous between "the information wasn't there" and "the investigator
didn't find it," exactly the confound the brief instructs to avoid.

**Per-regime deterministic procedure (specified fully in
`implementation-spec.md`; summarized here):**

- **Regime A:** Answer Questions 4 and 6 using whatever policy/authority
  values are currently live at t1 (there is no history to consult) — this
  is not an evasion but the only algorithmically possible behavior, and it
  is the behavior that produces Regime A's expected failures under drift.
- **Regime B:** For Questions 4 and 6, execute an as-of-t0 valid-time query
  against `PolicyVersions`/`AuthorityAssignments` (the best possible use of
  bitemporal history); for Question 2, read the raw evidence values from
  the per-decision event trace directly (no inference needed, since B's
  event trace captures these already). Answer `UNDETERMINED` only if the
  as-of-t0 query returns zero or more than one matching interval
  (a genuine, detectable ambiguity) — never guess.
- **Regime C:** For Questions 2, 4, and 6, read the referenced value or
  version directly from `DecisionBindingRecord` — no inference, no query
  ambiguity possible by construction.

**Secondary experiment (explicitly out of scope for this design, flagged
for later):** Once the deterministic-evaluator experiment has run and been
reviewed, a follow-up study substituting a human or LLM investigator could
test whether real-world investigators achieve the deterministic upper
bound in practice, or underperform it due to reasoning limitations. This is
not designed here and must not be conflated with the primary experiment's
results.
