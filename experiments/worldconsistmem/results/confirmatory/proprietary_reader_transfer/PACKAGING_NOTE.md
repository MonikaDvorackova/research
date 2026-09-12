# Proprietary-reader transfer — packaging note (anonymized)

## Included in the public reproducibility supplement

- `results/new/stronger_reader_pilot/GPT41_MINI_PRIMARY_REPORT.json` (+ `.sha256`)
- `PILOT_CONFIG.json`, `COST_ESTIMATE.json`, `sample_manifest.jsonl`
- `predictions.jsonl`, `metrics.json`, `spend_ledger.jsonl`
- `results/confirmatory/proprietary_reader_transfer/` (analysis JSON, CIs, family breakdowns, matched Qwen extract)
- `src/worldconsistmem/proprietary_transfer_analysis.py`
- `scripts/run_proprietary_transfer_analysis.py`
- `tests/test_proprietary_transfer_analysis.py`

## Excluded from the public ZIP (integrity retained)

- `results/new/stronger_reader_pilot/api_cache.jsonl` (raw model strings; not required to recompute Acc/BCR from `predictions.jsonl`)

SHA-256 of excluded cache (from primary report):  
`89ce7069b8cfb45922caea662b304e4445335a96c2ad9f23dc88409d82bdb330`

Primary report SHA-256:  
`e3ac10ae4b6395966f594bbc280ebaf2a2e996e29003d6b0b7e429ffd4f4e06d`

## Not Option A

These artefacts are labelled NEW / confirmatory and must not be pooled with frozen Option A tables.
