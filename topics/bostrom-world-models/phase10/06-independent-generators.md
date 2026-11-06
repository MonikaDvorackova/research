---
id: topic-bostrom-world-models-phase10-generators
title: "Independent environment generators, stream separation and the structure registry"
topic: bostrom-world-models
type: note
status: active
created: 2026-11-04
tags: [generators, registry, reproducibility]
---

# Generators and registry (Phase 10)
Code: `src/eid/e6gen.py` (extended with `gen_hmm_small`), `src/eid/e6streams.py`; tests `tests/test_e6gen.py`, `tests/test_e6streams.py`. Namespace **10000** (`NS10`), disjoint from 200, 300–311, 400–405, 500–505, 600–629, 700–719, 800–829 and 9000.
| Family | Sampled per structure | Used in Phase 10 development |
|---|---|---|
| `markov` (fully observed, S = O = 3) | Dirichlet concentration c ∈ [0.2, 3] log-uniform; random b₀ | **60 structures**: certified procedure (coverage, type-I, power, adversary) |
| `hmm` (S = 3…6) | S, c_T, c_Z, b₀ | predictive-comparison scenarios (10 structures per scenario) |
| `hmm_small` (S ∈ {2, 3}) | S, c_T, c_Z, b₀ | **40 structures**: EM study |
| `controlled` (revealing action) | partner-state map, designated action | generator exists; not exercised in Phase 10 |
| `regime` (two kernels, persistent flips ε ∈ [10⁻³, 0.2]) | both kernels, ε | scenario R1 of the comparison study |
| `changing` (one action's rows redrawn) | changed action, new rows | scenarios M3/H3 |
| `equivalent_pair` (bisimilar split) | state split | negative control (TV = 0, Phase 9) |
**Diversity.** Independent `hmm` draws: mean pairwise KL 0.63 nats vs 0.013 for the jittered copies of the hand-built POMDP of Phase 7 (≈ 50×). Interface limits (stated): A = O = 3, T = 4; Markov contexts (previous observation, action).
**Independent random streams** (`streams(family, idx, rep)`): five generators spawned from SeedSequence([10000, family, idx, rep]): `env` (observations/outcome draws), `train` (training data), `intervene` (adversarial/exploratory action choices), `eval` (test streams), `mc` (Monte-Carlo replication). Structure generation uses a separate key (`e6gen._rng`). No stream is shared across roles; a unit test checks five distinct generators and determinism.
**Registry** (`registry_markov.jsonl`, `registry_hmm_small.jsonl`): family, index, structural parameters (S, concentrations), training coverage, reset semantics ("state; observed-state Markov" / "state; episodic"), model class, namespace. What is recorded vs not: the registry records the *experimenter's* generative parameters; the observer's inputs are only action–observation streams (`test_procedures_receive_only_data_arrays_no_environment_objects`). Hidden-state persistence and reset semantics are tags (`regime`: ε; episodic resets for `hmm_small`).
**Not independent in a stronger sense:** all families share the same alphabet sizes and episode length; two structures with the same family differ by random tensors, not by qualitative design. Generality beyond A = O = 3, T = 4 and to learned neural world models is untested.
