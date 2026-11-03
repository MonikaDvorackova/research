"""Sanity checks for the Bayesian observer (Gate 2): normalisation, exact agreement with a direct computation, observational
equivalence, simulation-based calibration, and absence of access to the true environment."""
import numpy as np
import pytest
from scipy.stats import norm

from eid.bayes1 import GAMMA_GRID, Space, brng, class_post, lse, run_observer
from eid.env import SIGMA, RefEnv, ref_mean, sample_x0


class Shifted:
    """Analytic base: E0 mean plus a smooth deviation, used so that no network training is needed in unit tests."""
    def __init__(self, k):
        self.k = k

    def predict(self, x, a):
        mu = ref_mean(x, a)
        mu[:, 0] += self.k * np.tanh(a) if self.k else 0.0
        return mu, np.full_like(mu, SIGMA)


class SpyEnv:
    """Environment stub exposing only step(); any other attribute access fails."""
    def __init__(self, env):
        self._env = env

    def step(self, x, a, rng):
        return self._env.step(x, a, rng)

    def __getattr__(self, name):
        raise AssertionError(f"observer touched env.{name}")


def small_space(prior=(1 / 3, 1 / 3, 1 / 3)):
    bases = [Shifted(0.0), Shifted(0.15), Shifted(0.3)]
    members = [dict(base=0, shift="none", param=0, cls=0), dict(base=1, shift="none", param=0, cls=1),
               dict(base=2, shift="none", param=0, cls=2), dict(base=0, shift="ood", param=0.4, cls=2)]
    return Space(bases, members, prior)


def test_posterior_is_normalised_and_matches_direct_formula():
    sp = small_space()
    rng = np.random.default_rng(0)
    x = sample_x0(rng, 5)
    a = rng.uniform(-3, 3, 5)
    env = RefEnv("direct")
    logw = np.tile(sp.logprior, (5, 1))
    y = env.step(x, a, rng)
    mu, std = sp.predict(x, a)
    logw = logw + (-0.5 * ((y[None] - mu) / std) ** 2 - np.log(std) - 0.5 * np.log(2 * np.pi)).sum(-1).T
    p = class_post(sp, logw)
    assert np.allclose(p.sum(1), 1.0)
    # direct computation with scipy
    for r in range(5):
        lik = [np.prod(norm.pdf(y[r], mu[m, r], std[m, r])) for m in range(sp.M)]
        prior = np.exp(sp.logprior)
        post = prior * lik / np.sum(prior * lik)
        direct = np.array([post[sp.cls == c].sum() for c in range(3)])
        assert np.allclose(p[r], direct, atol=1e-10)


def test_observationally_equivalent_hypotheses_keep_their_prior_ratio_exactly():
    """Two members with identical kernels (an observationally equivalent pair) cannot be separated: posterior ratio = prior ratio."""
    bases = [Shifted(0.0), Shifted(0.0), Shifted(0.5)]
    members = [dict(base=0, shift="none", param=0, cls=0), dict(base=1, shift="none", param=0, cls=1), dict(base=2, shift="none", param=0, cls=2)]
    sp = Space(bases, members, (0.7, 0.2, 0.1))
    out = run_observer(sp, RefEnv("direct"), "wide", np.random.default_rng(1), R=20, steps=30, checkpoints=(30,))
    p = out["post"][:, 0]
    assert np.allclose(p[:, 0] / p[:, 1], 0.7 / 0.2, rtol=1e-9)


def test_observer_uses_only_env_step():
    sp = small_space()
    for pol in ("passive", "wide", "sweep", "eig"):
        out = run_observer(sp, SpyEnv(RefEnv("direct")), pol, np.random.default_rng(2), R=4, steps=3, checkpoints=(3,))
        assert out["post"].shape == (4, 1, 3)


@pytest.mark.parametrize("policy", ["passive", "eig"])
def test_simulation_based_calibration_with_truth_drawn_from_the_prior(policy):
    """Bayesian coherence: when the truth is drawn from the observer's prior, posterior probabilities are calibrated.
    Runs are stratified by truth member in proportion to the prior; the pooled reliability error must be small."""
    sp = small_space((0.5, 0.25, 0.25))
    prior = np.exp(sp.logprior)
    N = 4000
    ps, truth = [], []
    for m, mem in enumerate(sp.members):
        n = int(round(N * prior[m]))
        base = sp.bases[mem["base"]]

        class E:
            def step(self, x, a, rng, base=base, mem=mem):
                mu, _ = base.predict(x, a)
                if mem["shift"] == "ood":
                    mu[:, 0] += mem["param"] * np.maximum(np.abs(a) - 1.0, 0.0)
                return mu + SIGMA * rng.standard_normal(mu.shape)
        out = run_observer(sp, E(), policy, np.random.default_rng(100 + m), R=n, steps=3, episode_len=3, checkpoints=(3,))
        ps.append(out["post"][:, 0])
        truth += [mem["cls"]] * n
    P, T = np.concatenate(ps), np.array(truth)
    # reliability of the posterior probability of each class
    err = 0.0
    for c in range(3):
        bins = np.clip((P[:, c] * 5).astype(int), 0, 4)
        for b in range(5):
            s = bins == b
            if s.sum() > 50:
                err += (s.mean()) * abs(P[s, c].mean() - (T[s] == c).mean())
    assert err / 3 < 0.03, err
    assert 0.0 <= P.min() and P.max() <= 1.0 + 1e-12


def test_log_sum_exp_is_stable():
    assert lse(np.array([[-1000.0, -1000.0]]), 1)[0] == pytest.approx(-1000 + np.log(2))


def test_independent_random_streams_for_observer_materials():
    sigs = {tuple(brng(300, t, e).random(3)) for t in ("q", "w", "w2", "alt", "sim", "cand", "q2") for e in range(8)}
    assert len(sigs) == 7 * 8


def test_monte_carlo_eig_matches_numerical_integration():
    """Validate the MC expected-information-gain estimator against the exact mutual information of a two-member Gaussian mixture."""
    from scipy import integrate
    from eid.bayes1 import _eig_values

    class B:
        def __init__(self, m):
            self.m = m

        def predict(self, x, a):
            mu = np.zeros((len(a), 2))
            mu[:, 0] = self.m
            return mu, np.full_like(mu, 0.5)
    sp = Space([B(0.0), B(0.8)], [dict(base=0, shift="none", param=0, cls=0), dict(base=1, shift="none", param=0, cls=1)], (0.6, 0.4, 0.0))
    w = np.array([[0.6, 0.4]])
    mc = np.mean([_eig_values(sp, np.zeros((1, 2)), w, np.zeros((1, 1)), 4000, np.random.default_rng(i))[0, 0] for i in range(5)])
    f = lambda y: w[0, 0] * norm.pdf(y, 0, .5) + w[0, 1] * norm.pdf(y, .8, .5)  # noqa: E731
    exact = integrate.quad(lambda y: -f(y) * np.log(f(y)), -6, 6)[0] - 0.5 * np.log(2 * np.pi * np.e * .25)
    assert abs(mc - exact) < 0.01
