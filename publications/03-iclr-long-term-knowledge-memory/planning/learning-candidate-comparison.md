---
id: pub-03-learning-candidate-comparison
title: "Learning-candidate comparison and ranking"
type: research-notes
status: search-complete
created: 2026-08-01
updated: 2026-08-01
---

# Learning-candidate comparison

Source: [`learning-centric-rq-search.md`](learning-centric-rq-search.md).  
Literature: [`memory-learning-literature-matrix.md`](memory-learning-literature-matrix.md).

## Novelty classification

| ID | Space | Novelty class | Rank? |
|---|---|---|---|
| C1 Observational delayed-write identifiability | Credit | **PARTIALLY OPEN** (strong) | Yes |
| C2 Catastrophic persistence after shift | Non-stationarity | **OCCUPIED** | No |
| C3 Rewrite hysteresis / absorbing errors | Feedback | **OCCUPIED** | No |
| C4 Consolidation SS preservation | Representation | **PARTIALLY OPEN** | Yes |
| C5 Joint write–retrieve degenerate equilibria | Policy + stability | **OCCUPIED** | No |
| C6 Test-time memory adaptation | Test-time | **OCCUPIED** | No |

None classified **OPEN**. None **NOT FEASIBLE** locally among survivors. None purely **NOT ICLR-SHAPED** if framed correctly (C1/C4 become NOT ICLR-SHAPED if reduced to SOTA manager / compression bakeoff).

## Occupied candidates (detail)

| ID | Occupying work |
|---|---|
| C2 | OSL-MR (retention under shift/stale risk); Oblivion; Memory Worth / When to Forget; ALMA |
| C3 | Honest Lying (confabulation); EDV (self-confirmation) |
| C5 | InfoMem (reward-induced memory degeneration); Memory-R1 / MemPO joint training |
| C6 | AdaMEM; MemCon; MemRL; ALMA |

## Surviving candidates — scorecard (1–5)

Higher is better except **literature saturation risk** (5 = most saturated / dangerous).

| Criterion | C1 | C4 |
|---|---|---|
| Novelty | 3 | 3 |
| ICLR fit | 4 | 4 |
| Scientific depth | 4 | 4 |
| Falsifiability | 5 | 5 |
| Learning-content strength | 5 | 4 |
| Local pilot feasibility | 5 | 5 |
| Full-study feasibility | 3 | 3 |
| Literature saturation risk | **5** | 4 |
| Potential for theory / general law | 4 | 4 |
| Compatibility with LTKM platform | 4 | 4 |
| **Mean (invert sat: 6−sat)** | **3.9** | **3.9** |
| **Tie-break** | Prefer **C1** (clearer credit-assignment law; matches preferred RQ shape; sharper kill criteria) | Runner-up |

Saturation note: C1’s method neighborhood is denser (Memory-R2 family). C4’s risk is being read as “another abstraction/compression paper” (MCMA).

## Ranked shortlist

1. **C1** — Observational identifiability of delayed memory-write value  
2. **C4** — Consolidation sufficient-statistic preservation vs irreversible collapse  

## Recommendation

**C1** — see full package in [`learning-centric-rq-search.md`](learning-centric-rq-search.md) § Final recommendation.

If C1 fails novelty-kill deep-read or pilot abandonment criteria → evaluate C4; if C4 fails → `NO VIABLE LEARNING-CENTRIC MEMORY QUESTION FOUND` for this search round.
