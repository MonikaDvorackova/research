---
id: pub-03-sec-04-worldconsistmem
title: "WorldConsistMem Benchmark"
type: chapter
status: camera-ready-pass
created: 2026-08-04
updated: 2026-08-04
---

# 4. WorldConsistMem Benchmark

WorldConsistMem is a deterministic synthetic benchmark that instantiates Section 3. It is designed so that consistency constraints are automatically derived from a shared gold history, and so that bundles are not bags of unrelated questions.

## 4.1 Entities, events, and validity

Worlds contain typed entities (persons, organizations, projects, documents, locations) and relations (employment/CEO roles, ownership, membership, document versions, dependencies). An event grammar emits start, end, transfer, update, and related lifecycle events. Role and attribute assertions induce **validity intervals**. Each event carries a **provenance** identifier used by provenance queries and provenance constraints.

Generation is seed-deterministic. Given a seed and tier, the world, event log, observation stream, bundles, gold answers, and applicable constraints are fixed.

## 4.2 Observation stream

Systems never read gold \(W_t\) directly. They ingest an observation stream: structured fields plus canonical text (and, in smoke settings, paraphrases/distractors as configured). Observations are the only channel through which event information enters memory.

## 4.3 Query-bundle generation and families

For each focal lifecycle (for example, a CEO succession or project ownership chain), the generator emits a **bundle** whose queries share that focus and therefore share entities, times, and supporting events. Query families include:

- current state;
- historical state;
- transition;
- temporal order;
- provenance;
- multi-hop;
- contradiction;
- counterfactual;
- conflict validity.

**Why bundles are not unrelated questions.** Bundle members are linked by construction: answering “who is CEO now,” “who was CEO before,” “when did the change occur,” and “what evidence supports the current role” refers to one succession. Constraints such as transition coherence and provenance support are meaningful only because those answers must agree. A shuffled pool of independent factual questions would not induce the same \(\mathcal{C}_b\).

## 4.4 Constraint derivation

Constraints are compiled from gold history and query slots (uniqueness of exclusive roles, temporal order of events, transition payload agreement with current/historical answers, relational closure for multi-hop items, provenance alignment, contradiction/conflict rules). The evaluator applies \(\mathcal{C}_b\) to predictions without consulting the memory implementation’s internals.

## 4.5 Dataset scale and roles

**Scaled benchmark** (seed 100; frozen):

| Quantity | Value |
|---|---:|
| Worlds | 102 (34 small / 34 medium / 34 large) |
| Bundles | 1,088 |
| Queries | 7,140 |

Tier differ in event volume (mean events per world: 35 / 97 / 215). Bundle difficulty labels (`intermediate`, `complex`) are structural annotations for stratified reporting.

**Smoke benchmark** (frozen checksum `3aa67ed1…`): 25 worlds, 125 bundles, 825 queries. Smoke confirms gold metrics (Acc = BCR = ConsAcc = 1) and the corruption suite that separates Acc from \(\Phi\). Scaled evaluation reuses the same metric and constraint path; smoke is the regression lock, scaled is the primary empirical setting.

**H4 LLM subset** (frozen protocol): first 6 worlds per tier (18 worlds), 192 bundles, 1,260 queries, used only for the local Qwen reader study (Section 7–8). Symbolic scaled results use the full 102-world set unless noted.

## 4.6 Scope statement

WorldConsistMem is a controlled synthetic-world benchmark. Its purpose is to make Acc and joint world-answer consistency separately measurable under identical gold histories and constraints. Ecological and deployment limits are stated in Section 10.3.
