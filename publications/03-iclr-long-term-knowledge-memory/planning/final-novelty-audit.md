---
id: pub-03-final-novelty-audit
title: "Final novelty positioning audit — WorldConsistMem"
type: research-notes
status: audit-complete
created: 2026-08-04
updated: 2026-08-04
---

# Final novelty positioning audit

**Paper shape:** BENCHMARK + EVALUATION METHODOLOGY  
**Question:** What is the smallest scientific residual of WorldConsistMem over existing long-term-memory evaluation benchmarks (and highly adjacent consistency work)?

**Method:** Primary-source audit of named memory benchmarks (2023–2026) plus adjacent cross-query consistency literature that uses similar metric language. Frozen WorldConsistMem evidence from `experiments/worldconsistmem/outputs/*` and planning specs. No new experiments.

**Presence codes:** F = fully present as primary evaluation object; P = partially present / adjacent ability or metric; A = absent.  
**Confidence:** H / M / L.

---

## WorldConsistMem reference row (frozen)

| Dimension | Presence | Evidence |
|---|---|---|
| Evolving world | F | Deterministic \(W_{0:T}\), event log (`benchmark-specification.md`) |
| Dependent query bundles | F | Bundles spanning current/hist/transition/… |
| One shared latent world history | F | Gold history retained for scoring only |
| Current / historical / transition / provenance / multi-hop / conflict queries | F | Query families in generator + scaled data |
| Machine-checkable cross-query constraints | F | `constraints.py` / Φ over answer sets |
| Strict bundle consistency | F | BCR |
| Partial consistency | F | CSR, PConsAcc grid (2026-08-04) |
| Acc ≠ world consistency | F | Smoke corruption; symbolic Gap_query; Qwen Acc>0, BCR=0 |
| Evaluator independent of memory | F | `evaluate_predictions` path |

---

## Compact comparison matrix

Legend cell = Presence (Confidence). Detail tables follow.

| Dimension | LME | LME-V2 | MemConflict | DynamicMem | EvoMemBench | EverMemBench | MemoryAgentBench | WorldMemArena | LogicBench-Cross / SetCons* |
|---|---|---|---|---|---|---|---|---|---|
| Evolving world | P(H) | F(H) | P(H) | F(H) | P(H) | F(H) | P(H) | F(H) | A(H) |
| Dependent query bundles | A(H) | A(H) | A(H) | P(M) | A(H) | A(H) | A(H) | P(M) | F(H)* |
| One shared latent world history | P(M) | P(H) | P(H) | F(H) | P(M) | P(M) | P(M) | P(H) | A/P(M)* |
| Current-state queries | F(H) | F(H) | F(H) | F(H) | P(H) | F(H) | F(H) | F(H) | P(M) |
| Historical queries | F(H) | P(H) | P(H) | P(H) | P(M) | P(H) | P(H) | P(H) | P(M) |
| Temporal-transition queries | P(H) | P(H) | P(H) | P(H) | A/P(L) | P(H) | P(M) | P(M) | P(M) |
| Provenance queries | A(M) | A(M) | P(M) | A(M) | A(H) | A(M) | A(M) | P(M) | A(H) |
| Multi-hop queries | F(H) | P(H) | P(M) | A/P(L) | P(H) | F(H) | F(H) | P(H) | P(H) |
| Contradiction/conflict | P(H) | P(M) | F(H) | P(H) | P(M) | P(M) | F(H) | P(H) | F(H)* |
| Machine-checkable cross-query constraints | A(H) | A(H) | A/P(M) | A/P(M) | A(H) | A(H) | A(H) | A(H) | F(H)* SMT |
| Strict bundle consistency | A(H) | A(H) | A(H) | A(H) | A(H) | A(H) | A(H) | A(H) | F(H)* SetCons |
| Partial consistency metric | A(H) | A(H) | P(M) | P(M) | A(H) | A(H) | A(H) | P(M) | P(H)* |
| Acc ≠ world consistency | A/P(M) | A/P(M) | P(H) | P(H) | A(H) | A/P(M) | A/P(M) | P(H) | F(H)* |
| Evaluator ⊥ memory impl. | F(H) | F(H) | F(H) | F(H) | F(H) | F(H) | F(H) | F(H) | F(H)* |

\*Not a long-term memory benchmark; included because it shares **cross-query consistency / Acc≠Cons** language and is the strongest novelty attack if Related Work omits it.

---

## Per-benchmark evidence notes

### LongMemEval (Wu et al., ICLR 2025; arXiv:2410.10813)

- **Evidence:** 500 questions; five abilities (IE, multi-session reasoning, temporal reasoning, knowledge updates, abstention); histories scalable; primary metric answer accuracy under memory/long-context protocols.  
- **Dependent bundles / Φ:** Absent as primary object—questions test abilities, not joint constraint satisfaction over an answer set.  
- **Residual gap:** Ability-factorized Acc ≠ WorldConsistMem Φ/BCR/CSR.

### LongMemEval-V2 (Wu et al., arXiv:2605.12493)

- **Evidence:** 451 questions; abilities (static state, dynamic tracking, workflow, gotchas, premise awareness); AgentRunbook pools; Acc + latency (LAFS).  
- **Dependent bundles / Φ:** Absent. Dynamic state tracking is per-question Acc, not cross-answer constraints.  
- **Residual gap:** Experienced-colleague Acc ≠ joint world-answer-set consistency.

### MemConflict (Tao et al., arXiv:2605.20926)

- **Evidence:** Dynamic/static/conditional conflicts; black-box answer Acc + white-box retrieval/ranking; answer correctness can diverge from retrieval fitness.  
- **Dependent bundles / Φ:** Absent—conflicts are query-conditioned fitness-for-use, not multi-query Φ over one entity-relation world bundle.  
- **Closest neighbor** among memory benches for “correctness ≠ retrieval health,” still not Acc≠joint consistency.

### DynamicMem (Xie et al., arXiv:2606.22877)

- **Evidence:** 15-month evolving user profile (attributes/habits/preferences); Temporal Checkpoint Evaluation; state completion vs personalized service; retrieval dominates failures.  
- **Partial:** Checkpoint profile reconstruction is a form of state coherence for a **user**, not multi-view multi-entity world constraints (CEO/owner/doc/provenance jointly).  
- **Residual gap:** Profile TCE ≠ Φ over interdependent world queries.

### EvoMemBench (arXiv:2605.18421)

- **Evidence:** Scope×content taxonomy; task Acc/success + efficiency; 15 methods vs long-context.  
- **Dependent bundles / Φ:** Absent.  
- **Residual gap:** Mechanism taxonomy ≠ consistency suite.

### EverMemBench (arXiv:2602.01313)

- **Evidence:** Multi-party chats; recall / awareness / profile; multi-hop Acc collapse reported; QA Acc primary.  
- **Dependent bundles / Φ:** Absent.  
- **Residual gap:** Social/dialog Acc ≠ machine-checkable world Φ.

### MemoryAgentBench (Hu et al., arXiv:2507.05257)

- **Evidence:** AR / TTL / LRU / selective forgetting; FactConsolidation multi-hop after edits; Acc primary.  
- **Conflict:** Present as selective forgetting / edit consistency **within** the forgetting competency, not as bundle Φ across current+hist+transition+provenance.  
- **Residual gap:** Competency Acc ≠ WorldConsistMem constraint suite.

### WorldMemArena (arXiv:2605.29341)

- **Evidence:** Action–world loop; write/maintain/retrieve/use diagnosis; Lifelong Evolution + Agentic Execution; QA Acc + retrieval + faithfulness.  
- **Partial:** Evolving personal/task states; stage metrics can show write≠use.  
- **Dependent cross-query Φ:** Absent as primary. Multimodal/agentic Acc ≠ structured multi-query world constraints.

### Adjacent (must cite): LogicVault / LogicBench-Cross; Cross-Query Contradictions / SetCons (arXiv:2604.14525)

- **Evidence:** Multi-query bundles; SetConsRate / Case Satisfiability; Acc preserved while consistency rises under solver repair. Explicit Acc≠global coherence.  
- **Not memory:** Logical/case-file reasoning; SMT satisfiability; no evolving multi-entity world memory systems under evaluation.  
- **Attack surface:** Reviewer may say “consistency already has benchmarks.”  
- **Rebuttal:** Different scientific object—logical belief SAT vs **memory** evaluation over **evolving gold worlds** with **world-history-derived** temporal/transition/provenance/relational constraints.

---

## Answers to audit questions

1. **Smallest defensible residual:** Evaluating whether a memory system’s answers to **interdependent queries over one shared evolving multi-entity gold world** jointly satisfy **machine-checkable world-history constraints** (strict BCR and complementary CSR), thereby making **per-query Acc and world-answer-set consistency separately measurable**—with an evaluator independent of the memory implementation.

2. **Could an AC call it “another memory benchmark”?** Yes, if Intro/Related Work lead with evolving facts, long histories, or ability Acc. Residual is **evaluation methodology for consistency**, not “yet another long-horizon Acc suite.”

3. **Defensible novelty claim:** Acc and cross-query world consistency are empirically distinct for memory systems; existing LTM benches primarily score Acc (or retrieval fitness / profile TCE / lifecycle stages), not Φ over dependent world bundles.

4. **Overclaim wording:** “First consistency benchmark”; “no prior work studies consistency”; “necessary hierarchical memory”; “architecture superiority”; “SOTA”; “real-world validity”; “unique because worlds evolve.”

5. **Strongest reviewer attack:** (a) Incremental memory Acc bench; and/or (b) SetCons/LogicVault already own cross-query consistency; and/or (c) DynamicMem already tracks evolving state consistency; and/or (d) Qwen BCR=0 means metrics are uninformative / synthetic toy.

6. **Strongest rebuttal (completed evidence):** Smoke corruption: high Acc with Φ=0 and consistent-wrong with Acc≪BCR; symbolic Gap_query with BCR>0; Qwen Acc∈[0.09,0.19] with BCR=0 **and** CSR∈[0.26,0.33] separating systems—so floor is real but partial metrics remain informative; object differs from SetCons (memory+world Φ) and DynamicMem (profile TCE).

7. **Contribution #1:** Cross-query consistency evaluation methodology for evolving-world memory (bundles + Φ/BCR + CSR + Acc–consistency gap).

8. **Remove completely:** H0/architecture superiority as a contribution; “first/only consistency”; SOTA; real-world transfer; five-layer necessity; LLM-independent architecture gains.

---

## Recommendation

**ONE POSITIONING CHANGE REQUIRED**

Before drafting Intro/Related Work: (i) add LogicVault/SetCons as **adjacent non-memory** consistency work; (ii) sharpen DynamicMem/MemConflict contrast (profile TCE / conflict fitness ≠ world-bundle Φ); (iii) lead Contribution #1 with Acc≠consistency methodology, not “new memory dataset.”

After that wording lock: READY FOR MANUSCRIPT (benchmark/eval sections already authorized).
