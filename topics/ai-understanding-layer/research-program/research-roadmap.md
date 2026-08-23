---
id: note-research-program-research-roadmap
title: "Research Programme — Execution Roadmap"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, roadmap]
refs: []
---

## Research Programme — Execution Roadmap

Scope: Task 12. An execution sequence for the recommended architecture (`recommended-program.md`). Every step specifies its research question, why it comes now (not earlier or later), required reading/prior-art work, required formalization, required empirical work, required implementation work, deliverable, stop condition, and what must be learned before the next step. The next step is never assumed to be prose drafting unless the step's own logic actually calls for it.

---

### Step 1 — Decision-Level Control research and drafting *(complete)*

- **Research question:** What must an architecture make explicit before an AI output causes a consequential action, and how is that made to actually constrain behavior?
- **Why this comes now:** It was the branch discovered first, during initial engagement with Source B, and required no dependency on anything else in the graph.
- **Required reading / prior-art work:** Done — `article-01-decision-level-control/novelty-audit.md` against access control, admission control, supply-chain security, CI/CD, ML model registries.
- **Required formalization:** Done — the evidence/requirements/authority/gate decomposition, the ALLOW/BLOCK/ESCALATE outcome model.
- **Required empirical work:** None required to stand; `empirical-program.md` Programme 3 remains available as optional, lower-priority strengthening.
- **Required implementation work:** None required; a reference implementation is not a prerequisite for this contribution's validity.
- **Deliverable:** `article-01-decision-level-control/` in full — spine, evidence inventory, three drafts, novelty audit, sourcing audit, self-reviewed final article.
- **Stop condition:** Met — audited (Position B, new synthesis), drafted, adversarially self-reviewed.
- **What was learned before moving on:** The model-vs-decision inversion (C1b) is the strongest sub-claim; the field's dominant prior art (XACML, Sigstore) confirms no mechanism novelty, which sharpened rather than weakened the final positioning; merging the inversion argument with the concrete gate pattern produced a stronger piece than either alone.

---

### Step 2 — Preservation-cluster prior-art audit *(complete, 2026-08-23)*

- **Status:** Complete. Full adversarial audit executed in
  `contribution-02/` (`problem-formalization.md`, `prior-art-audit.md`,
  `collision-tests.md`, `temporal-semantics.md`, `minimal-decision-record.md`,
  `novelty-verdict.md`, `empirical-next-step.md`, `deferred-contribution-03.md`).
  Verdict: **B — narrowed survival.** Every individual primitive needed
  (bitemporal valid-time semantics, W3C PROV lineage, in-toto/Sigstore
  signed attestation, event-sourced replay) already exists in mature,
  separate literatures and was tested against nine explicit collision
  objections, none of which defeats the contribution outright. What
  survives is narrower and more precise than "State Is Not Knowledge": no
  existing mechanism, applied by default, binds a decision at t0 to the
  specific temporally-valid versions of the policy, evidence, and authority
  that made it valid — versioning existing elsewhere is not the same as
  that binding being recorded (`collision-tests.md`, Objection 8). "State
  Is Not Knowledge" is retired as the technical thesis statement (retained
  only as practitioner-register color); the recommended precise
  formulation and its shorthand ("Versioned is not bound") are in
  `contribution-02/novelty-verdict.md`. The repository-audit method
  proposed in Source B and re-scoped in `empirical-program.md` is rejected
  for Contribution 2 specifically (it cannot observe the object of
  interest — runtime decision-time binding is not code-visible); the
  controlled-failure/reconstruction experiment survives with a required
  refinement (three preservation regimes, not two, to isolate the binding
  property from mere artifact versioning — `contribution-02/
  empirical-next-step.md`).
- **What must be learned before moving on — resolved:** C6/C7's claims
  survive adversarial prior-art testing, narrowed to the binding-specific
  formulation above. Human review of this audit is the required next step
  before Step 3 (experiment design) proceeds on the updated three-regime
  design.

- **Original research question:** What existing mechanisms across software engineering, database systems, and archival/digital-preservation practice already address "does retained state suffice to reconstruct why a past decision was valid," and where do they stop for AI-specific transient context?
- **Why this comes now:** Per `claim-graph.md`'s branching-dependency finding, Contribution 2 depends only on Contribution 1's shared premise (C1), not on Contribution 1's architecture — so this can and should begin immediately rather than waiting. It is also the step that resolves the largest concrete gap identified by the adversarial self-review's Q5 (imprecision of "state is not knowledge") and directly informs the reconstruction-experiment design in Step 3.
- **Required reading / prior-art work:** SLSA/in-toto, deepened specifically on durability-over-time (not just admission-time checking, which is already covered from Contribution 1's work); bitemporal/point-in-time-recovery database design; digital-preservation and archival-science practice (untouched so far); distributed-systems observability-vs-explainability literature; incident-investigation practice in safety-critical industries (flagged by Inversion E in `conceptual-inversions.md`, not yet researched); any existing regulatory record-keeping requirements resembling decision-context preservation (e.g., EU AI Act logging obligations — flagged in `../notes/intellectual-progression.md` Task 8, not yet investigated).
- **Required formalization:** A technically precise restatement of "state is not knowledge" (per the Q5 precision concern in `recommended-program.md`) — this is a formalization task, not just a literature review.
- **Required empirical work:** None yet — this step is research, not experimentation.
- **Required implementation work:** None.
- **Deliverable:** A prior-art matrix and adversarial collision test for Contribution 2, comparable in rigor and format to `article-01-decision-level-control/novelty-audit.md`.
- **Stop condition:** The matrix and collision test exist with comparable rigor to `novelty-audit.md`, and a precise technical formulation of C6 has been adopted.
- **What must be learned before moving on:** Whether C6/C7's claims survive adversarial prior-art testing the way C5's did, and what the strongest genuine distinction actually is once compared against real prior art — currently only a hypothesis (Inversion D, defensibility 3/5, precisely because this audit has not yet happened).

---

### Step 3 — Design the reconstruction experiment *(COMPLETE — DESIGN ONLY, 2026-08-23)*

- **Status: COMPLETE — DESIGN ONLY.** Full design executed in
  `contribution-02/experiment-design/` (`research-question.md`,
  `experimental-system.md`, `preservation-regimes.md`,
  `perturbation-matrix.md`, `reconstruction-task.md`,
  `metrics-and-scoring.md`, `validity-and-confounders.md`,
  `preregistered-interpretation.md`, `implementation-spec.md`, `README.md`).
  **The experiment has NOT been implemented. The experiment has NOT been
  executed. There are NO experimental results — positive, negative, or
  partial — anywhere in this repository.**
- **Locked primary question:** Given independent, complete version
  histories for policy, authority, evidence, and model (Regime B), does
  that versioning alone suffice for temporally correct reconstruction, or
  is an explicit decision-time binding (Regime C) required? Regime A
  (bare) serves only as a floor/manipulation-check condition, not part of
  the primary comparison.
- **Design verdict:** READY FOR IMPLEMENTATION (`experiment-design/README.md`,
  Task 18) — the B-vs-C distinction is well-defined (a verified
  information-equivalence table shows C adds no new underlying facts, only
  an explicit version-identifier binding), and the perturbation matrix
  includes cases pre-registered to falsify the thesis if the theorized
  mechanism (the transaction-time/valid-time confound under retroactive
  correction, and interval-matching ambiguity under concurrency) does not
  manifest.
- **Primary metric:** Temporal Correctness; primary diagnostic metric:
  False Historical Confidence (`metrics-and-scoring.md`).
- **Method note:** Uses a pre-registered, pattern-based diagnostic
  evaluation over a deliberately constructed ~10-case matrix, not
  frequentist significance testing — the case matrix is not a random
  sample and does not support a p-value, and the design says so explicitly
  rather than manufacturing false statistical authority.
- **Investigator choice:** A deterministic, rule-based reconstruction
  procedure, not a human or LLM, to isolate the information-architecture
  question from investigator-skill confounds; human/LLM investigators are
  explicitly deferred to a secondary, later experiment.
- **What must be learned before moving on — now the actual next action:**
  Whether human review of this design approves it for implementation.
  Per the frozen workflow recorded in `CHECKPOINT-2026-08-23.md`,
  implementation and execution require explicit human authorization and
  do not proceed automatically from design completion.

- **Original research question (superseded by the locked question above):** Given a fully evidenced, properly gated decision, does realistic context drift make that decision's original validity unreconstructable using only currently-standard artifacts?
- **Why this comes now:** Cannot be designed accurately before Step 2 establishes what "currently-standard artifacts" realistically includes as a baseline.
- **Required reading / prior-art work:** None beyond Step 2's output.
- **Required formalization:** The reconstruction-completeness scoring protocol, the blinded-auditor methodology, and the condition matrix (which context elements drift vs. are versioned) — full skeleton already sketched in `empirical-program.md`, Programme 2, but needs a rigorous, reviewable specification, not just the sketch.
- **Required empirical work:** None yet — design only.
- **Required implementation work:** A specification for the minimal testbed (built around Contribution 1's own running example); no code yet.
- **Deliverable:** An experiment design document — methodology only, no results.
- **Stop condition:** A rigorous, falsifiable design exists, reviewed specifically for whether it can actually distinguish the hypothesis from the null. **Met.**
- **What must be learned:** Whether this is feasible to run at all before committing resources, and what the minimal viable version looks like. **Resolved: yes, feasible — see `implementation-spec.md`.**

---

### Step 4 — Run the experiment / conduct the repository-audit companion study

- **Research question:** (Empirical — answered by running Step 3's design, plus `empirical-program.md` Programme 1, redesigned to target Contribution 2 rather than Contribution 1 per that document's explicit redesign note.)
- **Why this comes now:** Cannot run before the design (Step 3) exists.
- **Required reading / prior-art work:** None further.
- **Required formalization:** None further.
- **Required empirical work:** The experiment and the audit themselves — this step *is* the empirical work.
- **Required implementation work:** The minimal testbed specified in Step 3, actually built.
- **Deliverable:** Results, written up honestly, including negative results if the hypothesis is not supported (a genuinely live possibility per `empirical-program.md`'s stated falsification conditions).
- **Stop condition:** Results obtained, whatever they show.
- **What must be learned:** Whether C6's diagnosis actually holds under test, and by how much — this determines how strongly the eventual Contribution 2 paper can state its central claim, and directly resolves the falsification condition specified for Programme 1 and Programme 2 in `empirical-program.md`.

---

### Step 5 — Draft the Preservation & Reconstruction paper

- **Research question:** (Synthesis of Steps 2–4.)
- **Why this comes now:** All required inputs (audit, design, results) now exist.
- **Required reading / prior-art work:** None further beyond Step 2's output, revisited in light of Step 4's results.
- **Required formalization:** Final thesis wording, informed by Step 4's actual findings rather than the hypothesis-only state this roadmap currently reflects.
- **Required empirical work:** None further — already done in Step 4.
- **Required implementation work:** None further.
- **Deliverable:** A drafted paper on Contribution 2, following the same process Step 1 used: spine → evidence inventory → draft → novelty audit → sourcing audit → final version.
- **Stop condition:** Draft exists with its own novelty/sourcing audit pair, mirroring Step 1's process.
- **What must be learned:** Whether Contribution 2 is as strong in practice as `claim-graph.md` and `conceptual-inversions.md` currently predict.

---

### Step 6 — Understanding-layer historical/prior-art audit *(can run in parallel with Steps 2–5, low dependency)*

- **Research question:** Does the historical pattern Source A claims (software engineering responding to complexity by inventing preservation mechanisms) hold up under rigorous history-of-technology review, and do the AI sub-fields (explainability, interpretability, observability, provenance, governance, auditability) actually talk past each other the way Source A claims, or is that a simplification?
- **Why this comes now (or in parallel):** Technically independent of Steps 2–5 (a different claim cluster, per `claim-graph.md`'s branching structure) — may begin at any time. Explicitly should **not** be turned into a drafted paper until Steps 1 and 5 are complete, per the terminal-thesis protection reconfirmed in `recommended-program.md`.
- **Required reading / prior-art work:** The actual history of version control (Git and its predecessors — including honestly investigating whether Git's real origin, distributed collaboration and merge-conflict resolution, complicates the "preserving knowledge" framing, a concern raised explicitly in `claim-graph.md`'s C9m entry), transaction logs, and distributed tracing as engineering responses, not just technical descriptions; a survey of how the explainability/interpretability/observability/governance/auditability literatures describe their own relationships to each other and to one another's fields.
- **Required formalization:** A precise, defensible statement of the "fragmentation" claim — currently asserted rhetorically by Source A, not yet tested against how those research communities describe themselves.
- **Required empirical work:** None — explicitly not an empirical claim (`empirical-program.md`'s scoping decision).
- **Required implementation work:** None.
- **Deliverable:** A literature/history audit for Contribution 3, comparable in rigor to `novelty-audit.md`.
- **Stop condition:** Audit complete, covering both the historical-pattern claim and the fragmentation claim with real sources, and explicitly addressing the missing generalizing premise flagged in `recommended-program.md` Q3 (does decision-specific reconstruction actually generalize to system-behavior-wide understanding, or must the thesis be scoped down).
- **What must be learned:** Whether C9m/C9a's central historical analogy survives scrutiny the way C1–C5's prior-art comparisons did, and whether the "fragmentation" framing is fair or needs qualification.

---

### Step 7 — Draft The Understanding Layer capstone

- **Research question:** (Full synthesis of Contributions 1 and 2, informed by Step 6.)
- **Why this comes now:** Requires Steps 1, 5, and 6 complete — the terminal node of the graph, sequenced last by design, not by default.
- **Required reading / prior-art work:** None further beyond Step 6's output.
- **Required formalization:** Final resolution of whether C9's thesis is stated at full generality (system behavior broadly) or scoped down to decisions specifically, per the Q3 gap.
- **Required empirical work:** None — by design.
- **Required implementation work:** None — C9b is explicitly framed as a problem statement, not a specified design (per `claim-graph.md`).
- **Deliverable:** A drafted capstone paper, only after Steps 1, 5, and 6 are complete.
- **Stop condition:** Draft + audit, with explicit confirmation that it does not overclaim beyond what Steps 1–6 actually established.
- **What must be learned:** Whether the programme's terminal thesis, once properly earned, actually lands — or whether the audits along the way revealed it needs further qualification.

---

### Step 8 — Book-level synthesis *(deferred, out of scope for now)*

Revisit `book-implications.md`'s three-part arc and the Option 3 capstone question from `oreilly-role.md` for real drafting, only after Step 7. Not scheduled here.

---

### Immediate next action

**Step 2 — the Preservation-cluster prior-art audit.** Not prose drafting. A literature/primary-source research task, in the same style and rigor as `article-01-decision-level-control/novelty-audit.md`, scoped to Contribution 2 (C6+C7), with a specific deliverable of technically precise-formulation work (Q5's gap) alongside the prior-art matrix itself.
