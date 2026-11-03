"""Phase 10 DEVELOPMENT: regret scaling of the price of a broad null (iid categorical change detection with unknown pre-change law).
Null: iid with SOME law on K cells (saturated).  Pre-change law uniform; post-change q tilted so that KL(q||p) = KL0 exactly.  Change at observation n0.
Measures the evidence needed D*KL until the mixture-changepoint e-process crosses 1/alpha.  python scripts/phase10_kscaling.py results/phase10_dev"""
import sys, json, os
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from scipy.optimize import brentq
from eid.e6proc import cp_etest

KL0, N0, ALPHA, PER = 0.1, 4000, 0.05, 20

def tilt(K, kl):
    p = np.full(K, 1.0 / K); s = np.where(np.arange(K) % 2 == 0, 1.0, -1.0)
    f = lambda th: (lambda q: float((q * np.log(q / p)).sum()) - kl)((p * np.exp(th * s)) / (p * np.exp(th * s)).sum())
    th = brentq(f, 1e-6, 20.0)
    q = p * np.exp(th * s); return p, q / q.sum()

def one(args):
    K, rep = args
    p, q = tilt(K, KL0)
    rng = np.random.default_rng(np.random.SeedSequence([10000, 123, K, rep]))
    n_post = 12000
    x = np.concatenate([rng.choice(K, N0, p=p), rng.choice(K, n_post, p=q)])
    c = np.zeros(len(x), int)
    # evaluate at every PER observations; first crossing after the change
    best, rej = cp_etest(c, x, 1, K, PER, ALPHA)
    return dict(K=K, rep=rep, delay=(None if rej is None else rej * PER - N0))

if __name__ == "__main__":
    out = sys.argv[1]
    Ks = [2, 4, 8, 16, 32, 64, 128]
    with ProcessPoolExecutor(11) as ex: res = list(ex.map(one, [(K, r) for K in Ks for r in range(12)], chunksize=3))
    L = ["## K1. Regret scaling of a broad (saturated iid) null: evidence needed to detect a change of fixed size (KL = 0.1 nats/observation), pre-change law unknown\n",
         "| cells K | detected within 12000 post-change obs | median delay (obs) | median delay x KL (nats of evidence) | (K-1)/2 | ratio evidence/((K-1)/2) |\n|---|---|---|---|---|---|"]
    for K in Ks:
        d = [r["delay"] for r in res if r["K"] == K]; det = [x for x in d if x is not None and x > 0]
        med = np.median([x if x is not None and x > 0 else 12000 for x in d]) if d else np.nan
        L.append(f"| {K} | {len(det)}/{len(d)} | {med:.0f} | {med*KL0:.1f} | {(K-1)/2:.1f} | {med*KL0/max((K-1)/2,1e-9):.2f} |")
    # extrapolation to the X1/E_ep setting, using the slope measured on the detected K values (K = 8, 16, 32)
    ev = {K: np.median([r["delay"] for r in res if r["K"] == K and r["delay"] is not None and r["delay"] > 0]) * KL0 for K in (8, 16, 32)}
    slope = np.polyfit(list(ev.keys()), list(ev.values()), 1)[0]
    K_ep, kl_ep = 27 * 80, 1e-2
    L.append(f"\nMeasured slope of evidence needed versus K (detected cases K = 8, 16, 32): {slope:.1f} nats per cell (naive Krichevsky-Trofimov redundancy would be (1/2) ln n per cell, about 4-5 nats).")
    L.append(f"Extrapolation (beyond the measured range, indicative only) to the episode-level saturated model of Phases 7/9 (2160 free cells; change of 0.01 nats/episode): evidence ~ {slope*K_ep:.0f} nats, i.e. about {slope*K_ep/kl_ep:.1e} episodes, versus N = 3000 in the dev run.")
    open(os.path.join(out, "kscaling.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
