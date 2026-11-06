"""Proposition 1' (equivalence relative to an intervention class): randomised exact check on finite processes."""
import numpy as np
import pytest

from eid.finite import history_law, tv

NA, NO = 3, 2


def env_pair(seed, forbidden):
    """E and E' agree at every action except `forbidden`, where E' differs on all histories."""
    r = np.random.default_rng(seed)
    cache, cache2 = {}, {}

    def e(h, a):
        if (h, a) not in cache:
            cache[(h, a)] = r.dirichlet(np.ones(NO))
        return cache[(h, a)]

    def e2(h, a):
        if a != forbidden:
            return e(h, a)
        if (h, a) not in cache2:
            cache2[(h, a)] = np.roll(e(h, a), 1) * 0.7 + 0.3 * r.dirichlet(np.ones(NO))
        return cache2[(h, a)]
    return e, e2


@pytest.mark.parametrize("seed", range(10))
def test_laws_equal_under_every_policy_that_avoids_the_forbidden_action_and_differ_otherwise(seed):
    forbidden = seed % NA
    e, e2 = env_pair(seed, forbidden)
    r = np.random.default_rng(100 + seed)
    allowed = [a for a in range(NA) if a != forbidden]
    for k in range(5):
        cache = {}

        def pol(h, cache=cache):
            if h not in cache:
                v = np.zeros(NA)
                v[allowed] = r.dirichlet(np.ones(len(allowed)))
                cache[h] = v
            return cache[h]
        l1, l2 = history_law(e, pol, NA, NO, 3), history_law(e2, pol, NA, NO, 3)
        assert max(abs(l1[x] - l2[x]) for x in l1) < 1e-14
    steer = lambda h: np.eye(NA)[forbidden]  # noqa: E731
    assert tv(history_law(e, steer, NA, NO, 2), history_law(e2, steer, NA, NO, 2)) > 1e-3
