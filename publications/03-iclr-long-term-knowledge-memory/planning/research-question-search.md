# Research Question Search — Hierarchical Long-Term Knowledge Memory

**Status:** exploratory analysis for Publication 03  
**Constraint:** the hierarchical LTKM system is **fixed** as experimental platform; architecture is **not** the claim  
**Non-goals:** redesign the system; write a manuscript; search unrelated ICLR topics  
**Central question this document answers:** *What is the best scientific question that this existing system can answer?*

**Date:** 2026-07-31  
**Method:** Area-Chair style — enumerate → cluster → literature-gate → novelty-filter individuals → rank survivors only

---

## Governing principles

1. Treat every outline ingredient as an **experimental variable**, not a contribution.
2. Reject questions that ask “does our architecture work?” without an isolable scientific object.
3. Prefer questions where the team’s system supplies **controlled levers** (tiers, lifecycle ops, archive, graph, promotion) that other papers lack as a clean factorial platform.
4. Do **not** resurrect CR-Gap (overwrite vs revision-aware reconstruction) or Information-Access Regime Dissociation (multi-turn vs single-shot).

---

# Step 1 — Scientific ingredients (variables only)

Extracted from the collaborative outline / research specification. None of these is assumed to be a contribution.

| ID | Ingredient | Treat as variable / factor |
|---|---|---|
| I1 | Hierarchy (working / session / long-term / archive) | number of tiers; which tiers exist |
| I2 | Working memory | presence; capacity; eviction |
| I3 | Session memory | boundary policy; retention across turns |
| I4 | Long-term memory | write policy; indexing; capacity |
| I5 | Archive | retention of superseded / historical states |
| I6 | Graph structure | graph vs flat; edge types; update rules |
| I7 | Knowledge lifecycle | create / update / promote / demote / forget / archive |
| I8 | Promotion | criterion; timing; source→target tier |
| I9 | Forgetting / pruning | criterion; rate; hard delete vs soft invalidate |
| I10 | Consolidation / summarization | when; lossiness; cue preservation |
| I11 | Retrieval | method; budget *k*; tier routing |
| I12 | Update / conflict handling | overwrite; revise; keep both; adjudicate |
| I13 | Temporal change | timestamps; as-of queries; order cues |
| I14 | Long-term consistency | metric over evolving knowledge |
| I15 | Evolving world | synthetic dynamics; conflict density; horizon |
| I16 | Agent interaction | write after act; feedback into lifecycle |
| I17 | Task families | current / historical / conflicting / multi-hop / temporal |
| I18 | Memory organization / representation | fact / episode / note / graph node units |
| I19 | Scaling | history length; entity count; write rate |
| I20 | Baselines / transfer | other memory systems as platforms for same IV |

---

# Step 2 — Candidate research questions (no judgment)

*N = 48. Illustrative phrasing only at generation time.*

### Hierarchy & representation
1. Does hierarchy improve long-term consistency vs a single flat store under matched capacity?
2. Which tier, if removed, causes the largest drop on which task family?
3. Is an archive tier necessary for historical queries, or does long-term alone suffice?
4. Do different memory units (raw episode vs extracted fact vs summary note) dominate accuracy?
5. What representations emerge under consolidation (do compressed units preserve temporal/conflict cues)?
6. Is graph structure necessary given hierarchy, or is hierarchy alone enough?
7. Does edge typing (temporal vs semantic vs causal) matter beyond untyped links?
8. Does hierarchy change *what* is stored, or only *where* it is stored?

### Lifecycle, promotion, forgetting, consolidation
9. Does an explicit lifecycle improve consistency vs append-only storage?
10. When does promotion help vs hurt downstream reasoning?
11. Which promotion criterion dominates (recurrence, importance, conflict, semantic-shift, recency)?
12. Can forgetting improve reasoning accuracy under fixed retrieval budget?
13. Does soft invalidation outperform hard deletion for conflicting/historical tasks?
14. Which lifecycle operation has the largest marginal effect (write, update, promote, forget, archive, retrieve)?
15. Does decoupling encoding from consolidation reduce interference?
16. Does consolidation destroy chronological cues needed for temporal/historical tasks?
17. Is early vs late consolidation better under rapid world change?
18. Can promotion/forgetting policies be learned from task feedback better than fixed heuristics?

### Retrieval, routing, update, conflict
19. Does retrieval quality dominate write sophistication under this system’s evolving-world tasks?
20. Does query-type × tier routing beat uniform search across all tiers?
21. Is retrieval failure or utilization failure the primary bottleneck?
22. How should conflicts be resolved at write time vs read time?
23. Does detecting implicit conflict (no explicit negation) require different lifecycle ops than explicit conflict?
24. Does update correctness predict answer correctness, or can they dissociate?
25. Under conflict, is “keep-all + adjudicate at read” better than “write-time resolve”?

### Temporal reasoning & evolving world
26. Does hierarchical LTKM preserve temporal order better than flat RAG under evolution?
27. As horizon grows, which failure mode appears first (retrieval miss, stale promotion, cue loss, conflict)?
28. Does performance on current-state queries trade off against historical-state queries under fixed memory budget?
29. Does conflict density interact with hierarchy (does hierarchy help more as conflicts increase)?
30. Can the system answer as-of-*t* queries without replaying full history?
31. Do temporal gains transfer from conversational benchmarks (LoCoMo/LongMemEval) to a synthetic evolving world?

### Continual adaptation & interaction
32. Does agent action feedback change optimal promotion thresholds?
33. Does write-after-act memory improve consistency vs write-from-dialogue-only?
34. Under continual updates, does the memory store remain stable or catastrophically degrade?
35. Do policies tuned on short horizons transfer to long horizons?

### Graph structure (focused)
36. For which task families is graph necessary given the rest of the stack?
37. Does graph help updates more than retrieval (or the reverse)?
38. Are multi-hop gains from graph causal, or confounded by denser indexing?

### Benchmark & evaluation
39. Can a synthetic evolving-world benchmark expose failures that LoCoMo/LongMemEval miss?
40. Do black-box answer metrics hide white-box memory failures (retrieval/ranking/update)?
41. Which primary metric best tracks “long-term knowledge consistency”?
42. Do relative rankings of memory systems change across task families (no universal winner)?

### Scaling & theory
43. What scales: entities, sessions, conflict rate, or retrieval budget?
44. Is there a capacity–accuracy Pareto frontier across tiers?
45. Can lifecycle dynamics be modeled as a control process with identifiable regimes?
46. Does hierarchy reduce sample complexity of retrieval learning?

### Transfer & interaction with baselines
47. Do findings about lifecycle ops transfer across memory backends (team system vs Mem0/A-Mem/MemGPT-style)?
48. Does the same promotion policy help all baselines, or only hierarchical ones?

---

# Step 3 — Clusters

| Cluster | Candidate IDs |
|---|---|
| Representation | 1, 2, 3, 4, 5, 8 |
| Graph structure | 6, 7, 36, 37, 38 |
| Lifecycle | 9, 14, 15 |
| Consolidation | 10, 11, 16, 17 |
| Forgetting | 12, 13, 18 |
| Retrieval | 19, 20, 21 |
| Conflict / update | 22, 23, 24, 25 |
| Temporal reasoning | 26, 27, 30, 31 |
| Continual adaptation | 28, 29, 32, 33, 34, 35 |
| Scaling | 43, 44, 46 |
| Theory | 45 |
| Benchmark / evaluation | 39, 40, 41, 42 |
| Transfer / interaction | 47, 48 |

---

# Step 4 — Openness by cluster (with literature)

Evidence is current literature as of mid/late 2026 searches. Labels:

- **Solved / heavily occupied:** multiple strong papers already answer the question as stated  
- **Partially open:** answered in a related setting; open under this system’s factors/world  
- **Genuinely open:** no clean causal answer located for this formulation

### Representation
| Status | Notes |
|---|---|
| Heavily occupied | Q1–Q2: HiMem, HiGMem, H-MEM, GAM ablations show hierarchy components matter on dialogue benchmarks. |
| Partially open | Q3 (archive necessity for *historical* vs long-term alone): archive tiers exist (MemGPT/Letta, HMO), but causal necessity for historical *knowledge consistency* under evolving worlds is thinner. |
| Partially open | Q4–Q5: write-unit comparisons exist (raw vs fact vs summary; “Diagnosing Retrieval vs Utilization,” Infini Memory), but cue-loss under consolidation for historical/conflict is flagged as open by MemoryData-style evaluations. |
| Occupied as architecture claim | Q8 as “our hierarchy organizes better” is a system paper, not a scientific RQ. |

### Graph structure
| Status | Notes |
|---|---|
| Heavily occupied | Q6, Q36: ACL 2026 “Does Memory Need Graphs?”; Mem0-g; GAM; systematic MemoryData findings (graph helps some slices, not all). |
| Partially open | Q37–Q38: MemoryData suggests graphs help updates; causal separation from indexing density still messy. |

### Lifecycle / consolidation / forgetting
| Status | Notes |
|---|---|
| Heavily occupied | Q9, Q15: GAM decoupling encoding/consolidation; RecMem when-to-consolidate; many “lifecycle” system papers. |
| Heavily occupied | Q12: FadeMem; MemoryAgentBench FactConsolidation; MemCon prune/consolidate. |
| Partially open | Q10–Q11: promotion *timing* studied (RecMem recurrence); **which criterion dominates under multi-task evolving worlds** less settled as a factorial science question. |
| Partially open | Q13: Engram-style invalidate-not-delete; Zep bitemporal; not fully settled vs hard delete on historical tasks. |
| Partially open | Q14: retrieval often dominates write on LoCoMo (“Diagnosing Retrieval vs Utilization”); **dominance under synthetic evolving + archive/historical/conflict suite** not established. |
| Partially open | Q16–Q17: MemoryData notes consolidation can destroy chronological cues; Infini/Engram explore maintenance—causal “does consolidation destroy cues?” under controlled lossiness is still fertile. |
| Partially open | Q18: MemCon learns adaptive control; still early vs fixed heuristics on hierarchical multi-tier LTKM. |

### Retrieval / conflict
| Status | Notes |
|---|---|
| Heavily occupied | Q19, Q21: retrieval vs utilization diagnostics. |
| Heavily occupied | Q20: SelRoute; “Did You Check the Right Pocket?” store routing. |
| Heavily occupied | Q22–Q23, Q25: STALE (implicit conflict); MemConflict; HiMem conflict-aware update; CUPMEM. |
| Partially open | Q24: MemConflict already shows answer vs retrieval dissociation; extending to *lifecycle white-box* states under team system is incremental. |

### Temporal / continual / budget tradeoffs
| Status | Notes |
|---|---|
| Partially open | Q26, Q30: bi-temporal Engram; MAGMA temporal; still contested whether hierarchy *causally* preserves order vs flat under matched info. |
| Partially open | Q27, Q34: BEAM scale drops; MemoryData long-horizon degradation—mechanism identity under team levers open. |
| **Genuinely open (high value)** | **Q28:** current vs historical accuracy under **fixed memory budget** with an explicit archive lever—accuracy/latency tradeoffs exist, but **current↔historical Pareto under archive retention** is not a settled causal finding. |
| Partially open | Q29: conflict × structure interactions appear in MemConflict sensitivity; hierarchy×conflict factorial rare. |
| Partially open | Q31: transfer conversational→synthetic world under-tested as a scientific claim. |
| Thin | Q32–Q33: write-after-act / interactive promotion less central in LoCoMo-style papers. |

### Benchmark / scaling / theory / transfer
| Status | Notes |
|---|---|
| Heavily occupied as *paper type* | Q39–Q42: LoCoMo, LongMemEval, BEAM, STALE, MemConflict, MemoryAgentBench, MemoryData—benchmark papers are crowded unless the metric object is new. |
| Partially open | Q43–Q44: system characterization papers exist; tier Pareto under scientific IVs still usable as secondary. |
| Open but hard for ICLR empirics | Q45–Q46: theory/control. |
| Partially open | Q47–Q48: backend-agnostic lifecycle findings (MemCon spirit) attractive if ops are the object. |

---

# Step 5 — Novelty filtering (reject individuals, not clusters)

## Rejected questions

| ID | Question (short) | Reject reason |
|---|---|---|
| 1 | Does hierarchy help? | Occupied: HiMem / HiGMem / H-MEM / GAM ablations. Asking it again = architecture paper. |
| 2 | Which tier ablation hurts most? | Occupied as standard ablation appendix; not a primary ICLR RQ unless tied to a new causal claim. |
| 4 | Which memory unit is best? | Occupied: write-strategy comparisons; often small effects vs retrieval. |
| 6 | Is graph necessary? | Occupied: “Does Memory Need Graphs?” + MemoryData. |
| 7 | Do edge types matter? | Incremental system detail; weak standalone science without new phenomenon. |
| 8 | Hierarchy changes what vs where? | Too vague / definitional for decisive experiment. |
| 9 | Does lifecycle beat append-only? | Occupied by many lifecycle systems; claims “lifecycle helps” are saturated. |
| 12 | Can forgetting improve reasoning? | Occupied: FadeMem et al. |
| 15 | Decouple encode vs consolidate? | Occupied: GAM core claim. |
| 18 | Learn promotion/forget policies? | Occupied enough by MemCon; high overlap unless sharply different object. |
| 19 | Retrieval dominates write? | Occupied: Diagnosing Retrieval vs Utilization (LoCoMo). |
| 20 | Query-type routing helps? | Occupied: SelRoute; store-routing paper. |
| 21 | Retrieval vs utilization bottleneck? | Occupied by same diagnostic line. |
| 22 | Write-time vs read-time conflict? | Crowded: STALE, MemConflict, conflict-aware memories. |
| 23 | Implicit conflict special? | Occupied: STALE’s primary object. |
| 25 | Keep-all vs resolve-at-write? | Too close to failed CR-Gap / conflict papers; high duplicate risk. |
| 26 | Hierarchy preserves temporal order? | Partially answered; remaining gap is narrow and easy to overclaim. |
| 30 | As-of-*t* without full history? | Engram bi-temporal already pushes this; system-overlap risk. |
| 36–38 | Graph necessity / causality | Occupied or confounded; poor primary RQ for this team. |
| 39 | New benchmark exposes failures? | Benchmark-only papers crowded; OK as *vehicle*, not *question*. |
| 41 | Best consistency metric? | Metrology paper; usually secondary. |
| 42 | No universal winner? | MemoryData already argues workload dependence. |
| 45–46 | Theory / sample complexity | Not matched to current experimental ownership. |

## Surviving questions (after filter)

| ID | Surviving question | Why it survives |
|---|---|---|
| **S1 ← 28** | Under a fixed memory budget, does retaining archived historical states improve historical-task accuracy without harming current-task accuracy (Pareto / tradeoff)? | Uses archive as IV; not “is hierarchy good?”; distinct from CR-Gap’s overwrite mechanism. Literature covers cost/accuracy and staleness, not this Pareto cleanly. |
| **S2 ← 11** | Which promotion criterion (recurrence / importance / conflict / semantic-shift / recency) dominates accuracy across task families in an evolving world? | RecMem answers *when* (recurrence) in one design; factorial *which criterion* under multi-family evolving world remains open. Object = criterion, not architecture. |
| **S3 ← 14** | Which lifecycle operation dominates performance on an evolving-world suite with historical/conflict tasks—does retrieval still dominate as on LoCoMo? | Tests transfer of a published dominance result to a different scientific regime the team already planned. |
| **S4 ← 16** | Does increasing consolidation lossiness causally destroy temporal/conflict cues required for historical and conflicting tasks? | MemoryData flags the phenomenon; decisive causal dose–response on lossiness is still open. Object = information destruction, not “we consolidate better.” |
| **S5 ← 3** | Is an explicit archive tier necessary for historical queries given long-term memory, under matched total storage? | Sharper than “hierarchy helps”; isolable tier necessity. |
| **S6 ← 10** | When does promotion help vs hurt (non-monotonicity / regime boundary)? | Goes beyond “promotion good”; seeks failure regimes. |
| **S7 ← 29** | Does hierarchy’s benefit increase with conflict density (interaction effect)? | Interaction claims rarer than main-effect ablations; still moderate novelty risk. |
| **S8 ← 24** | Do white-box update/retrieval correctness and black-box answers dissociate under lifecycle interventions? | MemConflict shows dissociation; survives only if lifecycle intervention is the IV (not another conflict taxonomy paper). |
| **S9 ← 31** | Do relative effects of lifecycle interventions transfer from conversational memory benchmarks to a synthetic evolving world? | Transfer science; uses system as platform across worlds. |
| **S10 ← 47** | Do lifecycle-operation effects transfer across memory backends? | Backend-agnostic scientific object; architecture becomes disposable substrate. |
| **S11 ← 27** | As horizon grows, which failure mode appears first under controlled lifecycle settings? | Mechanism-ordering question; needs careful labeling protocol. |
| **S12 ← 13** | Soft invalidation vs hard deletion for historical vs current tasks under matched budget? | Related to Engram/Zep; survives if framed as task-family tradeoff, not new delete operator. |
| **S13 ← 33** | Does write-after-act change optimal promotion relative to dialogue-only writes? | Thinner literature; higher execution risk if agent loop immature. |
| **S14 ← 5** | What cues survive consolidation (emergent representation fidelity)? | Measurement-heavy; good secondary, risky as sole RQ. |
| **S15 ← 44** | What is the tier capacity–accuracy Pareto frontier? | Strong systems contribution; weaker pure science unless tied to S1. |

---

# Step 6 — Survivor cards

### S1 — Current–historical Pareto under archive retention
- **Scientific object:** archive retention policy (how much superseded state is kept) under fixed total memory budget.
- **Hypothesis:** Increasing archive retention improves historical-task accuracy up to a point, then harms current-task accuracy via retrieval competition (non-trivial Pareto, not free lunch).
- **Smallest decisive experiment:** 2×N grid — archive retention ∈ {0, low, mid, high} × task family ∈ {current, historical}; freeze retrieval *k* and total bytes/tokens; one backend (team LTKM).
- **Required benchmark:** synthetic evolving world with paired current/historical queries on the same entities (team suite); optional LongMemEval knowledge-update slice as transfer check.
- **ICLR fit:** high — causal tradeoff, clear plots, falsifiable, not “another memory system.”
- **Novelty risk:** **medium-low**. Staleness/conflict papers nearby; Pareto framing under archive lever is less occupied than hierarchy ablations.

### S2 — Promotion-criterion dominance
- **Scientific object:** promotion criterion (rule selecting what moves between tiers).
- **Hypothesis:** No single criterion dominates all task families; conflict-triggered promotion helps conflicting/current, recurrence helps multi-hop, etc. (interaction, not universal winner).
- **Smallest decisive experiment:** swap only the promotion scorer; hold tiers, retrieval, capacity fixed; measure per-family accuracy + promotion traffic stats.
- **Required benchmark:** evolving world with labeled task families; LoCoMo as secondary.
- **ICLR fit:** high — factorial science on a control knob.
- **Novelty risk:** **medium**. RecMem/GAM touch nearby; survives if criterion×task-family is pre-registered and not sold as a new memory OS.

### S3 — Lifecycle-operation dominance under evolving world
- **Scientific object:** marginal contribution of lifecycle ops (ablate update / promote / forget / archive / retrieve quality) on non-dialogue evolving tasks.
- **Hypothesis:** Unlike LoCoMo conversational QA, update/archive ops rival or exceed retrieval improvements on historical/conflict slices.
- **Smallest decisive experiment:** controlled op ablations + one retrieval upgrade, same write store; compare Δaccuracy by task family.
- **Required benchmark:** team evolving-world suite (must include historical + conflict).
- **ICLR fit:** high if it **falsifies or bounds** the published retrieval-dominance result.
- **Novelty risk:** **medium**. Risky if results merely reconfirm retrieval dominance without a regime map.

### S4 — Consolidation lossiness destroys cues
- **Scientific object:** consolidation lossiness (information-retention level of summaries/facts).
- **Hypothesis:** Higher lossiness selectively collapses temporal and conflict performance while sparing single-hop current facts.
- **Smallest decisive experiment:** dose–response over lossiness levels; probe cue presence in memory store (white-box) + answers (black-box).
- **Required benchmark:** temporal + conflicting + current controls; MemoryData-style probes optional.
- **ICLR fit:** high — clean causal story about representation fidelity.
- **Novelty risk:** **medium**. Phenomenon noted; decisive dose–response still publishable if measurement is rigorous.

### S5 — Archive tier necessity
- **Scientific object:** presence of archive tier under matched storage.
- **Hypothesis:** Without archive, historical accuracy drops more than current; matched-capacity long-term expansion cannot substitute.
- **Smallest decisive experiment:** archive on vs off, redistribute capacity to LTM; same retrieval budget.
- **Required benchmark:** historical vs current split.
- **ICLR fit:** medium-high (ablation-shaped; needs strong matched-capacity controls).
- **Novelty risk:** **medium-high** (looks like hierarchy ablation unless matched-capacity is airtight).

### S6 — When promotion helps vs hurts
- **Scientific object:** promotion rate / aggressiveness.
- **Hypothesis:** Over-promotion harms current consistency (noise in hot tiers); under-promotion harms multi-hop/historical; U-shaped curve.
- **Smallest decisive experiment:** sweep promotion threshold; plot accuracy vs promotion volume.
- **Required benchmark:** multi-family evolving world.
- **ICLR fit:** high if non-monotonicity is real and robust.
- **Novelty risk:** **medium**.

### S7 — Hierarchy × conflict-density interaction
- **Scientific object:** interaction term hierarchy×conflict.
- **Hypothesis:** Hierarchy’s relative gain increases with conflict density.
- **Smallest decisive experiment:** 2×3 design (flat vs hierarchical × conflict levels), matched capacity.
- **Required benchmark:** controllable conflict-density world (team) + MemConflict-style distractors.
- **ICLR fit:** medium-high.
- **Novelty risk:** **medium-high** (hierarchy main effect occupied; interaction must be clean).

### S8 — White-box / black-box dissociation under lifecycle IV
- **Scientific object:** dissociation between memory-state correctness and answer correctness under lifecycle interventions.
- **Hypothesis:** Some ops fix answers without fixing memory ranking (or reverse).
- **Smallest decisive experiment:** intervene on one op; report answer metric + retrieval/update probes.
- **Required benchmark:** MemConflict-like white-box labels or team equivalent.
- **ICLR fit:** medium (evaluation methodology flavor).
- **Novelty risk:** **medium-high** vs MemConflict.

### S9 — Transfer across worlds
- **Scientific object:** external validity of lifecycle effects.
- **Hypothesis:** Effect rankings differ between LoCoMo/LongMemEval and synthetic evolving world.
- **Smallest decisive experiment:** same interventions on both worlds; rank-correlate Δs.
- **Required benchmark:** both.
- **ICLR fit:** medium (negative transfer is valuable; positive is incremental).
- **Novelty risk:** **medium**.

### S10 — Transfer across backends
- **Scientific object:** backend-agnostic lifecycle effects.
- **Hypothesis:** Promotion/archive effects replicate on ≥2 backends; hierarchy-specific effects do not.
- **Smallest decisive experiment:** identical op policies wrapped on team system + one external memory API.
- **Required benchmark:** shared task suite.
- **ICLR fit:** high for generality claims.
- **Novelty risk:** **medium** (MemCon already backend-agnostic control).

### S11 — Failure-mode ordering with horizon
- **Scientific object:** ordered degradation mechanisms.
- **Hypothesis:** As horizon grows, retrieval competition precedes cue loss precedes update failure (or another fixed order).
- **Smallest decisive experiment:** horizon sweep with labeled failure taxonomy.
- **Required benchmark:** long-horizon evolving world / BEAM-like scale if feasible.
- **ICLR fit:** medium-high.
- **Novelty risk:** **medium** (taxonomy must not be post-hoc).

### S12 — Soft invalidate vs hard delete tradeoff
- **Scientific object:** deletion semantics.
- **Hypothesis:** Soft invalidation helps historical, hard delete helps current under tight budgets.
- **Smallest decisive experiment:** two delete semantics × budget levels × task families.
- **Required benchmark:** historical/current split.
- **ICLR fit:** medium.
- **Novelty risk:** **medium-high** near Engram/Zep.

### S13 — Write-after-act vs dialogue-only
- **Scientific object:** interaction-sourced writes.
- **Hypothesis:** Action-grounded writes change promotion optima and reduce false promotions.
- **Smallest decisive experiment:** dialogue-only vs act-coupled write channel; same world.
- **Required benchmark:** interactive evolving world (needs agent loop).
- **ICLR fit:** medium (depends on agent fidelity).
- **Novelty risk:** **medium**; **execution risk high**.

### S14 — Emergent cue survival
- **Scientific object:** measurable cue retention under consolidation.
- **Hypothesis:** Temporal/conflict cues decay faster than entity facts under standard consolidation.
- **Smallest decisive experiment:** probe suite on memory contents across consolidation levels.
- **Required benchmark:** white-box probes + QA.
- **ICLR fit:** medium (can be subsumed by S4).
- **Novelty risk:** **medium**.

### S15 — Tier capacity Pareto
- **Scientific object:** allocation across tiers.
- **Hypothesis:** Optimal allocation depends on task-family mixture.
- **Smallest decisive experiment:** simplex sweep over tier budgets.
- **Required benchmark:** multi-family suite.
- **ICLR fit:** medium (systems/Pareto).
- **Novelty risk:** **medium**; better as companion to S1.

---

# Step 7 — Ranking of surviving research questions only

Rank by: (a) isolable scientific object, (b) literature gap, (c) fit to **existing** LTKM levers, (d) decisive small experiment, (e) ICLR empirics, (f) distance from failed CR-Gap / Information-Access.

| Rank | ID | Score rationale (short) |
|---|---|---|
| 1 | **S1** | Clean object (archive retention); uses distinctive team lever; Pareto is falsifiable; not architecture worship; far from CR-Gap mechanism fight. |
| 2 | **S2** | Strong factorial science; system is platform for criterion swap; clear ICLR plots. |
| 3 | **S4** | Causal story about information destruction; explains *why* lifecycle ops matter. |
| 4 | **S3** | High conceptual payoff if it bounds retrieval-dominance; depends on world differing from LoCoMo. |
| 5 | **S6** | Non-monotonic promotion regimes; elegant if real. |
| 6 | S5 | Good but ablation-shaped; easier to dismiss as “hierarchy paper.” |
| 7 | S10 | Generality attractive; needs multi-backend cost. |
| 8 | S9 | Important validity check; weaker as sole claim. |
| 9 | S7 | Interaction interesting; hierarchy factor raises occupancy risk. |
| 10 | S11 | Valuable mechanism map; taxonomy risk. |
| 11 | S12 | Narrow vs Engram/Zep. |
| 12 | S8 | Too close to MemConflict unless lifecycle IV is central. |
| 13 | S15 | Secondary systems result. |
| 14 | S14 | Fold into S4. |
| 15 | S13 | Scientifically fine; execution/agent-loop risk highest. |

---

# Step 8 — Five strongest RQs (system = platform only)

1. **S1 — Current–historical Pareto under archive retention**  
   *Architecture enables controlled archive budgets; claim is the tradeoff law.*

2. **S2 — Promotion-criterion × task-family dominance**  
   *Architecture enables tier moves; claim is which selection rule wins when.*

3. **S4 — Consolidation lossiness selectively destroys temporal/conflict cues**  
   *Architecture enables consolidation dial; claim is causal cue destruction.*

4. **S3 — Lifecycle-operation dominance on evolving-world historical/conflict tasks**  
   *Architecture exposes ops; claim is which op binds in this regime.*

5. **S6 — Non-monotonic effect of promotion aggressiveness**  
   *Architecture exposes promotion rate; claim is help/hurt regimes.*

---

## One recommended research question

> **Under a fixed total memory budget, how does archive retention of superseded knowledge trade off current-state accuracy against historical-state accuracy in long-term LLM agents operating in an evolving world?**

**Operational form (for experiments):**

> Holding hierarchy, retrieval budget *k*, and total memory capacity fixed, does increasing archive retention of superseded states improve historical-task accuracy, and at what retention levels does current-task accuracy degrade due to retrieval competition?

**Scientific object:** archive retention (not “hierarchical memory”).  
**Platform role of LTKM:** supplies archive + lifecycle + evolving-world task suite so the tradeoff can be measured.  
**Primary claim type:** empirical tradeoff / regime characterization.  
**Not claimed:** that the team invented hierarchical memory, that hierarchy is new, or that the system beats all baselines by architecture.

### Why this is stronger than rejected CR-Gap

| | CR-Gap (rejected) | Recommended S1 |
|---|---|---|
| Object | Overwrite vs revision-aware *reconstruction* of past state | Archive retention budget vs current/historical *accuracy tradeoff* |
| Failure mode | Reader-confounded; fair keep-all ≈ revision-aware; no clean causal factor | Isolable continuous IV (retention) with predicted non-monotonic / Pareto structure |
| Dependence on “who is right about history” | High (reconstruction faithfulness) | Lower (task-labeled current vs historical questions with ground truth in synthetic world) |
| Occupancy | Adjacent to conflict/update literature; hard to isolate | Nearby papers study staleness or cost/accuracy, not this archive Pareto on paired current/historical families |
| Role of system | Tempted to become the claim | Explicitly only the experimental platform |

### Why this is stronger than rejected Information-Access (C1)

| | Information-Access Regime Dissociation | Recommended S1 |
|---|---|---|
| Object | Multi-turn vs single-shot information access | Memory archive retention under capacity constraints |
| Occupancy | Occupied (e.g. *Lost in Conversation*, ICLR 2026 Best Paper lineage) | Not that paper’s object |
| Fit to LTKM | Weak — does not need hierarchical archive/lifecycle | Strong — archive tier is a native lever |
| Risk | Topic replacement / duplicate of conversational failure work | Stays inside the collaborative subject while changing the *question* |

### Why not recommend “does hierarchical LTKM improve consistency?” (outline RQ-A)

That question makes **architecture the claim**. Area Chairs will score it as yet another hierarchical agent-memory system paper against HiMem/GAM/H-MEM/HiGMem. S1 keeps the same system and asks a sharper, less occupied scientific question.

---

## Deliverable checklist

| Deliverable | Location in this doc |
|---|---|
| All candidate questions | Step 2 (Q1–Q48) |
| Clusters | Step 3 |
| Literature-supported openness | Step 4 |
| Rejected questions + reasons | Step 5 |
| Surviving questions | Step 5–6 |
| Ranking | Step 7 |
| Top five + one recommendation | Step 8 |
| Contrast vs CR-Gap & Information-Access | Step 8 |

---

## Unresolved issues / next validation

1. Confirm with technical coauthors that **archive retention** is an independently controllable knob (bytes/tokens/entries) without silently changing retrieval.  
2. Freeze definitions of **current-task** vs **historical-task** labels in the synthetic world.  
3. Pre-register the Pareto decision rule (e.g. report both axes; claim is characterization, not “we win overall”).  
4. Optional: update `research-specification-v0.1.md` RQ section to S1 once coauthors approve — **not done in this task**.  
5. Literature gate should be re-run immediately before submission; agent-memory area moves quickly.

---

## Changed files

- `publications/03-iclr-long-term-knowledge-memory/planning/research-question-search.md` (created)

**Validation performed:** web literature scan (hierarchical memory ablations; forgetting/consolidation; graph necessity; conflict/STALE/MemConflict; retrieval-vs-write diagnostics; routing; archive/tier systems; bi-temporal Engram). No manuscript writing. No system redesign. No new topic search outside LTKM ingredients.
