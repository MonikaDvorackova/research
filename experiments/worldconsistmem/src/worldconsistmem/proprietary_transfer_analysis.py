"""Deterministic analysis for the proprietary-reader transfer check (NEW).

Does not mutate primary GPT-4.1 mini artefacts or Option A.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Optional

from .baselines.interface import ABSTAIN_TOKEN
from .generate import GeneratedWorld
from .metrics import aggregate_metrics, answers_equal, evaluate_bundle
from .models import (
    AnswerSchema,
    ConstraintFamily,
    Prediction,
    Query,
    QueryBundle,
    QueryFamily,
)
from .scaled_generate import generate_scaled_world

ROOT = Path(__file__).resolve().parents[2]
PILOT_DIR = ROOT / "results" / "new" / "stronger_reader_pilot"
ANALYSIS_DIR = ROOT / "results" / "confirmatory" / "proprietary_reader_transfer"

OPTION_A_HASHES = {
    "data/scaled/manifest.json": "37aa8604c3e6d87691332f66d2f7c0ab93578f2fe468bc29f7e8217c1675af3f",
    "results/scaled/system_results.csv": "eb5bd5fa87496586bd830e5f685b9950e119f9fd0ac491194b3f003343f9a2a8",
}

PRIMARY_REPORT_EXPECTED_SHA = "e3ac10ae4b6395966f594bbc280ebaf2a2e996e29003d6b0b7e429ffd4f4e06d"
BOOTSTRAP_SEED = 20260911
BOOTSTRAP_N = 10000
QWEN_PRED_PATH = (
    ROOT
    / "results"
    / "scaled"
    / "run2"
    / "run2_predictions"
    / "Qwen2.5-3B-Instruct-4bit__H0_ltkm_cap150_ret8.jsonl"
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open() as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def rebuild_query(q: dict[str, Any]) -> Query:
    return Query(
        query_id=q["query_id"],
        bundle_id=q["bundle_id"],
        family=QueryFamily(q["family"]),
        text=q["text"],
        structured=q["structured"],
        target_time=q.get("target_time"),
        target_interval=None,
        gold_answer=q["gold_answer"],
        answer_schema=AnswerSchema(q["answer_schema"]),
        applicable_constraints=[ConstraintFamily(c) for c in q["applicable_constraints"]],
        supporting_event_ids=q["supporting_event_ids"],
        supporting_provenance_ids=q["supporting_provenance_ids"],
        metadata=q.get("metadata") or {},
    )


def rebuild_bundle(row: dict[str, Any]) -> QueryBundle:
    return QueryBundle(
        bundle_id=row["bundle_id"],
        world_id=row["world_id"],
        focal_entities=row["focal_entities"],
        queries=[rebuild_query(q) for q in row["queries"]],
        description=row.get("description", ""),
        metadata=row.get("metadata") or {},
    )


def load_h4_bundles() -> dict[str, dict[str, Any]]:
    wi = json.loads((ROOT / "data" / "scaled" / "world_index.json").read_text())
    by_tier: dict[str, list] = defaultdict(list)
    for r in wi:
        by_tier[r["tier"]].append(r)
    h4 = set()
    for t in ("small", "medium", "large"):
        for r in by_tier[t][:6]:
            h4.add(r["world_id"])
    out = {}
    with (ROOT / "data" / "scaled" / "bundles.jsonl").open() as f:
        for line in f:
            b = json.loads(line)
            if b["world_id"] in h4:
                out[b["bundle_id"]] = b
    return out


def load_worlds(world_ids: set[str]) -> dict[str, GeneratedWorld]:
    wi = {r["world_id"]: r for r in json.loads((ROOT / "data" / "scaled" / "world_index.json").read_text())}
    worlds = {}
    for wid in world_ids:
        row = wi[wid]
        worlds[wid] = generate_scaled_world(int(row["seed"]), int(wid.split("_")[-1]), tier=row["tier"])
    return worlds


@dataclass
class ReaderScore:
    reader_id: str
    n_queries: int
    n_bundles: int
    mean_acc: float
    bcr: float
    gap_acc_bcr: float
    n_abstain: int
    n_malformed: int
    n_ok: int
    acc_ci95_bundle_bootstrap: dict[str, float]
    bcr_point: str
    bcr_ci95_clopper_pearson: dict[str, float]
    family_breakdown: dict[str, dict[str, Any]]
    source_path: str
    source_sha256: str


def clopper_pearson_zero_success(n: int, alpha: float = 0.05) -> dict[str, float]:
    """Exact Clopper–Pearson 95% interval for k=0 successes in n trials.

    For k=0: lo = 0, hi = 1 - (alpha/2)^(1/n) (two-sided).
    Also report one-sided 95% upper bound: 1 - alpha^(1/n).
    """
    if n <= 0:
        return {"lo": 0.0, "hi": 1.0, "one_sided_upper_95": 1.0, "n": 0, "k": 0}
    hi = 1.0 - (alpha / 2.0) ** (1.0 / n)
    one_sided = 1.0 - alpha ** (1.0 / n)
    return {
        "lo": 0.0,
        "hi": hi,
        "one_sided_upper_95": one_sided,
        "n": float(n),
        "k": 0.0,
        "method": "clopper_pearson_exact_zero_success",
    }


def bundle_bootstrap_acc(
    bundle_metrics: list,
    n_boot: int = BOOTSTRAP_N,
    seed: int = BOOTSTRAP_SEED,
    alpha: float = 0.05,
) -> dict[str, float]:
    """Resample complete bundles with replacement; recompute query-weighted Acc."""
    rng = random.Random(seed)
    n = len(bundle_metrics)
    if n == 0:
        return {"mean": 0.0, "lo": 0.0, "hi": 0.0, "n_bundles": 0, "n_boot": 0}

    def acc_of(sample) -> float:
        n_q = sum(m.n_queries for m in sample)
        if n_q == 0:
            return 0.0
        return sum(m.mean_query_accuracy * m.n_queries for m in sample) / n_q

    point = acc_of(bundle_metrics)
    boots = []
    for _ in range(n_boot):
        sample = [bundle_metrics[rng.randrange(n)] for _ in range(n)]
        boots.append(acc_of(sample))
    boots.sort()
    lo_i = int(alpha / 2 * n_boot)
    hi_i = int((1 - alpha / 2) * n_boot) - 1
    return {
        "mean": point,
        "lo": boots[max(0, lo_i)],
        "hi": boots[min(n_boot - 1, hi_i)],
        "n_bundles": float(n),
        "n_boot": float(n_boot),
        "seed": float(seed),
        "method": "bundle_resample_with_replacement_query_weighted_acc",
    }


def _status_counts_from_rows(
    rows_by_qid: dict[str, dict[str, Any]], query_ids: list[str], kind: str
) -> tuple[int, int, int]:
    n_ok = n_abs = n_mal = 0
    for qid in query_ids:
        r = rows_by_qid[qid]
        if kind == "gpt":
            st = r.get("status")
        else:
            st = (r.get("metadata") or {}).get("status")
            if st is None:
                if r.get("predicted_answer") == ABSTAIN_TOKEN:
                    st = "abstain"
                elif (r.get("metadata") or {}).get("malformed"):
                    st = "malformed"
                else:
                    st = "ok"
        if st == "malformed":
            n_mal += 1
        elif st == "abstain":
            n_abs += 1
        else:
            n_ok += 1
    return n_ok, n_abs, n_mal


def family_breakdown(
    bundles: dict[str, dict[str, Any]],
    selected_bids: list[str],
    pred_by: dict[str, dict[str, Any]],
    status_kind: str,
) -> dict[str, dict[str, Any]]:
    fam: dict[str, dict[str, Any]] = {}
    for bid in selected_bids:
        for q in bundles[bid]["queries"]:
            f = q["family"]
            slot = fam.setdefault(
                f,
                {"n": 0, "correct": 0, "abstentions": 0, "malformed": 0, "valid_outputs": 0},
            )
            slot["n"] += 1
            pr = pred_by[q["query_id"]]
            if status_kind == "gpt":
                st = pr.get("status")
            else:
                st = (pr.get("metadata") or {}).get("status") or (
                    "abstain" if pr.get("predicted_answer") == ABSTAIN_TOKEN else "ok"
                )
                if (pr.get("metadata") or {}).get("malformed"):
                    st = "malformed"
            if st == "abstain":
                slot["abstentions"] += 1
            elif st == "malformed":
                slot["malformed"] += 1
            else:
                slot["valid_outputs"] += 1
            ans = pr.get("predicted_answer")
            if answers_equal(ans, q["gold_answer"]):
                slot["correct"] += 1
    for f, slot in fam.items():
        n = slot["n"]
        slot["accuracy"] = slot["correct"] / n if n else 0.0
    return dict(sorted(fam.items()))


def score_reader(
    reader_id: str,
    pred_rows: list[dict[str, Any]],
    manifest: list[dict[str, Any]],
    bundles: dict[str, dict[str, Any]],
    worlds: dict[str, GeneratedWorld],
    source_path: Path,
    status_kind: str,
) -> ReaderScore:
    pred_by = {r["query_id"]: r for r in pred_rows}
    qids = [m["query_id"] for m in manifest]
    bids = sorted({m["bundle_id"] for m in manifest})
    missing = [q for q in qids if q not in pred_by]
    if missing:
        raise ValueError(f"{reader_id}: missing {len(missing)} predictions, e.g. {missing[:3]}")

    bms = []
    scored_bundles = []
    for bid in bids:
        brow = bundles[bid]
        bobj = rebuild_bundle(brow)
        preds = []
        for q in bobj.queries:
            pr = pred_by[q.query_id]
            preds.append(
                Prediction(
                    bundle_id=bid,
                    query_id=q.query_id,
                    predicted_answer=pr.get("predicted_answer"),
                    predicted_provenance=pr.get("predicted_provenance"),
                    system_id=str(pr.get("system_id") or reader_id),
                    run_id="proprietary_transfer_analysis",
                )
            )
        bms.append(evaluate_bundle(worlds[brow["world_id"]], bobj, preds))
        scored_bundles.append(bobj)

    agg = aggregate_metrics(bms, scored_bundles)
    n_ok, n_abs, n_mal = _status_counts_from_rows(pred_by, qids, status_kind)
    n_consistent = sum(1 for m in bms if m.consistent)
    if n_consistent != 0:
        # Still compute CP around observed rate via beta relation for general k;
        # for this study BCR is 0 — use zero-success helper.
        bcr_ci = {
            "lo": float("nan"),
            "hi": float("nan"),
            "note": "non_zero_bcr_general_cp_not_implemented_in_stdlib_path",
            "n": float(len(bids)),
            "k": float(n_consistent),
        }
    else:
        bcr_ci = clopper_pearson_zero_success(len(bids))

    return ReaderScore(
        reader_id=reader_id,
        n_queries=len(qids),
        n_bundles=len(bids),
        mean_acc=agg.mean_query_accuracy,
        bcr=agg.bcr,
        gap_acc_bcr=agg.gap_mean_acc_minus_bcr,
        n_abstain=n_abs,
        n_malformed=n_mal,
        n_ok=n_ok,
        acc_ci95_bundle_bootstrap=bundle_bootstrap_acc(bms),
        bcr_point=f"{n_consistent}/{len(bids)}",
        bcr_ci95_clopper_pearson=bcr_ci,
        family_breakdown=family_breakdown(bundles, bids, pred_by, status_kind),
        source_path=str(source_path.relative_to(ROOT)),
        source_sha256=sha256_file(source_path),
    )


def verify_primary_provenance() -> dict[str, Any]:
    report_path = PILOT_DIR / "GPT41_MINI_PRIMARY_REPORT.json"
    sidecar = (PILOT_DIR / "GPT41_MINI_PRIMARY_REPORT.sha256").read_text().strip().split()[0]
    report_sha = sha256_file(report_path)
    report = json.loads(report_path.read_text())
    file_checks = {}
    for name, expect in report["files_sha256"].items():
        got = sha256_file(PILOT_DIR / name)
        file_checks[name] = {"ok": got == expect, "sha256": got}
    option_a = {}
    for rel, expect in OPTION_A_HASHES.items():
        got = sha256_file(ROOT / rel)
        option_a[rel] = {"ok": got == expect, "sha256": got}

    man = load_jsonl(PILOT_DIR / "sample_manifest.jsonl")
    cache = load_jsonl(PILOT_DIR / "api_cache.jsonl")
    preds = load_jsonl(PILOT_DIR / "predictions.jsonl")
    mal = [r for r in cache if r.get("status") == "malformed"]
    return {
        "report_sha256": report_sha,
        "sidecar_match": report_sha == sidecar,
        "matches_expected_user_sha": report_sha == PRIMARY_REPORT_EXPECTED_SHA,
        "file_checks": file_checks,
        "option_a": option_a,
        "manifest_n": len(man),
        "manifest_unique_q": len({m["query_id"] for m in man}),
        "manifest_bundles": len({m["bundle_id"] for m in man}),
        "cache_n": len(cache),
        "cache_unique_q": len({r["query_id"] for r in cache}),
        "preds_n": len(preds),
        "preds_set_eq_manifest": {r["query_id"] for r in preds} == {m["query_id"] for m in man},
        "malformed_n": len(mal),
        "malformed_all_completion_tokens_48": all(r.get("completion_tokens") == 48 for r in mal),
        "all_ok": (
            report_sha == sidecar == PRIMARY_REPORT_EXPECTED_SHA
            and all(v["ok"] for v in file_checks.values())
            and all(v["ok"] for v in option_a.values())
            and len(man) == 149
            and len({m["query_id"] for m in man}) == 149
            and len({m["bundle_id"] for m in man}) == 22
            and len(cache) == 149
            and len(preds) == 149
            and len(mal) == 6
            and all(r.get("completion_tokens") == 48 for r in mal)
        ),
    }


def extract_matched_qwen(manifest: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    need = {m["query_id"] for m in manifest}
    if not QWEN_PRED_PATH.exists():
        return [], {"available": False, "reason": f"missing {QWEN_PRED_PATH}", "checked": [str(QWEN_PRED_PATH)]}
    found = {}
    with QWEN_PRED_PATH.open() as f:
        for line in f:
            r = json.loads(line)
            qid = r.get("query_id")
            if qid in need:
                found[qid] = r
    missing = sorted(need - set(found))
    meta = {
        "available": len(missing) == 0,
        "source_path": str(QWEN_PRED_PATH.relative_to(ROOT)),
        "source_sha256": sha256_file(QWEN_PRED_PATH),
        "n_found": len(found),
        "n_needed": len(need),
        "missing_ids": missing,
        "checked": [str(QWEN_PRED_PATH.relative_to(ROOT))],
    }
    return [found[m["query_id"]] for m in manifest], meta


def run_analysis(out_dir: Path | None = None) -> dict[str, Any]:
    out = out_dir or ANALYSIS_DIR
    out.mkdir(parents=True, exist_ok=True)

    prov = verify_primary_provenance()
    if not prov["all_ok"]:
        raise RuntimeError(f"provenance failed: {json.dumps(prov, indent=2)}")

    manifest = load_jsonl(PILOT_DIR / "sample_manifest.jsonl")
    gpt_preds = load_jsonl(PILOT_DIR / "predictions.jsonl")
    bundles = load_h4_bundles()
    bids = sorted({m["bundle_id"] for m in manifest})
    # verify complete bundles
    for bid in bids:
        need = {q["query_id"] for q in bundles[bid]["queries"]}
        have = {m["query_id"] for m in manifest if m["bundle_id"] == bid}
        if need != have:
            raise RuntimeError(f"incomplete bundle {bid}")

    worlds = load_worlds({bundles[bid]["world_id"] for bid in bids})
    gpt = score_reader(
        "gpt-4.1-mini",
        gpt_preds,
        manifest,
        bundles,
        worlds,
        PILOT_DIR / "predictions.jsonl",
        status_kind="gpt",
    )

    qwen_rows, qwen_meta = extract_matched_qwen(manifest)
    result: dict[str, Any] = {
        "label": "NEW_proprietary_reader_transfer_analysis",
        "not_option_a": True,
        "provenance": prov,
        "model_requested_alias": "gpt-4.1-mini",
        "smoke_test_resolved_model": "gpt-4.1-mini-2025-04-14",
        "snapshot_note": (
            "Requested alias gpt-4.1-mini; independent smoke test resolved to "
            "gpt-4.1-mini-2025-04-14. Stored API cache rows record the requested alias, "
            "not resp['model']."
        ),
        "malformed_policy": "six truncated JSON outputs at completion_tokens==48 counted conservatively incorrect; no selective retry",
        "gpt41_mini": asdict(gpt),
        "matched_qwen": None,
        "matched_qwen_meta": qwen_meta,
    }

    if qwen_meta["available"]:
        # write extract without modifying source
        extract_path = out / "qwen_matched_subset_predictions.jsonl"
        with extract_path.open("w") as f:
            for r in qwen_rows:
                f.write(json.dumps(r, sort_keys=True) + "\n")
        qwen = score_reader(
            "Qwen2.5-3B-Instruct-4bit",
            qwen_rows,
            manifest,
            bundles,
            worlds,
            QWEN_PRED_PATH,
            status_kind="qwen",
        )
        result["matched_qwen"] = asdict(qwen)
        result["matched_qwen_extract_sha256"] = sha256_file(extract_path)
        result["matched_qwen_extract_path"] = str(extract_path.relative_to(ROOT))

    # write artefacts
    (out / "TRANSFER_ANALYSIS.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    (out / "family_breakdown_gpt41_mini.json").write_text(
        json.dumps(gpt.family_breakdown, indent=2, sort_keys=True) + "\n"
    )
    if result["matched_qwen"]:
        (out / "family_breakdown_qwen_matched.json").write_text(
            json.dumps(result["matched_qwen"]["family_breakdown"], indent=2, sort_keys=True) + "\n"
        )
    ci = {
        "gpt41_mini_acc_ci95": gpt.acc_ci95_bundle_bootstrap,
        "gpt41_mini_bcr_point": gpt.bcr_point,
        "gpt41_mini_bcr_ci95": gpt.bcr_ci95_clopper_pearson,
    }
    if result["matched_qwen"]:
        ci["qwen_matched_acc_ci95"] = result["matched_qwen"]["acc_ci95_bundle_bootstrap"]
        ci["qwen_matched_bcr_point"] = result["matched_qwen"]["bcr_point"]
        ci["qwen_matched_bcr_ci95"] = result["matched_qwen"]["bcr_ci95_clopper_pearson"]
    (out / "ci_report.json").write_text(json.dumps(ci, indent=2, sort_keys=True) + "\n")

    # integrity manifest for analysis outputs (not primary)
    lines = []
    for p in sorted(out.glob("*")):
        if p.is_file():
            lines.append(f"{sha256_file(p)}  {p.name}")
    (out / "MANIFEST.sha256").write_text("\n".join(lines) + "\n")
    return result


if __name__ == "__main__":
    print(json.dumps(run_analysis(), indent=2, sort_keys=True))
