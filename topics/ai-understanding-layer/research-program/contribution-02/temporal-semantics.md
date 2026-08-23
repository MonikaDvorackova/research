---
id: note-contribution-02-temporal-semantics
title: "Contribution 2 — Temporal Semantics of the Reconstruction Problem"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, temporal-semantics, bitemporal]
refs: [problem-formalization.md, prior-art-audit.md]
---

## Contribution 2 — Temporal Semantics

Scope: Task 7. Determines whether Contribution 2 is fundamentally a
temporal-information problem, using the vocabulary already standardized in
bitemporal database theory (Snodgrass; SQL:2011) rather than inventing new
terms where existing ones apply.

---

## Is this fundamentally a temporal-information problem?

**Largely yes, for sub-problems D and E; only partly for C; not primarily
for G.** The audit in `prior-art-audit.md` (Objection 4) found that
bitemporal database theory already supplies complete, decades-old semantics
for "what was true, and what was recorded as true, at any point in the
past" — for anything actually modeled that way. Sub-problems D (policy) and
E (authority) are, structurally, exactly the kind of fact bitemporal
modeling was built for: a policy or a role assignment has a period during
which it was the operative one (valid time), independent of when someone
recorded that it would be the operative one (transaction time).

Sub-problem C (evidence) is only partially temporal: whether a retrieved
document was *available* at t0 is a valid-time question, but whether it was
an *accurate* representation of ground truth is a separate, non-temporal
adequacy question that bitemporal modeling does not address. Sub-problem G
(justification) is not primarily temporal at all — it is a normative
synthesis question that presupposes the temporal bindings from C/D/E are
already resolved.

**Necessary temporal concepts, tested against the brief's list:**

| Concept | Needed? | Role |
|---|---|---|
| **Valid time** | Yes | When a policy, evidence item, or authority assignment was true/operative in the modeled reality — independent of when it was recorded. This is the concept the audit found most consistently missing from AI-relevant stores (prompt stores, retrieval corpora, policy-as-config). |
| **Transaction time** | Yes | When a fact was recorded in the system. Needed alongside valid time specifically to detect and represent *retroactive* corrections (a policy is recorded today as having been in effect starting last month) — a real and common pattern in policy administration that a valid-time-only model cannot represent. |
| **Decision time** | Yes, and this is not identical to either of the above | The instant D was made — the reference point against which valid-time slices of policy/evidence/authority must be evaluated. Decision time is the *query point* for a bitemporal lookup, not itself a property of the things being queried. |
| **Observation time** | Conditionally | Relevant specifically for sub-problem C when evidence is itself an observation (a sensor reading, a retrieval result) whose own valid-time and observation-time can diverge — e.g., a document retrieved at decision time may describe a fact true as of an earlier observation. Needed only where evidence has this two-layer structure; not universal. |
| **Policy-effective interval** | Yes | The valid-time interval specifically for policy objects — named separately from generic "valid time" only because policy administration commonly involves scheduled future effective dates and retroactive corrections, both of which stress-test the transaction-time/valid-time distinction more than most other data. |
| **Evidence-validity interval** | Yes, but incompletely solved by temporal modeling alone | The period during which a piece of evidence was an accurate representation of the state of the world it claimed to describe. Bitemporal modeling can represent the interval *if someone declares it*; it cannot determine that interval from the evidence itself — this remains a domain-specific, not a temporal-database, problem. |
| **Authority-validity interval** | Yes | The period during which a given role/delegation assignment was in force — structurally identical to policy-effective interval, but tracked as a separate record because policy and authority can each change independently of the other (a rule can change while the same person retains authority to apply it, or a rule can stay fixed while authority is reassigned). |

---

## Can a system preserve every artifact and still reconstruct the past incorrectly?

**Yes — and this is the central positive finding of this section.** A
system can retain the full historical version sequence of its policy
document, its retrieval corpus, and its authority/role assignments — nothing
is deleted, nothing is overwritten without a new version being created — and
still reconstruct the past **incorrectly** at t1, for a reason that has
nothing to do with data loss:

**If the decision record does not pin which valid-time slice of each
dependency applied at t0, a later query naturally defaults to "whatever
version is current as of decision time" — which is correct only by
accident.** Concretely: suppose policy P was recorded (transaction time)
last week as having been effective (valid time) starting three months ago —
a retroactive correction, which is common and legitimate in policy
administration (a compliance team discovers an interpretation error and
backdates the correct reading). An investigator at t1 querying "what was
policy P as of t0" using only valid-time semantics will get the
*corrected* answer, which may not be what the decision-maker at t0 actually
saw or relied upon — the decision-maker's own transaction-time view of the
world at t0 is a third, distinct fact from either the pre-correction or
post-correction valid-time record. **Full artifact preservation, including
full bitemporal history, is not sufficient — the system also needs to know,
and record, which of potentially several different "as of t0" answers is
the one relevant to what the decision-maker actually saw**, which is
precisely the binding problem identified in `collision-tests.md` Objection
8. Bitemporal completeness solves the query "what does our best current
understanding say was true at t0" — it does not by itself solve "what did
the decision-maker actually rely on at t0," which can diverge from that
query's answer whenever retroactive correction occurs.

This establishes, precisely: **temporal completeness of the underlying data
is necessary but not sufficient for reconstruction; an explicit
decision-time binding — recorded at t0, not inferred later — is also
required**, and no amount of retroactive bitemporal querying can substitute
for a binding that was never recorded.

---

## Conclusion

Contribution 2 is substantially, but not entirely, a temporal-information
problem. The parts that are temporal (D, E, and half of C) already have
mature, standardized theory (bitemporal modeling) that is simply not applied
to the relevant AI-specific objects by default. The parts that are not
purely temporal (the adequacy of evidence content, and the normative
synthesis of G) require additional, non-temporal machinery — a minimal
decision record with an explicit binding step, developed next in
`minimal-decision-record.md`.
