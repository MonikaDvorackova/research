import sys, os
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.gwb import gen, agents, models, policies, evalcore as ev, train as tr


def _u(n, L=48, seed=0, kind="uniform"):
    return policies.sample_actions(kind, n, L, torch.Generator().manual_seed(seed))


def test_sampling_deterministic_and_fields():
    a = gen.sample_instances(50, "train", seed=3); b = gen.sample_instances(50, "train", seed=3)
    for k in ("cls", "K", "b", "p", "sigma", "label"):
        assert torch.equal(a[k], b[k])
    assert set(a["cls"].tolist()) <= set(range(6))
    assert (a["label"] == a["cls"]).all()
    assert (a["sigma"][a["fam"] == 1].min() >= 2.5 * 0.08 - 1e-9)


def test_cont_matches_euler_and_delay_is_shift():
    n = 5
    K = torch.full((n,), 0.5, dtype=torch.float64); b = torch.full((n,), 1.0, dtype=torch.float64)
    u = _u(n)
    x = gen.simulate(torch.zeros(n, dtype=torch.long), K, b, torch.zeros(n, dtype=torch.float64), u)
    ref = torch.zeros(n, dtype=torch.float64)
    for t in range(48):
        ref = ref + gen.DT * (-0.5 * ref + u[:, t]); assert torch.allclose(x[:, t], ref)
    d = 3
    xd = gen.simulate(torch.full((n,), 3), K, b, torch.full((n,), float(d), dtype=torch.float64), u)
    ush = torch.cat([torch.zeros(n, d, dtype=torch.float64), u[:, :-d]], 1)
    xs = gen.simulate(torch.zeros(n, dtype=torch.long), K, b, torch.zeros(n, dtype=torch.float64), ush)
    assert torch.allclose(xd, xs)


def test_equivalent_worlds_have_identical_law():
    for reg in ("eqA", "eqB"):
        inst = gen.sample_instances(200, reg, seed=1)
        for kind in ("uniform", "sweep", "block", "pulse"):
            u = _u(200, kind=kind)
            x = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u)
            assert x.abs().max() == 0.0, (reg, kind)      # both members: y is pure noise => identical observation law
        assert (inst["label"] == -1).all() and len(set(inst["cls"].tolist())) == 2


def test_oracle_does_not_claim_on_equivalent_worlds_but_claims_on_identifiable():
    g = torch.Generator().manual_seed(0)
    inst = gen.sample_instances(150, "eqA", seed=2)
    u, y = agents.interact("oracle_eig", inst, 48, g)
    pr = ev.oracle_probs(inst, u, y)
    assert ev.metrics_eq(pr, 0.8)["claim_rate"] < 0.05
    idn = gen.sample_instances(150, "train", seed=2)
    u, y = agents.interact("oracle_eig", idn, 48, g)
    acc = (ev.oracle_probs(idn, u, y).argmax(1) == idn["label"].numpy()).mean()
    assert acc > 0.8


def test_oracle_eig_beats_passive():
    inst = gen.sample_instances(250, "train", seed=5)
    accs = {}
    for c in ("passive", "oracle_eig"):
        g = torch.Generator().manual_seed(1)
        u, y = agents.interact(c, inst, 48, g)
        accs[c] = (ev.oracle_probs(inst, u, y).argmax(1) == inst["label"].numpy()).mean()
    assert accs["oracle_eig"] > accs["passive"] + 0.1


def test_paired_noise_shared_across_conditions():
    inst = gen.sample_instances(20, "train", seed=1)
    N = 20
    eps = torch.randn(N, 48, generator=torch.Generator().manual_seed(4), dtype=torch.float64)
    u1, y1 = agents.interact("uniform", inst, 48, torch.Generator().manual_seed(2), eps=eps)
    x = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u1)
    assert torch.allclose(y1 - x, inst["sigma"][:, None] * eps)


def test_no_label_leakage_through_interface():
    """Models accept only (a, y); instance labels / hidden params cannot influence model outputs or interaction."""
    inst = gen.sample_instances(30, "train", seed=1)
    inst2 = dict(inst); inst2["label"] = (inst["label"] + 1) % 6
    inst2["fam"] = 1 - inst["fam"]
    u1, y1 = agents.interact("uniform", inst, 48, torch.Generator().manual_seed(2))
    u2, y2 = agents.interact("uniform", inst2, 48, torch.Generator().manual_seed(2))
    assert torch.equal(u1, u2) and torch.equal(y1, y2)
    import inspect
    for M in (models.RSSM, models.DetGRU):
        assert list(inspect.signature(M.forward).parameters)[1:3] == ["a", "y"]


def test_models_forward_shapes_finite_and_filter_consistent():
    torch.manual_seed(0)
    a = _u(6, 24).float(); inst = gen.sample_instances(6, "train", seed=0)
    y, _ = gen.observe(inst, a.double(), torch.Generator().manual_seed(1)); y = y.float()
    for M in (models.RSSM(H=32), models.DetGRU(H=32)):
        o = M(a, y, sample=False)
        assert o["nll"].shape == (6, 24) and torch.isfinite(o["nll"]).all() and o["feat"].shape == (6, 32)
        h, z, mu, ls = M.filter(a, y)
        assert mu.shape == (6, 24)
        r = M.rollout(h, z, a[:, :5]); assert r.shape == (6, 5)
        (o["nll"].mean() + o["kl"].mean()).backward()
        named = {n: p for n, p in M.named_parameters() if not n.startswith("proj")}   # proj head only used by ICI
        assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in named.values())


def test_infonce_prefers_matched_pairs():
    e = torch.randn(32, 16)
    assert models.info_nce(e, e) < models.info_nce(e, torch.randn(32, 16))


def test_training_batch_is_deterministic_in_seed_and_step():
    _, v1 = tr.make_batch(7, 3, 8, 48, "cpu"); _, v2 = tr.make_batch(7, 3, 8, 48, "cpu")
    assert torch.equal(v1[0][1], v2[0][1]) and not torch.equal(v1[0][1], v1[1][1])


def test_train_resume_equals_uninterrupted(tmp_path):
    a = str(tmp_path / "a"); b = str(tmp_path / "b")
    common = ["--model", "det", "--H", "16", "--batch", "8", "--seed", "1", "--threads", "1"]
    tr.main(common + ["--steps", "250", "--out", a])
    tr.main(common + ["--steps", "250", "--budget_s", "0", "--out", b])  # stops after 1 step, checkpoints
    tr.main(common + ["--steps", "250", "--out", b])
    sa = torch.load(os.path.join(a, "final.pt")); sb = torch.load(os.path.join(b, "final.pt"))
    for k in sa:
        assert torch.allclose(sa[k], sb[k], atol=1e-6), k


def test_passive_quiescent_system_reveals_nothing_but_interventions_do():
    """Counterexample (predictive sufficiency under a policy discards class): with a_t = 0 every class gives x == 0,
    so a representation sufficient for prediction under that policy carries no class information."""
    n = 60
    inst = gen.sample_instances(n, "train", seed=11)
    u0 = torch.zeros(n, 48, dtype=torch.float64)
    x0 = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u0)
    assert x0.abs().max() == 0.0
    x1 = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], _u(n, kind="sweep"))
    assert x1.abs().max() > 0.1
    # and the oracle posterior under passive-zero actions stays at its prior within each family
    g = torch.Generator().manual_seed(0)
    y = inst["sigma"][:, None] * torch.randn(n, 48, generator=g, dtype=torch.float64)
    pr = ev.oracle_probs(inst, u0, y)
    assert pr.max() < 0.5


def test_ece_and_probe_utilities():
    lab = np.array([0, 1, 2, 3] * 25)
    perfect = np.eye(6)[lab]
    assert ev.ece(perfect, lab) == 0.0
    assert ev.metrics_id(perfect, lab)["acc"] == 1.0
    over = np.eye(6)[(lab + 1) % 6]
    assert ev.ece(over, lab) == 1.0 and ev.metrics_eq(over)["claim_rate"] == 1.0
    F = np.random.default_rng(0).normal(size=(200, 5)); l = (F[:, 0] > 0).astype(int)
    pr = ev.probe_probs(ev.fit_probe(F, l), F)
    assert pr.shape == (200, 6) and (pr.argmax(1) == l).mean() > 0.9 and np.allclose(pr.sum(1), 1)


def test_matched_oracle_restricted_prior_and_hand_features_shape():
    inst = gen.sample_instances(40, "train", seed=3)
    u, y = agents.interact("uniform", inst, 48, torch.Generator().manual_seed(1))
    a = ev.oracle_probs(inst, u, y, matched=False); b = ev.oracle_probs(inst, u, y, matched=True)
    assert np.allclose(a.sum(1), 1) and np.allclose(b.sum(1), 1)
    assert gen.HGRID[0] != gen.HGRID_MATCHED[0]            # grid restored after matched call
    assert ev.hand_features(u, y).shape[0] == 40


def test_untrained_init_checkpoint_has_no_training(tmp_path):
    tr.main(["--model", "det", "--steps", "0", "--H", "16", "--out", str(tmp_path / "u"), "--seed", "1"])
    assert os.path.exists(tmp_path / "u" / "final.pt")
