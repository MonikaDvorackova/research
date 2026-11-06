"""Tune baseline hyper-parameters (NARX ridge, SINDYc library degree and threshold per state set) on KNOWN families only, namespace 24200,
sweep-B schedule, B=5.  Evaluation families/namespaces are not touched."""
import sys, os, json, itertools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, torch
from multiprocessing import Pool
from eid.sdw import env, agent as A, baselines as bl, rep
HERE = os.path.join(os.path.dirname(__file__), "..")
LAMS = [1e-3, 1e-2, 1e-1, 1.0]; DEG = [1, 2, 3]; THR = [0.01, 0.05, 0.1, 0.3]; MODES = ["raw", "embed", "learned", "oracle"]


def work(k):
    torch.set_num_threads(1)
    fam = env.KNOWN[k % 3]; iseed = 24200 + k; inst = env.make_instance(fam, np.random.default_rng(iseed)); Ut, truth = A.test_set(inst, 200 + k)
    data = A.Data(inst, iseed)
    for pid in env.SWEEP_B[:3]: data.add(pid, env.POOL[pid])
    U, Y = data.arr; X2 = np.stack(data.X2); out = {}
    for lam in LAMS: out[("narx", lam)] = A.rmse(bl.fit_narx(U, Y, lam)(Ut), truth)
    ms = []
    for s in (1, 2, 3):
        m = rep.Est(); m.load_state_dict(torch.load(f"{HERE}/results/sdw_dev/est/est_s{s}.pt")); ms.append(m)
    x2hat = np.mean([rep.infer(m, Y[..., 1], U[..., 1]) for m in ms], 0)
    for mode, d, t in itertools.product(MODES, DEG, THR):
        try: p = bl.fit_sindyc(U, Y, mode, t, x2hat=x2hat, x2true=X2, degree=d)[0](Ut); out[(mode, d, t)] = A.rmse(p, truth)
        except Exception: out[(mode, d, t)] = float("inf")
    for mode, t in itertools.product(MODES, [0.1, 0.3, 1.0, 3.0]):
        try: p = bl.fit_sindyc(U, Y, mode, t, x2hat=x2hat, x2true=X2, lib="dict")[0](Ut); out[("dict_" + mode, 0, t)] = A.rmse(p, truth)
        except Exception: out[("dict_" + mode, 0, t)] = float("inf")
    return out


if __name__ == "__main__":
    with Pool(10) as P: R = P.map(work, range(30))
    keys = R[0].keys(); med = {k: float(np.median([min(r[k], 10) for r in R])) for k in keys}
    cfg = dict(lam_narx=min([k for k in keys if k[0] == "narx"], key=lambda k: med[k])[1], sindy={})
    for mode in MODES: cfg["sindy"][mode] = list(min([k for k in keys if k[0] == mode], key=lambda k: med[k])[1:])
    cfg["sindy_dict"] = {m: min([k for k in keys if k[0] == "dict_" + m], key=lambda k: med[k])[2] for m in MODES}
    json.dump(cfg, open(f"{HERE}/results/sdw_dev/tuned_config_ns24200.json", "w"), indent=1)
    json.dump({str(k): v for k, v in med.items()}, open(f"{HERE}/results/sdw_dev/tuning_median_rmse_ns24200.json", "w"), indent=1)
    print(cfg); [print(k, round(v, 4)) for k, v in sorted(med.items(), key=lambda q: q[1])[:12]]
