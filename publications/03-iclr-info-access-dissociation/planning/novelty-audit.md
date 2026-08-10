---
id: pub-03-c1-novelty-audit
title: "Novelty and feasibility audit — C1 Information-Access Regime Dissociation"
type: research-notes
status: stopped
created: 2026-07-31
updated: 2026-07-31
novelty_verdict: OCCUPIED
tags: [iclr, novelty-audit, occupied, c1]
literature_checked: 2026-07-31
---

# Novelty and feasibility audit — C1

**Working name:** Information-Access Regime Dissociation  
**Novelty verdict:** `OCCUPIED`  
**Action:** Stop C1. Do not rename, wrap in tools, or proceed to pilot implementation.

---

## Frozen candidate (as audited)

**Research question.** When decision-relevant information is held fixed and presentation length is matched, does sequential tool-mediated acquisition reduce language-model agent task success relative to simultaneous presentation of the same information?

**Core hypothesis.** Even with fixed facts, information, token budget, distractors, and final task, models perform worse under sequential tool-mediated acquisition than under simultaneous presentation.

**Intended contribution.** Controlled capability dissociation — not a new tool-use architecture.

---

## Duplicate test result

| Criterion from duplicate test | Laban et al. 2026 (ICLR Best Paper) | Tool-wrap residual? |
|---|---|---|
| Identical underlying facts | Yes (shards jointly = FULL instruction) | No material change |
| Equivalent final task | Yes (same generation/eval tasks) | Cosmetic if ported |
| Simultaneous vs sequential access | Yes: FULL / CONCAT vs SHARDED | Already present |
| Matched token / context length | Partial: CONCAT recovers ≈95% of FULL while being *shorter* than SHARDED; length is not the driver they isolate | Padding simultaneous upward would likely *shrink* gaps, not open a new claim |
| No tool-selection confound | Yes (no tools; user simulator reveals shards) | Adding forced tools does not create a new scientific object |
| Multiple model families | Yes (15 models, 8 providers) | — |
| Outcome accuracy comparison | Yes (~39% average drop; reliability collapse) | — |
| Agent-style consolidation controls | Yes: RECAP and SNOWBALL | C1’s RECAP condition already covered |

**Classification:** `OCCUPIED`.

Cosmetically renaming the phenomenon as “tool-mediated information-access regime dissociation” does **not** clear the duplicate test. Laban et al. already frame the finding as relevant to agentic workflows and show that agent-style RECAP/SNOWBALL do not fully restore FULL/CONCAT performance.

---

## Five closest papers (design-level)

### 1. Laban, Hayashi, Zhou, Neville — *LLMs Get Lost In Multi-Turn Conversation* (ICLR 2026 Best Paper)

- **RQ:** Do LLMs lose aptitude/reliability when the same instruction information is revealed across multi-turn underspecified conversation vs single-turn full specification?
- **Conditions:** FULL; SHARDED (≤1 shard/turn); CONCAT (all shards one message); RECAP; SNOWBALL.
- **Identical information:** Yes (sharding properties + CONCAT ≈ FULL).
- **Length matched:** No explicit pad of FULL/CONCAT to SHARDED transcript length; CONCAT shorter yet recovers.
- **Order controlled:** Shard order via simulator; gradual-shard ablations.
- **Tool mediation isolated:** No tools; conversational reveal. Tool-selection not a confound.
- **Models:** 15 LLMs (frontier + open).
- **Tasks:** Code, SQL, actions/BFCL, math, data-to-text, multi-doc summary.
- **Metrics:** Task scores; aptitude vs unreliability decomposition.
- **Principal result:** ~39% average multi-turn drop; CONCAT recovers ~95% of FULL; RECAP/SNOWBALL only partial recovery; premature answering + failure to revise.
- **Overlap with C1:** Core simultaneous vs sequential identical-information comparison; RECAP control; agentic implications.
- **Residual not covered:** Forced deterministic *tool-observation* surface forms; explicit transcript-length padding; NO_SELF_TEXT forced schedules. Insufficient for a new ICLR claim given Best Paper status.

### 2. *Multi-Turn Reasoning When Context Arrives in Pieces* (arXiv 2606.12941, 2026)

- **RQ:** Can memory-augmented RL mitigate Lost-in-Conversation when context arrives in shards?
- **Conditions:** Sharded episodes; rolling memory vs full history; training ablations.
- **Identical information:** Sharded GSM8K/MATH from single-turn sources.
- **Length:** Memory capped (256 tokens); not a C1-style pad control.
- **Tools:** No.
- **Result:** Training on sharded data + compact memory substantially recovers multi-turn accuracy.
- **Overlap:** Treats LiC as established; occupies mitigation / training follow-on space.
- **Residual for C1:** None for novelty of the dissociation itself.

### 3. Cheng et al. — *Are Tools All We Need? Unveiling the Tool-Use Tax* (arXiv 2605.00136)

- **RQ:** Why can native CoT beat tool-augmented agents under semantic distractors?
- **Conditions:** CoT → FCStyle → NoopTool → Full; OracleCalc; OracleEvid; Max1Turn.
- **Identical information:** Shared noisy context; not simultaneous vs sequential *same facts via tools*.
- **Length matched:** Not the primary axis.
- **Tool mediation:** Protocol overhead isolated vs computation gain — different scientific object.
- **Result:** Large CoT–Tool gaps on GSM8K-style tasks; protocol tax dominates.
- **Overlap:** Shows tool *protocol* can hurt; does **not** run information-equivalent simultaneous vs sequential evidence delivery.
- **Residual:** Orthogonal; does not reopen C1.

### 4. Rakhsha et al. — *LUMINA* (ACL Findings 2026)

- **RQ:** Which skills (planning, state tracking, history pruning, …) matter for multi-turn long-horizon agents under oracle interventions?
- **Conditions:** Tunable game environments; oracle skill interventions; step vs task success.
- **Identical information / length match for access regime:** No.
- **Result:** Step accuracy ≫ task success; compounding errors; environment-dependent oracles.
- **Overlap:** Multi-turn hardness / compounding — adjacent background only.
- **Residual:** Not an information-access regime dissociation.

### 5. Liu et al. — *Lost in the Middle* (TACL 2024) + progressive-disclosure / parallel-tool lines

- **Lost in the Middle:** Position effects *within one* long context — not sequential acquisition across turns.
- **Progressive disclosure (e.g. arXiv 2607.17598):** Skills packaging / efficiency for long documents — not matched simultaneous vs sequential decision facts.
- **Parallel vs sequential tool calling (LLMCompiler, W&D, TPS-Bench):** Latency and scheduling when calls are independent — not competence under information-equivalent access regimes.

---

## Why a “tool-only residual” fails

A defender might claim: Laban studies *conversational underspecification*; C1 studies *tool observations*.

That residual fails because:

1. The **information-access comparison** (all facts at once vs piece-by-piece) is already the experimental object in Laban FULL/CONCAT vs SHARDED.
2. Laban already tests **agent-style consolidation** (RECAP/SNOWBALL) and discusses agent frameworks as inadequate patches.
3. C1’s proposed kill conditions map onto Laban’s conditions almost 1:1 (SIMULTANEOUS≈FULL/CONCAT; SEQUENTIAL≈SHARDED; SEQUENTIAL_RECAP≈RECAP).
4. Wrapping shards as `tool_return` messages without model tool choice is a **surface-form rename**, not a new falsifiable ML question.
5. Follow-on work already treats LiC as established and moves to training mitigations.

---

## C2 duplicate assessment (same standard)

**C2 claim:** Offline plan competence substantially overestimates online tool-execution success on the same tasks under matched information/tools.

| Close work | Verdict |
|---|---|
| Agent Planning Benchmark (APB, arXiv 2606.04874) | Diagnoses plan correctness vs executable validation; plan-first vs direct execution on ToolSandbox / τ²-bench |
| *Illusion of Diminishing Returns* (arXiv 2509.09677) | Explicitly decouples planning from long-horizon *execution* when the plan is known |
| SIMMER (arXiv 2606.14574) | Executable planning failures / latent hazards |
| FH vs SH planning-horizon study (arXiv 2605.08477) | Full-horizon vs step-wise tool calling — related scaffolding comparison |
| Knowing–doing gap in tool necessity (arXiv 2605.14038) | Related but different (when tools are needed vs invoked) |

**C2 classification:** `OCCUPIED` / no defensible ICLR residual under the same duplicate bar. Plan-vs-execute dissociation is already a 2025–2026 diagnostic theme with dedicated benchmarks.

---

## Programme implication

From the Publication 03 shortlist (C1 primary, C2 secondary, C4 tertiary):

- C1 — **OCCUPIED**
- C2 — **OCCUPIED**
- C4 — previously ranked weak / LUMINA corollary (not re-audited as primary here)

**Conclusion:** No viable ICLR candidate remains among the ranked shortlist under evidence-first duplicate standards. Do **not** implement C1. Return to blank-slate topic search with explicit exclusion of LiC renames and plan–execute renames.

---

## Feasibility note (for the record; pilot not authorized)

Local hardware (audit date): Apple M1, 8 GB RAM, ~4.7 GB free disk, MLX available; cached Qwen2.5-0.5B/3B, Llama-3.2-3B, Phi-3.5-mini 4-bit. A kill pilot would be hardware-feasible at tiny scale but is **scientifically unauthorized** given occupancy.

---

## Files policy

Because the novelty audit **fails**, this package does **not** authorize:

- `decisive-pilot-protocol.md` as an implementation green light  
- experiment code under `experiments/info-access-pilot/`  
- manuscript drafting  

See sibling `STOP.md` and topic-search status note.
