import sys, os
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.mdw import env, agents as A, model as M


def test_families_equal_under_zero_input_and_differ_under_probes():
    U0 = torch.zeros(5, env.T, 2, dtype=torch.float64)
    for f in env.TRAIN_FAMS + env.HELD_FAMS:
        inst = env.sample_instances((f,), 5, 3)
        assert env.simulate(inst, U0).abs().max() == 0.0                          # passive/zero input reveals nothing (all families identical)
    d = {f: env.true_descriptors(env.sample_instances((f,), 20, 4)).mean(0) for f in env.TRAIN_FAMS + env.HELD_FAMS}
    assert d["sat"][0] > d["lin"][0] + 0.3 and d["gate"][0] < 0.3 and d["delay"][2] > d["lin"][2] + 2 and d["backlash"][3] > d["lin"][3] + 0.1


def test_lin_reduces_to_linear_system_and_delay_shifts():
    inst = env.sample_instances(("lin",), 4, 5); U = torch.rand(4, env.T, 2, dtype=torch.float64) * 2 - 1
    y1 = env.simulate(inst, U); y2 = env.simulate(inst, 2 * U.clamp(-1, 1) * 0.5)
    assert torch.allclose(y1, y2)
    # linearity of the x3 channel in the lin family: scaling the input scales the output
    y3 = env.simulate(inst, U * 0.5); assert torch.allclose(y3[..., 1], 0.5 * y1[..., 1], atol=1e-9)
    inst_d = env.sample_instances(("delay",), 4, 6); lin = dict(fam=torch.zeros(4, dtype=torch.long), c=inst_d["c"], par=torch.zeros(4, dtype=torch.float64))
    xd = env.simulate(inst_d, torch.ones(4, env.T, 2, dtype=torch.float64) * torch.tensor([1.0, 0.0], dtype=torch.float64))
    xl = env.simulate(lin, torch.ones(4, env.T, 2, dtype=torch.float64) * torch.tensor([1.0, 0.0], dtype=torch.float64))
    assert (xd[..., 1][:, -1] <= xl[..., 1][:, -1] + 1e-9).all()                       # delayed coupling lags the undelayed one


def test_normalisation_uses_training_families_only_and_probe_set():
    assert set(env.PROBES) == {"small", "large", "neg", "tri"} and env.DESC_SD.min() > 0
    assert env.CANDS.shape == (8, env.T, 2) and env.CANDS.abs().max() <= 1.0


def test_no_family_metadata_in_agent_interface():
    import inspect
    for fn in (A.est_direct, A.est_sysid, A.wm_desc, A.wm_choose, A.reg_desc, A.bayes_post):
        assert not any(p in ("inst", "fam", "par", "label") for p in inspect.signature(fn).parameters)


def test_direct_probe_recovers_descriptors_with_full_budget():
    inst = env.sample_instances(env.TRAIN_FAMS, 10, 7); N = 30
    eps = torch.randn(N, 4, env.T, 2, generator=torch.Generator().manual_seed(1), dtype=torch.float64) * 0
    U, Y = A.collect_fixed(inst, A.sweep_programmes(N, 4), eps, 4)
    est = A.est_direct(U, Y); tr = env.true_descriptors(inst)
    assert torch.allclose(est[:, [0, 1, 3]], tr[:, [0, 1, 3]], atol=1e-6)


def test_bayes_grid_posterior_concentrates_on_truth_family_in_class():
    inst = env.sample_instances(("sat",), 6, 8); N = 6
    eps = torch.randn(N, 4, env.T, 2, generator=torch.Generator().manual_seed(2), dtype=torch.float64)
    U, Y = A.collect_fixed(inst, A.sweep_programmes(N, 4), eps, 4)
    est, chi2, post = A.bayes_est(U, Y)
    sat_mass = post[:, 3:12].sum(1); assert (sat_mass > 0.9).all() and chi2.max() < 3.0
    held = env.sample_instances(("gate",), 6, 9); Uh, Yh = A.collect_fixed(held, A.sweep_programmes(N, 4), eps, 4)
    assert A.bayes_est(Uh, Yh)[1].min() > 3.0                                            # misfit flags the out-of-class family


def test_context_model_shapes_and_imagination():
    torch.manual_seed(0); m = M.CtxGRU(H=16, n_desc=4)
    N = 3; U = torch.rand(N, 2 * env.T, 2); Y = torch.randn(N, 2 * env.T, 2)
    nll, h = m.run(U, Y, env.T, ss_prob=0.5, free_last=True)
    assert nll.shape == (N, 2 * env.T) and torch.isfinite(nll).all() and h.shape == (N, 16)
    assert m.imagine(h, torch.rand(N, env.T, 2), env.T).shape == (N, env.T, 2) and m.predict_desc(h).shape == (N, 4)
    assert m.encode(U[:, :0], Y[:, :0], env.T).abs().max() == 0


def test_gate_is_exactly_unidentifiable_below_actuator_reach():
    """x1 is a stable first-order filter of u1: |x1| <= G/B1 * max|u1|. For amplitude-limited inputs with G/B1*umax <= theta the gated
    coupling never activates, so x3 == 0 for EVERY theta above the reach (exact equivalence to 'no coupling' and to each other)."""
    reach = env.G / env.B1                               # 0.9375
    umax = 0.3; ceiling = reach * umax                   # 0.28125
    thetas = [0.29, 0.4, 0.7]
    g = torch.Generator().manual_seed(0)
    U = (torch.rand(20, env.T, 2, generator=g, dtype=torch.float64) * 2 - 1) * umax; U[..., 1] = 0.0
    outs = []
    for th in thetas:
        inst = dict(fam=torch.full((20,), 3), c=torch.full((20,), 2.0, dtype=torch.float64), par=torch.full((20,), th, dtype=torch.float64))
        outs.append(env.simulate(inst, U)[..., 1])
        assert outs[-1].abs().max() == 0.0
    # with full-range inputs the thresholds ARE distinguishable (gate below the reach is identifiable)
    Ufull = torch.ones(1, env.T, 2, dtype=torch.float64) * torch.tensor([1.0, 0.0], dtype=torch.float64)
    x = [env.simulate(dict(fam=torch.tensor([3]), c=torch.tensor([2.0], dtype=torch.float64), par=torch.tensor([th], dtype=torch.float64)), Ufull)[0, :, 1] for th in (0.3, 0.7)]
    assert float((x[0] - x[1]).abs().max()) > 5e-2           # theta shows up in the TRANSIENT (x1 crosses it at different times) ...
    assert abs(float(x[0][-1] - x[1][-1])) < 5e-3            # ... while the end-state is almost independent of theta


def test_eval_harness_runs_end_to_end_on_tiny_models(tmp_path):
    import subprocess, json
    for kind in ("wm", "reg"):
        torch.manual_seed(0); m = M.CtxGRU(H=16, n_desc=4 if kind == "reg" else 0)
        d = tmp_path / kind; d.mkdir(); torch.save(m.state_dict(), d / "final.pt"); json.dump({"H": 16}, open(d / "config.json", "w"))
    out = tmp_path / "o.json"
    r = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), "..", "scripts", "mdw_eval.py"), "--ns", "24000", "--n", "2", "--lam", "0.1",
                        "--wm", str(tmp_path / "wm"), str(tmp_path / "wm"), "--reg", str(tmp_path / "reg"), "--threads", "2", "--out", str(out)],
                       capture_output=True, text=True, env=dict(os.environ, PYTHONPATH=os.path.join(os.path.dirname(__file__), "..", "src")))
    assert r.returncode == 0, r.stderr[-500:]
    res = json.load(open(out)); assert set(res["sets"]) == {"known", "gate", "backlash"} and "wm(plan)" in res["sets"]["known"]
