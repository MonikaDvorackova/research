---
id: pub-03-ltkm-manuscript-outline
title: "Manuscript outline — Publication 03"
type: research-notes
status: authorized-direction
created: 2026-07-31
updated: 2026-08-02
---

# Manuscript outline — Publication 03

**Venue:** ICLR (year TBD).  
**Paper type:** Benchmark + evaluation methodology + hierarchical memory system.  
**Object:** Cross-query consistency over evolving worlds.

## Section order

| # | Section | Content |
|---|---|---|
| 0 | Abstract | After results |
| 1 | Introduction | Evolving worlds; Acc ≠ consistency; contributions |
| 2 | Related Work | Memory systems; evolving-memory benchmarks; consistency/temporal QA; position residual |
| 3 | Cross-Query Consistency in Evolving Worlds | Formal \(W,E,M,Q,Y^*,\mathcal{C}\); Acc vs \(\Phi\); examples; constraint families |
| 4 | Hierarchical Long-Term Knowledge Memory | Five components; lifecycle; interfaces; predicted consistency roles |
| 5 | WorldConsistMem Benchmark | Generator; entities; observation stream; query families; bundles |
| 6 | Experimental Setup | Metrics suite; baselines; ablations; matched budgets; models |
| 7 | Results | H1–H4 tests; main tables; Acc–Gap |
| 8 | Failure Analysis | Violation types; qualitative bundles; component diagnostics |
| 9 | Discussion | Limits; relation to MemConflict/LongMemEval; what consistency does not measure |
| 10 | Conclusion | |
| A | Appendix | Schemas, prompts, hyperparams, extra tables |

## Figures / tables (provisional)

| Artefact | Content |
|---|---|
| Fig. 1 | Acc vs consistency; inconsistent high-Acc example |
| Fig. 2 | Architecture + lifecycle |
| Fig. 3 | Benchmark world + bundle schematic |
| Table 1 | Benchmark statistics |
| Table 2 | Main results (Acc, BCR, ConsAcc, Gap) |
| Table 3 | Constraint violation breakdown |
| Table 4 | Ablations |
| Table RW | Benchmark positioning |

## Contribution hygiene

- No CR-Gap / Archive Pareto / AUG / P-Bind / C1 / C4 as primary claims.  
- H1–H4 stated as hypotheses until measured.  
- Experimental sections empty until runs exist.
