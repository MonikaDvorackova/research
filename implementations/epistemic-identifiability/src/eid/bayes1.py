"""Bayesian model-selection observer for the fully observed environment (Phase 5, Parts B and C).

Hypothesis classes (what the observer entertains):
  H0  the reference environment E0
  H1  a learned computational world model of E0
  H2  a non-learned alternative mechanism: E0 plus a structured deviation (two shapes, each with an unknown size on a fixed grid)

Each class is a finite set of *members* (concrete Gaussian transition kernels). The observer keeps a log-weight per member and
updates it with the exact Gaussian log-likelihood of every observed transition; the class posterior is the sum of member
posteriors. Information regimes differ only in what the members are:
  oracle   members are the true kernels (E0; the true W; the true alternative parameters)
  learned  one plug-in learned kernel per class (a theory Q0 trained on in-distribution E0 data; one independently trained world model W';
           deviations of Q0 on a parameter grid)
  bma      Bayesian model averaging over heterogeneous learners (ReLU and tanh theories; world models of several sizes and architectures;
           deviations of the ensemble mean)
The observer never receives the identity of the environment; the oracle regime is an evaluation upper bound.
"""
from __future__ import annotations

import time

import numpy as np

from .env import SIGMA, X0_STD, LearnedEnv, RefEnv, gauss_logpdf, kl_gauss, ref_mean, sample_x0

A_IN, A_WIDE = 1.0, 3.0
GAMMA_GRID = np.geomspace(0.05, 1.6, 9)   # sizes of the OOD-localised deviation (a fixed grid chosen before any run; truth is not on it)
DELTA_GRID = np.geomspace(0.1, 3.0, 9)    # sizes of the coupling deviation
CLASSES = 3


def lse(a, axis):
    m = np.max(a, axis=axis, keepdims=True)
    return (m + np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True))).squeeze(axis)


def brng(seed, tag, extra=0):
    ids = {"q": 1, "w": 2, "w2": 3, "alt": 4, "sim": 5, "cand": 6, "q2": 7}
    return np.random.default_rng(np.random.SeedSequence([seed, 1000 + ids[tag], extra]))


class Space:
    """A finite hypothesis space of Gaussian-kernel members."""

    def __init__(self, bases, members, class_prior):
        """bases: list of objects with predict(x, a) -> (mu, std). members: list of dicts {base, shift, param, cls}.
        class_prior: probabilities over the classes present (renormalised over present classes)."""
        self.bases, self.members = bases, members
        self.cls = np.array([m["cls"] for m in members])
        present = sorted(set(self.cls.tolist()))
        cp = np.zeros(CLASSES)
        for c in present:
            cp[c] = class_prior[c]
        cp = cp / cp.sum()
        counts = np.array([np.sum(self.cls == c) for c in range(CLASSES)])
        self.logprior = np.array([np.log(cp[m["cls"]] / counts[m["cls"]]) if cp[m["cls"]] > 0 else -np.inf for m in members])
        self.M = len(members)

    def predict(self, x, a):
        """x: (N,2); a: (N,). Returns mu, std of shape (M, N, 2)."""
        cache = {}
        mu = np.empty((self.M, len(a), 2))
        std = np.empty_like(mu)
        for i, m in enumerate(self.members):
            b = m["base"]
            if b not in cache:
                cache[b] = self.bases[b].predict(x, a)
            bm, bs = cache[b]
            mi = bm.copy()
            if m["shift"] == "ood":
                mi[:, 0] += m["param"] * np.maximum(np.abs(a) - 1.0, 0.0)
            elif m["shift"] == "alt":
                mi[:, 0] += m["param"] * x[:, 1]
            mu[i], std[i] = mi, bs
        return mu, std


class ExactRef:
    def predict(self, x, a):
        mu = ref_mean(x, a)
        return mu, np.full_like(mu, SIGMA)


class EnsembleMean:
    """Moment-matched mean of an ensemble of Gaussian models (used as the base for deviation families in the bma regime)."""

    def __init__(self, nets):
        self.nets = nets

    def predict(self, x, a):
        mus, stds = zip(*(n.predict(x, a) for n in self.nets))
        mus, stds = np.stack(mus), np.stack(stds)
        return mus.mean(0), np.sqrt((stds**2).mean(0) + mus.var(0))


def build_space(regime, ctx, class_prior=(1 / 3, 1 / 3, 1 / 3), complete="full"):
    """ctx holds the observer's materials: ctx['Q'] (list of theory nets: tanh then relu), ctx['Wp'] (list of (size, arch, net)),
    ctx['W_true'] (the true world model, used ONLY by the oracle regime), ctx['gamma_star'], ctx['delta_star'].
    complete: 'full' | 'no_h1' | 'no_h2' | 'only_ood' | 'only_alt' (incomplete hypothesis spaces)."""
    bases, members = [], []

    def add_base(b):
        bases.append(b)
        return len(bases) - 1

    if regime == "oracle":
        b0, bw = add_base(ExactRef()), add_base(ctx["W_true"])
        members.append(dict(base=b0, shift="none", param=0, cls=0))
        members.append(dict(base=bw, shift="none", param=0, cls=1))
        members.append(dict(base=b0, shift="ood", param=ctx["gamma_star"], cls=2))
        members.append(dict(base=b0, shift="alt", param=ctx["delta_star"], cls=2))
    elif regime == "learned":
        q0 = ctx["Q"][0]
        wp = [w for (n, a, w) in ctx["Wp"] if n == 12500 and a == "tanh"][0]
        b0, b1 = add_base(q0), add_base(wp)
        members.append(dict(base=b0, shift="none", param=0, cls=0))
        members.append(dict(base=b1, shift="none", param=0, cls=1))
        for g in GAMMA_GRID:
            members.append(dict(base=b0, shift="ood", param=float(g), cls=2))
        for d in DELTA_GRID:
            members.append(dict(base=b0, shift="alt", param=float(d), cls=2))
    elif regime == "bma":
        for net in ctx["Q"]:
            members.append(dict(base=add_base(net), shift="none", param=0, cls=0))
        for (_, _, w) in ctx["Wp"]:
            members.append(dict(base=add_base(w), shift="none", param=0, cls=1))
        bm = add_base(EnsembleMean(ctx["Q"][:5]))   # the tanh theories
        for g in GAMMA_GRID:
            members.append(dict(base=bm, shift="ood", param=float(g), cls=2))
        for d in DELTA_GRID:
            members.append(dict(base=bm, shift="alt", param=float(d), cls=2))
    else:
        raise ValueError(regime)
    if complete == "no_h1":
        members = [m for m in members if m["cls"] != 1]
    elif complete == "no_h2":
        members = [m for m in members if m["cls"] != 2]
    elif complete == "only_ood":    # H2 contains only the OOD-localised shape: the coupling-shape truth lies outside the class
        members = [m for m in members if not (m["cls"] == 2 and m["shift"] == "alt")]
    elif complete == "only_alt":
        members = [m for m in members if not (m["cls"] == 2 and m["shift"] == "ood")]
    return Space(bases, members, class_prior)


# ------------------------------------------------------------------------------------------------ interventions
def _eig_values(space, x, w, cand, S, rng):
    """Monte-Carlo expected information gain about the class for candidate actions cand (R, K). Returns (R, K).
    EIG(a) = E[log p(y | class) - log p(y)] with (class, member, y) drawn from the observer's own posterior predictive."""
    R, K = cand.shape
    mu, std = space.predict(np.repeat(x, K, axis=0), cand.reshape(-1))            # (M, R*K, 2)
    mu, std = mu.reshape(space.M, R, K, 2), std.reshape(space.M, R, K, 2)
    cdf = np.cumsum(w, axis=1)
    u = rng.random((R, K, S))
    midx = np.minimum((u[..., None] > cdf[:, None, None, :]).sum(-1), space.M - 1)  # (R, K, S)
    ri, ki = np.arange(R)[:, None, None], np.arange(K)[None, :, None]
    y = mu[midx, ri, ki] + std[midx, ri, ki] * rng.standard_normal((R, K, S, 2))  # (R, K, S, 2)
    ld = gauss_logpdf(y[None], mu[:, :, :, None, :], std[:, :, :, None, :])        # (M, R, K, S)
    logw_m = np.log(np.maximum(w, 1e-300)).T[:, :, None, None]                      # (M, R, 1, 1)
    pc = np.stack([w[:, space.cls == c].sum(1) for c in range(CLASSES)], axis=1)   # (R, C) class posterior
    log_pyc = []
    for c in range(CLASSES):
        sel = space.cls == c
        if not sel.any():
            log_pyc.append(np.full((R, K, S), -np.inf))
            continue
        wc = np.maximum(w[:, sel], 1e-300) / np.maximum(pc[:, c:c + 1], 1e-300)    # within-class weights (R, Mc)
        log_pyc.append(lse(ld[sel] + np.log(wc).T[:, :, None, None], 0))
    log_pyc = np.stack(log_pyc)                                                    # (C, R, K, S)
    log_py = lse(ld + logw_m, 0)
    log_py_given_h = np.take_along_axis(log_pyc, space.cls[midx][None], axis=0)[0]
    return np.mean(log_py_given_h - log_py, axis=2)


def eig_select(space, x, logw, rng, K=16, S=24, S_check=128):
    """Myopic expected information gain about the *class* for K random candidate actions per run; no access to the true environment.
    The reported expected gain of the chosen action is re-estimated with fresh draws to remove the winner's-curse bias of taking a
    maximum over noisy estimates."""
    R = x.shape[0]
    w = np.exp(logw - lse(logw, 1)[:, None])
    cand = rng.uniform(-A_WIDE, A_WIDE, (R, K))
    eig = _eig_values(space, x, w, cand, S, rng)
    a = cand[np.arange(R), eig.argmax(1)]
    fresh = _eig_values(space, x, w, a[:, None], S_check, rng)[:, 0]
    return a, fresh


SWEEP = np.linspace(-A_WIDE, A_WIDE, 11)


def choose(policy, t, x, space, logw, rng):
    R = x.shape[0]
    if policy == "passive":
        return rng.uniform(-A_IN, A_IN, R), np.zeros(R)
    if policy == "wide":
        return rng.uniform(-A_WIDE, A_WIDE, R), np.zeros(R)
    if policy == "sweep":
        return np.full(R, SWEEP[t % len(SWEEP)]), np.zeros(R)
    if policy == "eig":
        return eig_select(space, x, logw, rng)
    raise ValueError(policy)


def class_post(space, logw):
    w = np.exp(logw - lse(logw, 1)[:, None])
    return np.stack([w[:, space.cls == c].sum(1) for c in range(CLASSES)], axis=1)


def run_observer(space, env, policy, rng, R=40, steps=80, episode_len=10, checkpoints=(10, 20, 40, 80), thresh=0.95):
    """R independent observers interact with one fixed environment. Returns a dict of arrays."""
    t0 = time.time()
    x = sample_x0(rng, R)
    logw = np.tile(space.logprior, (R, 1))
    out_post = np.zeros((R, len(checkpoints), CLASSES))
    dec_time = np.full(R, np.inf)
    dec_class = np.full(R, -1)
    real_gain = np.zeros(R)      # realised information gain: sum_t KL(post_after || post_before) over classes
    exp_gain = np.zeros(R)       # expected information gain at the chosen actions (observer's own model)
    p_prev = class_post(space, logw)
    for t in range(steps):
        if t > 0 and t % episode_len == 0:
            x = sample_x0(rng, R)
        a, e = choose(policy, t, x, space, logw, rng)
        exp_gain += e
        y = env.step(x, a, rng)
        mu, std = space.predict(x, a)
        logw = logw + gauss_logpdf(y[None], mu, std).T
        p = class_post(space, logw)
        real_gain += np.sum(np.where(p > 0, p * (np.log(np.maximum(p, 1e-300)) - np.log(np.maximum(p_prev, 1e-300))), 0.0), axis=1)
        p_prev = p
        newly = (p.max(1) >= thresh) & ~np.isfinite(dec_time)
        dec_time[newly] = t + 1
        dec_class[newly] = p.argmax(1)[newly]
        if (t + 1) in checkpoints:
            out_post[:, checkpoints.index(t + 1)] = p
        x = y
    return dict(post=out_post, dec_time=dec_time, dec_class=dec_class, real_gain=real_gain, exp_gain=exp_gain, seconds=time.time() - t0)
