import itertools
import numpy as np
from eid.e6gen import (NS_DEV, descriptors, gen_changing, gen_equivalent_pair, gen_hmm, gen_markov, gen_regime_pair, simulate_regime_stream,
                       simulate_stream_probs)
from eid.pomdp import exact_obs_law, make_e0


def _law(p, T=3):
    return np.concatenate([exact_obs_law(p, a) for a in itertools.product(range(3), repeat=T)]) / 27


def _kl(p, q):
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / np.clip(q[m], 1e-300, None))))


def test_generators_are_deterministic_and_in_dev_namespace():
    assert NS_DEV == 9000 and NS_DEV not in set(range(200, 830))
    a, b = gen_hmm(3)[0], gen_hmm(3)[0]
    assert np.array_equal(a.T, b.T) and np.array_equal(a.Z, b.Z)
    assert gen_hmm(3)[1]["S"] in (3, 4, 5, 6)


def test_independent_draws_are_far_apart_compared_with_jittered_copies():
    ind = [_law(gen_hmm(i)[0]) for i in range(8)]; jit = [_law(make_e0(500 + i)) for i in range(8)]
    mean = lambda L: np.mean([_kl(a, b) for i, a in enumerate(L) for j, b in enumerate(L) if i != j])
    assert mean(ind) > 10 * mean(jit)


def test_equivalent_pair_has_zero_tv_and_different_state_counts():
    (p, q), d = gen_equivalent_pair(1)
    assert q.S == p.S + 1 and np.abs(_law(p) - _law(q)).max() < 1e-12


def test_mixed_state_count_stream_and_regime_stream_run():
    (p, q), _ = gen_equivalent_pair(2)
    ctx, obs = simulate_stream_probs((p, q), 50, lambda e: [1 / 3] * 3, 100, 4, np.random.default_rng(0))
    assert ctx.shape == (100, 4) and obs.max() < 3
    pair, d = gen_regime_pair(1)
    ctx, obs, reg = simulate_regime_stream(pair, d["eps_per_episode"], 200, 4, 1 / 3, np.random.default_rng(1))
    assert ctx.shape == (200, 4) and set(np.unique(reg)) <= {0, 1}


def test_changing_pair_differs_only_on_one_action():
    (p, p2), d = gen_changing(2)
    a = d["changed_action"]
    for b in range(3):
        assert (np.abs(p.T[b] - p2.T[b]).max() > 1e-9) == (b == a)
