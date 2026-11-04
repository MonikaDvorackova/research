"""Train a gwb world model. Resumable; deterministic given (seed, step). Development use only."""
from __future__ import annotations
import argparse, json, os, time
import torch
from . import gen, models, policies

SEED_NS = dict(val=9001, probe=9100, test=9200)


def make_batch(step, seed, B, L, dev, family="both"):
    g = torch.Generator().manual_seed(seed * 1_000_003 + step)
    inst = gen.sample_instances(B, "train", family=family, seed=seed * 1_000_003 + step)
    views = []
    for _ in range(2):
        a = policies.sample_train_actions(B, L, g)
        y, _ = gen.observe(inst, a, g)
        views.append((a.float().to(dev), y.float().to(dev)))
    return inst, views


def build(kind, H=128):
    return models.RSSM(H=H) if kind == "rssm" else models.DetGRU(H=H)


def evaluate_nll(model, dev, n=512, L=48):
    inst = gen.sample_instances(n, "train", seed=SEED_NS["val"])
    g = torch.Generator().manual_seed(SEED_NS["val"])
    a = policies.sample_train_actions(n, L, g); y, _ = gen.observe(inst, a, g)
    with torch.no_grad():
        o = model(a.float().to(dev), y.float().to(dev), sample=False)
    return float(o["nll"].mean())


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["rssm", "det"], required=True)
    ap.add_argument("--lam", type=float, default=0.0, help="InfoNCE (ICI) weight; 0 = prediction-only")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--steps", type=int, default=3000)
    ap.add_argument("--batch", type=int, default=128)
    ap.add_argument("--L", type=int, default=48)
    ap.add_argument("--H", type=int, default=128)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--beta", type=float, default=1.0)
    ap.add_argument("--family", default="both", choices=["both", "A", "B"])
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--threads", type=int, default=3)
    ap.add_argument("--budget_s", type=float, default=3600)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    torch.set_num_threads(a.threads)
    os.makedirs(a.out, exist_ok=True)
    torch.manual_seed(a.seed)
    model = build(a.model, a.H).to(a.device)
    opt = torch.optim.Adam(model.parameters(), lr=a.lr)
    ck = os.path.join(a.out, "ckpt.pt"); start = 0; elapsed = 0.0
    json.dump(vars(a), open(os.path.join(a.out, "config.json"), "w"))
    if os.path.exists(ck):
        s = torch.load(ck, weights_only=False)
        model.load_state_dict(s["model"]); opt.load_state_dict(s["opt"]); start = s["step"]; elapsed = s["elapsed"]
    log = open(os.path.join(a.out, "log.jsonl"), "a")
    t0 = time.time() - elapsed
    for step in range(start, a.steps):
        _, views = make_batch(step, a.seed, a.batch, a.L, a.device, a.family)
        outs = [model(v[0], v[1]) for v in views]
        pred = sum(o["nll"].mean() + a.beta * o["kl"].mean() + (o["nll_prior"].mean() if "nll_prior" in o else 0.0) for o in outs) / 2
        loss = pred; ici = torch.zeros(())
        if a.lam > 0:
            ici = models.info_nce(model.proj(outs[0]["feat"]), model.proj(outs[1]["feat"]))
            loss = pred + a.lam * ici
        opt.zero_grad(); loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 10.0); opt.step()
        if (step + 1) % 100 == 0 or step == a.steps - 1:
            rec = dict(step=step + 1, loss=float(loss.detach()), nll=float(outs[0]["nll"].mean().detach()), nllp=float(outs[0]["nll_prior"].mean().detach()) if "nll_prior" in outs[0] else None, ici=float(ici.detach()), t=time.time() - t0)
            if (step + 1) % 500 == 0 or step == a.steps - 1:
                rec["val_nll"] = evaluate_nll(model, a.device, L=a.L)
            log.write(json.dumps(rec) + "\n"); log.flush()
        if (step + 1) % 250 == 0 or step == a.steps - 1:
            torch.save(dict(model=model.state_dict(), opt=opt.state_dict(), step=step + 1, elapsed=time.time() - t0), ck)
        if time.time() - t0 > a.budget_s:
            torch.save(dict(model=model.state_dict(), opt=opt.state_dict(), step=step + 1, elapsed=time.time() - t0), ck)
            log.write(json.dumps(dict(note="budget_exhausted", step=step + 1)) + "\n"); break
    torch.save(model.state_dict(), os.path.join(a.out, "final.pt"))


if __name__ == "__main__":
    main()
