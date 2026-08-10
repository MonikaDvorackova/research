---
id: pub-03-pbind-kill-pilot-protocol
title: "P-Bind kill pilot protocol"
type: research-notes
status: ready-after-novelty-ack
created: 2026-08-01
updated: 2026-08-01
---

# P-Bind kill pilot protocol

**Parent:** [`research-specification-v0.2.md`](research-specification-v0.2.md)  
**Novelty:** [`p-bind-novelty-audit.md`](p-bind-novelty-audit.md) — PARTIALLY OPEN  
**Gates:** [`p-bind-go-no-go.md`](p-bind-go-no-go.md)

**Do not implement until novelty PARTIALLY OPEN is team-acknowledged.** Implementation prompt at end.

---

## 0. Pilot questions

1. Does binding-error rate increase with \(\rho\) under gold-present, fixed \(k\), matched length, fixed gold rank?  
2. Are ≥50% of *additional* high-ρ errors genuine entity/attribute swaps?  
3. Does the effect survive across ≥2 model families?  
4. Does explicit binding-table prompting fully eliminate it (<5pp residual)?

---

## 1. Symbolic overlap variable \(\rho\) (primary)

Do **not** use embedding similarity as the sole primary IV.

### Competitor schema

Each context item: `(entity_id, entity_surface, attribute, value)`.

### Overlap factors (composable)

| Factor | Levels |
|---|---|
| F1 Same attribute, different entity | off/on |
| F2 Same entity, different attribute | off/on |
| F3 Same value, different entity/attribute | off/on |
| F4 Lexically similar entity names (shared prefix / edit distance ≤2) | off/on |
| F5 Semantically related attributes (predefined groups, e.g. city/country/region) | off/on |
| F6 Near-duplicate records (paraphrase surfaces, same triple meaning) | count 0–2 |

### Ordinal \(\rho \in \{0,1,2,3\}\)

| \(\rho\) | Construction |
|---|---|
| 0 | **Oracle / no-distractor:** \(C_k=\{g\}\) padded with unrelated filler facts (no shared entity, attribute, value, or name prefix with \(g\)) to matched length |
| 1 | **Low:** fillers + 1 competitor with **at most one** of F1–F5 |
| 2 | **Medium:** \(k-1\) competitors; majority share **exactly one** strong factor (prefer F1 or F4); no F6 |
| 3 | **High / adversarial binding:** multiple F1+F4 (+ optional F3/F5); include ≥1 near-duplicate (F6); maximize cross-entity same-attribute competition |

Record the exact factor bitvector per instance. Secondary analyses may use bitvectors; primary plots use \(\rho\).

**Length matching:** pad with neutral filler propositions so total context tokens (approx. whitespace-split) match within ±5% across ρ for the same template.

---

## 2. Retrieval / context control

Pilot **constructs** \(C_k\) directly (no learned retriever). This still tests gold-present retrieved context.

| Control | Primary setting | Secondary |
|---|---|---|
| \(k\) | 6 | — |
| Gold present | Always | — |
| Gold rank | **Fixed middle** (position 3 of 6) | first / last |
| Token length | Matched across ρ | — |
| Answer format | Forced single token/span | — |
| Order | Fixed construction order | shuffled-order repeat (seeded) |

Log per instance: gold rank, competitor ranks, token count, order hash, ρ, factor bits.

---

## 3. Task families (≥3)

All deterministic exact-match gold.

### A. Direct attribute lookup
`What is {attr} of {entity}?` → gold value.

### B. Multi-entity comparison
Several similar entities in \(C_k\); ask for one entity’s attribute. Stresses entity swaps.

### C. Relational binding
Role/relation attributes (`reports_to`, `works_at`, `owns`); ask who/what binds to the queried entity.

≥100 instances total; balanced across A/B/C as possible (e.g. 40/30/30).

---

## 4. Error taxonomy (primary label, priority order)

Classify each incorrect answer with **exactly one** primary label (first match wins):

1. **entity_swap** — output equals a competitor value that is the queried attribute for a *different* entity in \(C_k\).  
2. **attribute_swap** — output equals a value of the *queried entity* but for a *different* attribute in \(C_k\).  
3. **value_substitution** — output equals some other value appearing in \(C_k\) that is not (1) or (2).  
4. **unsupported** — output not in any \(C_k\) values.  
5. **gold_ignored** — model produces empty/wrong schema while gold string was trivially copyable (rare; use if output is refusal or boilerplate).  
6. **malformed** — fails parse / not in allowed answer format.  
7. **other** — residual.

**Examples**

- Context: Alice city=Prague; Bob city=Berlin. Q: city of Alice? Answer Berlin → **entity_swap**.  
- Context: Alice city=Prague; Alice role=Manager. Q: city of Alice? Answer Manager → **attribute_swap**.  
- Context includes Prague & Berlin; answer Vienna → **unsupported**.  
- Answer “Berlin, Prague” → **malformed** (if single span required).

Secondary labels allowed (e.g. `near_duplicate_confused`) but must not replace primary.

---

## 5. Models and decoding (local MLX)

≥2 families, e.g.:

- Family 1: Qwen2.5 or similar small instruct (MLX)  
- Family 2: Llama-3.x or Phi instruct (MLX)

Deterministic decoding: temperature 0; fixed max tokens; identical prompts. Exact-match scoring (normalized case/punctuation).

If a second family cannot be downloaded, document blockage — GO requires two families.

---

## 6. Inference conditions (not architectures)

| ID | Condition | Purpose |
|---|---|---|
| C0 | Plain bullet list of facts | Baseline |
| C1 | Structured table (Entity \| Attr \| Value) | Representational |
| C2 | Explicit “extract entity–attribute pairs” then answer | Prompt-induced |
| C3 | Scratchpad: fill binding table for queried entity before answer | Intermediate binding |
| C4 | Oracle context = gold only (matched length via inert padding) | Ceiling / parametric check |

Primary dose–response reported on **C0**. Interventions C1–C3 tested at ρ=0 and ρ=3. C4 sanity check.

---

## 7. Metrics

**Primary**

- Exact accuracy  
- Binding-error rate = (entity_swap + attribute_swap) / N  
- Entity-swap rate; attribute-swap rate  

**Dose–response:** plot accuracy and binding-error rate vs \(\rho\) (with Wilson or bootstrap 95% CIs).

**Secondary:** by task family; by gold position (secondary); by competitor count; tokens/latency diagnostics only.

Do **not** headline a single collapsed score.

---

## 8. Confound controls (checklist)

- [ ] Context length matched across ρ  
- [ ] Gold position fixed in primary  
- [ ] Number of facts = \(k\) fixed  
- [ ] Entity-name frequency balanced (surface sampling)  
- [ ] Answer-token frequency: avoid rare values only in high-ρ  
- [ ] Lexical similarity recorded; ρ symbolic primary  
- [ ] Attribute-domain size fixed per attribute  
- [ ] Prompt wording frozen  
- [ ] Order: primary fixed + shuffled repeat  
- [ ] Model scale: ≥2 families  
- [ ] Gold always present (assert in code)

**Limitation to state if true:** symbolic ρ correlates with lexical similarity by construction (F4); report partials / ablation with F4 off.

---

## 9. Smallest decisive design

| Factor | Value |
|---|---|
| Instances | ≥100 (recommend 120) |
| ρ levels | 0,1,2,3 |
| Seeds | 42, 43 for generation; eval deterministic |
| Primary gold rank | middle |
| Conditions | C0 full ρ sweep; C1–C3 at ρ∈{0,3}; C4 at all ρ or ρ∈{0,3} |
| Models | ≥2 MLX instruct models |

---

## 10. Artefacts

```text
experiments/p-bind-pilot/
  data/instances.jsonl
  outputs/{model}/predictions.jsonl
  outputs/summary_by_rho.csv
  outputs/error_taxonomy.csv
  outputs/go_nogo.md
```

---

## 11. Exact implementation prompt

```text
Implement experiments/p-bind-pilot per
publications/03-iclr-long-term-knowledge-memory/planning/p-bind-kill-pilot-protocol.md
and research-specification-v0.2.md.

Scientific object: entity–attribute binding accuracy under semantically
competitive retrieved context, conditional on gold evidence present.

Requirements:
- Generate ≥100 instances with symbolic overlap rho in {0,1,2,3}.
- Always include gold in C_k; primary gold rank = middle; k=6;
  match context length across rho (±5% tokens).
- Task families A/B/C with deterministic exact-match answers.
- Error taxonomy with priority: entity_swap, attribute_swap,
  value_substitution, unsupported, gold_ignored, malformed, other.
- Run ≥2 local MLX instruct model families, temperature 0.
- Conditions: C0 plain (full rho sweep); C1 table, C2 extract,
  C3 binding scratchpad at rho 0 and 3; C4 oracle-gold.
- Emit summary_by_rho.csv, error_taxonomy.csv, go_nogo.md using
  thresholds in p-bind-go-no-go.md.
- Do not redesign LTKM; no learned retriever; do not reopen S1/CR-Gap;
  do not commit unless asked.

Engineering success = runs complete + go_nogo.md filled.
```
