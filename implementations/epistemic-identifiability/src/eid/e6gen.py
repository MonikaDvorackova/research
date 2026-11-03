"""Phase 9: independent environment generators for the E6 validity map (development namespace).
Each instance is drawn from SeedSequence([NS, family, index]); structure (state count, concentration, sharpness, regime persistence) is sampled per
instance, not jittered from one template.  Interface constraint (documented limitation): A = 3 actions, O = 3 observation symbols, as in eid.pomdp.
Experimenter-side descriptors (exact) are computed for audit and scoring only; they are never given to an observer."""
from __future__ import annotations

import numpy as np

from eid.pomdp import A, O, POMDP, split_state0
from eid.phase8 import learner_limit_and_entropy

NS_DEV = 9000          # development namespace (E6 reserves 800-829 for confirmatory instances; no overlap with any earlier seed)
FAMILIES = {"markov": 1, "hmm": 2, "controlled": 3, "regime": 4, "changing": 5}


def _rng(family, idx):
    return np.random.default_rng(np.random.SeedSequence([NS_DEV, FAMILIES[family], idx]))


def _norm(M):
    return M / M.sum(-1, keepdims=True)


def gen_markov(idx):
    """Fully observed finite Markov environment (S = O = 3; identity emission), random concentration per instance."""
    r = _rng("markov", idx)
    conc = float(np.exp(r.uniform(np.log(0.2), np.log(3.0))))
    T = r.dirichlet(np.full(3, conc), size=(A, 3))
    return POMDP(T, np.eye(3), r.dirichlet(np.ones(3))), dict(family="markov", S=3, conc_T=conc)


def gen_hmm(idx):
    """Random hidden-state POMDP: S in 3..6, random transition/emission concentrations; emission rows not forced to be informative."""
    r = _rng("hmm", idx)
    S = int(r.integers(3, 7))
    cT = float(np.exp(r.uniform(np.log(0.2), np.log(2.0)))); cZ = float(np.exp(r.uniform(np.log(0.2), np.log(2.0))))
    T = r.dirichlet(np.full(S, cT), size=(A, S)); Z = r.dirichlet(np.full(O, cZ), size=S); b0 = r.dirichlet(np.ones(S))
    return POMDP(T, Z, b0), dict(family="hmm", S=S, conc_T=cT, conc_Z=cZ)


def gen_controlled(idx):
    """Controlled POMDP with a designated 'revealing' action: action a* sends hidden state to an observationally distinct block."""
    r = _rng("controlled", idx)
    S = int(r.integers(4, 7)); star = int(r.integers(0, A))
    p, d = gen_hmm(10_000 + idx)
    T = p.T.copy()
    half = S // 2
    for s_ in range(S):
        row = np.full(S, 0.02 / S)
        row[(s_ + half) % S] += 0.9                          # the revealing action moves the hidden state to a fixed partner state
        T[star, s_] = _norm(row)
    d.update(family="controlled", revealing_action=star, S=S)
    return POMDP(T, p.Z, p.b0), d


def gen_regime_pair(idx):
    """Persistent latent regime: two independently drawn kernels K0, K1 (regime-conditional), regime flips between episodes with probability eps."""
    r = _rng("regime", idx)
    p0, d0 = gen_hmm(20_000 + 2 * idx); p1, d1 = gen_hmm(20_000 + 2 * idx + 1)
    eps = float(np.exp(r.uniform(np.log(1e-3), np.log(0.2))))
    return (p0, p1), dict(family="regime", eps_per_episode=eps, S0=d0["S"], S1=d1["S"])


def gen_changing(idx):
    """Explicit mechanism change: independently redrawn rows of one random action (the changed mechanism), at an episode chosen by the experiment."""
    r = _rng("changing", idx)
    p, d = gen_hmm(30_000 + idx)
    a = int(r.integers(0, A)); T2 = p.T.copy(); T2[a] = r.dirichlet(np.full(p.S, 0.5), size=p.S)
    d.update(family="changing", changed_action=a)
    return (p, POMDP(T2, p.Z, p.b0)), d


def gen_equivalent_pair(idx):
    """Observationally equivalent but mechanistically distinct: a random POMDP and its bisimilar state-split version (S+1 hidden states)."""
    p, d = gen_hmm(40_000 + idx)
    return (p, split_state0(p)), dict(d, family="equivalent_pair")


def descriptors(p: POMDP):
    """Exact experimenter-side descriptors of a POMDP under the uniform-action policy, T = 4: misspecification plateau of the best order-1 kernel,
    mean transition-row entropy and second-largest eigenvalue modulus of the averaged transition matrix (mixing)."""
    _, d1, _ = learner_limit_and_entropy(p, 1)
    Tm = p.T.mean(0)
    ev = np.sort(np.abs(np.linalg.eigvals(Tm)))[::-1]
    H = float(-(p.T * np.log(np.clip(p.T, 1e-300, None))).sum(-1).mean())
    return dict(order1_plateau=float(d1), slem=float(ev[1]) if len(ev) > 1 else 0.0, mean_T_entropy=H)


def simulate_regime_stream(pair, eps, N, T, p2, rng):
    """Persistent-regime stream: regime r_e in {0,1} is a two-state Markov chain over episodes (flip prob eps); each episode runs kernel K_{r_e}
    from a fresh latent state.  Returns ctx (N, T) and obs (N, T) in the order-1 context encoding of eid.phase8."""
    from eid.phase8 import simulate_stream
    flips = rng.random(N) < eps
    reg = np.cumsum(flips) % 2
    ctx = np.zeros((N, T), int); obs = np.zeros((N, T), int)
    for r_ in (0, 1):
        idx = np.flatnonzero(reg == r_)
        if len(idx):
            c, o = simulate_stream((pair[r_], pair[r_]), None, lambda e: p2, len(idx), T, rng)
            ctx[idx], obs[idx] = c, o
    return ctx, obs, reg


def _pad(p: POMDP, S: int) -> POMDP:
    """Zero-pad a POMDP to S hidden states (padded states are unreachable); used to mix kernels with different state counts in one stream."""
    if p.S == S:
        return p
    T = np.zeros((A, S, S)); T[:, :p.S, :p.S] = p.T
    for k in range(p.S, S):
        T[:, k, k] = 1.0
    Z = np.full((S, O), 1.0 / O); Z[:p.S] = p.Z
    b0 = np.zeros(S); b0[:p.S] = p.b0
    return POMDP(T, Z, b0)


def simulate_stream_probs(envs, change_at, probs_sched, N, T, rng):
    """Like eid.phase8.simulate_stream but with an arbitrary action distribution per episode: probs_sched(ep) -> length-3 probability vector."""
    from eid.pomdp import O as O_
    e1, e2 = _pad(envs[0], max(envs[0].S, envs[1].S)), _pad(envs[1], max(envs[0].S, envs[1].S))
    ep = np.arange(N)
    after = np.zeros(N, bool) if change_at is None else ep >= change_at
    P = np.array([probs_sched(e) for e in ep])                             # (N, 3)
    cum = np.cumsum(P, 1)
    acts = np.stack([(rng.random(N)[:, None] > cum).sum(1).clip(max=A - 1) for _ in range(T)], 1)
    S = e1.S
    b0 = np.where(after[:, None], e2.b0[None], e1.b0[None])
    s = (rng.random(N)[:, None] > np.cumsum(b0, 1)).sum(1).clip(max=S - 1)
    prev = np.full(N, O_); ctx = np.zeros((N, T), int); obs = np.zeros((N, T), int)
    for t in range(T):
        a = acts[:, t]
        Pt = np.where(after[:, None], e2.T[a, s], e1.T[a, s])
        s = (rng.random(N)[:, None] > np.cumsum(Pt, 1)).sum(1).clip(max=S - 1)
        Zr = np.where(after[:, None], e2.Z[s], e1.Z[s])
        o = (rng.random(N)[:, None] > np.cumsum(Zr, 1)).sum(1).clip(max=O_ - 1)
        ctx[:, t] = prev * A + a; obs[:, t] = o; prev = o
    return ctx, obs
