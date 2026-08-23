"""Step 12 required checks:
- B cannot infer hidden precision;
- C does not receive hidden precision either;
- C uses binding only;
- B/C equivalence (with F10-6's single, disclosed exemption).
"""

import dataclasses

from src.cases import all_worlds
from src.regimes import RegimeBView, RegimeCView, regime_b_view, regime_c_view, verify_b_c_equivalence


def test_neither_view_type_carries_true_t0_or_ground_truth():
    forbidden = {"true_t0", "ground_truth"}
    for view_type in (RegimeBView, RegimeCView):
        fields = {f.name for f in dataclasses.fields(view_type)}
        assert fields.isdisjoint(forbidden), fields & forbidden


def test_b_and_c_views_only_ever_carry_observed_t0_not_true_t0():
    for world in all_worlds():
        b = regime_b_view(world)
        c = regime_c_view(world)
        assert b.observed_t0 == world.event_trace.observed_t0
        assert c.observed_t0 == world.event_trace.observed_t0
        assert b.observed_t0 != world.true_t0  # observed_t0 is always truncated
        assert c.observed_t0 != world.true_t0


def test_b_c_equivalence_holds_for_every_case():
    for world in all_worlds():
        verify_b_c_equivalence(world)  # raises AssertionError on failure


def test_c_never_receives_the_causal_consumption_event_even_in_f10_6():
    world = next(w for w in all_worlds() if w.case_id == "F10-6")
    assert world.event_trace.causal_consumption_event is not None  # B's world-level source has it
    c = regime_c_view(world)
    assert c.event_trace.causal_consumption_event is None


def test_only_f10_6_gives_b_a_causal_consumption_event():
    for world in all_worlds():
        b = regime_b_view(world)
        if world.case_id == "F10-6":
            assert b.event_trace.causal_consumption_event is not None
        else:
            assert b.event_trace.causal_consumption_event is None


def test_c_binding_references_only_identifiers_present_in_b_history():
    for world in all_worlds():
        b = regime_b_view(world)
        c = regime_c_view(world)
        policy_ids = {p.version_id for p in b.policy_history}
        authority_ids = {a.agent_id for a in b.authority_history}
        model_ids = {m.version_id for m in b.model_history}
        assert c.binding.policy_ref["version_id"] in policy_ids
        assert c.binding.authority_ref["agent_id"] in authority_ids
        assert c.binding.model_ref["version_id"] in model_ids
