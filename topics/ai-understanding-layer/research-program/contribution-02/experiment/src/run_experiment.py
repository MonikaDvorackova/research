"""Experiment orchestrator (PHASE 3). Runs the regime-appropriate
deterministic reconstruction procedure for every case x regime combination,
scores each result against ground truth, and writes raw, machine-readable
output. This script performs no analysis and no interpretation -- that is
PHASE 4/4A, done separately against the raw output this script produces.

Usage:
    python3 -m src.run_experiment            # writes results/raw_results.jsonl
    python3 -m src.run_experiment --manifest  # writes only the pre-execution
                                               # case manifest (no reconstruction
                                               # or scoring is run in this mode)
"""

from __future__ import annotations

import csv
import dataclasses
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from .cases import all_worlds
from .domain import UNDETERMINED
from .reconstruction import reconstruct
from .regimes import ALL_REGIMES, verify_b_c_equivalence, view_for
from .scoring import aggregate_by_category, score_case

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"


def _json_default(obj: Any):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    raise TypeError(f"not JSON serializable: {type(obj)}")


def case_manifest() -> list[dict]:
    """Non-result, structural metadata about every case: what exists,
    not what the experiment finds. Used for the pre-execution freeze
    (PHASE 2) -- generating this requires no reconstruction and no
    scoring, only the case definitions themselves."""
    rows = []
    for world in all_worlds():
        rows.append({
            "case_id": world.case_id,
            "category": world.category,
            "decision_id": world.decision_id,
            "description": world.description,
            "t0": world.t0.isoformat(),
            "query_time": world.query_time.isoformat(),
            "requester_id": world.requester_id,
            "n_policy_history_rows": len(world.policy_history),
            "n_authority_history_rows": len(world.authority_history),
            "n_model_history_rows": len(world.model_history),
            "n_watchlist_history_rows": len(world.watchlist_history),
        })
    return rows


def run() -> list[dict]:
    """Run every case x regime combination, verify the B/C equivalence
    invariant per world first (halting the run if it ever fails), and
    return the raw per-case-per-regime result rows."""
    rows = []
    for world in all_worlds():
        verify_b_c_equivalence(world)  # PHASE 1B: must hold before scoring
        for regime in ALL_REGIMES:
            view = view_for(world, regime)
            answers = reconstruct(regime, view)
            score = score_case(world, regime, answers)
            rows.append({
                "case_id": world.case_id,
                "category": world.category,
                "decision_id": world.decision_id,
                "regime": regime,
                "answers": dataclasses.asdict(answers),
                "score": dataclasses.asdict(score),
            })
    return rows


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if "--manifest" in sys.argv:
        manifest = case_manifest()
        out = RESULTS_DIR.parent / "PRE-EXECUTION-case-manifest.json"
        out.write_text(json.dumps(manifest, indent=2, default=_json_default) + "\n")
        print(f"wrote {out} ({len(manifest)} rows)")
        return

    rows = run()

    raw_path = RESULTS_DIR / "raw_results.jsonl"
    with raw_path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, default=_json_default) + "\n")
    print(f"wrote {raw_path} ({len(rows)} rows)")

    scores = []
    from .scoring import CaseScore
    for row in rows:
        scores.append(CaseScore(**row["score"]))
    summaries = aggregate_by_category(scores)

    agg_path = RESULTS_DIR / "aggregate_by_category.csv"
    with agg_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "regime", "n", "mean_aia", "tc_rate", "mean_ac", "mean_jc", "mean_fhc_rate"])
        for s in summaries:
            writer.writerow([s.category, s.regime, s.n, f"{s.mean_aia:.4f}", f"{s.tc_rate:.4f}",
                              f"{s.mean_ac:.4f}", f"{s.mean_jc:.4f}", f"{s.mean_fhc_rate:.4f}"])
    print(f"wrote {agg_path} ({len(summaries)} rows)")

    case_path = RESULTS_DIR / "case_level_results.csv"
    with case_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["case_id", "category", "decision_id", "regime", "aia", "tc", "ac", "jc", "fhc_rate"])
        for row in rows:
            s = row["score"]
            writer.writerow([row["case_id"], row["category"], row["decision_id"], row["regime"],
                              f"{s['aia']:.4f}", s["tc"], s["ac"], f"{s['jc']:.4f}", f"{s['fhc_rate']:.4f}"])
    print(f"wrote {case_path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
