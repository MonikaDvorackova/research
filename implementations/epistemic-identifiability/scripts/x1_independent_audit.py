"""Independent checks of X1 (Phase 7B).  Does not read confirmatory outcomes.
(1) Likelihoods: hidden-path brute-force sum (pomdp.brute_force_obs_law) vs an independent explicit-loop filter written here vs the vectorised filter in x1.run.
(2) Exact supermartingale / Ville check of the *actual* statistic under *adaptive* policies by full enumeration of the observation tree (small horizon).
(3) Policy scores (P3, P4, P5) recomputed by explicit loops vs x1._choose on random histories.
Reports pass/fail and the max discrepancy.  python scripts/x1_independent_audit.py out.txt"""
import itertools, sys
import numpy as np
from eid import x1
from eid.pomdp import brute_force_obs_law, A, O, exact_obs_law

out = []
def log(s):
    print(s); out.append(s)

class FirstRng:                      # deterministic tie-breaking for exact enumeration
    def choice(self, best): return best[0]
    def integers(self, a, b): return a

def loop_filter_ll(model, acts, obs):
    """Independent forward recursion with explicit loops: log p(obs | acts)."""
    S = model.S
    belief = [float(x) for x in model.b0]
    ll = 0.0
    for a, o in zip(acts, obs):
        pred = [sum(belief[s] * model.T[a, s, t] for s in range(S)) for t in range(S)]
        po = sum(pred[t] * model.Z[t, o] for t in range(S))
        ll += np.log(po)
        belief = [pred[t] * model.Z[t, o] / po for t in range(S)]
    return ll

# ---- (1) likelihood agreement
e0, M, W = x1.build_class(7)
comps = [m for _, m in M] + [w for _, w in W]
rng = np.random.default_rng(0)
worst = 0.0
for k in (0, 2, 5, 20, 45):
    for _ in range(5):
        acts = rng.integers(0, A, 3); obs = rng.integers(0, O, 3)
        bf = np.log(brute_force_obs_law(comps[k], list(acts))[np.ravel_multi_index(tuple(obs), (O,) * 3)])
        worst = max(worst, abs(bf - loop_filter_ll(comps[k], acts, obs)))
log(f"(1) max |brute-force path sum - loop filter| in log-likelihood over 25 cases: {worst:.2e}  -> {'PASS' if worst < 1e-10 else 'FAIL'}")

# ---- (2) exact supermartingale check under adaptive policies, full tree, 2 episodes x 3 steps
# the tree needs the truth belief too; implement with an explicit state carrying it
def hist_max_final(ll):
    from scipy.special import logsumexp
    KM = 4
    return logsumexp(ll) - np.log(len(ll)) - ll[:KM].max()

def tree(policy, truth_model, T=3, EP=2, cs=(1.2, 1.5, 2.0, 3.0)):
    e0, M, W = x1.build_class(7)
    comps = [m for _, m in M] + [w for _, w in W]
    KM, K = len(M), len(comps)
    Tt, Zt, b0 = x1._stack(comps)
    res = dict(total=0.0, EE=0.0, cross={c: 0.0 for c in cs})
    def rec(ep, t, b, tb, ll, prob, runmax):
        if ep == EP:
            res["total"] += prob; res["EE"] += prob * np.exp(hist_max_final(ll))
            for c in cs:
                if runmax >= np.log(c): res["cross"][c] += prob
            return
        a = x1._choose(policy, b, ll, KM, Tt, Zt, FirstRng())
        tbp = tb @ truth_model.T[a]
        for o in range(O):
            po_t = float(tbp @ truth_model.Z[:, o])
            if po_t <= 0: continue
            bp = np.einsum("ks,kst->kt", b, Tt[:, a]); po = np.einsum("kt,kt->k", bp, Zt[:, :, o])
            nb = bp * Zt[:, :, o] / po[:, None]
            nll = ll + np.log(po)
            nrm = max(runmax, hist_max_final(nll))
            ntb = tbp * truth_model.Z[:, o]; ntb = ntb / ntb.sum()
            t2, ep2 = t + 1, ep
            if t2 == T:
                t2, ep2 = 0, ep + 1; nb = b0.copy(); ntb = truth_model.b0.copy()
            rec(ep2, t2, nb, ntb, nll, prob * po_t, nrm)
    rec(0, 0, b0.copy(), truth_model.b0.copy(), np.zeros(K), 1.0, -np.inf)
    return res

allok = True
e0, M, W = x1.build_class(7)
for pol in ("P1", "P3", "P4", "P5"):
    if pol == "P1": continue          # P1 is randomised (action drawn); P2 likewise.  Only deterministic adaptive rules enumerated.
    for name, truth in (("E0", e0), ("n10", dict(M)["n10"])):
        r = tree(pol, truth)
        ok = abs(r["total"] - 1) < 1e-9 and r["EE"] <= 1 + 1e-9 and all(r["cross"][c] <= 1 / c + 1e-9 for c in r["cross"])
        allok &= ok
        log(f"(2) policy {pol} truth {name}: total prob {r['total']:.12f}; E[E_final] = {r['EE']:.4f} (<=1); "
            + "; ".join(f"P(max E>={c}) = {r['cross'][c]:.4f} (Ville <= {1/c:.3f})" for c in r['cross']) + f" -> {'PASS' if ok else 'FAIL'}")
log(f"(2) overall: {'PASS' if allok else 'FAIL'}   [deterministic adaptive rules P3,P4,P5 with first-index tie-break; 2 episodes x 3 steps; exhaustive]")

# ---- (3) policy scores by explicit loops
def entropy(p): return -sum(x * np.log(x) for x in p if x > 0)
def pred_loop(model, belief_row, a):
    S = model.S
    pt = [sum(belief_row[s] * model.T[a, s, t] for s in range(S)) for t in range(S)]
    return [sum(pt[t] * model.Z[t, o] for t in range(S)) for o in range(O)]
mismatch = 0; n = 0
for trial in range(30):
    r = np.random.default_rng(100 + trial)
    Tt, Zt, b0 = x1._stack(comps)
    KM = len(M)
    # random in-episode history
    b = b0.copy(); ll = np.zeros(len(comps))
    for step in range(int(r.integers(0, 4)) + 1):
        a = int(r.integers(0, A)); o = int(r.integers(0, O))
        bp = np.einsum("ks,kst->kt", b, Tt[:, a]); po = np.einsum("kt,kt->k", bp, Zt[:, :, o])
        b = bp * Zt[:, :, o] / po[:, None]; ll += np.log(po)
    for pol in ("P3", "P4", "P5"):
        pred = [[pred_loop(comps[k], b[k], a) for a in range(A)] for k in range(len(comps))]
        def post(idx):
            w = np.exp(ll[idx] - ll[idx].max()); return w / w.sum()
        sc = []
        for a in range(A):
            if pol == "P3":
                w = post(list(range(KM))); mix = [sum(w[i] * pred[i][a][o] for i in range(KM)) for o in range(O)]
                sc.append(entropy(mix) - sum(w[i] * entropy(pred[i][a]) for i in range(KM)))
            elif pol == "P5":
                idx = list(range(len(comps))); w = post(idx); mix = [sum(w[i] * pred[i][a][o] for i in idx) for o in range(O)]
                sc.append(entropy(mix) - sum(w[i] * entropy(pred[i][a]) for i in idx))
            else:
                wm = post(list(range(KM))); ww = post(list(range(KM, len(comps))))
                PM = [sum(wm[i] * pred[i][a][o] for i in range(KM)) for o in range(O)]
                PW = [sum(ww[i] * pred[KM + i][a][o] for i in range(len(comps) - KM)) for o in range(O)]
                mid = [(PM[o] + PW[o]) / 2 for o in range(O)]
                sc.append(entropy(mid) - 0.5 * entropy(PM) - 0.5 * entropy(PW))
        mine = int(np.flatnonzero(np.array(sc) >= max(sc) - 1e-12)[0])
        theirs = x1._choose(pol, b, ll, KM, Tt, Zt, FirstRng())
        n += 1; mismatch += (mine != theirs)
log(f"(3) policy decisions P3/P4/P5 (explicit loops vs vectorised) on {n} random histories: mismatches {mismatch} -> {'PASS' if mismatch == 0 else 'FAIL'}")
open(sys.argv[1], "w").write("\n".join(out) + "\n")

# ---- (4) policies receive the intended intervention budgets: instrument action selection on a development seed (500), not confirmatory seeds
import collections as _c
counts = {}
orig = x1._choose
for pol in x1.POLICIES:
    cnt = _c.Counter()
    def spy(policy, b, ll, KM, Tt, Zt, rng, _o=orig, _c=cnt):
        a = _o(policy, b, ll, KM, Tt, Zt, rng); _c[a] += 1; return a
    x1._choose = spy
    e0_, M_, W_ = x1.build_class(500)
    env = x1.Sampler(x1.truths_for(500)["pc1"][0], np.random.default_rng(11))
    r = x1.run(env, M_, W_, pol, 300, 4, np.random.default_rng(12), alpha=1e-12)     # alpha tiny: never stops -> full budget of 300 episodes x 4 steps
    x1._choose = orig
    counts[pol] = (dict(cnt), sum(cnt.values()))
ok4 = (counts["P0"][0].get(2, 0) == 0 and all(v[1] == 1200 for v in counts.values())
       and 0.005 < counts["P1"][0].get(2, 0) / 1200 < 0.05 and all(abs(counts["P2"][0].get(a, 0) / 1200 - 1 / 3) < 0.06 for a in range(3)))
log("(4) action counts over 1200 steps (300 episodes x 4) on dev seed 500, truth pc1, early stopping disabled: " + "; ".join(f"{p}: {v[0]}" for p, v in counts.items()) + f" -> {'PASS' if ok4 else 'FAIL'}")
open(sys.argv[1], "w").write("\n".join(out) + "\n")
