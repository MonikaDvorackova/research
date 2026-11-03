"""World-models programme, pilot platform (Phase 12).  Components kept separate:
 Generator   : privileged (evaluator + environment only): linear 1-D controlled system with a hidden computational property
               cont   : x' = v
               quant  : x' = q * round(v / q)             (finite precision: lattice state)
               stiff  : x' = v if |v - x| >= delta else x  (continuous-valued dead zone, 'stiction')  -- the matched PHYSICAL alternative
               v = x + dt (-k x + b u).
 Interface   : observation y_t = x_t + N(0, sigma^2), action u_t; episodes of T steps from x_0 = 0.  The agent receives only `env.act(u) -> y` and public constants.
 Hypotheses  : the agent's structural hypothesis system: {cont} u {quant(q): q in QS} u {stiff(delta): delta in DS}; physics (k, b, dt, sigma) known.
 Evaluator   : compares the agent's posterior with the generator's identity; never passed to the agent."""
from __future__ import annotations

import numpy as np

DT, K, T_EP = 0.1, 0.5, 20
QS = (0.1, 0.2, 0.4)
DS = (0.05, 0.1, 0.2)
HYPS = [("cont", 0.0)] + [("quant", q) for q in QS] + [("stiff", d) for d in DS]
CLASSES = ["cont", "quant", "stiff"]


def step(kind, par, x, u, b):
    v = x + DT * (-K * x + b * u)
    if kind == "cont":
        return v
    if kind == "quant":
        return par * np.round(v / par)
    return np.where(np.abs(v - x) >= par, v, x)


class PilotEnv:
    """Privileged generator wrapped behind the agent interface.  The agent only calls act()."""
    def __init__(self, kind, par, b, sigma, rng):
        self._kind, self._par, self._b, self.sigma, self._rng = kind, par, b, sigma, rng
        self.reset()

    def reset(self):
        self._x = np.zeros(())

    def act(self, u):
        self._x = step(self._kind, self._par, self._x, u, self._b)
        return float(self._x + self._rng.normal(0, self.sigma))


def hyp_means(us, b):
    """Noise-free observation means of every hypothesis for control programs us: array (P, T) -> (P, H, T)."""
    us = np.atleast_2d(us); P, T = us.shape
    x = np.zeros((P, len(HYPS))); out = np.zeros((P, len(HYPS), T))
    for t in range(T):
        for h, (kd, par) in enumerate(HYPS):
            x[:, h] = step(kd, par, x[:, h], us[:, t], b)
        out[:, :, t] = x
    return out


def class_of(h):
    return CLASSES.index(HYPS[h][0])


def program_menu():
    c = [0.0, 0.02, 0.05, 0.1, 0.2, 0.4, 1.0, 2.0]
    progs = [np.full(T_EP, v) for v in c] + [np.full(T_EP, -v) for v in c[1:]]
    progs += [np.where(np.arange(T_EP) % 2 == 0, v, -v) for v in (0.1, 0.4, 1.0)]
    return np.array(progs)


def eig(post, mu, sigma, rng, S=64):
    """Monte-Carlo expected information gain about hypothesis identity for each program: mu (P, H, T)."""
    P, H, T = mu.shape; out = np.zeros(P)
    h0 = -(post * np.log(np.clip(post, 1e-300, None))).sum()
    for p in range(P):
        hs = rng.choice(H, size=S, p=post)
        y = mu[p, hs] + rng.normal(0, sigma, (S, T))
        ll = -((y[:, None, :] - mu[p][None]) ** 2).sum(2) / (2 * sigma ** 2) + np.log(np.clip(post, 1e-300, None))[None]
        ll -= ll.max(1, keepdims=True); pp = np.exp(ll); pp /= pp.sum(1, keepdims=True)
        out[p] = h0 - (-(pp * np.log(np.clip(pp, 1e-300, None))).sum(1)).mean()
    return out


def run_agent(env, b, policy, n_episodes, rng):
    """Bayesian structural-hypothesis agent.  policy in {passive, probe, active}.  Returns posterior over HYPS and the controls used."""
    sigma = env.sigma; logp = np.zeros(len(HYPS)); menu = program_menu(); mu_menu = hyp_means(menu, b); used = []
    for ep in range(n_episodes):
        post = np.exp(logp - logp.max()); post /= post.sum()
        if policy == "passive":
            us = rng.uniform(-2, 2, T_EP)                          # large random controls (the usual data-collection regime)
        elif policy == "probe":
            us = rng.uniform(-1, 1, T_EP) * 10 ** rng.uniform(-2, 0.3)     # random amplitude over three decades
        else:
            us = menu[int(np.argmax(eig(post, mu_menu, sigma, rng)))]
        env.reset(); y = np.array([env.act(u) for u in us])
        mu = hyp_means(us[None], b)[0]
        logp += -((y[None] - mu) ** 2).sum(1) / (2 * sigma ** 2)
        used.append(us)
    post = np.exp(logp - logp.max()); post /= post.sum()
    return post, used
