"""kick-world: a partially observed nonlinear oscillator whose hidden shocks come from an n-bit deterministic generator
(LFSR: linear feedback; NLFSR: degree-2 nonlinear feedback) or from true randomness (R).

Hidden state (p, v, w); the agent observes o_t = (p, v) + sigma*eps and chooses a_t in [-1,1].  The shock bit b_t enters the
hidden variable w (kappa*(2b-1)), which feeds v with a one-step delay: the bit is visible in the observations (SNR ~ 10) but the
generator state, taps and type are never exposed.
"""
from __future__ import annotations
import numpy as np

DT, K_, C_, ALPHA, BETA, G_, KAPPA, DECAY, SIGMA = 0.1, 1.0, 0.3, 0.5, 1.0, 1.0, 2.0, 0.9, 0.02


def _par(x):
    x = x ^ (x >> 32); x = x ^ (x >> 16); x = x ^ (x >> 8); x = x ^ (x >> 4); x = x ^ (x >> 2); x = x ^ (x >> 1)
    return x & 1


class Gen:
    """Deterministic bit generator spec. kind in {'lfsr','nlfsr'}; state is an n-bit integer, output = LSB."""

    def __init__(self, kind, n, lin_mask, nl=None):
        self.kind, self.n, self.lin_mask, self.nl = kind, n, int(lin_mask), nl   # nl = (i, j): AND of bits i, j (nlfsr)

    def step(self, s):
        fb = _par(s & self.lin_mask)
        if self.kind == "nlfsr":
            i, j = self.nl
            fb = fb ^ (((s >> i) & 1) & ((s >> j) & 1))
        return (s >> 1) | (fb << (self.n - 1))

    def stream(self, seeds, T):
        s = seeds.astype(np.int64).copy(); out = np.empty((len(s), T), dtype=np.int8)
        for t in range(T):
            out[:, t] = s & 1; s = self.step(s)
        return out

    def period(self, seed=1, cap=1 << 22):
        s0 = np.array([seed], dtype=np.int64); s = s0.copy()
        for k in range(1, cap):
            s = self.step(s)
            if s[0] == seed: return k
        return None

    def describe(self):
        return dict(kind=self.kind, n=self.n, lin_mask=self.lin_mask, nl=self.nl)


def sample_gen(kind, n, rng, weight=None, min_period_frac=0.25):
    """Random generator of given type/size with a long cycle (LFSR: maximal 2^n-1; NLFSR: >= frac * 2^n)."""
    for _ in range(20000):
        w = weight or int(rng.choice([2, 4])) if kind == "lfsr" else int(rng.integers(1, 4))
        taps = [n - 1] + list(rng.choice(np.arange(0, n - 1), size=min(w - 1, n - 1), replace=False))
        mask = sum(1 << int(t) for t in set(taps))
        nl = tuple(int(x) for x in rng.choice(n, size=2, replace=False)) if kind == "nlfsr" else None
        g = Gen(kind, n, mask, nl)
        per = g.period(1, cap=(1 << min(n + 1, 22)))
        if per is None: continue
        if kind == "lfsr" and per == (1 << n) - 1: return g
        if kind == "nlfsr" and per >= max(8, int(min_period_frac * (1 << n))): return g
    raise RuntimeError("no generator found")


def random_bits(N, T, rng):
    return rng.integers(0, 2, size=(N, T)).astype(np.int8)


def bit_streams(spec, N, T, rng):
    """spec: None -> true randomness; Gen -> deterministic generator with a random nonzero seed per episode (continuing-stream
    interface). Returns [N,T] bits."""
    if spec is None: return random_bits(N, T, rng)
    seeds = rng.integers(1, 1 << spec.n, size=N)
    return spec.stream(seeds, T)


def smooth_actions(N, T, rng):
    u = np.zeros((N, T)); cur = np.zeros(N); e = rng.standard_normal((N, T))
    for t in range(T):
        cur = 0.9 * cur + 0.5 * e[:, t]; u[:, t] = cur
    return np.clip(u, -1, 1)


def dynamics(bits, acts, rng_noise):
    N, T = bits.shape
    p = np.zeros(N); v = np.zeros(N); w = np.zeros(N); obs = np.empty((N, T, 2))
    for t in range(T):
        w = DECAY * w + KAPPA * (2.0 * bits[:, t] - 1.0)
        v = v + DT * (-K_ * p - C_ * v - ALPHA * p ** 3 + BETA * w + G_ * acts[:, t])
        p = p + DT * v
        obs[:, t, 0] = p; obs[:, t, 1] = v
    return obs + SIGMA * rng_noise.standard_normal(obs.shape)


def make_batch(spec, N, T, rng):
    bits = bit_streams(spec, N, T, rng); acts = smooth_actions(N, T, rng)
    return dict(obs=dynamics(bits, acts, rng), act=acts, bits=bits, click=bits.copy())


def replay_pair(spec, N, T, rng, reseed_fixed=True):
    """Interface with a RESET: both episodes start the generator from the same hidden seed (deterministic generators) and use
    identical actions; for true randomness the two shock sequences are independent. Returns the two observation arrays."""
    acts = smooth_actions(N, T, rng)
    if spec is None:
        b1, b2 = random_bits(N, T, rng), random_bits(N, T, rng)
    else:
        seeds = rng.integers(1, 1 << spec.n, size=N); b1 = spec.stream(seeds, T); b2 = spec.stream(seeds, T)
    return dict(obs1=dynamics(b1, acts, rng), obs2=dynamics(b2, acts, rng), act=acts, bits1=b1, bits2=b2)
