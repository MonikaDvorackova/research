"""Run the proof-of-concept experiment. Usage: python -m eid.run --config configs/poc.yaml --out results/poc"""
from __future__ import annotations

import argparse
import csv
import json
import os
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import torch
import yaml

from .agent import POLICIES, interact
from .env import COUPLING, SIGMA, LearnedEnv, RefEnv, gauss_logpdf, kl_gauss, ref_mean, sample_x0
from .metrics import auroc, platt_ece_brier, prefix_stat
from .model import AnalyticTheory, Ensemble, train_gauss, train_poly

TAGS = {"q": 1, "w": 2, "test": 3, "alt": 4, "eval": 5, "cal": 6, "alto_eval": 7, "alto_cal": 8}
EP_LEN = 20


def rng_for(seed: int, tag: str, extra: int = 0):
    return np.random.default_rng(np.random.SeedSequence([seed, TAGS[tag], extra]))


def collect(n_transitions: int, rng, amp: float = 1.0):
    """Training transitions from E0 under the training policy (actions in [-amp, amp]; default [-1, 1])."""
    env, n_ep = RefEnv("direct"), int(np.ceil(n_transitions / EP_LEN))
    x = sample_x0(rng, n_ep)
    X, A, Y = [], [], []
    for _ in range(EP_LEN):
        a = rng.uniform(-amp, amp, n_ep)
        y = env.step(x, a, rng)
        X.append(x), A.append(a), Y.append(y)
        x = y
    X, A, Y = np.concatenate(X), np.concatenate(A), np.concatenate(Y)
    return X[:n_transitions], A[:n_transitions], Y[:n_transitions]


def model_quality(model, rng, n: int = 4000):
    """True per-step KL(E0 || W) on independent test inputs, in-distribution and out-of-distribution actions."""
    out = {}
    x = sample_x0(rng, n)
    for name, amp in (("kl_in", 1.0), ("kl_ood", 3.0)):
        a = rng.uniform(-amp, amp, n)
        mu, std = model.predict(x, a)
        out[name] = float(kl_gauss(ref_mean(x, a), SIGMA, mu, std).mean())
    return out


def _build_ensemble(cfg, seed, steps, arch, amp):
    Xq, Aq, Yq = collect(cfg["q_train_n"], rng_for(seed, "q"), amp)
    brng = rng_for(seed, "q", 1)
    members = []
    for k in range(cfg["ensemble_k"]):
        idx = brng.integers(0, len(Xq), len(Xq))
        if arch == "tanh64":
            members.append(train_gauss(Xq[idx], Aq[idx], Yq[idx], seed=seed * 100 + k, steps=steps))
        elif arch == "relu128":
            members.append(train_gauss(Xq[idx], Aq[idx], Yq[idx], seed=seed * 100 + k, steps=steps, hidden=128, act="relu", depth=3))
        elif arch == "poly3":
            members.append(train_poly(Xq[idx], Aq[idx], Yq[idx]))
        else:
            raise ValueError(arch)
    return Ensemble(members)


def run_seed(cfg: dict, seed: int):
    torch.set_num_threads(1)
    steps, B, grid = cfg["train_steps"], cfg["eval_episodes"], cfg["horizon_grid"]
    Tmax = max(grid)
    # agent's theory Q: independent data, bootstrap ensemble (ablation options: architecture, training action range,
    # analytic theory with a separate learned ensemble used only to choose actions)
    arch, amp = cfg.get("q_arch", "tanh64"), cfg.get("q_action_amp", 1.0)
    Q = _build_ensemble(cfg, seed, steps, arch, amp) if cfg.get("theory", "ensemble") == "ensemble" else AnalyticTheory()
    selector = _build_ensemble(cfg, seed, steps, "tanh64", 1.0) if cfg.get("theory") == "analytic" and cfg.get("selector") == "ensemble" else None

    qual_rows, rows, envs, meta = [], [], {"E0": RefEnv("direct"), "E0split": RefEnv("split")}, {}
    envs_alto = {}  # post-hoc control kept apart (own random streams) so v1 columns are reproduced exactly
    for qi, n_train in enumerate(cfg["train_sizes"]):
        Xw, Aw, Yw = collect(n_train, rng_for(seed, "w", qi))
        W = train_gauss(Xw, Aw, Yw, seed=seed * 100 + 50 + qi, steps=steps)
        envs[("W", qi)] = LearnedEnv(W)
        meta[qi] = (W, model_quality(W, rng_for(seed, "test", qi)))

    # matched-divergence control Ealt: coupling shift s.t. KL(E0||Ealt) equals KL(E0||W) under wide interventions
    ref_run = interact(RefEnv("direct"), "wide", Q, 400, EP_LEN, rng_for(seed, "alt"), selector)
    xs, as_ = ref_run[0][:, :-1].reshape(-1, 2), ref_run[1].reshape(-1)
    for qi, (W, qual) in meta.items():
        mu, std = W.predict(xs, as_)
        klbar = float(kl_gauss(ref_mean(xs, as_), SIGMA, mu, std).mean())
        delta = float(np.sqrt(2 * SIGMA**2 * klbar / np.mean(xs[:, 1] ** 2)))
        envs[("Alt", qi)] = RefEnv("direct", COUPLING + delta)
        # post-hoc control (added after run poc_v1): real mismatch localised at |a|>1, matched to the same KL
        gamma = float(np.sqrt(2 * SIGMA**2 * klbar / np.mean(np.maximum(np.abs(as_) - 1.0, 0.0) ** 2)))
        envs_alto[("AltO", qi)] = RefEnv("direct", ood_gamma=gamma)
        qual_rows.append(dict(seed=seed, quality=qi, n_train=cfg["train_sizes"][qi], alt_delta=delta, altood_gamma=gamma, kl_matched_wide=klbar, **qual))

    for policy in POLICIES:
        runs = {}
        for split, tag in (("eval", "eval"), ("cal", "cal")):
            for ki, (key, env) in enumerate(envs.items()):
                runs[(split, key)] = interact(env, policy, Q, B, Tmax, rng_for(seed, tag, 10 * POLICIES.index(policy) + ki), selector)
            for key, env in envs_alto.items():
                runs[(split, key)] = interact(env, policy, Q, B, Tmax, rng_for(seed, "alto_" + split, 10 * POLICIES.index(policy) + key[1]), selector)
        for qi, (W, qual) in meta.items():
            def llr(run):  # experimenter-side oracle: log p_W / log p_E0 along the observed trajectory
                X, A, _ = run
                x, a, y = X[:, :-1].reshape(-1, 2), A.reshape(-1), X[:, 1:].reshape(-1, 2)
                mu, std = W.predict(x, a)
                d = gauss_logpdf(y, mu, std) - gauss_logpdf(y, ref_mean(x, a), SIGMA)
                return d.reshape(A.shape)

            for T in grid:
                S = {}
                for split in ("eval", "cal"):
                    S[split] = {k: prefix_stat(runs[(split, k)][2], T) for k in ("E0", "E0split", ("W", qi), ("Alt", qi), ("AltO", qi))}
                (Dn0, Rn0), (Dn1, Rn1) = S["eval"]["E0"], S["eval"]["E0split"]
                (Dw, Rw), (Da, Ra) = S["eval"][("W", qi)], S["eval"][("Alt", qi)]
                (Do, Ro) = S["eval"][("AltO", qi)]
                null_D, null_R = np.r_[Dn0, Dn1], np.r_[Rn0, Rn1]
                Lw = llr(runs[("eval", ("W", qi))])[:, :T].sum(1)
                Ln = np.r_[llr(runs[("eval", "E0")])[:, :T].sum(1), llr(runs[("eval", "E0split")])[:, :T].sum(1)]
                cal_pos, cal_neg = S["cal"][("W", qi)][0], np.r_[S["cal"]["E0"][0], S["cal"]["E0split"][0]]
                e, br = platt_ece_brier(np.r_[cal_pos, cal_neg], np.r_[np.ones(len(cal_pos)), np.zeros(len(cal_neg))],
                                        np.r_[Dw, null_D], np.r_[np.ones(len(Dw)), np.zeros(len(null_D))])
                rows.append(dict(
                    seed=seed, quality=qi, policy=policy, T=T,
                    auroc_W_vs_null=auroc(Dw, null_D), auroc_null_vs_null=auroc(Dn0, Dn1),
                    auroc_W_vs_alt=auroc(Dw, Da), auroc_alt_vs_null=auroc(Da, null_D),
                    auroc_W_vs_altood=auroc(Dw, Do), auroc_altood_vs_null=auroc(Do, null_D), tpr_altood=float(Ro.mean()),
                    tpr_W=float(Rw.mean()), tpr_alt=float(Ra.mean()), fpr_null=float(null_R.mean()),
                    fpr_E0=float(Rn0.mean()), fpr_E0split=float(Rn1.mean()),
                    oracle_auroc=auroc(Lw, Ln), info_gain_per_step=float(Lw.mean() / T), ece=e, brier=br))
    return qual_rows, rows


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 1)
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config))
    os.makedirs(args.out, exist_ok=True)
    seeds = list(range(cfg["n_seeds"]))
    with ProcessPoolExecutor(min(args.workers, len(seeds))) as ex:
        res = list(ex.map(run_seed, [cfg] * len(seeds), seeds))
    write_csv(os.path.join(args.out, "quality.csv"), [r for q, _ in res for r in q])
    write_csv(os.path.join(args.out, "metrics.csv"), [r for _, m in res for r in m])
    json.dump(cfg, open(os.path.join(args.out, "config_used.json"), "w"), indent=2)
    print("wrote", args.out)


if __name__ == "__main__":
    main()
