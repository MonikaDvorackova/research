"""Phase 8 lightweight diagnostics (EXPLORATORY; not preregistered).  python scripts/phase8_diagnostics.py results/phase8
Deterministic: all random streams are SeedSequence-keyed integers."""
import sys, os, json
import numpy as np
from eid.phase8 import *
from eid.pomdp import make_e0, perturb_action2, with_emission_noise
from eid import x1

out_dir = sys.argv[1]; os.makedirs(out_dir, exist_ok=True)
L = []
def w(s=""): print(s); L.append(s)
def rng(*key): return np.random.default_rng(np.random.SeedSequence(list(key)))
N, T, R = 3000, 4, 100
wide = lambda e: 1 / 3
narrow = lambda e: 0.02
shift_pol = lambda e: 0.02 if e < 1500 else 1 / 3

# ---- D2: stationarity e-process on scenarios
mk = markov_env(1); mk2 = change_action2(mk, 1)
hid = make_e0(1); hid2 = perturb_action2(hid, 1.0)
scen = {
 "S0 Markov, stationary, wide (epistemic only)":        ((mk, mk), None, wide),
 "S1 Markov, stationary, policy shift narrow->wide (C)": ((mk, mk), None, shift_pol),
 "S2 Markov, kernel change at ep 1500, wide (D)":        ((mk, mk2), 1500, wide),
 "S3 Markov, kernel change at ep 1500, narrow (D, low coverage)": ((mk, mk2), 1500, narrow),
 "S4 hidden-state POMDP, stationary, wide (B: order-1 class misspecified)": ((hid, hid), None, wide),
 "S5 hidden-state POMDP, stationary, policy shift (B+C)": ((hid, hid), None, shift_pol),
 "S6 hidden-state POMDP, kernel change at ep 1500, wide (B+D)": ((hid, hid2), 1500, wide),
}
w("## D2 Stationarity e-process (changepoint mixture / stationary-MLE), alpha = 0.05, N = 3000 episodes x 4 steps, R = 100 streams per scenario\n")
w("| scenario | rejection within N | median rejection episode among rejected | rejections before episode 1500 |\n|---|---|---|---|")
for i, (name, (envs, ch, pol)) in enumerate(scen.items()):
    rej = []
    for r in range(R):
        ctx, obs = simulate_stream(envs, ch, pol, N, T, rng(8, i, r))
        _, e = stationarity_etest(ctx, obs)
        rej.append(e)
    rr = [e for e in rej if e]
    pre = sum(1 for e in rr if e <= 1500)
    w(f"| {name} | {len(rr)}/{R} | {np.median(rr) if rr else '–'} | {pre} |")

# ---- D4a: frozen learned null under pure policy shift (kernel unchanged)
w("\n## D4a Frozen learned null (count model trained once on a narrow policy, p(action 2) = 0.02) tested on a WIDE-policy stream from the SAME Markov kernel (no change of mechanism)\n")
w("| training episodes | false-alarm rate within N = 3000 | median rejection episode |\n|---|---|---|")
for ntr in (100, 1000, 10000, 100000):
    rej = []
    for r in range(R):
        ctx_tr, obs_tr = simulate_stream((mk, mk), None, narrow, ntr, T, rng(9, ntr, r, 0))
        ctx, obs = simulate_stream((mk, mk), None, wide, N, T, rng(9, ntr, r, 1))
        rej.append(frozen_null_etest(ctx_tr, obs_tr, ctx, obs)[1])
    rr = [e for e in rej if e]
    w(f"| {ntr} | {len(rr)}/{R} | {np.median(rr) if rr else '–'} |")
w("\nFor comparison the stationarity e-process on the same wide stream (S0 above) has the rejection rate shown there.\n")

# ---- D3: learning curves, plateau, comparator
w("## D3 Learning curves of Dirichlet(1/2) count learners (uniform actions, T = 4); excess held-out log-loss in nats per episode, mean over R = 40 training sets (+- s.e.)\n")
ns = (10, 30, 100, 300, 1000, 3000, 10000)
for name, p in (("Markov truth", mk), ("hidden-state truth E0", hid)):
    H1, d1, _ = learner_limit_and_entropy(p, 1)
    H2, d2, _ = learner_limit_and_entropy(p, 2)
    w(f"**{name}**: entropy of the truth H = {H1:.4f}; exact misspecification plateau of the best order-1 kernel d1 = {d1:.2e}, of the best order-2 kernel d2 = {d2:.2e}\n")
    c1 = learning_curve(p, 1, ns, 40, rng(10, 1)); c2 = learning_curve(p, 2, ns, 40, rng(10, 2))
    w("| n | order-1 excess loss | order-2 excess loss | comparator gap L1 − L2 |\n|---|---|---|---|")
    for n in ns:
        w(f"| {n} | {c1[n][0]:.2e} ± {c1[n][1]:.1e} | {c2[n][0]:.2e} ± {c2[n][1]:.1e} | {c1[n][0]-c2[n][0]:+.2e} |")
    w("")
# ---- D4b: approximate maximiser in the denominator (X1 machinery)
w("## D4b Approximate maximiser: truth = member n10 of the true class; denominator maximises over a coarse subset (n10 omitted) while the numerator mixture contains the full class\n")
e0, M, W = x1.build_class(1)
Mfull = M; Mcoarse = [m for m in M if m[0] in ("E0", "n20")]
Wfull = W + [(9, m) for nme, m in M]                              # alternative mixture also contains all class members
w("| denominator | rejection within 3000 episodes (R = 40, random wide policy) |\n|---|---|")
for lab, Mx in (("exact maximiser over the true class (valid)", Mfull), ("coarse maximiser, true member missed", Mcoarse)):
    k = 0
    for r in range(40):
        env = x1.Sampler(dict(M)["n10"], rng(11, r, 0)); res = x1.run(env, Mx, Wfull, "P2", 3000, 4, rng(11, r, 1))
        k += res["reject_episode"] <= 3000
    w(f"| {lab} | {k}/40 |")
open(os.path.join(out_dir, "diagnostics.md"), "w").write("\n".join(L) + "\n")
