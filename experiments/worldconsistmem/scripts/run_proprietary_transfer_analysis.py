#!/usr/bin/env python3
"""Run proprietary-reader transfer analysis (read-only w.r.t. primary artefacts)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from worldconsistmem.proprietary_transfer_analysis import run_analysis  # noqa: E402


def main() -> int:
    result = run_analysis()
    gpt = result["gpt41_mini"]
    print(
        json.dumps(
            {
                "provenance_ok": result["provenance"]["all_ok"],
                "gpt_acc": gpt["mean_acc"],
                "gpt_bcr": gpt["bcr"],
                "gpt_acc_ci": gpt["acc_ci95_bundle_bootstrap"],
                "gpt_bcr_ci": gpt["bcr_ci95_clopper_pearson"],
                "matched_qwen_available": result["matched_qwen_meta"]["available"],
                "qwen_acc": None if not result["matched_qwen"] else result["matched_qwen"]["mean_acc"],
                "qwen_bcr": None if not result["matched_qwen"] else result["matched_qwen"]["bcr"],
                "out": "results/confirmatory/proprietary_reader_transfer/",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
