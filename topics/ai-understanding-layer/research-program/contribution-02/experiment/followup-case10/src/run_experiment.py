"""Follow-up orchestrator. Mirrors ../../src/run_experiment.py's shape."""

from __future__ import annotations

import csv
import dataclasses
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from .cases import all_worlds
from .reconstruction import reconstruct
from .regimes import ALL_REGIMES, verify_b_c_equivalence, view_for
from .scoring import score_case

RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"


def _json_default(obj: Any):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    raise TypeError(f"not JSON serializable: {type(obj)}")


def case_manifest() -> list[dict]:
    rows = []
    for world in all_worlds():
        rows.append({
            "case_id": world.case_id,
            "decision_id": world.decision_id,
            "description": world.description,
            "true_t0": world.true_t0.isoformat(),
            "observed_t0": world.event_trace.observed_t0.isoformat(),
            "ambiguous_dimensions": list(world.ground_truth.ambiguous_dimensions),
            "n_policy_history_rows": len(world.policy_history),
            "n_authority_history_rows": len(world.authority_history),
            "n_model_history_rows": len(world.model_history),
            "has_causal_consumption_event": world.event_trace.causal_consumption_event is not None,
        })
    return rows


def run() -> list[dict]:
    rows = []
    for world in all_worlds():
        verify_b_c_equivalence(world)
        for regime in ALL_REGIMES:
            view = view_for(world, regime)
            answers = reconstruct(regime, view)
            score = score_case(world, regime, answers)
            rows.append({
                "case_id": world.case_id,
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

    case_path = RESULTS_DIR / "case_level_results.csv"
    with case_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "case_id", "decision_id", "regime", "policy_class", "authority_class", "model_class",
            "tc", "urr", "adr", "ac", "fhc_rate",
        ])
        for row in rows:
            s = row["score"]
            writer.writerow([
                row["case_id"], row["decision_id"], row["regime"],
                s["policy_class"], s["authority_class"], s["model_class"],
                s["tc"], f"{s['urr']:.4f}",
                "" if s["adr"] is None else f"{s['adr']:.4f}",
                s["ac"], f"{s['fhc_rate']:.4f}",
            ])
    print(f"wrote {case_path} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
