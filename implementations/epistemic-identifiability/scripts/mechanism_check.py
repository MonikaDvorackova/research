"""Exploratory check of Proposition 7(b): which environment looks less anomalous under the observer's theory?

For each seed, rebuild the baseline theory Q and the world model W (quality 3) exactly as in eid.run, draw fresh evaluation
episodes under wide interventions, and compute the mean per-step negative log-likelihood (moment-matched Gaussian) of the
observed transitions under (i) the baseline learned theory and (ii) the analytic true law. Report mean(NLL on W) - mean(NLL on E0)
and the AUROC of the NLL score for W as positive class. Exploratory: not part of the pre-specified analysis.

Usage: PYTHONPATH=src python scripts/mechanism_check.py
"""
import os
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import torch
import yaml

from eid.agent import interact
from eid.env import LearnedEnv, RefEnv, SIGMA, gauss_logpdf, ref_mean
from eid.metrics import auroc
from eid.model import AnalyticTheory
from eid.run import _build_ensemble, collect, rng_for, train_gauss

ROOT = os.path.join(os.path.dirname(__file__), "..")
T, B = 10, 400


def nll(theory, X, A):
    x, a, y = X[:, :-1].reshape(-1, 2), A.reshape(-1), X[:, 1:].reshape(-1, 2)
    mean, var, _ = theory.predictive(x, a)
    return (-gauss_logpdf(y, mean, np.sqrt(var))).reshape(A.shape).mean(1)   # per-episode mean per-step NLL


def one(seed):
    torch.set_num_threads(1)
    cfg = yaml.safe_load(open(os.path.join(ROOT, "configs", "poc.yaml")))
    Q = _build_ensemble(cfg, seed, cfg["train_steps"], "tanh64", 1.0)
    Xw, Aw, Yw = collect(cfg["train_sizes"][3], rng_for(seed, "w", 3))
    W = train_gauss(Xw, Aw, Yw, seed=seed * 100 + 50 + 3, steps=cfg["train_steps"])
    out = {}
    for name, theory in (("learned", Q), ("analytic", AnalyticTheory())):
        runs = {}
        for k, env in (("E0", RefEnv("direct")), ("W", LearnedEnv(W))):
            runs[k] = interact(env, "wide", Q, B, T, rng_for(seed, "eval", 900 + (0 if k == "E0" else 1)))
        s0, s1 = nll(theory, runs["E0"][0], runs["E0"][1]), nll(theory, runs["W"][0], runs["W"][1])
        out[name] = (float(s1.mean() - s0.mean()), auroc(s1, s0))
    return out


if __name__ == "__main__":
    with ProcessPoolExecutor(10) as ex:
        res = list(ex.map(one, range(10)))
    for name in ("learned", "analytic"):
        d = np.array([r[name][0] for r in res]); a = np.array([r[name][1] for r in res])
        print(f"{name:9s} theory: mean NLL(W)-NLL(E0) = {d.mean():+.3f} (seeds with W looking MORE anomalous: {(d > 0).sum()}/10); "
              f"AUROC of NLL score for W = {a.mean():.3f} [min {a.min():.3f}, max {a.max():.3f}]")
