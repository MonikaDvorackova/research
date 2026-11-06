"""Reference environment E0, its equivalent implementation, a perturbed control, and a learned wrapper.

Every environment exposes only ``step(x, a, rng) -> x_next`` (batched). The agent never sees
anything else. Oracle densities live in ``ref_mean`` / ``gauss_logpdf`` and are used only by
experimenter-side code.
"""
from __future__ import annotations

import numpy as np

SIGMA = 0.1       # transition noise std (per dimension)
X0_STD = 0.5      # initial-state std
COUPLING = 0.2    # E0 coupling constant


def ref_mean(x: np.ndarray, a: np.ndarray, c: float = COUPLING) -> np.ndarray:
    """Noise-free dynamics of E0. x: (B, 2); a: (B,)."""
    x1, x2 = x[:, 0], x[:, 1]
    n1 = 0.8 * x1 + 0.6 * np.sin(a) + c * x2
    n2 = 0.9 * x2 - 0.3 * np.tanh(x1)
    return np.stack([n1, n2], axis=1)


def gauss_logpdf(y, mu, std):
    """Sum over the last axis of independent Gaussian log-densities."""
    std = np.broadcast_to(std, mu.shape)
    return np.sum(-0.5 * ((y - mu) / std) ** 2 - np.log(std) - 0.5 * np.log(2 * np.pi), axis=-1)


def kl_gauss(mu_p, std_p, mu_q, std_q):
    """KL(N(mu_p, std_p^2) || N(mu_q, std_q^2)) summed over the last axis (diagonal)."""
    std_p = np.broadcast_to(std_p, mu_p.shape)
    std_q = np.broadcast_to(std_q, mu_p.shape)
    t = np.log(std_q / std_p) + (std_p**2 + (mu_p - mu_q) ** 2) / (2 * std_q**2) - 0.5
    return np.sum(t, axis=-1)


def ref_mean_ood(x, a, gamma: float):
    """E0 dynamics plus a deviation that vanishes for |a| <= 1: a real, non-learned mismatch localised out of distribution."""
    m = ref_mean(x, a)
    m[:, 0] += gamma * np.maximum(np.abs(a) - 1.0, 0.0)
    return m


class RefEnv:
    """E0 (impl='direct'), its observationally equivalent twin (impl='split'), or a perturbed control."""

    def __init__(self, impl: str = "direct", coupling: float = COUPLING, ood_gamma: float = 0.0):
        assert impl in ("direct", "split")
        self.impl, self.coupling, self.ood_gamma = impl, coupling, ood_gamma

    def step(self, x, a, rng):
        mu = ref_mean(x, a, self.coupling) if self.ood_gamma == 0.0 else ref_mean_ood(x, a, self.ood_gamma)
        if self.impl == "direct":
            noise = SIGMA * rng.standard_normal(mu.shape)
        else:  # sum of two independent half-variance Gaussians: identical law, different mechanism
            noise = (SIGMA / np.sqrt(2.0)) * (rng.standard_normal(mu.shape) + rng.standard_normal(mu.shape))
        return mu + noise


class LearnedEnv:
    """A learned world model used as an environment: x' ~ N(mu_W(x,a), sigma_W(x,a)^2)."""

    def __init__(self, model):
        self.model = model

    def moments(self, x, a):
        return self.model.predict(x, a)

    def step(self, x, a, rng):
        mu, std = self.moments(x, a)
        return mu + std * rng.standard_normal(mu.shape)


def sample_x0(rng, batch: int) -> np.ndarray:
    return X0_STD * rng.standard_normal((batch, 2))
