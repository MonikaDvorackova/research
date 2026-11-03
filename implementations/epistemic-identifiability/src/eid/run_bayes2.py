"""Run the Bayesian observer on the partially observed benchmark. Usage:
python -m eid.run_bayes2 --config configs/bayes2_dev.yaml --out results/bayes2_dev"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import platform
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import torch
import yaml

from .bayes2 import ETA_GRID, CatchAll, ContamMember, GRUMember, POMDPMember, Space2, run_observer2
from .gruworld import GRUEnv, POMDPEnv, gru_obs_law, sample_dataset, train_gru
from .pomdp import A, O, exact_obs_law, make_e0, perturb_action2, split_state0, with_emission_noise

SCENARIOS = ["E0", "E0split", "W", "AltOOD", "Ealt"]   # generic names shared with environment 1; mapping in meta
MAPPING = {"E0": "reference POMDP", "E0split": "bisimilar split-state POMDP (observationally equivalent)", "W": "GRU world model",
           "AltOOD": "transition-perturbed POMDP (mechanism-distinct, similar)", "Ealt": "emission-noise POMDP"}
HORIZON = 6


def rs(seed, tag, extra=0):
    ids = {"env": 1, "train": 2, "q": 3, "wp": 4, "match": 5, "sim": 6, "exact": 7}
    return np.random.default_rng(np.random.SeedSequence([seed, 2000 + ids[tag], extra]))


def action_seqs(kind, n, rng, T=HORIZON):
    if kind == "training":
        return rng.choice(A, size=(n, T), p=[0.49, 0.49, 0.02])
    if kind == "uniform":
        return rng.integers(0, A, (n, T))
    if kind == "no_action2":
        return rng.integers(0, 2, (n, T))
    if kind == "action2_heavy":
        return rng.choice(A, size=(n, T), p=[0.1, 0.1, 0.8])
    raise ValueError(kind)


def law_of(obj, acts):
    return gru_obs_law(obj, acts) if hasattr(obj, "seq_logprob") else exact_obs_law(obj, acts)


def exact_divergences(p, q, kind, rng, n=40):
    """Mean exact TV and KL(p||q) between the observation laws over sampled action sequences of the given kind."""
    tvs, kls = [], []
    for acts in action_seqs(kind, n, rng):
        a, b = law_of(p, tuple(acts)), law_of(q, tuple(acts))
        tvs.append(0.5 * np.abs(a - b).sum())
        kls.append(float(np.sum(np.where(a > 0, a * np.log(np.clip(a, 1e-300, None) / np.clip(b, 1e-300, None)), 0.0))))
    return float(np.mean(tvs)), float(np.mean(kls))


def match_param(build, e0, target_kl, rng_seed, lo=0.0, hi=1.0):
    """Bisection on a one-parameter family so that mean KL(E0 || alt) under uniform action sequences equals target_kl (clipped to [lo, hi])."""
    def kl(x):
        return exact_divergences(e0, build(x), "uniform", np.random.default_rng(rng_seed), n=24)[1]
    if kl(hi) < target_kl:
        return hi
    for _ in range(18):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if kl(mid) < target_kl else (lo, mid)
    return (lo + hi) / 2


def build_materials(cfg, seed):
    torch.set_num_threads(1)
    e0 = make_e0(seed)
    T_tr, steps, nep = cfg["train_horizon"], cfg["train_steps"], cfg["train_episodes"]
    p2 = cfg.get("train_p2", 0.02)
    a, o = sample_dataset(e0, nep, T_tr, rs(seed, "train"), p2)
    hid = cfg.get("hidden", 32)
    W2 = train_gru(a, o, seed=seed * 100 + 1, steps=steps, hidden=hid)
    aq, oq = sample_dataset(e0, nep, T_tr, rs(seed, "q"), cfg.get("q_p2", p2))
    br = rs(seed, "q", 1)
    Q = []
    for k in range(5):
        idx = br.integers(0, nep, nep)
        Q.append(train_gru(aq[idx], oq[idx], seed=seed * 100 + 10 + k, steps=steps, hidden=hid))
    Wp = []
    sizes = cfg.get("wp_sizes", [nep, 300, 300, 1000, 1000, 3000, 3000])
    for j, n in enumerate(sizes):
        ap_, op_ = sample_dataset(e0, n, T_tr, rs(seed, "wp", j), p2)
        Wp.append((n, "main" if j == 0 else str(j), train_gru(ap_, op_, seed=seed * 100 + 30 + j, steps=steps, hidden=hid)))
    # matched non-learned alternatives: same mean exact KL(E0 || .) under uniform random action sequences as the true learned model W2
    target = exact_divergences(e0, W2, "uniform", rs(seed, "match"), n=40)[1]
    eps_t = match_param(lambda x: perturb_action2(e0, x), e0, target, seed)
    eta_n = match_param(lambda x: with_emission_noise(e0, x), e0, target, seed, hi=0.9)
    Et, En, Eeq = perturb_action2(e0, eps_t), with_emission_noise(e0, eta_n), split_state0(e0)
    # exact distinguishability table: how far apart the laws are under several intervention classes
    table = {}
    for kind in ("training", "uniform", "no_action2", "action2_heavy"):
        for (n1, o1), (n2, o2) in [(("E0", e0), ("E0split", Eeq)), (("E0", e0), ("W", W2)), (("E0", e0), ("AltOOD", Et)), (("E0", e0), ("Ealt", En)),
                                    (("W", W2), ("AltOOD", Et)), (("W", W2), ("Ealt", En))]:
            tv, kl = exact_divergences(o1, o2, kind, rs(seed, "exact"), n=30)
            table[f"{kind}|{n1}->{n2}"] = dict(tv=tv, kl=kl)
    return dict(e0=e0, Eeq=Eeq, W2=W2, Q=Q, Wp=Wp, Et=Et, En=En, eps_t=eps_t, eta_n=eta_n, target_kl=target, table=table)


def scenario_env(name, c):
    return {"E0": POMDPEnv(c["e0"]), "E0split": POMDPEnv(c["Eeq"]), "W": GRUEnv(c["W2"]), "AltOOD": POMDPEnv(c["Et"]), "Ealt": POMDPEnv(c["En"])}[name]


def build_space2(regime, c, prior, complete="full"):
    members, cls = [], []

    def add(m, k):
        members.append(m)
        cls.append(k)
    if regime == "oracle":
        add(POMDPMember(c["e0"]), 0)
        add(GRUMember(c["W2"]), 1)
        add(POMDPMember(c["Et"]), 2)
        add(POMDPMember(c["En"]), 2)
    elif regime == "learned":
        q0 = GRUMember(c["Q"][0])
        add(q0, 0)
        add(GRUMember(c["Wp"][0][2]), 1)
        for eta in ETA_GRID:
            add(ContamMember(q0, eta), 2)
    elif regime == "bma":
        for q in c["Q"]:
            add(GRUMember(q), 0)
        for (_, _, w) in c["Wp"]:
            add(GRUMember(w), 1)
        for q in c["Q"]:
            for eta in ETA_GRID:
                add(ContamMember(GRUMember(q), eta), 2)
    else:
        raise ValueError(regime)
    if complete == "no_h1":
        keep = [i for i, k in enumerate(cls) if k != 1]
    elif complete == "no_h2":
        keep = [i for i, k in enumerate(cls) if k != 2]
    else:
        keep = list(range(len(cls)))
    members, cls = [members[i] for i in keep], [cls[i] for i in keep]
    if len(prior) == 4 and prior[3] > 0:
        add(CatchAll(), 3)
    return Space2(members, cls, tuple(prior) if len(prior) == 4 else tuple(prior) + (0.0,))


def run_seed(cfg, seed):
    torch.set_num_threads(1)
    c = build_materials(cfg, seed)
    out, timing = {}, {}
    for regime in cfg["regimes"]:
        for complete in cfg.get("complete", ["full"]):
            for pname, prior in cfg.get("priors", {"uniform": [1 / 3, 1 / 3, 1 / 3]}).items():
                for sc in cfg.get("scenarios", SCENARIOS):
                    for pol in cfg["policies"]:
                        space = build_space2(regime, c, prior, complete)
                        rng = rs(seed, "sim", abs(hash((regime, complete, pname, sc, pol))) % 100000)
                        r = run_observer2(space, scenario_env(sc, c), pol, rng, R=cfg["R"], steps=cfg["steps"], episode_len=cfg["episode_len"],
                                          checkpoints=tuple(cfg["checkpoints"]))
                        key = f"{regime}|{complete}|{pname}|{sc}|{pol}"
                        for k in ("post", "dec_time", "dec_class", "real_gain", "exp_gain"):
                            out[f"{key}|{k}"] = r[k]
                        timing[key] = r["seconds"]
    meta = dict(seed=seed, eps_t=c["eps_t"], eta_n=c["eta_n"], target_kl=c["target_kl"], table=c["table"], timing=timing, mapping=MAPPING)
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
    json.dump(dict(config=cfg, environment=dict(python=platform.python_version(), torch=torch.__version__, numpy=np.__version__,
                                                platform=platform.platform(), machine=platform.machine(), torch_threads_per_worker=1)),
              open(os.path.join(a.out, "provenance.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
