"""P5 test: finite-context predictors of an n-bit LFSR click stream. MLP on the last k clicks; k < n must give CE >= ln2 - O(2^-(n-k))."""
import json, math, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.kick import world as W
torch.set_num_threads(2); LN2 = math.log(2); res = {}
for kind, n in (("lfsr", 6), ("lfsr", 8), ("lfsr", 10), ("lfsr", 12)):
    spec = W.sample_gen(kind, n, np.random.default_rng(14000 + 97 * n + 0))            # same instance as the grid (inst 0)
    # exact conditional-entropy bound from the window property: empirical over one full period
    per = (1 << n) - 1; full = spec.stream(np.array([1]), per + n + 2)[0].astype(int)
    res[f"n{n}"] = {}
    for k in sorted({max(1, n - 3), n - 1, n, n + 2}):
        # exact Bayes-optimal CE of a k-context predictor over one full period (counts of next bit given previous k bits)
        ctx = np.array([int("".join(map(str, full[t - k:t])), 2) for t in range(k, per + k)]); nxt = full[k:per + k]
        cnt = np.zeros((1 << k, 2)); np.add.at(cnt, (ctx, nxt), 1)
        p = cnt / np.maximum(cnt.sum(1, keepdims=True), 1); w = cnt.sum(1) / cnt.sum()
        h = float(-(w[:, None] * np.where(cnt > 0, p * np.log(np.clip(p, 1e-12, 1)), 0)).sum())
        # learned MLP, trained on fresh random-phase streams, evaluated on fresh streams
        torch.manual_seed(0); rng = np.random.default_rng(1)
        net = torch.nn.Sequential(torch.nn.Linear(k, 128), torch.nn.ReLU(), torch.nn.Linear(128, 128), torch.nn.ReLU(), torch.nn.Linear(128, 1))
        opt = torch.optim.Adam(net.parameters(), lr=2e-3)
        def batch(N, T=96):
            b = W.bit_streams(spec, N, T, rng).astype(np.float32)
            X = np.stack([b[:, t - k:t] for t in range(k, T)], 1).reshape(-1, k); y = b[:, k:].reshape(-1)
            return torch.tensor(X), torch.tensor(y)
        for step in range(3000):
            X, y = batch(64); loss = torch.nn.functional.binary_cross_entropy_with_logits(net(X).squeeze(-1), y)
            opt.zero_grad(); loss.backward(); opt.step()
        ces = []
        for s in range(40):
            X, y = batch(32)
            with torch.no_grad(): ces.append(float(torch.nn.functional.binary_cross_entropy_with_logits(net(X).squeeze(-1), y)))
        ces = np.array(ces); z = (LN2 - ces.mean()) / (ces.std(ddof=1) / math.sqrt(len(ces)))
        res[f"n{n}"][f"k{k}"] = dict(k=k, bayes_ce_exact_over_period=h, ln2=LN2, learned_ce=float(ces.mean()), z=float(z))
        print(n, k, "exactBayesCE", round(h, 4), "learned", round(float(ces.mean()), 4), "z", round(float(z), 1), flush=True)
json.dump(res, open("results/kick_dev/window_control.json", "w"), indent=1)
