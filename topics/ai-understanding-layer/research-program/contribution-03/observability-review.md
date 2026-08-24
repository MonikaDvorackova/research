---
id: note-contribution-03-observability-review
title: "Contribution 3 — Observability Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, observability, control-theory]
refs: [pre-research-claim-ledger.md, source-ledger.md]
---

## Testing whether "understanding" reduces to observability

## Control-theoretic vs. software observability

Observability originates in control theory as a precise, mathematical
property: **the extent to which a system's internal state can be
determined from its external outputs** [S14]. Software observability
borrows the term with the same informal meaning, applied to logs,
metrics, and traces (the conventional "three pillars") [S14][S15]. The
field already draws a load-bearing internal distinction directly
relevant to Source A's framing: **"monitoring tells you whether a system
is broken; observability helps you understand why"** [S14] — this is,
almost verbatim, a technical restatement of part of Source A's own
diagnostic language, already established practitioner vocabulary, not a
novel distinction this programme introduces.

## Could the Understanding Layer simply be "better observability + provenance + history"?

**This possibility must not be dismissed, per the authorizing task's
explicit instruction, and this review does not dismiss it.** The
control-theoretic definition of observability — inferring internal state
from external outputs — is, at the right level of abstraction, almost
exactly what "reconstructing why a decision was authorized" (Contribution
2's object) or "understanding system behavior" (Source A's object)
requires: the ability to infer something not directly, currently visible
from what has been retained. Contribution 2's own finding (retained
history is not equivalent to being able to identify what was consumed)
can be restated in observability's own vocabulary: **retained data
existing is not the same as the system being observable with respect to
the specific internal fact in question** (which policy version a
decision used). This is a strong, direct collision.

**What observability's own literature does not yet claim to solve,
based on this review:** the *temporal* dimension Contribution 2's primary
experiment specifically tested — whether the record's own account of the
past can itself be legitimately revised after the fact (retroactive
correction), and what that does to an "infer state from outputs" query.
Standard software-observability treatments (logs/metrics/traces) do not,
in the sources reviewed, address transaction-time semantics or
retroactive correction as a distinct failure mode — that vocabulary
comes from bitemporal database theory, not observability theory, and
Contribution 2's own prior-art audit already found this gap
independently (`../contribution-02/prior-art-audit.md`, bitemporal
databases entry).

## Verdict

**Partially reduces, does not fully reduce.** A meaningful fraction of
what Source A gestures at with "understanding" is already precisely
named by observability theory's own definition (inferring internal state
from external signal) — this is not a new property this programme is
discovering. What does not reduce cleanly to observability, based on the
literature reviewed here: (1) the temporal/transaction-time dimension
Contribution 2 tested, which is bitemporal-database territory, not
observability territory; (2) the *decision-specific, per-instance*
binding question (which version did *this* decision use), which is
narrower than "can we infer the system's general internal state" and
closer to provenance's object (see `provenance-review.md`); (3) the
*normative* half of reconstruction (was the decision justified, not just
which values were consulted) — observability tooling has no normative
vocabulary, matching Contribution 2's own finding about tracing
specifically (`../contribution-02/collision-tests.md` Objection 6).
**Recommendation: any future Article 3 must state directly that
"understanding," as this programme uses the term, is not a new property
name for a genuinely new discovery — it substantially overlaps
observability's own long-standing definition, with the addition of a
temporal and a per-decision-binding dimension this programme's own
Contribution 2 already isolated and tested, not a dimension newly
identified here.**
