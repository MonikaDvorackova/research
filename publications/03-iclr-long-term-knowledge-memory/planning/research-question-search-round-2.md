# Research Question Search — Round 2 (Phenomena First)

**Status:** exploratory; previous RQs (S1–S15, CR-Gap, archive Pareto, information-access) are **out of scope**  
**Constraint:** LTKM ≈ experimental platform only; architecture is not the claim  
**Non-goals:** manuscript; redesign; implementation; commit  
**Method:** dimensions → hypothesized phenomena → literature kill → architecture-independence → feasibility → top 10 → one recommendation

**Date:** 2026-07-31

---

## Governing rules

1. Begin every candidate with a **phenomenon / hypothesis**, never “we propose a system.”  
2. Reject aggressively against ICLR/NeurIPS/ICML/ACL/EMNLP/COLM/OpenReview/arXiv 2024–2026.  
3. If the architecture disappeared and the question would not matter, **reject**.  
4. Stay inside long-term agent memory / persistence / evolving knowledge / organization / retrieval / continual interaction.

---

# Step 1 — Scientific dimensions (≥80)

Independent axes of long-term agent memory (not contributions):

1. memory formation  
2. encoding fidelity  
3. write admission / gating  
4. write frequency  
5. write latency  
6. eager vs deferred write  
7. consolidation  
8. consolidation timing  
9. consolidation lossiness  
10. consolidation batching  
11. abstraction level  
12. compression ratio  
13. promotion  
14. demotion  
15. forgetting / decay  
16. eviction policy  
17. soft invalidation  
18. hard deletion  
19. interference  
20. associative interference  
21. proactive interference  
22. retroactive interference  
23. retrieval competition  
24. top‑k diversity  
25. near‑duplicate collapse  
26. semantic overlap  
27. lexical overlap  
28. entity overlap  
29. retrieval robustness  
30. retrieval latency  
31. retrieval budget \(k\)  
32. retrieval routing  
33. hybrid retrieval fusion  
34. reranking  
35. memory aging  
36. recency bias  
37. frequency / rehearsal  
38. memory reuse  
39. procedural reuse  
40. episodic reuse  
41. memory scheduling (when to retrieve relative to act)  
42. representation granularity (token / chunk / fact / episode / summary)  
43. structured vs unstructured units  
44. graph structure  
45. graph densification  
46. graph evolution rate  
47. edge typing  
48. conflict density  
49. explicit vs implicit conflict  
50. update locality  
51. update cascade / propagation  
52. revision completeness  
53. provenance richness  
54. provenance utilization at read  
55. source trust / authority  
56. index freshness vs content freshness  
57. indexing lag  
58. memory maintenance cost  
59. memory fragmentation  
60. memory locality of reference  
61. working vs long-term coupling  
62. session boundary effects  
63. cross-session identity binding  
64. multi-store consistency  
65. consolidation lag / eventual consistency  
66. torn reads / partial maintenance visibility  
67. transactional atomicity of belief commit  
68. redundancy  
69. deduplication aggressiveness  
70. calibration of retrieval confidence  
71. uncertainty propagation through memory  
72. abstention / deferral on low confidence  
73. compositionality of multi-evidence assembly  
74. attribute–entity binding at read  
75. temporal binding (value↔time)  
76. causal binding  
77. irreversibility of updates  
78. path dependence / write-order effects  
79. hysteresis after temporary change + revert  
80. saturation of useful capacity  
81. scaling with store size \(N\)  
82. phase transition / critical \(N^\star\)  
83. robustness to distractors  
84. adversarial / poisoned writes  
85. self-generated content pollution  
86. memory laundering via summarization  
87. synchronization across agents  
88. shared vs private memory isolation  
89. query–memory representation mismatch  
90. evidence sufficiency detection  
91. escalation from summary to raw  
92. negative / retracted evidence retention  
93. counterfactual / rollback consistency  
94. auditability / traceability of errors  
95. memory of absence (“never stored” vs “stored false”)  
96. churn rate / belief volatility  
97. distractor temporal distance  
98. intervening update count  
99. multi-target aggregation load  
100. reader utilization given perfect retrieval  

---

# Step 2 — Phenomena / hypotheses (compressed atlas)

For each dimension family, hypothesized phenomena (illustrative, not all carried forward):

| Family | Example hypotheses (form: “We hypothesize that…”) |
|---|---|
| Formation / admission | Write-time admission errors dominate later failures more than retrieval misses; self-generated writes contaminate faster than user writes. |
| Consolidation | Lossiness selectively destroys temporal cues; continuous consolidation is order-sensitive even with fixed episode pools; mid-consolidation torn reads create duplication+contradiction signatures. |
| Interference / competition | Interference concentrates in a minority of items; top‑k collapses to near-duplicates above a redundancy threshold; **attribute binding errors rise with pairwise overlap even when gold is in context**. |
| Retrieval | Fixed-\(k\) accuracy undergoes a nonlinear collapse at critical \(N^\star\) set by semantic density; retrieval success ≠ answer success (utilization gap). |
| Aging / decay | Decay helps until a threshold then erases rare-but-critical facts; rehearsal creates winner-take-all recall. |
| Update / cascade | Related-fact invalidation is incomplete (STALE-like); cascade depth grows superlinearly with graph density. |
| Consistency / lag | Accuracy falls sharply when consolidation lag \(\tau\) exceeds inter-query interval; dual-read of buffer+store removes the cliff. |
| Provenance | Provenance ignored at read unless forced; escalation-to-raw is necessary exactly when summary sufficiency fails. |
| Composition | Multi-hop failures persist after oracle retrieval; binding/rebinding failures dominate omission failures under overlap. |
| Path / hysteresis | Temporary change+revert leaves residual bias; write order changes outcomes under irreversible consolidation. |
| Contamination | Laundering hides toxicity below detectors but changes behavior; poisoned writes have long half-life without gates. |
| Scaling | Usable scale is interface-dependent (Pass@B), not storage-dependent. |
| Multi-agent | Shared memory without isolation propagates contamination faster than private stores. |

---

# Step 3 — Aggressive literature verification (high-signal kills)

| Phenomenon cluster | Closest literature (2024–2026) | Gate |
|---|---|---|
| Interference / multi-target | MINTEval; AIM (associative interference); GAM contamination | **Occupied** as primary story |
| Modular localize compression | “Agentic Memory Should Localize Compression” (ICLR’26 MemAgents) | **Occupied** |
| Retain vs consolidate under budget | *Retain or Consolidate?* | **Occupied** |
| Faulty continuous consolidation | *Useful Memories Become Faulty…* | **Occupied** |
| Lazy vs eager construction | LazyMem; RecMem; MemForest | **Occupied** |
| Staleness / implicit conflict | STALE; MemConflict; CUPMEM | **Occupied** |
| Cascade / compositional after change | **RECON** benchmark | **Occupied** as benchmark object |
| Scale usability / top‑k break | *When Stored Evidence Stops Being Usable*; xMemory; *Price of Meaning* | **Occupied** |
| Contamination / admission | ConsistencyGate; MemGuard; A-MemGuard; State Contamination | **Occupied** |
| Provenance / escalation | TierMem; Eywa; provenance surveys | **Occupied** |
| Rollback / versioning | ChronoMem; bi-temporal TOKI/TGMS/Engram | **Occupied** (systems) |
| Uncertainty in memory | AUQ; Critic Experience Bank | **Occupied** (agent UQ) |
| Retrieval vs utilization | Diagnosing Retrieval vs Utilization | **Occupied** |
| Order sensitivity of consolidation | Useful Memories… (explicit) | **Occupied** |
| Archive / capacity Pareto | **Closed S1 Phase A NO-GO** | **Forbidden** |
| Hierarchy-as-claim | HiMem/GAM/H-MEM/… | **Forbidden** |

### Clusters that remain *partially* open (not clean; need sharp framing)

| ID | Phenomenon | Why not fully killed |
|---|---|---|
| P-Bind | **Attribute–entity binding errors under semantic competition when gold is present** | Interference papers measure accuracy drop; RECON notes post-retrieval failure; few isolate **binding swaps** as dose–response of overlap with gold-in-context held fixed |
| P-Lag | **Consolidation-lag consistency cliff** (accuracy vs \(\tau\)) | Widely noted in systems blogs / async pipelines; scarce as controlled empirical *law* with falsifiable cliff + dual-read ablation |
| P-Torn | **Torn-read signature during multi-step maintenance** (see both new+old) | Mentioned in engineering posts; MemTX argues transactions; little dose–response science |
| P-UtilGap | **Utilization failure modes taxonomy beyond “retrieval missed”** | Known dissociation; still room if taxonomy is causal and overlap-controlled (overlaps P-Bind) |
| P-Hyst | **Hysteresis after temp change+revert under non-versioned stores** | Belief revision papers exist; pure hysteresis curves under matched final state less cleanly published |
| P-Neg | **Necessity of storing explicit retractions for “is X false?” queries** | NeuSymMS retracts without persisting negation; open whether negation memory is required |
| P-Stab | **Historical QA without versioning explained by fact stability, not change memory** | Phase A observation; thin as sole ICLR claim |
| P-Dup | **Near-duplicate top‑k diversity collapse threshold** | xMemory / blogs; high occupancy |
| P-CritN | **Critical \(N^\star(\rho)\) collapse set by overlap density** | Theory+eval exist; residual if \(\rho\) is causal IV with phase-transition test |
| P-Sched | **Retrieve-before-act vs act-then-retrieve scheduling effects** | Thin in memory papers; execution needs agent loop |

---

# Step 4 — Scoring survivors (0–5; higher better)

| ID | Novelty | Falsifiable | Depth | Impl. cost (5=cheap) | Bench need | Proprietary dep. (5=none) | ICLR fit | Arch-free? |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| P-Bind | 4 | 5 | 4 | 5 | 4 (synth OK) | 5 | 4 | Yes |
| P-Lag | 3 | 5 | 3 | 4 | 4 | 5 | 3 | Yes |
| P-Torn | 3 | 4 | 3 | 4 | 4 | 5 | 3 | Yes |
| P-UtilGap | 2 | 4 | 3 | 4 | 3 | 5 | 3 | Yes |
| P-Hyst | 3 | 4 | 3 | 4 | 4 | 5 | 3 | Yes |
| P-Neg | 3 | 4 | 3 | 4 | 4 | 5 | 3 | Yes |
| P-Stab | 2 | 5 | 2 | 5 | 5 | 5 | 2 | Yes |
| P-Dup | 2 | 4 | 2 | 4 | 3 | 5 | 2 | Yes |
| P-CritN | 2 | 4 | 4 | 3 | 3 | 5 | 3 | Yes |
| P-Sched | 3 | 3 | 3 | 2 | 3 | 4 | 3 | Yes |

---

# Step 5 — Architecture-independence filter

Ask: *If LTKM disappeared, would the question still matter?*

| ID | Still matter? | Note |
|---|---|---|
| P-Bind | **Yes** | Any retrieve-then-read memory agent |
| P-Lag | **Yes** | Any async dual-store memory |
| P-Torn | **Yes** | Any multi-step maintenance |
| P-UtilGap | **Yes** | General |
| P-Hyst | **Yes** | Non-versioned stores |
| P-Neg | **Yes** | Belief/retraction semantics |
| P-Stab | **Yes** | Eval methodology |
| P-Dup | **Yes** | Top‑k retrieval |
| P-CritN | **Yes** | Scaling |
| P-Sched | **Yes** | Agent loop; weaker platform fit now |

All above pass. Rejected earlier items that fail this test: “is hierarchy necessary,” “does our five-layer beat Mem0,” etc.

---

# Step 6 — Priority filter (ALL required)

Must be: falsifiable · architecture-independent · ML contribution · agent-memory relevant · publishable without new architecture · small-team executable · local-compute pilot possible.

**Pass:** P-Bind, P-Lag, P-Torn, P-Hyst, P-Neg, P-CritN (borderline novelty), P-UtilGap (borderline novelty).  
**Fail / defer:** P-Dup (occupied), P-Stab (too thin), P-Sched (agent loop cost).

---

# Step 7 — Ten strongest survivors

### 1) P-Bind — Retrieval-conditioned attribute binding failure *(recommended)*

- **RQ:** When gold evidence is present in the retrieved set, do answer errors concentrate in **attribute–entity binding swaps** among semantically overlapping memories, and does that rate scale with overlap independently of Recall@\(k\)?  
- **Phenomenon:** binding/composition failure under semantic competition.  
- **Hypothesis:** We hypothesize that, holding gold-in-top-\(k\) fixed, binding-error rate rises monotonically with pairwise semantic/entity overlap among distractors, while omission errors stay flat.  
- **Closest literature:** MINTEval (interference); RECON (post-retrieval failures); MemGuard (type contamination); LLM rebinding circuits (parametric, not external memory).  
- **Remaining gap:** causal dose–response of **binding** with oracle gold-in-context; not another interference benchmark.  
- **Kill experiment:** synthetic entities; controlled overlap \(\rho\); always insert gold in retrieved set; score omission vs swap vs other; \(\rho\) sweep. Local, symbolic/small reader.  
- **Biggest novelty risk:** “just distractors / Lost in the Middle.”

### 2) P-Lag — Consolidation-lag consistency cliff

- **RQ:** Does answer accuracy exhibit a sharp drop when consolidation lag \(\tau\) exceeds the write–query interval, and does dual-reading raw buffer + consolidated store eliminate it?  
- **Phenomenon:** eventual-consistency cliff in agent memory.  
- **Hypothesis:** We hypothesize a threshold \(\tau^\star\) set by query timing, not by store size.  
- **Closest literature:** async consolidation practice (MemForest, CortexDB, blogs); little controlled \(\mathrm{Acc}(\tau)\) law.  
- **Gap:** empirical cliff + dual-read ablation as science, not ops advice.  
- **Kill experiment:** controllable \(\tau\); queries at offsets; with/without buffer read.  
- **Novelty risk:** “databases 101 / systems paper.”

### 3) P-Torn — Torn-read anomalies in multi-step maintenance

- **RQ:** Do mid-maintenance queries produce a distinctive duplication+contradiction error signature vs pure staleness?  
- **Phenomenon:** torn reads.  
- **Hypothesis:** Error signature frequency scales with maintenance duration × query rate.  
- **Closest literature:** MemTX (transactional commit); engineering posts on partial consolidation.  
- **Gap:** measured anomaly taxonomy vs transactional baseline.  
- **Kill experiment:** non-atomic update protocol vs atomic; probe mid-update.  
- **Novelty risk:** systems/DB framing.

### 4) P-Hyst — Hysteresis after temporary change + revert

- **RQ:** After temp change and revert to the same final state, does non-versioned memory retain residual error vs versioned/as-of stores?  
- **Phenomenon:** path hysteresis.  
- **Hypothesis:** Residual error > 0 under append+similarity retrieval; ≈0 under explicit validity intervals.  
- **Closest literature:** bi-temporal stores; ChronoMem rollback; STALE.  
- **Gap:** hysteresis curve with matched final world state.  
- **Kill experiment:** temp change+revert sequences; matched endpoints.  
- **Novelty risk:** collapses into “use timestamps.”

### 5) P-Neg — Explicit retraction memory for negative queries

- **RQ:** For “is X true?” after retraction, is storing explicit negated evidence necessary, or is deletion of positives sufficient?  
- **Phenomenon:** memory of absence vs memory of negation.  
- **Hypothesis:** Deletion-only fails closed-world negative queries under distractors; explicit retraction marks help.  
- **Closest literature:** NeuSymMS (retract without persisting negation); belief revision.  
- **Gap:** controlled necessity of negation residues.  
- **Kill experiment:** retraction events; negative QA; delete-only vs negate-store.  
- **Novelty risk:** KR-trivial / niche.

### 6) P-CritN — Overlap-conditioned critical store size

- **RQ:** Is there a critical \(N^\star(\rho)\) where fixed-\(k\) accuracy collapses nonlinearly as overlap density \(\rho\) rises?  
- **Phenomenon:** phase-transition-like usable scale.  
- **Hypothesis:** Collapse point depends on \(\rho\) more than on \(N\) alone.  
- **Closest literature:** Price of Meaning; scale-conditioned evaluation; flat-importance collapse.  
- **Gap:** causal \(\rho\) manipulation with transition test.  
- **Kill experiment:** grow \(N\) under low vs high \(\rho\); look for threshold shift.  
- **Novelty risk:** rediscovery of known scaling.

### 7) P-UtilGap — Causal taxonomy of post-retrieval failures

- **RQ:** Conditional on gold in context, what failure mode dominates (binding, contradiction preference, abstention, instruction neglect)?  
- **Phenomenon:** utilization taxonomy.  
- **Hypothesis:** Binding dominates under overlap; contradiction preference dominates under conflict.  
- **Closest literature:** retrieval-vs-utilization; MemConflict; RECON.  
- **Gap:** factorial mapping mode←condition.  
- **Kill experiment:** condition grid; forced gold-in-context.  
- **Novelty risk:** incremental diagnostic paper.

### 8) P-Lag×Rate — Write rate × lag interaction

- **RQ:** Does the lag cliff move predictably with write frequency (queueing of consolidation)?  
- **Phenomenon:** load-dependent consistency.  
- **Hypothesis:** \(\tau^\star\) shrinks as write rate rises under fixed consolidator throughput.  
- **Closest literature:** consolidation queue monitoring (ops); scarce ML curves.  
- **Gap:** controlled throughput experiment.  
- **Kill experiment:** vary write rate & consolidator speed.  
- **Novelty risk:** queueing theory restatement.

### 9) P-Hyst-Ret — Revert completeness under soft vs missing invalidation

- **RQ:** After revert, soft-invalidated old values still leak into answers at rate predicted by retrieval score margins?  
- **Phenomenon:** invalidation leakage.  
- **Hypothesis:** Leakage ∝ similarity(old, query) when invalidation flags are ignored by retriever.  
- **Closest literature:** Engram/Zep invalidate; STALE.  
- **Gap:** leakage vs score-margin law.  
- **Kill experiment:** soft-invalidate but retrieve without filter vs with filter.  
- **Novelty risk:** “filter on deprecated” obvious.

### 10) P-Bind-Temp — Temporal binding failures (right value, wrong time)

- **RQ:** Under overlapping values across time, do errors concentrate in wrong-interval selection rather than wrong entity?  
- **Phenomenon:** temporal binding error.  
- **Hypothesis:** Temporal swaps dominate entity swaps when values recur across intervals.  
- **Closest literature:** temporal memory benchmarks; bi-temporal QA.  
- **Gap:** error-type isolation with recurring values.  
- **Kill experiment:** recurring values across time; score temporal vs entity errors.  
- **Novelty risk:** temporal QA occupancy.

---

# Step 8 — One recommendation

## Recommended scientific question

> **We ask whether, when the gold memory item is already present in the retrieved top‑\(k\), remaining answer errors are primarily attribute–entity binding failures induced by semantic competition among co-retrieved items—and whether that binding-error rate scales with overlap structure independently of Recall@\(k\).**

**Operational hypothesis:**  
We hypothesize a dissociation: under oracle (or near-oracle) gold-in-context, omission errors stay near floor while **binding-swap errors** rise with controlled distractor overlap \(\rho\); reducing overlap or enforcing entity-constrained retrieval reduces swaps without changing Recall@\(k\).

**Scientific object:** post-retrieval **binding / composition** failure under competition.  
**Not the object:** a new memory architecture; archive allocation; hierarchy superiority.

**Platform role of LTKM:** store large evolving sets of overlapping facts across tiers; expose deterministic retrieval of size \(k\); enable white-box inspection of retrieved sets. Any memory store with top‑\(k\) retrieval could host the experiment—the question still matters if LTKM vanishes.

### Why stronger than S1 (archive Pareto)

| | S1 (closed) | P-Bind |
|---|---|---|
| Phenomenon | Current–historical Pareto under \(\alpha\) | Binding errors under overlap with gold present |
| Phase A lesson | Joint degradation; \(\alpha=0\) dominated; fake historical hits via stability | Does **not** rely on splitting \(B_c/B_a\); holds gold-in-context fixed |
| Failure mode | Capacity starvation confound | Composition/utilization confound—the field’s stated bottleneck after retrieval |
| Architecture temptation | High (archive tier) | Low (error taxonomy + scaling law) |

### Why stronger than CR-Gap

| | CR-Gap | P-Bind |
|---|---|---|
| Object | Overwrite vs revision reconstruction | Binding under competition |
| Confound | Reader / fair keep-all | Controlled by forcing gold into retrieved set |
| Occupancy | Conflict/update adjacent | Interference benches exist, but binding dose–response with gold fixed is sharper |

### Why it survives current literature

- MINTEval / AIM show **interference hurts** — they do not isolate **binding swaps** with gold held in context.  
- RECON shows **post-retrieval reasoning** is hard — it is a broad compositional benchmark, not a binding scaling law.  
- Retrieval-vs-utilization shows retrieval dominates LoCoMo — P-Bind studies the residual **when retrieval is solved**.  
- MemGuard studies type contamination — related, but not overlap dose–response for attribute swaps.  

Residual novelty risk remains (“distractors”); the kill pilot must pre-register error types and the gold-in-context invariant.

### Why an ICLR Area Chair would care

1. **Clear ML object:** an error mechanism + scaling with a continuous IV (\(\rho\)), not a system bake-off.  
2. **Explains a known pain:** agents fail even when evidence is retrieved (RECON/MemConflict signal) — offers a *mechanistic* account.  
3. **Falsifiable cheaply:** synthetic world, local compute, symbolic or small extractive reader first.  
4. **Actionable without selling architecture:** entity-constrained retrieval / diversity constraints / reranking become *interventions on the phenomenon*, not the paper’s identity.  
5. **Fits agent memory:** long-term stores accumulate overlap; competition worsens with persistence—core to the area without requiring “our hierarchy.”

---

## Provisional next step (not executed here)

Design a **kill pilot** for P-Bind only:

1. Synthetic entities with tunable overlap \(\rho\).  
2. Force gold ∈ retrieved set.  
3. Measure P(bind swap), P(omit), P(other).  
4. GO only if \(\mathrm{range}_\rho P(\mathrm{swap})\ge 0.10\) and omit stays within 0.03.  
5. NO-GO if errors are unstructured or fully explained by reader noise independent of \(\rho\).

---

## Explicit exclusions (Round 2)

Do not revive: S1–S15 labels, archive Pareto, CR-Gap, information-access dissociation, hierarchy-superiority claims, “LTKM beats baselines” claims.

---

## Changed files

- `publications/03-iclr-long-term-knowledge-memory/planning/research-question-search-round-2.md` (this file)

**Validation:** targeted literature scans (interference, consolidation lag, contamination, provenance, scaling, RECON, binding/rebinding, async consistency). No experiments run. No manuscript. No architecture redesign.
