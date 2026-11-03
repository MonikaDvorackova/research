import numpy as np
import yaml

from eid.run import run_seed

CFG = yaml.safe_load(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "..", "configs", "smoke.yaml")))


def test_smoke_pipeline_runs_and_is_deterministic():
    q1, r1 = run_seed(CFG, 0)
    q2, r2 = run_seed(CFG, 0)
    assert r1 == r2 and q1 == q2
    assert len(r1) == len(CFG["train_sizes"]) * 3 * len(CFG["horizon_grid"])
    for r in r1:
        for k in ("auroc_W_vs_null", "auroc_null_vs_null", "oracle_auroc", "tpr_W", "fpr_null"):
            assert 0.0 <= r[k] <= 1.0 and np.isfinite(r[k])
        assert np.isfinite(r["info_gain_per_step"]) and np.isfinite(r["ece"])
    assert all(q["alt_delta"] > 0 for q in q1)
