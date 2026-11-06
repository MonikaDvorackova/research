"""X1 implementation checks: exact likelihood factorisation under adaptive policies, equivalence/barrier controls, determinism, no leakage."""
import inspect
import itertools
import numpy as np
from eid import x1
from eid.pomdp import A, O, exact_obs_law
from eid.x1 import Sampler, build_class, run, truths_for
from eid.x1_exact import policy_kl


def _seq_prob(m, acts_fn, T):
    """Total probability of all observation sequences when actions are chosen by acts_fn(past_obs) -- must be 1 for every model."""
    tot = 0.0
    for obs in itertools.product(range(O), repeat=T):
        acts = []
        for t in range(T):
            acts.append(acts_fn(obs[:t]))
        law = exact_obs_law(m, acts)
        tot += law[np.ravel_multi_index(obs, (O,) * T)]
    return tot


def test_adaptive_policy_preserves_normalisation_and_ratio_martingale():
    e0, M, W = build_class(1)
    f = lambda past: (past[-1] + 1) % A if past else 0          # adaptive: action depends on the observation history
    comps = [m for _, m in M] + [w for _, w in W]
    # each model's likelihood of an adaptively collected history is a proper law -> q (a mixture) is too -> E_truth[q/p_truth] = 1
    for m in comps[:6]:
        assert abs(_seq_prob(m, f, 3) - 1) < 1e-10
    q_total = np.mean([_seq_prob(m, f, 3) for m in comps])
    assert abs(q_total - 1) < 1e-10


def test_equivalence_and_barrier_controls_are_exact():
    tr = truths_for(2)
    e0, M, W = build_class(2)
    assert abs(policy_kl(tr["split"][0], e0, 1 / 3, T=3)) < 1e-12
    for name in ("t05", "t10"):
        assert abs(policy_kl(tr[name][0], e0, 0.0, T=3)) < 1e-12
        assert policy_kl(tr[name][0], e0, 1 / 3, T=3) > 1e-4
    assert abs(policy_kl(tr["pc2"][0], e0, 0.0, T=3)) < 1e-12        # pc2 differs only in action-2 rows


def test_run_is_deterministic_and_observer_never_touches_truth():
    e0, M, W = build_class(3)
    out = []
    for _ in range(2):
        env = Sampler(truths_for(3)["pc1"][0], np.random.default_rng(5))
        out.append(run(env, M, W, "P4", 60, 3, np.random.default_rng(6)))
    assert out[0] == out[1]
    src = inspect.getsource(x1.run) + inspect.getsource(x1._choose)
    assert "env.truth" not in src and ".truth" not in src


def test_null_run_never_rejects_in_a_short_smoke_run():
    e0, M, W = build_class(4)
    rej = 0
    for rep in range(10):
        env = Sampler(e0, np.random.default_rng([4, rep]))
        rej += run(env, M, W, "P2", 80, 3, np.random.default_rng([5, rep]))["reject_episode"] <= 80
    assert rej == 0
