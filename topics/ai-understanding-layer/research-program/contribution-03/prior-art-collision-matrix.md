---
id: note-contribution-03-prior-art-collision-matrix
title: "Contribution 3 — Prior-Art Collision Matrix"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, prior-art, collision-matrix]
refs: [historical-literature-review.md, program-comprehension-review.md, observability-review.md, provenance-review.md, ai-systems-review.md, source-ledger.md]
---

## Prior-Art Collision Matrix

Consolidates every field/mechanism reviewed. "Level" refers to
`residual-gap-analysis.md`'s six-level decomposition (model / inference-
decision / pipeline-system / historical-system / behavioral-envelope /
human-system-knowledge).

| Field / mechanism | What it preserves | Level | Temporal? | Dependency relation? | Reconstruction? | Explanation? | Prediction? | Control? | Collision with our thesis | Residual gap |
|---|---|---|---|---|---|---|---|---|---|---|
| Version control | Code history | 3 | No native valid-time | Yes (commit DAG) | Yes, for code | No | No | No | Confirms history-retention is old; motivation was NOT preservation-of-understanding (`historical-literature-review.md`) | None for code; does not extend to runtime decisions |
| Transaction logs / WAL | State-change history | 3–4 | Transaction-time only | Yes, sequential | Yes, for state | No | No | No | Durability/crash-recovery goal, not explanatory | Explanation, always |
| Distributed tracing (Dapper-lineage) | Per-request execution path/timing | 3 | Short-horizon only | Yes, causal (span graph) | Yes, execution | Partial (how, not why) | No | No | Closest historical match to "preserve knowledge to understand," but narrowly scoped to latency diagnosis | Long horizon; normative why |
| Program comprehension (field) | N/A — a research method, not a mechanism | 1/3 (source code) | N/A | N/A | N/A | Studies human explanation-seeking | No | No | Already formalizes "systems hard to understand" as a measured research object | Does not cover AI-runtime behavior as its unit |
| Architectural knowledge management | Design rationale | 3 (design-time) | No | Partial (decisions to components) | Partial | Yes (rationale) | No | No | Already names "knowledge vaporization" — Source A's core mechanism, pre-existing | Runtime/per-decision instance, not just design-time |
| Software archaeology / architecture recovery | Recovered structure from artifacts | 3 | No | Recovered post hoc | Yes | Partial | No | No | Already solves "reconstruct lost understanding" for legacy systems | Real-time/AI-runtime application untested |
| Observability (control theory + software) | Inferable internal state from outputs | 3–4 | Depends on retention | Causal (traces) | Yes, if retained | Partial ("why," informally) | No | No | "Monitoring vs. understanding why" is already this field's own distinction | No native temporal/transaction-time semantics; no per-decision binding |
| W3C PROV / database provenance (why/where/how) | Lineage relations | 3–4 | Point-in-time only (PROV); none (Buneman) | Yes, exactly | Yes, if populated | No normative vocabulary | No | No | Formal provenance theory predates PROV by 12+ years | No valid-time interval (Contribution 2's own finding, reused here) |
| Deterministic replay / time-travel debugging | Full execution trace | 3 | N/A (full history) | Implicit (causal execution) | Yes, complete | No | No | No | Answers "what happened," not "was it authorized" | Normative justification, always |
| Bitemporal databases | Valid-time + transaction-time facts | 4 | Yes, natively | No | Yes, completely, within scope | No | No | No | Solves D/E sub-problems completely per Contribution 2's own audit | Adoption for AI-specific dependencies; per-decision binding |
| ML lineage / Hidden Technical Debt findings | Training-time data/model lineage; named ML-specific risk factors | 1–3 | Partial | Yes (training DAG) | Training-time only | No | No | No | Confirms genuine AI/ML-specific complications (entanglement, feedback loops) exist and are literature-supported | Runtime decision-time consumption (Contribution 2's own gap, confirmed still open here) |
| Mechanistic interpretability | Model-internal feature/circuit structure | 1 | No | Causal (circuit tracing) | N/A (model, not decision) | Partial, and field itself reports many queries intractable | No | No | Field self-reports intractability as an open problem (2025) | Scaling to system-level, multi-component decisions |
| Agent/LLM observability (2026 tooling) | Layered traces across LLM calls/tools/env | 2–3 | Short-horizon, typically | Yes, causal | Yes, execution-level | Partial | No | No | Direct, current (2026) evidence of depth-without-integration across layers | Cross-layer integration; historical (long-horizon) retention |
| XAI (interpretability, attribution, counterfactual) | Per-output explanation | 1–2 | No | No | No | Yes, for single outputs | No | No | Field's own self-description matches Source A's framing closely | Does not aggregate to multi-component decision justification |
| Runtime verification / formal methods | Property-conformance verdicts | 3 | Online or offline traces | Formal spec relation | No (verdict only) | No | Partial (spec violation as early warning) | Yes, if paired with enforcement | Answers "does P hold," a different question from reconstruction | Explanation of *why* behavior occurred, not just whether it conformed |
| Assurance/safety cases | Structured argument over evidence | 5–6 | No | Argument structure | N/A (consumes evidence) | Yes, structurally | No | Indirect (informs go/no-go) | Real, mature candidate umbrella for Source A's "fragmentation" claim | Does not generate the underlying evidence itself |

## Reading the matrix

No single row spans Levels 1 through 6. The closest multi-level
coverage — assurance cases (5–6) plus whatever evidence feeds them from
rows 1–9 — is exactly the **coordination-not-generation** finding from
`ai-systems-review.md`: a structuring methodology exists, but it
presupposes the underlying reconstruction/observability/provenance
content already reviewed here, none of which by itself reaches Levels 5
or 6 (behavioral envelope; human/system knowledge). This is the shape of
whatever residual gap survives — see `residual-gap-analysis.md`.
