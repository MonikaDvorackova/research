---
id: pub-03-final-citation-audit
title: "Final citation audit — WorldConsistMem neighboring benchmarks"
type: research-notes
status: audit-complete
created: 2026-08-04
updated: 2026-08-04
---

# Final citation audit

**Method:** Primary sources only (arXiv Atom API / abs pages; OpenReview forum IDs where reachable; official GitHub only for implementation facts). Search snippets and blogs were not used as evidence. Verified 2026-08-04.

**Citation style:** `authorYearShortTitle` in `references/bib/library.bib`.

---

## Neighboring benchmark records

### `wu2025longMemEval` — LongMemEval

| Field | Content |
|---|---|
| Verified source | arXiv:2410.10813 (title/authors via Atom); arXiv comment `ICLR 2025`; OpenReview forum `pZiyCaVuti` |
| Title | LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory |
| Authors | Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, Dong Yu |
| Year / venue | 2025 / ICLR (conference; also arXiv preprint lineage) |
| Benchmark object | Long-horizon chat memory abilities (IE, multi-session, temporal, updates, abstention) |
| Metrics | Primarily answer / ability Acc |
| Dependent bundles | No (primary) |
| Cross-query world constraints | No (primary) |
| Claim supported | LTM Acc suites primarily score per-query outcomes |
| Sections | §1, §2.1, §2.3, closest-work table |
| Confidence | **H** |
| Caveat | OpenReview HTML bot-walled at audit; venue corroborated by arXiv comment + established forum id |

### `wu2026longMemEvalV2` — LongMemEval-V2

| Field | Content |
|---|---|
| Verified source | arXiv:2605.12493 |
| Title | LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues |
| Authors | Di Wu, Zixiang Ji, Asmi Kawatkar, Bryan Kwan, Jia-Chen Gu, Nanyun Peng, Kai-Wei Chang |
| Year / venue | 2026 / **preprint** (no archival venue claimed in bib) |
| Benchmark object | Experienced-colleague Acc; dynamic tracking, workflows, premise awareness |
| Metrics | Acc (+ latency-oriented reporting in paper narrative) |
| Dependent bundles | No |
| Cross-query world constraints | No |
| Claim supported | Dynamic tracking ≠ joint world-answer \(\Phi\) |
| Sections | §1, §2.1, §2.2, §2.3, table |
| Confidence | **H** |
| Caveat | Preprint status may change; do not upgrade venue without primary confirmation |

### `hu2025memoryAgentBench` — MemoryAgentBench

| Field | Content |
|---|---|
| Verified source | arXiv:2507.05257 |
| Paper title | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions |
| Authors | Yuanzhe Hu, Yu Wang, Julian McAuley |
| Year / venue | 2025 / **preprint** |
| Benchmark object | MemoryAgentBench competencies (AR/TTL/LRU/selective forgetting, FactConsolidation) |
| Metrics | Competency / answer Acc |
| Dependent bundles | No |
| Cross-query world constraints | No |
| Claim supported | Competency Acc after edits ≠ world-bundle \(\Phi\) |
| Sections | §1, §2.1, §2.3, table |
| Confidence | **H** |
| Caveat | Bib uses paper title; note field records MemoryAgentBench as introduced framework |

### `tao2026memConflict` — MemConflict

| Field | Content |
|---|---|
| Verified source | arXiv:2605.20926 |
| Title | MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts |
| Authors | Zhen Tao, Jinxiang Zhao, Peng Liu, Dinghao Xi, Yanfang Chen, Wei Xu, Zhiyu Li |
| Year / venue | 2026 / **preprint** |
| Benchmark object | Memory conflicts (dynamic/static/conditional) |
| Metrics | Answer Acc + retrieval/ranking fitness |
| Dependent bundles | No |
| Cross-query world constraints | No as primary; Partial adjacency via correctness≠retrieval |
| Claim supported | Conflict fitness ≠ multi-query world consistency |
| Sections | §1, §2.3, table |
| Confidence | **H** |
| Caveat | Preprint |

### `xie2026dynamicMem` — DynamicMem

| Field | Content |
|---|---|
| Verified source | arXiv:2606.22877 |
| Title | DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings |
| Authors | Wenya Xie, Shengming Zhou, Zelin Li, Pouya Parsa, Shuang Zhou, Xinheng Ding, Chinmay Arvind, Guanchu Wang, Vladimir Braverman, Ali Payani, Yantao Zheng, Zirui Liu |
| Year / venue | 2026 / **preprint** |
| Benchmark object | Evolving user-profile memory; temporal checkpoints |
| Metrics | Checkpoint / personalized-service Acc |
| Dependent bundles | Partial (checkpoint probes), not WorldConsistMem bundles |
| Cross-query world constraints | No as primary |
| Claim supported | Evolving profile TCE ≠ multi-entity world \(\Phi\) |
| Sections | §1, §2.2, table |
| Confidence | **H** |
| Caveat | Preprint; “shared gold history” = profile ground truth (user-centric) |

### `wang2026evoMemBench` — EvoMemBench

| Field | Content |
|---|---|
| Verified source | arXiv:2605.18421 |
| Title | EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective |
| Authors | Yuyao Wang, Zhongjian Zhang, Mo Chi, Kaichi Yu, Yuhan Li, Miao Peng, Bing Tong, Chen Zhang, Yan Zhou, Jia Li |
| Year / venue | 2026 / **preprint** |
| Benchmark object | Self-evolving memory taxonomy (scope×content) |
| Metrics | Task Acc / success (+ efficiency narrative) |
| Dependent bundles | No |
| Cross-query world constraints | No |
| Claim supported | Mechanism taxonomy ≠ consistency suite |
| Sections | §1, §2.1, table |
| Confidence | **H** |
| Caveat | Preprint; temporal-transition cell conservative Partial/No |

### `hu2026everMemBench` — EverMemBench

| Field | Content |
|---|---|
| Verified source | arXiv:2602.01313 |
| **arXiv title** | Evaluating Long-Horizon Memory for Multi-Party Collaborative Dialogues |
| Authors | Chuanrui Hu, Tong Li, Xingze Gao, Hongda Chen, Yi Bai, Dannong Xu, Tianwei Lin, Xiaohong Li, Yunyun Han, Jian Pei, Yafeng Deng |
| Year / venue | 2026 / **preprint** |
| Benchmark object | EverMemBench: multi-party collaborative long-horizon memory QA |
| Metrics | Recall / awareness / profile Acc |
| Dependent bundles | No |
| Cross-query world constraints | No |
| Claim supported | Collaborative dialog Acc ≠ world \(\Phi\) |
| Sections | §1, §2.1, §2.2, table |
| Confidence | **H** |
| Caveat | Cite **arXiv title** in BibTeX; “EverMemBench” is the benchmark name in the abstract. Do not invent a distinct paper titled only EverMemBench. |

### `liu2026worldMemArena` — WorldMemArena

| Field | Content |
|---|---|
| Verified source | arXiv:2605.29341 |
| Title | WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction |
| Authors | Chengzhi Liu, Yuzhe Yang, Sophia Xiao Pu, Yepeng Liu, Lin Long, Yichen Guo, Nuo Chen, Zhaotian Weng, Elena Kochkina, Simerjot Kaur, Charese Smiley, Xiaomo Liu, James Zou, Sheng Liu, Yuheng Bu, Songyou Peng, Xin Eric Wang |
| Year / venue | 2026 / **preprint** |
| Benchmark object | Multimodal action–world agent memory lifecycle |
| Metrics | Lifecycle Acc / retrieval / faithfulness-style stage metrics |
| Dependent bundles | Partial adjacency |
| Cross-query world constraints | No as primary |
| Claim supported | Lifecycle Acc ≠ world-bundle \(\Phi\) |
| Sections | §1, §2.2, table |
| Confidence | **H** |
| Caveat | Preprint; BibTeX uses en-dash in Action--World for TeX; do not hard-code contested instance counts in prose |

### `salla2026crossQueryContradictions` — SetCons metrics paper

| Field | Content |
|---|---|
| Verified source | arXiv:2604.14525 (comment: accepted ICLR 2026 Workshop on Logical Reasoning of LLMs) |
| Title | Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning |
| Authors | Rohit Kumar Salla, Ramya Manasa Amancherla, Manoj Saravanan |
| Year / venue | 2026 / **workshop acceptance noted on arXiv**; still `@misc` with workshop note (not archival conference proceedings) |
| Benchmark object | Multi-query case-file logical consistency (390 instances in abstract) |
| Metrics | Case Satisfiability, Contradiction Density, Revision Cost, SetConsRate |
| Dependent bundles | Yes |
| Cross-query constraints | Yes (logical / set-level) |
| Claim supported | Acc–global coherence already separated outside memory eval |
| Sections | §1, §2.4, table |
| Confidence | **H** |
| Caveat | “SetCons” is a metric name, not the paper title. Do not invent `@setCons2026`. |

### `chaudhry2026logicVault` — LogicVault (+ LogicBench-Cross)

| Field | Content |
|---|---|
| Verified source | OpenReview forum `https://openreview.net/forum?id=3pkSTLDiHo` (URL retained; HTML bot-walled at audit); GitHub `Sarimsaljook/LogicVault` for LogicBench-Cross release fact |
| Title (as cited) | LogicVault: Persistent Symbolic Belief States for Cross-Query Logical Consistency in LLMs |
| Authors | Sarim Chaudhry |
| Year / venue | 2026 / **OpenReview / workshop-or-preprint**; **not** claimed as archival conference paper |
| Benchmark object | Cross-query logical consistency; LogicBench-Cross released with project |
| Metrics | Logical / SMT consistency over belief states |
| Dependent bundles | Yes |
| Cross-query constraints | Yes |
| Claim supported | Adjacent non-memory Acc–consistency work; LogicBench-Cross is not a separate paper |
| Sections | §1, §2.4, table |
| Confidence | **M** (title/author/URL from prior primary audit + GitHub; OpenReview HTML not re-fetched this pass) |
| Caveat | **No separate BibTeX for LogicBench-Cross.** Cite via LogicVault. Do not invent arXiv id. Venue string must stay non-archival until proceedings confirmation. |

---

## Not cited as established separate works

| Candidate | Action | Reason |
|---|---|---|
| LogicBench-Cross as standalone paper | **Do not add separate entry** | Released with LogicVault; cite `@chaudhry2026logicVault` |
| Alternate EverMemBench title-only entry | **Not added** | Official arXiv title differs; use `hu2026everMemBench` + note |
| Unverified blog/secondary “memory consistency” lists | **Excluded** | Not primary sources |

---

## Keys added to `references/bib/library.bib`

`wu2025longMemEval`, `wu2026longMemEvalV2`, `hu2025memoryAgentBench`, `tao2026memConflict`, `xie2026dynamicMem`, `wang2026evoMemBench`, `hu2026everMemBench`, `liu2026worldMemArena`, `salla2026crossQueryContradictions`, `chaudhry2026logicVault`.

No duplicate keys found prior to append.
