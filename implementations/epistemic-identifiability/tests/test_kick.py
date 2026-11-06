import sys, os, math
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.kick import world as W, model as M, algebra as A


def test_lfsr_is_maximal_and_deterministic():
    rng = np.random.default_rng(0)
    for n in (4, 7, 10):
        g = W.sample_gen("lfsr", n, rng)
        assert g.period(1) == 2 ** n - 1
        s1 = g.stream(np.array([3, 5]), 50); s2 = g.stream(np.array([3, 5]), 50)
        assert np.array_equal(s1, s2) and set(np.unique(s1)) <= {0, 1}
    g = W.sample_gen("nlfsr", 8, rng)
    assert g.period(1) >= 0.25 * 2 ** 8


def test_berlekamp_massey_recovers_linear_complexity_with_2n_bits():
    rng = np.random.default_rng(1)
    for n in (5, 9, 12):
        g = W.sample_gen("lfsr", n, rng); s = list(g.stream(np.array([7]), 4 * n)[0].astype(int))
        L, c = A.berlekamp_massey(s)
        assert L == n
        assert all(A.predict_lfsr(s[:t], L, c) == s[t] for t in range(2 * n, 4 * n))
    # a nonlinear-feedback register has larger linear complexity than its state size (BM, the linear class, does not explain it)
    g = W.sample_gen("nlfsr", 8, rng); s = list(g.stream(np.array([9]), 400)[0].astype(int))
    assert A.berlekamp_massey(s)[0] > 8


def test_gf2_solver_and_degree2_recurrence_on_nlfsr():
    rng = np.random.default_rng(2)
    g = W.sample_gen("nlfsr", 8, rng)
    seqs = [list(g.stream(np.array([k + 1]), 150)[0].astype(int)) for k in range(4)]
    fit = A.fit_recurrence(seqs, 8, 2)
    assert fit is not None
    fresh = g.stream(np.array([77]), 120)[0].astype(np.uint8)
    H = np.array([fresh[t - 8:t][::-1] for t in range(8, 120)], dtype=np.uint8)
    assert (A.predict_recurrence(fit, H) == fresh[8:]).all()
    # inconsistent system returns None
    assert A.gf2_solve(np.array([[1, 0], [1, 0]], dtype=np.uint8), np.array([0, 1], dtype=np.uint8)) is None


def test_replay_pair_deterministic_generator_repeats_random_does_not():
    rng = np.random.default_rng(3)
    g = W.sample_gen("lfsr", 12, rng)
    rp = W.replay_pair(g, 64, 48, rng); assert (rp["bits1"] == rp["bits2"]).all()
    rr = W.replay_pair(None, 64, 48, rng); assert abs((rr["bits1"] == rr["bits2"]).mean() - 0.5) < 0.05


def test_click_ce_is_null_valid_for_any_past_only_predictor():
    """Under iid fair bits any predictor computed from the past has E[CE] >= ln 2; the frozen-predictor z-test cannot reward it."""
    rng = np.random.default_rng(4)
    b = W.make_batch(None, 400, 96, rng)
    # an overconfident past-only predictor (always predicts the previous click with prob 0.9)
    prev = np.concatenate([np.zeros((400, 1)), b["click"][:, :-1]], 1)
    p = 0.1 + 0.8 * prev
    ce = -(b["click"] * np.log(p) + (1 - b["click"]) * np.log(1 - p))
    per = ce[:, 16:].mean(1); z = (math.log(2) - per.mean()) / (per.std(ddof=1) / math.sqrt(len(per)))
    assert z < 3.0 and per.mean() > math.log(2) - 0.05
    # a calibrated constant predictor sits at ln 2
    assert abs(-(np.log(0.5)) - math.log(2)) < 1e-12


def test_kick_model_shapes_and_training_step_reduces_loss():
    torch.manual_seed(0); rng = np.random.default_rng(5)
    g = W.sample_gen("lfsr", 4, rng); b = W.make_batch(g, 32, 40, rng)
    t = lambda x: torch.tensor(x, dtype=torch.float32)
    m = M.KickGRU(H=32); opt = torch.optim.Adam(m.parameters(), lr=3e-3)
    bce, nll, lg = m(t(b["obs"]), t(b["act"]), t(b["click"]))
    assert bce.shape == (32, 40) and nll.shape == (32, 40) and lg.shape == (32, 40)
    l0 = float((bce + nll).mean())
    for _ in range(40):
        bce, nll, _ = m(t(b["obs"]), t(b["act"]), t(b["click"])); loss = (bce + nll).mean(); opt.zero_grad(); loss.backward(); opt.step()
    assert float(loss) < l0


def test_make_batch_determinism_and_click_equals_shock_bit():
    g = W.sample_gen("lfsr", 6, np.random.default_rng(6))
    b1 = W.make_batch(g, 8, 30, np.random.default_rng(7)); b2 = W.make_batch(g, 8, 30, np.random.default_rng(7))
    assert np.array_equal(b1["obs"], b2["obs"]) and np.array_equal(b1["click"], b1["bits"])
