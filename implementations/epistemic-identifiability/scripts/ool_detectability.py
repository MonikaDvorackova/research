"""Detectability of every benchmark mechanism: max over the 24-programme pool of ||F_m(u) - F_null(u)|| / sigma (null = coupling removed), 6 instances per family."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from eid.ool import bench
from eid.sdw import env
out = {}
for f in bench.FAM:
    es = []
    for s in range(6):
        inst = bench.make_instance(f, np.random.default_rng(100 + s)); nul = dict(inst, c=0.0)
        es.append(max(float(np.sqrt(((bench.simulate(inst, u)[1] - bench.simulate(nul, u)[1]) ** 2).sum()) / bench.SIG) for u in env.POOL))
    out[f] = dict(min=min(es), median=float(np.median(es)), split=bench.FAM[f]["split"], klass=bench.FAM[f]["klass"])
json.dump(dict(manifest_sha256=bench.MAN_SHA, effect_sigma_units=out), open(sys.argv[1], "w"), indent=1)
