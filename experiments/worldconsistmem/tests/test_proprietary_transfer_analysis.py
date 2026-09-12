"""Tests for proprietary-reader transfer analysis (no API; no Option A writes)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from worldconsistmem.proprietary_transfer_analysis import (
    ANALYSIS_DIR,
    BOOTSTRAP_N,
    BOOTSTRAP_SEED,
    OPTION_A_HASHES,
    PILOT_DIR,
    PRIMARY_REPORT_EXPECTED_SHA,
    bundle_bootstrap_acc,
    clopper_pearson_zero_success,
    load_jsonl,
    run_analysis,
    sha256_file,
    verify_primary_provenance,
)

ROOT = Path(__file__).resolve().parents[1]


def test_primary_report_hash():
    assert sha256_file(PILOT_DIR / "GPT41_MINI_PRIMARY_REPORT.json") == PRIMARY_REPORT_EXPECTED_SHA


def test_provenance_ok():
    prov = verify_primary_provenance()
    assert prov["all_ok"] is True
    assert prov["malformed_n"] == 6
    assert prov["malformed_all_completion_tokens_48"] is True
    assert prov["manifest_unique_q"] == 149
    assert prov["manifest_bundles"] == 22


def test_option_a_untouched():
    for rel, expect in OPTION_A_HASHES.items():
        assert sha256_file(ROOT / rel) == expect


def test_clopper_pearson_zero():
    ci = clopper_pearson_zero_success(22)
    assert ci["lo"] == 0.0
    assert ci["k"] == 0.0
    assert ci["n"] == 22.0
    # one-sided upper for n=22, alpha=0.05: 1 - 0.05**(1/22) ≈ 0.127
    assert 0.12 < ci["one_sided_upper_95"] < 0.14
    assert ci["hi"] > ci["one_sided_upper_95"]


def test_bootstrap_deterministic():
    class M:
        def __init__(self, acc, nq):
            self.mean_query_accuracy = acc
            self.n_queries = nq

    ms = [M(0.5, 6), M(0.25, 8), M(1.0, 4)]
    a = bundle_bootstrap_acc(ms, n_boot=200, seed=BOOTSTRAP_SEED)
    b = bundle_bootstrap_acc(ms, n_boot=200, seed=BOOTSTRAP_SEED)
    assert a == b
    assert a["n_boot"] == 200


def test_run_analysis_end_to_end():
    # Ensure primary artefacts unchanged before/after
    before = {name: sha256_file(PILOT_DIR / name) for name in json.loads((PILOT_DIR / "GPT41_MINI_PRIMARY_REPORT.json").read_text())["files_sha256"]}
    result = run_analysis()
    after = {name: sha256_file(PILOT_DIR / name) for name in before}
    assert before == after
    gpt = result["gpt41_mini"]
    assert gpt["n_queries"] == 149
    assert gpt["n_bundles"] == 22
    assert gpt["mean_acc"] == 0.4563758389261745
    assert gpt["bcr"] == 0.0
    assert gpt["n_malformed"] == 6
    assert gpt["n_abstain"] == 41
    assert gpt["acc_ci95_bundle_bootstrap"]["n_boot"] == float(BOOTSTRAP_N)
    assert gpt["acc_ci95_bundle_bootstrap"]["seed"] == float(BOOTSTRAP_SEED)
    assert result["matched_qwen_meta"]["available"] is True
    assert result["matched_qwen"]["n_queries"] == 149
    assert result["matched_qwen"]["n_bundles"] == 22
    assert (ANALYSIS_DIR / "TRANSFER_ANALYSIS.json").exists()
    # Option A still unchanged
    for rel, expect in OPTION_A_HASHES.items():
        assert sha256_file(ROOT / rel) == expect


def test_malformed_truncation_policy_in_cache():
    cache = load_jsonl(PILOT_DIR / "api_cache.jsonl")
    mal = [r for r in cache if r.get("status") == "malformed"]
    assert len(mal) == 6
    assert all(r.get("completion_tokens") == 48 for r in mal)
