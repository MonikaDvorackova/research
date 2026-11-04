"""Budget-limited vs fundamental: exact-Bayes adaptive oracle, claim rate / median max posterior vs number of 8-step blocks.
Also: oracle WITHOUT the degenerate hypotheses (original grid) on the eqC source (hypothesis-class dependence)."""
import json, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.gwb import gen, epi, epi_agents as ea, agents

res = {}; N = 150; BL = (6, 12, 24)
with epi.EpiGrid():
    for i, c in enumerate(("id", "idnoisy", "approx", "eqA", "eqC", "eqD", "ooc_osc")):
        inst = epi.sample_epi(N, c, 13000 + 10 * i)
        g = torch.Generator().manual_seed(13000 + 10 * i + 7); gor = torch.Generator().manual_seed(1)
        res[c] = {}
        Lmax = 8 * max(BL); eps = torch.randn(N, Lmax, generator=g, dtype=torch.float64); u0 = ea.passive_block(N, g)
        u, y = ea.run_seq(inst, ea.oracle_chooser(gor), u0, eps, L=Lmax)
        for b in BL:
            T = 8 * b
            o = ea.oracle_outputs(inst, u[:, :T], y[:, :T]); p = o["post"]
            row = dict(median_max_post=float(np.median(p.max(1))), claim_rate_0p9=float((p.max(1) >= 0.9).mean()))
            if c in ("id", "idnoisy", "approx"):
                row["acc"] = float((p.argmax(1) == inst["cls"].numpy()).mean())
            res[c][f"blocks{b}"] = row
        print(c, res[c], flush=True)
# oracle whose grid lacks the degenerate members, on eqC (queried at 6 blocks)
inst = epi.sample_epi(N, "eqC", 13100); g = torch.Generator().manual_seed(13107); gor = torch.Generator().manual_seed(1)
eps = torch.randn(N, 48, generator=g, dtype=torch.float64); u0 = ea.passive_block(N, g)
saved = {k: list(v) for k, v in gen.HGRID.items()}
gen.HGRID[1] = [h for h in gen.HGRID[1] if h not in ((3, 0.0), (4, 0.05))]; gen.HGRID[1]  # original grid
try:
    from eid.gwb import epi as E
    old = E.HGRID_EPI[1]; E.HGRID_EPI[1] = list(gen.HGRID[1])
    u, y = ea.run_seq(inst, ea.oracle_chooser(gor), u0, eps)
    o = ea.oracle_outputs(inst, u, y)
    res["eqC_oracle_without_degenerate_members"] = dict(claim_rate_0p9=float((o["post"].max(1) >= 0.9).mean()),
        median_max_post=float(np.median(o["post"].max(1))), persistent_frac=float((o["dmax"] < ea.DELTA_PERSIST).mean()))
    E.HGRID_EPI[1] = old
finally:
    gen.HGRID.clear(); gen.HGRID.update(saved)
print(res["eqC_oracle_without_degenerate_members"])
json.dump(res, open("results/epi_final/budget_curve.json", "w"), indent=1)
