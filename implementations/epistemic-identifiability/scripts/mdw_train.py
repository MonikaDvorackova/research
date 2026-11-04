"""Train the meta context world model (kind=wm) or the supervised descriptor regressor (kind=reg) on TRAINING families only."""
import argparse, json, os, sys, time
import torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.mdw import env, model as M

ap = argparse.ArgumentParser()
ap.add_argument("--kind", choices=["wm", "reg"], required=True); ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--steps", type=int, default=2500); ap.add_argument("--batch", type=int, default=32)
ap.add_argument("--threads", type=int, default=3); ap.add_argument("--H", type=int, default=128); ap.add_argument("--ss", type=float, default=0.5); ap.add_argument("--wlast", type=float, default=2.0); ap.add_argument("--out", required=True); ap.add_argument("--budget_s", type=float, default=2400)
a = ap.parse_args(); torch.set_num_threads(a.threads); torch.manual_seed(a.seed); os.makedirs(a.out, exist_ok=True)
m = M.CtxGRU(H=a.H, n_desc=4 if a.kind == "reg" else 0); opt = torch.optim.Adam(m.parameters(), lr=1.5e-3)
t0 = time.time(); log = open(os.path.join(a.out, "log.jsonl"), "w"); T = env.T
for step in range(a.steps):
    g = torch.Generator().manual_seed(21000 + 100003 * a.seed + step)                    # training namespace 21000+
    Bctx = [1, 2, 4, 8][int(torch.randint(0, 4, (1,), generator=g))]
    inst = env.sample_instances(env.TRAIN_FAMS, a.batch // 3 + 1, 21000 + 100003 * a.seed + step)
    N = inst["c"].shape[0]
    eps = torch.randn(N, (Bctx + 1) * T, 2, generator=g, dtype=torch.float64)
    # context episodes: random programmes (sweep order with prob .5 for the supervised regressor); last = a random probe
    progs = [env.random_programmes(N, g) for _ in range(Bctx)]
    if a.kind == "reg" and float(torch.rand(1, generator=g)) < 0.5:
        progs = [env.PROBES[env.PROBE_ORDER[i % 4]][None].expand(N, -1, -1).clone() for i in range(Bctx)]
    qi = int(torch.randint(0, 4, (1,), generator=g)); progs.append(env.PROBES[env.PROBE_ORDER[qi]][None].expand(N, -1, -1).clone())
    U = torch.cat(progs, 1); Y = torch.cat([env.simulate(inst, p, eps[:, i * T:(i + 1) * T]) for i, p in enumerate(progs)], 1)
    U, Y = U.float(), Y.float()
    if a.kind == "wm":
        nll, _ = m.run(U, Y, T, ss_prob=a.ss, free_last=True)
        w = torch.ones(nll.shape[1]); w[-T:] = a.wlast
        loss = (nll * w).mean()
    else:
        td = ((env.true_descriptors(inst) - env.DESC_MEAN) / env.DESC_SD).float()
        _, h = m.run(U[:, :Bctx * T], Y[:, :Bctx * T], T)
        loss = ((m.predict_desc(h) - td) ** 2).mean()
    opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(m.parameters(), 5.0); opt.step()
    if (step + 1) % 50 == 0:
        log.write(json.dumps(dict(step=step + 1, loss=float(loss.detach()), Bctx=Bctx, t=time.time() - t0)) + "\n"); log.flush()
    if time.time() - t0 > a.budget_s: log.write(json.dumps(dict(note="budget_exhausted", step=step + 1)) + "\n"); break
torch.save(m.state_dict(), os.path.join(a.out, "final.pt")); json.dump(vars(a), open(os.path.join(a.out, "config.json"), "w"))
