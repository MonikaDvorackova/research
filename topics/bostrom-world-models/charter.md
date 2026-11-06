---
id: topic-bostrom-world-models-charter
title: "Epistemic Identifiability of Agents Embedded in Learned World Models"
topic: bostrom-world-models
type: governance
status: active
created: 2026-11-03
updated: 2026-11-03
tags: [philosophy-of-ai, world-models, hypothesis-testing, simulation-argument]
---

## Topic: Epistemic Identifiability of Agents Embedded in Learned World Models

### Purpose

Bostrom (2003) argues about the probability that we are simulated; it says nothing about whether an observer could empirically tell. Learned world models give a controlled setting for a related, narrower question. This topic investigates what an agent limited to observations and interventions can and cannot infer about how its environment is generated. It is an independent research topic and is not part of AIGov.

### Scope

- In scope: formal distinguishability of a reference environment E0 and a learned model E1 under passive and active interventions; the inferential gap between "mismatch detected" and "environment is simulated"; small reproducible PyTorch experiments; philosophical analysis for *Minds and Machines*.
- Out of scope: any claim that the physical universe is simulated; any claim about consciousness of the experimental agents; estimating Bostrom's probabilities; large-scale training.

### Non-goals

- Re-deriving Chernoff/Stein/Le Cam results and presenting them as new.
- Treating a toy-environment result as evidence about physical reality.

### Current status

`active`. Phase 1 and Phase 2 are recorded in `notes/phase1-decision.md` (decision: REVISE, continue). A small proof-of-concept experiment has been executed (`notes/results.md`); open verification items are listed in the decision note and verification log.

### Key questions

1. When does a detected discrepancy license an inference about the generating process, and what bridge premises are needed to reach "simulation"?
2. How do model approximation error, intervention class, and horizon determine detection power, and what does active experimentation add?

### Entry points

| Kind | Path |
|---|---|
| Verification log | `literature/verification-log.md` |
| Comparison matrix | `literature/comparison-matrix.md` |
| Novelty and gap | `notes/novelty-and-gap.md` |
| Formal feasibility | `notes/formal-feasibility.md` |
| Phase 1 and 2 decision | `notes/phase1-decision.md` |
| Formal framework and proofs | `notes/formal-framework.md` |
| Philosophical analysis | `notes/philosophical-analysis.md` |
| Experiment design | `notes/experiment-design.md` |
| Results and limits | `notes/results.md` |
| Reviewer-style assessment | `reviews/2026-11-03-minds-and-machines-reviewer-assessment.md` |
| Claim-evidence-assumption matrix | `notes/claim-evidence-assumption-matrix.md` |
| Pre-specification (Phase 5) | `notes/preregistration-phase5.md` |
| Phase 5 results | `notes/results-phase5.md` |
| Corrections log | `notes/corrections-log.md` |
| Reproducibility | `notes/reproducibility-phase5.md` |
| Novelty threat matrix | `literature/novelty-threat-matrix.md` |
| Phase 5 gates and readiness review | `reviews/2026-11-03-phase5-publication-readiness.md` |
| Implementation | `implementations/epistemic-identifiability/` |
