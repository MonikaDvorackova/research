---
id: pub-03-ltkm-archive-pareto-pilot-protocol
title: "Archive Pareto pilot protocol — Publication 03"
type: research-notes
status: ready-for-implementation
created: 2026-07-31
updated: 2026-07-31
tags: [iclr, publication-03, pilot, archive-pareto, s1]
---

# Archive Pareto pilot protocol

**Parent contract:** [`research-specification-v0.1.md`](research-specification-v0.1.md)  
**RQ:** [`research-question.md`](research-question.md)  
**Goal:** Fastest experiment that can **kill or green-light** S1 before any manuscript work.

---

## 0. Pilot questions (must answer)

1. Does a real current–historical trade-off appear under a fixed budget?  
2. Does archive ratio \(\alpha\) move systems along a Pareto frontier?  
3. Does LTKM (active+archive split) differ from a flat temporal baseline under the same \(B\)?  
4. Does the effect vary with world-change rate or historical-query horizon?

---

## 1. Scientific object (pilot)

**IV:** archive ratio \(\alpha = B_a / B\) under hard constraint \(B_c + B_a = B\).  
**DVs:** current-state accuracy \(A_c\); historical-state accuracy \(A_h\) (also by horizon).  
**Platform:** minimal LTKM-compatible active store + archive store (full five-layer stack **not** required).

### Not tested in pilot

Hierarchy superiority; learned routing; graph necessity; conflict/multi-hop as primary; CR-Gap reconstruction.

---

## 2. Fixed-budget accounting

### 2.1 Symbols

| Symbol | Meaning |
|---|---|
| \(B\) | Total budget in **fact slots** |
| \(B_c\) | Active/current slots |
| \(B_a\) | Archive slots |
| \(\alpha\) | \(B_a / B\) |
| \(k\) | Retrieval budget (max facts into reader) |

### 2.2 Primary unit: fact slots

One **slot** = one dated atomic assertion:

```text
(entity_id, attribute, value, t_valid_from, t_valid_to | null, source_event_id)
```

**Counts toward \(B\):** every stored assertion in active or archive, including superseded rows retained for history.  
**Also count (pilot rule):** if a summary replaces \(n\) facts, it costs \(\max(1, \lceil n/m \rceil)\) slots with \(m=4\) fixed—or **forbid summaries in pilot** (preferred).

**Pilot preference:** **no summaries, no embeddings, no graph index** — store structured facts only. Eliminates representation-cost confounds.

**Limitations:** slot ≠ byte cost of production vector DBs; document that main study may add byte accounting as sensitivity.

### 2.3 Fairness invariants

1. For every condition: `slots_active + slots_archive <= B` (equality target when full).  
2. No shadow store outside the count.  
3. Identical fact schema for all baselines.  
4. Identical \(k\) unless an analysis explicitly sweeps \(k\).  
5. Log per-step occupancy `(B_c_used, B_a_used, B)`.

---

## 3. Hypotheses and thresholds (pilot)

Copy from Spec §3.2:

| Symbol | Value |
|---|---|
| \(\tau_c\) | 0.05 absolute accuracy |
| \(\tau_h\) | 0.05 |
| \(\tau_{\mathrm{flat}}\) | 0.03 mean abs. diff. vs flat temporal at same \(B\) |
| Material trade-off | \(\mathrm{range}_\alpha(A_c)\ge \tau_c\) **and** \(\mathrm{range}_\alpha(A_h)\ge \tau_h\), **or** Spearman \(\rho(A_c,A_h)\le -0.3\) with both ranges \(\ge 0.03\) |

**H0 / H1:** Spec §3.  
Do **not** assume an interior \(\alpha\) optimum.

---

## 4. Fastest falsification experiment (design)

| Factor | Pilot levels |
|---|---|
| Sequences | \(N \ge 100\) (recommend 120) |
| Seeds | 42, 43 (minimum) |
| Archive ratios \(\alpha\) | \(\{0, 0.25, 0.50, 0.75\}\) (4 minimum; optional +0.10,+1.0) |
| Total budgets \(B\) | \(\{32, 64, 128\}\) fact slots |
| Retrieval \(k\) | 8 (fixed); optional sensitivity \(k\in\{4,8,16\}\) at one \(B\) |
| World-change rate | \(\{\mathrm{low}, \mathrm{high}\}\) |
| Horizon | short vs long historical queries (see §5) |
| Reader | **Symbolic exact match** on retrieved facts (primary); optional extractive string match |
| Learned routing | **Forbidden** |
| LLM downloads | **Forbidden** unless symbolic reader blocked (should not be) |

**Core cell count (minimum):**  
\(100\times 2\text{ seeds} \times 4\alpha \times 3B \times 2\text{ rates}\) is heavy if naively crossed.  
**Pilot schedule (kill-first):**

1. **Phase A (kill):** \(N=100\), seed 42, \(B=64\), \(\alpha\in\{0,0.25,0.5,0.75\}\), change rate high, all baselines B0/B2/B3/B4/B5, \(k=8\).  
2. If Phase A shows no trade-off → **stop** (optional confirm seed 43 once).  
3. **Phase B:** add \(B\in\{32,128\}\); change rate low; horizon split; seed 43; compare LTKM vs B3.  
4. **Phase C (optional):** \(k\) sweep; \(\alpha\in\{0.1,0.9,1.0\}\).

---

## 5. Evolving-world benchmark (minimal)

### 5.1 State

- Entities: \(E\) (pilot default 20).  
- Attributes: fixed set (e.g. `location`, `status`, `owner`, `level`) — 4 attributes.  
- Relations: optional binary `works_with` (pilot may omit relations to reduce scope).  
- World state \(Z_t\): map `(entity, attribute) -> value` with full history log.

### 5.2 Events (generator must support)

| Event type | Effect |
|---|---|
| `init` | Set initial facts at \(t=0\) |
| `update` | Supersede value; old value becomes historical |
| `temp_change` | Change with scheduled reversion |
| `revert` | Restore previous value |
| `unrelated` | Update a different entity/attribute (distractor churn) |

**Supersession:** on `update`, previous assertion gets `t_valid_to = t` and is eligible for archive retention.

### 5.3 Independent axes

| Axis | Pilot encoding |
|---|---|
| World-change rate | Expected updates per timestep: low=0.2, high=1.0 (Poisson or Bernoulli per entity-attr) |
| Entities | 20 (fixed in Phase A); optional 10/40 later |
| Revisions per fact | Cap mean revisions; high-rate worlds induce more |
| Historical-query proportion | Phase A: 50% current / 50% historical; Phase B: also 20/80 and 80/20 |
| Query horizon | Short: \(t_q - t^\star \le 3\); Long: \(t_q - t^\star \ge 10\) |
| Memory budget \(B\) | 32 / 64 / 128 |

Horizon \(T\): 40 timesteps (Phase A). Queries issued at fixed probe times \(\{10,20,30,40\}\).

### 5.4 Query types (primary)

**Current:** “What is `attr` of `entity` at time \(t_q\)?” → gold = \(Z_{t_q}\).  
**Historical:** “What was `attr` of `entity` at time \(t^\star\)?” or “Before the update at \(t_u\), what was …?” → gold from history log.

**Determinism:** given `(seed, sequence_id, params)`, world and gold are pure functions. No LLM-as-judge.

### 5.5 CR-Gap / reuse policy

- Do **not** use CR-Gap metrics (reconstruction faithfulness, overwrite vs revision-aware labels).  
- If adapting code from `experiments/cr-gap-pilot/`, document: files reused, what was removed (conflict-density CR claims), and that gold is current/historical QA—not reconstruction.

### 5.6 Output artefacts

```text
data/archive_pareto_pilot/
  sequences.jsonl          # worlds + event logs
  queries.jsonl            # query_id, type, gold, horizon, ...
outputs/archive_pareto_pilot/
  predictions.jsonl
  summary_by_alpha.csv
  pareto_points.csv
  go_nogo.md
```

---

## 6. Archive-allocation dial (LTKM platform)

### 6.1 Ratios

| \(\alpha\) | \(B_a\) | \(B_c\) | Meaning |
|---|---|---|---|
| 0.00 | 0 | \(B\) | Current-only; superseded facts dropped when leaving active |
| 0.10 | \(0.1B\) | \(0.9B\) | Small archive |
| 0.25 | \(0.25B\) | \(0.75B\) | Pilot grid |
| 0.50 | \(0.5B\) | \(0.5B\) | Pilot grid |
| 0.75 | \(0.75B\) | \(0.25B\) | Pilot grid |
| 0.90 | \(0.9B\) | \(0.1B\) | Optional |
| 1.00 | \(B\) | 0 | Archive-all; active empty (retrieve from archive only) |

Use integer floors; assert \(B_c + B_a = B\).

### 6.2 Deterministic policies (pilot — measure allocation, not learning)

**Write path (active):**

1. On new assertion: write to active if space; else evict from active per policy, then write.  
2. When an assertion is superseded: move old assertion to archive if \(B_a>0\) and archive has space (or after archive eviction); else drop.

**Active eviction (when \(B_c\) binds):** drop least-recently-updated **current** fact among entities not referenced in the last \(w=5\) events (tie-break: lowest entity_id, attribute name).  
**Archive eviction (when \(B_a\) binds):** drop superseded fact with oldest `t_valid_to` (FIFO among superseded).  
**Promotion:** superseded → archive only (no learned score).  
**Retrieval:** from allowed stores, rank by: (1) exact entity+attribute match, (2) temporal applicability to query time, (3) recency; return top \(k\).

At \(\alpha=0\): superseded facts are **deleted** (not archived).  
At \(\alpha=1\): \(B_c=0\); all retained knowledge lives in archive under FIFO superseded + any “current snapshot” packed into archive slots (document packing rule: keep latest value per `(entity,attr)` preferentially in archive when active is empty).

---

## 7. Baseline matrix

| ID | Name | \(B\) use | Write | Eviction | Superseded | Retrieval | Notes |
|---|---|---|---|---|---|---|---|
| B0 | Current-only | All \(B\) as active; \(B_a=0\) | Latest facts only | Same as LTKM active | Drop | Top-\(k\) from active | ≡ LTKM \(\alpha=0\) |
| B1 | Archive-all | All \(B\) as archive; \(B_c=0\) | Append dated facts | Archive FIFO | Retain until FIFO | Top-\(k\) from archive | ≡ \(\alpha=1\); optional Phase C |
| B2 | LTKM fixed-\(\alpha\) | \(B_c+B_a=B\) | §6.2 | §6.2 | To archive | Active∪archive | **Primary sweep** |
| B3 | Flat temporal keep-all | Single store size \(B\) | Append all dated facts | Global FIFO when \(>B\) | Retain until FIFO | Top-\(k\) temporal match | **Indispensable** |
| B4 | Recency eviction | Single store \(B\) | Latest-only per key + optional last value | Evict globally oldest current | Drop history | Top-\(k\) | Trivial “hot” memory |
| B5 | Random/reservoir | Single store \(B\) | Reservoir sample of all assertions | Random replace | Stochastic retain | Top-\(k\) | Non-intelligent control |
| B6 | Oracle allocation | \(B\) with hindsight split | Ideal retain set for query mix | N/A | Keep query-needed | Gold facts if stored | Optional upper bound |

**Every baseline** must log counted slots ≤ \(B\) and use the **same** \(k\) and **same** reader.

**Architecture demotion rule:** if B3’s Pareto (vary FIFO pressure / effective history fraction if needed) matches or dominates B2’s \(\alpha\) frontier within \(\tau_{\mathrm{flat}}\), LTKM cannot be credited; S1 may still survive as an **allocation** finding on B3 alone—but hierarchy platform claim is demoted.

For pilot Phase A, generate B3 points by running the flat store at full \(B\) (one point). To compare *frontiers*, optionally sub-sample retention pressure by varying how aggressively FIFO drops—or compare B2’s cloud of \(\alpha\) points to B3’s single best point at each \(B\) (minimum bar). Prefer: also run B3 with forced history-capacity fractions mirroring \(\alpha\) via “tagged cold slots” **without** hierarchical APIs—if that collapses to B2, hierarchy is irrelevant.

---

## 8. Reader and scoring

### 8.1 Symbolic reader (primary)

Input: query `(entity, attribute, time_ref)` + retrieved facts.  
Select fact whose validity interval covers `time_ref` (or latest `t_valid_from ≤ time_ref` with open `t_valid_to`).  
If none: abstain → incorrect.  
Score: exact value match → 1 else 0.

### 8.2 Metrics to emit

Per condition `(baseline, α, B, rate, seed)`:

- \(A_c\), \(A_h\), \(A_h\) short, \(A_h\) long  
- mean slots used  
- mean retrieval hits that contain gold fact  
- superseded retained count  

Aggregate:

- Pareto CSV of \((A_c, A_h)\) by \(\alpha\)  
- ranges and Spearman \(\rho\)  
- go/no-go checklist (§10)

**Forbidden as headline:** single scalar mixing \(A_c\) and \(A_h\).  
If reporting \(U_\lambda\), use \(\lambda \in \{0.25, 0.5, 0.75\}\).

---

## 9. Indispensable analyses (pilot minimum)

| Analysis | Phase |
|---|---|
| \(\alpha\) sweep → Pareto at fixed \(B=64\), high change | A |
| Compare B2 vs B3 vs B4 vs B5 | A |
| Reproduce seed 43 | B |
| Low vs high change rate | B |
| Short vs long horizon \(A_h\) | B |
| \(B \in \{32,128\}\) | B |
| Matched-\(k\) sensitivity | C optional |
| Partial correlation \(A_h\) vs retained-count controlling \(\alpha\) | B |

---

## 10. Go / no-go (numeric)

### Go (all required)

| # | Criterion | Numeric rule |
|---|---|---|
| G1 | Material \(\alpha\) movement | \(\mathrm{range}(A_c)\ge 0.05\) and \(\mathrm{range}(A_h)\ge 0.05\) at ≥1 \(B\), **or** Spearman criterion §3 |
| G2 | No universal dominate | No \(\alpha\) with \(A_c\) and \(A_h\) both ≥ all others − 0.01 in all Phase A/B cells |
| G3 | Regime sensitivity | \(\Delta\mathrm{range}\) or frontier shift ≥ 0.05 on \(A_h\) or \(A_c\) between low/high change **or** short/long horizon |
| G4 | Fair budgets | Occupancy logs show ≤\(B\); same \(k\) |
| G5 | Non-trivial vs recency | At ≥1 regime, B2 best-\(U_{0.5}\) exceeds B4 by ≥ 0.05 on \(U_{0.5}\) **or** B2 \(A_h\) exceeds B4 by ≥ 0.05 at \(A_c\) within 0.05 |
| G6 | Seed replication | Trade-off sign (negative \(\rho\) or opposing ranges) agrees on seeds 42 and 43 |

### No-go (any triggers stop/reframe)

| # | Criterion | Numeric rule |
|---|---|---|
| N1 | Universal dominate | Violates G2 |
| N2 | Record-count only | Linear \(A_h \sim\) retained_count has \(R^2\ge 0.95\) and \(\mathrm{range}(A_c)<0.05\) |
| N3 | Flat matches/dominates | For each \(B\), B3 within 0.03 of best B2 on both axes, or B3 ≥ B2 on both |
| N4 | \(A_c\) insensitive | \(\mathrm{range}(A_c)<0.05\) across \(\alpha\) at all \(B\) |
| N5 | Free historical lunch | \(\mathrm{range}(A_h)\ge 0.05\) and \(\mathrm{range}(A_c)<0.05\) |
| N6 | Accounting brittle | Slots vs token recount (if run) flips go decision |

Write `outputs/.../go_nogo.md` with PASS/FAIL per row.

---

## 11. Implementation constraints

- Deterministic synthetic world only.  
- Symbolic reader first.  
- ≥100 sequences; ≥4 \(\alpha\); ≥3 \(B\) before claiming Phase B complete.  
- Flat temporal baseline mandatory.  
- No learned routing; no large model downloads for Phase A.  
- Do not redesign full five-layer LTKM.  
- Do not import CR-Gap claims.

### Suggested package layout

```text
experiments/archive-pareto-pilot/
  README.md
  configs/pilot.yaml
  src/...
  tests/...
  data/...
  outputs/...
```

---

## 12. Exact implementation prompt

Copy-paste for the implementing agent/engineer:

```text
Implement experiments/archive-pareto-pilot per
publications/03-iclr-long-term-knowledge-memory/planning/archive-pareto-pilot-protocol.md
and research-specification-v0.1.md (S1).

Scientific object: under fixed total memory budget B (fact slots),
sweep archive ratio alpha = B_a/B with B_c + B_a = B, and measure
current-state accuracy A_c vs historical-state accuracy A_h on a
deterministic evolving-world QA benchmark.

Requirements:
- Deterministic world generator (entities, attributes, updates,
  supersession, temp changes, reversions, unrelated churn).
- Gold current and historical answers; no LLM-as-judge.
- Primary memory unit: dated fact slots; no uncounted capacity.
- LTKM platform simplified to active + archive with deterministic
  eviction/promotion as specified; no learned controller.
- Phase A: N>=100, seed 42, B=64, alpha in {0,0.25,0.5,0.75},
  high change rate, k=8, symbolic reader.
- Baselines: B0 current-only, B2 LTKM alpha sweep, B3 flat temporal
  keep-all under same B, B4 recency, B5 reservoir/random.
- Log slot occupancy every step; enforce <= B.
- Emit summary_by_alpha.csv, pareto_points.csv, go_nogo.md using
  thresholds tau_c=tau_h=0.05, tau_flat=0.03.
- Do not redesign five-layer architecture; do not use CR-Gap claims;
  do not download large LLMs for Phase A; do not commit unless asked.

Success of engineering task = Phase A runs + go_nogo.md filled.
Then run Phase B if Phase A does not no-go.
```

---

## 13. Contribution positioning (for later writing — not manuscript now)

Use only after go:

- constrained resource-allocation study;  
- trade-off characterization / empirical Pareto analysis;  
- regime map: when archive retention is beneficial, costly, or unnecessary;  
- LTKM as experimental control surface, not the result.

---

## Document control

| Field | Value |
|---|---|
| Status | Ready for implementation |
| Blocks manuscript? | Yes until go |
| Owner (code) | Technical collaborators |
| Owner (interpretation) | Monika after results |
