# ICLR Final Readiness — WorldConsistMem (post GPT-4.1 mini transfer)

Date: 2026-09-11  
Verdict: **Poster-acceptance case materially strengthened** by a proprietary-reader transfer check with meaningful Acc and BCR=0/22. Still not a frontier multi-model oral case.

## Explicit answers

1. **Does transfer demonstrate Acc–BCR divergence?** Yes on the frozen stratified H0 subset: GPT-4.1 mini Acc=45.6% with BCR=0/22 (bundle-bootstrap Acc CI [40.4%, 50.7%]).
2. **Persists for a stronger/proprietary reader?** Yes for this one proprietary reader (non-frontier). Exact matched Qwen subset Acc=20.1%, BCR=0/22.
3. **Parser failure explain zero BCR?** No for GPT-4.1 mini: 102/149 valid non-abstaining outputs; 6 truncations counted incorrect; Acc still 45.6%.
4. **Conjunction alone?** Residual interpretation still rests on frozen symbolic Accⁿ; transfer BCR=0/22 with Acc≈0.46 is below naïve p̄⁴≈0.043, but n=22 limits strong residual claims.
5. **Strongest remaining rejection risk?** Limited transfer n (22 bundles); single proprietary non-frontier reader; synthetic scope; system-level confound (retrieval+prompt+model+parser).

## Formal compliance (this compile)

| Gate | Status |
|------|--------|
| Main text ≤9 | Pass (Conclusion + AI Use p.7; Appendix ~p.9) |
| AI Use Statement | Pass |
| Anonymous | Pass |
| Unresolved cites | 0 |
| Option A hashes | Unchanged |
| PDF SHA-256 | `6caff86647f72a334a34cbbd1ea92763972aa09a88828ef261ab9fcba1161bf2` |
| Primary report SHA-256 | `e3ac10ae4b6395966f594bbc280ebaf2a2e996e29003d6b0b7e429ffd4f4e06d` |
| Supplement ZIP SHA-256 | `eab6ce7cdf2bc9a2caa3e772398f7212132637063b9f686a1a8444a26414bfbc` |

## Assessments

1. **Formal submission compliance:** Pass for ICLR 2027 page/AI/anonymity gates on current PDF.
2. **Reproducibility:** Strong for primary pilot artefacts + analysis utilities; `api_cache.jsonl` excluded from public ZIP with hash retained.
3. **Empirical strength:** Materially improved vs Qwen-only low-Acc floor; matched-subset comparison available.
4. **Scientific remaining risks:** n=22; non-frontier single proprietary reader; synthetic worlds; not ecological validity.
