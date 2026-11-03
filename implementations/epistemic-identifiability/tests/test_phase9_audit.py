"""Phase 9 independent computational checks of audited claims."""
import itertools
import numpy as np
from eid.pomdp import A, O, exact_obs_law, make_e0, perturb_action2
from eid.phase9_audit import (chernoff_exponent, change_time_mixture_law, cp_upper, max_k_for_upper, occam_offset,
                              prob_demonstrate_bound, regime_hmm_law, runs_needed_zero)
from eid.phase8 import occam_dissociation


def test_occam_offset_matches_phase8_at_half_and_is_nonmonotone_off_half():
    a = dict((n, p) for n, p, _ in occam_dissociation([10, 100, 1000]))
    b = dict((n, p) for n, p, _ in occam_offset([10, 100, 1000], 0.5))
    assert all(abs(a[n] - b[n]) < 1e-9 for n in a)                       # independent implementation agrees at the non-generic truth
    off = dict((n, p) for n, p, _ in occam_offset([10, 100, 1000, 10000], 0.56))
    assert off[100] < off[10] or off[1000] > off[100]                      # generic truth: identification eventually improves
    assert off[10000] > 0.99 and off[1000] > off[100]


def test_regime_chain_equals_change_time_mixture_exactly():
    q0 = np.array([.7, .2, .1]); q1 = np.array([.2, .3, .5])
    a = regime_hmm_law(q0, q1, 0.13, 4); b = change_time_mixture_law(q0, q1, 0.13, 4)
    assert max(abs(a[k] - b[k]) for k in a) < 1e-15 and abs(sum(a.values()) - 1) < 1e-12


def test_binomial_claim_arithmetic():
    assert runs_needed_zero(0.07) == 42 and runs_needed_zero(0.05) == 59        # zero rejections: runs needed to certify rate <= thr at 95 %
    assert cp_upper(0, 20) > 0.13                                                # 20 runs per structure cannot certify a per-structure bound of 0.07
    # pooled 600 runs: true rate 0.02 -> certifies <= 0.07 almost surely; true rate 0.05 -> certifies <= 0.07 only sometimes
    assert prob_demonstrate_bound(600, 0.02, 0.07) > 0.999
    assert 0.2 < prob_demonstrate_bound(600, 0.05, 0.07) < 0.99


def test_chernoff_exponent_exceeds_uniform_and_matches_closed_form_on_two_actions():
    K = np.array([[0.0, 1.0], [0.5, 0.5]])                                # two competitors, two 'actions'
    val, lam = chernoff_exponent(K)
    unif = min(K @ np.array([.5, .5]))
    assert val >= unif - 1e-9 and abs(val - 0.5) < 1e-6                   # competitor 2 caps the exponent at 0.5 whatever lambda is


def _filter_pred(model, acts, obs):
    """Explicit-loop predictive distribution of the next observation given history (acts includes the NEXT action as last entry)."""
    S = model.S
    b = [float(x) for x in model.b0]
    for a, o in zip(acts[:-1], obs):
        pred = [sum(b[s] * model.T[a, s, t] for s in range(S)) for t in range(S)]
        po = sum(pred[t] * model.Z[t, o] for t in range(S))
        b = [pred[t] * model.Z[t, o] / po for t in range(S)]
    a = acts[-1]
    pred = [sum(b[s] * model.T[a, s, t] for s in range(S)) for t in range(S)]
    return np.array([sum(pred[t] * model.Z[t, o] for t in range(S)) for o in range(O)])


def test_chain_rule_for_kl_holds_under_an_adaptive_policy_independent_enumeration():
    """Prop 2(b) with a history-dependent policy: KL(P0||P1) = E_P0 sum_t KL(p0(.|h,a_t) || p1(.|h,a_t)), by explicit path enumeration."""
    p0 = make_e0(3); p1 = perturb_action2(p0, 0.5)
    T = 3
    policy = lambda obs: 0 if not obs else (obs[-1] + 1) % 3           # a_1 = 0, then depends on the last observation
    kl_direct, kl_chain = 0.0, 0.0
    for obs in itertools.product(range(O), repeat=T):
        acts = [policy(obs[:t]) for t in range(T)]
        pr0 = pr1 = 1.0
        for t in range(T):
            q0 = _filter_pred(p0, acts[:t + 1], obs[:t]); q1 = _filter_pred(p1, acts[:t + 1], obs[:t])
            pr0 *= q0[obs[t]]; pr1 *= q1[obs[t]]
        kl_direct += pr0 * np.log(pr0 / pr1)
    # chain-rule side: expectation under P0 of per-step conditional KL, computed by recursion over prefixes
    def rec(obs_prefix, prob):
        nonlocal kl_chain
        t = len(obs_prefix)
        if t == T:
            return
        acts = [policy(obs_prefix[:s]) for s in range(t + 1)]
        q0 = _filter_pred(p0, acts, obs_prefix); q1 = _filter_pred(p1, acts, obs_prefix)
        kl_chain += prob * float(np.sum(q0 * np.log(q0 / q1)))
        for o in range(O):
            rec(obs_prefix + (o,), prob * q0[o])
    rec((), 1.0)
    assert abs(kl_direct - kl_chain) < 1e-12 and kl_direct > 1e-4


def test_adaptive_wald_lower_bound_on_expected_stopping_time():
    """PO-2: E[tau] >= ln(omega)/delta_max for the first time the posterior log-odds drop below zero, any adaptive design (Wald with conditional KL <= delta_max).
    Monte Carlo on a two-armed Bernoulli pair with an adaptive arm rule."""
    rng = np.random.default_rng(5)
    p0 = np.array([0.5, 0.5]); p1 = np.array([0.5, 0.8])                 # arm 1 distinguishes; arm 0 does not
    kl = lambda a, b: a * np.log(a / b) + (1 - a) * np.log((1 - a) / (1 - b))
    dmax = max(kl(p0[0], p1[0]), kl(p0[1], p1[1])); omega = np.exp(6.0)
    taus = []
    for _ in range(300):
        S, t = np.log(omega), 0
        while S > 0 and t < 10000:
            arm = 1 if (t % 3 or S > 3) else 0                              # adaptive rule depending on the running log-odds
            x = rng.random() < p0[arm]                                      # E0 true
            S += np.log((1 - p1[arm]) / (1 - p0[arm])) if not x else np.log(p1[arm] / p0[arm])
            t += 1
        taus.append(t)
    assert np.mean(taus) >= np.log(omega) / dmax - 3 * np.std(taus) / np.sqrt(len(taus))


def test_exact_supremum_is_valid_and_grid_maximiser_is_not_exact_dp():
    """Bernoulli stream, truth p = 0.5 inside the null interval [0.3, 0.7].  Exact sup: P(reject by N) <= alpha (Ville).  Denominator maximised over the
    grid {0.3, 0.7} only (the true value missed): rejection probability is far above alpha and grows with N.  Exact dynamic programming, no Monte Carlo."""
    from eid.phase10_exact import rejection_probability, sup_grid, sup_interval
    alpha = 0.05
    valid = rejection_probability(0.5, 1500, alpha, lambda k, n: sup_interval(k, n, 0.3, 0.7))
    grid = lambda k, n: sup_grid(k, n, [0.3, 0.7])
    bad_500 = rejection_probability(0.5, 500, alpha, grid); bad_1500 = rejection_probability(0.5, 1500, alpha, grid)
    assert valid <= alpha and bad_1500 > 0.5 and bad_1500 >= bad_500 > alpha
