"""Calibration follow-up (doc 19 addendum B): empirical-null threshold on the in-sample misfit statistic from valid KNOWN-family fits (ns 27000),
applied to a fresh evaluation (ns 28000).  usage: sdw_calib_report.py calib.pkl test.pkl out.md"""
import sys, os, pickle, json, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from eid.sdw import env, agent as A
cal = pickle.load(open(sys.argv[1], "rb"))["res"]; tst = sorted(pickle.load(open(sys.argv[2], "rb"))["res"], key=lambda r: r["k"])
fam = np.array([r["fam"] for r in tst]); N = len(tst); rng = np.random.default_rng(1); NB = 10000
stat = lambda rec: -np.log10(max(rec["p_in"], 1e-300))
L = []; P = L.append; J = {}
P(f"# Calibrated criticism follow-up: calibration ns 27000 ({len(cal)} valid known-family instances), test ns 28000 ({N} instances, {N//9} per family)\n")
thr = {}
for d in ("falsify", "sweepB"):
    for B in (3, 5, 8):
        s = np.sort([stat(r["agents"][d][B]) for r in cal]); n = len(s); k = min(math.ceil((n + 1) * 0.95), n) - 1; thr[(d, B)] = float(s[k])
P("Threshold on -log10 p_in (95% empirical quantile of valid fits), by design and B:\n\n| design | B=3 | B=5 | B=8 |\n|---|---|---|---|")
for d in ("falsify", "sweepB"): P(f"| {d} | " + " | ".join(f"{thr[(d,B)]:.2f}" for B in (3, 5, 8)) + f" |  (uncalibrated rule corresponds to {-np.log10(0.01/3):.2f} / {-np.log10(0.01/5):.2f} / {-np.log10(0.01/8):.2f})")
def outcome(rec, d, mode):
    if mode == "nocrit": return "claim"
    if mode == "cal": rej = stat(rec) > thr[(d, rec["B"])]
    elif mode == "uncal": rej = A.outcome(rec, "crit_in") == "abstain_ool"
    else: rej = A.outcome(rec, "full") == "abstain_ool"
    if rej: return "abstain_ool"
    return "abstain_amb" if rec["amb_ratio"] > A.EPS else "claim"
def ci(x, m):
    x = np.asarray(x, float)[m]; idx = rng.integers(0, len(x), (NB, len(x))); b = x[idx].mean(1); return f"{x.mean():.2f} [{np.percentile(b,2.5):.2f},{np.percentile(b,97.5):.2f}]"
def paired(x, y):
    z = np.asarray(x, float) - np.asarray(y, float); idx = rng.integers(0, N, (NB, N)); b = z[idx].mean(1); return f"{z.mean():+.3f} [{np.percentile(b,2.5):+.3f},{np.percentile(b,97.5):+.3f}]"
m = dict(known=np.isin(fam, env.KNOWN), unf=np.isin(fam, env.UNFAMILIAR), osc=fam == "osc", unr=fam == "unreach")
P("\n| design | B | rule | false rejection known | false rejection unfamiliar | osc claim rate | unreach claim&ok | coverage (in-lang) | precision | decision accuracy |\n|---|---|---|---|---|---|---|---|---|---|")
acc = {}
for d in ("falsify", "sweepB"):
    for B in (3, 5, 8):
        ok = np.array([r["agents"][d][B]["ok"] for r in tst]).astype(float)
        for mode in ("nocrit", "full", "uncal", "cal"):
            o = np.array([outcome(r["agents"][d][B], d, mode) for r in tst]); claim = (o == "claim").astype(float); rej = (o == "abstain_ool").astype(float)
            right = np.where(fam == "osc", 1 - claim, claim * ok); acc[(d, B, mode)] = right; inl = np.isin(fam, env.INLANG)
            prec = (claim * ok)[inl].sum() / max(claim[inl].sum(), 1)
            P(f"| {d} | {B} | {mode} | {ci(rej, m['known'])} | {ci(rej, m['unf'])} | {ci(claim, m['osc'])} | {ci(claim*ok, m['unr'])} | {ci(claim, inl)} | {prec:.2f} | {right.mean():.2f} |")
            J[f"{d}/{B}/{mode}"] = dict(fr_known=float(rej[m['known']].mean()), fr_unf=float(rej[m['unf']].mean()), osc_claim=float(claim[m['osc']].mean()), acc=float(right.mean()))
P("\nPaired decision-accuracy differences at B=8 (all 9 families): " + "; ".join(f"{d}: cal minus nocrit {paired(acc[(d,8,'cal')], acc[(d,8,'nocrit')])}, cal minus uncal {paired(acc[(d,8,'cal')], acc[(d,8,'uncal')])}" for d in ("falsify", "sweepB")))
fr = J["falsify/8/cal"]; meet = fr["fr_unf"] <= 0.10 and fr["osc_claim"] <= 0.20 and fr["acc"] >= J["falsify/8/nocrit"]["acc"]
P(f"\n**Pre-fixed success rule for 'calibration artefact' (falsify, B=8): false rejection unfamiliar {fr['fr_unf']:.2f} (<=0.10?), osc claim rate {fr['osc_claim']:.2f} (<=0.20?), accuracy {fr['acc']:.2f} vs no-criticism {J['falsify/8/nocrit']['acc']:.2f} => {'MET' if meet else 'NOT MET'}**")
J["calibration_artefact_rule_met"] = bool(meet); J["thr"] = {f"{k[0]}/{k[1]}": v for k, v in thr.items()}
json.dump(J, open(sys.argv[3].replace(".md", ".json"), "w"), indent=1)
open(sys.argv[3], "w").write("\n".join(L)); print("\n".join(L))

# exploratory (not pre-registered): design effect in decision accuracy under the calibrated rule
P2 = ["", "**Exploratory (not pre-registered): falsify minus sweepB decision accuracy, same rule, paired over the 270 test instances**\n"]
for mode in ("cal", "nocrit"):
    P2.append(f"* {mode}: " + "; ".join(f"B={B} {paired(acc[('falsify',B,mode)], acc[('sweepB',B,mode)])}" for B in (3, 5, 8)))
print("\n".join(P2)); open(sys.argv[3], "a").write("\n".join(P2) + "\n")
