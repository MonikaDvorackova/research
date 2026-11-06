"""Epistemic-abstention study (development). usage: epi_run.py --ns 11200 --scale 1.0 --out results/epi_dev/x.json"""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.gwb import gen, agents, epi, epi_agents as ea, evalcore as ev, models, policies, train as tr

L = 48
CATS = [("id", 800), ("idnoisy", 400), ("eqA", 400), ("eqB", 400), ("eqC", 400), ("eqD", 400), ("approx", 400),
        ("ooc_sat", 300), ("ooc_osc", 300), ("ooc_qd", 300)]
COV = 0.70


def make(kind, n, seed):
    inst = epi.sample_epi(n, kind, seed)
    g = torch.Generator().manual_seed(seed + 7)
    eps = torch.randn(n, L, generator=g, dtype=torch.float64)
    u0 = ea.passive_block(n, g)
    return dict(inst=inst, eps=eps, u0=u0, g=g)


def wilson(k, n, z=1.96):
    if n == 0: return [0, 0]
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d; h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [float(c - h), float(c + h)]


def sweep_data(D):
    u = policies.sample_actions("sweep", D["inst"]["K"].shape[0], L, D["g"])
    return u, epi.x_of(D["inst"], u) + D["inst"]["sigma"][:, None] * D["eps"]


def seq_data(D, chooser):
    return ea.run_seq(D["inst"], chooser, D["u0"], D["eps"])


def threshold_for_coverage(score, cov=COV):
    return float(np.quantile(score, 1 - cov))


def analyse(name, score_by_cat, pred_by_cat, t, inst_by_cat, extra=None):
    out = {}
    for cat, s in score_by_cat.items():
        claim = s >= t; inst = inst_by_cat[cat]; pred = pred_by_cat[cat]; n = len(s)
        row = dict(n=n, claim_rate=float(claim.mean()), claim_ci=wilson(int(claim.sum()), n))
        if cat in ("id", "idnoisy", "approx"):
            correct = pred == inst["cls"].numpy() if cat != "id" and cat != "idnoisy" else pred == inst["label"].numpy()
            row["acc_all"] = float(correct.mean()); row["wrong_claim_rate"] = float((claim & ~correct).mean())
            row["acc_among_claimed"] = float(correct[claim].mean()) if claim.any() else None
        elif cat.startswith("eq"):
            inm = np.array([bool(inst["eqmask"][i, pred[i]]) for i in range(n)])
            row["claim_of_equivalent_member"] = float((claim & inm).mean())     # right-by-luck, still unsupported
        out[cat] = row
    return out


def auroc(pos, neg):
    from sklearn.metrics import roc_auc_score
    y = np.r_[np.ones(len(pos)), np.zeros(len(neg))]; s = np.r_[pos, neg]
    return float(roc_auc_score(y, s))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ns", type=int, default=11200); ap.add_argument("--scale", type=float, default=1.0)
    ap.add_argument("--calns", type=int, default=11100); ap.add_argument("--threads", type=int, default=8)
    ap.add_argument("--wm", nargs="+", required=True); ap.add_argument("--cond", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(); torch.set_num_threads(a.threads)
    sc = lambda n: max(40, int(n * a.scale))
    wms = []
    for d in a.wm:
        m = tr.build("det", 128); m.load_state_dict(torch.load(os.path.join(d, "final.pt"))); m.eval(); wms.append(m)
    conds = []
    for d in a.cond:
        m = models.CondGRU(); m.load_state_dict(torch.load(os.path.join(d, "final.pt"))); m.eval(); conds.append(m)
    t_all = time.time(); R = dict(args=vars(a))
    # ---------------- datasets ----------------
    with epi.EpiGrid():
        test = {c: make(c, sc(n), a.ns + 10 * i) for i, (c, n) in enumerate(CATS)}
        cal = make("id", sc(1000), a.calns + 10); ptr = make("id", sc(1500), a.calns)
        expo = {k: make(k, sc(300), a.calns + 20 + j) for j, k in enumerate(("eqA", "eqB"))}
        inst_by = {c: D["inst"] for c, D in test.items()}
        lab = lambda i: i["label"].numpy()
        methods = {}                        # name -> dict(cal_score, cal_pred, score{cat}, pred{cat}, extra)
        # ---- fixed-sweep protocol datasets
        sw = {c: sweep_data(D) for c, D in test.items()}; swc = sweep_data(cal); swp = sweep_data(ptr)
        swe = {k: sweep_data(D) for k, D in expo.items()}
        # ---- probes M2/M3/M5/M6 on frozen prediction-trained world models
        feats = lambda m, u, y: ev.feats_model(m, u, y)
        P = {}
        for si, m in enumerate(wms):
            Ftr = feats(m, *swp); ltr = lab(ptr["inst"])
            pr_plain = ev.fit_probe(Ftr, ltr)
            Fe = [feats(m, *swe[k]) for k in swe]; le = []
            for k, D in expo.items():                  # ambiguity exposure: duplicate labels over the equivalence set
                em = D["inst"]["eqmask"].numpy(); le.append(em)
            Fx = np.concatenate([Ftr] + [np.repeat(F, 2, 0) for F in Fe]); lx = np.concatenate([ltr] + [np.concatenate([[np.where(em[i])[0][j] for j in range(2)] for i in range(len(em))]).reshape(-1) for em in le])
            pr_exp = ev.fit_probe(Fx, lx)
            Fc = feats(m, *swc); pc = ev.probe_probs(pr_plain, Fc)
            # temperature scaling on calibration set
            lg = np.log(np.clip(pc, 1e-9, 1)); labc = lab(cal["inst"])
            Ts = np.linspace(0.5, 4, 36); T = Ts[int(np.argmin([-np.mean(np.log(np.clip(torch.softmax(torch.tensor(lg / t_), 1).numpy()[np.arange(len(labc)), labc], 1e-9, 1))) for t_ in Ts]))]
            P[si] = dict(m=m, plain=pr_plain, exp=pr_exp, T=T, Fc=Fc, pc=pc, labc=labc)
        def probe_fn(kind, si, u, y):
            p = ev.probe_probs(P[si]["exp" if kind == "M5" else "plain"], feats(P[si]["m"], u, y))
            if kind == "M3": p = torch.softmax(torch.tensor(np.log(np.clip(p, 1e-9, 1)) / P[si]["T"]), 1).numpy()
            return p
        for kind in ("M2", "M3", "M5"):
            for si in P:
                pc = probe_fn(kind, si, *swc)
                methods[f"{kind}[s{si+1}]"] = dict(cal=(pc.max(1), pc.argmax(1)), test={c: (lambda p: (p.max(1), p.argmax(1)))(probe_fn(kind, si, *sw[c])) for c in test})
        # M6 ensemble average of plain probes
        ens = lambda u, y: np.mean([probe_fn("M2", si, u, y) for si in P], 0)
        pc = ens(*swc); methods["M6[ens3]"] = dict(cal=(pc.max(1), pc.argmax(1)), test={c: (lambda p: (p.max(1), p.argmax(1)))(ens(*sw[c])) for c in test})
        # M4 conformal (singleton rule) for each alpha, seed 1 probe
        conf = {}
        pc1 = P[0]["pc"]; labc = P[0]["labc"]
        for alpha in (0.05, 0.1, 0.2, 0.3):
            s = 1 - pc1[np.arange(len(labc)), labc]; n = len(s)
            q = np.quantile(s, min(1, np.ceil((n + 1) * (1 - alpha)) / n))
            rows = {}
            for c in test:
                p = probe_fn("M2", 0, *sw[c]); size = (1 - p <= q).sum(1); single = size == 1
                rows[c] = dict(singleton_rate=float(single.mean()), empty_rate=float((size == 0).mean()), mean_size=float(size.mean()))
                if c == "id": rows[c]["coverage_true"] = float(((1 - p[np.arange(len(p)), lab(inst_by[c])]) <= q).mean())
            conf[str(alpha)] = rows
        R["M4_conformal"] = conf
        # ---- M1 / M1s oracle
        orc_cal_seq = seq = None
        def oracle_pack(u_y_by, ucal_ycal):
            oc = ev.oracle_probs(cal["inst"], *ucal_ycal)
            return oc
        # sweep protocol
        o_sw = {c: ea.oracle_outputs(inst_by[c], *sw[c]) for c in test}; o_swc = ea.oracle_outputs(cal["inst"], *swc)
        methods["M1s[oracle,sweep]"] = dict(cal=(o_swc["post"].max(1), o_swc["post"].argmax(1)), test={c: (o["post"].max(1), o["post"].argmax(1)) for c, o in o_sw.items()}, aux={c: o for c, o in o_sw.items()}, auxcal=o_swc)
        # adaptive oracle
        g_or = torch.Generator().manual_seed(a.ns + 555)
        seq_or = {c: ea.run_seq(D["inst"], ea.oracle_chooser(g_or), D["u0"], D["eps"]) for c, D in test.items()}
        seq_orc = ea.run_seq(cal["inst"], ea.oracle_chooser(g_or), cal["u0"], cal["eps"])
        o_sq = {c: ea.oracle_outputs(inst_by[c], *seq_or[c]) for c in test}; o_sqc = ea.oracle_outputs(cal["inst"], *seq_orc)
        methods["M1[oracle,adaptive]"] = dict(cal=(o_sqc["post"].max(1), o_sqc["post"].argmax(1)), test={c: (o["post"].max(1), o["post"].argmax(1)) for c, o in o_sq.items()}, aux=o_sq, auxcal=o_sqc)
        # ---- M7 / M7s learned simulators
        for si, cm in enumerate(conds):
            o = {c: ea.m7_outputs(cm, *sw[c]) for c in test}; oc = ea.m7_outputs(cm, *swc)
            methods[f"M7s[cond{si+1},sweep]"] = dict(cal=(oc["post"].max(1), oc["post"].argmax(1)), test={c: (v["post"].max(1), v["post"].argmax(1)) for c, v in o.items()}, aux=o, auxcal=oc)
            seq = {c: ea.run_seq(D["inst"], ea.cond_chooser(cm), D["u0"], D["eps"]) for c, D in test.items()}
            seqc = ea.run_seq(cal["inst"], ea.cond_chooser(cm), cal["u0"], cal["eps"])
            o = {c: ea.m7_outputs(cm, *seq[c]) for c in test}; oc = ea.m7_outputs(cm, *seqc)
            methods[f"M7[cond{si+1},adaptive]"] = dict(cal=(oc["post"].max(1), oc["post"].argmax(1)), test={c: (v["post"].max(1), v["post"].argmax(1)) for c, v in o.items()}, aux=o, auxcal=oc)
        print("methods built", f"{time.time()-t_all:.0f}s", flush=True)
        # ---------------- analysis at matched coverage ----------------
        R["methods"] = {}
        for name, M in methods.items():
            t = threshold_for_coverage(M["cal"][0])
            sc_ = {c: M["test"][c][0] for c in test}; pr_ = {c: M["test"][c][1] for c in test}
            row = analyse(name, sc_, pr_, t, inst_by); row["threshold"] = t
            row["cal_acc"] = float((M["cal"][1] == lab(cal["inst"])).mean())
            pos = sc_["id"][pr_["id"] == lab(inst_by["id"])]
            neg = np.concatenate([sc_[c] for c in ("eqA", "eqB", "eqC", "eqD", "ooc_sat", "ooc_osc", "ooc_qd")])
            row["auroc_justified_vs_unjustified"] = auroc(pos, neg)
            row["auroc_justified_vs_unseen_eq"] = auroc(pos, np.concatenate([sc_["eqC"], sc_["eqD"]]))
            if "aux" in M:       # persistence flag and goodness-of-fit among abstentions
                gcal = M["auxcal"]["gof"]; gthr = float(np.quantile(gcal, 0.99)); row["gof_threshold"] = gthr
                reasons = {}
                for c in test:
                    abst = sc_[c] < t; aux = M["aux"][c]
                    persistent = aux["dmax"] < ea.DELTA_PERSIST; flagged = aux["gof"] > gthr
                    reasons[c] = dict(n_abstain=int(abst.sum()), persistent_frac=float(persistent[abst].mean()) if abst.any() else None,
                                      gof_flag_rate_all=float(flagged.mean()), median_dmax=float(np.median(aux["dmax"])))
                    # combined: claim only if score>=t AND not gof-flagged
                    row[c]["claim_rate_with_gof"] = float(((sc_[c] >= t) & ~flagged).mean())
                row["reasons"] = reasons
                # threshold-free persistence AUROC among abstentions: unseen-eq (eqC,eqD) should have SMALLER d_max than id/idnoisy
                ab = lambda c: M["aux"][c]["dmax"][sc_[c] < t]
                posd = np.concatenate([ab("eqC"), ab("eqD")]); negd = np.concatenate([ab("id"), ab("idnoisy")])
                row["persist_auroc_unseenEq_vs_id"] = auroc(-posd, -negd) if len(posd) > 5 and len(negd) > 5 else None
                row["persist_n"] = [int(len(posd)), int(len(negd))]
            R["methods"][name] = row
        # cost: earliest block with posterior >= tau for adaptive learned agent
        R["timing_s"] = time.time() - t_all
    json.dump(R, open(a.out, "w"), indent=1, default=float)
    print("done", f"{time.time()-t_all:.0f}s")


if __name__ == "__main__":
    main()
