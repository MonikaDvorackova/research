# Scientific manuscript change log (ICLR WorldConsistMem)

Date: 2026-09-08  
Scope: scientific claim discipline and reviewer objections — not packaging polish.  
Frozen Option A artefacts were **not** mutated.

## Substantive changes

### Abstract (`worldconsistmem.tex`)
- Unified central claim: Acc can overstate joint reconstruction and mis-rank systems.
- Stated BCR as a different evaluation object; Gapq definition.
- Scale + strongest supported numbers (identical Acc/BCR split; BM25 Acc/BCR; Qwen BCR floor).
- Explicit scope boundary (controlled synthetic diagnostic; no architecture superiority / ecological validity claims).

### Introduction (`sec_intro.tex`)
- Argumentative sequence: failure mode → why Acc misses it → central claim → approach → primary finding → novelty residual → contributions.
- Numbered contributions limited to demonstrated objects (formal metrics; freeze; empirical Acc–BCR dissociation + NEW anti-retrieval-hardness diagnostics).
- Avoided “first consistency metric” overclaim vs SetCons/LogicVault.

### Related work (`sec_related.tex`)
- Reviewer-facing distinction by evaluation object / failure mode (what Acc measures vs what BCR detects).
- Residual vs closest consistency benchmarks made explicit.

### Method / metric (`sec_object.tex`, `sec_metrics.tex`)
- Notation before use; Acc/Φ/BCR/Gapq equations with ranges.
- Empty-𝒞 → Φ=1 defined.
- Minimal identical-Acc / different-BCR construction aligned with frozen B2/B3-k3.
- What Gapq means and does **not** mean.
- CSR relation clarified without replacing BCR.

### Systems / setup (`sec_systems.tex`, `sec_setup.tex`)
- Fairness callouts (compact padding; capacity metadata) pointed toward appendix.

### Results (`sec_results.tex`)
- Reframed as RQ1 (Acc≠BCR objects), RQ2 (Qwen H4), RQ3 (not only retrieval).
- Centered identical Acc / different BCR and Acc-overstatement examples.
- B1 compact fairness note in main text.
- Frozen vs NEW separation enforced in structure.

### Failures (`sec_failures.tex`)
- Tied Qwen transition 192/192 failures to schematic Fig. 2 failure mode.
- Gold H4 satisfiability (NEW) surfaced.

### Discussion (`sec_discussion.tex`)
- Alternative explanations subsection with existing evidence.
- Threats to validity with threaten / does-not-threaten structure.
- Consistency ≠ factual correctness explicit.

### Conclusion (`sec_conclusion.tex`)
- Demonstrated / significance (bounded) / scope / next validation — no new evidence.
- AI Use, Ethics, Reproducibility statements retained/aligned.

## Non-changes (intentional)

- No edits to frozen CSVs, predictions, manifests, or Option A protocol.
- No new expensive experiments.
- No bit-exact figure regeneration; existing vector PDFs retained.
- No ZIP rebuild required solely for this scientific prose pass (repro package hashes unchanged by design).

## 2026-09-08 (B2 vignette + formal compliance)

### Manuscript
- Added frozen B2 CEO vignette Table `tab:b2vignette` in `sec_object.tex` (main text), with Acc=0.75 / Φ=0 over an **8-query** belief set (6 correct); historical and temporal-order abstentions fail ∀c constraints.
- Cross-links from Results and Failures without repeating the full explanation.
- Appendix pointer to `results/new/b2_vignette_ss0100_ceo0.json`.
- Shortened proposition / Gapq / practical-consequence prose to keep ≤9 main pages after adding the table.

### Code / evidence (no Option A mutation)
- Added `scripts/extract_b2_vignette.py` with explicit `ConstraintResult.to_dict()` serialization.
- Added `tests/test_extract_b2_vignette.py` (regression for prior `.get()` failure + frozen Acc/Φ checks).
- Wrote `results/new/b2_vignette_ss0100_ceo0.json`.

### Narrative correction
- Early console summary implied a 4-item “3/4” story; authoritative freeze is **6/8**. Manuscript uses 6/8.
