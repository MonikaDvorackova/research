"""Run X1.  python -m eid.run_x1 --config configs/x1_dev.yaml --out results/x1_dev
Output: runs.jsonl (one line per run, all fields), meta.json.  Every random stream is a deterministic function of integers."""
from __future__ import annotations

import argparse
import json
import os
import platform
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import yaml

from .x1 import POLICIES, Sampler, build_class, run, truths_for

TRUTH_ID = {"E0": 0, "split": 1, "n10": 2, "n20": 3, "t05": 4, "t10": 5, "pc0": 6, "pc1": 7, "pc2": 8, "shift": 9}


def _one(args):
    seed, cfg = args
    e0, M, W = build_class(seed)
    truths = truths_for(seed)
    rows = []
    for tn in cfg["truths"]:
        for pi, pol in enumerate(cfg["policies"]):
            for rep in range(cfg["R"]):
                key = [seed, TRUTH_ID[tn], POLICIES.index(pol), rep]
                env_rng = np.random.default_rng(np.random.SeedSequence(key + [1]))
                obs_rng = np.random.default_rng(np.random.SeedSequence(key + [2]))
                if tn == "shift":     # exploratory: switches between two class members mid-run; still outside the stationary class
                    env = Sampler(e0, env_rng, switch_to=dict(M)["n20"], switch_at=cfg["N"] // 3)
                else:
                    env = Sampler(truths[tn][0], env_rng)
                t0 = time.perf_counter()
                r = run(env, M, W, pol, cfg["N"], cfg["T"], obs_rng, alpha=cfg["alpha"])
                rows.append(dict(seed=seed, truth=tn, policy=pol, rep=rep, role=("shift" if tn == "shift" else truths[tn][1]),
                                 reject_episode=r["reject_episode"], reject_step=r["reject_step"], max_logE=r["max_logE"],
                                 seconds=time.perf_counter() - t0))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    cfg = yaml.safe_load(open(a.config))
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()
    with ProcessPoolExecutor(a.workers) as ex:
        res = list(ex.map(_one, [(s, cfg) for s in cfg["seeds"]]))
    with open(os.path.join(a.out, "runs.jsonl"), "w") as f:
        for rows in res:
            for r in rows:
                f.write(json.dumps(r) + "\n")
    json.dump(dict(config=cfg, python=sys.version, platform=platform.platform(), numpy=np.__version__,
                   wall_seconds=time.time() - t0), open(os.path.join(a.out, "meta.json"), "w"), indent=1)
    print("done", time.time() - t0)


if __name__ == "__main__":
    main()
