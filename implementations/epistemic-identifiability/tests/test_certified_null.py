import itertools
import numpy as np
from scipy.optimize import minimize
from eid.certified_null import in_set, lr_gamma, sup_over_set, _xlogy
from eid.e6proc import dir_logml


def test_sup_matches_numerical_optimiser_and_is_an_upper_bound():
    r = np.random.default_rng(1)
    for _ in range(12):
        n = r.integers(0, 40, (3, 3)).astype(float); m = r.integers(0, 40, (3, 3)).astype(float)
        gamma = dir_logml(n) - np.log(20)
        v = sup_over_set(m, n, gamma)
        f = lambda x: -(_xlogy(m, x.reshape(3, 3)).sum())
        cons = [{"type": "eq", "fun": lambda x, i=i: x.reshape(3, 3)[i].sum() - 1} for i in range(3)] + \
               [{"type": "ineq", "fun": lambda x: _xlogy(n, np.clip(x.reshape(3, 3), 1e-12, 1)).sum() - gamma}]
        best = max(-minimize(f, x0=np.full(9, 1 / 3), bounds=[(1e-9, 1)] * 9, constraints=cons, method="SLSQP").fun, -1e9)
        assert v >= best - 1e-6 and v - best < 1e-3


def _exact_overall_rejection(nu_true, ntr, nte, alpha, delta):
    """Exhaustive enumeration: 2 contexts, binary outcomes, adaptive context rule c_{t+1} = o_t (start 0).  Returns
    (P(nu* not in C at some training prefix), P(reject at some test checkpoint), P(reject and nu* in C)).  Exact up to the sup solver."""
    def paths(T, start=0):
        for outs in itertools.product((0, 1), repeat=T):
            c, pr, cnt = start, 1.0, np.zeros((2, 2))
            seq = []
            for o in outs:
                p1 = nu_true[c]
                pr *= p1 if o == 1 else 1 - p1
                cnt[c, o] += 1; seq.append(cnt.copy()); c = o
            yield pr, seq
    nu = np.stack([1 - np.array(nu_true), np.array(nu_true)], 1)
    p_out = p_rej = p_both = 0.0
    tests = list(paths(nte))
    for ptr, seq_tr in paths(ntr):
        out = any(not in_set(nu, cnt, delta) for cnt in seq_tr)
        cnt_tr = seq_tr[-1]
        gam = lr_gamma(cnt_tr, delta)
        rej_prob = 0.0
        for pte, seq_te in tests:
            if any(dir_logml(m) - sup_over_set(m, cnt_tr, gam) >= np.log(1 / alpha) for m in seq_te):
                rej_prob += pte
        p_out += ptr * out; p_rej += ptr * rej_prob; p_both += ptr * rej_prob * (not out)
    return p_out, p_rej, p_both


def test_exact_enumeration_certified_test_respects_alpha_plus_delta_under_adaptive_contexts():
    alpha, delta = 0.4, 0.3
    for nu_true in itertools.product((0.1, 0.5, 0.9), repeat=2):
        p_out, p_rej, p_both = _exact_overall_rejection(list(nu_true), 4, 5, alpha, delta)
        assert p_out <= delta + 1e-9                                        # time-uniform coverage of the LR confidence set
        assert p_both <= alpha + 1e-9                                       # conditional on coverage, size <= alpha
        assert p_rej <= alpha + delta + 1e-9                                # overall guarantee


def test_exact_expected_evalue_is_at_most_one_when_truth_in_confidence_set():
    """Non-vacuous exact check (dynamic programming over count states): given training counts for which the truth lies in C, E[E_N] <= 1, for several truths."""
    from eid.phase10_exact import expected_evalue_certified
    delta = 0.3
    for nu in ((0.2, 0.8), (0.5, 0.5)):
        nu_m = np.array([[1 - nu[0], nu[0]], [1 - nu[1], nu[1]]])
        seen_in = 0
        for tr in ([[2, 1], [1, 1]], [[1, 2], [1, 1]], [[3, 0], [0, 2]], [[1, 1], [2, 1]], [[2, 2], [1, 0]]):
            tr = np.array(tr, float)
            if in_set(nu_m, tr, delta):
                seen_in += 1
                assert expected_evalue_certified(nu, tr, delta, 6) <= 1 + 1e-9
        assert seen_in >= 2
