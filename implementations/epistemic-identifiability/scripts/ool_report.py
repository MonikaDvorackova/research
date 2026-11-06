"""Analysis of an OOL run, implementing the decision rules of doc 23.
usage: ool_report.py --run results/ool_dev/dev_ns30000.pkl [--pysr results/ool_dev/dev_pysr.pkl] --cal results/ool_dev/calibration_ns29000.json --out results/ool_dev/dev_report"""
import sys, os, json, pickle, argparse, itertools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, pandas as pd
from eid.ool import bench, evals, loop

ap = argparse.ArgumentParser(); ap.add_argument("--run", required=True); ap.add_argument("--pysr", default=None); ap.add_argument("--cal", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--title", default="OOL development run"); a = ap.parse_args()
cal = json.load(open(a.cal)); run = pickle.load(open(a.run, "rb")); res = run["res"]; rng = np.random.default_rng(7)
IOOL = {"sin", "rectsq", "leak", "bilin", "bump", "sqrtabs", "rate", "gdelay", "quadlag"}                  # identifiable out-of-L0
NONID = {"thresh", "bumpfar"}; BEYOND = {"saw"}; CTRL = {"lin", "sat", "quad", "gate", "delay"}
rows = []
for r in res:
    fam, inst = r["fam"], r["inst"]
    for name, byB in r["agents"].items():
        for B, rec in byB.items():
            dec_full = loop.decide(rec, cal, "full"); dec_in = loop.decide(rec, cal, "crit_in") if False else loop.decide(rec, cal, "nocrit")
            l2 = evals.level2(fam, rec["desc"]); l3 = evals.level3(fam, inst, rec["terms"], rec["gamma"], rec["desc"])
            rows.append(dict(fam=fam, k=r["k"], method=name, B=B, rmse=rec["rmse"], ok=rec["ok"], l2=l2, l3=l3, dec=dec_full, ncol=rec["ncol"], wall=rec["wall"], label=rec["label"], stage=rec["stage_used"],
                             s_in=rec["s_in"], s_oos=rec["s_oos"], amb=rec["amb_ratio"], nstage=rec["nstage"], nnew=rec["nnew"], rmse_l0=rec.get("rmse_l0")))
    for B, rec in r.get("oracle", {}).items():
        rows.append(dict(fam=fam, k=r["k"], method="oracle_struct", B=B, rmse=rec["rmse"], ok=rec["rmse"] <= loop.TAU, l2=evals.level2(fam, rec["desc"]),
                         l3=evals.level3(fam, inst, rec["terms"], rec["gamma"], rec["desc"]), dec="claim", ncol=np.nan, wall=np.nan, label=rec["label"]))
    for name, byB in r.get("base", {}).items():
        for B, rec in byB.items(): rows.append(dict(fam=fam, k=r["k"], method=name, B=B, rmse=rec["rmse"], ok=rec["ok"], l2=np.nan, l3=np.nan, dec="", ncol=np.nan, wall=rec["wall"], diverged=rec["diverged"]))
if a.pysr:
    for o in pickle.load(open(a.pysr, "rb"))["res"]:
        for (B, src, lib), rec in o["pysr"].items():
            rows.append(dict(fam=o["fam"], k=o["k"], method=f"pysr_{lib}_{src}", B=B, rmse=rec["rmse"], ok=rec["ok"], l2=np.nan if rec["struct"] is None else bool(rec["struct"]), l3=np.nan, dec="", ncol=np.nan,
                             wall=rec["wall"] + rec.get("fit_wall", 0.0), label=rec["eq"][:60]))
df = pd.DataFrame(rows); df["uid"] = df["fam"] + "|" + df["k"].astype(str)


def boot(vals_by_fam, f, n=10000):
    """vals_by_fam: {fam: array of per-instance values (or tuples)}; stratified percentile bootstrap of f(list of concatenated resampled values)."""
    fams = list(vals_by_fam); out = np.empty(n)
    for i in range(n): out[i] = f(np.concatenate([vals_by_fam[g][rng.integers(0, len(vals_by_fam[g]), len(vals_by_fam[g]))] for g in fams]))
    return float(np.mean(f(np.concatenate([vals_by_fam[g] for g in fams])))), float(np.quantile(out, .025)), float(np.quantile(out, .975))


def rate(method, B, fams, col="ok"):
    d = df[(df.method == method) & (df.B == B) & (df.fam.isin(fams))]
    if d.empty or d[col].isna().all(): return None
    v = {g: x[col].astype(float).values for g, x in d.groupby("fam")}; return boot(v, np.mean, 4000)


def pdiff(ma, mb, B, fams, col="ok"):
    """paired difference ma - mb on the same instances."""
    A = df[(df.method == ma) & (df.B == B) & (df.fam.isin(fams))].set_index("uid"); Bd = df[(df.method == mb) & (df.B == B) & (df.fam.isin(fams))].set_index("uid")
    ids = A.index.intersection(Bd.index)
    if len(ids) == 0 or A.loc[ids, col].isna().all() or Bd.loc[ids, col].isna().all(): return None
    d = (A.loc[ids, col].astype(float) - Bd.loc[ids, col].astype(float)); fam = A.loc[ids, "fam"]
    v = {g: d[fam == g].values for g in fam.unique()}; return boot(v, np.mean, 4000) + (len(ids),)


fmt = lambda t: "n/a" if t is None else f"{t[0]:.2f} [{t[1]:.2f},{t[2]:.2f}]"
fams_present = sorted(df.fam.unique()); ioo = [f for f in fams_present if f in IOOL]; out = [f"# {a.title}", "", f"Manifest sha256: `{run['manifest_sha']}`; instances: {len(res)}; families: {', '.join(fams_present)}. Cal thresholds: c_in={cal['in']}, c_oos={cal['oos']}.", ""]
Bs = sorted(df.B.unique()); AG = [m for m in df.method.unique() if m.startswith(("adapt_", "L0_", "all_", "ord_", "oracle"))]
BL = [m for m in df.method.unique() if m not in AG]

# 1. per-family L1/L2 table for the main contenders
out += ["## 1. Per-family recovery (L1 predictive = RMSE<=0.05; L2 structural = signature match), B=8 and 12", ""]
main = [m for m in ["adapt_sweepB", "adapt_falsify", "L0_sweepB", "all_sweepB", "oracle_struct", "pysr_fixed_kalman", "pysr_expanded_kalman", "pysr_expanded_learned", "pysr_expanded_oracle", "pysr_expanded_raw",
                    "sindyc_kalman", "sindyc_oracle", "weak_kalman", "implicit_kalman", "narx", "hammerstein"] if m in df.method.unique()]
for B in (8, 12):
    out += [f"### B={B}", "", "| method | " + " | ".join(f"{f} L1/L2" for f in fams_present) + " |", "|---|" + "---|" * len(fams_present)]
    for m in main:
        cells = []
        for f in fams_present:
            d = df[(df.method == m) & (df.B == B) & (df.fam == f)]
            if d.empty: cells.append("-"); continue
            l1 = d.ok.astype(float).mean(); l2 = d.l2.astype(float).mean() if d.l2.notna().any() else None
            cells.append(f"{l1:.1f}/{'' if l2 is None else f'{l2:.1f}'}")
        out.append(f"| {m} | " + " | ".join(cells) + " |")
    out.append("")

# 2. pooled identifiable-out-of-L0 rates
out += ["## 2. Pooled over identifiable out-of-L0 mechanisms (95% stratified bootstrap over instances)", "", "| method | " + " | ".join(f"B={B} L1 | B={B} L2" for B in (5, 8, 12)) + " |", "|---|" + "---|---|" * 3]
for m in main:
    out.append(f"| {m} | " + " | ".join(f"{fmt(rate(m, B, ioo, 'ok'))} | {fmt(rate(m, B, ioo, 'l2'))}" for B in (5, 8, 12)) + " |")
out.append("")

# 3. H1 paired differences
out += ["## 3. H1 - paired differences, adapt_sweepB minus competitor (identifiable out-of-L0 pooled)", "", "| competitor | B | dL1 | dL2 (competitor L2 only where defined) | n |", "|---|---|---|---|---|"]
for m in [x for x in main if x not in ("adapt_sweepB",)]:
    for B in (8, 12):
        p1 = pdiff("adapt_sweepB", m, B, ioo, "ok"); p2 = pdiff("adapt_sweepB", m, B, [f for f in ioo if not df[(df.method == m) & (df.fam == f)].l2.isna().all()] if m in df.method.unique() else ioo, "l2")
        if p1: out.append(f"| {m} | {B} | {fmt(p1[:3])} | {fmt(p2[:3]) if p2 else 'n/a'} | {p1[3]} |")
out.append("")

# 4. efficiency
out += ["## 4. Cost per instance (median) at B=12: candidate columns evaluated (cumulative over all revisions) and wall-clock of the fit (agent: cumulative discovery time; baselines: fit+rollout time)", "", "| method | candidates | wall s |", "|---|---|---|"]
for m in main:
    d = df[(df.method == m) & (df.B == 12) & (df.fam.isin(ioo))]
    if not d.empty: out.append(f"| {m} | {d.ncol.median():.0f} | {d.wall.median():.1f} |")
out.append("")

# 5. criticism
out += ["## 5. Model criticism (H4)", "", "False rejection of a correct L0 explanation on dev controls (lin) and power against out-of-L0 (L0_sweepB, c_in threshold; statistic = best-L0 s_in)", "", "| B | false rejection (lin) | power out-of-L0 | median s_in lin | median s_in out-of-L0 | AUROC |", "|---|---|---|---|---|---|"]
from sklearn.metrics import roc_auc_score
for B in (5, 8, 12):
    d = df[(df.method == "L0_sweepB") & (df.B == B)]
    if d.empty: continue
    lin = d[d.fam == "lin"]; oo = d[d.fam.isin(ioo)]
    thr = cal["in"][str(B)]
    au = roc_auc_score(np.r_[np.zeros(len(lin)), np.ones(len(oo))], np.r_[lin.s_in, oo.s_in]) if len(lin) and len(oo) else float("nan")
    out.append(f"| {B} | {(lin.s_in > thr).mean():.2f} | {(oo.s_in > thr).mean():.2f} | {lin.s_in.median():.2f} | {oo.s_in.median():.2f} | {au:.2f} |")
out += ["", "Per-family L0 rejection rate at c_in:", "", "| B | " + " | ".join(fams_present) + " |", "|---|" + "---|" * len(fams_present)]
for B in (5, 8, 12):
    d = df[(df.method == "L0_sweepB") & (df.B == B)]; thr = cal["in"][str(B)]
    if not d.empty: out.append(f"| {B} | " + " | ".join(f"{(d[d.fam == f].s_in > thr).mean():.2f}" for f in fams_present) + " |")
out.append("")

# 6. decisions
out += ["## 6. Epistemic decisions of the full agent (adapt_falsify, calibrated criticism): counts of claim / abstain_amb / abstain_ool, with claim correctness (L2) and false-discovery rate", ""]
out += ["| family | B | claim_correct | claim_wrong | abstain_amb | abstain_ool |", "|---|---|---|---|---|---|"]
tot = {B: dict(cc=0, cw=0) for B in (5, 8, 12)}
for f in fams_present:
    for B in (5, 8, 12):
        d = df[(df.method == "adapt_falsify") & (df.B == B) & (df.fam == f)]
        if d.empty: continue
        cl = d[d.dec == "claim"]; cc = int(cl.l2.astype(bool).sum()); cw = len(cl) - cc
        out.append(f"| {f} | {B} | {cc} | {cw} | {(d.dec == 'abstain_amb').sum()} | {(d.dec == 'abstain_ool').sum()} |"); tot[B]["cc"] += cc; tot[B]["cw"] += cw
out += ["", "Pooled false-discovery rate among claims (wrong-structure claims / all claims): " + ", ".join(f"B={B}: {t['cw']}/{t['cw']+t['cc']}" for B, t in tot.items()), ""]

# 7. H3 design: first budget with a correct claim
out += ["## 7. H3 - first budget at which the agent holds a correct claim (claim and L2; 16 if never), identifiable out-of-L0, mean over instances", "", "| design | mean first-correct B | paired diff vs falsify [95%] |", "|---|---|---|"]
def first_correct(meth):
    d = df[(df.method == meth) & (df.fam.isin(ioo))]; o = {}
    for uid, g in d.groupby("uid"):
        ok = g[(g.dec == "claim") & g.l2.astype(bool)].B; o[uid] = float(ok.min()) if len(ok) else 16.0
    return pd.Series(o)
fc = {m: first_correct(m) for m in ("adapt_falsify", "adapt_sweepB", "adapt_random", "adapt_ens") if m in df.method.unique()}
for m, s in fc.items():
    if m == "adapt_falsify" or "adapt_falsify" not in fc: out.append(f"| {m} | {s.mean():.2f} | - |"); continue
    ids = s.index.intersection(fc["adapt_falsify"].index); d = (fc["adapt_falsify"][ids] - s[ids]); fam = pd.Series([i.split("|")[0] for i in ids], index=ids)
    out.append(f"| {m} | {s.mean():.2f} | {fmt(boot({g: d[fam == g].values for g in fam.unique()}, np.mean, 4000))} (falsify minus {m}; negative favours falsify) |")
out.append("")

# 8. world model
out += ["## 8. Learned world model (H2)", "", "| comparison | B | dL1 [95%] | dL2 [95%] |", "|---|---|---|---|"]
for ma, mb in [("pysr_expanded_learned", "pysr_expanded_kalman"), ("pysr_fixed_learned", "pysr_fixed_kalman"), ("sindyc_learned", "sindyc_kalman"), ("weak_learned", "weak_kalman"),
               ("ord_learned_sweepB", "adapt_sweepB"), ("ord_kalman_sweepB", "adapt_sweepB"), ("ord_learned_sweepB", "ord_kalman_sweepB"), ("pysr_expanded_kalman", "pysr_expanded_raw"), ("pysr_expanded_oracle", "pysr_expanded_kalman")]:
    for B in (8, 12):
        p1 = pdiff(ma, mb, B, ioo, "ok"); p2 = pdiff(ma, mb, B, ioo, "l2")
        if p1: out.append(f"| {ma} - {mb} | {B} | {fmt(p1[:3])} | {fmt(p2[:3]) if p2 else 'n/a'} |")
out += ["", "Stage ordering by equation-error evidence (candidates evaluated, median, B=12, identifiable out-of-L0): " + ", ".join(
    f"{m}: {df[(df.method == m) & (df.B == 12) & (df.fam.isin(ioo))].ncol.median():.0f}" for m in ("adapt_sweepB", "ord_kalman_sweepB", "ord_learned_sweepB", "all_sweepB") if m in df.method.unique()), ""]

# 9. predictive vs structural vs mechanistic
out += ["## 9. Levels of success for the full agent (adapt_sweepB, identifiable out-of-L0 pooled)", "", "| B | L1 predictive | L2 structural | L3 mechanistic | predictive-but-not-structural |", "|---|---|---|---|---|"]
for B in (5, 8, 12):
    d = df[(df.method == "adapt_sweepB") & (df.B == B) & (df.fam.isin(ioo))]
    if not d.empty: out.append(f"| {B} | {fmt(rate('adapt_sweepB', B, ioo, 'ok'))} | {fmt(rate('adapt_sweepB', B, ioo, 'l2'))} | {fmt(rate('adapt_sweepB', B, ioo, 'l3'))} | {((d.ok) & (~d.l2.astype(bool))).mean():.2f} |")
out += ["", "Baseline divergence flags (fraction of rollouts flagged diverged): " + ", ".join(f"{m}: {df[(df.method == m)].get('diverged', pd.Series([np.nan])).astype(float).mean():.2f}" for m in BL if m in ("sindyc_kalman", "weak_kalman", "implicit_kalman")), ""]

# 10. L0 vs expansions
out += ["## 10. Fixed-language search vs adaptive expansion (same data, B=12): RMSE medians", "", "| family | L0_sweepB | adapt_sweepB | all_sweepB | expansion stage used (adapt_sweepB, mode) |", "|---|---|---|---|---|"]
for f in fams_present:
    g = lambda m: df[(df.method == m) & (df.B == 12) & (df.fam == f)]
    st = g("adapt_sweepB").stage.astype(str)
    out.append(f"| {f} | {g('L0_sweepB').rmse.median():.3f} | {g('adapt_sweepB').rmse.median():.3f} | {g('all_sweepB').rmse.median():.3f} | {(st.mode().iloc[0] if len(st.mode()) else '') if len(st) else ''} |")
open(a.out + ".md", "w").write("\n".join(out)); df.to_pickle(a.out + "_long.pkl"); print("\n".join(out))
