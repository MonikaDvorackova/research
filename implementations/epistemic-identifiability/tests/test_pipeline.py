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


def test_default_path_unchanged_by_ablation_refactor():
    """The default configuration must reproduce the stored pre-refactor output exactly."""
    import json
    import os
    gold = json.load(open(os.path.join(os.path.dirname(__file__), "golden_smoke_seed0.json")))
    q, r = run_seed(CFG, 0)
    assert json.loads(json.dumps({"quality": q, "rows": r})) == gold


def test_ablation_configs_run():
    import os
    d = os.path.join(os.path.dirname(__file__), "..", "configs")
    for name in ("abl_relu128", "abl_poly3", "abl_qwide", "abl_analytic"):
        cfg = dict(yaml.safe_load(open(os.path.join(d, name + ".yaml"))))
        cfg.update(n_seeds=1, train_sizes=[100], q_train_n=400, ensemble_k=2, train_steps=100, eval_episodes=40, horizon_grid=[2, 5])
        _, rows = run_seed(cfg, 0)
        assert len(rows) == 3 * 2 and all(np.isfinite(r["auroc_W_vs_null"]) for r in rows)
