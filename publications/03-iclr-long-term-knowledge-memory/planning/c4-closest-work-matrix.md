---
id: pub-03-c4-closest-work-matrix
title: "C4 closest-work matrix"
type: research-notes
status: audit-complete
created: 2026-08-02
updated: 2026-08-02
---

# C4 closest-work matrix

Inspected methods/objectives/experiments (not abstracts alone). Focus: learned consolidation, compression under shift, sufficiency, irreversibility, decoder recovery.

| Work | What is learned | Consolidation objective | Task distribution | Task shift evaluated? | Lost info unrecoverable? | Decoder retrained after shift? | Raw history available? | Characterizes SS transfer? | Task-agnostic preservation? | Exact overlap with C4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Retain or Consolidate?** (Kang et al., 2026) | OAS utility router over Retain/Merge/Abstract/Rewrite | Budgeted answer utility; coverage vs replacement effects | Fixed LongMemEval / LoCoMo query pools | No T1→T2 scientific shift; budget pressure changes which queries fit | Empirically: consolidation can lose query-critical details vs raw | N/A (generation packing, not Z-encoder + d2*) | Yes as Retain action | No SS overlap law | No | **High with closed S4** (lossy consolidation vs retention); **low with C4’s learned T1-sufficiency → T2 irrecoverability** |
| **Useful Memories Become Faulty…** (arXiv:2605.12978) | LLM consolidator schedules (stream/static); optional Retain/Delete/Consolidate policy | Distill trajectories into textual lessons; continuous update | ALFWorld, ScienceWorld, WebShop, AppWorld, ARC-AGI Stream | **Yes** — task-switch sequences; family misgrouping; stream vs static | Empirically: applicability stripping, overwrite across tasks; episodic retain beats forced consolidate | Not C4’s retrained linear decoder protocol; eval uses memory-in-context | Episodic-only control keeps raw | Mechanisms (misgroup, strip applicability, overfit) — not SS-overlap theorem | Argues gate consolidation; keep episodic | **Highest empirical overlap** with irreversible / path-dependent consolidation harm under shift |
| **MemoryData** (“Are We Ready…”, arXiv:2606.24775) | Benchmark suite; compares systems | Maintenance / consolidation as module among four | Multi-workload agent memory | Update / long-horizon stability; not C4 formal shift | Representation fidelity ablations; not unrecoverable-Z proof | No | Varies by system | No | No | Systems eval of consolidation fidelity — **S4 neighbor**, not C4 law |
| **TiMem** (ACL Findings 2026) | Hierarchical Temporal Memory Tree (prompted, no FT) | Semantic-guided L1→L5 persona abstraction | Conversational LoCoMo / LongMemEval | Personalization continuity, not T1/T2 SS | Claims better structure; not irrecoverable-loss study | No | Leaves retain finer levels in tree | No | Hierarchical multi-granularity | Architecture for consolidation; **opposite claim direction** (better keep structure) |
| **RecMem** (ACL Findings 2026) | When to consolidate (recurrence trigger) + semantic refinement | Reduce eager consolidation cost; recover omitted fine facts | LoCoMo / LongMemEval | No T1→T2 SS shift | Refinement recovers facts omitted by extraction — **acknowledges loss** | No | Subconscious layer keeps raw interactions | No | Keep raw until recurrence | Timing of consolidation + recovery from raw — **partial** on irreversibility (they keep raw) |
| **MemCon** (arXiv:2607.13591) | Contextual bandit over Retrieve/Consolidate/Forget/… | Task success; token cost | Multi-benchmark agent streams | Online adaptation across task streams | Not representation unrecoverability | No | Backend-dependent | No | Control of consolidate/forget | Adaptive **when** to consolidate — not SS collapse law |
| **MCMA** (ACL Findings 2026) | Memory copilot (DPO) for abstraction hierarchy | Downstream utility of abstracted memory; transfer copilot | ALFWorld / ScienceWorld / BabyAI | **Yes** — OOD and cross-task copilot transfer | Aims to **improve** transfer via learnable abstraction | Frozen task model; copilot transferred | Trajectories used to train abstractions | Transfer of abstraction skill, not SS-overlap characterization of collapse | Hierarchical reuse | Closest **learned consolidation for transfer** — studies success of transferable abstraction, **not** irreversible T1→T2 collapse with retrained decoder |
| **LycheeMemory / InfoMem** (ACL 2026 / 2026) | Joint compress–reason RL; info-gain rewards | Answer-conditioned memory quality | Long-context QA | Limited | Degenerate query-copy under bad rewards (InfoMem) | Joint with reasoner | Compressed Θ replaces context | No C4 SS law | Answer-conditioned sufficiency for current QA | Compression for **current** task; degeneration, not shift irrecoverability |
| **IB for zero-shot transfer in RL** (OpenReview / theory) | State-policy IB encoder | Compress S while keeping I(Z; A^π) | Multi-MDP transfer | **Yes** — theory of when IB transfers | Excess info / distortion bounds | Decoder/policy transfer analysis | Full state during training | **Yes** — DJS, bisimulation, LAD, transfer radius vs β | Explicit | **Textbook occupation of claim B** in RL state space |
| **Bisimulation / state abstraction** (Givan, Ferns, Abel, Li et al.; DBC; GCB) | Task-dependent abstractions | Preserve value-relevant distinctions for a reward / goal class | MDP families | Classical: abstraction for R1 fails for R2 | By definition of approximate bisimulation / homomorphism | Optimal abstract policies | Full state for constructing abstraction | **Core theory of task-conditioned sufficiency** | Universal / goal-conditioned variants aim for broader sufficiency | **Primary standard-theory occupation of C4’s formal object** |
| Closed **S4** (repo) | N/A (rejected RQ) | Lossiness ladder destroying temporal/conflict cues | Historical / conflict queries | Cue-type dissociation | Descriptive destruction under compression | Probe tasks | Matched budget | No | No | C4 must differ from this — see audit |

## Saturation summary

| C4 ingredient | Status in literature |
|---|---|
| Compression loses unused details | Occupied / obvious (S4 neighbors; Retain-or-Consolidate) |
| Continuous consolidation path-dependent / faulty under shift | Occupied (**Useful Memories**) |
| Task-conditioned abstraction ≠ transferable | **Standard state abstraction / IB** |
| Keep raw episodic evidence | Occupied (Useful Memories, RecMem, Retain) |
| Learned transferable abstraction | Occupied as positive method (MCMA) |
| Retrained-decoder irrecoverability + SS-overlap law in agent memory | Not as a named agent-memory theorem — but **implied by standard theory** once H is discarded |
