"""Metrics, paired comparisons and equivalence tests for the Bayesian observer experiments (environment 1).
Usage: python -m eid.analyze_bayes1 --dir results/bayes1_dev --out results/bayes1_dev/analysis.md [--ck 2]"""
from __future__ import annotations

import argparse
import glob
import os

import numpy as np
from scipy import stats
from sklearn.metrics import roc_auc_score

from .metrics import bootstrap_ci

GROUPS = {0: ["E0", "E0split"], 1: ["W"], 2: ["AltOOD", "Ealt"]}


def load(d):
    out = {}
    for f in sorted(glob.glob(os.path.join(d, "seed*.npz"))):
        seed = int(os.path.basename(f)[4:-4])
        z = np.load(f)
        out[seed] = {k: z[k] for k in z.files}
    return out


def _g(arrs, regime, complete, pname, sc, pol, k):
    return arrs[f"{regime}|{complete}|{pname}|{sc}|{pol}|{k}"]


def _ece(conf, correct, w, bins=10):
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(conf, edges[1:-1]), 0, bins - 1)
    tot = w.sum()
    return float(sum(w[idx == b].sum() / tot * abs(np.average(conf[idx == b], weights=w[idx == b]) - np.average(correct[idx == b], weights=w[idx == b]))
                     for b in range(bins) if (idx == b).any()))


def metrics_seed(arrs, regime, policy, ck, complete="full", pname="uniform"):
    P = {c: np.concatenate([_g(arrs, regime, complete, pname, s, policy, "post")[:, ck] for s in sc if f"{regime}|{complete}|{pname}|{s}|{policy}|post" in arrs])
         for c, sc in GROUPS.items()}
    D = {c: np.concatenate([_g(arrs, regime, complete, pname, s, policy, "dec_time") for s in sc]) for c, sc in GROUPS.items()}
    DC = {c: np.concatenate([_g(arrs, regime, complete, pname, s, policy, "dec_class") for s in sc]) for c, sc in GROUPS.items()}
    present = [c for c in (0, 1, 2) if len(P[c])]
    acc = {c: float(np.mean(P[c].argmax(1) == c)) for c in present}
    ls = {c: float(np.mean(-np.log(np.clip(P[c][:, c], 1e-12, 1)))) for c in present}
    brier = {c: float(np.mean(np.sum((P[c] - np.eye(3)[c]) ** 2, axis=1))) for c in present}
    ent = {c: float(np.mean(-np.sum(np.where(P[c] > 0, P[c] * np.log(np.clip(P[c], 1e-300, 1)), 0), axis=1))) for c in present}
    conf = np.concatenate([P[c].max(1) for c in present])
    corr = np.concatenate([(P[c].argmax(1) == c).astype(float) for c in present])
    w = np.concatenate([np.full(len(P[c]), 1.0 / len(P[c])) for c in present])
    out = dict(acc3=float(np.mean(list(acc.values()))), acc_h0=acc.get(0, np.nan), acc_h1=acc.get(1, np.nan), acc_h2=acc.get(2, np.nan),
               logscore=float(np.mean(list(ls.values()))), brier=float(np.mean(list(brier.values()))), entropy=float(np.mean(list(ent.values()))),
               ece=_ece(conf, corr, w))

    def pair(pos_c, neg_c):
        if not (len(P[pos_c]) and len(P[neg_c])):
            return np.nan, np.nan
        sp = P[pos_c][:, pos_c] / np.maximum(P[pos_c][:, pos_c] + P[pos_c][:, neg_c], 1e-300)
        sn = P[neg_c][:, pos_c] / np.maximum(P[neg_c][:, pos_c] + P[neg_c][:, neg_c], 1e-300)
        ba = 0.5 * (np.mean(sp > 0.5) + np.mean(sn <= 0.5))
        au = roc_auc_score(np.r_[np.ones(len(sp)), np.zeros(len(sn))], np.r_[sp, sn])
        return float(ba), float(au)
    out["h1v0_bal_acc"], out["h1v0_auroc"] = pair(1, 0)
    out["h1v2_bal_acc"], out["h1v2_auroc"] = pair(1, 2)
    dec = {c: np.isfinite(D[c]) for c in present}
    out["decided"] = float(np.mean([dec[c].mean() for c in present]))
    out["false_id"] = float(np.nanmean([np.mean(DC[c][dec[c]] != c) if dec[c].any() else np.nan for c in present]))
    alltimes = np.concatenate([D[c][dec[c]] for c in present])
    out["median_time"] = float(np.median(alltimes)) if len(alltimes) else np.nan
    rg = np.concatenate([_g(arrs, regime, complete, pname, s, policy, "real_gain") for sc in GROUPS.values() for s in sc if f"{regime}|{complete}|{pname}|{s}|{policy}|post" in arrs])
    eg = np.concatenate([_g(arrs, regime, complete, pname, s, policy, "exp_gain") for sc in GROUPS.values() for s in sc if f"{regime}|{complete}|{pname}|{s}|{policy}|post" in arrs])
    out["real_gain"], out["exp_gain"] = float(rg.mean()), float(eg.mean())
    return out


def across_seeds(data, regime, policy, ck, **kw):
    rows = [metrics_seed(a, regime, policy, ck, **kw) for a in data.values()]
    return {m: np.array([r[m] for r in rows]) for m in rows[0]}


def tost_paired(d, margin, alpha=0.05):
    """Paired two one-sided tests: H0: |mean difference| >= margin. Returns the TOST p-value (max of the two one-sided p-values)."""
    d = np.asarray(d, float)
    n = len(d)
    if n < 3 or np.std(d, ddof=1) == 0:
        return 0.0 if (n >= 1 and abs(np.mean(d)) < margin) else 1.0
    se = np.std(d, ddof=1) / np.sqrt(n)
    p1 = 1 - stats.t.cdf((np.mean(d) + margin) / se, n - 1)
    p2 = stats.t.cdf((np.mean(d) - margin) / se, n - 1)
    return float(max(p1, p2))


def holm(p):
    p = np.asarray(p, float)
    order = np.argsort(p)
    adj = np.empty(len(p))
    run = 0.0
    for r, i in enumerate(order):
        run = max(run, (len(p) - r) * p[i])
        adj[i] = min(1.0, run)
    return adj


def fmt(v):
    m, lo, hi = bootstrap_ci(v)
    return f"{m:.3f} [{lo:.3f}, {hi:.3f}]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ck", type=int, default=2, help="checkpoint index (default 2 = step 40)")
    a = ap.parse_args()
    data = load(a.dir)
    keys = list(next(iter(data.values())))
    regimes = sorted({k.split("|")[0] for k in keys}, key=["oracle", "learned", "bma"].index)
    policies = sorted({k.split("|")[4] for k in keys}, key=["passive", "wide", "sweep", "eig"].index)
    lines = [f"# Bayesian observer, environment 1: {os.path.basename(a.dir)}", "", f"Seeds: {sorted(data)} (n = {len(data)}). Checkpoint index {a.ck}. Mean over seeds [bootstrap 95% CI].",
             "Class-balanced metrics: H0-true pools E0 and E0split; H2-true pools AltOOD and Ealt.", ""]
    for regime in regimes:
        lines += [f"## Regime: {regime}", "", "| policy | acc (3-class) | acc H0 | acc H1 | acc H2 | H1 vs H0 AUROC | H1 vs H2 AUROC | H1 vs H2 bal. acc | log-score | Brier | entropy | ECE | decided (0.95) | false-id | median decision step | realised / expected info gain |",
                  "|---|" + "---|" * 15]
        for pol in policies:
            m = across_seeds(data, regime, pol, a.ck)
            lines.append(f"| {pol} | " + " | ".join(fmt(m[k]) for k in ["acc3", "acc_h0", "acc_h1", "acc_h2", "h1v0_auroc", "h1v2_auroc", "h1v2_bal_acc", "logscore", "brier", "entropy", "ece", "decided", "false_id"])
                         + f" | {np.nanmedian(m['median_time']):.0f} | {m['real_gain'].mean():.2f} / {m['exp_gain'].mean():.2f} |")
        lines.append("")
    open(a.out, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
