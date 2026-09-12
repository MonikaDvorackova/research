# Hostile Reviewer Simulation (post-revision)

Date: 2026-09-07  
Manuscript: `submission/latex/worldconsistmem.tex` → `submission/worldconsistmem.pdf` (13 pp total; Conclusion/References ~p.8; Appendix from ~p.9)  
Central claim preserved: Acc and BCR are different objects; high Acc can coexist with joint world-history failure; Gapq = Acc − BCR exposes what Acc hides.

**Submission-readiness verdict: NOT submission-ready.**  
Reasons below checklist. Do not treat this PDF as OpenReview-ready until the anonymized experiment package exists and remaining unresolved items are closed or accepted as explicit limitations.

---

## Reviewer 1 — Novelty and related work

### Criticisms

1. **“Acc ≠ consistency is already known (SetCons / LogicVault).”**  
   *Response / change:* Related work now states explicitly that Acc–consistency separation is **not** claimed as generally new; residual is the evaluation object (persistent memory over evolving multi-entity gold worlds with world-history-derived constraints). Appendix Table `tab:closest` keeps Y/P/N contrast.  
   *Residual risk:* Incremental novelty remains a poster-track pressure point.

2. **“No general theory; why ICLR?”**  
   *Response / change:* Intro/conclusion forbid general memory/reasoning theory claims; contributions are formal Acc/Φ/BCR/Gapq separation, benchmark, and controlled demonstration.  
   *Unresolved:* Venue fit still depends on reviewer taste for diagnostic benchmarks.

3. **“Novelty underspecified vs exact-match / temporal / multi-hop / state-tracking / long-context.”**  
   *Response / change:* Intro “What is new (and what is not)” lists four concrete contributions and negatives. Object section defines why BCR ≠ Acc / EM / pairwise consistency.

---

## Reviewer 2 — Empirical validity and synthetic scope

### Criticisms

1. **“Synthetic toy; no external validity.”**  
   *Response / change:* New §“Why a synthetic generator is necessary”; threats table distinguishes what is/isn’t threatened; conclusion limits claims to tested symbolic setting.  
   *Unresolved limitation:* External validity **not** established; no human/real-world validation.

2. **“B3 seed sweep looks like replication but outcomes are identical.”**  
   *Response / change:* Narrowed claim: identical B3 Acc/BCR across seeds 100–105 is **not** independent replication; B3 seed sweep is a controlled diagnostic with limited diversity. Retrieval-budget NEW table used instead of fake seed diversity.  
   *Unresolved:* No structurally different alternate generator transfer run (blocked / deferred); retrieval-budget is the labelled NEW perturbation.

3. **“Only a 3B Qwen reader; BCR=0 is a model failure, not a memory finding.”**  
   *Response / change:* Model-scale robustness stated as **not** established in abstract, systems, results, coverage table, and appendix pre-registered plan. Gold H4 sanity Acc=BCR=1 separates metric soundness from reader failure.  
   *Unresolved:* Stronger reader not run (mlx_lm / disk). Pre-registered plan only.

4. **“Frozen vs NEW mixing.”**  
   *Response / change:* Every primary table labelled Frozen vs Labelled NEW; results open with never-pooled statement; Option A numbers unchanged.

---

## Reviewer 3 — Clarity, metrics, reproducibility

### Criticisms

1. **“BCR recoverable from Acc / just EM.”**  
   *Response / change:* Formal Acc, Φ, BCR, Gapq; proposition with minimal Acc-equal BCR-unequal construction; frozen B2 vs B3-k3 identical Acc different BCR; practical Acc-only mis-ranking example.

2. **“Reproducibility incomplete.”**  
   *Response / change:* Reproducibility statement + appendix protocol + stronger-reader plan; anonymity clean (no `/Users/`, author names, planning paths).  
   *Unresolved (blocks submission-ready):* Research tree `experiments/worldconsistmem/` empty; anonymized zip from `~/worldconsistmem-experiments/` **not** packaged into submission materials. Checksums/manifest for freeze must ship with OpenReview supplement.

3. **“Missing CIs / n / visuals.”**  
   *Response / change:* World-level CIs on BCR/CSR in symbolic/Qwen tables; sample sizes in captions; Acc vs BCR figure; Gapq in tables (corruption, symbolic, ablations, budget). Per-tier figure in appendix.  
   *Residual:* No dedicated Gapq-ablation bar chart (Gapq columns in `tab:ablations` / `tab:budget` used instead).

4. **“Reader protocol underspecified.”**  
   *Response / change:* Parameter count, prompting, context/evidence pack, decoding, runs, hardware documented in systems + appendix.

---

## Checklist vs user gate

| Gate | Status |
|------|--------|
| Novelty claim explicit | Yes (intro + related) |
| BCR formally ≠ Acc / existing metrics | Yes (object + proposition + empirical twin Acc) |
| B3 seed limitation honest | Yes (narrowed; not replication) |
| Stronger-reader limitation visible | Yes (prominent; pre-registered plan) |
| Frozen vs NEW unambiguous | Yes |
| Reproducibility package complete + anonymized | **No** — package still pending |
| Final PDF + supplement internally consistent | PDF rebuilt; supplement package incomplete |

---

## Subjective poster odds (unchanged band)

~35–50% poster: stronger Acc–BCR story and honest limitations help; synthetic scope + single 3B reader + incremental novelty vs SetCons/LogicVault still dominate reject risk.

---

## Changed files (this revision pass)

- `submission/latex/sec_intro.tex`, `sec_related.tex`, `sec_object.tex`, `sec_benchmark.tex`, `sec_metrics.tex` (prior)
- `submission/latex/sec_systems.tex`, `sec_results.tex`, `sec_failures.tex`, `sec_discussion.tex`, `sec_conclusion.tex`, `sec_appendix.tex`, `worldconsistmem.tex`
- `submission/latex/worldconsistmem.pdf`, `submission/worldconsistmem.pdf`
- This report: `planning/iclr-hostile-reviewer-simulation-v3.md`
