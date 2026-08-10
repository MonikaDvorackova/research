---
id: pub-03-memory-learning-literature-matrix
title: "Memory-learning literature matrix (2024–2026)"
type: research-notes
status: audit
created: 2026-08-01
updated: 2026-08-01
---

# Memory-learning literature matrix (primary sources)

Inspected for methods/objectives/experiments (not titles alone). Focus: learned memory behavior, credit, non-stationarity, feedback, representation, test-time adaptation.

| Paper | Venue/status | Learned component | Objective | Experiments | Relation to search spaces |
|---|---|---|---|---|---|
| **Memory-R1** (Yan et al.) | ACL 2026 | LLM Memory Manager + Answer Agent (PPO/GRPO) | Downstream QA reward for ADD/UPDATE/DELETE/NOOP | LoCoMo, MSC, LongMemEval | A: write/revise; F: RL memory policy |
| **Mem-α** | OpenReview/arXiv 2025 | RL write policy over core/episodic/semantic stores | QA + memory quality; fixed retriever/generator | Long narrative / complex memory | A: construction; E: multi-store |
| **Mem-T + MoT-GRPO** | arXiv 2026 | Tree-guided RL memory ops | Densify sparse delayed rewards via tree credit | Streaming memory agents | **B: credit assignment** |
| **Memory-R2 + LoGo-GRPO** | arXiv 2026 | Local+global GRPO; co-learn extract+manage | Fair credit when memory changes environment | Multi-session LoCoMo-scale | **B: credit assignment** |
| **HiMPO** | arXiv 2026 | Hindsight-informed memory-write advantages | Less-entangled credit for writes vs tool/reason noise | Open-domain + compressive memory QA | **B: credit assignment** |
| **MemCon** | arXiv 2026 | Tabular contextual bandit over memory MDP | Online when/what/how-much retrieve; consolidate/forget | 6 benches, 3 frameworks | A/F: adaptive control; lightweight |
| **MemPO** | arXiv 2026 | Self-memory policy in agent loop | Memory-effectiveness advantages; token efficiency | Long-horizon agent tasks | A: retain; B: credit |
| **ALMA** | arXiv 2026 | Meta-agent searches executable memory designs | Continual learning via meta-learned memory code | ALFWorld etc.; shift eval | C: non-stationarity; F: meta |
| **MCMA** | ACL Findings 2026 | Memory copilot (DPO) for abstraction hierarchy | Structured transferable memory | ALFWorld, ScienceWorld, BabyAI | E: representation/abstraction; C: transfer |
| **AdaMEM** | arXiv 2026 | Test-time short-term strategy memory | Step-wise adaptation without weight updates | ALFWorld, WebShop, HotpotQA | F: test-time |
| **Oblivion** | arXiv 2026 | Decay-driven activation / utility reinforcement | Accessibility not hard delete | Agentic memory control | A: forget; C: adaptation |
| **Honest Lying** | arXiv 2026 | (Analysis) Reflexion write path | Memory confabulation; self-reinforcing false beliefs | 16 envs; memory vs no-memory | **D: feedback/stability** |
| **EDV** | arXiv 2026 | Execute–Distill–Verify for experience write | Escape self-confirmation trap | τ²-bench, Mind2Web, MMTB | **D: feedback** |
| **SSGM** | arXiv 2026 | Governed write validation | Semantic/procedural drift risks | Framework/proposal | D: stability/safety |
| **A-MEM** | NeurIPS 2025 | Agentic Zettelkasten linking/evolution | Dynamic organization | Multi-model benches | A/E: organization (less RL) |
| **Survey: Foundation Agents memory (2026)** | arXiv | — | Taxonomy of episodic/semantic ops | Survey | Landscape map |
| **OSL-MR** | arXiv 2026 | Learned retention under budget | Constrained stochastic opt; stale risk; demand shift | LoCoMo, LongMemEval | **C: non-stationarity**; A: retain |
| **InfoMem** | arXiv 2026 | Chunk-wise memory RL reward | Answer-conditioned info-gain; documents query-copy degeneration | Long-context memory agents | **A/D: degeneration under bad rewards** |
| **MemQ** | arXiv 2026 | Q-learning over provenance DAG | Structural credit via parent retrieval edges | Self-evolving memory agents | **B: credit assignment** |
| **Memory Worth / When to Forget** | arXiv 2026 | Per-memory outcome co-occurrence counters | Staleness / deprecation governance | Online memory quality | C: stale persistence |
| **MemRL** | 2026 | Runtime Q over episodic retrieval | Non-parametric RL; frozen LLM | Stability–plasticity | F: test-time; A: retrieve |
| **LycheeMemory** | ACL 2026 | Joint compress + reason RL | End-to-end compressed memory | Long-context QA | E: consolidation; A: joint opt |
| **Honest Lying** | arXiv 2026 | (Analysis) Reflexion write path | Memory confabulation; self-reinforcing false beliefs | ALFWorld, HumanEval | **D: feedback/stability** |

## Saturation assessment

| Space | Saturation | Local residual (if any) |
|---|---|---|
| A Memory-policy learning via RL/bandits | **Very high** (Memory-R1, Mem-α, MemCon, MemPO, …) | Not “can we learn write/retrieve?” — occupied |
| B Credit assignment for memory | **Very high** (Mem-T, Memory-R2, HiMPO, MemQ, MemPO) | **Characterization** of observational (non-)identifiability / bias-vs-delay — not another GRPO |
| C Non-stationarity | **Very high** (ALMA, MemCon, Oblivion, OSL-MR, Memory Worth) | Catastrophic persistence as primary claim — **occupied** |
| D Feedback/stability | **Very high** (Honest Lying, EDV, InfoMem degeneration) | Confabulation / rewrite hysteresis — **occupied** |
| E Representation / consolidation | **High** (MCMA, Mem-α, LycheeMemory, InfoMem) | Oracle **SS preservation vs irreversible collapse** under task change — partially open |
| F Test-time adaptation | **Very high** (AdaMEM, MemCon, MemRL, ALMA) | Occupied |

## Compute note

Most top empirical claims fine-tune LLM managers with PPO/GRPO on multi-session dialogue. **Not compatible** with local first-pilot constraints (no frontier fine-tune; no large RL). Local survivors must use **small controllers + frozen LLM or fully synthetic memory MDPs**.
