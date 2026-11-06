"""MDW evaluation. usage: mdw_eval.py --ns 23000 --n 40 --wm dirs --reg dirs --out file.json"""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.mdw import env, agents as A, model as M

BUDGETS = (2, 4, 8)


def load(dirs, reg=False):
    ms = []
    for d in dirs:
        H = json.load(open(os.path.join(d, 'config.json'))).get('H', 128); m = M.CtxGRU(H=H, n_desc=4 if reg else 0); m.load_state_dict(torch.load(os.path.join(d, "final.pt"))); m.eval(); ms.append(m)
    return ms


def boot_ci(v, n=1000, seed=0):
    v = np.asarray(v); rng = np.random.default_rng(seed); b = [v[rng.integers(0, len(v), len(v))].mean() for _ in range(n)]
    return [float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5))]


def auroc(pos, neg):
    from sklearn.metrics import roc_auc_score
    return float(roc_auc_score(np.r_[np.ones(len(pos)), np.zeros(len(neg))], np.r_[pos, neg]))


def evaluate(inst, eps, Urand, wms, regs, lam):
    N = inst["c"].shape[0]; Bmax = max(BUDGETS)
    true = env.true_descriptors(inst); res = {}; flags = {}
    Usw = A.sweep_programmes(N, Bmax)
    Usw_, Ysw = A.collect_fixed(inst, Usw, eps, Bmax); Ur_, Yr = A.collect_fixed(inst, Urand, eps, Bmax)
    # sequential planners
    g_planbed = None
    Upl, Ypl = torch.zeros(N, 0, env.T, 2, dtype=torch.float64), torch.zeros(N, 0, env.T, 2, dtype=torch.float64)
    Ubd, Ybd = Upl.clone(), Ypl.clone()
    plan_hist = {}
    for i in range(Bmax):
        j = A.wm_choose(wms, Upl, Ypl); prog = env.CANDS[j]
        Upl = torch.cat([Upl, prog[:, None]], 1); Ypl = torch.cat([Ypl, A.run_programmes(inst, prog, eps[:, i])[:, None]], 1)
        post, _ = A.bayes_post(Ubd, Ybd) if i > 0 else (torch.full((N, A.HN), 1.0 / A.HN, dtype=torch.float64), None)
        jb = A.bayes_choose(post); progb = env.CANDS[jb]
        Ubd = torch.cat([Ubd, progb[:, None]], 1); Ybd = torch.cat([Ybd, A.run_programmes(inst, progb, eps[:, i])[:, None]], 1)
    for B in BUDGETS:
        e = {}
        e["prior"] = A.DM[None].repeat(N, 1)
        e["direct(sweep)"] = A.est_direct(Usw_[:, :B], Ysw[:, :B])
        e["sysid(sweep)"] = A.est_sysid(Usw_[:, :B], Ysw[:, :B], lam); e["sysid(random)"] = A.est_sysid(Ur_[:, :B], Yr[:, :B], lam)
        bs, chi_s, _ = A.bayes_est(Usw_[:, :B], Ysw[:, :B]); bb, chi_b, _ = A.bayes_est(Ubd[:, :B], Ybd[:, :B])
        e["bayes(sweep)"], e["bayes(BED)"] = bs, bb
        for name, (U_, Y_) in dict(sweep=(Usw_, Ysw), random=(Ur_, Yr), plan=(Upl, Ypl)).items():
            d = A.wm_desc(wms, U_[:, :B], Y_[:, :B]); e[f"wm({name})"] = d.mean(0)
            if name == "plan" or name == "sweep": flags[(B, f"wm({name})")] = (d.std(0) / A.DS).mean(1)
        e["wm(no-context)"] = A.wm_desc(wms, Usw_[:, :0], Ysw[:, :0]).mean(0)
        e["reg(sweep)"] = A.reg_desc(regs, Usw_[:, :B], Ysw[:, :B]); e["reg(random)"] = A.reg_desc(regs, Ur_[:, :B], Yr[:, :B])
        flags[(B, "bayes(sweep)")] = chi_s; flags[(B, "bayes(BED)")] = chi_b
        for k, v in e.items():
            err = env.norm_err(v, true)
            res.setdefault(k, {})[B] = dict(err_desc=err.mean(0).tolist(), err_med=err.median(1).values.numpy().tolist(), err_all=err.mean(1).numpy().tolist())
    return res, flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ns", type=int, default=23000); ap.add_argument("--n", type=int, default=40)
    ap.add_argument("--wm", nargs="+", required=True); ap.add_argument("--reg", nargs="+", required=True)
    ap.add_argument("--lam", type=float, default=1.0); ap.add_argument("--threads", type=int, default=8); ap.add_argument("--out", required=True)
    a = ap.parse_args(); torch.set_num_threads(a.threads); t0 = time.time()
    wms, regs = load(a.wm), load(a.reg, True)
    sets = {"known": env.sample_instances(env.TRAIN_FAMS, a.n, a.ns), "gate": env.sample_instances(("gate",), a.n * 3, a.ns + 1),
            "backlash": env.sample_instances(("backlash",), a.n * 3, a.ns + 2)}
    out = dict(args=vars(a), sets={}, flags={})
    allflags = {}
    for name, inst in sets.items():
        N = inst["c"].shape[0]; g = torch.Generator().manual_seed(a.ns + 77 + len(name))
        eps = torch.randn(N, max(BUDGETS), env.T, 2, generator=g, dtype=torch.float64)
        Urand = torch.stack([env.random_programmes(N, g) for _ in range(max(BUDGETS))], 1)
        res, flags = evaluate(inst, eps, Urand, wms, regs, a.lam)
        out["sets"][name] = res; allflags[name] = flags; print(name, f"{time.time()-t0:.0f}s", flush=True)
    # epistemic flags: held-out vs known AUROC and correlation with error
    ep = {}
    for key in allflags["known"]:
        B, m = key
        kn = allflags["known"][key].numpy(); row = {}
        for h in ("gate", "backlash"):
            row[f"auroc_{h}_vs_known"] = auroc(allflags[h][key].numpy(), kn)
        ep[f"{m}@B{B}"] = row
    out["epistemic_flags"] = ep; out["seconds"] = time.time() - t0
    json.dump(out, open(a.out, "w"), indent=1, default=float); print("done", f"{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
