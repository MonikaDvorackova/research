"""Phase 8 exact verifications and deterministic diagnostics."""
import itertools
import numpy as np
from eid.phase8 import (change_action2, counter_augmented, frozen_null_etest, markov_env, occam_dissociation, simulate_stream,
                        stationarity_etest, time_varying_law, learner_limit_and_entropy)
from eid.pomdp import A, O, exact_obs_law, make_e0


def test_occam_dissociation_exact():
    rows = dict((n, (p, k)) for n, p, k in occam_dissociation([1, 5, 10, 100, 1000]))
    assert abs(rows[1][0] - 0.5) < 1e-12                                   # n = 1: posterior = prior
    assert rows[5][0] > rows[10][0] > rows[100][0] > rows[1000][0]         # identification of the TRUE mechanism decays with n
    assert rows[10][1] > rows[100][1] > rows[1000][1]                      # while predictive KL vanishes
    assert rows[1000][0] < 0.1 and rows[1000][1] < 1e-4


def test_time_varying_kernel_equals_stationary_counter_model():
    e0 = make_e0(0)
    Zs = [e0.Z, e0.Z, 0.7 * e0.Z + 0.1, 0.7 * e0.Z + 0.1]
    aug = counter_augmented(e0, Zs)
    for acts in itertools.product(range(A), repeat=4):
        assert np.abs(time_varying_law(e0, acts, Zs) - exact_obs_law(aug, acts)).max() < 1e-12


def test_entropy_limits_markov_vs_hidden():
    H, d1, _ = learner_limit_and_entropy(markov_env(1), 1)
    assert abs(d1) < 1e-9                                                    # Markov truth is inside the order-1 class
    H2, d2, _ = learner_limit_and_entropy(make_e0(1), 1)
    assert d2 > 1e-2                                                         # hidden-state truth is not


def test_stationarity_eprocess_valid_and_powerful_with_coverage_only():
    mk = markov_env(1); mk2 = change_action2(mk, 1)
    rng = lambda i: np.random.default_rng(np.random.SeedSequence([88, i]))
    null = [stationarity_etest(*simulate_stream((mk, mk), None, lambda e: 1 / 3, 1200, 4, rng(i)))[1] for i in range(15)]
    chg = [stationarity_etest(*simulate_stream((mk, mk2), 600, lambda e: 1 / 3, 1200, 4, rng(100 + i)))[1] for i in range(15)]
    low = [stationarity_etest(*simulate_stream((mk, mk2), 600, lambda e: 0.0, 1200, 4, rng(200 + i)))[1] for i in range(15)]
    assert sum(e is not None for e in null) == 0
    assert sum(e is not None for e in chg) >= 12
    assert sum(e is not None for e in low) == 0                              # no action 2 -> the changed rows are never visited


def test_frozen_learned_null_false_alarms_on_unchanged_kernel_with_narrow_training():
    mk = markov_env(1)
    k = 0
    for i in range(10):
        tr = simulate_stream((mk, mk), None, lambda e: 0.02, 100, 4, np.random.default_rng(np.random.SeedSequence([77, i, 0])))
        te = simulate_stream((mk, mk), None, lambda e: 1 / 3, 3000, 4, np.random.default_rng(np.random.SeedSequence([77, i, 1])))
        k += frozen_null_etest(*tr, *te)[1] is not None
    assert k >= 9
