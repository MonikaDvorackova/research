"""Run the Bayesian observer experiment on environment 1. Usage:
python -m eid.run_bayes1 --config configs/bayes1_dev.yaml --out results/bayes1_dev
Raw per-seed posteriors are stored as compressed npz; metrics are computed by eid.analyze_bayes1."""
from __future__ import annotations

import argparse
import json
import os
import platform
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import torch
import yaml

from .bayes1 import SIGMA, brng, build_space, run_observer
from .env import LearnedEnv, RefEnv, kl_gauss, ref_mean
from .model import train_gauss

SCENARIOS = ["E0", "E0split", "W", "AltOOD", "Ealt"]
TRUTH_CLASS = {"E0": 0, "E0split": 0, "W": 1, "AltOOD": 2, "Ealt": 2}


def collect_b(n, rng, amp=1.0, ep_len=20):
    env, n_ep = RefEnv("direct"), int(np.ceil(n / ep_len))
    x = 0.5 * rng.standard_normal((n_ep, 2))
    X, A, Y = [], [], []
    for _ in range(ep_len):
        a = rng.uniform(-amp, amp, n_ep)
        y = env.step(x, a, rng)
        X.append(x), A.append(a), Y.append(y)
        x = y
    X, A, Y = np.concatenate(X), np.concatenate(A), np.concatenate(Y)
    return X[:n], A[:n], Y[:n]


def build_materials(cfg, seed):
    torch.set_num_threads(1)
    steps, amp = cfg["train_steps"], cfg.get("q_amp", 1.0)
    # the observer's theories: 5 tanh and 5 ReLU networks on bootstrap resamples of one narrow (or wide) E0 sample
    Xq, Aq, Yq = collect_b(cfg["q_train_n"], brng(seed, "q"), amp)
    br = brng(seed, "q", 1)
    Q = []
    for k, (hidden, act, depth) in enumerate([(64, "tanh", 2)] * 5 + [(128, "relu", 3)] * 5):
        idx = br.integers(0, len(Xq), len(Xq))
        Q.append(train_gauss(Xq[idx], Aq[idx], Yq[idx], seed=seed * 100 + k, steps=steps, hidden=hidden, act=act, depth=depth))
    # the observer's own guesses of what a learned world model of E0 looks like: independent samples, several sizes and architectures
    Wp = []
    for j, (n, arch) in enumerate([(500, "tanh"), (500, "relu"), (2500, "tanh"), (2500, "relu"), (12500, "tanh"), (12500, "relu")]):
        X, A, Y = collect_b(n, brng(seed, "w2", j), 1.0)
        hidden, act, depth = (64, "tanh", 2) if arch == "tanh" else (128, "relu", 3)
        Wp.append((n, arch, train_gauss(X, A, Y, seed=seed * 100 + 20 + j, steps=steps, hidden=hidden, act=act, depth=depth)))
    # the true world model that the environment will be (independent of everything above)
    X, A, Y = collect_b(cfg["w_train_n"], brng(seed, "w"), 1.0)
    W_true = train_gauss(X, A, Y, seed=seed * 100 + 60, steps=steps)
    # matched non-learned alternatives: equal mean KL(E0 || W) under uniform wide interventions
    ar = brng(seed, "alt")
    x = 0.5 * ar.standard_normal((400, 2))
    xs, as_ = [], []
    for _ in range(20):
        a = ar.uniform(-3, 3, 400)
        xs.append(x), as_.append(a)
        x = RefEnv("direct").step(x, a, ar)
    xs, as_ = np.concatenate(xs), np.concatenate(as_)
    mu, std = W_true.predict(xs, as_)
    klbar = float(kl_gauss(ref_mean(xs, as_), SIGMA, mu, std).mean())
    gamma = float(np.sqrt(2 * SIGMA**2 * klbar / np.mean(np.maximum(np.abs(as_) - 1.0, 0.0) ** 2)))
    delta = float(np.sqrt(2 * SIGMA**2 * klbar / np.mean(xs[:, 1] ** 2)))
    return dict(Q=Q, Wp=Wp, W_true=W_true, gamma_star=gamma, delta_star=delta, klbar=klbar)


def scenario_env(name, ctx):
    return {"E0": RefEnv("direct"), "E0split": RefEnv("split"), "W": LearnedEnv(ctx["W_true"]),
            "AltOOD": RefEnv("direct", ood_gamma=ctx["gamma_star"]), "Ealt": RefEnv("direct", coupling=0.2 + ctx["delta_star"])}[name]


def run_seed(cfg, seed):
    torch.set_num_threads(1)
    ctx = build_materials(cfg, seed)
    out, timing = {}, {}
    prior_sets = cfg.get("priors", {"uniform": [1 / 3, 1 / 3, 1 / 3]})
    cell = 0   # deterministic, collision-free index of each (regime, completeness, prior, scenario, policy) cell
    for regime in cfg["regimes"]:
        for complete in cfg.get("complete", ["full"]):
            for pname, prior in prior_sets.items():
                space = build_space(regime, ctx, tuple(prior), complete)
                for sc in cfg.get("scenarios", SCENARIOS):
                    env = scenario_env(sc, ctx)
                    for pol in cfg["policies"]:
                        rng = brng(seed, "sim", cell)
                        cell += 1
                        r = run_observer(space, env, pol, rng, R=cfg["R"], steps=cfg["steps"], episode_len=cfg["episode_len"],
                                         checkpoints=tuple(cfg["checkpoints"]))
                        key = f"{regime}|{complete}|{pname}|{sc}|{pol}"
                        for k in ("post", "dec_time", "dec_class", "real_gain", "exp_gain"):
                            out[f"{key}|{k}"] = r[k]
                        timing[key] = r["seconds"]
    meta = dict(seed=seed, gamma_star=ctx["gamma_star"], delta_star=ctx["delta_star"], klbar=ctx["klbar"], timing=timing)
    return seed, out, meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 1)
    a = ap.parse_args()
    cfg = yaml.safe_load(open(a.config))
    os.makedirs(a.out, exist_ok=True)
    seeds = cfg["seeds"]
    with ProcessPoolExecutor(min(a.workers, len(seeds))) as ex:
        for seed, out, meta in ex.map(run_seed, [cfg] * len(seeds), seeds):
            np.savez_compressed(os.path.join(a.out, f"seed{seed}.npz"), **out)
            json.dump(meta, open(os.path.join(a.out, f"seed{seed}_meta.json"), "w"), indent=1)
            print("saved seed", seed, flush=True)
    env = dict(python=platform.python_version(), torch=torch.__version__, numpy=np.__version__, platform=platform.platform(),
               machine=platform.machine(), torch_threads_per_worker=1)
    json.dump(dict(config=cfg, environment=env), open(os.path.join(a.out, "provenance.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
