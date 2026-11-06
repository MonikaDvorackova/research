"""Sanity checks for the POMDP Bayesian observer (Gate 2, environment 2): chain rule, exact EIG, calibration, equivalence, interface."""
import itertools

import numpy as np
import pytest
import torch

from eid.bayes2 import (CLS, CatchAll, ContamMember, GRUMember, POMDPMember, Space2, _ent, class_probs, class_predictives, eig_myopic, eig_two_step,
                        run_observer2)
from eid.gruworld import GRUEnv, GRUWorld, POMDPEnv, gru_obs_law, sample_dataset, train_gru
from eid.pomdp import A, O, exact_obs_law, make_e0, perturb_action2, split_state0, with_emission_noise


def test_gru_assigns_a_proper_distribution_over_observation_sequences():
    torch.manual_seed(0)
    m = GRUWorld(8)
    for acts in [(0, 1, 2, 2), (2, 2, 2, 2)]:
        assert gru_obs_law(m, acts).sum() == pytest.approx(1.0, abs=1e-5)


def test_member_chain_rule_equals_exact_sequence_probability():
    """Product of one-step predictive probabilities from a POMDP member equals the exact enumerated law."""
    p = make_e0(1)
    mem = POMDPMember(p)
    acts = (2, 0, 1, 2)
    law = exact_obs_law(p, acts).reshape((O,) * len(acts))
    st = mem.init(1)
    for obs in itertools.product(range(O), repeat=len(acts)):
        st = mem.init(1)
        pr = 1.0
        for a, o in zip(acts, obs):
            pr *= mem.pred(st)[0, a, o]
            st = mem.update(st, np.array([a]), np.array([o]))
        assert pr == pytest.approx(law[obs], rel=1e-9, abs=1e-12)


def test_exact_eig_equals_brute_force_mutual_information():
    """One-step class EIG from class-conditional predictives equals mutual information computed from the joint (class, observation)."""
    ps = [make_e0(2), perturb_action2(make_e0(2), 0.5), with_emission_noise(make_e0(2), 0.3)]
    sp = Space2([POMDPMember(p) for p in ps], [0, 1, 2], (0.5, 0.3, 0.2, 0.0))
    sp.states = None
    sp.reset(2)
    logw = np.tile(sp.logprior, (2, 1))
    _, w = class_probs(sp, logw)
    P = sp.preds()
    e = eig_myopic(sp, w, P)
    pri = np.exp(sp.logprior)
    for a in range(A):
        joint = np.stack([pri[m] * P[m, 0, a] for m in range(3)])      # (class, o)
        mi = np.sum(joint * np.log(joint / (joint.sum(1, keepdims=True) * joint.sum(0, keepdims=True))))
        assert e[0, a] == pytest.approx(mi, abs=1e-12)


def test_two_step_eig_matches_brute_force_and_is_at_least_one_step():
    p = make_e0(3)
    ps = [p, perturb_action2(p, 0.6)]
    sp = Space2([POMDPMember(q) for q in ps], [0, 2], (0.5, 0.0, 0.5, 0.0))
    sp.states = None
    sp.reset(1)
    _, w = class_probs(sp, np.tile(sp.logprior, (1, 1)))
    P = sp.preds()
    e2 = eig_two_step(sp, w, P)[0]
    pri = np.exp(sp.logprior)
    for a1, a2 in [(0, 2), (2, 2), (1, 0)]:
        joint = np.stack([pri[m] * exact_obs_law(ps[m], (a1, a2)) for m in range(2)])
        mi = np.sum(joint * np.log(np.clip(joint, 1e-300, None) / (joint.sum(1, keepdims=True) * joint.sum(0, keepdims=True))))
        assert e2[a1, a2] == pytest.approx(mi, abs=1e-10)
    e1 = eig_myopic(sp, w, P)[0]
    assert e2[2, 2] + 1e-12 >= e1[2]                       # more steps can only add information about the class


def test_space_with_observationally_equivalent_members_keeps_prior_ratio():
    p = make_e0(4)
    q = split_state0(p)
    sp = Space2([POMDPMember(p), POMDPMember(q)], [0, 1], (0.7, 0.3, 0.0, 0.0))
    out = run_observer2(sp, POMDPEnv(p), "random", np.random.default_rng(0), R=20, steps=30, checkpoints=(30,))
    pr = out["post"][:, 0]
    assert np.allclose(pr[:, 0] / pr[:, 1], 0.7 / 0.3, rtol=1e-8)


@pytest.mark.parametrize("policy", ["random", "eig"])
def test_simulation_based_calibration_in_the_finite_world(policy):
    """Truth drawn from the prior over exact POMDP members; posterior class probabilities are calibrated (Bayesian coherence)."""
    p = make_e0(5)
    ps = [p, perturb_action2(p, 0.7), with_emission_noise(p, 0.25)]
    pri = np.array([0.5, 0.25, 0.25])
    N = 3000
    P_all, T_all = [], []
    for k, q in enumerate(ps):
        n = int(round(N * pri[k]))
        sp = Space2([POMDPMember(x) for x in ps], [0, 1, 2], (0.5, 0.25, 0.25, 0.0))
        out = run_observer2(sp, POMDPEnv(q), policy, np.random.default_rng(10 + k), R=n, steps=4, episode_len=4, checkpoints=(4,))
        P_all.append(out["post"][:, 0, :3])
        T_all += [k] * n
    P, T = np.concatenate(P_all), np.array(T_all)
    err = 0.0
    for c in range(3):
        bins = np.clip((P[:, c] * 5).astype(int), 0, 4)
        for b in range(5):
            s = bins == b
            if s.sum() > 50:
                err += s.mean() * abs(P[s, c].mean() - (T[s] == c).mean())
    assert err / 3 < 0.03, err


def test_observer_uses_only_the_observation_interface():
    class Spy:
        def __init__(self, env):
            self._e = env

        def reset(self, R, rng):
            return self._e.reset(R, rng)

        def step(self, a, rng):
            return self._e.step(a, rng)

        def __getattr__(self, name):
            raise AssertionError(f"touched env.{name}")
    p = make_e0(6)
    sp = Space2([POMDPMember(p), ContamMember(POMDPMember(p), 0.2), CatchAll()], [0, 2, 3], (0.4, 0.0, 0.4, 0.2))
    for pol in ("passive", "random", "sweep", "eig", "eig2"):
        out = run_observer2(sp, Spy(POMDPEnv(p)), pol, np.random.default_rng(1), R=3, steps=3, checkpoints=(3,))
        assert out["post"].shape == (3, 1, CLS)


def test_gru_world_trains_and_gru_env_samples_its_own_predictive():
    p = make_e0(7)
    a, o = sample_dataset(p, 200, 8, np.random.default_rng(0))
    m = train_gru(a, o, seed=0, steps=40)
    env, rng = GRUEnv(m), np.random.default_rng(1)
    env.reset(500, rng)
    mem = GRUMember(m)
    st = mem.init(500)
    act = np.zeros(500, dtype=int)
    pred = mem.pred(st)[0, 0]
    obs = env.step(act, rng)
    freq = np.bincount(obs, minlength=O) / 500
    assert np.abs(freq - pred).max() < 0.1


def test_equivalence_is_relative_to_the_intervention_class():
    """Exact: with truth Et, an observer holding exact E0 and Et members keeps the prior odds under a policy that never uses action 2,
    and moves away from them under a policy that does."""
    e0 = make_e0(8)
    et = perturb_action2(e0, 0.9)
    sp = Space2([POMDPMember(e0), POMDPMember(et)], [0, 2], (0.5, 0.0, 0.5, 0.0))
    out = run_observer2(sp, POMDPEnv(et), "no2", np.random.default_rng(0), R=30, steps=60, checkpoints=(60,))
    p = out["post"][:, 0]
    assert np.abs(p[:, 2] / p[:, 0] - 1.0).max() < 1e-8
    sp2 = Space2([POMDPMember(e0), POMDPMember(et)], [0, 2], (0.5, 0.0, 0.5, 0.0))
    out2 = run_observer2(sp2, POMDPEnv(et), "random", np.random.default_rng(0), R=30, steps=60, checkpoints=(60,))
    p2 = out2["post"][:, 0]
    assert np.abs(np.log(p2[:, 2] / p2[:, 0])).max() > 0.5
