---
id: pub-03-ltkm-research-question
title: "Research question and scientific spine — Publication 03 (provisional)"
type: research-notes
status: provisional-frozen-s1
created: 2026-07-31
updated: 2026-07-31
---

# Research question and scientific spine (provisional — S1)

**Status:** Provisional primary RQ **adopted as S1** (archive Pareto). Architecture is platform, not claim.  
**Authority:** [`research-question-search.md`](research-question-search.md) → S1; contract in [`research-specification-v0.1.md`](research-specification-v0.1.md); pilot in [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md).  
**Manuscript:** Not authorized. Pilot go/no-go first.

---

## Frozen provisional research question (S1)

> **Under a fixed total memory budget, how does archive retention of superseded knowledge trade off current-state accuracy against historical-state accuracy in an evolving world?**

**Operational form:**

> Holding hierarchy interface, retrieval budget \(k\), and total memory capacity \(B\) fixed, does increasing archive ratio \(\alpha = B_a / B\) improve historical-task accuracy, and at what \(\alpha\) does current-task accuracy degrade due to reduced active-memory capacity and/or retrieval competition?

---

## Scientific object

**Memory-budget allocation between:**

1. knowledge optimized for **current** use (\(B_c\)); and  
2. retained **superseded** knowledge required for **historical** queries (\(B_a\));

under the hard constraint \(B_c + B_a = B\).

Hierarchical LTKM is the **experimental platform** that exposes the archive dial. It is not the result.

### Explicitly not claimed

- hierarchy is generally superior;
- archives are universally necessary;
- more storage improves performance;
- historical preservation is always desirable;
- the five-layer taxonomy is novel.

---

## Intended contribution (provisional wording)

Empirical **trade-off characterization** / **Pareto analysis** of current–historical accuracy as a function of archive allocation \(\alpha\) under fixed \(B\), including regimes where archive retention is beneficial, costly, or unnecessary.

Do **not** claim a universal law before experiments. Prefer “trade-off characterization” or “empirical Pareto analysis” until pilot + main results support stronger language.

---

## Hypotheses (summary)

- **H0:** Varying \(\alpha\) does not induce a nontrivial current–historical Pareto (flat, dominated, or trivially monotone in retained-fact count).  
- **H1:** Varying \(\alpha\) under fixed \(B\) induces a nontrivial Pareto frontier between current-state and historical-state accuracy, with regime dependence on world-change rate and/or query mix.

Full H0/H1, falsification, and go/no-go: [`research-specification-v0.1.md`](research-specification-v0.1.md) §§3–9; [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md).

---

## Method role (platform, not claim)

LTKM supplies:

- controllable \(B\), \(B_c\), \(B_a\), \(\alpha\);
- deterministic promotion/eviction for the pilot (no learned controller);
- write/read paths over evolving-world traces;
- evaluation on current and historical queries.

Novelty of the five-layer stack is **out of scope** as a primary claim.

---

## Benchmark role

Minimal controlled synthetic evolving world with gold current and historical states; independent axes for change rate, entities, revisions, historical-query proportion, horizon, and \(B\).  
Pilot protocol: [`archive-pareto-pilot-protocol.md`](archive-pareto-pilot-protocol.md).

**Do not import** closed CR-Gap reconstruction claims. Simulator code may be adapted only if scientifically appropriate and documented.

---

## Indispensable evidence

1. Fixed-budget accounting with one primary normalized unit.  
2. ≥4 archive ratios at matched \(B\).  
3. Current and historical accuracies reported **separately** (no single headline score).  
4. Flat temporal keep-all baseline under the **same** \(B\).  
5. Matched retrieval budget \(k\).  
6. Regime checks (change rate, horizon, query mix).  
7. Go/no-go gates passed before manuscript drafting.

---

## Conceptual vs implementation contribution

| Contribution type | Content | Owner |
|---|---|---|
| Conceptual | Fixed-budget framing; current vs historical objectives; RQ/H0/H1; literature positioning; Pareto-regime interpretation; Intro/Discussion after pilot passes; claim discipline | Monika |
| Implementation / empirical | World generator; memory stores; baselines; runs; stats; plots | Technical collaborators |
| Joint | Contribution list after results; abstract | All authors |

---

## Superseded provisional RQ (outline RQ-A)

~~Does hierarchical LTKM with lifecycle improve long-term knowledge consistency vs existing agent-memory systems?~~  

**Superseded.** That question made architecture the claim and is occupied by hierarchical agent-memory literature. Retained only as historical outline context in the research-question search archive.
