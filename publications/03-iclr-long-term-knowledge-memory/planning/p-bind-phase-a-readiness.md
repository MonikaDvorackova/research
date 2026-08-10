---
id: pub-03-pbind-phase-a-readiness
title: "P-Bind Phase A readiness verdict and Phase B protocol"
type: research-notes
status: decision
created: 2026-08-01
updated: 2026-08-01
---

# P-Bind Phase A readiness verdict and Phase B protocol

**Inputs (assumed correct):**  
`experiments/p-bind-kill-pilot/outputs/{kill_findings,model_comparison,cross_model_analysis}.md`  
and accompanying prediction/metric artefacts under `outputs/` and `outputs/by_model/`.

**Constraints:** Benchmark frozen. No redesign of P-Bind, task generation, metrics, or RQ.

**Final verdict:** **B — ONE MORE PILOT REQUIRED** (PromptKill).  
Full ICLR study (Phase B) is **not** yet scientifically authorized.

---

## Step 1 — Empirical phenomenon demonstrated

**Demonstrated phenomenon (C0, frozen gold-present top‑k contexts):**

> When gold entity–attribute evidence is already present in a length-matched, fixed-rank retrieved context, increasing symbolic semantic competition among co-retrieved records (\(\rho{:}0\to3\)) increases the rate of **attribute–entity binding swaps** (primarily entity swaps), rather than retrieval misses, length confounds, or unstructured non-binding errors — and this pattern appears in more than one model family.

**Not demonstrated (yet):** monotonic dose–response across intermediate \(\rho\); factor-level attribution; survival under structured prompting; position-secondary robustness; frontier-scale generality.

---

## Step 2 — Property checklist

| Property | Status | Justification |
|---|---|---|
| **Reproducible** | **Yes (Phase A scope)** | Phi: seeds 14/12/14 pp; cross-seed sign and magnitude stable. Same frozen 300 inputs reused. |
| **Cross-model** | **Yes (conditional)** | Phi (13.3) and Qwen2.5-3B (11.3) both \(\Delta_{\mathrm{bind}}\ge10\) with SwapShare≥50%. Llama positive but 8.7pp (below gate). 0.5B confirmatory but capability-floor. |
| **Mechanism-independent** | **Partial — not yet** | Across *competent* models, extra ρ=3 errors are binding-dominated (entity_swap primary). Not shown independent of *prompt format* (C1–C3 untested). Not factor-decomposed (F1–F6 co-occur). Item-level Jaccard low (~0.12–0.20): shared *class* of failure, not identical instances. |
| **Statistically meaningful** | **Yes (for ρ∈{0,3} C0)** | Competent CIs exclude 0 (Phi [8.0,19.3]; Qwen3B [6.7,16.7]; Llama [4.7,13.3]). Effect sizes ~9–13pp competent. N=150/arm aggregate. |
| **Potentially generalisable** | **Partial** | Synthetic controlled records; small instruct MLX models only; relational strongest; Llama weak on direct/multi. Plausible for post-retrieval memory contexts, not yet shown beyond this construction. |
| **Interesting for ICLR** | **Conditional — blocked** | Matches the residual in the novelty audit *if* residual survives PromptKill and is not LitM. Pre-registered GO requires C3 not wipe the effect. Untested → not yet ICLR-ready. |

---

## Step 3 — Rejection-grade threats

### Internal validity
- **Prompt-triviality (critical):** Structured binding prompting (C3) or tables (C1) may eliminate \(\Delta_{\mathrm{bind}}\). Pre-registered PromptKill. Untested. Highest rejection risk.
- **Ceiling at ρ=0:** Competent models ≈100% at ρ=0; \(\Delta_{\mathrm{bind}}\) partly reflects easy baseline. Still valid contrast, but reviewers may call the low-overlap condition non-stressful.
- **Confounded ρ construction:** High-ρ packs F1–F6 jointly; cannot claim which factor causes swaps from C0 alone (mitigate in Phase B with reporting discipline, not redesign).

### Construct validity
- **“Binding” via taxonomy:** Labels are deterministic heuristics over competitor values; possible miscategorization of multi-factor cases (e.g. shared-value F3).
- **Synthetic schema:** Entity\|attribute\|value lines may overstate binding failures relative to naturalistic prose memory.
- **SwapShare >100% edge case:** Frozen definition can exceed 100% when ρ=0 non-binding errors are replaced; must be reported carefully.

### External validity
- Small local models only (≤~4B 4-bit); no frontier API model.
- Constructed \(C_k\), not live retriever + real corpus.
- English synthetic names/attrs; three task families only.
- Llama’s family skew (relational-heavy) weakens “uniform across tasks” rhetoric.

### Statistical validity
- Bootstrap CIs; limited independent bases (100) × 3 orderings (not fully independent trials).
- Multiple seeds/families without Phase A multiplicity correction (exploratory gates OK; Phase B must correct).
- Between-model pooling invalid (k small; 0.5B non-exchangeable) — already avoided.

### Novelty / positioning (reviewer)
- Binding ID / LitM / RECON neighborhood: paper must insist on **gold-present × swap-labeled × ρ** residual. If PromptKill succeeds (effect dies), novelty collapses to prompt sensitivity → **NO-GO**.

---

## Step 4 — Phase B (full study) — frozen plan

**Authorization:** Phase B runs **only after** the PromptKill micro-pilot (Step 6) returns GO.

**Benchmark:** Frozen instances, ρ definition, taxonomy, metrics, parser. New runs may add **conditions** (C1–C4) and **ρ levels** on the same bases; no regenerating competitive structure.

### 4.1 Pre-registered hypotheses

| ID | Hypothesis |
|---|---|
| **H1** | On C0, BindErr increases near-monotonically in \(\rho\in\{0,1,2,3\}\) under gold-present, fixed \(k\), matched length, fixed gold rank. |
| **H2** | \(\Delta_{\mathrm{bind}}(\rho{=}3-\rho{=}0)\ge 0.10\) on ≥2 competent model families; SwapShare\((\rho{=}3)\ge 0.50\). |
| **H3** | Primary middle-rank effect persists within 5pp under length-matched gold-first and gold-last secondary controls (PersistPos). |
| **H4 (PromptKill / survival)** | C3 at ρ=3 does **not** reduce BindErr to within 5pp of C0@ρ=0 **and** does not match C4 accuracy within 5pp. |
| **H5** | C1/C2 reduce BindErr at ρ=3 relative to C0 but leave residual \(\ge 5\)pp above C0@ρ=0 (partial mitigation, not elimination). |
| **H6** | C4 (oracle gold-only, length-matched padding) BindErr ≈ 0 and accuracy ≈ ceiling (parametric/format sanity). |

**H0 family:** flat ρ response; SwapShare\<0.50; position/length explains effect; or PromptKill triggers.

### 4.2 C1–C4 objectives (inference conditions only)

| ID | Condition | Objective |
|---|---|---|
| **C0** | Plain fixed record list (Phase A) | Primary dose–response |
| **C1** | Structured Entity\|Attr\|Value table | Representational mitigation |
| **C2** | “Extract pairs then answer” | Prompt-induced binding |
| **C3** | Scratchpad binding table for queried entity, then answer | Strongest prompt intervention / PromptKill |
| **C4** | Oracle gold-only + inert length pad | Ceiling / non-competition control |

### 4.3 Success criteria (full study GO for manuscript)

All required:

1. H1 near-monotonic on C0 (≤1 adjacent inversion ≤3pp).  
2. H2 on ≥2 competent families.  
3. H3 PersistPos.  
4. H4 PromptKill **fails** (effect survives C3).  
5. H6 C4 sanity holds.  
6. Novelty audit still PARTIALLY OPEN at write-up.

### 4.4 Stopping rules (abort manuscript track)

Stop / reframe if **any**:

1. PromptKill: C3 closes gap (BindErr@ρ=3 within 5pp of C0@ρ=0 **and** acc within 5pp of C4).  
2. \(\Delta_{\mathrm{bind}}<0.05\) on C0 full ladder for all but one family.  
3. SwapShare\<0.30 at ρ=3 on primary models.  
4. Effect only on one task family after multiplicity-aware tests.  
5. Gold-position secondary fully explains \(\Delta_{\mathrm{bind}}\) (middle unique).  
6. Novelty reclassified OCCUPIED.

### 4.5 Statistical protocol (fixed before runs)

- **Primary estimand:** \(\Delta_{\mathrm{bind}}\) on C0; paired by base instance where possible.  
- **CIs:** percentile bootstrap 95% (B=5000), seed fixed; also Wilson CIs on raw rates.  
- **Tests:** permutation or McNemar-style paired tests on bind-error indicators for ρ=0 vs ρ=3; trend test across ordered ρ (e.g. Cochran–Armitage or bootstrap contrast of slopes).  
- **Effect sizes:** absolute pp difference; risk ratio BindErr₃/BindErr₀ when defined; SwapShare.  
- **Multiplicity:** Holms within family of primary H1–H4 tests; secondary task-family and C1/C2 contrasts marked exploratory or hierarchical (primary → secondary).  
- **Models:** primary = Phi-3.5-mini + Qwen2.5-3B; Llama-3.2-3B secondary; Qwen2.5-0.5B sensitivity only (competence screen: ρ=0 acc≥95%).  
- **No pooling** across models for primary claim; report per-model + descriptive heterogeneity.  
- **Robustness:** seed-level; task-family; exclude F3-shared-value items (sensitivity); recompute SwapShare capped/uncapped.  
- **Sensitivity:** gold rank {1,3,6} length-matched; optional paraphrase surfaces without changing triples (if added, must not alter ρ labels).

### 4.6 Execution order (after PromptKill GO)

1. C0 full \(\rho\in\{0,1,2,3\}\) on primary models (reuse ρ∈{0,3} cache).  
2. C4 sanity.  
3. C3 Confirm survival (may already be done in micro-pilot — reconfirm on full ρ if needed).  
4. C1, C2.  
5. Position secondary.  
6. Lock tables → manuscript authorization.

---

## Step 5 — Publication claims

### Primary scientific claim
Under gold-present, length-matched, fixed-rank retrieved contexts, **binding-swap error rate increases with semantic competition among co-retrieved entity–attribute records**, independently of Recall@k, in multiple LM families.

### Secondary claims
- Additional high-competition errors are predominantly entity/attribute swaps (high SwapShare).  
- Structured prompting may mitigate but (if H4 holds) does not eliminate the residual.  
- Evaluation protocol for gold-present binding stress tests.

### Claims not supported by Phase A
- Full monotonic dose–response over \(\rho\in\{0,1,2,3\}\).  
- Survival under C3 / non-prompt-triviality.  
- Factor-specific causality (F1 vs F4 vs …).  
- Frontier-model generality; live-retriever generality.  
- Uniform magnitude across all task families and all model families (Llama <10pp; family skew).

### Claims that must never appear
- Hierarchical LTKM / architecture superiority.  
- “We introduce a better memory system.”  
- “Retrieval is solved; only binding remains” as a universal claim.  
- Occupation of Binding ID mechanistic story as this paper’s novelty.  
- “Distractors always hurt” without swap taxonomy and gold-present controls.  
- S1 archive Pareto / CR-Gap revival claims.

---

## Step 6 — Final verdict

# B. ONE MORE PILOT REQUIRED

### Missing pilot (exact): **PromptKill micro-pilot**

| Field | Spec |
|---|---|
| **Name** | P-Bind PromptKill |
| **Why blocking** | Pre-registered GO criterion #6 and ICLR-fit table: if C3 eliminates the effect, direction is prompt sensitivity → NO-GO |
| **Frozen** | Same `kill_instances.jsonl`; same metrics/taxonomy/parser; no new bases |
| **Conditions** | C0 vs **C3 only** (optional C4 sanity on same subset) |
| **ρ** | {0, 3} only |
| **Models** | Phi-3.5-mini + Qwen2.5-3B (competent primary pair) |
| **N** | Full 300 ordered evals per model × condition (or pre-registered balanced subset ≥100 bases if compute-bound, locked before run) |
| **GO** | At ρ=3, C3 BindErr remains **>** C0@ρ=0 BindErr + 5pp on **both** models **or** C3 fails to reach within 5pp of C4 accuracy while C0@ρ=3 still shows \(\Delta_{\mathrm{bind}}\ge10\) vs C0@ρ=0 |
| **NO-GO** | C3 brings BindErr@ρ=3 within 5pp of C0@ρ=0 **and** accuracy within 5pp of C4 on both primary models |
| **After GO** | Authorize Phase B full study (§4) |
| **After NO-GO** | Stop P-Bind as ICLR primary; do not run full C1–C4 factorial |

**Not sufficient substitutes for this pilot:** more models; ρ ladder alone; manuscript drafting.

---

## Status implication

Phase A **existence + cross-model robustness** gates: **passed**.  
Phase A **ICLR-authorization** gate: **not passed** until PromptKill.
