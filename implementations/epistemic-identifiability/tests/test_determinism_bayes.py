"""Regression test for the Phase 5 reproducibility defect: stream identifiers were derived from Python's per-process randomised str hash.
The Bayesian runners must now give identical output across separate interpreter processes with different PYTHONHASHSEED values."""
import json
import os
import subprocess
import sys

import numpy as np

ROOT = os.path.join(os.path.dirname(__file__), "..")

SCRIPT = r'''
import sys, json, hashlib
sys.path.insert(0, "src")
import numpy as np
from eid.run_bayes1 import run_seed as r1
from eid.run_bayes2 import run_seed as r2
cfg1 = dict(seeds=[1], R=6, steps=12, episode_len=6, checkpoints=[6, 12], regimes=["oracle", "learned"], policies=["wide", "eig"],
            q_train_n=300, w_train_n=300, train_steps=20, q_amp=1.0)
cfg2 = dict(seeds=[1], R=6, steps=12, episode_len=6, checkpoints=[6, 12], regimes=["oracle", "learned"], policies=["random", "eig"],
            train_episodes=60, train_horizon=6, train_steps=10, hidden=8, train_p2=0.02, wp_sizes=[60, 40, 40, 60, 60, 60, 60])
h = hashlib.sha256()
for run, cfg in ((r1, cfg1), (r2, cfg2)):
    _, out, _ = run(cfg, 1)
    for k in sorted(out):
        h.update(k.encode()); h.update(np.ascontiguousarray(out[k], dtype=np.float64).tobytes())
print(h.hexdigest())
'''


def _run(hashseed):
    env = dict(os.environ, PYTHONHASHSEED=str(hashseed), PYTHONPATH=os.path.join(ROOT, "src"))
    return subprocess.run([sys.executable, "-c", SCRIPT], cwd=ROOT, env=env, capture_output=True, text=True, check=True).stdout.strip()


def test_bayesian_runners_are_deterministic_across_processes_and_hash_seeds():
    a, b = _run(1), _run(12345)
    assert a == b and len(a) == 64
