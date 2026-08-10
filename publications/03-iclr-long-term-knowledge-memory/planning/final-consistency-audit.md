---
id: pub-03-final-consistency-audit
title: "Final scientific consistency audit"
type: planning
status: final
created: 2026-08-04
updated: 2026-08-04
---

# Final consistency audit

Audit of `manuscript/paper.md` against `experiments/worldconsistmem/outputs/scaled/FINAL_EXPERIMENT_STATUS.md` and frozen CSVs.

## Claim → evidence map

| Claim in manuscript | Evidence | Status |
|---|---|---|
| Acc and consistency are empirically distinct | Corruption suite (Table 7); symbolic Acc–BCR gaps (Table 3) | Supported |
| High-Acc retrieval can violate bundle constraints | Symbolic B4 Acc 0.929, BCR 0.591, CSR 0.881 (Table 3) | Supported |
| Under Qwen H4, BCR = 0 for B1/B3/B4/H0 | `qwen_system_results.csv` / Table 4 | Supported |
| CSR remains discriminative (~0.26–0.33) under Qwen | `partial_consistency_results.csv`: 0.258 / 0.258 / 0.329 / 0.284 | Supported |
| H0 Acc highest (0.185) but CSR not strongest (B4 0.329) | Table 4 + partial CSR | Supported |
| Architecture superiority unsupported | Freeze + all Qwen BCR = 0 | Supported |
| Scale 102 / 1088 / 7140; H4 18 / 192 / 1260 | Dataset stats / freeze | Supported |
| Contributions are methodology, benchmark, metrics, empirical characterization | Abstract / §1 / freeze permitted claims | Supported |

## Limitations acknowledged

| Limitation | Where acknowledged |
|---|---|
| Synthetic worlds; ecological validity not claimed | §10, Table 8, Conclusion |
| Exact-match Acc | §10 |
| Frozen constraint library scope | §10 |
| Single local 3B-class reader (Qwen); Phi not run | §10, Table 8, freeze |
| H4 subset only for LLM | Table 8, freeze |
| H0 is reference baseline, not claimed winner under Qwen | Abstract, §1, §8, §10, Conclusion |
| CSR complementary when BCR floors; does not redefine BCR | §5, freeze metric notes |

## Notation / acronym check

| Symbol / acronym | Defined |
|---|---|
| Acc | Yes (per-query accuracy) |
| BCR | Yes (strict bundle consistency) |
| CSR | Yes (partial constraint satisfaction) |
| \(\Phi\), \(\mathcal{C}\) | Yes (§3 / metrics) |
| Gap_query | Yes |
| ConsAcc / PConsAcc | Yes |
| B1 / B3 / B4 / H0 | Yes (§6) |

## Figure / table reference check

| Asset | Referenced in body | Present on disk |
|---|---|---|
| Fig 1–5 | Yes | Yes (`figures/*.svg`) |
| Tab 1–8 | Yes | Yes (`tables/*.md`) + inlined |

## Residual non-blockers (editorial, not scientific)

1. Markdown assembly is authoritative for this pass; venue-specific LaTeX/PDF compile not yet executed.
2. SVG figures are camera-ready for Markdown/HTML; PDF submission may need PDF/PNG export of the same frozen plots.
3. BibTeX keys are listed; full formatted bibliography depends on venue style + `library.bib` render.

## Verdict

**PASS** for scientific freeze integrity: no new claims; numbers match frozen Option A / symbolic / corruption artefacts; limitations explicit; architecture superiority closed.
