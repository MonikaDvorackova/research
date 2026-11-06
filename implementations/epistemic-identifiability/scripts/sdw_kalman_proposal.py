"""Post-hoc (doc 19 addendum B): proposal recall@3 with a Kalman/RTS-smoother state reconstruction, on the same ns-25000 instances."""
import sys, os, pickle, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np, torch
from eid.sdw import env, agent as A
from sdw_run import load_est
d = pickle.load(open(sys.argv[1], "rb")); est = load_est(); out = {}
for r in sorted(d["res"], key=lambda r: r["k"]):
    if r["fam"] not in A.EXPECT: continue
    inst = r["inst"]; data = A.Data(inst, 25000 + r["k"])
    for pid in env.SWEEP_B[:6]: data.add(pid, env.POOL[pid])
    U, Y = data.arr; X2 = np.stack(data.X2)
    out[r["k"]] = dict(fam=r["fam"], **{w: A.proposal_rank(U, Y, X2, est, w)[:3] for w in ("analytic", "learned", "kalman", "oracle")})
json.dump(out, open(sys.argv[2], "w"))
rec = lambda w, fams: np.mean([any(e in v[w] for e in A.EXPECT[v["fam"]]) for v in out.values() if v["fam"] in fams])
for w in ("oracle", "analytic", "kalman", "learned"): print(w, "known", round(rec(w, env.KNOWN), 3), "unfamiliar", round(rec(w, env.UNFAMILIAR), 3), "all", round(rec(w, env.INLANG), 3))
