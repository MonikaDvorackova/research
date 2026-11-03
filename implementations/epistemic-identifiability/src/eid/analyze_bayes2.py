"""Metrics for the partially observed benchmark (K posterior classes; the catch-all class 3 is optional).
Usage: python -m eid.analyze_bayes2 --dir results/bayes2_dev --out results/bayes2_dev/analysis.md [--ck 2]"""
from __future__ import annotations

import argparse
import glob
import json
import os

import numpy as np
from sklearn.metrics import roc_auc_score

from .analyze_bayes1 import _ece, fmt, holm, tost_paired  # noqa: F401  (shared helpers; the environment-1 analysis code is unchanged)

GROUPS = {0: ["E0", "E0split"], 1: ["W"], 2: ["AltOOD", "Ealt"]}


def load(d):
    out = {}
    for f in sorted(glob.glob(os.path.join(d, "seed*.npz"))):
        seed = int(os.path.basename(f)[4:-4])
        z = np.load(f)
        out[seed] = {k: z[k] for k in z.files}
    return out


def metrics_seed(arrs, regime, policy, ck, complete="full", pname="uniform"):
    key = lambda s, k: arrs[f"{regime}|{complete}|{pname}|{s}|{policy}|{k}"]  # noqa: E731
    P = {c: np.concatenate([key(s, "post")[:, ck] for s in sc]) for c, sc in GROUPS.items()}
    K = P[0].shape[1]
    D = {c: np.concatenate([key(s, "dec_time") for s in sc]) for c, sc in GROUPS.items()}
    DC = {c: np.concatenate([key(s, "dec_class") for s in sc]) for c, sc in GROUPS.items()}
    acc = {c: float(np.mean(P[c].argmax(1) == c)) for c in GROUPS}
    ls = {c: float(np.mean(-np.log(np.clip(P[c][:, c], 1e-12, 1)))) for c in GROUPS}
    brier = {c: float(np.mean(np.sum((P[c] - np.eye(K)[c]) ** 2, axis=1))) for c in GROUPS}
    ent = {c: float(np.mean(-np.sum(np.where(P[c] > 0, P[c] * np.log(np.clip(P[c], 1e-300, 1)), 0), axis=1))) for c in GROUPS}
    conf = np.concatenate([P[c].max(1) for c in GROUPS])
    corr = np.concatenate([(P[c].argmax(1) == c).astype(float) for c in GROUPS])
    w = np.concatenate([np.full(len(P[c]), 1.0 / len(P[c])) for c in GROUPS])
    out = dict(acc3=float(np.mean(list(acc.values()))), acc_h0=acc[0], acc_h1=acc[1], acc_h2=acc[2], logscore=float(np.mean(list(ls.values()))),
               brier=float(np.mean(list(brier.values()))), entropy=float(np.mean(list(ent.values()))), ece=_ece(conf, corr, w))
    for name, (pc, nc) in {"h1v0": (1, 0), "h1v2": (1, 2)}.items():
        sp = P[pc][:, pc] / np.maximum(P[pc][:, pc] + P[pc][:, nc], 1e-300)
        sn = P[nc][:, pc] / np.maximum(P[nc][:, pc] + P[nc][:, nc], 1e-300)
        out[f"{name}_bal_acc"] = float(0.5 * (np.mean(sp > 0.5) + np.mean(sn <= 0.5)))
        out[f"{name}_auroc"] = float(roc_auc_score(np.r_[np.ones(len(sp)), np.zeros(len(sn))], np.r_[sp, sn]))
    dec = {c: np.isfinite(D[c]) for c in GROUPS}
    out["decided"] = float(np.mean([dec[c].mean() for c in GROUPS]))
    out["false_id"] = float(np.nanmean([np.mean(DC[c][dec[c]] != c) if dec[c].any() else np.nan for c in GROUPS]))
    times = np.concatenate([D[c][dec[c]] for c in GROUPS])
    out["median_time"] = float(np.median(times)) if len(times) else np.nan
    out["real_gain"] = float(np.mean(np.concatenate([key(s, "real_gain") for sc in GROUPS.values() for s in sc])))
    out["exp_gain"] = float(np.mean(np.concatenate([key(s, "exp_gain") for sc in GROUPS.values() for s in sc])))
    out["p_h0_E0"] = float(key("E0", "post")[:, ck, 0].mean())
    out["p_h0_E0split"] = float(key("E0split", "post")[:, ck, 0].mean())
    return out


def across_seeds(data, regime, policy, ck, **kw):
    rows = [metrics_seed(a, regime, policy, ck, **kw) for a in data.values()]
    return {m: np.array([r[m] for r in rows]) for m in rows[0]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ck", type=int, default=2)
    a = ap.parse_args()
    data = load(a.dir)
    keys = list(next(iter(data.values())))
    regimes = sorted({k.split("|")[0] for k in keys}, key=["oracle", "learned", "bma"].index)
    order = ["passive", "random", "sweep", "eig", "eig2", "no2"]
    policies = sorted({k.split("|")[4] for k in keys}, key=order.index)
    L = [f"# Bayesian observer, partially observed benchmark: {os.path.basename(a.dir)}", "", f"Seeds {sorted(data)} (n = {len(data)}), checkpoint index {a.ck}. Mean over seeds [bootstrap 95% CI].",
         "H0-true pools the reference POMDP and its bisimilar split-state copy; H2-true pools the transition-perturbed and emission-noise POMDPs.", ""]
    for regime in regimes:
        L += [f"## Regime: {regime}", "", "| policy | acc (3-class) | acc H0 | acc H1 | acc H2 | H1 vs H0 AUROC | H1 vs H2 AUROC | log-score | entropy | ECE | decided (0.95) | false-id | median step | realised / expected gain |",
              "|---|" + "---|" * 13]
        for pol in policies:
            m = across_seeds(data, regime, pol, a.ck)
            L.append(f"| {pol} | " + " | ".join(fmt(m[k]) for k in ["acc3", "acc_h0", "acc_h1", "acc_h2", "h1v0_auroc", "h1v2_auroc", "logscore", "entropy", "ece", "decided", "false_id"])
                     + f" | {np.nanmedian(m['median_time']):.0f} | {m['real_gain'].mean():.2f} / {m['exp_gain'].mean():.2f} |")
        L.append("")
    # exact distinguishability table averaged over seeds
    metas = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(a.dir, "seed*_meta.json")))]
    L += ["## Exact distinguishability (mean over seeds of the exact total-variation distance between observation laws, horizon 6, 30 sampled action sequences per intervention class)", "",
          "| intervention class | E0 vs equivalent copy | E0 vs W | E0 vs transition-perturbed | E0 vs emission-noise | **W vs transition-perturbed** | **W vs emission-noise** |", "|---|---|---|---|---|---|---|"]
    for kind in ("training", "no_action2", "uniform", "action2_heavy"):
        g = lambda pair: float(np.mean([m["table"][f"{kind}|{pair}"]["tv"] for m in metas]))  # noqa: E731
        L.append(f"| {kind} | {g('E0->E0split'):.4f} | {g('E0->W'):.4f} | {g('E0->AltOOD'):.4f} | {g('E0->Ealt'):.4f} | {g('W->AltOOD'):.4f} | {g('W->Ealt'):.4f} |")
    L += ["", f"Matched parameters (mean over seeds): transition-swap eps = {np.mean([m['eps_t'] for m in metas]):.3f}, emission-noise eta = {np.mean([m['eta_n'] for m in metas]):.3f}, target mean KL(E0 || W) under uniform actions = {np.mean([m['target_kl'] for m in metas]):.3f}"]
    open(a.out, "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
