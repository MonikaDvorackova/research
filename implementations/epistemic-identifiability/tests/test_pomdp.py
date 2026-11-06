"""Exact checks on the finite POMDP benchmark (Gate 2, environment 2)."""
import itertools

import numpy as np
import pytest

from eid.pomdp import A, O, brute_force_obs_law, exact_obs_law, make_e0, perturb_action2, split_state0, with_emission_noise


def test_rows_are_distributions():
    p = make_e0(0)
    assert np.allclose(p.T.sum(-1), 1) and np.allclose(p.Z.sum(-1), 1) and np.isclose(p.b0.sum(), 1)


@pytest.mark.parametrize("seed", [0, 1])
def test_forward_algorithm_matches_brute_force_over_hidden_paths(seed):
    p = make_e0(seed)
    acts = [2, 0, 1]
    assert np.allclose(exact_obs_law(p, acts), brute_force_obs_law(p, acts), atol=1e-14)
    assert np.isclose(exact_obs_law(p, acts).sum(), 1.0)


def test_split_state_control_is_exactly_observationally_equivalent():
    """Hidden-structure change with identical observation law under every action sequence (bisimilar)."""
    p = make_e0(3)
    q = split_state0(p)
    assert q.S == p.S + 1
    worst = 0.0
    for T_len in (1, 3, 5):
        for acts in itertools.islice(itertools.product(range(A), repeat=T_len), 0, None, max(1, A ** T_len // 40)):
            worst = max(worst, np.abs(exact_obs_law(p, acts) - exact_obs_law(q, acts)).max())
    assert worst < 1e-13


def test_hidden_state_matters_only_under_action_two():
    """Fundamental equivalence relative to an intervention class: the transition-perturbed control has TV = 0 under any action sequence
    that never uses action 2 (to numerical precision), and TV > 0 once action 2 is used."""
    p = make_e0(4)
    q = perturb_action2(p, 0.4)
    no2 = [exact_obs_law(p, a) - exact_obs_law(q, a) for a in itertools.product([0, 1], repeat=5)]
    assert max(np.abs(d).max() for d in no2) < 1e-13
    with2 = 0.5 * np.abs(exact_obs_law(p, (0, 2, 0, 0, 0)) - exact_obs_law(q, (0, 2, 0, 0, 0))).sum()
    assert with2 > 1e-3


def test_emission_noise_control_differs_everywhere():
    p = make_e0(5)
    q = with_emission_noise(p, 0.15)
    assert 0.5 * np.abs(exact_obs_law(p, (0, 0, 0)) - exact_obs_law(q, (0, 0, 0))).sum() > 1e-3


def test_filtering_update_is_consistent_with_enumeration():
    """The one-step predictive from the belief equals the exact conditional law."""
    p = make_e0(6)
    acts = (1, 2)
    law = exact_obs_law(p, acts).reshape(O, O)
    b = p.belief0(1)
    pred1 = p.predict(b)[0, acts[0]]
    assert np.allclose(pred1, law.sum(1), atol=1e-14)
    for o in range(O):
        b2 = p.update(b, np.array([acts[0]]), np.array([o]))
        pred2 = p.predict(b2)[0, acts[1]]
        assert np.allclose(pred2 * pred1[o], law[o], atol=1e-14)
