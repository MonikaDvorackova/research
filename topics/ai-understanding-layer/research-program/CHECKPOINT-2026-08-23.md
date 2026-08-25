---
id: note-ai-understanding-layer-checkpoint-2026-08-23
title: "AI Understanding Layer — Research Programme Checkpoint (2026-08-23)"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-23
updated: 2026-08-23
tags: [checkpoint, resume-document, programme-status]
refs: [research-program/research-roadmap.md, research-program/contribution-boundaries.md]
---

# Research Programme Status — Resume Document

This file exists so a future session can resume this programme without
reading the full prior conversation history. It is a snapshot as of
2026-08-23; treat any claim about "current" repository state as frozen at
this commit, not as live fact — verify against the actual files before
acting on anything below.

---

## Contribution 1 — Decision-Level Control

**Status: substantially complete.**

- Complete: spine, evidence inventory, three drafting iterations
  (`draft-v1.md`, `draft-v2.md`), a full adversarial prior-art audit
  (`novelty-audit.md`, verdict: **Position B — new synthesis, not new
  mechanism**), and a claim-by-claim sourcing audit (`sourcing-audit.md`).
  Two O'Reilly-facing drafts exist (`oreilly-submission-draft.md`,
  `oreilly-submission-disruptive.md`).
- No mechanism novelty is claimed anywhere in this material — every draft
  explicitly concedes the underlying mechanisms (access control, admission
  control, supply-chain attestation) are pre-existing; the claimed
  contribution is the model-vs-decision synthesis and framing.
- **What remains:** no further research is required for this contribution
  to stand on its own. Whether either O'Reilly draft is actually submitted
  for publication is an open, human decision not made by this programme
  (see "O'Reilly status" below).

---

## Contribution 2 — Preservation & Reconstruction

**Status: prior-art audit complete; experiment designed; NOT implemented;
NOT executed; NO results exist.**

- **Prior-art verdict:** **B — narrowed survival**
  (`research-program/contribution-02/novelty-verdict.md`). Every
  individual primitive needed (bitemporal valid-time semantics, W3C PROV
  lineage, in-toto/Sigstore attestation, event-sourced replay) already
  exists in mature, separate literatures; none is applied by default to
  the AI-specific set of transient dependencies (prompts, live retrieval,
  policy-as-config, delegated authority), and no existing artifact
  combines them with an explicit per-decision binding for this purpose.
- **Surviving thesis:** "State Is Not Knowledge" is retired as the
  technical thesis (retained only as practitioner-register color).
  Replacement: *retained system state does not, by default, bind a
  decision to the temporally valid versions of the evidence, policy, and
  authority that made it valid when it occurred.* Working shorthand:
  **"Versioned is not bound."**
- **Experiment design status:** Complete
  (`research-program/contribution-02/experiment-design/`, 10 files).
  Design verdict: **READY FOR IMPLEMENTATION.** Compares Regime B
  (independently versioned, unbound) against Regime C (versioned and
  explicitly bound at decision time) as the scientific center, with Regime
  A (bare) as a floor/manipulation-check condition. Primary metric:
  Temporal Correctness; primary diagnostic metric: False Historical
  Confidence. Uses a pre-registered, pattern-based diagnostic evaluation
  over a ~10-case perturbation matrix and a deterministic (not human or
  LLM) reconstruction procedure, deliberately to avoid conflating
  information-architecture sufficiency with investigator skill.
- **NO experiment code exists. NO experiment has been run. NO results —
  positive, negative, or partial — exist anywhere in this repository.**

---

## Contribution 3 — The Understanding Layer

**Status: reserved. Not drafted. Not developed.**

- Its research gaps remain exactly as `claim-graph.md` and
  `research-roadmap.md` Step 6 describe them: a dedicated
  historical/comparative literature review (does the software-engineering
  "recurring preservation pattern" claim survive scrutiny — e.g., Git's
  actual origin is distributed collaboration/merge-conflict resolution,
  not explicitly "preserving knowledge," a complication flagged but not
  yet investigated) and a resolution of the missing generalizing premise
  between decision-specific reconstruction (Contribution 2) and
  system-behavior-wide "understanding" (Contribution 3) — flagged in
  `recommended-program.md`'s adversarial self-review (Q3) and never
  argued for directly in either primary source.
- Material encountered during the Contribution 2 audit that touches this
  territory was logged, not developed, in
  `research-program/contribution-02/deferred-contribution-03.md`.
- **This contribution must not be started before Steps 1 (done), 5
  (Contribution 2 drafting, not yet reached — see "Next exact action"
  below), and 6 (this literature review) are complete**, per
  `research-roadmap.md`'s explicit sequencing and the terminal-thesis
  protection reconfirmed across both prior adversarial passes.

---

## Current Publication Architecture

**Approved: three independent contributions**
(`contribution-boundaries.md`, Task 5), **sharing one root premise (C1:
output ≠ decision) but branching from there — not a strict linear chain.**

```
                  MODEL LEVEL (substrate, not a claim)
                        │
                        ▼
                 DECISION LEVEL (C1 — shared root)
                        │
           ┌────────────┴────────────┐
           ▼                         ▼
  CONTRIBUTION 1                HISTORICAL / PROVENANCE LEVEL
  Decision-Level Control        CONTRIBUTION 2
  (terminal on this branch)     Preservation & Reconstruction
                                         │
                                [generalizing premise,
                                 not yet argued]
                                         │
                                         ▼
                                CONTRIBUTION 3
                                The Understanding Layer
                                (terminal; requires 1 and 2
                                 as earned scaffolding first)
```

**This branching structure matters operationally:** Contribution 2 depends
only on Contribution 1's shared premise (C1), not on Contribution 1's
architecture, its drafts, or its publication status. Contribution 2's
prior-art audit and experiment design were correctly able to proceed
without waiting on any further Contribution 1 work, and did.

---

## O'Reilly Status

Two O'Reilly-facing drafts exist for Contribution 1 only
(`article-01-decision-level-control/oreilly-submission-draft.md` and
`oreilly-submission-disruptive.md`). **No further O'Reilly work is
required before resuming this programme.** Whether either draft is
actually submitted for publication is a decision this programme has not
made and does not make automatically — it requires an explicit human
choice to publish Contribution 1 separately, at whatever time that is
wanted. Nothing in Contribution 2's or Contribution 3's status depends on
that decision being made first.

---

## Book Status

The original book proposal (`sources/source-b-original-book-proposal.md`)
remains **source material only** — a verbatim historical capture, not a
draft. It has **not** been rewritten against the mature three-contribution
research programme that has since developed well beyond its original
scope (the proposal's own "controlled failure experiments" and
"repository audit" methodological claims were re-examined and substantially
redesigned for Contribution 2 in `empirical-program.md` and
`contribution-02/empirical-next-step.md` — the proposal's originally
intended use of those methods for Contribution 1 was found less
well-motivated than their redesigned use for Contribution 2). No decision
has been made about whether or when to revise the book proposal itself.

**Note on this file specifically:** as of this checkpoint, the personal
mailing address, phone number, and email fields in that source document
have been redacted (by explicit author instruction, given this repository
is public) — see the redaction note at the top of that file. No other
content was altered.

---

## Next Exact Action

**Implement the approved Contribution 2 reconstruction experiment from
`research-program/contribution-02/experiment-design/implementation-spec.md`,
then execute it only after a human confirms the design.**

This is a two-step gate, and both steps require explicit human
authorization before proceeding — this is the frozen workflow for this
programme going forward:

1. A human reviews the experiment design
   (`contribution-02/experiment-design/README.md` is the entry point) and
   either approves it, requests changes, or rejects it.
2. Only after approval does implementation begin; only after
   implementation is reviewed does execution begin. No session should
   implement or execute this experiment without that explicit
   authorization having been given in the conversation that does so.

---

## Known Open Questions

Only items that materially affect the next phase are listed; resolved
questions from earlier passes are not repeated here.

1. **Case 10's boundary-precision question** (`implementation-spec.md`,
   Section 5 and Section 7): whether the concurrency-ambiguity case should
   be built as a genuine fault-injection test or documented as a
   structural limitation of the synthetic design — left open for the
   implementer, not resolved by this checkpoint.
2. **External validity beyond the synthetic testbed** is explicitly
   unaddressed by the current design (`validity-and-confounders.md`) — a
   real-system follow-up study is anticipated but not designed.
3. **The missing generalizing premise for Contribution 3** (Q3 in
   `recommended-program.md`'s adversarial self-review) remains unresolved
   and gates Contribution 3's drafting, not Contribution 2's — no action
   needed until Contribution 2's own drafting (Step 5) is reached.
4. **Whether to submit either Contribution 1 O'Reilly draft** is an
   open human decision, independent of and not blocking any further
   research step.
5. **Whether/how to revise `source-b-original-book-proposal.md`** beyond
   this checkpoint's contact-info redaction remains undecided.

---

## Experiment execution update (2026-08-23)

The Contribution 2 reconstruction experiment described above under
"Next Exact Action" was implemented and executed in this session, under
explicit human authorization for both steps of the two-step gate.

- **Implementation:** complete.
  `contribution-02/experiment/` (`src/`, `tests/`, `results/`,
  `analysis/`). Pure Python 3 standard library. 31 pre-execution invariant
  tests, all passing. The B/C information-equivalence invariant
  (`preservation-regimes.md`) is machine-checked and held for every case.
- **Execution date:** 2026-08-23. Fully deterministic (no randomness used
  anywhere; no seed required). Raw output: `experiment/results/`.
- **Result classification:** **PARTIAL SUPPORT** for H1, against the
  pre-registered interpretation table
  (`experiment-design/preregistered-interpretation.md`). The
  retroactive-correction mechanism (Cases 3, 8, 9) was confirmed with a
  clean, categorical result (Regime C: TC=1.00/FHC=0.00 vs. Regime B:
  TC=0.00/FHC=0.50–1.00; B ≈ C exactly on every non-retroactive case). The
  concurrency-ambiguity mechanism (Case 10) was not tested by this run — a
  disclosed implementation choice (exact, non-fault-injected timestamps)
  meant no genuine ambiguity was present for Regime B to fail on. Full
  report: `experiment/analysis/experiment-report.md`; short verdict:
  `experiment/RESULT.md`.
- **Contribution 2 status:** thesis narrowed and empirically grounded, not
  broadened or weakened. See `contribution-02/novelty-verdict.md`'s
  post-experiment update (appended, dated, does not erase the
  pre-experiment verdict). Contribution 2 remains independently
  publishable under the thesis as stated, with its empirical support now
  precisely scoped to the retroactive-correction mechanism.
- **Exact next step (superseded by the follow-up below):** a follow-up
  run of Case 10 with genuine clock/timestamp-precision fault injection
  is required before the concurrency-ambiguity mechanism can be reported
  as tested in either direction. This is new work requiring its own
  explicit authorization — it was not performed in this session, per the
  hard-stop instruction this session operated under (no exploratory
  follow-up experiments, no case tuning, no post-hoc metrics without a
  new human decision). No other contribution (1 or 3) was touched in this
  session.

---

## Follow-up Case 10 execution update (2026-08-23)

The follow-up named above was separately, explicitly authorized and
executed in a later session on the same date. Implementation:
`contribution-02/experiment/followup-case10/`. **The primary experiment
(commit `31c58ddc6e95b5f66153b4c2dd35d91f4ae8e725`) was not modified** —
this follow-up is fully isolated (its own `src/`, `tests/`, `results/`,
`analysis/`), reusing only the primary experiment's stable schema
(`domain.py`) read-only.

- **Mechanism tested:** timestamp precision loss (distinct from the
  primary experiment's retroactive correction). Six cases; Regime B vs.
  C only; 17 follow-up tests plus all 31 original primary-experiment
  tests re-run unmodified, all passing.
- **Result:** where no causal signal exists, complete version history
  cannot uniquely resolve a decision's consumed version under precision
  loss (Regime C succeeds, Regime B honestly reports ambiguity — never a
  confident wrong answer, False Historical Confidence = 0.00 throughout).
  A disclosed negative control (F10-6) showed an ordinary, non-binding
  causal consumption event resolves the same ambiguity exactly as well
  as explicit binding does.
- **Consequence:** narrows the surviving thesis from "explicit
  decision-time binding is required" to "a preserved causal relation
  between decision and consumed version is required; explicit binding is
  one general, buildable implementation, not the only one." Full
  statement: `contribution-02/novelty-verdict.md`'s follow-up-dated
  update.
- **Integrated Contribution 2 empirical verdict: NARROWED SUPPORT.**
- **Contribution 2 empirical phase: CLOSED.** No further pre-drafting
  empirical question is currently known to be a must-have.
- **Exact next step:** human review of Contribution 2's evidence (primary
  + follow-up) before drafting. Per this follow-up's own hard-stop
  instruction, no further Contribution 2 experiments, no paper drafting,
  no O'Reilly revision, and no Contribution 3 work were performed in this
  session.

---

## Contribution 2 drafting-readiness review

The human review named above as the exact next step was performed in a
later session on the same date, producing the authoritative drafting
package at `contribution-02/drafting-readiness/`
(`contribution-definition.md`, `novelty-review.md`, `prior-art-matrix.md`,
`claim-ledger.md`, `evidence-review.md`, `non-obvious-result.md`,
`thesis-and-titles.md`, `terminology.md`, `formalization.md`,
`article-spine.md`, `diagram-plan.md`, `contribution-boundary-check.md`,
`VERDICT.md`). **No experimental result, manifest, or case definition was
altered** — this phase interprets the existing evidence from the primary
experiment and the Case 10 follow-up; it does not rerun or modify either.

- **Final thesis:** complete version history answers "what does the
  retained record now say was valid at t0," not "what did this decision
  actually consume" — the two diverge under retroactive correction
  (confidently wrong) and under observational precision loss (honestly
  ambiguous); closing the gap requires a preserved causal relation
  between decision and consumed context, of which explicit binding is one
  sufficient, general implementation, not the only one (`VERDICT.md`).
- **Novelty classification:** primarily new synthesis, empirically
  demonstrated for the first time in this programme across two
  independent mechanisms; not a new mechanism, not a new architecture
  (`contribution-definition.md`).
- **Publication-readiness verdict: YES — independently publishable**
  (`VERDICT.md`).
- **Article working title:** "Retained Is Not Consumed: A Measured
  Causal Gap in AI Decision Reconstruction" (technical); "Why Keeping
  Every Version Still Isn't Enough to Explain an AI Decision"
  (publication) (`thesis-and-titles.md`).
- **Contribution 2 empirical phase: CLOSED** (confirmed, not reopened, by
  this review).
- **Contribution 3 non-consumption:** explicitly scanned
  (`contribution-boundary-check.md`) — no leakage found; all mentions of
  "understanding layer" / capability-vs-understanding / fragmentation
  terminology appear only inside explicit exclusion statements.
- **Exact next step:** human approval of the Contribution 2 drafting
  position (`VERDICT.md`) before any article is drafted. No article was
  drafted in this session; no work was performed on Contribution 1,
  Contribution 3, or the O'Reilly synthesis.

---

## Article 2 draft-v1

Written in a later session, on explicit authorization, from the drafting
package above. `contribution-02/article/draft-v1.md` (2,723 words),
`editorial-notes.md`, `draft-v1-audit.md` (self-audit against novelty
inflation, empirical overreach, negative-control honesty, prior-art
fairness, Article 3 leakage, terminology, evidence traceability, and
reader value — all PASS, one accuracy fix applied).

- **Article 2 draft-v1: COMPLETE.**
- **Empirical phase: still CLOSED** — no experiment was rerun or altered;
  every number in the draft was checked directly against the committed
  CSVs in `contribution-02/experiment/results/` and
  `contribution-02/experiment/followup-case10/results/`.
- **Drafting phase: IN REVIEW.**
- **No publication venue locked.** Written as an independent article, not
  adapted for O'Reilly (see `article/editorial-notes.md`'s "Publication
  venue questions").
- **Exact next step:** human editorial review of Contribution 2
  draft-v1. No draft-v2, no submission, no O'Reilly adaptation, no
  Contribution 3 work, and no further experiments were performed in this
  session.

---

## Article 2 draft-v2

Written on explicit authorization, as a substantive corrective revision
of draft-v1 (which remains unmodified, at
`contribution-02/article/draft-v1.md`) incorporating the adversarial
review and dedicated bitemporal-verification pass
(`contribution-02/article/review/`). New title: "Retained Is Not
Consumed: Why Version History Doesn't Guarantee Decision Reconstruction."

- **Article 2 draft-v2: COMPLETE** (`contribution-02/article/draft-v2.md`,
  2,519 words; `editorial-notes-v2.md`; `draft-v2-audit.md`, all eight
  audited dimensions PASS).
- **Technical correction incorporated:** the overstated bitemporal claim
  from draft-v1 is removed. Case 8 (retroactive authority correction) is
  now the article's primary, clean retroactive-correction evidence; Cases
  3 and 9 (retroactive policy correction) are explicitly reframed as a
  reconstruction-algorithm limitation, not an information-architecture
  gap — matching `contribution-02/article/review/BITEMPORAL-VERDICT.md`
  exactly.
- **Primary experiment interpretation: narrowed**, per the above. The
  Case 10 follow-up and its F10-6 negative control now carry more of the
  article's argumentative weight, presented earlier in the revised
  structure.
- **Empirical phase: still CLOSED** — no experiment was rerun, no raw
  result or implementation file was touched; every number added or
  retained in draft-v2 was checked directly against the committed CSVs.
- **Drafting phase: IN HUMAN REVIEW.**
- **No publication venue locked**, publication architecture unchanged.
- **Exact next step:** human editorial review of Contribution 2
  draft-v2. No draft-v3, no submission, no O'Reilly adaptation, and no
  Contribution 3 work were performed in this session.

---

## Article 2 final acceptance

The human editorial review named above as the exact next step was
performed in a later session. Full record:
`contribution-02/article/FINAL-ACCEPTANCE.md`. **Verdict: ACCEPT.** No
blocking issue was found on independent re-verification against the
committed raw results; `draft-v2.md` was left unmodified, per the
acceptance gate's own rule that zero blocking issues means no edit is
made.

- **Contribution 2 research: COMPLETE.**
- **Empirical phase: CLOSED.**
- **Article 2: COMPLETE.**
- **Argument/evidence: FROZEN** — `contribution-02/article/draft-v2.md`
  (2,519 words, title "Retained Is Not Consumed: Why Version History
  Doesn't Guarantee Decision Reconstruction") is the frozen article
  text; `draft-v1.md` remains as the unmodified historical first draft;
  the full review and verification trail
  (`contribution-02/article/review/`) is preserved unmodified.
- **Publication venue: NOT LOCKED.**
- **Next research-program step: Contribution 3** — not started in this
  session. Per `contribution-boundaries.md` and this checkpoint's own
  publication-architecture section, Contribution 3 requires Contributions
  1 and 2 as earned scaffolding and a dedicated historical/comparative
  literature review (Step 6) not yet performed.
- **O'Reilly synthesis:** unchanged, not drafted in this session; see
  `contribution-02/article/FINAL-ACCEPTANCE.md`'s "Later O'Reilly
  synthesis" section for the boundary note on what Article 2 should and
  should not contribute to it, when that work is eventually authorized.

---

## Contribution 3 — historical/comparative review

`research-roadmap.md` Step 6 (`contribution-03/`) executed on explicit
authorization: 14 documents, ~29 external sources across version-control/
transaction-log/tracing history, program comprehension, architectural
knowledge management, observability, provenance/replay, ML systems
(Hidden Technical Debt), foundation-model/agent interpretability and
observability, XAI, formal/runtime verification, and assurance cases.
Full verdict: `contribution-03/VERDICT.md`.

- **Contribution 1: COMPLETE** (unchanged).
- **Contribution 2: COMPLETE** (unchanged, frozen at
  `contribution-02/article/draft-v2.md`).
- **Contribution 3: HISTORICAL/COMPARATIVE REVIEW COMPLETE.** Terminal
  thesis survives **narrowed**, not as originally stated — decomposed
  into five separable claims, of which only the AI-specific-complications
  claim and a much-weakened historical-pattern claim survive; the
  comparative "capability outpaces understanding" claim is classified
  **untested conjecture, bordering unfalsifiable**; "Understanding
  Layer" is **demoted to metaphor** (no specifiable invariant, interface,
  or boundary found). Residual gap: **integration + measurement**, not a
  missing mechanism or architecture. Novelty: primary **new synthesis**.
  Strongest collision: **epistemic opacity** (philosophy of
  science/STS), a near-identical existing thesis to Source A's
  diagnostic claim.
- **Article 3: NOT STARTED.** Not ready to draft — `contribution-03/research-questions.md`'s
  five questions (above all: can system-level "understanding" be
  operationalized at all) are open.
- **O'Reilly synthesis: NOT STARTED**, unchanged.
- **Next step (superseded by the narrow follow-up pass below):** per
  `contribution-03/VERDICT.md`, resolve
  `contribution-03/research-questions.md`'s open questions before any
  Article 3 drafting is authorized.

---

## Contribution 3 — narrow follow-up pass (RQ1/RQ3)

One final, narrow research pass, answering exactly the two blocking
questions the prior verdict left open. Full record:
`contribution-03/FINAL-RESEARCH-VERDICT.md`. New documents:
`operationalization-review.md`, `diagnosability-review.md`,
`assurance-integration-review.md`, `composition-review.md`,
`generalization-from-c2.md`, `article-03-options.md`; `source-ledger.md`
updated (11 new sources). The prior historical/comparative review
(`VERDICT.md` and all documents from the first pass) is preserved
unmodified.

- **Contribution 1: COMPLETE.**
- **Contribution 2: COMPLETE.**
- **Contribution 3 research: NARROW PASS COMPLETE.** RQ1 (can system-
  level understanding be operationalized?) — **PARTIALLY**: only as a
  vector of already-named properties (reconstructability ≈
  diagnosability, observability, interpretability, predictability ≈
  system identification, verifiability), not one new scalar or umbrella.
  RQ3 (does Contribution 2 generalize?) — **PARTIALLY**: fully supported
  at the single-decision level (G1); only a plausible, unconfirmed
  extension to execution-level (G2); trajectory-level and beyond (G3+)
  require new evidence. Integration gap **NARROWED** (dynamic/continuous
  assurance cases already exist and are being applied to AI systems —
  the gap is adoption/composition with Contribution 2's specific claim
  type, not absent coordinating infrastructure). Measurement gap
  **CONFIRMED**. Composition effect **PLAUSIBLE** for reconstructability
  specifically (directly SUPPORTED only for the adjacent property of
  behavioral predictability). "Understanding Layer": **DEMOTED TO
  METAPHOR**, further weakened. Capability-vs-understanding: **RETIRED
  from Article 3.**
- **Article 3 classification: C — research agenda article** (not a new
  technical property, not a strong-enough synthesis given dynamic
  assurance cases already exist). Surviving candidate thesis: whether
  Contribution 2's earned per-decision reconstructability guarantee
  composes to the trajectory level — genuinely open, not yet tested.
- **Independent publication: UNCERTAIN**, conditional on further
  empirical work not yet done.
- **Article 3: NOT STARTED. Not ready to draft.**
- **O'Reilly synthesis: NOT STARTED**, unchanged.
- **Next step (exactly one action):** a human decision on whether to
  authorize the experiment `FINAL-RESEARCH-VERDICT.md` specifies
  (testing whether per-decision reconstructability composes to
  trajectory-level reconstructability) — no further unscoped research
  pass, and no Article 3 drafting, until that decision is made.

---

## Contribution 3 — trajectory-composition experiment (2026-08-25)

The experiment the prior section's "Next step" named has been
authorized, designed, pre-registered, executed, and reported. Full
record: `contribution-03/experiment/RESULT.md`,
`contribution-03/experiment/analysis/experiment-report.md`,
`contribution-03/experiment/analysis/results-summary.md`, raw data in
`contribution-03/experiment/results/`. `FINAL-RESEARCH-VERDICT.md`
updated with an appended (not rewritten) `POST-VERDICT EXPERIMENT
UPDATE` section. Prior Contribution 3 research (both the first-pass
historical review and the narrow RQ1/RQ3 follow-up) preserved
unmodified.

- **Contribution 3 empirical phase: CLOSED**, pending separate
  authorization to draft Article 3.
- **Result: H1 supported.** Per-decision reconstructability
  (Local Decision Reconstruction = 1.00, both regimes, all 6 cases) does
  not necessarily compose into trajectory-level reconstructability
  (Trajectory Identifiability = 0.33 without the cross-decision relation
  vs. 1.00 with it). No false confidence occurred in this run
  (Dependency Edge Accuracy = 1.00, False Global Confidence Rate = 0.00
  across all cases) — a genuine, disclosed asymmetry with Contribution
  2's Case 8 finding (which did produce false historical confidence),
  attributable to testing a structurally different mechanism, not to
  this experiment being more favorable in general.
- **Article 3 consequence:** technical article now survivable, narrowly
  framed as "trajectory reconstructability requires an explicit retained
  cross-decision relation, not merely more per-decision detail" —
  extending, not replacing, Contribution 2's "retained is not consumed"
  thesis. "Understanding Layer" and "capability-vs-understanding"
  remain retired from Article 3, per the prior verdict.
- **Article 3: still NOT STARTED. Still not ready to draft** — this
  update closes the empirical precondition the prior verdict left open;
  it does not itself authorize drafting.
- **O'Reilly synthesis: NOT STARTED**, unchanged. One consequence
  paragraph recorded (not drafted) in
  `contribution-03/experiment/analysis/experiment-report.md`.
- **Next step (exactly one action):** a human decision on whether to
  authorize drafting Article 3, using the narrow framing above — no
  further experiments, and no Article 3 drafting, until that decision is
  made.

---

## Contribution 3 — Article 3 draft-v1 (2026-08-25)

The prior section's "Next step" has been authorized and completed.
Full record: `contribution-03/article/draft-v1.md` (3,257 words),
`contribution-03/article/editorial-notes.md`,
`contribution-03/article/draft-v1-audit.md`. Title: "When
Reconstructable Decisions Produce an Unreconstructable System." Prior
Contribution 3 research and the experiment results are preserved
unmodified; Contribution 2's frozen article and results are preserved
unmodified.

- **Contribution 3 research: COMPLETE.**
- **Empirical phase: CLOSED.**
- **Article 3 draft-v1: COMPLETE.**
- **Drafting phase: IN REVIEW.**
- **"Understanding Layer": RETIRED as technical architecture** — zero
  resurrection in draft-v1 (verified by grep, `draft-v1-audit.md`).
- **Capability-vs-understanding: RETIRED from Article 3** — zero
  resurrection in draft-v1 (verified by grep, `draft-v1-audit.md`).
- **Thesis drafted:** decision-level reconstructability does not
  necessarily compose into trajectory-level reconstructability; the
  missing ingredient is a preserved cross-decision dependency relation,
  not a new mechanism. Framed as an extension of Contribution 2's
  "retained is not consumed" thesis, one level up.
- **Novelty framing:** controlled empirical demonstration, not a new
  provenance/graph-theory/observability/diagnosability result — five
  real citations used (W3C PROV, OpenTelemetry, Fowler's Event Sourcing,
  Sampath et al. 1995 diagnosability, Bakirtzis & Topcu 2022
  compositional verification), all independently verified before
  drafting.
- **O'Reilly synthesis: NOT STARTED**, unchanged. One framing note
  recorded (not drafted) in `contribution-03/article/editorial-notes.md`.
- **Article 3: draft-v1 only. NOT marked complete.** No draft-v2, no
  submission.
- **Next step (exactly one action):** human editorial review of
  Contribution 3 draft-v1 — no draft-v2, no submission, no O'Reilly
  revision, no further experiments, until that review authorizes the
  next step.

---

## Publication architecture — human editorial decision (2026-08-25)

Following the completed adversarial review of Contribution 3 draft-v1
(`contribution-03/article/review/VERDICT.md`), a human editorial
decision on publication architecture was made. Full record:
`PUBLICATION-ARCHITECTURE-FINAL.md`,
`contribution-03/FINAL-EDITORIAL-DISPOSITION.md`,
`contribution-03/ARTICLE-2-INTEGRATION-CANDIDATES.md`,
`OREILLY-SYNTHESIS-MAP.md`. This is a publication-architecture decision,
not a finding of factual invalidity — every experiment, draft, and
review in Contribution 3 remains part of the permanent research record,
preserved unmodified. Superseded-architecture notices were added
(append-only, historical analysis left intact) to
`publication-architectures.md`, `recommended-program.md`,
`research-roadmap.md`, `contribution-boundaries.md`, `oreilly-role.md`,
and `book-implications.md`.

- **Contribution 1:** independent core article. Unchanged.
- **Contribution 2:** independent core article, frozen. Unchanged.
- **Contribution 3:** research complete; standalone full-article
  development closed; retained as supporting research note ("Trajectory
  Reconstruction and Honest Ambiguity"). `draft-v1.md` frozen as a
  historical research-note draft; no draft-v2 authorized.
- **Three-standalone-article architecture: CLOSED / SUPERSEDED** by the
  two-core-articles-plus-supporting-research-note architecture in
  `PUBLICATION-ARCHITECTURE-FINAL.md`.
- **Current publication architecture:** 2 core articles + 1 supporting
  research note + future O'Reilly synthesis (not yet drafted).
- **Understanding Layer: RETIRED.** Confirmed not resurrected anywhere
  in the new governance documents (grep-checked in
  `OREILLY-SYNTHESIS-MAP.md` §8).
- **Capability-vs-understanding: RETIRED.** Same confirmation.
- **O'Reilly: NOT YET DRAFTED.** A synthesis map exists
  (`OREILLY-SYNTHESIS-MAP.md`) — a dependency map, not publication prose.
  Recommended format: article first, book later (§11).
- **Article 2 integration:** identified as candidates only
  (`contribution-03/ARTICLE-2-INTEGRATION-CANDIDATES.md`), recommendation
  KEEP SEPARATE for now / USE ONLY IN O'REILLY. Article 2's frozen
  `draft-v2.md` was not modified.
- **Exact next step:** human review of `OREILLY-SYNTHESIS-MAP.md` before
  authorizing O'Reilly drafting — no O'Reilly drafting, no Article 1/2
  modification, no Article 3 v2, no C3-into-C2 merge, no further
  experiments, until that review authorizes the next step.

---

## O'Reilly synthesis review — final human-reviewed decision (2026-08-25)

The prior section's "Next step" has been executed: an adversarial
re-review of `OREILLY-SYNTHESIS-MAP.md`'s own recommendation, not a
re-trust of it. Full record: `OREILLY-FINAL-BRIEF.md` (new,
authoritative for drafting), and an appended "FINAL HUMAN-REVIEWED
SYNTHESIS DECISION" section in `OREILLY-SYNTHESIS-MAP.md` (historical
reasoning above it left unmodified).

- **O'Reilly synthesis review: COMPLETE.**
- **Final thesis:** "A production AI decision must be authorized before
  it happens and explainable after it happens — and neither is possible
  without preserving the right relations, not just the right artifacts,
  around the decision itself, not just the model that produced it." This
  **replaces** the synthesis map's prior Rank-1 recommendation
  ("Auditability is relational"), which is demoted to a supporting
  subthesis after adversarial testing found it flattens the earned
  control/reconstruction duality and risks a relational-database
  misreading for an ML/MLOps audience.
- **Final article format:** Tier B — one 3,500–5,000 word deep O'Reilly
  article. Multi-part series and book formats explicitly considered and
  not selected; book proposal at original scope explicitly rejected.
- **GO/NO-GO: GO WITH CONDITIONS.** Six drafting-discipline conditions
  recorded in `OREILLY-FINAL-BRIEF.md` §"GO / NO-GO" (combined-thesis
  wording; the "not only the model" qualifier; Contribution 3 capped at
  one ~400-word section; dynamic/continuous assurance-case literature
  cited explicitly; no forced umbrella noun; 3,500–5,000 word target).
  No blocking research gap was found or claimed.
- **Contribution 3 role in the article:** one short section (Option A),
  honest-ambiguity principle only, no experiment-internal vocabulary.
- **Understanding Layer / capability-vs-understanding:** both confirmed
  RETIRED, grep-checked against every new document this pass — every
  occurrence found is inside an explicit prohibition/retirement
  statement, never a live claim.
- **Book proposal:** not modified; not reopened at original scope.
- **Exact next step:** "Draft O'Reilly article from
  `OREILLY-FINAL-BRIEF.md`." No further research, no experiments, no
  reopening of Contributions 1–3, until that drafting pass is
  separately authorized.
