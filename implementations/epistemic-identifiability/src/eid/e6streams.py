"""Phase 10: named, independent random streams and a structure registry for E6' development runs.
Streams are spawned from SeedSequence([namespace, family, index, rep]) so that environment generation, training, intervention selection, evaluation
and Monte-Carlo replication never share a generator."""
from __future__ import annotations

import json

import numpy as np

NS10 = 10000                       # Phase 10 development namespace (disjoint from 200, 300-311, 400-405, 500-505, 600-629, 700-719, 800-829, 9000)
NAMES = ("env", "train", "intervene", "eval", "mc")
FAMILY_ID = {"markov": 1, "hmm": 2, "controlled": 3, "regime": 4, "changing": 5, "hmm_small": 6}


def streams(family: str, idx: int, rep: int = 0, ns: int = NS10) -> dict:
    kids = np.random.SeedSequence([ns, FAMILY_ID[family], idx, rep]).spawn(len(NAMES))
    return {n: np.random.default_rng(k) for n, k in zip(NAMES, kids)}


def registry_row(family: str, idx: int, params: dict, **tags) -> dict:
    """One registry line: family, index, structural parameters, plus tags (training coverage, reset semantics, model class, budget...)."""
    return dict(namespace=NS10, family=family, index=idx, params={k: (float(v) if isinstance(v, (int, float, np.floating)) else v) for k, v in params.items()}, **tags)


def dump_registry(rows, path):
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
