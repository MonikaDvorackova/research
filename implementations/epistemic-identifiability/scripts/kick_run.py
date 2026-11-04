"""Train an MDN-GRU world model on ONE kick-world instance and evaluate determinism detection, extraction, replay.
usage: kick_run.py --kind lfsr|nlfsr|rand --n 8 --inst 0 --H 128 --steps 4000 --out DIR"""
import argparse, json, math, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from eid.kick import world as W, model as M, algebra as A

LN2 = math.log(2)
EVAL_T0 = 16


def tt(x): return torch.tensor(x, dtype=torch.float32)


def run(model, b):
    return model(tt(b['obs']), tt(b['act']), tt(b['click']))


def detect_stats(model, spec, rng, N=512, T=96):
    b = W.make_batch(spec, N, T, rng)
    with torch.no_grad():
        bce, nll, lg = run(model, b)
    ce = bce[:, EVAL_T0:].mean(1).numpy()                                    # per-stream mean click CE (independent streams)
    z = (LN2 - ce.mean()) / (ce.std(ddof=1) / math.sqrt(len(ce)) + 1e-12)
    return dict(ce_inferred=float(ce.mean()), z=float(z), frac_predicted=float((LN2 - ce.mean()) / LN2),
                nll_obs=float(nll[:, EVAL_T0:].mean()), acc_click=float(((lg > 0).float() == tt(b["click"]))[:, EVAL_T0:].float().mean()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", required=True); ap.add_argument("--n", type=int, default=8); ap.add_argument("--inst", type=int, default=0)
    ap.add_argument("--H", type=int, default=128); ap.add_argument("--steps", type=int, default=4000); ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--T", type=int, default=96); ap.add_argument("--lr", type=float, default=2e-3); ap.add_argument("--threads", type=int, default=3)
    ap.add_argument("--out", required=True); ap.add_argument("--budget_s", type=float, default=900); ap.add_argument("--train_seed", type=int, default=0)
    a = ap.parse_args(); torch.set_num_threads(a.threads); os.makedirs(a.out, exist_ok=True)
    grng = np.random.default_rng(14000 + 97 * a.n + a.inst)
    spec = None if a.kind == "rand" else W.sample_gen(a.kind, a.n, grng)
    torch.manual_seed(a.train_seed + 1000 * a.inst)
    model = M.KickGRU(H=a.H); opt = torch.optim.Adam(model.parameters(), lr=a.lr)
    trng = np.random.default_rng(15000 + 97 * a.n + a.inst + 7 * a.train_seed)
    erng = lambda tag: np.random.default_rng(16000 + 97 * a.n + a.inst + tag)       # fresh-stream evaluation (same for every checkpoint)
    rrng = np.random.default_rng(17000 + a.inst)
    log = []; t0 = time.time()
    for step in range(1, a.steps + 1):
        b = W.make_batch(spec, a.batch, a.T, trng)
        bce, nll, _ = run(model, b)
        loss = (bce + nll)[:, EVAL_T0:].mean()
        opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0); opt.step()
        if step % 250 == 0 or step == a.steps:
            model.eval(); rec = dict(step=step, train_nll=float(loss.detach()), t=time.time() - t0)
            rec["G"] = detect_stats(model, spec, erng(step))
            rec["cross_R"] = detect_stats(model, None, np.random.default_rng(17000 + a.inst + step))   # same model on TRUE-random shocks (validity)
            log.append(rec); model.train()
            if time.time() - t0 > a.budget_s: break
    model.eval()
    res = dict(args=vars(a), spec=None if spec is None else spec.describe(), curve=log, train_seconds=time.time() - t0)
    if spec is not None:
        res["period"] = spec.period(1, cap=1 << 22)
    # ---------- hypothesis extraction + exact verification (clicks are observed bits) ----------
    ex = {}
    rng = erng(99999); b = W.make_batch(spec, 1024, 96, rng)
    with torch.no_grad(): _, _, lg = run(model, b)
    pred = (lg.numpy() > 0).astype(np.uint8); bits = b["click"].astype(np.uint8)
    ex["model_next_click_acc"] = float((pred[:, EVAL_T0:] == bits[:, EVAL_T0:]).mean())
    for name, deg, LL in (("linear", 1, 32), ("deg2", 2, min(a.n + 2, 14))):
        # fit a GF(2) recurrence to the MODEL's own click predictions as a function of the observed click history
        H, Y = [], []
        for i in range(bits.shape[0]):
            for t in range(max(EVAL_T0, LL), 96):
                H.append(bits[i, t - LL:t][::-1]); Y.append(pred[i, t])
        H = np.array(H, dtype=np.uint8); Y = np.array(Y, dtype=np.uint8)
        mons = A._monomials(LL, deg); idx = np.random.default_rng(5).permutation(len(H))[: 4 * len(mons) + 50]
        coef = A.gf2_solve(A._design(H[idx], mons), Y[idx])
        if coef is None:
            ex[name] = dict(consistent=False, monomials=len(mons)); continue
        b2 = W.make_batch(spec, 512, 96, erng(88888)); bits2 = b2["click"].astype(np.uint8)
        H2 = np.array([bits2[i, t - LL:t][::-1] for i in range(512) for t in range(max(EVAL_T0, LL), 96)], dtype=np.uint8)
        Y2 = np.array([bits2[i, t] for i in range(512) for t in range(max(EVAL_T0, LL), 96)], dtype=np.uint8)
        acc = float((A.predict_recurrence((mons, coef), H2) == Y2).mean())
        ex[name] = dict(consistent=True, monomials=len(mons), verify_acc_vs_env_clicks=acc, verify_n=int(len(Y2)),
                        exact=bool(acc == 1.0), support=int(coef.sum()))
    # exact structured baselines on the observed click stream (privileged knowledge of the class only)
    if spec is not None:
        s_ = list(spec.stream(np.array([5]), 400)[0].astype(int))
        Lc, c = A.berlekamp_massey(s_); ex["BM_linear_complexity"] = int(Lc); ex["BM_bits_needed"] = int(2 * Lc)
    res["extraction"] = ex
    # ---------- replay test (interface with a reset): identical hidden seed + actions; compare observed click sequences ----------
    rp = W.replay_pair(spec, 256, 48, np.random.default_rng(18000 + a.inst))
    res["replay"] = dict(click_agreement=float((rp["bits1"] == rp["bits2"]).mean()))
    json.dump(res, open(os.path.join(a.out, "result.json"), "w"), indent=1, default=float)
    torch.save(model.state_dict(), os.path.join(a.out, "final.pt"))
    last = log[-1]; print(a.kind, a.n, a.inst, "H", a.H, "z", round(last["G"]["z"], 1), "frac", round(last["G"]["frac_predicted"], 3), "crossR z", round(last["cross_R"]["z"], 2), "ext", ex.get("deg2"), f"{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
