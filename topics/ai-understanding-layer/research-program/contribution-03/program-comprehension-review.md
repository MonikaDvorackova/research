---
id: note-contribution-03-program-comprehension-review
title: "Contribution 3 — Program Comprehension & Knowledge-Preservation Review (Claim A, F-disciplinary)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, program-comprehension, software-archaeology, knowledge-vaporization]
refs: [pre-research-claim-ledger.md, source-ledger.md]
---

## Testing Claim A and the disciplinary half of Claim F

> A. Modern AI-mediated systems are, as currently built, difficult to
> reconstruct, explain, and predict.
>
> F (disciplinary half). Explainability, interpretability, observability,
> provenance, governance, and auditability are fragmented, uncoordinated
> partial responses to a common, unrecognized problem.

## Program comprehension is already a formalized research field

**This is the single most important collision found in this review.**
Program comprehension — "the activity by which software engineers come
to an understanding of the behavior of a software system using the
source code as the primary reference" — is not an ad hoc concern; it is
a named, decades-old software-engineering research area with its own
measurement tradition [S5][S6]. Developers spend a measured ~58% of their
time on program-comprehension activities [S6]. The field has moved from
self-report methods to eye-tracking and neuroimaging (fMRI, EEG) to
study comprehension at a cognitive level [S6], and a systematic mapping
study covers "40 years of designing code comprehension experiments" [S7].

**Consequence for Claim A.** "Systems can become hard to understand as
they grow more complex" is not a novel diagnosis original to Source A or
to AI systems — it is the founding premise of an entire, mature
sub-field of software engineering, already operationalized (comprehension
time, task-success rate, eye-tracking fixation patterns) in ways Source
A's own prose does not attempt. Claim A, as a general descriptive
observation about software systems, is **not new**; what would need to
be new, if anything, is either (a) evidence that AI-mediated systems are
harder to comprehend than the systems this field already studies, in a
way that field's own methods cannot capture, or (b) an extension of the
field's object of study from *source code* to *system behavior at
runtime*, which is a genuinely different unit of analysis (see
`prior-art-collision-matrix.md`'s "Level" column).

## Architectural knowledge vaporization already names the "disappearing knowledge" phenomenon

Source A's central illustration — a decision's context (prompt version,
retrieval state, policy interpretation) silently disappearing even
though the decision itself is recorded — has a close, pre-existing
namesake in software-architecture research: **architectural knowledge
vaporization**, the finding that "architectural knowledge is mostly
tacit and only exists in the heads of creators... easily lost,
contributing to expensive system evolution, difficult stakeholder
communication, and limited reusability" [S8]. This has its own dedicated
literature, including pattern-driven approaches specifically aimed
*against* vaporization [S9] and studies connecting it directly to
architecture erosion and technical debt accumulation [S10].

**Consequence.** The mechanism Source A describes (design-time or
decision-time context becoming unrecoverable once it exists only
implicitly, in a person's head or a since-changed live system) is not a
new observation — it is a named, actively-researched phenomenon in
software-architecture literature, studied for design rationale and
architectural decisions specifically. Contribution 2's own object (a
single historical decision's consumed context) is a narrower, more
formally specified instance of this general phenomenon, not a
previously-unnamed one.

## Software archaeology and architecture recovery

Software archaeology — "the study of poorly documented legacy software"
— and architecture recovery methods already exist specifically to
*reconstruct* lost system understanding from what remains (code,
artifacts, partial documentation) [S11]. This is a direct collision with
any claim that reconstructing lost system knowledge is itself a new
engineering problem: it is an established discipline with its own
methods (concern-oriented recovery, pattern-based recovery) [S12].

## Testing the disciplinary fragmentation claim (F)

The question is not whether explainability, observability, provenance,
governance, and auditability are *different* fields (trivially true) but
whether they are *uncoordinated* in a way that constitutes a real,
citable finding rather than an assertion. This review found **mixed,
scoped evidence**, developed further in `ai-systems-review.md`: a
current (2026) technical source states directly that "the AI
observability landscape... is characterized by impressive depth at
individual layers but limited integration across them" [S13] — real,
current, and specific to *layers within AI observability tooling*, not
to the six named disciplines as a whole. No source found in this review
directly studies whether explainability, provenance, governance, and
auditability *as research communities* fail to coordinate with each
other; that broader claim remains an assertion, not yet a documented
finding, and Section 21's assurance-case counter-test (see
`ai-systems-review.md`) provides a genuine candidate umbrella that would
complicate it further if it applies.

## Verdict

**Claim A does not survive as a novel diagnosis** — program
comprehension already formalizes "systems can be hard to understand,"
with decades of measurement behind it. **The "knowledge disappears"
mechanism does not survive as a novel observation** — architectural
knowledge vaporization already names and studies it. What is not yet
disconfirmed, and would need to be the actual contribution if Contribution
3 proceeds, is narrower: whether *AI-mediated, runtime, multi-decision
system behavior* is a genuinely different unit of analysis than either
program comprehension's object (static source code) or architectural
knowledge management's object (design-time decisions), such that neither
field's existing methods transfer directly. That is a real, testable,
much narrower question than Source A's own framing — see
`residual-gap-analysis.md`.
