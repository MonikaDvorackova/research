"""Phase 10 DEVELOPMENT: why did the predictive-comparison procedure have zero detections?  Worst-case Hoeffding boundary (Phase 9) versus the
predictable-conditional-range boundary (Phase 10), same scenarios and comparators.  python scripts/phase10_comp.py results/phase10_dev"""
import sys, os, json
from concurrent.futures import ProcessPoolExecutor
import numpy as np
sys.path.insert(0, "scripts")
import eid.e6gen as e6gen
e6gen.NS_DEV = 10000
import phase9_dev_semantics as P9
from eid.e6gen import simulate_stream_probs, simulate_regime_stream
from eid.e6proc import comp_cs_test, comp_cs_test_adaptive, prequential_probs, brier, conditional_range
from eid.phase8 import NCTX, _contexts
from eid.pomdp import A, O

def one(args):
    si, idx, rep = args
    name, build, flags = P9.SC[si]
    rng = np.random.default_rng(np.random.SeedSequence([10000, 55, si, idx, rep]))
    envs, ch, probs, regime = build(idx)
    if regime is not None:
        pair, eps = regime; ctx, obs, _ = simulate_regime_stream(pair, eps, P9.N, P9.T, 1 / 3, rng)
    else:
        ctx, obs = simulate_stream_probs(envs, ch, probs, P9.N, P9.T, rng)
    c, y = ctx.ravel(), obs.ravel()
    p1 = prequential_probs(c, y, NCTX, O); pf = prequential_probs(c, y, NCTX, O, gamma=0.99)
    c2 = _contexts(ctx % A, obs, 2).ravel(); p2 = prequential_probs(c2, y, (O + 1) ** 2 * A, O)
    d = brier(p1, y) - brier(pf, y)
    return dict(scenario=name, inst=idx, rep=rep, flags=flags,
                hoeff_forget=comp_cs_test(p1, pf, y), hoeff_ord2=comp_cs_test(p1, p2, y),
                adapt_forget=comp_cs_test_adaptive(p1, pf, y), adapt_ord2=comp_cs_test_adaptive(p1, p2, y),
                mean_range_forget=float(conditional_range(p1, pf).mean()), sd_delta_forget=float(d.std()), mean_delta_forget=float(d.mean()))

if __name__ == "__main__":
    out = sys.argv[1]
    with ProcessPoolExecutor(11) as ex: res = list(ex.map(one, [(si, i, r) for si in range(len(P9.SC)) for i in range(10) for r in range(3)], chunksize=3))
    L = ["## C. Predictive-comparison procedures: worst-case Hoeffding boundary (rho = 2000, sigma = 2) vs predictable-range boundary; 10 instances x 3 runs per scenario, N = 3000 episodes\n",
         "| scenario | physical mechanism changed | Hoeffding / forgetting | adaptive / forgetting | Hoeffding / order-2 | adaptive / order-2 | mean conditional range R | sd of Brier difference | formal null (forgetting) approx. |\n|---|---|---|---|---|---|---|---|---|"]
    for name in dict.fromkeys(r["scenario"] for r in res):
        R = [r for r in res if r["scenario"] == name]; f = R[0]["flags"]; k = lambda key: sum(r[key] is not None for r in R)
        L.append(f"| {name} | {'yes' if f['phys'] else 'no'} | {k('hoeff_forget')}/30 | {k('adapt_forget')}/30 | {k('hoeff_ord2')}/30 | {k('adapt_ord2')}/30 | "
                 f"{np.mean([r['mean_range_forget'] for r in R]):.3f} | {np.mean([r['sd_delta_forget'] for r in R]):.3f} | {'true' if f['N_comp_forget'] else 'false'} |")
    open(os.path.join(out, "comp_adaptive.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
    with open(os.path.join(out, "comp_runs.jsonl"), "w") as fh:
        for r in res: fh.write(json.dumps(r) + "\n")
