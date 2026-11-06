"""Exact checks for the Phase 6 prediction-vs-identification diagnostic."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
from phase6_prediction_vs_identification import policy_kl
from eid.pomdp import make_e0, perturb_action2


def test_no_informative_action_gives_zero_kl_and_kl_increases_with_q():
    e0 = make_e0(0)
    et = perturb_action2(e0, 0.5)
    assert abs(policy_kl(e0, et, 0.0, T=3)) < 1e-12
    ks = [policy_kl(e0, et, q, T=3) for q in (0.02, 0.1, 1 / 3)]
    assert ks[0] < ks[1] < ks[2]
