"""Re-run one confirmatory seed of a Bayesian experiment in a fresh process and compare every stored array exactly (run B).
Usage: PYTHONPATH=src python scripts/reproduce_bayes.py 1 configs/bayes1_confirm.yaml results/bayes1_confirm_runB 300"""
import sys

import numpy as np
import yaml

kind, cfg_path, d, seed = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
run_seed = __import__(f"eid.run_bayes{kind}", fromlist=["run_seed"]).run_seed
cfg = yaml.safe_load(open(cfg_path))
_, out, _ = run_seed(cfg, seed)
stored = np.load(f"{d}/seed{seed}.npz")
bad = [k for k in stored.files if k not in out or not np.array_equal(stored[k], out[k], equal_nan=True)]
print(f"environment {kind} seed {seed}: arrays compared = {len(stored.files)}, mismatching = {len(bad)}", bad[:5])
sys.exit(1 if bad else 0)
