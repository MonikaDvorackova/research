# ICLR Acceptance Action Plan — WorldConsistMem

Date: 2026-09-09 (honesty update)  
Goal: keep confirmatory evidence correctly scoped; close strongest remaining *empirical* objection only with runnable evidence.

## Environment inventory (authoritative)

| Resource | Status |
|----------|--------|
| Frozen Option A | Available; must not mutate |
| Symbolic preds (B1–B5, H0) | Available full scale |
| Qwen2.5-3B H4 preds + raw cache | Available (run2) |
| Phi-3.5-mini weights / mlx | **Unavailable** |
| Disk free | ~5 GB (still insufficient for 7B+ download) |
| API keys | **Not set** |
| Ollama | Not installed |

**Authorization rule:** no new API spend; no large weight downloads without explicit approval.

## Status after honesty pass

| Risk | Status | Correct interpretation |
|------|--------|------------------------|
| R1 Narrow reader | Parser DONE; Phi BLOCKED | Parser ≠ semantic-memory proof when Acc is low |
| R2 Synthetic-only | NL n=36 DONE | **Difficulty/validity probe**, not Acc–BCR confirmation |
| R3 Retrieval/length | Accⁿ DONE | Residual Accⁿ−BCR on B4/H0 supports beyond-conjunction |
| R4 Scoring artefact | 3 parsers DONE | BCR=0 stable; Acc still low |
| R6 Conjunction | DONE symbolic; DONE transfer diagnostic | Transfer last-event BCR=0 ≈ expected under low p |
| R7 Stronger LLM | BLOCKED | Paid API estimate recorded; not executed |

## Paid API estimate (stopped before execution)

- Model: `openai/gpt-4o-mini` (example)
- Calls: 144 (36×4)
- Est. tokens: ~65k in / ~6k out
- Est. cost: ~$0.05
- Est. runtime: ~10 min

## Highest-impact next experiment (if authorized)

Run one meaningful-Acc NL LLM on the **frozen** 36 scenarios without altering gold/scorer/primary prompt after seeing results. Store under `results/confirmatory/naturalistic_transfer/readers/<model_id>/`.

## Acceptance posture

- **Poster-level case:** frozen symbolic Acc–BCR + Accⁿ residual + Acc-tied B2/B3 + honest confirmatory controls.  
- **Not yet:** strong oral / “transfer confirms central claim” without a meaningful-Acc NL/stronger reader.
