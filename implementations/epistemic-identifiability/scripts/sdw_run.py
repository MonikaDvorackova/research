"""Run the SDW development evaluation.  usage: sdw_run.py --ns 25000 --n 40 --out results/sdw_dev/main_ns25000.pkl [--fams ...] [--smoke]"""
import sys, os, argparse, pickle, time, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, torch
from multiprocessing import Pool
from eid.sdw import env, agent as A, hyp, rep

HERE = os.path.join(os.path.dirname(__file__), "..")
DESIGNS = ["falsify", "sweepA", "sweepB", "random", "ens", "eig"]


def load_est():
    ms = []
    for s in (1, 2, 3):
        p = f"{HERE}/results/sdw_dev/est/est_s{s}.pt"
        if os.path.exists(p): m = rep.Est(); m.load_state_dict(torch.load(p)); m.eval(); ms.append(m)
    return ms


def work(task):
    k, fam, ns, Bs, cfg, variants = task
    torch.set_num_threads(1)
    iseed = ns + k; inst = env.make_instance(fam, np.random.default_rng(iseed)); tests = A.test_set(inst, ns - 25000 + k)
    out = dict(k=k, fam=fam, inst={a: b for a, b in inst.items()}, agents={}, base={})
    for d in DESIGNS:
        if d in variants: out["agents"][d] = A.run_agent(inst, iseed, Bs, d, cfg, tests=tests)
    if "declared" in variants: out["agents"]["declared_eig"] = A.run_agent(inst, iseed, Bs, "eig", cfg, allowed=hyp.DECLARED, tests=tests)
    if "nou2" in variants:
        mask = np.array([i not in A.U2_IDS for i in range(len(env.POOL))])
        out["agents"]["falsify_nou2"] = A.run_agent(inst, iseed, Bs, "falsify", cfg, pool_mask=mask, tests=tests)
    if "base" in variants:
        est = load_est()
        out["base"]["B"] = A.run_baselines(inst, iseed, Bs, cfg, tests, est_models=est, sched="B")
        out["base"]["A"] = {k2: v for k2, v in A.run_baselines(inst, iseed, Bs, cfg, tests, est_models=None, sched="A").items() if k2 in ("grammar_sweep", "bayes_declared", "narx", "hammerstein")}
    if "proposal" in variants:
        data = A.Data(inst, iseed)
        for pid in env.SWEEP_B[:6]: data.add(pid, env.POOL[pid])
        U, Y = data.arr; X2 = np.stack(data.X2); est = load_est()
        out["proposal"] = {w: A.proposal_rank(U, Y, X2, est, w) for w in ("oracle", "analytic", "learned")}
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--ns", type=int, default=25000); ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--fams", default=",".join(env.ALL_FAMS)); ap.add_argument("--Bs", default="3,5,8"); ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=10); ap.add_argument("--variants", default="falsify,sweepA,sweepB,random,ens,eig,declared,nou2,base,proposal")
    ap.add_argument("--cfg", default=f"{HERE}/results/sdw_dev/tuned_config_ns24200.json")
    a = ap.parse_args(); Bs = tuple(int(x) for x in a.Bs.split(",")); cfg = json.load(open(a.cfg))
    tasks = [(k, f, a.ns, Bs, cfg, set(a.variants.split(","))) for f in a.fams.split(",") for k in range(a.n * 0 + a.n * 0, a.n)]
    # instance index must be unique across families: k enumerates within family, offset by family index
    fl = a.fams.split(","); tasks = [(fi * 1000 + k, f, a.ns, Bs, cfg, set(a.variants.split(","))) for fi, f in enumerate(fl) for k in range(a.n)]
    t0 = time.time()
    with Pool(a.workers) as P: res = []; [res.append(r) or print(f"{len(res)}/{len(tasks)} {time.time()-t0:.0f}s", flush=True) for r in P.imap_unordered(work, tasks)]
    pickle.dump(dict(args=vars(a), res=res), open(a.out, "wb")); print("done", time.time() - t0)
