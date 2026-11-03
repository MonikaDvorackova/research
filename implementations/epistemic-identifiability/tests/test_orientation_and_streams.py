"""Part G audit: score-orientation errors, random-stream collisions in the Phase 5 code paths, class-balance handling."""
import numpy as np

from eid.analyze_bayes1 import GROUPS, _ece, metrics_seed
from eid.bayes1 import brng
from eid.run_bayes2 import rs


def _fake(regime="oracle", good=True, R=40):
    """Synthetic posteriors for the five scenarios: a perfect observer (posterior = one-hot truth) or an inverted one."""
    truth = {"E0": 0, "E0split": 0, "W": 1, "AltOOD": 2, "Ealt": 2}
    arrs = {}
    for sc, c in truth.items():
        p = np.zeros((R, 1, 3))
        k = c if good else (c + 1) % 3
        p[:, 0, k] = 1.0
        arrs[f"{regime}|full|uniform|{sc}|wide|post"] = p
        arrs[f"{regime}|full|uniform|{sc}|wide|dec_time"] = np.full(R, 1.0)
        arrs[f"{regime}|full|uniform|{sc}|wide|dec_class"] = np.full(R, k)
        arrs[f"{regime}|full|uniform|{sc}|wide|real_gain"] = np.zeros(R)
        arrs[f"{regime}|full|uniform|{sc}|wide|exp_gain"] = np.zeros(R)
    return arrs


def test_metric_orientation_perfect_and_inverted_observers():
    good = metrics_seed(_fake(good=True), "oracle", "wide", 0)
    bad = metrics_seed(_fake(good=False), "oracle", "wide", 0)
    assert good["acc3"] == 1.0 and good["h1v0_auroc"] == 1.0 and good["h1v2_auroc"] == 1.0 and good["false_id"] == 0.0
    assert bad["acc3"] == 0.0 and bad["false_id"] == 1.0
    assert bad["h1v0_auroc"] < 0.5 + 1e-9         # an observer that reports the wrong class is not rescued by the pairwise score


def test_class_balanced_accuracy_is_insensitive_to_scenario_counts():
    """Accuracy pools E0 and E0split (2 scenarios) into one class and AltOOD/Ealt (2) into one; W is one scenario. Perfect on H0 only gives 1/3."""
    arrs = _fake(good=True)
    for sc in ("W", "AltOOD", "Ealt"):
        p = arrs[f"oracle|full|uniform|{sc}|wide|post"]
        p[:] = 0
        p[:, 0, 0] = 1.0
    m = metrics_seed(arrs, "oracle", "wide", 0)
    assert abs(m["acc3"] - 1 / 3) < 1e-12


def test_ece_is_zero_for_perfectly_calibrated_confidence():
    rng = np.random.default_rng(0)
    conf = rng.uniform(0.3, 1.0, 200000)
    correct = (rng.random(200000) < conf).astype(float)
    assert _ece(conf, correct, np.ones_like(conf)) < 0.01


def test_phase5_streams_are_distinct():
    sig = set()
    for tag in ("env", "train", "q", "wp", "match", "sim", "exact"):
        for extra in range(40):
            sig.add(tuple(rs(300, tag, extra).random(3)))
    assert len(sig) == 7 * 40
    assert tuple(rs(300, "train", 0).random(3)) != tuple(rs(301, "train", 0).random(3))
    assert tuple(brng(300, "sim", 5).random(3)) != tuple(brng(301, "sim", 5).random(3))
