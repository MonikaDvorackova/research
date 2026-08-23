---
id: note-contribution-02-drafting-verdict
title: "Contribution 2 Drafting Readiness — Publication-Readiness Verdict"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [contribution-02, drafting-readiness, verdict]
refs: [contribution-definition.md, novelty-review.md, prior-art-matrix.md, claim-ledger.md, evidence-review.md, non-obvious-result.md, thesis-and-titles.md, contribution-boundary-check.md]
---

## Is Contribution 2 independently publishable?

**YES.**

## What exactly is novel?

- The empirical demonstration, across two independent and differently-
  shaped mechanisms (retroactive correction; observational timestamp-
  precision loss), that complete, competently-implemented version history
  is not sufficient for temporally correct decision reconstruction — and
  that the two mechanisms fail in measurably different ways (confidently
  wrong vs. honestly ambiguous).
- The negative control (F10-6), which narrows the required property from
  a specific named schema ("decision-time binding") to a general one (any
  preserved causal relation) — not found stated or tested this way in the
  surveyed prior art (`novelty-review.md`, `prior-art-matrix.md`).
- The replay-vs-reconstruction distinction (`../collision-tests.md` Task
  6) and the C/D/E/F/G problem decomposition
  (`../problem-formalization.md`), not found named this way in the
  literature surveyed.

## What is NOT novel?

- Every underlying mechanism (bitemporal databases, event sourcing, W3C
  PROV, in-toto/Sigstore, distributed tracing) is pre-existing and
  unmodified.
- The engineering fix, once named, is mechanically trivial — a version
  reference, no different in kind from a foreign key
  (`novelty-review.md` Objection 5).
- That "some" preservation beats "no" preservation is already
  well-established and not part of this contribution's claim.
- The observation that audit-log integrity ≠ completeness, and that
  replay ≠ justification, both restate distinctions already implicit (if
  not formally named) in existing standards and taxonomies.
- Any claim that AI systems generally lack this property in production —
  not measured, not claimed.

## Strongest thesis

Complete version history answers "what does the retained record now say
was valid at t0," which is a different question from "what did this
decision actually consume" — and the two can diverge for at least two
independent, empirically demonstrated reasons: a record can be silently
rewritten after the fact (retroactive correction, producing a confident,
coherent, and wrong reconstruction), or a record can be genuinely
underdetermined by what was actually observable at decision time
(precision loss, producing an honest "unknown" rather than a wrong
answer). Closing this gap requires preserving a causal relation between
the decision and what it consumed — not preserving more history, and not
necessarily a schema named "binding" specifically, since any equivalent
causal signal closes the same gap.

## Strongest hostile-review objection

"Isn't this just [provenance / event sourcing / bitemporal data], done
correctly?" — and the sharpest form of it, per `novelty-review.md`
Objection 2, is that the F10-6 negative control itself concedes an
ordinary, non-binding event-sourced consumption record fully closes one
of the two tested mechanisms, meaning the contribution's own strongest
empirical result partially validates the objection rather than refuting
it.

## Why the article survives that objection

Because the objection, even in its strongest form, only closes *one* of
the two independently demonstrated mechanisms. F10-6 shows an ordinary
causal event resolves observational precision loss — but no result in
either experiment shows an *unmodified*, default-configured instance of
provenance, event sourcing, or bitemporal storage resolving retroactive
correction; the primary experiment's Regime B was a genuine, strong
instance of exactly these mechanisms and still failed there, confidently.
The article survives by conceding the objection's full strength on
mechanism 2 while holding mechanism 1 as the case the objection does not
reach — this is a narrower, more defensible position than the
pre-follow-up thesis, and it is the position the evidence actually
supports (`evidence-review.md`).

## Empirical contribution

Two completed, reproducible, deterministic experiments (33 + 12 raw
case-regime rows total) establish, in a synthetic but deliberately
non-strawmanned controlled setting: (1) a categorical Temporal
Correctness failure under retroactive correction, with measured False
Historical Confidence up to 1.00, confined exactly to the cases designed
to test it and absent everywhere else; (2) a categorical Unique
Reconstruction failure under observational precision loss, resolved
honestly (never confidently-wrong) in this implementation; and (3) a
negative control demonstrating the required property is general (any
causal relation), not specific to one schema. All raw data, pre-execution
manifests, and reproduction commands are committed
(`../experiment/`, `../experiment/followup-case10/`).

## Engineering contribution

A minimal, field-by-field justified decision-record schema
(`../minimal-decision-record.md`) — classified honestly as assembly, not
invention, of existing schema concepts (PROV relations, in-toto/Sigstore
container shape, bitemporal fields) — plus the diagnostic finding that
this record's *only* load-bearing, non-redundant addition over ordinary
versioning infrastructure is the binding step itself, empirically
confirmed to matter specifically (and only) under the two tested
mechanisms.

## Required external citations before drafting

Already gathered during the prior-art audit (`../prior-art-audit.md`) and
sufficient for drafting without further research:

- Snodgrass (TSQL2) / SQL:2011 bitemporal standard.
- W3C, "PROV-DM: The PROV Data Model," W3C Recommendation, 2013.
- Fowler, "Event Sourcing," 2005.
- in-toto Attestation Framework specification; SLSA v1.0; Sigstore/Rekor
  documentation.
- OpenTelemetry Specification.
- NIST SP 800-92, "Guide to Computer Security Log Management."
- Regulation (EU) 2024/1689 (AI Act), Article 12.
- ACM, "Artifact Review and Badging — Current," v1.1, 2020 (for the
  replay/reconstruction distinction's nearest adjacent formalization).
- MLflow documentation (Tracking, Model Registry).
- OASIS XACML 3.0 specification (new to this review pass — added to
  `prior-art-matrix.md`; not previously cited in `../prior-art-audit.md`
  and should be verified/re-fetched before publication, as it was not
  independently re-verified via live retrieval in this session).

## Claims forbidden in the article

The full list with reasoning is `claim-ledger.md`; the load-bearing
subset:

- "Versioning alone always/never suffices" (either absolute form).
- "Explicit decision-time binding is uniquely necessary" — directly
  contradicted by F10-6.
- "Provenance / event sourcing always solves the problem" (unconditional
  form) — only conditionally true, per the same negative control.
- Any claim about real-world prevalence of the failure mode, governance/
  compliance risk, or generalization to production systems — none
  measured by either experiment.
- "State is not knowledge" as a technical thesis statement (retained only
  as historical/practitioner color if referenced at all).

## Article boundary

Contribution 2 ends at: the demonstrated, scoped claim that historical
reconstructability of a specific decision requires a preserved causal
relation to its consumed context, evidenced by two synthetic experiments,
with no claim about prevalence, generalization, or the broader nature of
"understanding" as a systems property. Contribution 3 begins at: whether
this decision-specific finding is one instance of a more general pattern
spanning explainability, interpretability, observability, provenance, and
governance, and whether AI capability is outpacing the mechanisms needed
to preserve any of them — territory this package deliberately does not
enter (`contribution-boundary-check.md`).
