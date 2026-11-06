import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from eid.ool import bench, lang, loop, evals
from eid.sdw import env, hyp as H0


def test_manifest_splits_and_hash():
    assert set(bench.SPLITS["holdout"]).isdisjoint(bench.SPLITS["dev"]) and set(bench.SPLITS["holdout"]).isdisjoint(bench.SPLITS["calib"])
    assert len(bench.MAN_SHA) == 64


def test_bench_lin_matches_sdw():
    i = bench.make_instance("lin", np.random.default_rng(1)); j = dict(fam="lin", a=i["a"], b3=i["b3"], e=i["e"], d=i["d"], c=i["c"], par=0, kappa=0, om=0, ze=0)
    assert np.abs(bench.simulate(i, env.POOL[5])[1] - env.simulate(j, env.POOL[5])[1]).max() < 1e-12


def test_nonidentifiable_equivalent_to_null():
    for fam in ("thresh", "bumpfar"):
        i = bench.make_instance(fam, np.random.default_rng(3)); n = dict(i, c=0.0)
        assert max(np.abs(bench.simulate(i, u)[1] - bench.simulate(n, u)[1]).max() for u in env.POOL) < 1e-3


def test_world_hides_instance():
    w = bench.World(bench.make_instance("sin", np.random.default_rng(2)), 2)
    assert w.run(env.POOL[0], 0).shape == (env.T, 3) and w.n_runs == 1


def test_expansion_vocabulary_outside_L0():
    l0 = set(lang.keys_stage(0))
    for s in (1, 2, 3): assert not (set(lang.keys_stage(s)) & l0)
    assert lang.is_new(lang.K("sin", 3)) and not lang.is_new(lang.K("gate", 0.3))


def test_hypothesis_with_true_structure_fits_leak():
    inst = bench.make_instance("leak", np.random.default_rng(5)); w = bench.World(inst, 5); d = loop.Data(w)
    for pid in env.SWEEP_B[:6]: d.add(pid, env.POOL[pid])
    U, Y = d.arr; al, be, sg, st = loop.fit_state(U, Y)
    top, allh, nc, st2 = lang.search(U, Y, st, [k for k in lang.keys_stage(2)], True, False)
    Ut, tr = loop.make_tests(inst, 1)
    assert min(loop.rmse(lang.predict(h, al, be, Ut), tr) for h in top[:2]) < 0.05


def test_level2_and_sr_signature():
    assert evals.level2("sin", ["sin(id)"]) and not evals.level2("sin", ["dz(id)", "tanh(id)"]) and evals.level2("thresh", [])
    assert evals.sr_signature("sin", "sin(x * 4.3) * 2.1") and not evals.sr_signature("sin", "square(x)")


def test_sweep_ids_unique():
    ids = loop.sweep_ids(12); assert len(ids) == len(set(ids)) == 12
