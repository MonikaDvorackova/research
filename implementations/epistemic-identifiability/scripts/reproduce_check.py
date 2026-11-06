"""Re-run seed 0 of stored result directories at full configuration and compare to the stored metrics.csv.

Usage: PYTHONPATH=src python scripts/reproduce_check.py poc_v2 abl_analytic
Exits non-zero if any value differs by more than 1e-9.
"""
import csv
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import yaml

from eid.run import run_seed

ROOT = os.path.join(os.path.dirname(__file__), "..")


def check(name):
    cfg_name = "poc" if name in ("poc_v1", "poc_v2") else name
    cfg = yaml.safe_load(open(os.path.join(ROOT, "configs", cfg_name + ".yaml")))
    _, rows = run_seed(cfg, 0)
    stored = [r for r in csv.DictReader(open(os.path.join(ROOT, "results", name, "metrics.csv"))) if r["seed"] == "0"]
    bad = 0
    for a, b in zip(rows, stored):
        for k, v in a.items():
            bad += (v != b[k]) if isinstance(v, str) else abs(float(v) - float(b[k])) > 1e-9
    return name, len(rows), len(stored), int(bad)


if __name__ == "__main__":
    names = sys.argv[1:] or ["poc_v2"]
    with ProcessPoolExecutor(len(names)) as ex:
        results = list(ex.map(check, names))
    for r in results:
        print("reproduce seed 0: %s rows=%d stored=%d mismatches=%d" % r)
    sys.exit(1 if any(r[3] or r[1] != r[2] for r in results) else 0)
