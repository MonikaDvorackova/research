"""Train the class-conditional simulator bank (identifiable training regime only; labels = class). Resumable-free (short)."""
import argparse, os, sys, time, json
import torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.gwb import models, train as tr

ap = argparse.ArgumentParser()
ap.add_argument("--seed", type=int, default=1); ap.add_argument("--steps", type=int, default=3000)
ap.add_argument("--batch", type=int, default=128); ap.add_argument("--threads", type=int, default=3)
ap.add_argument("--out", required=True)
a = ap.parse_args()
torch.set_num_threads(a.threads); torch.manual_seed(a.seed); os.makedirs(a.out, exist_ok=True)
m = models.CondGRU(); opt = torch.optim.Adam(m.parameters(), lr=1e-3)
t0 = time.time(); log = open(os.path.join(a.out, "log.jsonl"), "w")
for step in range(a.steps):
    inst, views = tr.make_batch(step, a.seed + 700, a.batch, 48, "cpu")      # train-seed namespace 701.. (unexposed)
    loss = sum(m(v[0], v[1], inst["label"])["nll"].mean() for v in views) / 2
    opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(m.parameters(), 10.0); opt.step()
    if (step + 1) % 100 == 0: log.write(json.dumps(dict(step=step + 1, nll=float(loss.detach()), t=time.time() - t0)) + "\n"); log.flush()
torch.save(m.state_dict(), os.path.join(a.out, "final.pt")); json.dump(vars(a), open(os.path.join(a.out, "config.json"), "w"))
