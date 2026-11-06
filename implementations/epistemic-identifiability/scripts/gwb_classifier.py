"""Supervised end-to-end mechanism classifier (control).  Trained with class labels on the same training distribution."""
import argparse, os, sys, time, json
import torch, torch.nn.functional as F
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.gwb import models, train as tr

ap = argparse.ArgumentParser()
ap.add_argument("--seed", type=int, default=0); ap.add_argument("--steps", type=int, default=2500)
ap.add_argument("--batch", type=int, default=256); ap.add_argument("--threads", type=int, default=3)
ap.add_argument("--out", required=True)
a = ap.parse_args()
torch.set_num_threads(a.threads); torch.manual_seed(a.seed); os.makedirs(a.out, exist_ok=True)
m = models.ClassifierGRU(); opt = torch.optim.Adam(m.parameters(), lr=1e-3)
t0 = time.time(); log = open(os.path.join(a.out, "log.jsonl"), "w")
for step in range(a.steps):
    inst, views = tr.make_batch(step, a.seed + 50, a.batch, 48, "cpu")
    loss = sum(F.cross_entropy(m(*v), inst["label"]) for v in views) / 2
    opt.zero_grad(); loss.backward(); opt.step()
    if (step + 1) % 100 == 0: log.write(json.dumps(dict(step=step + 1, loss=float(loss), t=time.time() - t0)) + "\n"); log.flush()
torch.save(m.state_dict(), os.path.join(a.out, "final.pt")); json.dump(vars(a), open(os.path.join(a.out, "config.json"), "w"))
