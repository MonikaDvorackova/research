import numpy as np
from scipy.stats import ks_2samp

from eid.agent import interact
from eid.env import SIGMA, RefEnv, gauss_logpdf, kl_gauss, ref_mean, sample_x0
from eid.model import Ensemble, GaussMLP


def test_negative_control_has_identical_law():
    rng = np.random.default_rng(0)
    x, a = sample_x0(rng, 200_000), rng.uniform(-3, 3, 200_000)
    r1 = RefEnv("direct").step(x, a, rng) - ref_mean(x, a)
    r2 = RefEnv("split").step(x, a, rng) - ref_mean(x, a)
    for d in range(2):
        assert ks_2samp(r1[:, d], r2[:, d]).pvalue > 0.01
        assert abs(r1[:, d].std() - r2[:, d].std()) < 0.002
    assert abs(r2[:, 0].std() - SIGMA) < 0.002


def test_kl_gauss_matches_monte_carlo():
    rng = np.random.default_rng(1)
    mu_p, mu_q = np.array([[0.2, -0.1]]), np.array([[0.5, 0.3]])
    sp, sq = np.array([[0.1, 0.1]]), np.array([[0.15, 0.08]])
    y = mu_p + sp * rng.standard_normal((400_000, 2))
    mc = (gauss_logpdf(y, mu_p, sp) - gauss_logpdf(y, mu_q, sq)).mean()
    assert abs(mc - kl_gauss(mu_p, sp, mu_q, sq)[0]) < 0.02


class _Opaque:
    """Environment stub: any use other than step() fails, proving the agent has no other access."""
    def __init__(self):
        self.inner = RefEnv("direct")

    def step(self, x, a, rng):
        return self.inner.step(x, a, rng)

    def __getattribute__(self, name):
        if name in ("step", "inner", "__class__"):
            return object.__getattribute__(self, name)
        raise AssertionError(f"agent touched env.{name}")


def test_agent_only_uses_step():
    import torch
    torch.manual_seed(0)
    ens = Ensemble([GaussMLP(8) for _ in range(2)])
    for policy in ("passive", "wide", "active"):
        X, A, Z = interact(_Opaque(), policy, ens, 5, 3, np.random.default_rng(0))
        assert X.shape == (5, 4, 2) and A.shape == (5, 3) and Z.shape == (5, 3, 2)
        assert np.abs(A).max() <= (1.0 if policy == "passive" else 3.0)


def test_ood_control_coincides_with_e0_in_distribution():
    from eid.env import ref_mean_ood
    rng = np.random.default_rng(2)
    x = sample_x0(rng, 1000)
    a_in, a_out = rng.uniform(-1, 1, 1000), rng.uniform(1.5, 3, 1000)
    assert np.allclose(ref_mean_ood(x, a_in, 0.7), ref_mean(x, a_in))
    assert np.abs(ref_mean_ood(x, a_out, 0.7) - ref_mean(x, a_out)).max() > 0.1


def test_poly_model_fits_in_distribution_and_fails_outside():
    from eid.model import train_poly
    rng = np.random.default_rng(0)
    x, a = sample_x0(rng, 5000), rng.uniform(-1, 1, 5000)
    y = RefEnv("direct").step(x, a, rng)
    m = train_poly(x, a, y)
    xt, at = sample_x0(rng, 2000), rng.uniform(-1, 1, 2000)
    assert np.abs(m.predict(xt, at)[0] - ref_mean(xt, at)).mean() < 0.02
    ao = rng.uniform(2.5, 3, 2000)
    assert np.abs(m.predict(xt, ao)[0] - ref_mean(xt, ao)).mean() > 0.1  # cubic cannot track sin(a) out there


def test_analytic_theory_is_calibrated_for_e0_under_any_policy():
    """With the true law as null, standardised residuals of E0 are N(0,1) whatever the (adaptive) policy: FPR ~ alpha."""
    from eid.metrics import prefix_stat
    from eid.model import AnalyticTheory
    import torch
    torch.manual_seed(0)
    sel = Ensemble([GaussMLP(8) for _ in range(2)])
    for policy in ("passive", "wide", "active"):
        _, _, Z = interact(RefEnv("direct"), policy, AnalyticTheory(), 4000, 10, np.random.default_rng(1), sel)
        assert abs(prefix_stat(Z, 10)[1].mean() - 0.05) < 0.02
