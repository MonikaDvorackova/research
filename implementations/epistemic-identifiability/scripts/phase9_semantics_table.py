"""Tabulate the Phase 9 development semantics run with null-status and physical-change flags (cluster = environment instance)."""
import json, sys, collections
import numpy as np
from eid.phase9_audit import cp_upper
rows = [json.loads(l) for l in open(sys.argv[1] + "/runs.jsonl")]
procs = [("E_ctx", "N_ctx"), ("E_ep", "N_ep"), ("E_comp_forget", "N_comp_forget"), ("E_comp_ord2", "N_comp_ord2")]
sc = list(dict.fromkeys(r["scenario"] for r in rows))
rng = np.random.default_rng(99)
L = ["| scenario | physical mechanism changed | procedure | formal null true | rejections / runs | instances with ≥1 rejection | cell category | observed |", "|---|---|---|---|---|---|---|---|"]
for s in sc:
    R = [r for r in rows if r["scenario"] == s]
    for pk, nk in procs:
        k = sum(r[pk] is not None for r in R); n = len(R)
        inst = collections.defaultdict(list)
        for r in R: inst[r["inst"]].append(r[pk] is not None)
        ni = sum(any(v) for v in inst.values())
        phys, null = R[0]["phys"], R[0][nk]
        if null and not phys: cls = "null true, mechanism unchanged (type-I cell)"
        elif null and phys: cls = "mechanism changed but formal null still true (no rejection expected)"
        elif not null and not phys: cls = "null false, mechanism unchanged (misspecification; rejection risks false attribution)"
        else: cls = "null false and mechanism changed (power cell)"
        L.append(f"| {s} | {'yes' if phys else 'no'} | {pk} | {'yes' if null else 'no'}{' (approx.)' if 'comp' in pk else ''} | {k}/{n} (UB95 {cp_upper(k, n):.3f}) | {ni}/{len(inst)} | {cls} | {"rejected in some runs" if k else "no rejection"} |")
tm = collections.defaultdict(float)
for r in rows:
    for t in ("t_ctx", "t_ep", "t_comp"): tm[t] += r[t]
L.append(f"\nCost (summed seconds over {len(rows)} runs): " + ", ".join(f"{k}: {v:.0f}" for k, v in tm.items()))
open(sys.argv[1] + "/semantics_table.md", "w").write("\n".join(L) + "\n"); print("\n".join(L))
