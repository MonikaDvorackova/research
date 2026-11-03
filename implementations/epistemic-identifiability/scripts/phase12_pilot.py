"""World-models programme pilot (development, exploratory).  python scripts/phase12_pilot.py results/phase12_dev
Namespace SeedSequence([12000, ...]) (disjoint from every earlier/reserved seed)."""
import sys, os, json, time
from concurrent.futures import ProcessPoolExecutor
import numpy as np
from eid import worldgen_pilot as W

SIGMAS = tuple(float(x) for x in os.environ.get("PILOT_SIGMAS", "0.005,0.05,0.2").split(",")); POLS = ("passive", "probe", "active"); NEP, R = 12, 40
TRUTHS = [h for h in range(len(W.HYPS))]
def rng(*k): return np.random.default_rng(np.random.SeedSequence([12000, *k]))

def job(a):
    ti, si, pol, rep = a
    kind, par = W.HYPS[ti]; sigma = SIGMAS[si]; r = rng(1, ti, si, POLS.index(pol), rep)
    b = float(r.uniform(0.7, 1.3))
    env = W.PilotEnv(kind, par, b, sigma, r)
    post, used = W.run_agent(env, b, pol, NEP, r)
    # predictive accuracy on a fresh passive episode: posterior-mean predictor vs the observed y
    us = r.uniform(-2, 2, W.T_EP); env.reset(); y = np.array([env.act(u) for u in us]); mu = W.hyp_means(us[None], b)[0]
    pred = post @ mu
    cls = np.zeros(3); [cls.__setitem__(W.class_of(h), cls[W.class_of(h)] + post[h]) for h in range(len(post))]
    return dict(truth=ti, sigma=sigma, policy=pol, rep=rep, mass=float(post[ti]), cls_mass=float(cls[W.class_of(ti)]), cls_ok=bool(cls.argmax() == W.class_of(ti)),
                hyp_ok=bool(post.argmax() == ti), rmse=float(np.sqrt(np.mean((y - pred) ** 2))), noise=sigma)

def id_map():
    L = ["## P1. Exact identifiability map: per-episode KL (nats) between hypothesis pairs, for the best program in the menu and for a random large-control program (mean of 200)\n",
         "| sigma | pair | best menu program KL | random large-control KL | episodes to reach 3 nats (best) | episodes (random) |\n|---|---|---|---|---|---|"]
    menu = W.program_menu(); r = rng(0); b = 1.0
    mu_m = W.hyp_means(menu, b); rand = np.array([r.uniform(-2, 2, W.T_EP) for _ in range(200)]); mu_r = W.hyp_means(rand, b)
    pairs = {"cont vs quant(0.2)": (0, 2), "cont vs stiff(0.1)": (0, 5), "quant(0.2) vs stiff(0.1) [matched dead zone]": (2, 5)}
    for sg in SIGMAS:
        for name, (i, j) in pairs.items():
            klm = ((mu_m[:, i] - mu_m[:, j]) ** 2).sum(1) / (2 * sg ** 2); klr = ((mu_r[:, i] - mu_r[:, j]) ** 2).sum(1) / (2 * sg ** 2)
            L.append(f"| {sg} | {name} | {klm.max():.3g} | {klr.mean():.3g} | {3/max(klm.max(),1e-12):.2g} | {3/max(klr.mean(),1e-12):.2g} |")
    return L

def mlp_part():
    from sklearn.neural_network import MLPRegressor
    L = ["\n## P3. Prediction-oriented learned world model (MLP one-step predictor, 64-64 tanh), sigma = 0.05; 5 seeds per generator; RMSE in observation units\n",
         "| generator | training data | passive-test RMSE | probe RMSE (x = 0, u in {0.02, 0.05, 0.1}) | probe RMSE of the TRUE noise-free map = 0 | passive RMSE noise floor |\n|---|---|---|---|---|---|"]
    gens = [("cont", 0.0), ("quant", 0.2), ("stiff", 0.1)]
    for kind, par in gens:
        for data in ("passive", "probe+active-style"):
            pr, pb = [], []
            for s in range(5):
                r = rng(3, hash(kind) % 1000, s) if False else rng(3, gens.index((kind, par)), s)
                b = 1.0; env = W.PilotEnv(kind, par, b, 0.05, r)
                X, Y = [], []
                for ep in range(150):
                    if data == "passive": us = r.uniform(-2, 2, W.T_EP)
                    else: us = r.uniform(-1, 1, W.T_EP) * 10 ** r.uniform(-2, 0.3)
                    env.reset(); ys = [0.0] + [env.act(u) for u in us]
                    for t in range(W.T_EP): X.append([ys[t], us[t]]); Y.append(ys[t + 1])
                m = MLPRegressor(hidden_layer_sizes=(64, 64), activation="tanh", max_iter=400, random_state=int(s)).fit(np.array(X), np.array(Y))
                # passive test
                Xt, Yt = [], []
                for ep in range(40):
                    us = r.uniform(-2, 2, W.T_EP); env.reset(); ys = [0.0] + [env.act(u) for u in us]
                    for t in range(W.T_EP): Xt.append([ys[t], us[t]]); Yt.append(ys[t + 1])
                pr.append(np.sqrt(np.mean((m.predict(np.array(Xt)) - np.array(Yt)) ** 2)))
                # probe: true next state from x = 0 with small control is 0 for dead-zone systems, b*dt*u for cont
                for_true = []; Xp = []
                for u in (0.02, 0.05, 0.1):
                    Xp.append([0.0, u]); for_true.append(float(W.step(kind, par, np.array(0.0), u, b)))
                pb.append(np.sqrt(np.mean((m.predict(np.array(Xp)) - np.array(for_true)) ** 2)))
            L.append(f"| {kind}({par}) | {data} | {np.mean(pr):.4f} ± {np.std(pr, ddof=1)/np.sqrt(5):.4f} | {np.mean(pb):.4f} ± {np.std(pb, ddof=1)/np.sqrt(5):.4f} | 0 | 0.05 |")
    return L

if __name__ == "__main__":
    out = sys.argv[1]; t0 = time.time(); L = id_map()
    jobs = [(ti, si, pol, rep) for ti in TRUTHS for si in range(3) for pol in POLS for rep in range(R)]
    with ProcessPoolExecutor(11) as ex: res = list(ex.map(job, jobs, chunksize=20))
    with open(os.path.join(out, "agent_runs.jsonl"), "w") as f:
        for r in res: f.write(json.dumps(r) + "\n")
    L.append(f"\n## P2. Structural hypothesis agents, {NEP} episodes of {W.T_EP} steps, {R} replicate noise/physics draws per cell (no independent structures beyond b ~ U[0.7, 1.3])\n")
    L.append("Entry: posterior mass on the true hypothesis (mean) / correct-class decision rate / exact-hypothesis decision rate.\n")
    L.append("| truth | sigma | passive (large random controls) | random-amplitude probe | active EIG planner |\n|---|---|---|---|---|")
    for ti in TRUTHS:
        for si, sg in enumerate(SIGMAS):
            row = []
            for pol in POLS:
                R_ = [r for r in res if r["truth"] == ti and r["sigma"] == sg and r["policy"] == pol]
                row.append(f"{np.mean([r['mass'] for r in R_]):.2f} / {np.mean([r['cls_ok'] for r in R_]):.2f} / {np.mean([r['hyp_ok'] for r in R_]):.2f}")
            L.append(f"| {W.HYPS[ti][0]}({W.HYPS[ti][1]}) | {sg} | " + " | ".join(row) + " |")
    L.append("\nPredictive accuracy of the posterior-mean predictor on a fresh passive episode relative to the noise floor (RMSE / sigma), mean over truths and replicates:\n")
    L.append("| sigma | passive | probe | active |\n|---|---|---|---|")
    for sg in SIGMAS:
        L.append(f"| {sg} | " + " | ".join(f"{np.mean([r['rmse']/r['noise'] for r in res if r['sigma']==sg and r['policy']==pol]):.3f}" for pol in POLS) + " |")
    if not os.environ.get("PILOT_SKIP_MLP"): L += mlp_part()
    open(os.path.join(out, "pilot_results.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L)); print("wall", round(time.time() - t0))
