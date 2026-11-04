"""Interaction conditions: non-adaptive policies, exact-Bayes oracle EIG planner, learned-ensemble disagreement planner."""
from __future__ import annotations
import torch
from . import gen, policies

BLK = policies.BLOCK
_c = []
for a in policies.MENU.tolist():
    _c.append([a] * BLK)
for a in (0.15, 0.3, 0.6, 1.0):
    _c.append([a, -a] * (BLK // 2))
for a in (0.5, 1.0):
    _c.append([a] + [0.0] * (BLK - 1))
CAND = torch.tensor(_c, dtype=torch.float64)       # [C,8]
NC = CAND.shape[0]


def _fam_hyps(fam):
    hy = gen.HGRID[fam]
    return torch.tensor([c for c, _ in hy]), torch.tensor([p for _, p in hy], dtype=torch.float64)


def _hyp_sim(inst, hc, hp, U):
    """inst: N instances; U [N,C,T] actions -> means [N,H,C,T]."""
    N, C, T = U.shape; H = len(hc)
    cls = hc[None, :, None].expand(N, H, C).reshape(-1)
    p = hp[None, :, None].expand(N, H, C).reshape(-1)
    K = inst["K"][:, None, None].expand(N, H, C).reshape(-1)
    b = inst["b"][:, None, None].expand(N, H, C).reshape(-1)
    u = U[:, None].expand(N, H, C, T).reshape(-1, T)
    return gen.simulate(cls, K, b, p, u).reshape(N, H, C, T)


def oracle_choose(inst, fam, u_hist, y_hist, g, S=6):
    """Exact-Bayes expected-class-entropy-reduction over the candidate block programs. Knows family,K,b,sigma."""
    N, t0 = y_hist.shape
    hc, hp = _fam_hyps(fam); H = len(hc)
    prior = torch.zeros(H, dtype=torch.float64)
    for c in hc.unique():
        sel = hc == c; prior[sel] = 1.0 / (3 * sel.sum())
    U = torch.cat([u_hist[:, None].expand(N, NC, t0), CAND[None].expand(N, NC, BLK)], -1)  # [N,C,t0+8]
    m = _hyp_sim(inst, hc, hp, U)                                                           # [N,H,C,T]
    sig = inst["sigma"]
    if t0 > 0:
        ll = -((y_hist[:, None] - m[:, :, 0, :t0]) ** 2).sum(-1) / (2 * sig[:, None] ** 2)
    else:
        ll = torch.zeros(N, H, dtype=torch.float64)
    lp = torch.log_softmax(prior.log()[None] + ll, 1)                                       # [N,H]
    mb = m[..., t0:]                                                                        # [N,H,C,8]
    hs = torch.multinomial(lp.exp(), S, replacement=True, generator=g)                      # [N,S]
    eps = torch.randn(N, S, NC, BLK, generator=g, dtype=torch.float64)
    mt = torch.gather(mb, 1, hs[:, :, None, None].expand(N, S, NC, BLK))                    # [N,S,C,8]
    yb = mt + sig[:, None, None, None] * eps
    llb = -((yb[:, :, :, None, :] - mb.permute(0, 2, 1, 3)[:, None]) ** 2).sum(-1) / (2 * sig[:, None, None, None] ** 2)
    lp2 = torch.log_softmax(lp[:, None, None, :] + llb, -1)                                 # [N,S,C,H]
    ent = torch.zeros(N, S, NC, dtype=torch.float64)
    for c in hc.unique():
        pc = lp2[..., hc == c].exp().sum(-1).clamp_min(1e-12)
        ent -= pc * pc.log()
    return ent.mean(1).argmin(-1)                                                           # minimise expected entropy


def ensemble_choose(models, u_hist, y_hist):
    """Pick the block program maximising mean ensemble variance of imagined observation means."""
    N, t0 = y_hist.shape
    preds = []
    for m in models:
        if t0 == 0:
            h, z = m.init_state(N)
        else:
            h, z, _, _ = m.filter(u_hist.float(), y_hist.float())
        h = h[:, None].expand(N, NC, -1).reshape(N * NC, -1); z = z[:, None].expand(N, NC, -1).reshape(N * NC, -1)
        acts = CAND[None].expand(N, NC, BLK).reshape(N * NC, BLK).float()
        preds.append(m.rollout(h, z, acts).reshape(N, NC, BLK))
    P = torch.stack(preds, 0)                      # [M,N,C,8]
    return P.var(0, unbiased=False).mean(-1).argmax(-1)


def interact(cond, inst, L, g, models=None, eps=None):
    """Run one interaction condition. Returns u,y (float64). Noise realisation eps[N,L] shared across conditions."""
    N = inst["K"].shape[0]
    if eps is None:
        eps = torch.randn(N, L, generator=g, dtype=torch.float64)
    nonad = dict(passive="passive", uniform="uniform", sweep="sweep", randblock="block")
    if cond in nonad:
        u = policies.sample_actions(nonad[cond], N, L, g)
        x = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u)
        return u, x + inst["sigma"][:, None] * eps
    u = torch.zeros(N, L, dtype=torch.float64)
    for blk in range(L // BLK):
        t0 = blk * BLK
        if cond == "oracle_eig":
            ch = torch.zeros(N, dtype=torch.long)
            for fam in (0, 1):
                idx = (inst["fam"] == fam).nonzero().squeeze(-1)
                if len(idx) == 0: continue
                sub = gen.take(inst, idx)
                x = gen.simulate(sub["cls"], sub["K"], sub["b"], sub["p"], u[idx, :t0]) if t0 > 0 else None
                yh = (x + sub["sigma"][:, None] * eps[idx, :t0]) if t0 > 0 else torch.zeros(len(idx), 0, dtype=torch.float64)
                ch[idx] = oracle_choose(sub, fam, u[idx, :t0], yh, g)
        elif cond == "ens_disagree":
            if t0 > 0:
                x = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u[:, :t0])
                yh = x + inst["sigma"][:, None] * eps[:, :t0]
            else:
                yh = torch.zeros(N, 0, dtype=torch.float64)
            ch = ensemble_choose(models, u[:, :t0], yh)
        else:
            raise ValueError(cond)
        u[:, t0:t0 + BLK] = CAND[ch]
    x = gen.simulate(inst["cls"], inst["K"], inst["b"], inst["p"], u)
    return u, x + inst["sigma"][:, None] * eps
