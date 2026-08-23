---
id: note-research-program-contribution-boundaries
title: "Research Programme — Contribution Boundaries and Minimum Independent Set"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, contribution-boundaries, falsification]
refs: []
---

## Research Programme — Contribution Boundaries and Minimum Independent Set

Scope: Tasks 4 and 5. Tests every candidate contribution named in the brief, plus the new claim nodes from `claim-graph.md` (C1c, C5h, C9m, and the C9a/C9b split), against the ten-question falsification test, then derives the smallest set of genuinely independent contributions.

---

## Task 4 — Falsifying the candidates

Each candidate is tested against: (1) distinct research question, (2) independently-wrong-able thesis, (3) own evidence, (4) own prior-art literature, (5) different abstraction level, (6) strengthened by merging, (7) salami-slicing risk if separated, (8) risk of consuming later novelty, (9) substantial enough alone, (10) better as a section.

### Model Outputs Are Not Decisions (C1)

Distinct question: weakly. Independently wrong-able: barely — closer to a stipulated distinction. Own evidence: minimal. Own literature: thin. Different level: no, this claim *establishes* the level boundary rather than sitting inside one. Strengthened by merging: yes, dramatically. Salami risk if separated: high. Consumes later novelty: no. Substantial alone: no — one-page framing note. Better as a section: yes.

**Verdict: premise, merge into C5's paper.**

### Evaluation Is Not Authorization (C2)

Same pattern as C1 across all ten questions — thin alone, well-trodden prior art (AAA triad), no independent evidentiary path.

**Verdict: premise, merge into C5's paper.**

### Model Lifecycle vs. Decision Lifecycle (C1c)

Distinct question: yes — this is Task 1's level-distinction, genuinely a different abstraction-level question than C1's definitional move. Independently wrong-able: weakly (could be collapsed if decision architecture were shown to be derivable from the model lifecycle — no such evidence found). Own evidence: the two flow diagrams already built. Own literature: general software-engineering "artifact vs. authorization to use it" observations, not domain-specific. Different level: **yes, this claim is definitionally about levels being different** — the one candidate in this batch that scores differently from C1/C2 on question 5. Strengthened by merging: yes — it motivates C1b, and reads as throat-clearing without it. Salami risk: high if separated. Consumes later novelty: no. Substantial alone: no. Better as section: yes.

**Verdict: premise, merge into C5's paper — but retained as its own explicit claim node in `claim-graph.md` because it is doing distinct logical work (establishing the level boundary) even though it does not warrant separate publication.**

### Decision-Level Control (C5, incorporating C1/C1c/C1b/C2/C3/C4)

Distinct question: yes — "what must an architecture make explicit before an AI output causes a consequential action, and how is that made to constrain behavior?" Independently wrong-able: yes (gates could prove infeasible for runtime/agent decisions; model-registry-level control could prove sufficient in practice). Own evidence: yes, complete (architecture argument, three drafting iterations, adversarial audit). Own literature: yes, extensively mapped. Different level: yes, Decision level specifically. Strengthened by merging with C1/C1c/C1b/C2/C3/C4: **yes, demonstrated empirically by this programme's own process** — the two-draft comparison (`oreilly-submission-draft.md` → `oreilly-submission-disruptive.md`) showed the merged version was stronger, not just longer. Salami risk if split further: high (tested and rejected — see C1/C1c/C2/C4 verdicts above). Consumes later novelty: no — does not touch C6–C9. Substantial alone: yes, overwhelmingly. Better as section: no, this is the article.

**Verdict: strongest standalone candidate in the entire graph. Already exists as `article-01-decision-level-control/`.**

### Evidence as Authorization Input (C4)

Sub-component of C5's decomposition; fails question 1 and 9 on its own (no distinct question beyond "what does evidence need to contain," which only matters in service of C5's gate).

**Verdict: sub-component, merge into C5.**

### Governance Without Enforcement (C3)

Same pattern — the general principle (question 4's "own prior-art literature") is textbook access control, giving it near-zero standalone research value (question 9 fails badly); its interesting form is a narrow, evidenced observation about the responsible-AI documentation literature specifically, which is thin enough to be one section, not one paper.

**Verdict: premise/supporting observation, merge into C5.**

### Human-in-the-Loop as Explicit Authorization (C5h)

Distinct question: moderately — "what makes a human-in-the-loop step an actual authorization path rather than an informal exception?" is more specific than C5's general question. Independently wrong-able: yes (falsified by showing real HITL implementations already specify authority/evidence/refusal-enforcement by default). Own evidence: partial (MCP's consent model, general automation-bias literature — neither yet fully researched for this claim specifically). Own literature: a genuinely distinct field (agent/tool-use authorization, human-factors automation research) that C5's core paper does not otherwise touch. Different level: no, still Decision level, a refinement of C5's ESCALATE branch specifically. Strengthened by merging: currently yes, as one paragraph inside C5's paper it reads as a sharp, well-earned observation; if expanded to its own literature (agent authorization specifically), it *could* eventually support a focused piece. Salami risk if separated now: moderate-high, since the current treatment (one paragraph) would not sustain a full paper without substantially more research. Consumes later novelty: no. Substantial alone *currently*: no. Better as section *currently*: yes.

**Verdict: currently a subsection of C5's paper. Flagged as a possible future standalone piece (agent/HITL authorization specifically) if the agent-authorization literature is researched more deeply later — not recommended as a near-term priority.**

### State Is Not Knowledge (C6) / Decision Provenance / Historical Reconstruction (C7)

Tested together since Task 4's own logic (mirroring C1–C4 → C5) recommends merging them:

Distinct question (as a pair): yes — "does current state suffice to reconstruct why a past decision was valid, and if not, what architectural commitment closes the gap?" Independently wrong-able: **yes, decisively — this is the test that separates C6/C7 from C1–C4**: even if C5 (enforcement) is entirely correct and fully implemented, C6/C7 could independently be true or false; a perfectly gated decision could still become unreconstructable, or, as the falsifiable null hypothesis, existing artifacts (git + logs + registry) could turn out to already be sufficient. Own evidence: yes, and of a genuinely different *type* than C5's — reconstruction/drift experiments, not gate-implementation evidence (see `empirical-program.md`). Own literature: partially mapped (SLSA/in-toto), needs its own dedicated audit reaching into archival science/digital preservation — a domain untouched by C5's research. Different level: yes, Historical/provenance, distinct from Decision level by the independence test above. Strengthened by merging C6 with C7: yes, mirroring C1–C4→C5 exactly — a pure-diagnosis paper (C6 alone) would be under-motivated without a proposed response, and a pure-architecture paper (C7 alone) would be unmotivated without the diagnosis. Salami risk if C6 and C7 were separated: high, by direct structural analogy to the control cluster. Consumes later novelty (C8/C9): no — does not touch capability-vs-understanding or the historical software-engineering pattern. Substantial alone (as a merged unit): yes, and this is the freshest, most falsifiable material in the whole programme (Inversions D and E, both rated 5/5 disruptive potential).

**Verdict: standalone-worthy as one merged unit — the strongest unresearched contribution in the graph — but requires its own prior-art audit (Step 2 in `research-roadmap.md`) before drafting.**

### Capability vs. Understanding (C8)

Distinct question: yes, but very broad. Independently wrong-able: technically yes, but resistant to clean falsification (Inversion F, defensibility 2/5). Own evidence: weak, hard to operationalize. Own literature: thin, unaudited, adjacent to tech-debt folklore. Different level: yes, Systems-knowledge. Strengthened by merging into C9: **yes, and this is the decisive consideration** — alone, C8 is the weakest-evidenced claim in the graph and maximally exposed to "how do you measure understanding" pushback; inside C9, it is supported indirectly by C9m's historical-pattern argument. Salami risk if published standalone before C9: this is a *premature-spend* risk, not an ordinary duplication risk — publishing C8 alone would spend much of C9's rhetorical capital without earning C9's full payoff. Consumes later novelty: yes, specifically this risk. Substantial alone: marginally, but weakly defensible. Better as section: yes, decisively.

**Verdict: merge into C9. Do not publish standalone, and do not publish before C9's other premises (C6/C7, C9m) exist.**

### The Understanding Layer (C9m + C9a + C9b)

Distinct question: yes, the deepest in the programme. Independently wrong-able: yes in principle, though closer to an interpretive frame than a strict hypothesis, especially for C9b. Own evidence: requires a dedicated historical/comparative literature review — **not yet done, the largest concrete research gap identified across both passes.** Own literature: unaudited. Different level: yes, Systems-knowledge, the most general level. Strengthened by merging C9m+C9a+C9b into one piece rather than three: yes — C9m (the historical pattern) is the evidentiary backbone C9a (the diagnosis) needs, and C9b (the architectural response) is explicitly the most hedged, least-specified claim in the graph and should not stand without C9a's support. Salami risk if split: high, and specifically risks publishing C9b (the weakest, most speculative half) without C9a's comparative weight behind it. Consumes later novelty: not applicable — terminal node. Substantial alone (as one merged unit): yes, but only after C5 and C6+C7 exist to give it earned scaffolding, per the terminal-thesis-protection finding reconfirmed in both passes.

**Verdict: standalone capstone (C9m+C9a+C9b merged), sequenced last, framed explicitly as a diagnosis-plus-open-problem-statement rather than a specified architecture (per C9b's honest novelty-risk rating in `claim-graph.md`).**

### Evidence-Gated AI (the C5 architecture's name)

Not a separate contribution — this is C5 itself, under Source B's original working name. No separate treatment needed.

### AIGov Core

Not a theory-level claim — an implementation-role question. Full treatment in `aigov-role.md`. Its correct placement (established there) is as a motivating case study for the C6+C7 paper, not as a standalone contribution and not as evidence for any general claim.

---

## Task 5 — The minimum independent contribution set

**Three genuinely independent contributions survive**, confirmed identically by both the first and second passes through this falsification test, now with more granular and more adversarial testing behind the same conclusion:

### 1. Decision-Level Control

- **Name:** Decision-Level Control (also: "Model Outputs Are Not Decisions," "Evidence-Gated Decisions").
- **Research question:** What must an architecture make explicit before an AI-derived output is allowed to cause a consequential action, and how is that made to actually constrain behavior rather than merely describe it?
- **Thesis:** Production AI needs an explicit decision layer — output → proposed decision → evidence → requirements/authority → gate → ALLOW/BLOCK/ESCALATE → transition — attached to the decision, not the model, because a single model participates in many decisions with different requirements.
- **Why independent:** Confirmed via the ten-question test above; the merged C1–C5 unit has its own question, its own falsifiable thesis, its own complete evidence base, and its own extensively mapped prior art.
- **What would falsify it:** Evidence that decision boundaries at runtime/agent-level cannot sustain gates (e.g., latency infeasibility), or that model-registry-level control is already functionally sufficient in practice.
- **Required evidence:** Architecture/design argument (complete); optional strengthening via repository audit and controlled failure experiment (`empirical-program.md`).
- **Main prior-art field:** Access control (XACML, Cedar), admission control (Kubernetes, Sigstore), software supply-chain security (in-toto, SLSA), CI/CD deployment gates, ML model registries.
- **Dependency on other contributions:** None.
- **What it enables:** Nothing downstream is logically dependent on it (per `claim-graph.md`'s branching structure), but it supplies the concrete illustration of "decision-level specificity" that strengthens Contribution 3's eventual credibility.

### 2. Preservation & Reconstruction

- **Name:** Preservation & Reconstruction (also: "State Is Not Knowledge," working title pending Step 2's audit).
- **Research question:** Does current system state — including stored decisions and evidence — suffice to reconstruct why a past decision was valid, and if not, what architectural commitment (decision provenance, evidence continuity, versioned policy/model/context) closes the gap?
- **Thesis:** Current state is insufficient for reconstruction because AI-specific context (prompts, retrieval corpora, policy interpretation, tool behavior at the time) is transient by default and was never treated as a persistent engineering artifact; closing the gap requires treating decision provenance as a first-class, versioned architectural concern.
- **Why independent:** Decisively confirmed by the independence test — true or false regardless of Contribution 1's correctness; different evidence type (reconstruction experiments, not gate-implementation); different, largely unaudited prior-art field.
- **What would falsify it:** A repository audit or controlled failure experiment showing existing artifacts (git + logs + registry) already suffice for reconstruction without new mechanisms.
- **Required evidence:** A dedicated prior-art audit (not yet done — Step 2 in `research-roadmap.md`), plus a controlled failure experiment and repository audit (full designs in `empirical-program.md`).
- **Main prior-art field:** Software supply-chain provenance (SLSA, in-toto), bitemporal/point-in-time-recovery database design, digital preservation and archival science (untouched so far), incident-investigation practice in safety-critical industries (untouched so far).
- **Dependency on other contributions:** Only the shared premise C1 (output ≠ decision) from Contribution 1.
- **What it enables:** Contribution 3's C9a/C9b, which depend on this cluster's findings as concrete grounding.

### 3. The Understanding Layer

- **Name:** The Understanding Layer (also: "Capability vs. Understanding").
- **Research question:** Is AI capability advancing faster than the mechanisms required to preserve knowledge about system behavior, and if the recurring software-engineering pattern of building preservation mechanisms in response to complexity actually applies to AI, what architectural response — if any — follows?
- **Thesis:** AI may be the first major computing paradigm in which capability is scaling faster than the mechanisms required to preserve knowledge about system behavior; explainability, interpretability, observability, provenance, governance, and auditability may be fragmented, partial responses to one deeper requirement, which may need to become an explicit architectural property.
- **Why independent:** The most general level in the graph; not reducible to a claim about decisions specifically (that generalization step is itself flagged as a currently-unargued premise, per `claim-graph.md`'s Task 1 analysis).
- **What would falsify it:** Historical evidence that version control/transaction logs/tracing were not actually responses to the kind of complexity-driven knowledge loss Source A describes (a real risk — Git's actual origin, for instance, is more directly about distributed collaboration and merge-conflict resolution than about "preserving knowledge" as such, a complication Step 6 must investigate honestly rather than assume away); or evidence that explainability/observability/governance communities do not, in fact, talk past each other the way Source A characterizes.
- **Required evidence:** A dedicated historical/comparative literature review (not yet done — the largest concrete gap in the whole programme, Step 6 in `research-roadmap.md`), plus synthesis of Contributions 1 and 2.
- **Main prior-art field:** History of software engineering (version control, transaction logs, distributed tracing as engineering history, not just technical description); the self-descriptions of the explainability/interpretability/observability/governance/auditability research communities.
- **Dependency on other contributions:** Both 1 and 2 — needed as concrete grounding and, rhetorically, as earned credibility before the terminal claim is stated.
- **What it enables:** Nothing further — terminal node of the programme.

### Merged claims (looked independent, are really parts of another contribution)

C1 (output ≠ decision), C1c (levels are different), C1b (model is insufficient unit), C2 (evaluation ≠ authorization), C3 (governance without enforcement), C4 (evidence/requirements/authority distinction), C5h (human-in-the-loop) — all merged into Contribution 1. C8 (capability vs. understanding as variables) — merged into Contribution 3.

### Premises only (should not become standalone papers)

C1, C1c, C2, C3, C4 within Contribution 1; C8 within Contribution 3 (in the specific sense that its *standalone* publication is actively discouraged, not merely unnecessary — see the premature-spend finding above).

### Synthesis only (meaningful only after earlier work exists)

C9a and C9b (Contribution 3's own terminal claims) are themselves synthesis-only relative to C9m, C6, C7, and Contribution 1 — they do not stand without that earlier material, which is why Contribution 3 is sequenced last regardless of which publication architecture is chosen (see `publication-architectures.md`).

### Dropped

Nothing from the A–Q list was found too weak, derivative, unsupported, or redundant to warrant *any* role in the graph — every letter maps onto a live claim node with at least a "premise" or "merged" role. The closest candidate for outright dropping was C5h (human-in-the-loop) if it could not sustain even a subsection's worth of argument, but it survives at that scope (see its Task 4 verdict above). No claim is recommended for deletion from the programme; several are recommended for *demotion* from "candidate standalone contribution" to "premise" or "subsection," which is a different and more defensible outcome than dropping them.
