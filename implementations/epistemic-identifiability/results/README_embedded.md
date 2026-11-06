# Embedded-observer investigation: computational artifacts

Supports `topics/bostrom-world-models/world-models-programme/{embedded-observer-formal-model,candidate-theorems-and-counterexamples,proof-note-two-state-hidden-phase,originality-and-proof-status}.md`. **These are exact finite computations supporting precise statements; none is a proof, none is a learning experiment, nothing was trained.** Use `~/.venvs/eid/bin/python`.
| script | purpose | output |
|---|---|---|
| `scripts/embedded_reduction_check.py` | exact check of Theorem 1 (joint-chain vs POMDP belief filter, agreement 3.3e-16) and of the shared-noise counterexample (Theorem 2) | `embedded/reduction_check.json` |
| `scripts/embedded_finite_memory_search.py`, `embedded_finite_memory_repeat.py`, `embedded_m2_scaling_search.py` | stochastic optimisation of m-state automata under hidden phase K (reproduces Hellman–Cover at K=1, m=2,3; m>=3 searches are unreliable) | `embedded/finite_memory_search*.json`, `m2_scaling_check.json` |
| `scripts/embedded_m2_exact.py` | exact 4-parameter global search, 24 cells (p, K): sup TV = 2c/K to 2e-15 | `embedded/m2_exact_check.json` |
| `scripts/embedded_m2_identity_check.py` | Lemma 2 identity (1.8e-15) and inequality |R|/(1-sigma) <= 1 on 2e5 random draws | `embedded/m2_identity_check.json` |
| `scripts/embedded_m2_lemma4_check.py` | Lemma 3 closed form (3.9e-16) | `embedded/m2_lemma4_check.json` |
| `scripts/embedded_m2_vertex_check.py` | vertex inequality grid, minimum margin 0, never negative | `embedded/m2_vertex_check.txt` |
| `scripts/embedded_m2_endpoint_proof_check.py` | **failed proof approach, kept as a record**: endpoint bounding fails in the corner b0 ~ 1/4, b1 = 1 (the entry law is pinned near the absorbing state); superseded by the argument in the proof note | `embedded/m2_endpoint_check.json` |
| `scripts/embedded_general_m_identity_check.py` | m-state generalisation of the identity (9e-13) | `embedded/general_m_identity_check.json` |
`MANIFEST_embedded.sha256` lists file hashes.
