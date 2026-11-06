import numpy as np
from eid.analyze_x1 import cp_upper, cp_lower, ratio_ci


def test_clopper_pearson_and_bootstrap_sanity():
    assert abs(cp_upper(0, 100) - (1 - 0.05 ** (1 / 100))) < 1e-9
    assert cp_lower(0, 10) == 0.0 and cp_upper(10, 10) == 1.0
    m, lo, hi = ratio_ci(np.log(np.full(12, 2.0)) + np.linspace(-.1, .1, 12), np.random.default_rng(1))
    assert lo < m < hi and 1.9 < m < 2.1
