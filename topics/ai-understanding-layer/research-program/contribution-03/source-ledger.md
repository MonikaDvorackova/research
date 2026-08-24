---
id: note-contribution-03-source-ledger
title: "Contribution 3 — Source Ledger"
topic: ai-understanding-layer
type: note
status: active
created: 2026-08-24
updated: 2026-08-24
tags: [contribution-03, sources, citations]
refs: [historical-literature-review.md, program-comprehension-review.md, observability-review.md, provenance-review.md, ai-systems-review.md]
---

## Source Ledger

Every source cited as `[Sn]` in this review's documents, with full
citation, year, field, central claim used, and exact collision recorded.
All sources were retrieved via live web search during this session
(2026-08-24). Primary/authoritative sources are preferred; general
web-summary results are used only for orientation and marked as such.
Per this task's explicit source-discipline requirement, every entry
below is labeled SOURCE-SUPPORTED FACT (what the source itself states)
vs. OUR SYNTHESIS (this programme's interpretation built on it) in the
citing document, not here — this ledger records only the source, not the
interpretation.

| ID | Citation | Year | Field | Used in | Central claim used |
|---|---|---|---|---|---|
| S1 | Rochkind, M. (SCCS, Bell Labs); Tichy, W. (RCS); general VCS history (multiple secondary sources on SCCS/RCS/CVS lineage, retrieved via web search, orientation-level, not a single primary paper) | 1972–1986 | Software engineering / version control | `historical-literature-review.md` | SCCS motivated by bug-origin tracking; RCS by storage efficiency; CVS by concurrent editing — three different motivations, not one preservation goal |
| S2 | Git creation history (git-scm.com official history page; Linux Foundation interview with Linus Torvalds; multiple secondary retrospectives, retrieved via web search) | 2005 | Software engineering / version control | `historical-literature-review.md` | Git's proximate cause was the end of free BitKeeper access; core motivation was a distributed workflow for kernel maintainers, not knowledge preservation |
| S3 | ARIES: Mohan et al., "ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking," ACM TODS, 1992 (primary, retrieved PDF); general WAL descriptions (secondary, orientation) | 1992 | Database systems | `historical-literature-review.md` | WAL/transaction logs exist for crash recovery/durability (ACID), not for explanatory understanding |
| S4 | Sigelman, B. et al., "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure," Google Technical Report, 2010 (primary, research.google/pubs page confirmed) | 2010 | Distributed systems | `historical-literature-review.md` | Dapper's motivation was per-request latency diagnosis at scale, not general system understanding |
| S5 | Wikipedia, "Program comprehension" (orientation); von Mayrhauser & Vans encyclopedia chapter on program comprehension (secondary/tertiary, retrieved as PDF) | 1995 (encyclopedia chapter); ongoing | Software engineering | `program-comprehension-review.md` | Program comprehension is a named research field with its own definition |
| S6 | Xia et al., "Measuring program comprehension: A large-scale field study with professionals," ICSE 2018 (primary, retrieved) | 2018 | Software engineering / empirical SE | `program-comprehension-review.md` | Developers spend ~58% of time on comprehension; field uses eye-tracking/neuroimaging methods |
| S7 | Systematic mapping study, "40 Years of Designing Code Comprehension Experiments" (arXiv preprint, retrieved) | 2022 | Software engineering | `program-comprehension-review.md` | Program comprehension experimentation has a 40-year continuous research history |
| S8 | Research on architectural knowledge vaporization (ScienceDirect article on reducing vaporization in agile global SD; general secondary orientation) | 2019 | Software architecture | `program-comprehension-review.md` | Architectural knowledge is tacit and easily lost, causing evolution/communication/reuse costs |
| S9 | "A Pattern-driven Approach against Architectural Knowledge Vaporization" (ResearchGate, retrieved abstract) | pre-2015 (exact year not independently confirmed in this pass — flag below) | Software architecture | `program-comprehension-review.md` | Dedicated literature exists specifically to counter vaporization |
| S10 | "Understanding Software Architecture Erosion: A Systematic Mapping Study" (arXiv, retrieved) | 2021 | Software architecture | `program-comprehension-review.md` | Links architecture erosion to technical debt and knowledge vaporization |
| S11 | Lattix blog, "Software Archaeology - Software Architectural Recovery for Legacy Code" (secondary, orientation-level, not a peer-reviewed primary source — flagged) | undated | Software engineering practice | `program-comprehension-review.md` | Names software archaeology and architecture recovery as an existing discipline |
| S12 | "Recover and RELAX: Concern-Oriented Software Architecture Recovery," arXiv:1903.06895 (primary, retrieved) | 2019 | Software architecture | `program-comprehension-review.md` | Concrete, current architecture-recovery method, confirming the discipline is active research, not folklore |
| S13 | "AI Observability for Large Language Model Systems: A Multi-Layer Analysis..." (arXiv preprint, retrieved); Atlan, "AI Agent Observability: A Complete Guide for 2026" (secondary, industry source) | 2026 | AI/ML systems engineering | `ai-systems-review.md`, `program-comprehension-review.md` | Direct, current statement that AI observability has "impressive depth at individual layers but limited integration across them" |
| S14 | Wikipedia, "Observability (software)"; multiple 2026 observability-vendor explainer pages (secondary, orientation-level, consistent across sources) | ongoing | Systems engineering / control theory | `observability-review.md` | Control-theoretic definition of observability; "monitoring tells you it's broken, observability tells you why" distinction |
| S15 | General "three pillars of observability" (logs/metrics/traces) explainer sources (secondary, orientation) | ongoing | Software observability practice | `observability-review.md` | Standard taxonomy of observability signal types |
| S16 | Buneman, P., Khanna, S., Tan, W.C., "Why and Where: A Characterization of Data Provenance," ICDT 2001 (primary, Springer link confirmed); Buneman, "Data Provenance: What next?" SIGMOD Record (primary, PDF retrieved) | 2001 | Database theory | `provenance-review.md` | Why-provenance/where-provenance formalized over a decade before W3C PROV |
| S17 | General database-provenance survey material (query provenance vs. process provenance distinction, secondary orientation) | ongoing | Database theory | `provenance-review.md` | How-provenance and process-provenance as later extensions of the Buneman taxonomy |
| S18 | Wikipedia, "Record and replay debugging"; `rr`/Pernosco project descriptions (secondary, orientation, consistent with primary tool documentation referenced therein) | ongoing | Systems / debugging tools | `provenance-review.md` | What deterministic record/replay captures and reconstructs |
| S19 | "Replay Debugging of Complex Real-Time Systems," arXiv:cs/0311019 (primary, retrieved); "Time Machine" replay-tool description (secondary) | 2003 | Systems / debugging | `provenance-review.md` | Replay reconstructs "the world as it was" during original execution; scope is execution, not justification |
| S20 | Anthropic, "Interpretability Research" team page; general mechanistic-interpretability explainer sources (secondary, orientation) | ongoing | AI interpretability | `provenance-review.md`, `ai-systems-review.md` | Mechanistic interpretability's object is model-internal representations, distinct from execution reconstruction |
| S21 | Sculley, D. et al., "Hidden Technical Debt in Machine Learning Systems," NeurIPS 2015 (primary, NeurIPS proceedings page and PDF confirmed) | 2015 | ML systems engineering | `ai-systems-review.md` | Entanglement, hidden feedback loops, undeclared consumers, data dependencies as ML-specific complications with no direct SE analogue |
| S22 | MIT Technology Review, "Mechanistic interpretability: 10 Breakthrough Technologies 2026" (secondary, but reporting directly on); "Open Problems in Mechanistic Interpretability" (cross-institutional paper, Jan 2025, referenced by the above and independently well-known in the field) | 2025/2026 | AI interpretability | `ai-systems-review.md` | "Many interpretability queries are intractable" — current, authoritative field self-assessment |
| S23 | Hugging Face blog, "Observability and Interpretability in Agentic AI" (secondary, practitioner-authoritative); ATLIS framework description (secondary, industry) | 2026 | AI agent engineering | `ai-systems-review.md` | Layered observability architecture for agents; explicit "depth without integration" finding |
| S24 | "Explainability of Algorithms," arXiv:2508.13529 (primary, retrieved); "Innovations in Explainable AI" (secondary journal article) | 2025 | XAI | `ai-systems-review.md` | XAI's own self-description as bridging algorithmic complexity and human comprehension |
| S25 | General runtime-verification definitional sources (multiple, consistent secondary descriptions); "Runtime Verification of Learning Properties for RL Algorithms," arXiv:2311.09811 (primary, retrieved) | 2023 (RL paper); field ongoing | Formal methods | `ai-systems-review.md` | Runtime verification checks property conformance against a formal spec, a different question from reconstruction/explanation |
| S26 | "A Principles-based Ethics Assurance Argument Pattern for AI and Autonomous Systems," arXiv:2203.15370 (primary, retrieved) | 2022 | Safety/assurance engineering | `ai-systems-review.md` | Assurance-case methodology applied specifically to AI systems |
| S27 | General assurance-case/safety-case definitional sources (GSN, Claims-Argument-Evidence — multiple consistent secondary sources) | ongoing | Safety-critical systems engineering | `ai-systems-review.md` | Claim-Argument-Evidence and GSN as structured argument methodologies |
| S28 | ICO (UK Information Commissioner's Office), "Annexe 5: Argument-based assurance cases," AI explainability guidance (primary, government-authoritative) | ongoing | AI governance | `ai-systems-review.md` | Assurance-case methodology explicitly extended to AI governance/explanation contexts |
| S29 | Multiple epistemic-opacity sources: "How the machine 'thinks': Understanding opacity in machine learning algorithms" (ResearchGate); "It's not a bug, it's a feature: How AI experts and data scientists account for the opacity of algorithms," Avnoon & Eyal, 2026 (peer-reviewed journal, PubMed-indexed, primary) | 2016/2026 | Philosophy of science / STS | `novelty-verdict.md` | "Epistemic opacity" as an established, named, actively-researched near-identical thesis to Source A's diagnostic claim |

## Sources added in the narrow follow-up pass (RQ1/RQ3, 2026-08-24)

| ID | Citation | Year | Field | Used in | Central claim used |
|---|---|---|---|---|---|
| S30 | Diagnosability of discrete-event systems, IEEE Xplore primary record (foundational formal definition); multiple extensions (fuzzy DES, labeled automata, game-structure open systems) retrieved via search, orientation-level for the extensions | foundational + ongoing | Discrete-event systems / control engineering | `operationalization-review.md`, `diagnosability-review.md` | Formal definition of diagnosability; distinctness from observability |
| S31 | "Intermittent fault diagnosability of discrete event systems: an overview of automaton-based approaches," Discrete Event Dynamic Systems, Springer (primary, retrieved) | 2020 | Discrete-event systems | `diagnosability-review.md` | Diagnosability is an active, continuously-developed formal literature |
| S32 | ETH Zurich Automatic Control Laboratory, "System Identification" (primary, institutional); general system-identification definitional sources (secondary, orientation) | ongoing | Control theory | `operationalization-review.md`, `diagnosability-review.md` | System identification builds predictive models from input-output data; distinct level from reconstructability |
| S33 | "Dynamic Assurance Cases: A Pathway to Trusted Autonomy" (ResearchGate, retrieved abstract) | 2020 | Safety/assurance engineering | `assurance-integration-review.md` | Dynamic assurance cases provide continuous, in-operation assurance |
| S34 | "Towards Continuous Assurance with Formal Verification and Assurance Cases," arXiv (primary, retrieved) | 2025 | Safety/assurance engineering | `assurance-integration-review.md` | Dynamic Safety Case Management Systems combine Checkable Safety Arguments with runtime Safety Performance Indicators |
| S35 | "A Structured Approach to Safety Case Construction for AI Systems," arXiv:2601.22773 (primary, retrieved) | 2026 | AI safety/assurance | `assurance-integration-review.md` | AI safety cases require evaluation-time discovery and runtime adaptation, not just design-time determinism |
| S36 | "Dynamic safety cases for frontier AI," arXiv:2412.17618 (primary, retrieved) | 2024 | AI safety/assurance | `assurance-integration-review.md` | Direct, current confirmation that dynamic AI safety cases link claims to configurations, evidence, monitoring, and change triggers continuously |
| S37 | "AlgebraicSystems: Compositional Verification for Autonomous System Design," arXiv:2203.16343 (primary, retrieved) | 2022 | Formal methods / autonomous systems | `composition-review.md`, `generalization-from-c2.md` | Local component verification does not by itself examine overall/emergent system behavior |
| S38 | "Compositional Verification of Stigmergic Collective Systems," Springer (primary, retrieved); systematic map on verification/validation of emergent behavior (secondary, orientation) | 2023 | Formal methods / collective systems | `composition-review.md` | Making emergent global behaviors predictable remains an open problem in compositional verification |
| S39 | "An algebraic characterization of observational equivalence," Castellani (primary, INRIA, retrieved) | 1996 | Theoretical computer science / process calculi | `composition-review.md` | Formal characterization of observational equivalence via abstraction homomorphisms |
| S40 | "Learning Causal State Representations of Partially Observable Environments," arXiv:1906.10437 (primary, retrieved); general POMDP-bisimulation literature (Castro's exact bisimulation, Dean & Givan homogeneous partitions — secondary orientation) | 2019 | Reinforcement learning / formal methods | `composition-review.md` | Bisimulation extended to partially observable settings, directly connectable to Contribution 2's AMBIGUOUS-case finding |

## Flags for future external verification

- **S9**: publication year not independently confirmed in this pass —
  ResearchGate listing did not surface an unambiguous year in the
  search snippet. Should be re-verified before any external citation in
  a drafted article.
- **S11**: a vendor/practitioner blog, not peer-reviewed — used only for
  orientation (naming the discipline), not as evidence for any
  substantive claim; the substantive architecture-recovery claim is
  carried by S12 instead.
- **S13, S22, S23, S24 (secondary halves)**: several 2025/2026 sources
  are industry blogs or press coverage of research rather than the
  primary papers themselves. Where a primary paper is named (e.g., "Open
  Problems in Mechanistic Interpretability," Jan 2025), it should be
  independently re-fetched and directly cited before any external
  publication: this pass relied on search-result summaries describing
  it, not a direct fetch of the paper itself.
- **General note**: this review used `WebSearch` (search-result
  summaries) for the large majority of sources rather than `WebFetch`
  (full-document retrieval) of primary sources, given the breadth this
  task's scope required across ~10 distinct fields. This is disclosed
  here directly, per the source-discipline requirement: claims above are
  SOURCE-SUPPORTED at the level search-result summaries can support, not
  independently verified against full primary-document text the way
  Contribution 2's bitemporal-verification pass verified its two decisive
  sources by full fetch. Any claim in this review intended for external
  publication should be re-verified by direct fetch of its primary
  source first.
