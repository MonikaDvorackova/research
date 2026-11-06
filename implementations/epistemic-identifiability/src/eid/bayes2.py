"""Bayesian model-selection observer for the partially observed benchmark (Phase 5, Parts B-D).

Members are autoregressive predictors of the next observation given the observer's action-observation history:
  POMDPMember : exact filtering in a known POMDP (belief state)
  GRUMember   : a GRU world model (hidden state)
  ContamMember: a base member whose predictive is mixed with a uniform symbol with probability eta (non-learned 'noisy observation' mechanism)
  CatchAll    : Dirichlet-categorical model of p(o | a, previous observation); counts persist across episodes (optional fourth class)
Classes: 0 reference, 1 learned world model, 2 non-learned alternative, 3 catch-all. The observer sees only (action, observation) streams.
"""
from __future__ import annotations

import time

import numpy as np
import torch

from .gruworld import GRUWorld
from .pomdp import A, O, POMDP, START

CLS = 4
ETA_GRID = np.array([0.02, 0.05, 0.1, 0.2, 0.35, 0.5])


def lse(a, axis):
    m = np.max(a, axis=axis, keepdims=True)
    return (m + np.log(np.sum(np.exp(a - m), axis=axis, keepdims=True))).squeeze(axis)


def _fix(p):
    p = np.clip(p, 1e-12, None)
    return p / p.sum(-1, keepdims=True)


class POMDPMember:
    def __init__(self, pomdp: POMDP):
        self.p = pomdp

    def init(self, R):
        return self.p.belief0(R)

    def pred(self, st):
        return _fix(self.p.predict(st))

    def update(self, st, a, o):
        return self.p.update(st, a, o)


class GRUMember:
    def __init__(self, m: GRUWorld):
        self.m = m

    def init(self, R):
        return (torch.zeros(R, self.m.hidden), torch.full((R,), START, dtype=torch.long))

    def _all(self, st):
        h, prev = st
        out_h, out_p = [], []
        with torch.no_grad():
            for a in range(A):
                h2, lg = self.m.step(h, torch.full((len(prev),), a, dtype=torch.long), prev)
                out_h.append(h2)
                out_p.append(torch.softmax(lg, 1))
        return torch.stack(out_h), torch.stack(out_p, 1).numpy().astype(np.float64)   # (A,R,H), (R,A,O)

    def pred(self, st):
        return _fix(self._all(st)[1])

    def update(self, st, a, o):
        hs, _ = self._all(st)
        R = len(a)
        return (hs[torch.as_tensor(a), torch.arange(R)], torch.as_tensor(o, dtype=torch.long))


class ContamMember:
    def __init__(self, base, eta):
        self.base, self.eta = base, float(eta)

    def init(self, R):
        return self.base.init(R)

    def pred(self, st):
        return _fix((1 - self.eta) * self.base.pred(st) + self.eta / O)

    def update(self, st, a, o):
        return self.base.update(st, a, o)


class CatchAll:
    """Per-(action, previous observation) Dirichlet(1) categorical: a nonparametric, coarse catch-all."""

    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def init(self, R):
        return dict(counts=np.zeros((R, A, O + 1, O)), prev=np.full(R, START))

    def pred(self, st):
        c = st["counts"][np.arange(len(st["prev"])), :, st["prev"]]            # (R, A, O)
        return _fix((c + self.alpha) / (c.sum(-1, keepdims=True) + O * self.alpha))

    def update(self, st, a, o):
        c = st["counts"].copy()
        c[np.arange(len(a)), a, st["prev"], o] += 1
        return dict(counts=c, prev=np.asarray(o))

    def new_episode(self, st):
        return dict(counts=st["counts"], prev=np.full(len(st["prev"]), START))


class Space2:
    def __init__(self, members, cls, class_prior):
        self.members, self.cls = members, np.array(cls)
        present = sorted(set(self.cls.tolist()))
        cp = np.zeros(CLS)
        for c in present:
            cp[c] = class_prior[c]
        cp = cp / cp.sum()
        cnt = np.array([np.sum(self.cls == c) for c in range(CLS)])
        self.logprior = np.array([np.log(cp[c] / cnt[c]) for c in self.cls])
        self.M = len(members)

    def reset(self, R):
        if not hasattr(self, "states") or self.states is None:
            self.states = [m.init(R) for m in self.members]
        else:                                   # new episode: filtering states reset, catch-all counts persist
            self.states = [m.new_episode(s) if isinstance(m, CatchAll) else m.init(R) for m, s in zip(self.members, self.states)]

    def preds(self):
        return np.stack([m.pred(s) for m, s in zip(self.members, self.states)])   # (M, R, A, O)

    def update(self, a, o):
        self.states = [m.update(s, a, o) for m, s in zip(self.members, self.states)]

    def hyp_preds(self, a1, o1):
        """Predictive of every member after hypothetically observing (a1, o1) (vectors over runs); no state is changed."""
        return np.stack([m.pred(m.update(s, a1, o1)) for m, s in zip(self.members, self.states)])


def class_probs(space, logw):
    w = np.exp(logw - lse(logw, 1)[:, None])
    return np.stack([w[:, space.cls == c].sum(1) for c in range(CLS)], axis=1), w


def _ent(p, axis=-1):
    return -np.sum(np.where(p > 0, p * np.log(np.clip(p, 1e-300, 1)), 0.0), axis=axis)


def class_predictives(space, w, P):
    """Class-conditional predictive laws. P: (M, R, A, O). Returns (C, R, A, O) and class posterior (R, C)."""
    pc = np.stack([w[:, space.cls == c].sum(1) for c in range(CLS)], axis=1)
    out = np.zeros((CLS,) + P.shape[1:])
    for c in range(CLS):
        sel = space.cls == c
        if sel.any():
            wc = w[:, sel] / np.maximum(pc[:, c:c + 1], 1e-300)
            out[c] = np.einsum("rm,mrao->rao", wc, P[sel])
    return out, pc


def eig_myopic(space, w, P):
    """Exact one-step expected information gain about the class for every action: (R, A)."""
    cp, pc = class_predictives(space, w, P)
    mix = np.einsum("rc,crao->rao", pc, cp)
    return _ent(mix) - np.einsum("rc,cra->ra", pc, _ent(cp))


def eig_two_step(space, w, P):
    """Exact two-step non-myopic EIG for every plan (a1, a2): (R, A, A). Plans are open-loop pairs; the first action is executed."""
    R = P.shape[1]
    pc = np.stack([w[:, space.cls == c].sum(1) for c in range(CLS)], axis=1)
    out = np.zeros((R, A, A))
    P2 = {}
    for a1 in range(A):
        for o1 in range(O):
            P2[(a1, o1)] = space.hyp_preds(np.full(R, a1), np.full(R, o1))        # (M, R, A, O): predictive after (a1, o1)
    for a1 in range(A):
        for a2 in range(A):
            joint = np.zeros((space.M, R, O, O))
            for o1 in range(O):
                joint[:, :, o1, :] = P[:, :, a1, o1][:, :, None] * P2[(a1, o1)][:, :, a2, :]
            cj = np.zeros((CLS, R, O * O))
            for c in range(CLS):
                sel = space.cls == c
                if sel.any():
                    wc = w[:, sel] / np.maximum(pc[:, c:c + 1], 1e-300)
                    cj[c] = np.einsum("rm,mrk->rk", wc, joint[sel].reshape(sel.sum(), R, O * O))
            mix = np.einsum("rc,crk->rk", pc, cj)
            out[:, a1, a2] = _ent(mix) - np.einsum("rc,cr->r", pc, _ent(cj))
    return out


TRAIN_PROBS = np.array([0.49, 0.49, 0.02])
SWEEP2 = np.array([0, 1, 2])


def choose2(policy, t, space, w, P, rng):
    R = P.shape[1]
    if policy == "passive":
        return rng.choice(A, size=R, p=TRAIN_PROBS), np.zeros(R)
    if policy == "random":
        return rng.integers(0, A, R), np.zeros(R)
    if policy == "sweep":
        return np.full(R, SWEEP2[t % 3]), np.zeros(R)
    if policy == "no2":          # an intervention class that never uses the informative action 2
        return rng.integers(0, 2, R), np.zeros(R)
    if policy == "eig":
        e = eig_myopic(space, w, P)
        a = e.argmax(1)
        return a, e[np.arange(R), a]
    if policy == "eig2":
        e = eig_two_step(space, w, P)
        flat = e.reshape(R, -1).argmax(1)
        a = flat // A
        return a, e.reshape(R, -1)[np.arange(R), flat] / 2.0
    raise ValueError(policy)


def run_observer2(space, env, policy, rng, R=60, steps=60, episode_len=10, checkpoints=(10, 20, 40, 60), thresh=0.95):
    t0 = time.time()
    space.states = None
    env.reset(R, rng)
    space.reset(R)
    logw = np.tile(space.logprior, (R, 1))
    post = np.zeros((R, len(checkpoints), CLS))
    dec_time = np.full(R, np.inf)
    dec_class = np.full(R, -1)
    real_gain = np.zeros(R)
    exp_gain = np.zeros(R)
    p_prev, w = class_probs(space, logw)
    for t in range(steps):
        if t > 0 and t % episode_len == 0:
            env.reset(R, rng)
            space.reset(R)
        P = space.preds()
        a, e = choose2(policy, t, space, w, P, rng)
        exp_gain += e
        o = env.step(a, rng)
        logw = logw + np.log(P[:, np.arange(R), a, o]).T
        space.update(a, o)
        p, w = class_probs(space, logw)
        real_gain += np.sum(np.where(p > 0, p * (np.log(np.maximum(p, 1e-300)) - np.log(np.maximum(p_prev, 1e-300))), 0.0), axis=1)
        p_prev = p
        newly = (p.max(1) >= thresh) & ~np.isfinite(dec_time)
        dec_time[newly] = t + 1
        dec_class[newly] = p.argmax(1)[newly]
        if (t + 1) in checkpoints:
            post[:, checkpoints.index(t + 1)] = p
    return dict(post=post, dec_time=dec_time, dec_class=dec_class, real_gain=real_gain, exp_gain=exp_gain, seconds=time.time() - t0)
