import glob, json, os, sys, numpy as np
rows = []
for f in sorted(glob.glob(sys.argv[1] + "/runs/*/result.json")):
    r = json.load(open(f)); a = r["args"]; c = r["curve"]; last = c[-1]
    first = next((x["step"] for x in c if x["G"]["z"] > 4 and x["G"]["frac_predicted"] > 0.1), None)
    first50 = next((x["step"] for x in c if x["G"]["frac_predicted"] > 0.5), None)
    first99 = next((x["step"] for x in c if x["G"]["frac_predicted"] > 0.99), None)
    ex = r["extraction"]
    rows.append(dict(kind=a["kind"], n=a["n"], inst=a["inst"], H=a["H"], z=last["G"]["z"], frac=last["G"]["frac_predicted"], zR=last["cross_R"]["z"],
                     firstdet=first, f50=first50, f99=first99, lin=ex.get("linear", {}).get("exact"), d2=ex.get("deg2", {}).get("exact"),
                     bm=ex.get("BM_bits_needed"), replay=r["replay"]["click_agreement"], secs=r["train_seconds"], acc=last["G"]["acc_click"]))
print(f"{'kind':6s} {'n':>3s} {'i':>2s} {'H':>4s} {'frac':>6s} {'z':>9s} {'zCrossR':>8s} {'step>=50%':>9s} {'>=99%':>6s} {'lin✓':>5s} {'deg2✓':>6s} {'BMbits':>6s} {'replay':>6s}")
for r in rows:
    print(f"{r['kind']:6s} {r['n']:3d} {r['inst']:2d} {r['H']:4d} {r['frac']:6.3f} {r['z']:9.1f} {r['zR']:8.1f} {str(r['f50']):>9s} {str(r['f99']):>6s} {str(r['lin']):>5s} {str(r['d2']):>6s} {str(r['bm']):>6s} {r['replay']:6.3f}")
print("\nvalidity: max cross-environment z over all models (true-random shocks; must be <= ~3):", round(max(r["zR"] for r in rows), 2))
print("rand-control models' own z on random shocks (false-detection check):", [round(r["z"], 2) for r in rows if r["kind"] == "rand"])
