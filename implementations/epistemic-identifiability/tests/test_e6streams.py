import numpy as np
from eid import e6gen
from eid.e6streams import NAMES, NS10, dump_registry, registry_row, streams


def test_streams_are_deterministic_distinct_and_namespaced():
    a, b = streams("markov", 3, 1), streams("markov", 3, 1)
    assert all(a[n].random() == b[n].random() for n in NAMES)
    c = streams("markov", 3, 1)
    draws = [c[n].random() for n in NAMES]
    assert len(set(draws)) == len(NAMES)                                      # five independent generators
    assert NS10 == 10000 and NS10 not in set(range(200, 830)) | {9000}


def test_small_hmm_generator_and_registry(tmp_path):
    p, d = e6gen.gen_hmm_small(2)
    assert d["S"] in (2, 3)
    row = registry_row("hmm_small", 2, d, train_coverage="uniform", reset="state+regime", model_class="IO-HMM(S)")
    dump_registry([row], tmp_path / "r.jsonl")
    assert "reset" in (tmp_path / "r.jsonl").read_text()
