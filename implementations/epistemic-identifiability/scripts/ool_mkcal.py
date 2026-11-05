"""Build the calibration thresholds from the calibration-namespace run (valid L0 fits).  usage: ool_mkcal.py in.pkl out.json"""
import sys, pickle, json, numpy as np
d = pickle.load(open(sys.argv[1], "rb")); res = d["res"]; cal = dict(in_={}, oos={}, n={}, per_family={}, q=0.95)
Bs = sorted({B for r in res for B in r["agents"]["L0_falsify"]})
for B in Bs:
    si = [r["agents"]["L0_falsify"][B]["s_in"] for r in res]; so = [r["agents"]["L0_falsify"][B]["s_oos"] for r in res if r["agents"]["L0_falsify"][B]["s_oos"] is not None]
    cal["in_"][B] = float(np.quantile(si, 0.95)); cal["oos"][B] = float(np.quantile(so, 0.95)); cal["n"][B] = (len(si), len(so))
    cal["per_family"][B] = {f: dict(s_in_median=float(np.median([r["agents"]["L0_falsify"][B]["s_in"] for r in res if r["fam"] == f])),
                                    reject_in=float(np.mean([r["agents"]["L0_falsify"][B]["s_in"] > cal["in_"][B] for r in res if r["fam"] == f]))) for f in sorted({r["fam"] for r in res})}
cal["in"] = cal.pop("in_"); json.dump(cal, open(sys.argv[2], "w"), indent=1); print(json.dumps({k: cal[k] for k in ("in", "oos", "n")}))
