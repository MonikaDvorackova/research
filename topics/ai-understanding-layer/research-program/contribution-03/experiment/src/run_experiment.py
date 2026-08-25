"""Orchestrator: runs every case under both regimes, writes raw
machine-readable results to results/. No interpretation happens here --
this script only executes the frozen procedure and records what
happened.
"""

from __future__ import annotations

import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cases import all_worlds
from src.reconstruction import reconstruct
from src.regimes import ALL_REGIMES, view_for, verify_t1_t2_local_equivalence
from src.scoring import aggregate, score_case

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")


def run() -> None:
    worlds = all_worlds()

    for world in worlds:
        verify_t1_t2_local_equivalence(world)

    case_rows = []
    edge_rows = []
    case_scores_by_regime = {r: [] for r in ALL_REGIMES}

    for world in worlds:
        for regime in ALL_REGIMES:
            records = view_for(world, regime)
            answers = reconstruct(regime, records)
            case_score = score_case(world, regime, answers)
            case_scores_by_regime[regime].append(case_score)

            case_rows.append({
                "case_id": case_score.case_id,
                "regime": case_score.regime,
                "local_decision_reconstruction": case_score.local_decision_reconstruction,
                "trajectory_identifiable": case_score.trajectory_identifiable,
                "n_dependent_edges": len(case_score.edge_classifications),
            })
            for ec in case_score.edge_classifications:
                edge_rows.append({
                    "case_id": case_score.case_id,
                    "regime": case_score.regime,
                    "decision_id": ec.decision_id,
                    "true_predecessor": ec.true_predecessor,
                    "reconstructed_status": ec.reconstructed_status,
                    "reconstructed_predecessor": ec.reconstructed_predecessor,
                    "classification": ec.classification,
                    "is_ambiguous_by_construction": ec.is_ambiguous_by_construction,
                })

    os.makedirs(RESULTS_DIR, exist_ok=True)

    with open(os.path.join(RESULTS_DIR, "case_level_results.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(case_rows[0].keys()))
        writer.writeheader()
        writer.writerows(case_rows)

    with open(os.path.join(RESULTS_DIR, "edge_level_results.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(edge_rows[0].keys()))
        writer.writeheader()
        writer.writerows(edge_rows)

    aggregates = {regime: aggregate(case_scores_by_regime[regime]) for regime in ALL_REGIMES}
    with open(os.path.join(RESULTS_DIR, "aggregate_by_regime.json"), "w") as f:
        json.dump(
            {regime: agg.__dict__ for regime, agg in aggregates.items()},
            f, indent=2, default=str,
        )

    print("Experiment executed. Aggregate metrics:")
    for regime, agg in aggregates.items():
        print(f"  {regime}: {agg}")


if __name__ == "__main__":
    run()
