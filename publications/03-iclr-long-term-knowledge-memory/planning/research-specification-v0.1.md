---
id: pub-03-ltkm-research-specification-v0.1
title: "Research Specification v0.1 — Publication 03 (S1 archive Pareto)"
type: research-notes
status: draft
version: 0.1.1-s1
created: 2026-07-31
updated: 2026-07-31
approval: pending-team-review
tags: [iclr, publication-03, research-specification, archive-pareto, s1]
---

# Research Specification v0.1.1 (S1 adopted)

**Purpose:** Scientific contract for Publication 03.  
**Change in this revision:** Provisional primary RQ frozen to **S1 (archive Pareto)** from [`research-question-search.md`](research-question-search.md). Architecture is **platform**, not claim.  
**Rule:** Unsupported empirical claims remain unmarked as results. `TODO(collab):` only where implementation ownership or venue logistics remain open.  
**Pilot:** [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md)  
**RQ spine:** [`research-question.md`](research-question.md)

**Manuscript drafting authorization:** **Not granted.** Pilot go/no-go required first.

---

## 1. Problem Statement

### 1.1 Scientific problem

Long-horizon LLM agents must answer both **current-state** and **historical-state** questions about an **evolving world**. Under a **fixed total memory budget**, retaining superseded knowledge for historical queries competes with capacity used for knowledge optimized for current use. The scientific problem is to characterize this **resource-allocation trade-off**, not to propose a new memory taxonomy.

### 1.2 Why existing work is insufficient (positioning, not proven gap)

Prior agent-memory work studies hierarchy, forgetting, conflict, routing, and cost/accuracy trade-offs, but does not cleanly answer:

> Under fixed \(B\), how does archive allocation \(\alpha\) move systems on the **current–historical accuracy Pareto**, and in which regimes is archive retention useful, costly, or unnecessary?

This positioning is a **hypothesis about the literature gap**. It must be sharpened with must-cite lists before Related Work prose.  
`TODO(collab):` Confirm closest papers (Engram bitemporal, MemConflict, STALE, FadeMem, MemoryData, Letta/MemGPT archive tiers) and refine the gap sentence.

### 1.3 Why this is an ML / agent-learning evaluation problem

The object is a **constrained allocation policy** \(\alpha\) and its effect on two competing accuracy objectives under controlled world dynamics. That is an empirical characterization problem suitable for ICLR-style agent/memory evaluation—not a systems description of five stores.

Engineering alone (implementing LTKM) is **not** the contribution.

---

## 2. Research Question

### 2.1 Adopted primary RQ (S1) — provisional freeze

> **Under a fixed total memory budget, how does archive retention of superseded knowledge trade off current-state accuracy against historical-state accuracy in an evolving world?**

| Criterion | Status |
|---|---|
| Falsifiable | Yes — see §3 and §9 |
| Experimentally answerable | Yes — via \(\alpha\) sweep under fixed \(B\) |
| Architecture as claim? | **No** — LTKM is platform |
| Suitable for ICLR | Conditionally yes if Pareto/regime results are nontrivial and survive fair controls |

### 2.2 Retired competing RQs

| ID | Question | Status |
|---|---|---|
| RQ-A (outline) | Does hierarchical LTKM beat existing agent memory on consistency? | **Retired** as primary (architecture-as-claim; occupied) |
| RQ-B–D | Lifecycle / benchmark / organization variants | Secondary only if S1 passes |
| CR-Gap | Overwrite vs revision reconstruction | **Excluded** — closed cycle; do not import claims |
| Information-Access | Multi-turn vs single-shot dissociation | **Excluded** — occupied; not this paper |

### 2.3 Secondary questions (post-pilot only)

- Does LTKM’s frontier differ from a flat temporal store under the same \(B\)? (architecture demoted if no)  
- Does frontier shape depend on world-change rate, historical-query proportion, horizon, revision frequency, retrieval budget \(k\)?  
- Is any intermediate \(\alpha\) optimal for a given task-weighted utility \(U_\lambda\)? (**not assumed**)

---

## 3. Scientific Hypothesis

### 3.1 Definitions used in H0/H1

Let \(A_c(\alpha; B, \mathcal{W}, k)\) = current-state accuracy and \(A_h(\alpha; B, \mathcal{W}, k)\) = historical-state accuracy under archive ratio \(\alpha\), total budget \(B\), world regime \(\mathcal{W}\), retrieval budget \(k\).

A **nontrivial Pareto frontier** means: as \(\alpha\) varies over a fixed grid, the set of points \(\{(A_c, A_h)\}\) is not reducible to (i) a single dominating allocation, (ii) a flat cloud within noise, or (iii) a trivial monotone map of retained superseded-record count alone.

### 3.2 Primary hypotheses

**H0 (null):** Under the pilot/main protocol, varying \(\alpha \in \{0, 0.25, 0.5, 0.75\}\) (and extended grids in the main study) at fixed \(B\) and matched \(k\) does **not** produce a nontrivial current–historical Pareto. In particular, at least one of:

- \(\max_\alpha |A_c(\alpha)-A_c(\alpha')| < \tau_c\) and \(\max_\alpha |A_h(\alpha)-A_h(\alpha')| < \tau_h\) (no material movement); or  
- one \(\alpha^\star\) weakly dominates all others on both axes in all tested regimes; or  
- the frontier collapses to the flat temporal baseline within \(\tau_{\mathrm{flat}}\) on both axes; or  
- \(A_h\) is explained by retained superseded-record count with \(R^2 \ge 0.95\) and residual trade-off on \(A_c\) within noise.

**H1 (alternative):** Varying \(\alpha\) at fixed \(B\) induces a nontrivial Pareto frontier between \(A_c\) and \(A_h\). Directional expectations (falsifiable, **not assumed as necessary**):

- low \(\alpha\) tends to favor \(A_c\) and harm \(A_h\);  
- high \(\alpha\) tends to favor \(A_h\) and harm \(A_c\);  
- an intermediate \(\alpha\) **may** maximize \(U_\lambda = \lambda A_c + (1-\lambda)A_h\) for some \(\lambda\) and regimes—but **existence of an interior optimum is not part of H1**; H1 only requires a nontrivial frontier / regime-dependent trade-off.

**Pilot thresholds (pre-registered):**  
\(\tau_c = 0.05\) absolute accuracy; \(\tau_h = 0.05\); \(\tau_{\mathrm{flat}} = 0.03\) mean absolute difference vs best flat-temporal point at same \(B\); material trade-off requires **both** \(\mathrm{range}(A_c) \ge \tau_c\) **and** \(\mathrm{range}(A_h) \ge \tau_h\) across \(\alpha\), **or** a clear negative association (Spearman \(\rho(A_c,A_h) \le -0.3\) across \(\alpha\) points with both ranges \(\ge 0.03\)).

### 3.3 What rejects H1

See §9.2 and pilot go/no-go. Summarily: no material \(\alpha\) effect; universal dominance of one \(\alpha\); flat temporal matches/dominates; matched-\(k\) / matched-\(B\) eliminates effect; effect is pure record-count; accounting artifacts (unequal uncounted capacity or unequal representation cost).

---

## 4. Scientific Contribution

| Type | Intended content | Status |
|---|---|---|
| **Conceptual** | Fixed-budget current vs historical objectives; archive allocation as resource problem; regime interpretation | Framing ready; prose after pilot |
| **Methodological** | Protocol for Pareto measurement under \(\alpha\) with fair \(B\) and \(k\) | Specified in pilot protocol |
| **Engineering** | LTKM platform + world generator as controls | Platform only; not the claim |
| **Experimental** | Empirical Pareto / regime map | **Pending pilot** |

**Indispensable contribution:** empirical characterization of the current–historical accuracy trade-off under archive allocation. Without a nontrivial frontier or a clearly reported negative (H0), there is no S1 paper.

**Provisional contribution wording (conservative):**

- The paper studies archive allocation as a **constrained resource-allocation problem**.  
- It characterizes the trade-off between maintaining current knowledge and retaining superseded knowledge.  
- It identifies regimes in which archive retention is beneficial, costly, or unnecessary.  
- LTKM supplies experimental controls; **it is not itself the result**.

---

## 5. Scientific Object

### 5.1 Primary object (frozen for S1)

**Memory-budget allocation between knowledge optimized for current use and retained superseded knowledge required for historical queries.**

Formally: the map \(\alpha \mapsto (A_c(\alpha), A_h(\alpha))\) under \(B_c + B_a = B\), \(\alpha = B_a/B\).

### 5.2 Non-objects (do not elevate to primary claim)

- superiority of hierarchy;  
- necessity of archives in general;  
- novelty of five-layer taxonomy;  
- learned routing/controllers (out of pilot scope);  
- reconstruction faithfulness / CR-Gap overwrite debates.

---

## 6. Proposed Method (platform specification)

### 6.1 Role of hierarchical LTKM

Provides separable **active/current store** and **archive store** with measurable capacities \(B_c\), \(B_a\), deterministic write/eviction/promotion for the pilot, and retrieval with budget \(k\).

Working/session/long-term/graph layers may exist in the full system; for S1 pilots they may be **collapsed** into “active” vs “archive” as long as capacity accounting remains faithful. Do not redesign the architecture; **simplify controls** for measurement.

### 6.2 Fixed-budget formalism

| Symbol | Definition |
|---|---|
| \(B\) | Total memory budget (primary normalized units) |
| \(B_c\) | Active/current allocation |
| \(B_a\) | Archive allocation |
| Constraint | \(B_c + B_a = B\) (hard; no uncounted overflow) |
| \(\alpha\) | Archive ratio \(B_a / B\) |
| \(Z_0,\ldots,Z_T\) | World states over discrete time |
| Superseded knowledge | Facts true at some \(t' < t\) but false or replaced in \(Z_t\) |
| Current-state query | Gold answer determined by \(Z_t\) (or query time \(t_q\)) |
| Historical-state query | Gold answer determined by \(Z_{t^\star}\) for specified \(t^\star < t_q\) (or “as of” / “before update”) |
| Retention policy | Which superseded items enter/stay in archive when \(B_a\) binds |
| Eviction policy | What leaves active or archive when capacity binds |
| Retrieval policy | How top-\(k\) evidence is selected from allowed stores |

### 6.3 What counts toward \(B\)

**Must be counted if stored or required for retrieval:**

- raw tokens / text of memory entries;  
- chunks;  
- triples / structured facts;  
- embeddings (if stored);  
- summaries;  
- metadata required for correctness (timestamps, validity intervals);  
- index overhead that scales with retained entries (approximate if needed; document formula).

**Primary normalized unit for the pilot:** **structured fact slots** (one slot = one dated atomic assertion: entity, attribute, value, `valid_from`, `valid_to` or superseded flag).

**Rationale:** deterministic, comparable across baselines, avoids tokenizer variance.  
**Limitations:** ignores embedding bytes and graph-index asymmetry; if a baseline needs embeddings, charge **1 slot-equivalent per indexed fact** plus document any extra vector store cost as secondary. No method may receive extra uncounted archive capacity.

`TODO(collab):` If implementation uses embeddings-only stores, re-express \(B\) in bytes with a published conversion; pilot still forbids uncounted capacity.

### 6.4 Pilot method constraints

- Deterministic eviction/promotion (no learned controller).  
- Same total \(B\) for every \(\alpha\) and baseline.  
- Same retrieval budget \(k\).  
- Symbolic or extractive reader first (no large downloads unless required).

---

## 7. Benchmark

### 7.1 Minimal evolving world (S1)

Entities with attributes/relations; initial facts; updates; supersession; temporary changes; reversions; unrelated changes; paired **current** and **historical** queries. Gold states generated **deterministically** from the simulator.

**Independent axes:** world-change rate; number of entities; revisions per fact; proportion of historical queries; query horizon; total memory budget \(B\).

Full generator spec: [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md) §5.

### 7.2 Task families for S1 primary analysis

**Primary:** current-state; historical-state (including by horizon).  
**Secondary / deferred:** conflicting, multi-hop, temporal-as-ordering — may be retained for platform compatibility but **must not** redefine the primary Pareto axes.

### 7.3 CR-Gap exclusion

Do not reuse CR-Gap claims (overwrite vs revision-aware reconstruction). Reuse simulator code only with explicit documentation of what was adapted.

---

## 8. Experimental Plan

### 8.1 Archive-allocation dial

Example grid: \(\alpha \in \{0, 0.10, 0.25, 0.50, 0.75, 0.90, 1.0\}\).  
Pilot minimum: \(\{0, 0.25, 0.50, 0.75\}\) at ≥3 values of \(B\).

At ratio \(\alpha\): \(B_a = \lfloor \alpha B \rfloor\), \(B_c = B - B_a\). Active store **never** exceeds \(B_c\); archive **never** exceeds \(B_a\).

### 8.2 Baseline matrix (minimum)

| ID | Baseline | Role |
|---|---|---|
| B0 | No archive / current-only (\(\alpha=0\)) | Lower archive extreme |
| B1 | Archive-all / minimal active (\(\alpha\to 1\)) | Upper archive extreme |
| B2 | Fixed-ratio LTKM (\(\alpha\) grid) | Primary sweep |
| B3 | Flat temporal keep-all under same \(B\) | **Indispensable**; demotes architecture if matches frontier |
| B4 | Recency-based eviction (single store) | Trivial policy control |
| B5 | Reservoir / random retention | Non-intelligent retention control |
| B6 | Oracle allocation (if feasible) | Upper bound |

Per-baseline write/eviction/supersession/retrieval specs: pilot protocol §7.

### 8.3 Metrics

**Primary (always report separately):**

- \(A_c\) current-state accuracy;  
- \(A_h\) historical-state accuracy;  
- \(A_h\) by query horizon;  
- empirical Pareto set \(\{(A_c(\alpha), A_h(\alpha))\}_\alpha\).

**Secondary:** hypervolume / area under frontier (summary only); memory utilization; retrieval cost; storage cost; \(U_\lambda\) across multiple \(\lambda\) (never one arbitrary \(\lambda\) as headline).

### 8.4 Indispensable analyses

Frontier vs: world-change rate; historical-query proportion; query horizon; \(B\); revision frequency; \(k\).  
Check: monotonic curves; non-monotonic optima; crossing frontiers; dominance; sensitivity to retention policy.

---

## 9. Success Criteria

### 9.1 Continue (go)

Continue toward main experiments / manuscript framing only if:

1. Archive allocation creates a reproducible trade-off of meaningful magnitude (\(\mathrm{range}(A_c)\ge \tau_c\) and \(\mathrm{range}(A_h)\ge \tau_h\), or Spearman criterion in §3.2).  
2. No single \(\alpha\) dominates on both axes in all tested regimes.  
3. Frontier shape changes predictably with ≥1 of {change rate, historical proportion, horizon}.  
4. Effect survives matched \(B\) and matched \(k\).  
5. LTKM (or \(\alpha\)-sweep) reveals ≥1 regime not explained by recency-only (B4) within \(\tau_{\mathrm{flat}}\).  
6. Results reproduce across ≥2 seeds (pilot: seeds 42 and 43; sign of trade-off agrees).

### 9.2 Stop or reframe (no-go)

Stop S1 or reframe if:

1. One allocation dominates everywhere.  
2. Frontier explained entirely by count of retained facts (\(R^2\ge 0.95\) and no residual \(A_c\) cost beyond \(\tau_c\)).  
3. Flat temporal (B3) matches or dominates LTKM frontier (mean \(|\Delta| \le \tau_{\mathrm{flat}}\) on both axes at each \(B\), or B3 Pareto-dominates).  
4. \(A_c\) insensitive to reduced \(B_c\) (\(\mathrm{range}(A_c)<\tau_c\)).  
5. \(A_h\) rises with \(\alpha\) with no meaningful \(A_c\) cost (\(\mathrm{range}(A_c)<\tau_c\) while \(\mathrm{range}(A_h)\ge \tau_h\)).  
6. Results flip under alternate legitimate budget accounting (slots vs tokens) beyond \(\tau_c,\tau_h\).

**Paper-level policy if H0:** report negative characterization (still potentially valuable) **or** return to next surviving RQ from research-question search (S2/S4)—team decision. Do not silently revert to RQ-A architecture claim.

---

## 10. Threats to Validity

| Risk | Mitigation |
|---|---|
| Architecture-as-claim creep | Contribution wording forbids hierarchy superiority claims |
| Uncounted capacity | Hard \(B_c+B_a=B\); audit logging of slot counts |
| Representation-cost confound | Same entry schema across \(\alpha\); forbid richer archive encoding |
| Trivial record-count explanation | Partial out superseded-count; compare to B5 random |
| Flat store sufficiency | Mandatory B3 |
| Reader confounds | Symbolic/extractive reader first; freeze reader across conditions |
| CR-Gap contamination | Explicit exclusion; no reconstruction metrics as primary |
| Synthetic-world narrowness | Regime axes; later transfer checks optional |
| Novelty risk | Pareto/regime claim vs “yet another hierarchical memory” |

**Largest novelty risk:** nearby bitemporal / staleness / cost-accuracy papers; must emphasize **fixed-\(B\) current–historical Pareto under \(\alpha\)**, not “we keep history.”  
**Largest validity risk:** budget accounting and flat-baseline fairness.

---

## 11. Open Questions

### Research (mostly resolved for S1 framing)

- [x] Primary RQ = S1  
- [x] Scientific object = budget allocation current vs superseded  
- [x] H0/H1 + pilot thresholds  
- [ ] Team sign-off on thresholds \(\tau_\ast\)  
- [ ] Must-cite gap paragraph  

### Implementation

`TODO(collab):` Code location for pilot; whether any LTKM components already exist.  
`TODO(collab):` Confirm fact-slot accounting vs need for byte accounting.  
`TODO(collab):` Feasibility of oracle baseline B6.

### Infrastructure

`TODO(collab):` ICLR year/deadline; authors; Overleaf/Zotero SOT.

---

## 12. Responsibility Matrix

| Item | Monika | Technical collaborators | Shared |
|---|---|---|---|
| RQ / object / H0/H1 / claim discipline | **Own** | Review | Freeze |
| Literature positioning / Intro–Discussion after go | **Own** | Supply closest systems | Align |
| Pareto regime interpretation | **Own** | Supply plots/tables | Align |
| World generator, stores, baselines, runs, stats | Review protocol | **Own** | Protocol freeze |
| Pilot go/no-go decision | Advise | Produce evidence | **Decide** |
| Manuscript drafting | Blocked until go | Blocked until go | Unlock |

---

## 13. Readiness Assessment

| Area | Readiness | Explanation |
|---|--:|---|
| Scientific object / RQ / H0/H1 | **85%** | S1 frozen provisionally; thresholds set; team sign-off pending |
| Pilot protocol | **80%** | Specified in companion doc; not implemented |
| Method (full LTKM) | **25%** | Platform may be simplified to active vs archive for pilot |
| Benchmark | **40%** | Spec exists; code does not |
| Experiments | **10%** | Plan ready; no runs |
| Results | **0%** | — |
| Manuscript | **0%** | Not authorized |

**Overall for implementation start:** **Ready for pilot implementation** under [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md).  
**Not ready** for manuscript drafting or full-system redesign.

---

## 14. Critical Path

1. Team acknowledge S1 + thresholds.  
2. Implement archive Pareto **kill pilot** (protocol).  
3. Apply go/no-go (§9).  
4. If go: expand regime map + baselines; then Spec v0.2.  
5. If no-go: reframe to next survivor (S2/S4) or report negative.  
6. **Only after go:** conceptual manuscript sections (Monika) + full methods (collabs).

---

## Document control

| Field | Value |
|---|---|
| Version | 0.1.1-s1 |
| Status | Draft — S1 provisionally adopted; pending team review |
| Prior RQ | Outline RQ-A retired as primary |
| Next version trigger | Pilot go/no-go + threshold sign-off → v0.2 |

**Manuscript drafting authorization:** **Not granted.**
