import json, sys, numpy as np
r = json.load(open(sys.argv[1]))
ms = lambda v: f"{np.mean(v):.3f}±{np.std(v):.3f}" if len(v) > 1 else f"{v[0]:.3f}"
print("PREDICTIVE excess NLL | rollout16 RMSE/sigma | cover90  (mean±sd over training seeds)")
for g, lst in r["predictive"].items():
    for k in ("uniform", "sweep"):
        print(f"  {g:14s} {k:8s} {ms([p[k]['excess_nll'] for p in lst])} | {ms([p[k]['rollout16_rmse_over_sigma'] for p in lst])} | {ms([p[k]['cover90'] for p in lst])}")
rows = {}
for cond, gs in r["structural"].items():
    print(f"\n== {cond}: ID acc | hoparam | hosigma | ECE(id) | claim eqA/eqB plain | claim eqA/eqB withEA")
    for g, lst in gs.items():
        P = lambda v, k, m: [s[v][k][m] for s in lst]
        print(f"  {g:14s} {ms(P('plain','id','acc'))} | {ms(P('plain','hoparam','acc'))} | {ms(P('plain','hosigma','acc'))} | {ms(P('plain','id','ece'))} | {ms(P('plain','eqA','claim_rate'))}/{ms(P('plain','eqB','claim_rate'))} | {ms(P('withEA','eqA','claim_rate'))}/{ms(P('withEA','eqB','claim_rate'))}")
    b = r["baselines"][cond]
    for k in ("oracle_bayes", "oracle_matched_prior", "handfeat_gbm", "supervised_gru"):
        if k in b:
            x = b[k]; s = f"  {k:20s} {x['id']['acc']:.3f} | {x['hoparam']['acc']:.3f} | {x['hosigma']['acc']:.3f}"
            if "eqA" in x: s += f" | ece {x['id']['ece']:.3f} | claim {x['eqA']['claim_rate']:.2f}/{x['eqB']['claim_rate']:.2f}"
            print(s)
    print("  leak actions-only acc", round(b["leak_actions_only_acc"], 3), "  oracle id CI", [round(v, 3) for v in b["oracle_bayes"]["id"]["acc_ci"]])
