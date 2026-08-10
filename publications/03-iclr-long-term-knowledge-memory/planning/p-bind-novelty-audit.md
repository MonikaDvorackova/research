---
id: pub-03-pbind-novelty-audit
title: "P-Bind novelty audit"
type: research-notes
status: provisional
created: 2026-08-01
updated: 2026-08-01
---

# P-Bind novelty audit

**Object under audit:** entity–attribute binding accuracy under semantically competitive retrieved context, **conditional on gold evidence being present**.  
**Question:** Has prior work already isolated gold-present binding swaps as a dose–response of semantic competition?

**Verdict: PARTIALLY OPEN** (not OCCUPIED under the strict occupation criterion).

---

## Occupation criterion (frozen)

**OCCUPIED** only if prior work already isolates **gold-present** entity/attribute **swap** errors as a function of **controlled semantic competition**, with Recall@k (or gold-in-context) held, and reports a dose–response (or equivalent factorial) of overlap → swap rate.

Cosmetic renaming of “distractors hurt” or “lost in the middle” does **not** count as occupation of P-Bind.

---

## Closest-work matrix

| Paper | Task | Gold guaranteed present? | Overlap continuous IV? | Entity/attr swap labeled? | Recall@k held? | Context length matched? | Dose–response of overlap→swap? | Models / data | Principal result | Residual for P-Bind |
|---|---|---|---|---|---|---|---|---|---|---|
| **Feng & Steinhardt, ICLR 2024** (*How do LMs Bind Entities in Context?*) | In-context entity–attribute binding; Binding ID interventions | Context constructed with bindings; not RAG gold-rank control | No (mech. interventions) | Causal swap via activation patching, not behavioral error taxonomy under distractors | N/A (full context) | Small controlled lists | No | LLaMA etc.; synthetic binding | LMs use abstract Binding IDs | **Mechanism ≠** behavioral dose–response under competitive multi-item retrieval |
| **Feng et al., EMNLP 2024** (*Representational Analysis of Binding*) | Ordering ID / Binding ID | Same family | No | Causal OI edits induce binding swaps | N/A | Controlled | No | Multiple LMs | OI subspace causally affects binding | Interpretability; not overlap IV |
| **Mixing Mechanisms (arXiv:2510.06182)** | Retrieve bound entities in-context | Bindings in context | No (list length / position) | Studies retrieval mechanisms, not swap taxonomy under competitors | N/A | Varies with list length | No | 9 models, 10 binding tasks | Positional+lexical+reflexive mix; middle noise | Position/mechanism; not semantic-overlap dose–response |
| **Liu et al., TACL 2024** (*Lost in the Middle*) | Multi-doc QA; key-value | Relevant doc in context | No (position IV) | No swap taxonomy | Relevant present | Length grows with #docs | No | GPT-3.5, Claude, … | U-shaped position effect | **Position ≠ binding**; P-Bind must match length & position |
| **MINTEval (arXiv:2605.18565)** | Long-horizon memory under interference | No (retrieval systems evaluated) | No continuous ρ | No dedicated entity/attr swap labels | No | Very long contexts | No | 7 systems; 15.6k QA | Low accuracy under interference; retrieval/construction limited | Interference accuracy, not gold-present binding law |
| **AIM / Associative Interference (OpenReview NFAM 2026)** | Lifelong interference under domain shift | No | Domain-shift / load | Interference concentration, not attr swaps | No | Varies | Partial (load) | Streaming experiments | Interference concentrated; pattern separation helps | Different object (domain-shift interference) |
| **RECON (arXiv:2607.16716)** | Compositional reasoning after change | Oracle graph upper bound studied | No ρ | Cascade/invalidation tasks; not attr-swap taxonomy | Separates retrieval vs reasoning failures | Long case files | No | Many architectures | ~4/5 failures persist when retrieval succeeds | **Post-retrieval gap** supports need for P-Bind; does not isolate binding×ρ |
| **MemConflict (arXiv:2605.20926)** | Memory conflicts | White/black-box | Conflict types | Conflict fitness, not binding swaps | Analyzes retrieval | Controlled sims | No | 6 memory systems | Answer vs retrieval diverge | Conflict ≠ binding under gold present |
| **STALE (arXiv:2605.06527)** | Stale / implicit conflict | Updated evidence may be present | No | State resolution / premise resistance | No | Up to 150k | No | Frontier + memory systems | Retrieve≠act | Staleness, not competitive binding |
| **Diagnosing Retrieval vs Utilization (arXiv:2603.02473)** | Write×retrieve on LoCoMo | No | No | Failures attributed to retrieval stage mostly | Varies by method | Varies | No | 3×3 study | Retrieval dominates write | When retrieval solved, residual utilization underexplored — P-Bind targets that residual |
| **Faithfulness-QA (arXiv:2604.25313)** | Context vs parametric; entity substitution | Substituted entity in context | Type-consistent substitute | Conflict faithfulness training | N/A | Matched construction | No | SQuAD/TriviaQA derived | Train context faithfulness | Knowledge conflict, not co-retrieved competitor binding |
| **RAG knowledge-conflict / Entity Swap diagnostics (e.g. CDD, arXiv:2605.14473)** | Compliance under wrong retrieval / conflict | Often adversarial *wrong* context | Perturbation families | “Entity Swap” = swap in *source* to create conflict | Often assumes retrieved set | Controlled records | No | Gemini etc. | Robustness to conflicting retrieval | Tests **wrong evidence**, not gold+competitors binding |
| **MEME (arXiv:2605.12477)** | Multi-entity evolving memory | No | No | Cascade/absence | No | Episodic | No | Graphiti/Mem0/… | Dependency/cascade hard | Evolution/cascade ≠ binding×ρ |
| **LongMemEval / LoCoMo** | Conversational memory QA | No | No | Category scores | No | Long | No | Standard benches | Temporal/multi-hop hard | No binding taxonomy |
| **Multi-attribute confounding (arXiv:2511.04053)** | Numerical attribute entanglement | Attributes in prompt | Irrelevant numerical context | Representational confounding | N/A | Short | No | Size sweep | Shared subspaces; perturbation | Numerical confounding ≠ entity–attribute swap under retrieval competition |

---

## Single paper most likely to occupy P-Bind

**Feng & Steinhardt (ICLR 2024), *How do Language Models Bind Entities in Context?*** (Binding ID), together with follow-on binding/OI papers and *Mixing Mechanisms*.

**Why closest:** they literally study entity–attribute binding and can *induce* swaps.  
**Why not occupation under frozen criterion:** they do **not** treat gold-present RAG/memory contexts with a controlled continuous semantic-overlap IV, matched length/position, fixed Recall@k, and a behavioral dose–response of **swap error rate**. They are mechanistic accounts of binding skill, not the P-Bind error characterization.

**Second threat:** *Lost in the Middle* — will be used by reviewers to dismiss P-Bind unless position and length are locked.

**Third threat:** RECON / MINTEval — “post-retrieval / interference already known.” Must answer: *known that failures exist; unknown whether they are binding swaps scaling with ρ under gold-present.*

---

## Classification

| Label | Decision |
|---|---|
| OPEN | No — neighborhood too dense |
| **PARTIALLY OPEN** | **Yes** — residual is specific: gold-present · swap-labeled · ρ dose–response · matched length/position/Recall |
| OCCUPIED | **No** — no paper meets the strict occupation criterion |

**Implication:** Novelty is **conditional**. Continuation is justified only if the kill pilot shows the residual is real (swap↑ with ρ, not just accuracy↓ or position effects). If the pilot only rediscovers LitM or generic distractor hurt, treat as **effectively occupied** and stop.

---

## Exact residual left for P-Bind

> Under **fixed gold-in-context**, **fixed top‑k**, **matched token length**, and **controlled gold position**, does the rate of **entity/attribute binding swaps** (not omissions) increase as a **dose–response of a symbolic overlap variable ρ**, across ≥2 model families?

That residual is the only novelty claim allowed in planning docs.
