# ICLR Acceptance Risk Report v3

Date: 2026-09-07  
Depends on: hostile-reviewer revision + `iclr-hostile-reviewer-simulation-v3.md`

## Verdict

**Not submission-ready.** Manuscript positioning and honesty improved; reproducibility package and stronger-reader evidence remain open.

## What improved

- Formal Acc / Φ / BCR / Gapq + identical-Acc≠BCR proposition and frozen B2/B3-k3 example
- Novelty residual stated against Acc / temporal / multi-hop / state-tracking / SetCons
- Synthetic necessity subsection + threats with threaten / does-not-threaten
- B3 seed claim narrowed (not replication); NEW retrieval-budget table
- Reader protocol + pre-registered stronger-reader plan; model-scale not claimed
- Conservative conclusion; Frozen vs NEW labels

## Remaining blockers

1. Anonymized experiment/code/freeze package for OpenReview (research tree experiments path empty)
2. No stronger LLM reader result (explicit limitation only)
3. No alternate-generator transfer (retrieval-budget used as NEW perturbation instead)
4. Incremental novelty vs cross-query logical consistency literature still a reject vector

## Risk bands

| Risk | Level | Note |
|------|-------|------|
| Novelty incremental | High | Mitigated by object residual; not eliminated |
| Synthetic scope | High | Honest; still ICLR-hostile |
| Single 3B reader | High | Visible limitation |
| B3 seed diversity | Medium | Honestly narrowed |
| Option A integrity | Low | Frozen; not mutated |
| Anonymity in PDF | Low | Clean on last build |

## Poster odds

35–50% (diagnostic benchmark with clear Acc–BCR story; weak ecological + model-scale evidence).
