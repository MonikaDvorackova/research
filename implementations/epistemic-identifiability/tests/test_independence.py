"""Leakage and independence audit: random streams, data disjointness, and information access."""
import itertools

import numpy as np
import yaml

from eid.run import TAGS, collect, rng_for, run_seed


def test_all_random_streams_are_distinct():
    """No two (tag, extra) pairs used by the pipeline may produce the same random numbers for a seed."""
    used = []
    used += [("q", 0), ("q", 1), ("q2", 0), ("q2", 1), ("alt", 0)]
    used += [("w", i) for i in range(4)] + [("test", i) for i in range(4)]
    for tag in ("eval", "cal"):
        used += [(tag, 10 * p + k) for p in range(3) for k in range(10)]
    for tag in ("alto_eval", "alto_cal"):
        used += [(tag, 10 * p + k) for p in range(3) for k in range(4)]
    used += [("adapt", i) for i in range(0, 130)] + [("adapt", 1000 + i) for i in range(0, 130)]
    assert set(t for t, _ in used) <= set(TAGS)
    for seed in (0, 7):
        sigs = {}
        for tag, extra in used:
            sig = tuple(rng_for(seed, tag, extra).random(4))
            assert sig not in sigs, f"stream collision: {(tag, extra)} vs {sigs[sig]}"
            sigs[sig] = (tag, extra)
    # different seeds give different streams
    assert tuple(rng_for(0, "eval", 3).random(4)) != tuple(rng_for(1, "eval", 3).random(4))


def test_agent_theory_and_world_model_training_data_are_disjoint():
    Xq, Aq, _ = collect(5000, rng_for(3, "q"))
    Xq2, _, _ = collect(5000, rng_for(3, "q2"))
    Xw, Aw, _ = collect(12500, rng_for(3, "w", 3))
    rows = lambda X, A: {tuple(r) for r in np.c_[X, A].round(12)}  # noqa: E731
    assert not (rows(Xq, Aq) & rows(Xw, Aw))
    assert not (rows(Xq, Aq) & rows(Xq2, Aq))
    assert abs(np.corrcoef(Xq[:2000, 0], Xw[:2000, 0])[0, 1]) < 0.1  # no shared sample path


def test_adaptive_observer_smoke_and_disjoint_phases():
    cfg = yaml.safe_load(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "..", "configs", "smoke.yaml")))
    cfg["adaptive"] = {"episodes": 10, "horizon": 3, "steps": 20, "replay": 100}
    q, r = run_seed(cfg, 0)
    assert len(r) == len(cfg["train_sizes"]) * 3 * len(cfg["horizon_grid"])
    assert all(np.isfinite(x["auroc_W_vs_null"]) for x in r)
    q2, r2 = run_seed(cfg, 0)
    assert r == r2  # deterministic


def test_new_ablation_configs_run():
    import os
    d = os.path.join(os.path.dirname(__file__), "..", "configs")
    for name in ("abl_qindep", "abl_wrelu_qtanh", "abl_wrelu_qrelu", "adaptive_tanh"):
        cfg = dict(yaml.safe_load(open(os.path.join(d, name + ".yaml"))))
        cfg.update(n_seeds=1, train_sizes=[100], q_train_n=400, ensemble_k=2, train_steps=60, eval_episodes=30, horizon_grid=[2, 4])
        if "adaptive" in cfg:
            cfg["adaptive"] = {"episodes": 8, "horizon": 3, "steps": 10, "replay": 50}
        _, rows = run_seed(cfg, 0)
        assert len(rows) == 3 * 2 and all(np.isfinite(x["auroc_W_vs_null"]) for x in rows)
