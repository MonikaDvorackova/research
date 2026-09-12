# Claim–Evidence Ledger — WorldConsistMem ICLR

Authoritative artefacts: `experiments/worldconsistmem/results/scaled/*.csv`, `results/corruption_metrics.csv`, `results/new/**`, Option A freeze hashes.

| ID | Exact claim (target wording) | Evidence | Scope | Strength | Safe now? | Required edit |
|----|------------------------------|----------|-------|----------|-----------|---------------|
| C1 | Acc and BCR are different evaluation objects; BCR is joint Φ over a dependent answer set | Eq. Acc/Φ/BCR; `evaluate.py`/`constraints.py` | Formal | Demonstrated | Yes | Clarify empty-C and Gapq interpretation |
| C2 | Identical Acc need not imply identical BCR | Prop construction; frozen B2 vs B3-k3 Acc=0.4905 BCR 0.2188 vs 0.0 (`system_results.csv`) | Frozen symbolic full | Demonstrated | Yes | Keep; center in intro/results |
| C3 | High Acc can coexist with low BCR (Acc overstates joint reconstruction) | B4 Acc 0.929 BCR 0.591; B3-k8 Acc 0.567 BCR 0.0625; corruptions | Frozen | Demonstrated | Yes | Unify claim language |
| C4 | Acc-only ranking can mis-order systems | B2↔B3-k3 tie on Acc; B4 near-sat Acc with ~41% BCR fails | Frozen | Demonstrated | Yes | Keep practical consequence |
| C5 | Corruption suite separates Acc and BCR | `corruption_metrics.csv` | Smoke/corruption | Demonstrated | Yes | Keep |
| C6 | Under Qwen 3B H4, BCR=0 for all four systems; CSR weakly separates | `run2/qwen_system_results.csv` | Frozen H4 LLM | Demonstrated | Yes | Keep limitation prominent |
| C7 | Qwen BCR=0 is not unsatisfiable constraints on H4 | NEW gold Acc=BCR=1 (`h4_gold_sanity.json`) | NEW H4 gold | Demonstrated | Yes | Label NEW |
| C8 | Architecture superiority unsupported under Qwen | All BCR=0 | Frozen H4 | Demonstrated | Yes | Keep negative claim |
| C9 | Gap not only “retrieval hardness” | Shortcuts majority Acc≈0.352 BCR=0; consistent_wrong_world Acc 0.394 BCR 1; identical Acc≠BCR | Frozen+NEW | Supported | Partial | Explicit anti-confounder paragraph |
| C10 | Synthetic generator necessary for causal Φ scoring | Benchmark § | Method | Supported | Yes | Keep |
| C11 | Ecological / model-scale validity established | — | — | Speculative | **No** | Must not claim |
| C12 | B3 seed sweeps show generator robustness | Seeds identical B3 | NEW wpt=6 | Speculative if overclaimed | Narrowed | Keep “not replication” |
| C13 | H0 ablations: archive/temporal removal Acc 0.876 BCR 0.375 | `ablation_results.csv` | Frozen | Demonstrated | Yes | Keep |
| C14 | Residual novelty vs SetCons/LogicVault = evolving gold-world memory Φ | Related + App closest | Positioning | Supported | Yes | Strengthen early |
| C15 | Consistency ≠ factual correctness | consistent_wrong_world | Corruption | Demonstrated | Yes | Present in Discussion |
| C16 | Frozen B2 vignette: Acc=0.75 with Φ=0 on one CEO bundle (6/8 correct; historical+temporal abstain) | `results/scaled/predictions/B2_latest_only.jsonl` + `results/new/b2_vignette_ss0100_ceo0.json`; Table `tab:b2vignette` | Frozen single bundle | Demonstrated | Yes | Implemented |
| C17 | BCR is below Acc^n independence diagnostic for B4/H0 (residual beyond conjunction) | `results/confirmatory/alt_explanations/alt_explanations_summary.json` | Confirmatory read-only rescore | Demonstrated | Yes | In RQ3 |
| C18 | Qwen H4 BCR=0 robust to three parsers on frozen raw_output; Acc remains low (~0.09–0.19) | `results/confirmatory/readers/qwen_parser_sensitivity.json`; claim audit | Confirmatory | Demonstrated (parser); **not** high-Acc divergence | Yes if Acc disclosed | Honesty pass: report Acc with BCR |
| C19 | Naturalistic transfer n=36: gold Acc=BCR=1; last-event Acc=0.208 BCR=0 (difficulty probe) | `transfer_summary.json`; `analysis/claim_audit_report.json` | Confirmatory | Solvability + heuristic inadequacy | Yes if not overclaimed as Acc–BCR confirmation | Honesty pass |
| C20 | Stronger LLM / Phi confirmatory H4 completed | — | — | **Blocked** | Must not claim | PHI_BLOCKER.json |
| C21 | Stronger LLM on 36 NL scenarios completed | — | — | **Blocked** | Must not claim | `naturalistic_transfer/readers/STRONGER_READER_BLOCKER.json` |
| C22 | NL transfer demonstrates central Acc–BCR divergence under meaningful Acc | — | — | **Unsupported** | **No** | Do not claim |
| C23 | Last-event / Qwen low-Acc BCR=0 largely consistent with conjunction under low p | claim_audit conjunction diagnostic | Confirmatory | Diagnostic | Yes as diagnostic | State reference-only |

## B2 vignette trace (authoritative)

| Field | Value |
|-------|-------|
| Bundle ID | `ss0100_000:b:ceo:0` |
| System | `B2_latest_only` (baseline system, **not** a difficulty tier) |
| World tier / difficulty | small / intermediate |
| Predictions file | `experiments/worldconsistmem/results/scaled/predictions/B2_latest_only.jsonl` |
| Bundle source | `experiments/worldconsistmem/data/scaled/bundles.jsonl` |
| World source | `experiments/worldconsistmem/data/scaled/worlds/ss0100_000.json` |
| Extract JSON | `experiments/worldconsistmem/results/new/b2_vignette_ss0100_ceo0.json` |
| Extractor | `experiments/worldconsistmem/scripts/extract_b2_vignette.py` |
| Recomputed Acc | 0.75 (6/8) |
| Recomputed Φ / BCR contribution | 0 |
| Manuscript | Table `tab:b2vignette` in `sec_object.tex` (main text p.4) |

**Correction vs early summary:** the belief set has **8** queries, not 4. Acc=0.75 is six correct items. Historical CEO and temporal-order both abstain; transition/contradiction/temporal constraints fail under ∀c.
## Numerical anchors (raw → display)

| Item | Raw | Display in paper |
|------|-----|------------------|
| B2 Acc/BCR | 0.4905 / 0.2188 | 0.4905 or 0.490 / 0.219 |
| B3-k3 Acc/BCR | 0.4905 / 0.0 | same |
| B3-k8 Acc/BCR | 0.5669 / 0.0625 | 0.567 / 0.063 |
| B4 Acc/BCR | 0.929 / 0.591 | 0.929 / 0.591 |
| H0 Acc/BCR | 0.9762 / 0.8438 | 0.976 / 0.844 |
| Qwen H0 Acc/Abs | 0.1849 / 0.4825 | 0.185 / 0.483 |
| Scale | 102 / 1088 / 7140 | same |

## Frozen hash lock (must remain unchanged)

- `data/scaled/manifest.json` → `37aa8604c3e6d87691332f66d2f7c0ab93578f2fe468bc29f7e8217c1675af3f`
- `results/scaled/system_results.csv` → `eb5bd5fa87496586bd830e5f685b9950e119f9fd0ac491194b3f003343f9a2a8`
