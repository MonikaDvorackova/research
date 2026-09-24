---
id: topic-static-agent-verification-charter
title: "Static Verification of Python AI Agents: Scope and Stopping Rule"
topic: static-agent-verification
type: governance
status: active
created: 2026-09-24
updated: 2026-09-24
tags: [static-analysis, ai-agents, security]
refs: []
---

## Purpose

Ask which pre-execution assurances about Python AI-agent code can be defended, and whether the observed limits justify a new programming language. The implementation and tests live in the separate public [static verification experiment](https://github.com/MonikaDvorackova/static-agent-verification-experiment). This topic stores research claims and their evidentiary bounds, independent of AIGov or its governance product.

## Scope

- P1: LLM-derived values reaching privileged external actions require a trusted validation boundary.
- P2: sensitive values must not reach an unauthorized external model or tool.
- P3: critical external actions require an authorization or human-approval boundary. The stronger, operational P3* additionally binds an authentic, fresh, single-use approval to the concrete action, target, arguments and context and requires complete mediation.
- A three-valued analysis (`PROVED`, `VIOLATED`, `UNKNOWN`) with explicit soundness assumptions, a small authored corpus, selected pinned real agent modules, established analysis baselines and a bounded approval/capability comparison.

## Out of scope

- AIGov architecture, runtime observability, governance dashboards and compliance claims.
- Unconditional safety certification for arbitrary Python, a proof of model truthfulness, or assurance about external services.
- Language syntax design or assertions of novelty without an independent comparative evaluation.

## Current decision

The bounded phase supports useful **conditional** proofs in a sealed modeled subset and shows UNKNOWN on the selected unchanged real modules. CodeQL, Pysa, Scala capability checking and a runtime SDK each address parts of the problem under different assumptions. The evidence does **not** justify a new language. Stop adding synthetic analyzer rules merely to raise coverage; prepare an explicitly qualified research article and request independent review. See [claim inventory](notes/claim-inventory.md).

## Falsification and reopening criteria

1. An independent reviewer must define the policy and trusted contracts before judging a real application; otherwise a policy-conditional counterexample is not a statement about that application's intent.
2. To claim a practical proof, inventory all paths to the chosen effect and verify the trusted implementation and external boundary. A single selected path cannot establish complete mediation.
3. To reopen language design, first demonstrate a valuable guarantee that cannot be achieved under acceptable constraints with existing typed subsets, static analysis and effect-side approval mediation. This experiment has not met that threshold.

## Relationship to other topics

This topic investigates **pre-execution program properties** and runtime premises needed to justify them. The existing `ai-infrastructure-gap` topic investigates preservation and reconstruction of historical decision justification. Neither topic supplies the other's result; the repositories and research claims remain independent.
