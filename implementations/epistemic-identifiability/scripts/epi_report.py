import json, sys, numpy as np
r = json.load(open(sys.argv[1]))
cats = ["id", "idnoisy", "approx", "eqA", "eqB", "eqC", "eqD", "ooc_sat", "ooc_osc", "ooc_qd"]
print("claim rate at 70% identifiable-calibration coverage (lower is better on eq*/ooc*); acc among claimed on id")
print(f"{'method':28s} " + " ".join(f"{c[:8]:>8s}" for c in cats) + "  accClm  AUROC all/unseenEQ")
for k, m in r["methods"].items():
    print(f"{k:28s} " + " ".join(f"{m[c]['claim_rate']:8.2f}" for c in cats) + f"  {m['id']['acc_among_claimed'] if m['id']['acc_among_claimed'] is not None else float('nan'):.2f}   {m['auroc_justified_vs_unjustified']:.2f}/{m['auroc_justified_vs_unseen_eq']:.2f}")
print("\nreasons among abstentions: persistent-flag fraction | gof-flag rate")
for k, m in r["methods"].items():
    if "reasons" in m:
        print(f"{k:28s} " + " ".join(f"{(m['reasons'][c]['persistent_frac'] if m['reasons'][c]['persistent_frac'] is not None else float('nan')):4.2f}|{m['reasons'][c]['gof_flag_rate_all']:4.2f}" for c in cats))
print("\nconformal singleton-rate by alpha (id coverage_true):")
for al, rows in r["M4_conformal"].items():
    print(al, "cov", round(rows["id"]["coverage_true"], 3), " ".join(f"{c[:6]}:{rows[c]['singleton_rate']:.2f}" for c in cats))

print("\npersistence AUROC (unseen-eq abstentions vs id abstentions; 0.5 = no information):")
for k, m in r["methods"].items():
    if "persist_auroc_unseenEq_vs_id" in m: print(f"  {k:28s} {m['persist_auroc_unseenEq_vs_id']}  n={m['persist_n']}")
