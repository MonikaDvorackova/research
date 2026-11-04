import sys, os, re
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.sdw import env, hyp, agent as A, baselines as bl


def _data(inst, iseed, ids):
    d = A.Data(inst, iseed)
    for i in ids: d.add(i, env.POOL[i])
    return d


def test_zero_input_identical_across_families():
    for f in env.ALL_FAMS:
        inst = env.make_instance(f, np.random.default_rng(3)); _, x3, _ = env.simulate(inst, np.zeros((env.T, 2)))
        assert np.abs(x3).max() == 0.0                                       # passive/zero input reveals nothing


def test_unreach_gate_is_interventionally_equivalent_to_no_coupling():
    rng = np.random.default_rng(4); inst = env.make_instance("unreach", rng); null = dict(inst, fam="gate", par=10.0)
    for u in list(env.POOL) + env.random_programmes(20, rng):
        assert np.abs(env.simulate(inst, u)[1] - env.simulate(null, u)[1]).max() == 0.0     # never activates (S1)


def test_actuator_reach_bound():
    inst = env.make_instance("lin", np.random.default_rng(1)); u = np.ones((env.T, 2))
    # x1 is a filter of u1: |x1| <= reach (checked through the AR model fitted on clean data)
    y, _, _ = env.simulate(inst, u); assert np.abs(y[:, 0]).max() <= env.REACH + 1e-9


def test_iv_ar_estimate_is_unbiased_where_ols_is_not():
    inst = env.make_instance("lin", np.random.default_rng(2)); idx = [env.IDX[n] for n in ["u1 +1", "u1 -1", "u1 step 1>-1", "u1 tri +"]]
    d = _data(inst, 7, idx); U, Y = d.arr; al, be, sg = hyp.fit_x1(U, Y); true = (1 - env.B1 * env.DT / env.SUB) ** env.SUB
    assert abs(al - true) < 0.03 and abs(sg - env.SIG) < 0.01


def test_structure_search_recovers_in_language_structures_from_enough_episodes():
    ids = [env.IDX[n] for n in ["u1 -1", "u2 +1", "u1 +0.4", "u2 square", "u1 step 1>-1", "u1 tri +"]]
    hits = {}
    for fam, expect in [("lin", "lin"), ("quad", "quad"), ("delay", "delay"), ("sat", "tanh"), ("gate", "gate")]:
        ok = 0
        for k in range(4):
            inst = env.make_instance(fam, np.random.default_rng(100 + k)); d = _data(inst, 100 + k, ids); U, Y = d.arr
            al, be, sg, st = A.fit_state(U, Y); best = hyp.search(U, Y, st)[0]; ok += expect in hyp.names_of(best)
        hits[fam] = ok
    assert sum(hits.values()) >= 16, hits


def test_hypotheses_are_executable_and_predict_unseen_programmes():
    inst = env.make_instance("quad", np.random.default_rng(9)); ids = [env.IDX[n] for n in ["u1 -1", "u2 +1", "u1 +0.4", "u2 square", "u1 step 1>-1"]]
    d = _data(inst, 9, ids); U, Y = d.arr; al, be, sg, st = A.fit_state(U, Y); h = hyp.search(U, Y, st)[0]
    Ut, truth = A.test_set(inst, 1); assert A.rmse(hyp.predict(h, al, be, Ut), truth) < 0.05


def test_falsification_design_prefers_u2_to_separate_saturation_from_hidden_feedback():
    base = dict(a=1.5, b3=1.5, k=0.7, al=0.85, be=0.14)
    h_sat = dict(prims=[("tanh", 0.4)], w=np.array([3.0]), kappa=0.0, a=1.5, b3=1.5, k=0.7)
    h_fb = dict(prims=[("lin", None)], w=np.array([2.2]), kappa=0.4, a=1.5, b3=1.5, k=0.7)
    sc = hyp.disagreement_scores([h_sat, h_fb], 0.85, 0.14, A.POOL_U, 0.03)
    best_u2 = max(sc[i] for i in A.U2_IDS); best_u1 = max(sc[i] for i in range(len(env.POOL)) if i not in A.U2_IDS)
    assert best_u2 > 0.5 * best_u1 and sc.max() > 100                       # a u2 programme is competitive; hypotheses are separable


def test_no_family_or_parameter_access_in_agent_modules():
    d = os.path.join(os.path.dirname(__file__), "..", "src", "eid", "sdw")
    for f in ("hyp.py", "agent.py", "baselines.py", "rep.py"):
        src = open(os.path.join(d, f)).read()
        assert 'inst["' not in src and "inst['" not in src and '["fam"]' not in src      # agents and baselines never read instance fields; only observe()/test_set() simulate


def test_baselines_run_and_are_not_trivially_broken():
    inst = env.make_instance("lin", np.random.default_rng(11)); cfg = dict(lam_narx=1.0, sindy=dict(raw=[1, .05], embed=[1, .1], learned=[1, .05], oracle=[1, .3]), sindy_dict=dict(raw=1., learned=.3, oracle=.1))
    r = A.run_baselines(inst, 11, (5,), cfg, A.test_set(inst, 3), est_models=None)
    assert r["hammerstein"][5]["rmse"] < 0.2 and r["grammar_sweep"][5]["rmse"] < 0.05 and np.isfinite(r["narx"][5]["rmse"])


def test_agent_snapshots_nested_and_outcome_modes():
    inst = env.make_instance("sat", np.random.default_rng(12)); cfg = dict(lam_narx=1.0)
    out = A.run_agent(inst, 12, (3, 5), "sweepB", cfg, tests=A.test_set(inst, 4))
    assert out[5]["ids"][:3] == out[3]["ids"] and A.outcome(out[3], "nocrit") == "claim" and out[5]["ok"]
