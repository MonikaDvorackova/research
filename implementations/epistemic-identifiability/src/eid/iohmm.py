"""Input-output HMM (categorical) fitted by batch EM on short episodes: feasibility check for a learned-HMM observer (development).
Convention as eid.pomdp: s0 ~ b0; step t: s_t ~ T[a_t, s_{t-1}], o_t ~ Z[s_t]."""
from __future__ import annotations

import numpy as np

from eid.pomdp import A, O


def loglik(Tm, Zm, b0, acts, obs):
    """Exact log-likelihood of all episodes (N, T) by the scaled forward recursion; also returns the per-episode scaling constants."""
    N, T = obs.shape
    alpha = np.tile(b0, (N, 1)); ll = np.zeros(N)
    for t in range(T):
        pred = np.einsum("ns,nst->nt", alpha, Tm[acts[:, t]])
        a = pred * Zm[:, obs[:, t]].T
        c = a.sum(1); ll += np.log(c); alpha = a / c[:, None]
    return float(ll.sum())


def em_fit(acts, obs, S, rng, iters=60, tol=1e-6):
    """Batch EM from a random start.  Returns (Tm, Zm, b0, final total log-likelihood, iterations used)."""
    N, T = obs.shape
    Tm = rng.dirichlet(np.ones(S), size=(A, S)); Zm = rng.dirichlet(np.ones(O), size=S); b0 = rng.dirichlet(np.ones(S))
    prev = -np.inf
    for it in range(iters):
        al = np.zeros((N, T, S)); c = np.zeros((N, T)); a_ = np.tile(b0, (N, 1))
        for t in range(T):
            x = np.einsum("ns,nst->nt", a_, Tm[acts[:, t]]) * Zm[:, obs[:, t]].T
            c[:, t] = x.sum(1); a_ = x / c[:, t][:, None]; al[:, t] = a_
        be = np.ones((N, T, S))
        for t in range(T - 2, -1, -1):
            nxt = Zm[:, obs[:, t + 1]].T * be[:, t + 1]
            be[:, t] = np.einsum("nst,nt->ns", Tm[acts[:, t + 1]], nxt) / c[:, t + 1][:, None]
        gam = al * be                                                     # posterior of s_t
        Tn = np.full((A, S, S), 1e-6); Zn = np.full((S, O), 1e-6); b0n = np.full(S, 1e-6)
        for t in range(T):
            prev_al = np.tile(b0, (N, 1)) if t == 0 else al[:, t - 1]
            xi = prev_al[:, :, None] * Tm[acts[:, t]] * (Zm[:, obs[:, t]].T * be[:, t])[:, None, :] / c[:, t][:, None, None]
            for a in range(A):
                m = acts[:, t] == a
                if m.any():
                    Tn[a] += xi[m].sum(0)
            for o in range(O):
                m = obs[:, t] == o
                Zn[:, o] += gam[m, t].sum(0)
            if t == 0:
                b0n += xi.sum(2).sum(0)
        Tm = Tn / Tn.sum(2, keepdims=True); Zm = Zn / Zn.sum(1, keepdims=True); b0 = b0n / b0n.sum()
        ll = float(np.log(c).sum())
        if abs(ll - prev) < tol * N:
            break
        prev = ll
    return Tm, Zm, b0, loglik(Tm, Zm, b0, acts, obs), it + 1
