---
id: note-oreilly-submission-package
title: "O'Reilly Article Submission Package"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [oreilly, submission, package]
refs: [article-submission.md, references.md, diagram-spec.md, CURRENT-OREILLY-ROUTE.md, HUMAN-REVIEW.md]
---

# O'Reilly Article Submission Package

## Working/publication title

**Authorized Now, Reconstructable Later**

## Dek

*Approving a production AI decision and reconstructing it later require different evidence — and neither guarantees the other.*

## Author

Monika Dvořáčková

## Author bio

Monika Dvořáčková is an AI/ML engineer specializing in NLP, MLOps, and
AI governance, with a background in mathematics and law and ongoing
studies in technology and regulation. Her work focuses on the systems-
engineering side of accountable AI: decision-level control, evidence
architectures, and reconstructing what production ML decisions actually
relied on after the fact. She also teaches AI and machine learning,
helping engineers move from experimental models to production-grade
systems.

*(92 words. Drawn only from professional background material already on
record; no mailing address, phone number, or personal email included —
see the privacy scan in this task's validation step.)*

## Article type

Deep practitioner article.

## Target audience

**Primary:** ML/MLOps/AI engineers and architects building production
systems who make decisions about what gets deployed, how it's approved,
and what happens when someone needs to investigate a past decision.

**Secondary:** technical governance and platform-engineering
practitioners responsible for making production AI systems auditable.

**Prerequisite knowledge:** familiarity with model evaluation,
deployment pipelines, CI/CD, model registries, and logging/versioning
practices. No prior familiarity with access-control theory, provenance
standards, or assurance-case literature is assumed — each is introduced
in plain terms at first mention.

## Article length

3,810 words (article body, `article-submission.md`).

## Abstract

Most production AI systems can tell you a decision was approved. Far
fewer can tell you, months later, exactly what that decision relied on.
This article argues that authorization and reconstruction are separate
engineering properties — a system can pass one and still fail the
other — and walks through why, using a single model-promotion decision
followed from the moment it's approved to the moment someone needs to
reconstruct it. It shows what production systems already get right
(evidence-gated approval), what they typically miss (a preserved record
of what a decision actually consumed, not just what existed), and how
existing mechanisms from access control, provenance, and distributed
tracing already solve each half — the missing piece is connecting them
around the decision itself.

## Editor pitch

Most engineering teams building production AI systems have solved half
of "can we trust this decision": they evaluate the model, require
approvals, and gate deployment behind a policy check. That answers
whether the decision was authorized. It says nothing about whether
anyone can later establish what the decision actually relied on — which
model version, which evaluation run, which policy — once the model has
been retrained and the policy has been revised. This article challenges
the assumption that passing review and being explainable later are the
same property, or that one follows from the other.

For an ML/MLOps engineer, the payoff is concrete: a two-part pattern for
what to record around every consequential decision (an authorization
relation and a consumption relation), and a third, honest output —
"ambiguous" — for when the retained record genuinely can't determine a
unique answer, rather than a reconstruction tool quietly guessing.

This isn't a new architecture. The article is explicit that every
mechanism it describes — policy enforcement, provenance, distributed
tracing, event sourcing, and especially dynamic/continuous assurance
cases — already exists elsewhere in systems engineering. What's missing
in most ML tooling is applying that discipline at the level of the
production decision rather than the model. That's a systems-pattern
piece, not a trend piece — no claim is made about how common this gap
is, only that it's real and worth checking for.

*(230 words.)*

## Central thesis

Authorization and reconstruction are separate engineering properties of
a production AI decision, and both depend on preserving enough
information about the relationships around that decision — what
permitted it, and what it consumed — whether that information is
captured explicitly at the time or reliably established afterward.

## Reader transformation

**Before:** "We evaluated the model, required approval, and gated the
deployment. The decision is auditable."

**After:** Authorization and reconstruction are two different
questions, checked against two different kinds of evidence — passing
one tells you nothing about the other.

**Concrete design change:** for every consequential decision, preserve
both an authorization relation (evidence, requirements, policy,
approving authority, gate outcome) and a consumption relation (which
specific model, data, config, and context version the decision actually
used) — and give any reconstruction process a legitimate "ambiguous"
output, not just "answer" or "error."

## Key takeaways

1. Authorization and reconstruction are separate properties — a
   decision can pass one and fail the other.
2. Follow the decision, not only the model — a single model can
   participate in many differently-governed decisions.
3. Retaining every version isn't the same as recording what a specific
   decision consumed; preserve the relation, however it's captured.
4. Ambiguity is a legitimate reconstruction outcome — a system that
   can't represent it will eventually be forced to guess.
5. None of the required mechanisms are new — access control, provenance,
   tracing, and assurance-case practice already provide them; the gap is
   applying them at the decision boundary.

## Why O'Reilly

This is a practitioner systems-pattern article, not an academic paper or
a regulatory/compliance piece — it belongs where O'Reilly's audience
already is: engineers designing and operating production ML systems who
want an architecture pattern, not a policy framework. The article
translates established mechanisms (access control, provenance,
distributed tracing, event sourcing, assurance cases) into the specific
context of AI-mediated production decisions, with one running example
carried end to end and a concrete design checklist a reader can apply
directly. It's research-informed — grounded in a controlled experiment
on the reconstruction gap specifically — but reads as an engineering
essay, not a paper: no methodology section, no metrics table, no claim
requiring the reader to trust an experiment rather than the argument
itself.

*(122 words.)*

## Prior-art positioning

The article is explicit and unhedged about prior art: policy decision/
enforcement points (PDP/PEP, XACML), Kubernetes admission control,
software supply-chain attestation (in-toto, SLSA), database-provenance
theory and W3C PROV, distributed tracing (OpenTelemetry), event sourcing
(Fowler), and — identified as the closest single collision — dynamic and
continuous assurance cases, including recent work applying them
specifically to frontier AI systems. See `references.md` for the full
per-source check.

## Novelty positioning

**NEW SYNTHESIS + PRACTITIONER TRANSLATION.** The article claims a
practitioner synthesis connecting existing mechanisms around the
AI-mediated production decision as the operational unit, informed by a
controlled research finding about the specific gap (retained history
vs. consumed context). It does not claim a new enforcement mechanism, a
new provenance mechanism, a new assurance architecture, a new theory, or
a new architectural layer — see `article-submission.md`'s own "What This
Doesn't Claim" section, which states this directly to the reader.

## References

See `references.md` for the full per-source check and publication
formatting.

## Diagram

See `diagram-spec.md`. One conceptual diagram is recommended for
inclusion, in plain-text form as currently used in
`article-submission.md`, pending confirmation of whether O'Reilly's
production format requires a rendered figure instead.

## Current submission route

**VERIFIED:** general proposal route via **workwithus@oreilly.com**
(`oreilly.com/work-with-us`), which explicitly covers content shorter
than a book. Radar (`oreilly.com/radar`) is confirmed active and
currently publishing, but no distinct, publicly-documented Radar-
specific submission process or address was found. Full detail:
`CURRENT-OREILLY-ROUTE.md`.

## Items to confirm with O'Reilly

1. Whether to pitch this specifically as a Radar piece or as a general
   short-form content proposal and let the editor route it.
2. Whether a required article format, word-count ceiling, or metadata
   template exists beyond what's publicly documented (none was found).
3. Whether O'Reilly's production pipeline requires a rendered diagram
   figure rather than the plain-text version submitted here.

(Full discussion in `CURRENT-OREILLY-ROUTE.md`; author-facing decisions
that don't depend on O'Reilly's answer are in `HUMAN-REVIEW.md`.)
