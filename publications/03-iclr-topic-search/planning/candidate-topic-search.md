---
id: pub-03-candidate-topic-search
title: "Blank-slate ICLR candidate search for Publication 03"
type: research-notes
status: draft
created: 2026-07-31
updated: 2026-07-31
tags: [iclr, topic-search, diagnostic, agents]
literature_checked: 2026-07-31
---

# Blank-slate ICLR problem search

**Excluded from consideration (closed cycle):** hierarchical agent memory; BCWR; revision-aware retrieval; current–retrospective trade-offs; historical reconstruction under conflicting evidence.

**Selection posture:** diagnostic scientific questions; falsifiable; small-team / local or modest compute; ICLR-shaped (representation, learning under interaction, evaluation methodology)—not governance, not product RAG, not prompt bake-offs.

Literature was checked against 2025–2026 venues/preprints (ICLR/ACL/arXiv) on 2026-07-31. Citations below are to located sources; absence of a hit is not claimed as absence of all related work.

---

## Part A — At most five candidates

### C1 — Information-access regime dissociation

1. **Problem:** Models that solve a task when all decision-relevant facts are shown at once systematically fail when the *same* facts must be obtained through sequential tool observations.
2. **Hypothesis:** Holding information content and approximate token budget fixed, sequential tool-mediated access reduces task success by a large, stable margin relative to simultaneous presentation.
3. **Scientific object:** Interaction / information-access regime (not memory architecture).
4. **Why ICLR should care:** Tests whether agent competence is a property of available information or of the *access process*—a core question for interactive learning and representation under partial observability.
5. **Closest literature:** LUMINA long-horizon multi-turn agents (compounding errors; step vs task success) [ACL Findings 2026]; multi-turn context sensitivity; context-rot / pruning studies. Nearby but *distinct*: parallel vs sequential **tool-call scheduling** (LLMCompiler, W&D, provider parallel function calling)—those papers optimize latency/cost when calls are independent, not competence under **information-equivalent** simultaneous fact presentation vs sequential observation with length matching.
6. **Known:** Multi-turn is harder; step accuracy ≫ task success; long context can hurt; parallel tool calling reduces wall-clock when dependencies allow.
7. **Unresolved residual:** Is the competence gap due to missing information, length, distractors, or tool-scheduling inefficiency—or to the sequential *access regime itself* under matched information and length?
8. **Smallest decisive experiment:** Synthetic tool world; identical fact set; condition A = all facts in one prompt; condition B = same facts via N tool returns; length-matched padding; local MLX models; report Δ success with CIs.
9. **Compute/data:** Local 0.5B–8B MLX; few hundred instances; no training required for kill pilot.
10. **Likely rejection:** “Already known that multi-turn is harder” / confound with horizon—must pre-register length and information equivalence.
11. **Executable:** Yes for Monika’s conceptual framing mid-August; full-team expansion later.

### C2 — Offline plan competence vs online execution competence

1. **Problem:** Models produce correct multi-step plans when asked to plan offline, but fail the same tasks when executing online with tools under identical constraints.
2. **Hypothesis:** Offline plan accuracy substantially overestimates online execution success; the dissociation survives controls for prompt length and available tools.
3. **Scientific object:** Transfer of competence across evaluation regimes (plan vs act).
4. **Why ICLR:** Challenges the assumption that reasoning traces imply executable policies.
5. **Closest literature:** Planning-centric analyses of long-horizon LLM agents; ReAct/Reflexion comparisons; SIMMER latent planning failures; premature commitment diagnostics.
6. **Known:** Locally good reasoning can fail long-horizon planning; latent failures exist.
7. **Residual:** Controlled same-task offline/online dissociation with identical information and tool APIs, not a new planner architecture.
8. **Kill experiment:** Tasks with unique gold plan skeleton; score plan-only vs execute-only; measure plan-correct∧execute-wrong rate.
9. **Compute:** Local MLX + small deterministic tool sandbox.
10. **Likely rejection:** Too close to known plan-vs-act / ReAct literature; looks like agent scaffolding comparison.
11. **Executable:** Feasible, but saturation risk high.

### C3 — Final-answer success vs procedural validity dissociation

1. **Problem:** Agents achieve correct final answers via procedurally invalid tool trajectories; pass@1 hides this.
2. **Hypothesis:** A non-trivial fraction of successful outcomes violate mandatory procedural constraints; procedural failure rate is largely independent of final-answer accuracy across models.
3. **Scientific object:** Evaluation metrics for agentic competence.
4. **Why ICLR:** Metric critique with empirical dissociation is a classic ICLR evaluation contribution—if the magnitude and controls are new.
5. **Closest literature:** AgentLTL procedural compliance (2026); “Beyond the Final Answer” trajectory evaluation; ToolPRMBench; ReliabilityBench.
6. **Known:** Trajectory eval is necessary; correct-but-ungrounded traces exist.
7. **Residual:** Narrow if any—AgentLTL already formalizes judge-free procedural scoring.
8. **Kill experiment:** Reproduce AgentLTL-style constraints on a tiny sandbox; if rates match published patterns without a new phenomenon, stop.
9. **Compute:** Low.
10. **Likely rejection:** Renamed known problem / benchmark without surprising phenomenon.
11. **Executable:** Easy, but **poor novelty**.

### C4 — Irrecoverable early-error amplification under matched step accuracy

1. **Problem:** Environments with similar per-step accuracy yield radically different task success depending on whether errors are recoverable.
2. **Hypothesis:** Holding step accuracy approximately fixed, irrecoverable environments show sharply lower task success than recoverable ones—exposing that step metrics are not transportable.
3. **Scientific object:** Metric transport / environment interaction.
4. **Why ICLR:** Evaluation methodology under interaction.
5. **Closest literature:** LUMINA (explicitly discusses irrecoverable List World); ReliabilityBench robustness axes.
6. **Known:** Compounding errors; step≫task gaps.
7. **Residual:** Thin once LUMINA is credited; risk of being a LUMINA corollary.
8. **Kill experiment:** Two environments, matched step-accuracy bands, compare task success.
9. **Compute:** Low–moderate.
10. **Likely rejection:** Incremental to LUMINA.
11. **Executable:** Yes, but weak as sole contribution.

### C5 — Tool-observation adherence under controlled parametric conflict (agent setting)

1. **Problem:** When a tool returns a value that conflicts with parametric knowledge, agents inconsistently follow the tool despite instructions to trust tools.
2. **Hypothesis:** Tool-following rate collapses under high parametric certainty even when the tool is designated authoritative; prompting/RAG mitigations fail under pre-registered thresholds.
3. **Scientific object:** Tool–memory conflict / epistemic priority under interaction.
4. **Why ICLR:** Knowledge conflict is central; agent/tool variant is practically important.
5. **Closest literature:** Tool-Memory Conflict (TMC, 2026); Task Matters context–memory conflict (ACL Findings 2026); three-regime context-parametric conflict frameworks.
6. **Known:** TMC exists; mitigations incomplete; task framing matters.
7. **Residual:** Mostly occupied by 2026 TMC papers.
8. **Kill experiment:** Calculator/search tools with planted conflicts; measure tool adherence.
9. **Compute:** Low.
10. **Likely rejection:** Already covered by TMC 2026.
11. **Executable:** Easy, **novelty fail**.

---

## Part B — Aggressive novelty filter (rejections)

| Idea | Reject reason |
|---|---|
| C3 Final-answer vs procedural validity as main claim | Substantially covered by AgentLTL / trajectory-eval 2025–2026; risk of benchmark-without-phenomenon. |
| C5 Tool–memory conflict as main claim | Directly occupied by TMC and related 2026 conflict papers. |
| “Better agent memory / RAG / hierarchical memory” | Excluded by closure; saturated; solution-first. |
| Premature commitment as main claim | June 2026 diagnostic paper already exists (hidden-state commitment). |
| Schema-format tool calling as main claim | TSCG / schema-adaptation 2026 already argue format sensitivity as dominant mechanism. |
| G-Pass@k-style stability metrics alone | ACL Findings 2025 already proposed G-Pass@k; metric paper without new agent phenomenon is weak. |
| ReliabilityBench-style chaos reliability suite | Recent preprint; systems/evaluation product risk; heavy engineering. |
| Generic multi-turn hardness | Surveyed extensively; not a residual without information-equivalence controls. |

**Survivors for ranking:** C1 (primary), C2 (secondary), C4 (weak tertiary).

---

## Part C — Ranking (1–5)

Dimensions: Novelty (N), ICLR fit (I), Depth (D), Experiment feasibility (E), Compute (C), Saturation risk inverted as score (S; 5=low risk), Decisive pilot likelihood (P), Monika-fit (M).

| ID | N | I | D | E | C | S | P | M | Total | Notes |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **C1** | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | **37** | Clean diagnostic; learns length-control lesson from closed cycle |
| C2 | 3 | 4 | 4 | 4 | 5 | 2 | 4 | 4 | 30 | Real dissociation; saturation / scaffolding critique risk |
| C4 | 2 | 4 | 3 | 5 | 5 | 2 | 3 | 3 | 27 | Likely LUMINA corollary |

---

## Part D — Final recommendation

### Recommended: C1 — Information-access regime dissociation

> **POST-AUDIT UPDATE (2026-07-31):** Decisive novelty audit classified C1 as **`OCCUPIED`** by Laban et al., *LLMs Get Lost In Multi-Turn Conversation* (ICLR 2026 Best Paper). C2 under the same bar is also **`OCCUPIED`**. Do **not** implement C1. See [`../03-iclr-info-access-dissociation/planning/novelty-audit.md`](../03-iclr-info-access-dissociation/planning/novelty-audit.md) and [`topic-selection-status.md`](topic-selection-status.md). The text below is retained as the pre-audit recommendation only.

**Frozen research question:**  
When decision-relevant information is held fixed (and length-matched), does requiring that information to be acquired through sequential tool observations reduce LLM agent task success relative to presenting the same information simultaneously?

**Primary hypothesis:**  
Yes—sequential access causes a large, stable success drop that is not explained by missing facts, extra tokens, or added distractors.

**Fastest kill experiment (≤3–5 days):**  
1. Build a tiny deterministic tool world (e.g. attribute lookup / constrained QA) with a fixed fact set F.  
2. Condition **Simultaneous:** all facts from F in one user message (+ length padding).  
3. Condition **Sequential:** each fact returned by a tool call; pad to matched token budget.  
4. Evaluate ≥2 local MLX model families, temp 0, n≥100 tasks.  
5. Pre-register: continue only if Sequential success ≤ Simultaneous − 15 pp with non-overlapping 95% CIs after length match; stop if gap < 5 pp or disappears under padding controls.

**Continue if:** large length-controlled gap replicates across ≥2 families and at least two task templates.  
**Stop immediately if:** gap vanishes under length/information matching (same failure mode as the closed CR-Gap cycle).

**Required literature audit (before any expansion):**  
LUMINA; multi-turn surveys; context-rot / prior-context sensitivity; tool-use benchmarks (BFCL, τ-bench); partial-observability RL framing; any 2026 paper on information-equivalent interactive vs batched access (confirm residual still open).

**Seven-day plan:**  
Day 1–2 literature audit + freeze protocol; Day 3 sandbox + instance generator; Day 4–5 MLX pilot; Day 6 length/ablation controls; Day 7 go/no-go memo.

**Proposed Publication 03 directory name:**  
`publications/03-iclr-info-access-dissociation/`  
(Topic slug if locked: `topics/info-access-regime-dissociation/`)

**First implementation milestone:**  
`experiments/info-access-pilot/` with simultaneous vs sequential conditions, length-matched padding, local MLX runner, and a one-page go/no-go findings file.

---

## Exact next prompt (decisive novelty and feasibility audit)

```text
Run a decisive novelty and feasibility audit for Publication 03 candidate C1:

Frozen question: When decision-relevant information is held fixed (and length-matched),
does requiring sequential tool-mediated acquisition reduce LLM agent task success
relative to simultaneous presentation of the same information?

Requirements:
1. Exhaustive literature search (2023–2026) for any paper that already runs an
   information-equivalent simultaneous vs sequential / batched vs interactive
   access comparison with length or token controls.
2. If a near-duplicate exists, STOP and propose the next-ranked survivor (C2) or
   declare no-go.
3. If residual is open, write a 2-page protocol: instance generator, length-matching
   rule, metrics, abandon/continue thresholds, model ladder (local MLX only for pilot).
4. Do not implement the full experiment until the audit passes.
5. Do not reopen CR-Gap / memory / revision-aware retrieval topics.
```
