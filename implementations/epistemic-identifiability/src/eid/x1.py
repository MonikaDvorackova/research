"""X1: detecting hypothesis-class inadequacy in the finite POMDP, with exact filtering.

Null class M (finite): reference E0 and emission-noise variants.  Alternative family W: generic dense perturbations of E0's
transition table (the observer's own 'wide' family; it contains neither the truth nor the direction of the truth deviations).

Test (anytime-valid, proof in topics/bostrom-world-models/phase7/02-design-review-D1.md):
    E_t = ( (1/K) sum_{k in M u W} p_k(D_t) ) / max_{m in M} p_m(D_t),   reject 'truth in M' at the first t with E_t >= 1/alpha.
p_k(D_t) is the probability of the observations so far given the actions so far; the policy factors cancel in the ratio.

Policies choose the next action from the past only:
    P0 never uses action 2 (negative control)      P1 passive (training policy, action 2 w.p. 0.02)
    P2 random wide (uniform actions)               P3 within-class EIG: mutual information between member identity in M and next obs
    P4 class-level EIG: Jensen-Shannon divergence between the posterior-predictive of M and that of W (no truth information)
    P5 within-class EIG over the union M u W (member identity): same information as P4, different target variable (fairness comparator)
The environment is a sampler closure (`truth`); the observer code only ever sees actions it chose and observations returned.
"""
from __future__ import annotations

import numpy as np

from eid.pomdp import POMDP, make_e0, perturb_action2, split_state0, with_emission_noise, A, O

POLICIES = ("P0", "P1", "P2", "P3", "P4", "P5")
ALPHA = 0.05


def _norm(M):
    return M / M.sum(-1, keepdims=True)


def build_class(seed: int, nW: int = 14):
    """Return e0, M (list of (name, POMDP)), W (list of (action, POMDP)) -- deterministic in `seed`.
    W has three groups (one per action a): nW generic Dirichlet perturbations of E0's transition rows *for action a only*
    (lambda = 0.2 for the first half, 0.5 for the second).  W is the observer's wide family; it never contains the t05/t10 truths."""
    e0 = make_e0(seed)
    M = [("E0", e0)] + [(f"n{int(100 * eta):02d}", with_emission_noise(e0, eta)) for eta in (0.05, 0.1, 0.2)]
    r = np.random.default_rng([seed, 999])
    W = []
    for a in range(A):
        for i in range(nW):
            lam = 0.2 if i < nW // 2 else 0.5
            T = e0.T.copy()
            D = r.dirichlet(np.ones(e0.S), size=e0.S)
            T[a] = _norm((1 - lam) * e0.T[a] + lam * D)
            W.append((a, POMDP(T, e0.Z, e0.b0)))
    return e0, M, W


def truths_for(seed: int):
    """Truth environments (name -> (POMDP, role)).
    pc{a}: positive control = the member of W's action-a group whose wide-policy distance to M is the group median (exact rule)."""
    from eid.x1_exact import pc_member_index
    e0, M, W = build_class(seed)
    out = {"E0": (e0, "null"), "split": (split_state0(e0), "null"), "n10": (dict(M)["n10"], "null"), "n20": (dict(M)["n20"], "null"),
           "t05": (perturb_action2(e0, 0.5), "unanticipated"), "t10": (perturb_action2(e0, 1.0), "unanticipated")}
    for a in range(A):
        grp = [w for (g, w) in W if g == a]
        out[f"pc{a}"] = (grp[pc_member_index(e0, M, grp)], "anticipated")
    return out


def _stack(models):
    return (np.stack([m.T for m in models]), np.stack([m.Z for m in models]), np.stack([m.b0 for m in models]))


def _H(p):
    p = np.clip(p, 1e-300, None)
    return -(p * np.log(p)).sum(-1)


def _lse(x):
    m = x.max()
    return m + np.log(np.exp(x - m).sum())


def _choose(policy, b, ll, KM, Tt, Zt, rng):
    if policy == "P0":
        return int(rng.integers(0, 2))
    if policy == "P2":
        return int(rng.integers(0, A))
    if policy == "P1":
        return int(rng.choice(A, p=[0.49, 0.49, 0.02]))
    bp = np.einsum("ks,kast->kat", b, Tt)
    pred = np.einsum("kat,kto->kao", bp, Zt)                      # (K, A, O)
    if policy == "P5":
        wA = np.exp(ll - ll.max()); wA /= wA.sum()
        PA = np.einsum("k,kao->ao", wA, pred)
        score = _H(PA) - np.einsum("k,ka->a", wA, _H(pred))
        best = np.flatnonzero(score >= score.max() - 1e-12)
        return int(rng.choice(best))
    wM = np.exp(ll[:KM] - ll[:KM].max()); wM /= wM.sum()
    PM = np.einsum("k,kao->ao", wM, pred[:KM])
    if policy == "P3":
        score = _H(PM) - np.einsum("k,ka->a", wM, _H(pred[:KM]))
    else:                                                          # P4
        wW = np.exp(ll[KM:] - ll[KM:].max()); wW /= wW.sum()
        PW = np.einsum("k,kao->ao", wW, pred[KM:])
        score = _H(0.5 * (PM + PW)) - 0.5 * _H(PM) - 0.5 * _H(PW)
    best = np.flatnonzero(score >= score.max() - 1e-12)
    return int(rng.choice(best))


class Sampler:
    """The environment.  Hidden state never leaves this object."""
    def __init__(self, truth: POMDP, rng, switch_to: POMDP | None = None, switch_at: int | None = None):
        self.truth, self.rng, self.alt, self.sw = truth, rng, switch_to, switch_at
        self.ep = -1

    def new_episode(self):
        self.ep += 1
        self.cur = self.alt if (self.alt is not None and self.ep >= self.sw) else self.truth
        self.s = int(self.rng.choice(self.cur.S, p=self.cur.b0))

    def act(self, a: int) -> int:
        p = self.cur
        self.s = int(self.rng.choice(p.S, p=p.T[a, self.s]))
        return int(self.rng.choice(O, p=p.Z[self.s]))


def run(env: Sampler, M, W, policy: str, N: int, T: int, rng, alpha: float = ALPHA, trace_every: int = 0):
    """One experiment.  Returns dict(reject_episode (N+1 if none), reject_step, max_logE, trace).  `rng` is the observer's stream."""
    comps = [m for _, m in M] + [w for _, w in W]
    KM, K = len(M), len(comps)
    Tt, Zt, b0 = _stack(comps)
    ll = np.zeros(K)
    thr = np.log(1 / alpha)
    maxlogE, rej_ep, rej_t, trace = -np.inf, N + 1, -1, []
    for ep in range(N):
        env.new_episode()
        b = b0.copy()
        for t in range(T):
            a = _choose(policy, b, ll, KM, Tt, Zt, rng)
            o = env.act(a)
            bp = np.einsum("ks,kst->kt", b, Tt[:, a])
            po = np.einsum("kt,kt->k", bp, Zt[:, :, o])
            ll += np.log(np.clip(po, 1e-300, None))
            b = bp * Zt[:, :, o] / po[:, None]
            logE = _lse(ll) - np.log(K) - ll[:KM].max()
            maxlogE = max(maxlogE, logE)
            if logE >= thr and rej_ep == N + 1:
                rej_ep, rej_t = ep + 1, t
        if rej_ep <= N:
            break
        if trace_every and (ep + 1) % trace_every == 0:
            trace.append(float(logE))
    return dict(reject_episode=rej_ep, reject_step=rej_t, max_logE=float(maxlogE), trace=trace)
