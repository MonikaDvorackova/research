---
id: pub-03-introduction-locked-skeleton
title: "Introduction locked skeleton — WorldConsistMem"
type: research-notes
status: skeleton
created: 2026-08-04
updated: 2026-08-04
---

# Introduction — locked skeleton (not final prose)

Lead with evaluation gap, **not** five-layer architecture.

## Paragraph 1 — Answer-by-answer evaluation

- Long-term memory systems for assistants/agents are usually scored **query by query** (accuracy, ability Acc, retrieval fitness).  
- Cite LTM line with `TODO(cite):` placeholders.  
- Claim: this leaves open whether answers over one persistent world cohere.

## Paragraph 2 — Answers are not independent

- Queries about the same evolving world share entities, validity intervals, transitions, and provenance.  
- Individually plausible answers can still violate joint constraints (e.g., correct current and historical CEOs with an impossible transition).

## Paragraph 3 — Missing dimension

- Need: evaluate **jointly coherent world-model answers**, not only Acc.  
- Distinguish from logical multi-query consistency (`TODO(cite):` SetCons/LogicVault): those target SAT/case-file coherence; we target **memory systems** over **evolving multi-entity gold worlds**.

## Paragraph 4 — WorldConsistMem

- Dependent query bundles; one shared gold history; machine-checkable constraints \(\mathcal{C}\); BCR (strict) and CSR (partial).  
- Benchmark + methodology paper.

## Paragraph 5 — Contributions (exact classes)

1. Evaluation methodology (bundles + \(\Phi\)).  
2. WorldConsistMem benchmark (scale: 102 worlds / 1,088 bundles / 7,140 queries).  
3. Metrics: BCR, CSR, ConsAcc, gaps, family diagnostics.  
4. Empirical analysis: corruption, symbolic, Qwen—Acc ≠ consistency; BCR may floor while CSR remains diagnostic.  
5. Reference systems (including structured hierarchical baseline) for evaluation, **not** architecture superiority.

## Paragraph 6 — Preview of findings (optional, one sentence)

- Symbolic: Acc–BCR gaps persist; compact flat can match or beat structured baseline under matched budgets.  
- Qwen: Acc up to ~0.185 with BCR=0; B4 highest CSR; no architecture consistency advantage.

## Explicitly do **not** put in Intro

- Five-layer marketing; H0 wins; “first consistency benchmark”; SOTA; real-world generality.
