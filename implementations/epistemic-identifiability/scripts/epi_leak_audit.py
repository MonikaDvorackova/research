"""Leakage audit: can nuisance statistics of the common passive first block (noise level, mean, variance, range of y;
also episode length / action range, which are constant by construction) predict the epistemic category WITHIN a family?"""
import json, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_auc_score
from eid.gwb import epi, epi_agents as ea, gen

cats = ["id", "eqA", "eqB", "eqC", "eqD", "approx", "ooc_sat", "ooc_osc", "ooc_qd"]
rows = []; N = 500
for i, c in enumerate(cats):
    inst = epi.sample_epi(N, c, 12000 + 10 * i)                       # audit namespace 12000+ (never used for models)
    g = torch.Generator().manual_seed(12000 + 10 * i + 7)
    eps = torch.randn(N, 48, generator=g, dtype=torch.float64); u0 = ea.passive_block(N, g)
    u = torch.zeros(N, 48, dtype=torch.float64); u[:, :8] = u0
    y = (epi.x_of(inst, u) + inst["sigma"][:, None] * eps)[:, :8].numpy()
    dy = np.diff(y, axis=1)
    f = np.stack([dy.std(1), y.mean(1), y.std(1), np.abs(y).max(1), np.full(N, 48.0), np.full(N, 1.0)], 1)
    rows.append((c, f, inst["fam"].numpy()))
out = {}
for fam in (0, 1):
    X, Y = [], []
    for c, f, fm in rows:
        sel = fm == fam
        if sel.sum() > 30: X.append(f[sel]); Y.append(np.full(sel.sum(), int(c in ("eqA", "eqB", "eqC", "eqD"))))
    X = np.concatenate(X); Y = np.concatenate(Y)
    p = cross_val_predict(HistGradientBoostingClassifier(max_iter=100, random_state=0), X, Y, cv=5, method="predict_proba")[:, 1]
    out[f"family{'AB'[fam]}"] = dict(auroc_eq_vs_id_from_nuisance=float(roc_auc_score(Y, p)), n=int(len(Y)), eq_fraction=float(Y.mean()))
out["note"] = "AUROC near 0.5 => passive-block nuisance statistics do not reveal equivalence status within a family; episode length and action range are constant by construction"
json.dump(out, open("results/epi_final/leak_audit.json", "w"), indent=1); print(json.dumps(out, indent=1))
