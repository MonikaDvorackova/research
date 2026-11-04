"""Interventional prediction on UNSEEN programmes (16 random programmes not in the probe/candidate sets), after B sweep episodes.
RMSE of predicted x3 vs true noiseless x3; methods that can predict: SysID, declared-class Bayes (posterior mean), world model ensemble, prior (mean traj)."""
import argparse, json, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.mdw import env, agents as A, model as M
ap = argparse.ArgumentParser(); ap.add_argument("--ns", type=int, default=23500); ap.add_argument("--n", type=int, default=40)
ap.add_argument("--wm", nargs="+", required=True); ap.add_argument("--tag", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
torch.set_num_threads(8)
wms = []
for d in a.wm:
    H = json.load(open(os.path.join(d, "config.json"))).get("H", 128); m = M.CtxGRU(H=H); m.load_state_dict(torch.load(os.path.join(d, "final.pt"))); m.eval(); wms.append(m)
g = torch.Generator().manual_seed(a.ns + 999)
progs = env.random_programmes(16, g)                                             # shared unseen programmes (u1 + u2 injection)
sets = {"known": env.sample_instances(env.TRAIN_FAMS, a.n, a.ns), "gate": env.sample_instances(("gate",), a.n * 3, a.ns + 1),
        "backlash": env.sample_instances(("backlash",), a.n * 3, a.ns + 2)}
grid_sims = torch.stack([env.simulate(A.GRID, progs[j][None].expand(A.HN, -1, -1))[..., 1] for j in range(16)], 1)       # [HN,16,T]
out = {}
for name, inst in sets.items():
    N = inst["c"].shape[0]; g2 = torch.Generator().manual_seed(a.ns + 77 + len(name))
    eps = torch.randn(N, 8, env.T, 2, generator=g2, dtype=torch.float64)
    truth = torch.stack([env.simulate(inst, progs[j][None].expand(N, -1, -1))[..., 1] for j in range(16)], 1)       # [N,16,T]
    prior = truth.mean(0, keepdim=True)                                       # (privileged-free proxy: mean over THIS set is optimistic; use training-set mean below)
    trn = env.sample_instances(env.TRAIN_FAMS, 60, 20500)
    prior = torch.stack([env.simulate(trn, progs[j][None].expand(trn["c"].shape[0], -1, -1))[..., 1].mean(0) for j in range(16)], 0)[None].expand(N, -1, -1)
    out[name] = {"prior(train-mean traj)": {}}
    for B in (2, 4, 8):
        U, Y = A.collect_fixed(inst, A.sweep_programmes(N, 8), eps, B)
        rm = lambda p: float(((p - truth) ** 2).mean((1, 2)).sqrt().mean())
        r = {"prior(train-mean traj)": rm(prior)}
        r["sysid"] = rm(A.sysid_rollout(A.sysid_fit(U, Y, 0.1), progs))
        post, chi2 = A.bayes_post(U, Y); r["bayes(declared)"] = rm(torch.einsum("nh,hpt->npt", post, grid_sims))
        r[f"wm-ensemble[{a.tag}]"] = rm(A.wm_rollout(wms, U, Y, progs)); r[f"wm-no-context[{a.tag}]"] = rm(A.wm_rollout(wms, U[:, :0], Y[:, :0], progs))
        for k, v in r.items(): out[name].setdefault(k, {})[B] = v
    print(name, {k: {b: round(x, 3) for b, x in v.items()} for k, v in out[name].items()}, flush=True)
json.dump(out, open(a.out, "w"), indent=1)
