import numpy as np
from scipy.optimize import minimize
from eid.e6proc import (_row_sup, comp_cs_test, cp_etest, cs_repair_etest, ctx_etest, ep_etest, prequential_probs)
from eid.phase8 import markov_env, simulate_stream, stationarity_etest, change_action2
from eid.pomdp import make_e0


def _stream(env, N, seed, p2=1 / 3):
    return simulate_stream((env, env), None, lambda e: p2, N, 4, np.random.default_rng(np.random.SeedSequence([5, seed])))


def test_generic_changepoint_equals_phase8_implementation():
    ctx, obs = _stream(markov_env(2), 600, 1)
    assert abs(stationarity_etest(ctx, obs)[0] - ctx_etest(ctx, obs)[0]) < 1e-9


def test_row_supremum_matches_numerical_optimiser():
    r = np.random.default_rng(0)
    for _ in range(20):
        n = r.integers(0, 30, 3).astype(float); lo = np.array([0.05, 0.1, 0.0]); hi = np.array([0.7, 0.6, 0.9])
        v = _row_sup(n, lo, hi)
        res = minimize(lambda x: -(n * np.log(np.clip(x, 1e-12, None))).sum(), x0=np.array([.3, .3, .4]),
                       bounds=list(zip(lo, hi)), constraints={"type": "eq", "fun": lambda x: x.sum() - 1}, method="SLSQP")
        assert abs(v - (-res.fun)) < 1e-4


def test_robbins_boundary_validity_under_dependent_martingale_noise():
    # martingale differences with conditional range [-2,2] and dependence: sign flips depending on the past
    rej = 0
    for i in range(300):
        r = np.random.default_rng([6, i]); n = 3000; z = np.empty(n); s = 1.0
        for t in range(n):
            s = -s if r.random() < 0.3 else s
            z[t] = s * 2 * r.choice([-1.0, 1.0])            # conditionally mean zero given the past, |Z| = 2
        S = np.cumsum(z); tt = np.arange(1, n + 1)
        rej += bool((S >= 2 * np.sqrt((tt + 2000) * np.log((tt + 2000) / (2000 * 0.05 ** 2)))).any())
    assert rej / 300 <= 0.05


def test_episode_level_test_is_valid_for_hidden_state_truth_with_resets():
    k = 0
    for i in range(12):
        ctx, obs = _stream(make_e0(i), 500, 10 + i)
        k += ep_etest(ctx, obs)[1] is not None
    assert k == 0


def test_cs_repair_no_false_rejection_and_vacuous_without_coverage():
    mk = markov_env(1); mk2 = change_action2(mk, 1)
    fa = 0
    for i in range(8):
        tr = simulate_stream((mk, mk), None, lambda e: 0.02, 3000, 4, np.random.default_rng([7, i, 0]))
        te = simulate_stream((mk, mk), None, lambda e: 1 / 3, 1500, 4, np.random.default_rng([7, i, 1]))
        fa += cs_repair_etest(*tr, *te) is not None
    assert fa == 0
    tr = simulate_stream((mk, mk), None, lambda e: 0.0, 3000, 4, np.random.default_rng([8, 0]))
    ch = simulate_stream((mk, mk2), 100, lambda e: 1 / 3, 1500, 4, np.random.default_rng([8, 1]))
    assert cs_repair_etest(*tr, *ch) is None                 # contexts with action 2 never seen in training: box is [0,1], no power


def test_procedures_receive_only_data_arrays_no_environment_objects():
    import inspect
    from eid import e6proc
    for fn in (e6proc.ctx_etest, e6proc.ep_etest, e6proc.comp_cs_test, e6proc.cs_repair_etest, e6proc.cp_etest, e6proc.prequential_probs):
        names = set(inspect.signature(fn).parameters)
        assert not (names & {"env", "truth", "pomdp", "kernel", "labels", "label"})
    import ast
    tree = ast.parse(inspect.getsource(e6proc))
    ids = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)} | {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    assert not (ids & {"truth", "env", "pomdp", "labels"})                       # code (not docstrings) never references a true environment
