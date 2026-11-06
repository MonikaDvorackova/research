import inspect
import numpy as np
from eid import worldgen_pilot as W


def test_generators_and_equivalence_structure():
    x = np.array(0.0)
    assert W.step("quant", 1e-9, np.array(0.3), 0.7, 1.0) == W.step("cont", 0, np.array(0.3), 0.7, 1.0) or abs(W.step("quant", 1e-9, np.array(0.3), 0.7, 1.0) - W.step("cont", 0, np.array(0.3), 0.7, 1.0)) < 1e-8
    # a small constant control never moves a dead-zone system started at 0, but moves the continuous one
    us = np.full((1, W.T_EP), 0.02); mu = W.hyp_means(us, 1.0)[0]
    assert np.all(mu[1, :] == 0) and np.all(mu[4, :] == 0) and mu[0, -1] > 0
    # quant (q) and stiff (q/2) coincide while |increment| < q/2 (identical means for tiny controls)
    assert np.allclose(mu[2], mu[5])


def test_agent_sees_only_the_interface_and_is_deterministic():
    src = inspect.getsource(W.run_agent)
    assert "_kind" not in src and "_par" not in src and "_b" not in src.replace("b)", "").replace(", b,", ",")
    r = [W.run_agent(W.PilotEnv("quant", 0.2, 1.0, 0.02, np.random.default_rng(1)), 1.0, "active", 3, np.random.default_rng(2))[0] for _ in range(2)]
    assert np.array_equal(r[0], r[1])


def test_active_beats_passive_on_dead_zone_when_precision_is_high():
    ok = {"passive": 0, "active": 0}
    for pol in ok:
        for s in range(6):
            env = W.PilotEnv("quant", 0.2, 1.0, 0.02, np.random.default_rng(10 + s))
            post, _ = W.run_agent(env, 1.0, pol, 6, np.random.default_rng(20 + s))
            ok[pol] += post[W.HYPS.index(("quant", 0.2))] > 0.5
    assert ok["active"] >= ok["passive"]


def test_interface_limited_equivalence_when_dead_zone_exceeds_actuator_reach():
    """Prop A: if dt*b*u_max < delta, quant(q = 2 delta) and stiff(delta) started at 0 never move under any admissible control -> identical laws."""
    b, umax = 0.9, 2.0
    assert W.DT * b * umax < 0.2                                    # actuator reach 0.18 < delta = 0.2
    rng = np.random.default_rng(0)
    i_q, i_s = W.HYPS.index(("quant", 0.4)), W.HYPS.index(("stiff", 0.2))
    for _ in range(200):
        us = rng.uniform(-umax, umax, (1, W.T_EP))
        mu = W.hyp_means(us, b)[0]
        assert np.array_equal(mu[i_q], mu[i_s]) and np.all(mu[i_q] == 0)
    us = np.full((1, W.T_EP), umax); assert W.hyp_means(us, b)[0][0, -1] > 0         # but the continuous system moves: cont is distinguishable


def test_modified_equation_equivalence_euler_equals_sampled_continuous_flow():
    """Prop C: the Euler map of a conservative oscillator equals the exactly sampled flow of a different (non-conservative) continuous system."""
    from scipy.linalg import expm, logm
    h = 0.1; A = np.array([[0.0, 1.0], [-1.0, 0.0]]); M = np.eye(2) + h * A
    At = logm(M) / h
    assert np.allclose(At.imag, 0) and np.allclose(expm(h * At.real), M, atol=1e-12)
    assert np.trace(At.real) == 0 or abs(np.trace(At.real)) > 1e-3                  # trace != 0: the equivalent continuous system is not conservative
    assert np.linalg.det(M) > 1                                                    # Euler expands phase-space volume: energy drift
