"""Invariant checks required by PHASE 1G before execution:
(2) B and C contain the same underlying artifact facts;
(3) C's only intended additional signal is explicit binding;
(4) Regime A/B/C views cannot leak forbidden fields.
"""

import dataclasses

from src.cases import all_worlds
from src.regimes import (
    RegimeAView, RegimeBView, RegimeCView,
    regime_a_view, regime_b_view, regime_c_view, verify_b_c_equivalence,
)


def test_regime_a_view_has_no_history_or_binding_fields():
    fields = {f.name for f in dataclasses.fields(RegimeAView)}
    forbidden = {
        "policy_history", "authority_history", "model_history", "watchlist_history",
        "event_trace", "binding", "ground_truth",
    }
    assert fields.isdisjoint(forbidden), fields & forbidden


def test_regime_b_view_has_no_binding_or_ground_truth_fields():
    fields = {f.name for f in dataclasses.fields(RegimeBView)}
    forbidden = {"binding", "ground_truth", "live_policy", "live_authority", "live_model", "live_watchlist"}
    assert fields.isdisjoint(forbidden), fields & forbidden


def test_regime_c_view_has_no_ground_truth_field_and_has_binding():
    fields = {f.name for f in dataclasses.fields(RegimeCView)}
    assert "ground_truth" not in fields
    assert "binding" in fields


def test_regime_c_is_regime_b_plus_binding_for_every_case():
    for world in all_worlds():
        verify_b_c_equivalence(world)


def test_regime_a_view_cannot_be_used_to_reach_history():
    world = all_worlds()[0]
    view = regime_a_view(world)
    # Structural guarantee: no attribute access path exists from the view
    # object back to history, event trace, or binding.
    for forbidden_attr in ("policy_history", "authority_history", "event_trace", "binding"):
        assert not hasattr(view, forbidden_attr)


def test_regime_b_view_cannot_be_used_to_reach_binding():
    world = all_worlds()[0]
    view = regime_b_view(world)
    assert not hasattr(view, "binding")


def test_binding_references_only_facts_present_in_b_history():
    for world in all_worlds():
        b = regime_b_view(world)
        c = regime_c_view(world)
        policy_ids = {p.version_id for p in b.policy_history}
        authority_ids = {a.agent_id for a in b.authority_history}
        model_ids = {m.version_id for m in b.model_history}
        assert c.binding.policy_ref["version_id"] in policy_ids
        assert c.binding.authority_ref["agent_id"] in authority_ids
        assert c.binding.model_ref["version_id"] in model_ids
