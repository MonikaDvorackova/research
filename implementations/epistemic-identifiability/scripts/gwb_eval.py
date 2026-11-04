"""Evaluate trained gwb world models: predictive metrics, structural readout under interaction conditions,
non-identifiable controls, baselines and leak controls.  Development only.

usage: python scripts/gwb_eval.py --groups name=dir1,dir2,dir3 ... --ns 9300 --out results/gwb_dev/eval_x.json
"""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.gwb import gen, agents, evalcore as ev, train as tr

CONDS = ["passive", "uniform", "sweep", "randblock", "oracle_eig", "ens_disagree"]
L = 48
CLF = None


def load(d):
    cfg = json.load(open(os.path.join(d, "config.json")))
    m = tr.build(cfg["model"], cfg["H"]); m.load_state_dict(torch.load(os.path.join(d, "final.pt"))); m.eval()
    return m, cfg


def sets(ns, n_id=800, n_other=500, family="both"):
    return {
        "id": gen.sample_instances(n_id, "train", family=family, seed=ns + 0),
        "hoparam": gen.sample_instances(n_other, "hoparam", family=family, seed=ns + 1),
        "hosigma": gen.sample_instances(n_other, "train", family=family, sigma=(0.3, 0.4), seed=ns + 2),
        "eqA": gen.sample_instances(n_other, "eqA", seed=ns + 3),
        "eqB": gen.sample_instances(n_other, "eqB", seed=ns + 4),
    }


def predictive(model, ns):
    out = {}
    for kind in ("uniform", "sweep"):
        inst = gen.sample_instances(600, "train", seed=ns + 20)
        g = torch.Generator().manual_seed(ns + 21)
        u, y = agents.interact({"uniform": "uniform", "sweep": "sweep"}[kind], inst, L, g)
        x = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u)
        with torch.no_grad():
            h, z, mu, ls = model.filter(u.float(), y.float())
            nll = ev_nll(y.float(), mu, ls)
            h, z, _, _ = model.filter(u[:, :24].float(), y[:, :24].float())
            roll = model.rollout(h, z, u[:, 24:40].float()).double()
        floor = (inst["sigma"].log() + 0.5 * np.log(2 * np.pi * np.e)).mean().item()
        sd = ((mu.double() - y) / ls.exp().double())
        out[kind] = dict(nll=float(nll), nll_floor=floor, excess_nll=float(nll) - floor,
                         cover90=float((sd.abs() < 1.645).double().mean()),
                         rollout16_rmse=float(((roll - x[:, 24:40]) ** 2).mean().sqrt()),
                         rollout16_rmse_over_sigma=float((((roll - x[:, 24:40]) ** 2).mean(1).sqrt() / inst["sigma"]).mean()))
    return out


def ev_nll(y, mu, ls):
    return (0.5 * ((y - mu) / ls.exp()) ** 2 + ls + 0.5 * np.log(2 * np.pi)).mean()


def collect(cond, S, probe_inst, ns, ens=None):
    """Interact on probe-train and all test sets under a condition; return dict name -> (inst,u,y)."""
    data = {}
    for name, inst in [("probe", probe_inst)] + list(S.items()):
        g = torch.Generator().manual_seed(ns + 100 + sorted(list(S) + ["probe"]).index(name))
        u, y = agents.interact(cond, inst, L, g, models=ens)
        data[name] = (inst, u, y)
    return data


def readout(models, data, probe_inst_eqA=None):
    """Fit probe on 'probe' trajectories; evaluate on all sets. Also E-aware probe variant."""
    res = {}
    inst, u, y = data["probe"]
    lab = inst["label"].numpy()
    Fp = ev.feats_model(models, u, y)
    for variant in ("plain", "withEA"):
        Ftr, ltr = Fp, lab
        if variant == "withEA":
            ie, ue, ye = data["probeEA"]
            Fe = ev.feats_model(models, ue, ye)
            # equivalent worlds appear with BOTH members of the equivalence class as labels (soft 50/50)
            Ftr = np.concatenate([Fp, Fe, Fe]); ltr = np.concatenate([lab, np.ones(len(Fe), int), 2 * np.ones(len(Fe), int)])
        probe = ev.fit_probe(Ftr, ltr)
        r = {}
        for name in ("id", "hoparam", "hosigma"):
            i2, u2, y2 = data[name]
            pr = ev.probe_probs(probe, ev.feats_model(models, u2, y2))
            m = ev.metrics_id(pr, i2["label"].numpy()); m["acc_ci"] = ev.bootstrap_ci((pr.argmax(1) == i2["label"].numpy()).astype(float))
            r[name] = m
        for name in ("eqA", "eqB"):
            i2, u2, y2 = data[name]
            r[name] = ev.metrics_eq(ev.probe_probs(probe, ev.feats_model(models, u2, y2)))
        res[variant] = r
    return res


def oracle_and_baselines(data):
    out = {}
    r = {}
    for name in ("id", "hoparam", "hosigma"):
        i2, u2, y2 = data[name]
        pr = ev.oracle_probs(i2, u2, y2)
        m = ev.metrics_id(pr, i2["label"].numpy()); m["acc_ci"] = ev.bootstrap_ci((pr.argmax(1) == i2["label"].numpy()).astype(float)); r[name] = m
    for name in ("eqA", "eqB"):
        i2, u2, y2 = data[name]
        r[name] = ev.metrics_eq(ev.oracle_probs(i2, u2, y2))
    out["oracle_bayes"] = r
    r = {}
    for name in ("id", "hoparam", "hosigma"):
        i2, u2, y2 = data[name]
        pr = ev.oracle_probs(i2, u2, y2, matched=True)
        m = ev.metrics_id(pr, i2["label"].numpy()); m["acc_ci"] = ev.bootstrap_ci((pr.argmax(1) == i2["label"].numpy()).astype(float)); r[name] = m
    out["oracle_matched_prior"] = r
    # hand-feature gradient boosting (strong non-neural), trained on probe set
    from sklearn.ensemble import HistGradientBoostingClassifier
    ip, up, yp = data["probe"]
    clf = HistGradientBoostingClassifier(max_iter=200, random_state=0).fit(ev.hand_features(up, yp), ip["label"].numpy())
    r = {}
    for name in ("id", "hoparam", "hosigma"):
        i2, u2, y2 = data[name]
        pr = np.zeros((len(y2), gen.NCLS)); pr[:, clf.classes_] = clf.predict_proba(ev.hand_features(u2, y2))
        r[name] = ev.metrics_id(pr, i2["label"].numpy())
    for name in ("eqA", "eqB"):
        i2, u2, y2 = data[name]
        pr = np.zeros((len(y2), gen.NCLS)); pr[:, clf.classes_] = clf.predict_proba(ev.hand_features(u2, y2)); r[name] = ev.metrics_eq(pr)
    out["handfeat_gbm"] = r
    if CLF is not None:
        r = {}
        with torch.no_grad():
            for name in ("id", "hoparam", "hosigma", "eqA", "eqB"):
                i2, u2, y2 = data[name]
                pr = torch.softmax(CLF(u2.float(), y2.float()), -1).numpy()
                r[name] = ev.metrics_id(pr, i2["label"].numpy()) if name in ("id", "hoparam", "hosigma") else ev.metrics_eq(pr)
        out["supervised_gru"] = r
    # leak control: actions only
    clf = HistGradientBoostingClassifier(max_iter=100, random_state=0).fit(up.numpy(), ip["label"].numpy())
    i2, u2, y2 = data["id"]
    out["leak_actions_only_acc"] = float((clf.predict(u2.numpy()) == i2["label"].numpy()).mean())
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", nargs="+", required=True)
    ap.add_argument("--ns", type=int, default=9200)
    ap.add_argument("--conds", nargs="+", default=CONDS)
    ap.add_argument("--n_probe", type=int, default=1500)
    ap.add_argument("--out", required=True)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--classifier", default=None)
    ap.add_argument("--family", default="both")
    a = ap.parse_args()
    global CLF
    if a.classifier:
        from eid.gwb import models
        CLF = models.ClassifierGRU(); CLF.load_state_dict(torch.load(os.path.join(a.classifier, "final.pt"))); CLF.eval()
    torch.set_num_threads(a.threads)
    groups = {}
    for g in a.groups:
        name, dirs = g.split("="); groups[name] = [load(d) for d in dirs.split(",")]
    S = sets(a.ns, family=a.family)
    probe_inst = gen.sample_instances(a.n_probe, "train", family=a.family, seed=9100 + (a.ns - 9200))
    probe_ea = gen.sample_instances(300, "eqA", seed=9150 + (a.ns - 9200))
    results = dict(ns=a.ns, groups={k: [c for _, c in v] for k, v in groups.items()}, predictive={}, structural={}, baselines={}, timing={})
    for name, ms in groups.items():
        results["predictive"][name] = [predictive(m, a.ns) for m, _ in ms]
    for cond in a.conds:
        t = time.time()
        # learned-ensemble condition: use the group's ensemble (members = seeds of that group)
        cond_groups = [None] if cond != "ens_disagree" else list(groups)
        for cg in cond_groups:
            data = collect(cond, S, probe_inst, a.ns, ens=[m for m, _ in groups[cg]] if cg else None)
            if cond == "ens_disagree":
                g = torch.Generator().manual_seed(a.ns + 777)
                data["probeEA"] = (probe_ea, *agents.interact(cond, probe_ea, L, g, models=[m for m, _ in groups[cg]]))
            else:
                g = torch.Generator().manual_seed(a.ns + 777)
                data["probeEA"] = (probe_ea, *agents.interact(cond, probe_ea, L, g))
            key = cond if cg is None else f"{cond}[{cg}]"
            results["structural"][key] = {}
            for name, ms in groups.items():
                if cg is not None and name != cg: continue
                results["structural"][key][name] = [readout(m, data) for m, _ in ms]
            results["baselines"][key] = oracle_and_baselines(data)
        results["timing"][cond] = time.time() - t
        print(cond, f"{time.time()-t:.0f}s", flush=True)
        json.dump(results, open(a.out, "w"))
    json.dump(results, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
