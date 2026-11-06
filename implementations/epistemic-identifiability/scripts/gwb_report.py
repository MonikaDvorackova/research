import json, sys, numpy as np
r = json.load(open(sys.argv[1]))
print("PREDICTIVE (excess one-step NLL over noise floor | rollout16 RMSE/sigma | cover90)")
for g, lst in r["predictive"].items():
    for k in ("uniform", "sweep"):
        print(f"  {g:10s} {k:8s}", " ".join(f"{p[k]['excess_nll']:.3f}/{p[k]['rollout16_rmse_over_sigma']:.2f}/{p[k]['cover90']:.2f}" for p in lst))
for cond, gs in r["structural"].items():
    print(f"\n== {cond}  (acc id / hoparam / hosigma ; ECE id ; EA-probe: eqA claim, eqB claim ; plain eqA, eqB claim)")
    for g, lst in gs.items():
        for i, s in enumerate(lst):
            p, e = s["plain"], s["withEA"]
            print(f"  {g:10s} acc {p['id']['acc']:.3f} {p['hoparam']['acc']:.3f} {p['hosigma']['acc']:.3f} | ece {p['id']['ece']:.3f} | withEA claim {e['eqA']['claim_rate']:.2f} {e['eqB']['claim_rate']:.2f} | plain claim {p['eqA']['claim_rate']:.2f} {p['eqB']['claim_rate']:.2f}")
    b = r["baselines"][cond]
    for k in ("oracle_bayes", "oracle_matched_prior", "handfeat_gbm", "supervised_gru"):
        if k in b:
            x = b[k]
            if "eqA" not in x: print(f"  {k:12s} acc {x['id']['acc']:.3f} {x['hoparam']['acc']:.3f} {x['hosigma']['acc']:.3f}"); continue
            print(f"  {k:12s} acc {x['id']['acc']:.3f} {x['hoparam']['acc']:.3f} {x['hosigma']['acc']:.3f} | ece {x['id']['ece']:.3f} | claim eqA {x['eqA']['claim_rate']:.2f} eqB {x['eqB']['claim_rate']:.2f}")
    print("  leak(actions-only acc)", round(b["leak_actions_only_acc"], 3))
