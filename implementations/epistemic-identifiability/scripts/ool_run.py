"""Run the OOL evaluation (calibration / development / holdout).  usage: ool_run.py --split dev --ns 30000 --n 10 --out results/ool_dev/dev_ns30000.pkl --cal results/ool_dev/calibration_ns29000.json
Agents and the cheap baselines run here (eid venv); PySR runs from the prepared datasets (ool_pysr.py, eid-pysr venv)."""
import sys, os, argparse, pickle, time, json, warnings
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src")); warnings.filterwarnings("ignore")
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np, torch
from multiprocessing import Pool
from eid.ool import bench, loop, lang, base
from eid.sdw import env as E, baselines as bl, rep

HERE = os.path.join(os.path.dirname(__file__), "..")
AGENTS = {  # name: (design, mode, order)
    "adapt_sweepB": ("sweepB", "adaptive", loop.STAGE_ORDER), "adapt_falsify": ("falsify", "adaptive", loop.STAGE_ORDER), "adapt_random": ("random", "adaptive", loop.STAGE_ORDER),
    "adapt_ens": ("ens", "adaptive", loop.STAGE_ORDER), "L0_sweepB": ("sweepB", "L0", None), "L0_falsify": ("falsify", "L0", None), "all_sweepB": ("sweepB", "static_all", None),
    "ord_kalman_sweepB": ("sweepB", "adaptive", "kalman"), "ord_learned_sweepB": ("sweepB", "adaptive", "learned"),
}


def load_est():
    ms = []
    for s in (1, 2, 3):
        m = rep.Est(); m.load_state_dict(torch.load(f"{HERE}/results/sdw_dev/est/est_s{s}.pt")); m.eval(); ms.append(m)
    return ms


def order_fn(kind, est):
    def f(U, Y, st, sg):
        x2 = base.kalman_prof(U, Y, st, sg)[0] if kind == "kalman" else base.x2_source(U, Y, st, sg, "learned", est)
        return loop.propose_order(U, Y, st, x2)
    return f


def oracle_structure(U, Y, fam, tests):
    """Privileged upper bound: restrict the language to the true signature's terms, fit, take the best hypothesis whose structure equals the signature."""
    sig = set(bench.FAM[fam]["sig"][0]) if bench.FAM[fam]["sig"] else set()
    names = {s for s in sig if s not in ("XINT", "FB")}
    keys = [k for k in lang.keys_upto(3) if lang.tname(k) in names]
    al, be, sg, st = loop.fit_state(U, Y)
    top, allh, nc, st2 = lang.search(U, Y, st, keys, use_fb=False, use_xint="XINT" in sig, polish=4)
    pick = [h for h in top if set(lang.desc(h)) == sig] or top
    h = pick[0]; Ut, tr = tests
    return dict(rmse=loop.rmse(lang.predict(h, al, be, Ut), tr), label=lang.label(h), desc=list(lang.desc(h)), terms=[tuple(t) for t in h["terms"]], gamma=h["gamma"], matched=set(lang.desc(h)) == sig)


def work(task):
    fi, k, fam, ns, Bs, cal, variants, cfg, noise, nou2 = task
    torch.set_num_threads(1)
    iseed = ns + fi * 1000 + k; inst = bench.make_instance(fam, np.random.default_rng(iseed)); tests = loop.make_tests(inst, iseed)
    out = dict(k=k, fam=fam, iseed=iseed, inst=inst, agents={}, base={}, prep={}, oracle={}); est = None
    mask = np.array([i not in {j for j, u in enumerate(loop.POOL) if np.abs(u[:, 1]).max() > 0} for i in range(len(loop.POOL))]) if nou2 else None
    if any(v.startswith("ord_") or v == "base" or v == "prep" for v in variants): est = load_est()
    for name, (design, mode, order) in AGENTS.items():
        if name in variants:
            od = order_fn(order, est) if order in ("kalman", "learned") else (order if order else loop.STAGE_ORDER)
            out["agents"][name] = loop.run_agent(inst, iseed, Bs, design, mode, cal, tests, cfg, noise=noise, pool_mask=mask, order=od)
    ids = loop.sweep_ids(max(Bs)); world = bench.World(inst, iseed, noise); data = loop.Data.__new__(loop.Data); data.w = world; data.ids, data.U, data.Y = [], [], []
    for pid in ids: data.add(pid, E.E0 if pid < 0 else loop.POOL[pid])
    X2 = np.stack([bench.simulate(inst, u, np.random.default_rng([iseed, 999 if pid < 0 else pid]), noise)[2] for pid, u in zip(ids, data.U)])
    if "oracle_struct" in variants:
        for B in Bs: out["oracle"][B] = oracle_structure(np.stack(data.U[:B]), np.stack(data.Y[:B]), fam, tests)
    if "base" in variants or "prep" in variants:
        Ut, tr = tests
        for B in Bs:
            U, Y = np.stack(data.U[:B]), np.stack(data.Y[:B]); al, be, sg, st = loop.fit_state(U, Y)
            xk, q = base.kalman_prof(U, Y, st, sg); xl = base.x2_source(U, Y, st, sg, "learned", est); xo = X2[:B]
            if "prep" in variants and B in (8, 12):
                out["prep"][B] = dict(U=U, Y=Y, st=st, sg=sg, x2=dict(kalman=xk, learned=xl, oracle=xo), q=q, Ut=Ut, truth=tr,
                                      true_skel=dict(a=inst["a"], b3=inst["b3"], k=inst["e"] * inst["d"]))
            if "base" not in variants: continue
            res = out["base"]
            def put(name, fn, **kw):
                t0 = time.time()
                try: p, div = fn(); r = float(np.sqrt(np.mean((p - tr) ** 2))); r = r if np.isfinite(r) else 99.0
                except Exception as e: r, div = 99.0, True
                res.setdefault(name, {})[B] = dict(B=B, rmse=r, ok=bool(r <= loop.TAU), diverged=bool(div), wall=time.time() - t0, **kw)
            put("narx", lambda: (bl.fit_narx(U, Y, cfg["lam_narx"])(Ut), False)); put("hammerstein", lambda: (bl.fit_hammerstein(U, Y, st)(Ut), False))
            for form in ("sindyc", "weak"):
                _, lib, thr, vs = cfg["tuned"][form].split("|")
                for src, x2 in (("kalman", xk), ("learned", xl), ("oracle", xo)):
                    if form == "weak" and src == "oracle": continue
                    put(f"{form}_{src}", lambda x2=x2, form=form, lib=lib, thr=thr, vs=vs: base.simulate(base.fit_sindy(U, Y, x2, st, form, lib, float(thr), vs), st, Ut, full=True))
            _, lib, thr, vs = cfg["tuned"]["implicit"].split("|")
            put("implicit_kalman", lambda: base.simulate(lambda V, u2, f=base.fit_implicit(U, Y, xk, st, float(thr)): f(V), st, Ut))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--split", required=True); ap.add_argument("--ns", type=int, required=True); ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--Bs", default="5,8,12"); ap.add_argument("--out", required=True); ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--cal", default=None); ap.add_argument("--variants", default=",".join(list(AGENTS) + ["oracle_struct", "base", "prep"]))
    ap.add_argument("--fams", default=None); ap.add_argument("--noise", type=float, default=1.0); ap.add_argument("--nou2", action="store_true"); ap.add_argument("--cfg", default=f"{HERE}/results/ool_dev/baseline_tuning.json")
    a = ap.parse_args(); Bs = tuple(int(x) for x in a.Bs.split(","))
    tj = json.load(open(a.cfg)); cfg = dict(lam_narx=1.0, tuned=tj["best"])
    cal = json.load(open(a.cal)) if a.cal else None
    fams = a.fams.split(",") if a.fams else bench.SPLITS[a.split]
    tasks = [(fi, k, f, a.ns, Bs, cal, set(a.variants.split(",")), cfg, a.noise, a.nou2) for fi, f in enumerate(fams) for k in range(a.n)]
    t0 = time.time(); res = []
    with Pool(a.workers) as P:
        for r in P.imap_unordered(work, tasks): res.append(r); print(f"{len(res)}/{len(tasks)} {time.time()-t0:.0f}s", flush=True)
    pickle.dump(dict(args=vars(a), manifest_sha=bench.MAN_SHA, res=res), open(a.out, "wb")); print("done", time.time() - t0)
