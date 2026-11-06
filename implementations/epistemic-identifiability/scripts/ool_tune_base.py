"""Baseline tuning on the tuning namespace (instance seeds 310-312 per family; calib+dev families only; never holdout).  Selects (library, threshold, variable set) per method
by median rollout RMSE.  usage: ool_tune_base.py --out results/ool_dev/baseline_tuning.json"""
import sys, os, json, time, argparse, warnings, itertools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src")); warnings.filterwarnings("ignore")
import numpy as np
from eid.ool import bench, loop, base
from eid.sdw import env as E

ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--n", type=int, default=3); a = ap.parse_args()
fams = sorted(set(bench.SPLITS["calib"]) | set(bench.SPLITS["dev"])); sets = []
for f in fams:
    for s in range(a.n):
        inst = bench.make_instance(f, np.random.default_rng(310 + s)); w = bench.World(inst, 310 + s); d = loop.Data(w)
        for pid in E.SWEEP_B[:6]: d.add(pid, E.POOL[pid])
        U, Y = d.arr; al, be, sg, st = loop.fit_state(U, Y); x2, q = base.kalman_prof(U, Y, st, sg); Ut, tr = loop.make_tests(inst, 900 + s)
        sets.append((f, U, Y, st, x2, Ut, tr))
res = {}
def score(fn):
    out = []
    for f, U, Y, st, x2, Ut, tr in sets:
        try:
            ph, div = fn(U, Y, st, x2, Ut); r = float(np.sqrt(((ph - tr) ** 2).mean())); r = r if np.isfinite(r) else 99.0
        except Exception: r = 99.0
        out.append(r)
    return float(np.median(out)), float(np.mean(np.array(out) <= 0.05)), float(np.mean(np.array(out) > 1.0))
for form, lib, thr, vs in itertools.product(["sindyc", "weak"], ["poly2", "poly3", "expanded"], [0.02, 0.05, 0.1, 0.3, 1.0], ["core", "lags"]):
    t = time.time()
    def fn(U, Y, st, x2, Ut, form=form, lib=lib, thr=thr, vs=vs):
        f = base.fit_sindy(U, Y, x2, st, form, lib, thr, vs); return base.simulate(f, st, Ut, full=True)
    res[f"{form}|{lib}|{thr}|{vs}"] = score(fn); print(form, lib, thr, vs, [round(x, 3) for x in res[f"{form}|{lib}|{thr}|{vs}"]], f"{time.time()-t:.0f}s", flush=True)
for thr in [0.02, 0.05, 0.1, 0.3, 1.0]:
    def fn(U, Y, st, x2, Ut, thr=thr):
        f = base.fit_implicit(U, Y, x2, st, thr); return base.simulate(lambda V, u2: f(V), st, Ut)
    res[f"implicit|poly2|{thr}|lags"] = score(fn); print("implicit", thr, [round(x, 3) for x in res[f"implicit|poly2|{thr}|lags"]], flush=True)
best = {}
for m in ("sindyc", "weak", "implicit"):
    k = min((k for k in res if k.startswith(m)), key=lambda k: res[k][0]); best[m] = k
json.dump(dict(scores=res, best=best, n_sets=len(sets), fams=fams, note="median rollout RMSE, fraction RMSE<=0.05, fraction RMSE>1 over tuning instances"), open(a.out, "w"), indent=1)
print(best)
