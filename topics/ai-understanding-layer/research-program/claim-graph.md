---
id: note-research-program-claim-graph
title: "Research Programme — Problem Levels and Claim Graph"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, claim-graph, abstraction-levels]
refs: []
---

## Research Programme — Problem Levels and Claim Graph

Scope: this document answers Tasks 1 and 2 of the second, deeper research-architecture pass. It supersedes the first pass's version of this file in detail (more claim nodes, explicit A–Q mapping) while confirming its structural conclusion. It draws directly on both primary sources in full (not on later summaries of them), on `../notes/intellectual-progression.md`, and on everything produced under `../article-01-decision-level-control/`, including `novelty-audit.md` and `sourcing-audit.md`, which is treated as research output — the model-vs-decision inversion and the human-in-the-loop critique were both discovered during that drafting work, not present in either source document beforehand.

### Deepest research question (re-derived, not assumed)

The brief's provisional formulation bundles four properties — authorized, auditable, reconstructable, understandable — into one sentence. The claim graph below shows these resolve into two problem clusters sharing one root, not a single continuum. The strongest formulation states both clauses explicitly:

> As AI-derived outputs increasingly cause consequential, real-world state changes, what distinct architectural commitments are required — beyond producing good outputs — first, to govern whether a given action is authorized to happen at all, and second, to preserve enough knowledge about that authorization for it to remain understandable after the system that produced it has changed?

This formulation is retested (and survives) under the adversarial self-review in `recommended-program.md` — in particular the question of whether the second clause is actually entailed by the first, which it is not (see the dependency analysis below and Task 3's discussion of the missing generalizing premise between the two clusters).

---

## Task 1 — Abstraction levels, tested against the exact questions posed

### Model level

*What does model-centric ML engineering actually control?* It controls the model artifact itself: what gets trained, how it is evaluated, which version is registered, which version is deployed. Confirmed real (not a straw man) by direct research into MLflow, Databricks Unity Catalog, and Vertex AI Model Registry documentation (`../article-01-decision-level-control/novelty-audit.md`) — this is genuinely how production ML governance is organized today, in the tools that exist to do it. It is not itself a claim in this programme; it is the baseline the Decision-level claims are defined against.

### Decision level

*What changes when the unit of control moves from model to consequential decision?* The object being governed changes from "a versioned artifact" to "a proposed, evidence-backed, authorized state transition." This is where Source B's entire book proposal, and the bulk of `article-01-decision-level-control/`, operates. Evidence that this is a genuinely distinct level, not just a rebranding of the model level: a model can be perfectly evaluated and registered (model level fully satisfied) while a specific proposed action using its output is neither evidenced nor authorized (decision level unaddressed) — the two can vary independently.

### Historical / provenance level

*What must survive after the decision if we later need to know why it was valid?* Source A §5's explicit territory: not the decision's outcome (which is trivially retained — a record exists) but the *conditions* that made it valid at the time — which prompt version, which retrieval corpus state, which policy interpretation, which model version. Confirmed distinct from the Decision level by the same independence test: a decision can be perfectly gated and evidenced at t0 (Decision level fully satisfied) and still become unreconstructable at t0+6 months once its surrounding context has drifted (Historical/provenance level failing) — Source A's own worked example (§5, "six months after an important deployment decision... nothing has failed... the system simply never treated that decision context as something that needed to be preserved").

### System-knowledge / understanding level

*What happens when system capability grows faster than our mechanisms for preserving knowledge about its behavior?* The most general level — it does not ask about *decisions* specifically but about *system behavior* generally (explainability, interpretability, observability, provenance, governance, auditability treated as parallel, possibly fragmented responses to one deeper requirement). This is Source A's outer essay.

### Are these genuinely distinct levels?

Yes, on the same two tests applied in the first pass, now sharpened:

1. **Independent truth conditions**, demonstrated concretely above for each adjacent pair (Model/Decision; Decision/Historical).
2. **Independent evidence types.** Model-level claims are tested by evaluation harnesses. Decision-level claims are tested by architecture review and controlled failure experiments on enforcement. Historical/provenance-level claims are tested by reconstruction experiments (blinded-auditor protocols). Systems-knowledge-level claims are tested by historical/comparative argument and conceptual analysis, not by any experiment run on a live system.

**One genuine risk identified in this pass, not fully resolved in the first:** the move from the Historical/provenance level (which is *about decisions specifically*) to the Systems-knowledge level (which is about *system behavior generally*) is a **generalization**, not an entailment. Source A performs this generalization rhetorically but does not fully argue for it. This is flagged explicitly as a missing premise — see the dependency diagram below and the adversarial self-review in `recommended-program.md` (Q3).

### Dependency structure

```
                        MODEL LEVEL (substrate, not a claim)
                              │
                              ▼
                       DECISION LEVEL
                (C1, C1c, C1b, C2, C3, C4)
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
        DECISION-LEVEL ARCHITECTURE   HISTORICAL / PROVENANCE LEVEL
           (C5, C5h — terminal)            (C6, C7)
                                             │
                                    [MISSING / UNARGUED PREMISE:
                                     decision-specific reconstruction
                                     generalizes to system-behavior-
                                     wide understanding]
                                             │
                                             ▼
                                   SYSTEMS-KNOWLEDGE LEVEL
                                    (C8, C9m, C9a, C9b — terminal)
```

Both branches off the Decision level depend only on C1 existing — not on each other, and not on C5 being published, implemented, or correct. The bracket marks the one place in the whole graph where a logical jump exists that the sources do not fully close; it is not fatal (Source A's diagnostic claim, C9a, does not strictly require the generalization — it can be read narrowly as "AI decision behavior specifically" — but the fuller, more ambitious reading Source A clearly intends does require it, and no source material argues for the jump directly).

---

## Task 2 — Claim graph, with the A–Q hypothesis mapping

The brief's seventeen lettered hypotheses (A–Q) are mapped onto claim IDs below. Several map one-to-one; several turn out to be the same claim stated at different granularity (mergeable, per Task 3); two (C and M) are promoted to their own claim nodes in this pass because they were previously folded into other claims' prose rather than tested independently, and the brief now asks for them to be tested on their own.

| Letter | Hypothesis (as given) | Claim ID |
|---|---|---|
| A | Output is not a decision | C1 |
| B | Evaluation is not authorization | C2 |
| C | Model lifecycle and decision lifecycle are different abstractions | **C1c** (new node this pass) |
| D | The model may be an insufficient primary unit of control | C1b |
| E | Governance/documentation without enforcement does not constrain behavior | C3 |
| F | Evidence should become a first-class input to authorization | C4 |
| G | Decision-level enforcement / explicit decision boundaries | C5 |
| H | Human-in-the-loop requires explicit authority, evidence, scope, refusal, enforcement | **C5h** (new node this pass) |
| I | State is not knowledge | C6 |
| J | Current state may be insufficient to reconstruct historical decision validity | C6 (tightened restatement, not a separate claim) |
| K | Decision provenance / historical reconstruction | C7 |
| L | Evidence, policy, authority, version context may need continuity over time | C7 (specific content of the same claim, not separate) |
| M | Software engineering repeatedly creates preservation mechanisms as complexity grows | **C9m** (new node this pass) |
| N | Capability and understanding as divergence-capable variables | C8 |
| O | Capability may be scaling faster than preservation mechanisms | **C9a** (split out of what was previously undifferentiated "C9") |
| P | AI may require an architectural "understanding layer" | **C9b** (split out of what was previously undifferentiated "C9") |
| Q | Evidence-Gated AI / AIGov Core as an implementation response | Not a theory-level claim — an implementation-role question, answered fully in `aigov-role.md` |

### C1 — Output ≠ decision

- **Formulation:** An output is information produced by a system (a claim about the world). A decision is an authorized state transition. Systems that let outputs act as if already decisions have no structural checkpoint between the two.
- **Source:** Source B Ch. 3, explicit. Source A §3, explicit (partial). Developed extensively in `oreilly-submission-draft.md` / `oreilly-submission-disruptive.md`.
- **Label:** Explicit.
- **Level:** Decision.
- **Premises required:** None — foundational.
- **Claims it supports:** C1c, C1b, C2, C3, C4, C6.
- **Prior-art collision:** Low directly (domain-specific naming); moderate structurally (databases: compute vs. commit; access control: request vs. grant).
- **Evidence required:** Conceptual/definitional; illustrative example sufficient.
- **Falsifiability:** Weak — a framing move more than a testable hypothesis.
- **Novelty risk:** Low novelty claimed, correctly.
- **Independent intellectual value:** Moderate.
- **Potential publication role:** Premise only — see `contribution-boundaries.md`.

### C1c — Model lifecycle and decision lifecycle are different abstractions (new node, letter C)

- **Formulation:** The conventional ML engineering lifecycle (data → training → model → evaluation → deployment) and the decision architecture this programme proposes (output → proposed decision → evidence → authorization → transition) are not the same kind of structure and do not answer the same question. The first asks "how do we build a good model"; the second asks "what is this system allowed to do because of what the model said." Neither subsumes the other.
- **Source:** Not stated explicitly in either primary source. Crystallized during O'Reilly drafting (`oreilly-submission-disruptive.md`, "The model is not the unit of control") but distinct from C1b: C1c is a claim about *abstraction levels being different*, while C1b is the *normative conclusion* drawn from that difference (the model is insufficient as a governance object). C1c is the premise; C1b is what follows from it once you add the observation that governance is what's actually attached to the model.
- **Label:** Inferred / newly separated in this pass.
- **Level:** Bridges Model and Decision levels explicitly — this claim *is* Task 1's level-distinction, promoted to a testable node.
- **Premises required:** C1.
- **Claims it supports:** C1b.
- **Prior-art collision:** Low as a general software-engineering observation (any domain distinguishes "how the artifact was built" from "what it's authorized to do"), but the specific naming of *this* pair of lifecycles for AI/ML is not found stated this way elsewhere in the research done so far.
- **Evidence required:** Conceptual argument; the two explicit flow diagrams already built (`oreilly-submission-disruptive.md`) serve as the illustration.
- **Falsifiability:** Weak-moderate — falsifiable in principle if it could be shown the decision architecture is actually derivable from (not independent of) the model lifecycle, which would collapse the distinction; no evidence found supporting that collapse.
- **Novelty risk:** Low — explicitly framed as "these are different questions," not as an invented dichotomy.
- **Independent intellectual value:** Moderate — mostly serves as the scaffolding for C1b.
- **Potential publication role:** Premise, folded into C5's paper alongside C1/C1b — see `contribution-boundaries.md`.

### C1b — The model may be an insufficient primary unit of control (letter D)

- **Formulation:** Once outputs cause consequential actions, the model is necessary but insufficient as the object of governance: a single model participates in many decisions (summarize a document, deny a transaction, send an email, mutate a database) with different evidence, authority, and consequence profiles no model-level approval can express.
- **Source:** New synthesis during O'Reilly drafting (`oreilly-submission-disruptive.md`, "One model, many decisions"). Not present in either original source document.
- **Label:** Inferred / newly synthesized — the single most novel claim discovered by this programme's own drafting work.
- **Level:** Decision (stated as a critique of Model-level practice).
- **Premises required:** C1, C1c.
- **Claims it supports:** C5 (motivates why enforcement must attach to the decision, not the model); is Inversion A in `conceptual-inversions.md`.
- **Prior-art collision:** Moderate — confirmed real via direct research into MLflow/Databricks/Vertex documentation; access control's general request-level (not identity-level) authorization is the adjacent prior art, newly applied here.
- **Evidence required:** Conceptual argument + illustrative example (built); strengthenable by a repository audit measuring whether real governance artifacts are per-model or per-decision (see `empirical-program.md`).
- **Falsifiability:** Yes — falsified if existing model governance practice already effectively expresses per-decision authorization.
- **Novelty risk:** Correctly scoped in existing drafts (both O'Reilly drafts explicitly concede MLflow/Databricks/Vertex prior art) — see the fairness check under Q6 of the adversarial self-review in `recommended-program.md`.
- **Independent intellectual value:** Strong.
- **Potential publication role:** Currently merged into C5's paper; plausible as its own short piece, but stronger where it is — see `contribution-boundaries.md`.

### C2 — Evaluation ≠ authorization (letter B)

- **Formulation:** A model passing evaluation tells you the output is good. It does not, by itself, tell you the system may act on it.
- **Source:** Implicit in Source B Ch. 1; crystallized explicitly during O'Reilly drafting.
- **Label:** Inferred / crystallized in this programme's own drafting.
- **Level:** Decision.
- **Premises required:** C1.
- **Claims it supports:** C3, C4.
- **Prior-art collision:** High — the general access-control/AAA principle (authentication ≠ authorization) is the same shape in a different domain.
- **Evidence required:** Conceptual, illustrative.
- **Falsifiability:** Yes, in principle — falsified if eval metrics already functionally encode all authorization-relevant conditions in a given domain.
- **Novelty risk:** Low, correctly conceded.
- **Independent intellectual value:** Moderate — close to a corollary of C1.
- **Potential publication role:** Premise, merged into C5's paper.

### C3 — Governance without enforcement is descriptive (letter E)

- **Formulation:** Documenting a requirement and enforcing it are not the same act. A fully documented system can still execute a decision that violates its own stated requirements.
- **Source:** Source B, explicit ("why governance without enforcement does not work"); heavily developed across all `article-01` drafts.
- **Level:** Decision.
- **Premises required:** C1.
- **Claims it supports:** C5.
- **Prior-art collision:** Very high — the oldest, most established idea in access-control literature, confirmed in `novelty-audit.md`.
- **Evidence required:** Conceptual argument; strengthenable by repository audit or controlled failure experiment (see `empirical-program.md`).
- **Falsifiability:** Yes, directly.
- **Novelty risk:** Low as an abstract principle (textbook); the *sociologically interesting* part is that the responsible-AI documentation literature specifically has not integrated it — see Inversion C in `conceptual-inversions.md`.
- **Independent intellectual value:** Low alone; higher as an observation about the AI field's institutional history.
- **Potential publication role:** Premise, merged into C5's paper.

### C4 — Evidence, requirements, and authority are distinct (letter F)

- **Formulation:** Evidence (structured input into authorization) is not documentation attached after the fact, and is distinct from decision requirements (conditions evidence is checked against) and authority (who or what may say yes).
- **Source:** Source B Ch. 4, explicit; developed extensively across `article-01` drafts.
- **Level:** Decision.
- **Premises required:** C1, C2.
- **Claims it supports:** C5.
- **Prior-art collision:** Very high — confirmed against XACML, Cedar, in-toto in `novelty-audit.md`.
- **Evidence required:** Conceptual/design argument; architecture comparison already done.
- **Falsifiability:** Not empirically — a design recommendation.
- **Novelty risk:** Low, correctly conceded.
- **Independent intellectual value:** Moderate — connective tissue.
- **Potential publication role:** Sub-component of C5, not separable.

### C5 — Decision-level enforcement / explicit decision boundaries (letter G)

- **Formulation:** Once C1–C4 are granted, production AI needs an explicit decision layer: proposed decision + evidence bundle + decision requirements → gate → ALLOW/BLOCK/ESCALATE → authorized transition, generalizable across decision boundaries (deployment, runtime, agent tool-use), not tied to model promotion specifically.
- **Source:** Source B Chs. 6–7, explicit; the entire `article-01-decision-level-control/` body of work; `novelty-audit.md`'s explicit Position B verdict.
- **Level:** Decision (terminal node of this branch).
- **Premises required:** C1, C1c, C1b, C2, C3, C4.
- **Claims it supports:** None further within the control cluster. Cross-cluster: the artifacts C5 produces are what C6 asks whether they survive — but C6's truth does not depend on C5's correctness or implementation.
- **Prior-art collision:** Confirmed thoroughly (`novelty-audit.md`): XACML (very high), Sigstore policy-controller (very high), model registries (very high for the running example), CI/CD deployment gates (moderate). Verdict: new synthesis, not new mechanism.
- **Evidence required:** Architecture/design argument (complete); implementation/case study (**not** AIGov Core — see `aigov-role.md`); strengthenable by controlled failure experiments and repository audit.
- **Falsifiability:** Partially — "generalizes beyond model promotion" is falsifiable by showing runtime/agent decision boundaries can't sustain gates (e.g., latency constraints).
- **Novelty risk:** Correctly and explicitly disclaimed throughout `article-01` — "the mechanisms are old, the placement is the argument."
- **Independent intellectual value:** Yes — complete, three-times-drafted, audited.
- **Potential publication role:** **Strongest standalone candidate in the graph.** This is what `article-01-decision-level-control/` already is.

### C5h — Human-in-the-loop requires explicit authority, evidence, scope, refusal, enforcement (letter H, new node this pass)

- **Formulation:** A person present in a workflow is not, by itself, a control architecture. A genuine human-in-the-loop authorization path must make explicit: what evidence the approver sees, what specifically they are authorized to approve, what happens on refusal (is refusal actually enforced, or does the system proceed anyway on a timeout), and whether the approval itself is recorded and attributed. Without these, "human-in-the-loop" is a person standing near a button — a weaker version of the undocumented output-to-action transition the whole programme is about.
- **Source:** Not present in either original source document. Developed during O'Reilly drafting (`oreilly-submission-disruptive.md`, the human-in-the-loop paragraph within "One model, many decisions").
- **Label:** Inferred / newly synthesized during this programme's own work.
- **Level:** Decision (a refinement of C5's ESCALATE semantics specifically).
- **Premises required:** C5 (specifically, the ESCALATE outcome).
- **Claims it supports:** None further — a terminal refinement, not a load-bearing node for anything downstream.
- **Prior-art collision:** Moderate — MCP's human-in-the-loop tool-consent model (client presents prompt/action, user may edit/approve/reject) is a real, close analogue, confirmed via web research during the novelty audit for `article-01` (though not incorporated into the final six-analogy prior-art section of the article itself, since it was cut for length — see `sourcing-audit.md`/`novelty-audit.md` for the underlying research). General human-factors/automation-bias literature ("humans rubber-stamp systems they don't understand") is adjacent but not yet reviewed for this claim specifically.
- **Evidence required:** Conceptual argument (built); a repository audit could check whether real HITL approval steps actually specify authority/evidence/refusal-enforcement or are informal by default.
- **Falsifiability:** Yes — falsified by showing real HITL implementations already routinely specify these five properties (would make the critique moot).
- **Novelty risk:** Moderate — this is a genuinely useful, checkable critique, but it risks being read as a truism ("of course approval steps need clear authority") if not grounded in a concrete failure case; the article's current single-paragraph treatment is closer to a sharp observation than a developed argument.
- **Independent intellectual value:** Moderate — a strong section, not (by itself) a paper.
- **Potential publication role:** Currently a subsection of C5's paper. Could be expanded into its own short piece on agent/HITL authorization specifically if the agent-safety literature is engaged more deeply — flagged as an option, not recommended as a priority (see `contribution-boundaries.md`).

### C6 — State is not knowledge (letters I and J)

- **Formulation:** Current system state — even including stored decision and evidence records — is not sufficient to reconstruct the conditions under which a past decision was considered valid, because the surrounding context (prompts, retrieval corpus, policy interpretation, external tool behavior) is transient by default and was never treated as a persistent engineering artifact.
- **Source:** Source A §5, explicit (the core diagnostic claim; the six-months-later auditor scenario, verified verbatim against the source in this pass).
- **Level:** Historical/provenance.
- **Premises required:** C1 only. Explicitly does **not** require C5.
- **Claims it supports:** C7.
- **Prior-art collision:** Moderate — SLSA/in-toto anticipate the solution shape (durable, signed records) but were not built for AI-specific transient context. **Not yet audited with `novelty-audit.md`'s rigor** — the single largest concrete research gap for this cluster (see `empirical-program.md` and `research-roadmap.md`).
- **Evidence required:** Conceptual argument (built); genuinely amenable to a controlled failure experiment and repository audit — see `empirical-program.md` for full designs.
- **Falsifiability:** **Yes, strongly — the most empirically falsifiable claim in the whole graph.**
- **Novelty risk:** Low as the general observability-doesn't-equal-understanding point; higher and more defensible as applied specifically to AI's transient context types (prompts, live retrieval corpora, policy-service interpretation), which existing preservation tooling was not built to capture.
- **Independent intellectual value:** Strong.
- **Potential publication role:** Standalone-worthy, merged with C7.

**Precision concern flagged in this pass (adversarial self-review Q5):** "knowledge" is doing significant informal work in this formulation. A technically tighter restatement — e.g., "retained system state does not entail retained justificatory context" or "persistence of outcome ≠ persistence of the conditions that made the outcome valid" — should be adopted before this claim is formalized for a rigorous audience. The evocative phrase is appropriate for practitioner framing; it is not yet precise enough for a systems paper's thesis statement.

### C7 — Decision provenance / evidence continuity (letters K and L)

- **Formulation:** Preserving which prompt, policy, model, and retrieval-corpus version applied at decision time must become an explicit, versioned architectural concern — distinct from decision-time enforcement (C5) and from evidence merely existing (C4).
- **Source:** Source A §6–7, explicit (partial) — and, verified precisely in this pass, this is what Source A §7 actually describes AIGov Core's design objective as being: "to preserve not only the outcome of a decision, but also the evidence, authority, policy context, and assumptions that made the decision valid when it was taken." See `aigov-role.md` for the full correction this implies.
- **Level:** Historical/provenance.
- **Premises required:** C6.
- **Claims it supports:** Feeds C9m/C9a/C9b as one instance of the general pattern; is the architectural-response mirror of C5, for the preservation branch.
- **Prior-art collision:** SLSA/in-toto is the closest analogue, more directly relevant here than for C4/C5, since C7 is specifically about durability over time, which is in-toto's actual design goal.
- **Evidence required:** Architecture/design argument; implementation/case study (AIGov Core, as motivation only, not evidence — see `aigov-role.md`).
- **Falsifiability:** Yes, via the same reconstruction-experiment design as C6.
- **Novelty risk:** Needs its own audit — not yet tested against the digital-preservation/archival-science literature, a genuinely untouched domain for this programme.
- **Independent intellectual value:** Yes, but structurally mirrors C5's relationship to C1–C4.
- **Potential publication role:** Merges with C6 into one paper — see `contribution-boundaries.md`.

### C8 — Capability and understanding as independent variables (letter N)

- **Formulation:** Capability and understanding are distinct, non-interchangeable engineering variables that can diverge. The AI industry's dominant progress metrics (benchmarks, evaluations, leaderboards) measure only the former.
- **Source:** Source A, explicit (the extended "optimizing the wrong variable" passage).
- **Level:** Systems-knowledge.
- **Premises required:** Benefits from C6/C7 as concrete grounding but is logically somewhat independent.
- **Claims it supports:** C9a, C9b.
- **Prior-art collision:** Moderate/indirect — Sculley et al. 2015 (technical debt), "observability ≠ understanding" folklore (stated within Source A itself). Not yet rigorously audited.
- **Evidence required:** Conceptual argument; genuinely hard to operationalize (how do you quantify "understanding" independently of capability?).
- **Falsifiability:** Weak — the clean empirical test this needs does not currently exist.
- **Novelty risk:** Moderate-high if overclaimed; Source A itself concedes engineers "recognize this possibility intuitively," which bounds the claim to a critique of institutional measurement culture, not a discovery of a hidden fact.
- **Independent intellectual value:** Yes, portable beyond AI — but risks being too unfalsifiable to stand alone.
- **Potential publication role:** Merge into C9 — see `contribution-boundaries.md`.

### C9m — The recurring preservation pattern in software engineering (letter M, new node this pass)

- **Formulation:** Software engineering has repeatedly responded to rising complexity by inventing mechanisms that preserve knowledge current state cannot recover: version control (code history), transaction logs (state-transition history), distributed tracing (execution history). This is a genuine, recurring engineering pattern, not a one-off coincidence.
- **Source:** Source A §2, explicit; restated throughout the "Why capability is advancing faster than understanding" essay.
- **Label:** Explicit, but — critically — **treated in the prior pass as embedded inside C9's formulation rather than tested as its own premise.** This pass promotes it to its own node because Inversion G (see `conceptual-inversions.md`) specifically asks whether this pattern-claim itself survives prior-art testing, independent of whether AI is currently repeating or breaking it.
- **Level:** Systems-knowledge (premise for C9a/C9b).
- **Premises required:** None directly — a historical/comparative claim about software engineering generally, testable on its own terms without reference to AI at all.
- **Claims it supports:** C9a, C9b.
- **Prior-art collision:** **Not yet audited.** This is the single largest concrete research gap in the whole programme, larger even than C6/C7's gap, because it requires genuine history-of-technology research (why did version control, transaction logs, and distributed tracing emerge when they did, and is "preserving knowledge" actually the right characterization of what they were for, versus a retrospective narrative imposed after the fact) — not yet done at all.
- **Evidence required:** Dedicated historical/comparative literature review — see `research-roadmap.md`, Step 6.
- **Falsifiability:** Moderate — this is actually more falsifiable than C8 or C9a/C9b, since it makes a checkable historical claim (were these tools built in response to complexity-driven knowledge loss, or for other primary reasons — e.g., Git's actual origin was distributed collaboration and merge conflict resolution, not "preserving knowledge" as such, which is a real complication worth investigating honestly).
- **Novelty risk:** Low as a set of facts (these tools obviously exist); the risk is entirely in the *interpretive framing* ("they are all instances of one pattern") which has not been tested against how historians of software engineering or the original designers of these tools actually describe their motivations.
- **Independent intellectual value:** High — this is arguably the single best candidate for "the deepest, most defensible framing device across both clusters," precisely because it is checkable in a way C8/C9a/C9b are not.
- **Potential publication role:** Load-bearing premise for C9, not separable from it, but deserves the most rigorous individual research attention of any node feeding the terminal thesis.

### C9a — Capability may be scaling faster than preservation mechanisms (letter O)

- **Formulation:** AI may be the first major computing paradigm in which capability is scaling faster than the mechanisms required to preserve knowledge about system behavior. (The diagnostic/comparative half of what the prior pass called "C9," now split out per `../notes/intellectual-progression.md` Task 6's own finding that this half is stated more confidently in Source A than the architectural-response half.)
- **Source:** Source A, explicit (closing sentence, restated multiple times, verified verbatim in this pass).
- **Level:** Systems-knowledge (terminal, diagnostic).
- **Premises required:** C6, C7, C8, C9m.
- **Claims it supports:** C9b (but does not strictly entail it — a diagnosis does not by itself require a particular architectural cure).
- **Prior-art collision:** Not yet audited (shares C9m's gap).
- **Evidence required:** Synthesis of C6–C9m; historical/comparative argument. Not an experiment (see `empirical-program.md`'s explicit scoping decision).
- **Falsifiability:** Weak — diagnostic/interpretive, not a single testable hypothesis, though somewhat more falsifiable than C9b since it makes a comparative-rate claim that could in principle be contradicted by evidence of AI-specific preservation tooling actually keeping pace (a finding this programme has not looked for).
- **Novelty risk:** This is the terminal, most ambitious claim; risk is entirely in premature publication, not in the claim's content per se.
- **Independent intellectual value:** Very high.
- **Potential publication role:** Terminal capstone, sequenced last.

### C9b — AI may require an architectural "understanding layer" (letter P)

- **Formulation:** Closing the gap C9a diagnoses may require an explicit architectural layer whose purpose is not to increase capability but to preserve the conditions under which system behavior remains knowable.
- **Source:** Source A, explicit, but hedged more heavily than C9a — "whether this approach represents the right abstraction remains an open question" (§7, re: AIGov Core, quoted precisely).
- **Level:** Systems-knowledge (terminal, prescriptive).
- **Premises required:** C9a.
- **Claims it supports:** None — terminal.
- **Prior-art collision:** Not yet audited.
- **Evidence required:** None currently exists beyond the hedged assertion itself — Source A explicitly declines to specify what this layer's interfaces or components would be, and AIGov Core (the closest candidate implementation) does not, per Source A's own description, actually specify gate/enforcement mechanics of any kind (see `aigov-role.md`).
- **Falsifiability:** Very weak — currently closer to a call-to-action than a testable architectural claim.
- **Novelty risk:** **Highest in the graph.** This is the answer to adversarial self-review Q4 (`recommended-program.md`): as currently developed, this is primarily a memorable label, not a specified architecture. Publishing it as though it were a worked design would overclaim; publishing it as an open problem statement is defensible.
- **Independent intellectual value:** High as a research agenda-setting claim; low as a specified design.
- **Potential publication role:** Terminal, and should be framed explicitly as a problem statement / call for architecture, not as a proposed solution — a scoping decision, not a suppression of the claim.
