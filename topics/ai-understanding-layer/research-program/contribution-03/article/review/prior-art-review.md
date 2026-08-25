---
id: note-contribution-03-article-prior-art-review
title: "Contribution 3 Article draft-v1 — Prior-Art Review"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-25
tags: [contribution-03, article, review, prior-art]
refs: [../draft-v1.md, ../../prior-art-collision-matrix.md, ../../provenance-review.md, ../../diagnosability-review.md, ../../composition-review.md]
---

## Workflow provenance

Workflow provenance already formalizes activity dependencies,
`used`/`wasGeneratedBy` relations, data dependencies, and execution
graphs — confirmed directly by `../../prior-art-collision-matrix.md`'s
own row for "W3C PROV / database provenance": *Dependency relation? Yes,
exactly.* And `../../provenance-review.md` goes further: Buneman,
Khanna, and Tan's why-provenance/where-provenance formalism (ICDT 2001)
predates W3C PROV by twelve years and formalizes essentially the same
lineage concept in database-theoretic terms — a **more precise,
mathematically older** source for exactly the claim draft-v1 attributes
only to W3C PROV [1].

**What Article 3 adds beyond applying workflow provenance to AI-mediated
decision trajectories:** on the current evidence, not a new mechanism —
draft-v1 already concedes this (line 87: "not a new provenance
mechanism, and does not claim to be one"). What it adds is a controlled,
quantified demonstration, for this specific object class, that the gap
provenance already knows how to close is a gap that opens when the
relevant edge is not populated — plus the honest-ambiguity/false-
confidence separation (P5 in `reviewer-report.md`), which provenance
formalisms do not themselves address (provenance theory says how to
*represent* a dependency edge; it does not, by itself, prescribe how an
investigator should behave when the edge is genuinely absent from the
record).

**If the honest answer is "a practitioner translation plus a controlled
example" — say so.** It is. Say so in v2, explicitly, in the same
paragraph as the current provenance concession (see
`revision-plan-v2.md`).

**Missing source, confirmed and required:** Buneman, Khanna, Tan, "Why
and Where: A Characterization of Data Provenance," ICDT 2001 —
identified by this programme's own research (`source-ledger.md`'s S16,
Springer link confirmed) as the more precise, older provenance
formalization. Not citing it while claiming to fairly address "isn't
this just workflow provenance" is the single most concrete, fixable gap
in the article's citation base.

## Distributed tracing

If every decision corresponds to a span and parent-child/context
propagation is correctly instrumented, tracing already solves the
experiment — confirmed by `../../prior-art-collision-matrix.md`'s row
for "Distributed tracing (Dapper-lineage)": *Dependency relation? Yes,
causal (span graph).* Draft-v1 concedes this (line 85) but cites only
OpenTelemetry's own documentation [2], not the foundational academic
source behind it. `source-ledger.md`'s S4 — Sigelman et al., "Dapper, a
Large-Scale Distributed Systems Tracing Infrastructure," Google
Technical Report, 2010 — is already independently verified elsewhere in
this programme (primary source, `research.google/pubs` page confirmed)
and would strengthen this concession with an academic anchor alongside
the practitioner-facing docs. Recommended addition, not required with
the same force as Buneman.

**The actual engineering contribution, once conceded:** exactly what
draft-v1's "What to Preserve Across Decisions" section already states —
"decision records are not enough; trace/provenance relationships must
survive too" (paraphrased from lines 91–97). This is correct and does
not need inflation.

## Event sourcing

A correctly event-sourced workflow, instrumented to record which prior
event a later one consumed (not just what the later event itself did),
would retain exactly the causal chain draft-v1 calls missing — draft-v1
says this itself (line 85). **Classification: synthesis/application, not
mechanism novelty** — consistent with how the article already frames
itself, and consistent with how Article 2 treated the same source [3]
(Fowler's Event Sourcing) for its own, structurally similar finding.

## Compositional verification

`../../composition-review.md` already establishes, independently of this
article, that local component verification does not by itself examine
overall system behavior [S37][S38] — this is not new, and draft-v1
correctly attributes it to existing literature (line 87, citing [5]).

**Is reconstructability under composition a distinct property worth
isolating, or one instance of a generic principle?** On the evidence
available, it is the latter, applied carefully: `../../composition-
review.md`'s own verdict states the composition effect is "SUPPORTED,
for behavioral predictability specifically... PLAUSIBLE, not yet
SUPPORTED, for reconstructability specifically" before this experiment
ran. The experiment's genuine contribution is closing that specific,
previously-open gap (reconstructability, not predictability) with
evidence — a legitimate, modest, correctly-scoped synthesis move, not a
new instance of the generic principle requiring separate theoretical
standing.

## Diagnosability

`../../diagnosability-review.md` already identifies diagnosability as
"the strongest single formal collision found across both research
passes" for reconstructability at the single-decision level, and
observes that Contribution 2's own AMBIGUOUS/CORRECT_UNIQUE/WRONG_UNIQUE
classification is, in diagnosability's vocabulary, a diagnosability
verdict for a specific system model. **Could trajectory
reconstructability be expressed as diagnosability of histories/paths?**
Very plausibly — discrete-event-systems diagnosability theory has
decades of formal apparatus for "can you tell, from an observed output
sequence, which of several candidate event histories occurred," which is
structurally what T1's AMBIGUOUS verdicts are. This review did not
independently verify a specific named "path diagnosability" or "sequence
diagnosability" result in the DES literature (that would require new
research, out of scope for a review-only pass), but the collision is
strong enough that v2 should at minimum note the possibility rather than
implicitly presenting "trajectory reconstructability" as freestanding
vocabulary.

**Is "trajectory reconstructability" genuinely useful terminology, a
practitioner synonym, or unnecessary reinvention?** **A practitioner
synonym** — legitimate as an accessible on-ramp term for a practitioner
audience unfamiliar with discrete-event-systems theory, but not a new
technical property, and the article should not imply otherwise (it
currently does not explicitly claim novelty for the term, but it also
never flags the diagnosability connection for this trajectory-level
result the way `diagnosability-review.md` already did for the
single-decision case — an inconsistency worth fixing).

## Citation review (Section 20)

| Citation | Bibliographic accuracy | Primary/authoritative | Exact claim supported | Verdict |
|---|---|---|---|---|
| [1] W3C PROV-DM | Accurate (W3C Recommendation, 30 Apr 2013) | Yes | "used a specific prior entity, distinguishable from that activity's own descriptive attributes" | **PASS, but incomplete alone** — see Buneman gap above |
| [2] OpenTelemetry Traces | Accurate | Documentation, not primary academic source | "parent-span reference exists... to reconstruct causal execution order" | **PASS**; Dapper (S4) recommended as an academic companion |
| [3] Fowler, Event Sourcing | Accurate | Standard practitioner reference, previously verified in Article 2 | "event log... instrumented to record which prior event a later one consumed" | **PASS** |
| [4] Sampath et al., Diagnosability of Discrete-Event Systems, IEEE TAC 1995 | Verified independently this session (volume 40, issue 9, pp. 1555–1575, Sept 1995; primary PDF located) | Yes, foundational primary paper | "determining, from a system's observed output sequence, whether a specific event occurred" | **PASS** |
| [5] Bakirtzis & Topcu, AlgebraicSystems, arXiv:2203.16343, 2022 | Verified independently this session (authors, identifier, submission date confirmed via arXiv abstract page) | Yes, primary | "local, component-level correctness does not automatically compose into global, system-level guarantees" | **PASS** |

**Conclusion: the article's strongest collision is workflow provenance,
and its citation base for that collision is incomplete** — it cites the
general-purpose standard (PROV) but not the more precise, older,
programme-verified formalization (Buneman) that this programme's own
prior research already surfaced as the sharper match. This is the single
required citation addition for v2.
