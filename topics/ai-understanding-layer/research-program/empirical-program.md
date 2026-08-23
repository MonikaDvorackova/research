---
id: note-research-program-empirical-program
title: "Research Programme — Empirical Programme"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-21
updated: 2026-08-21
tags: [research-program, empirical-design]
refs: []
---

## Research Programme — Empirical Programme

Scope: Task 6. Classifies the appropriate research form for each surviving contribution (`contribution-boundaries.md`), then revisits Source B's original methodological claims — "controlled failure experiments" and "an audit of real-world ML repositories" — and redesigns them properly rather than assuming they belong wherever Source B originally implied. No results are reported anywhere in this document; every programme below is a design, not a finding, and none has been run.

---

### Research form by contribution

| Contribution | Primary form | Empirical strengthening (optional, not required to stand) |
|---|---|---|
| 1. Decision-Level Control | Architecture/design (complete) + practitioner synthesis (complete) | Repository audit (observational); controlled failure experiment (confirmatory) |
| 2. Preservation & Reconstruction | Conceptual argument (built) needing to become falsifiable, + architecture/design (not yet built) | Controlled failure/reconstruction experiment (central, high-value); repository audit (companion) |
| 3. The Understanding Layer | Conceptual argument + dedicated historical/comparative literature review + interdisciplinary synthesis | **None appropriate** — deliberately not an empirical/experimental piece |

C9's exclusion from experimental design is a deliberate scoping decision, not an oversight: "is capability outpacing understanding, across the field, in general" is not answerable by any single experiment, and attaching one would be the kind of forced academic dressing the brief explicitly warns against.

---

### Revisiting Source B's original methodological claims

Source B's "About the topic" section states the approach is "grounded in system design and supported by controlled failure experiments and an audit of real-world ML repositories, demonstrating systematic gaps in auditability and enforcement." As established in `../notes/intellectual-progression.md` (Task 8) and reconfirmed in `../article-01-decision-level-control/evidence.md` (claim 13), **neither experiment nor audit was ever actually run** — this is a stated intention in a book proposal, not completed work, and must never be treated as existing evidence.

Source B's own framing implicitly assumes both belong to the decision-level/auditability material (Contribution 1). **This assumption is tested and rejected below.** The redesign finds both programmes are better-motivated, and more novel, when aimed at Contribution 2 (Preservation & Reconstruction) than at Contribution 1 — because Contribution 1's central claims (documentation ≠ enforcement, model ≠ decision) are already well-supported by existing prior art elsewhere (access control literature has settled the general question), whereas Contribution 2's claims are the least prior-art-settled, most genuinely open empirical questions in the whole programme.

---

### Programme 1 — Repository audit

**Hypothesis:** Real-world production ML/AI repositories predominantly implement model-level governance artifacts (versioning, model cards, registry stage-transitions) and rarely implement decision-level evidence gating (a structured, per-decision authorization check distinct from model promotion) or the kind of preserved decision-provenance context (versioned prompts, retrieval-corpus snapshots, policy-interpretation records) that would allow a historical decision's validity to be reconstructed.

**Dataset / corpus / system under study:** A sampled set of open-source ML/AI production repositories with visible deployment pipelines (candidate sources: repositories using MLflow, Databricks, or similar registries with public CI/CD configuration; repositories implementing LLM-based agents with tool-use; repositories with documented incident or audit history, if any can be found). Sample size and selection criteria to be fixed at design time, not left to convenience sampling — this is itself a design task, not yet done.

**Independent variable / perturbation:** None — this is an observational study, not an intervention. The "variable" being measured is a classification of each repository's governance artifacts along two axes: (a) model-level vs. decision-level control, (b) presence/absence of versioned decision-context preservation.

**Dependent / observed outcome:** Two proportions: the fraction of repositories with any decision-level (not merely model-level) evidence-gating mechanism; the fraction of repositories in which a specific historical decision could plausibly be reconstructed (which prompt/policy/model version applied) using only artifacts present in the repository as retained.

**Comparison / baseline:** Repositories are compared against each other and against the explicit criteria derived from Contribution 1's evidence/requirements/authority decomposition (for the first proportion) and Contribution 2's reconstruction-completeness criteria (for the second, once Step 2's audit defines them precisely).

**Falsification condition:** If most sampled repositories already implement decision-level gating and/or already retain sufficient versioned context for reconstruction, the corresponding diagnostic claim (C1b for the first proportion, C6 for the second) is weakened, and the contribution's motivating premise needs revision.

**What it can support:** How common each pattern is, right now, in real repositories — a genuine, checkable fact this programme currently only asserts by illustration (one LLM example for C1b; one hypothetical auditor scenario for C6).

**What it cannot support:** That decision-level gating or provenance preservation *causes* better outcomes (fewer incidents, faster audits, higher trust) — only how prevalent each pattern is. Causal claims would require a different design entirely (e.g., a longitudinal or matched-comparison study), out of scope here.

**Redesign note relative to Source B's original framing:** Source B implied this audit would "demonstrate systematic gaps in auditability and enforcement" as if the conclusion were already known. The redesign above states it as a genuinely open question with a stated falsification condition — the audit could just as easily show the gaps are smaller than assumed, which would be a legitimate and useful finding, not a failed study.

---

### Programme 2 — Controlled failure / reconstruction experiment (central to Contribution 2)

**Hypothesis:** A production AI decision that was fully evidenced and gated at time t0 becomes not reconstructable — in the sense of a later party being unable to correctly restate its original justification, applicable policy, and validity conditions — after realistic context drift (prompt changes, retrieval-corpus updates, policy revisions, model updates), unless that context was explicitly and separately preserved as a versioned artifact.

**Dataset / corpus / system under study:** A minimal synthetic testbed built around Contribution 1's own running example (a model-promotion decision, or an agent tool-call decision) — not a real production system, at least initially, since access to real historical decisions with known ground truth is unlikely to be available and privacy/access constraints would complicate a first design. The testbed should implement Contribution 1's evidence-gated pattern faithfully, then allow controlled manipulation of the surrounding context.

**Independent variable / perturbation:** Systematically vary which context elements are allowed to drift or be overwritten (prompt template updated in place vs. versioned; retrieval corpus updated in place vs. snapshotted; policy document revised in place vs. versioned; model updated with the old version's artifacts discarded vs. retained) across a matrix of conditions, from "nothing preserved beyond the bare decision record" to "everything explicitly versioned" (Contribution 2's proposed architecture).

**Dependent / observed outcome:** A reconstruction-completeness score: given only the retained artifacts under a given condition, can a blinded auditor (a person, or a specified evaluation protocol, not told which condition produced the artifacts) correctly restate (a) what evidence was considered, (b) which policy version applied, (c) why the decision was judged valid at the time. Scored against a known ground truth fixed at experiment design time.

**Comparison / baseline:** The "nothing preserved beyond the bare decision record plus current system state" condition serves as the baseline — this is what Source A's six-months-later scenario describes as the default, and what most real systems are hypothesized (per Programme 1) to actually do today.

**Falsification condition:** If reconstruction-completeness scores do not differ meaningfully between the baseline condition and the fully-versioned condition — i.e., if decisions remain reconstructable using only ordinary retained artifacts (git history, logs, model registry) without any new preservation mechanism — this would directly weaken C6's diagnostic claim and, by extension, the motivation for C7's proposed architecture.

**What it can support:** Whether a reconstruction gap exists at all, and roughly how large it is under realistic drift conditions; which specific context elements matter most (the experiment's condition matrix would reveal this — e.g., prompt drift might matter more than policy-document drift, or vice versa, which is not currently known and would itself be a genuine finding).

**What it cannot support:** That any *specific* proposed architecture (an AIGov-Core-style provenance layer, or any other particular design) is the right or only way to close the gap — only that a gap exists and roughly how large it is. Also cannot support generalization to real organizational settings beyond whatever testbed is built, without a follow-up study using real systems.

**Redesign note relative to Source B's original framing:** Source B's "Controlled Failure Experiments" (Ch. 10) was scoped to demonstrating "system behavior under failure" in service of the enforcement/auditability argument (Contribution 1). The redesign above finds this experimental form is actually far better suited to, and far more novel for, Contribution 2 — Contribution 1's "does removing a gate increase violations" question is a confirmatory experiment (adjacent access-control literature already answers this in other domains, per `../article-01-decision-level-control/novelty-audit.md`); Contribution 2's reconstruction question is a genuinely open one with no settled answer in the AI-specific case, which is exactly where a controlled experiment earns its keep.

---

### Programme 3 — Confirmatory controlled failure experiment for Contribution 1 (lower priority, optional)

**Hypothesis:** Removing or weakening an enforcement gate — leaving only documentation of the requirement — increases the rate at which non-conforming decisions execute, relative to an otherwise identical pipeline with the gate present.

**Dataset / corpus / system under study:** The same minimal synthetic testbed as Programme 2, reused, with the gate itself toggled on/off rather than the surrounding context varied.

**Independent variable / perturbation:** Presence vs. absence of the evidence gate.

**Dependent / observed outcome:** Rate of policy-violating decisions that execute under each condition.

**Comparison / baseline:** Gate-present condition as the comparison point for the gate-absent condition.

**Falsification condition:** Outcomes statistically indistinguishable with and without the gate (e.g., because a human catches violations through some other channel anyway) would weaken the practical-necessity framing of Contribution 1's argument, though not its architectural-design claims, which do not depend on this experiment to be coherent.

**What it can support:** A concrete, quantified illustration of the "recording is not enforcing" argument, useful for a practitioner audience even if the qualitative result is already well established in adjacent domains.

**What it cannot support:** Generalization beyond the synthetic testbed; and, because this question is already well-answered in access-control literature generally, this experiment's *novelty* contribution is low even if its illustrative value for an AI-specific audience is real.

**Priority note:** Explicitly lower priority than Programme 2 — Contribution 1 does not need this experiment to stand (it is already a complete, audited architecture argument), whereas Contribution 2 is meaningfully strengthened, possibly load-bearingly so, by Programme 2's results. If resources are constrained, Programme 2 should run first.
