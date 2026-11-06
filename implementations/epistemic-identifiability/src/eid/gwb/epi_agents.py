"""Sequential epistemic agents: learned class-conditional simulators (M7) and exact-Bayes oracle (M1)."""
from __future__ import annotations
import numpy as np, torch
from . import gen, agents, epi, policies

BLK = policies.BLOCK
CAND, NC = agents.CAND, agents.NC
DELTA_PERSIST = 4.0                       # pre-stated: d_max < 4  (~ squared 2 noise-sd) => 'persistent-uncertified'


def passive_block(n, g):
    return (0.3 * torch.randn(n, BLK, generator=g, dtype=torch.float64)).clamp(-1, 1)


def _y_prefix(inst, u, eps, t):
    x = epi.x_of(inst, u[:, :t])
    return x + inst["sigma"][:, None] * eps[:, :t]


def run_seq(inst, chooser, u0, eps, L=48):
    N = u0.shape[0]
    u = torch.zeros(N, L, dtype=torch.float64); u[:, :BLK] = u0
    for blk in range(1, L // BLK):
        t0 = blk * BLK
        yh = _y_prefix(inst, u, eps, t0)
        idx = chooser(blk, u[:, :t0], yh, inst)
        u[:, t0:t0 + BLK] = CAND[idx]
    return u, epi.x_of(inst, u) + inst["sigma"][:, None] * eps


# ---------------- M7: learned class-conditional simulators ----------------
@torch.no_grad()
def cond_stats(model, u, y, bs=600):
    """per-class prefix log-likelihoods at block boundaries [N,6,nb], and per-class standardized-residual mean z^2 [N,6]."""
    N, T = u.shape; out_ll, out_gof = [], []
    for i in range(0, N, bs):
        a = u[i:i + bs].float(); yy = y[i:i + bs].float(); B = a.shape[0]
        aa = a.repeat_interleave(6, 0); yb = yy.repeat_interleave(6, 0); c = torch.arange(6).repeat(B)
        o = model(aa, yb, c)
        ll = -o["nll"].reshape(B, 6, T)                                  # per-step log-lik
        z2 = (((yb - o["mu"]) / o["ls"].exp()) ** 2).reshape(B, 6, T)
        out_ll.append(ll.cumsum(-1)[:, :, BLK - 1::BLK]); out_gof.append(z2.mean(-1))
    return torch.cat(out_ll).double(), torch.cat(out_gof).double()


@torch.no_grad()
def cond_choose(model, u, y, inst, bs=300):
    """Pick the block programme maximising posterior-weighted pairwise predicted divergence between class simulators."""
    N, t0 = y.shape; res = torch.zeros(N, dtype=torch.long)
    for i in range(0, N, bs):
        a = u[i:i + bs].float(); yy = y[i:i + bs].float(); B = a.shape[0]
        aa = a.repeat_interleave(6, 0); yb = yy.repeat_interleave(6, 0); c = torch.arange(6).repeat(B)
        h, yp, mu, ls, nll = model.filter(aa, yb, c)
        post = torch.softmax(-nll.sum(-1).reshape(B, 6), 1)                # uniform prior
        top = post.argmax(1)
        sig = ls.reshape(B, 6, -1)[torch.arange(B), top][:, -BLK:].mean(-1).exp()          # [B]
        hh = h.repeat_interleave(NC, 0); yy2 = yp.repeat_interleave(NC, 0); cc = c.repeat_interleave(NC)
        acts = CAND[None].expand(B * 6, NC, BLK).reshape(-1, BLK).float()
        pred = model.rollout(hh, yy2, acts, cc).reshape(B, 6, NC, BLK)
        diff = (pred[:, :, None] - pred[:, None]) ** 2                      # [B,6,6,NC,BLK]
        D = diff.sum(-1) / sig[:, None, None, None] ** 2
        w = post[:, :, None] * post[:, None, :]
        res[i:i + bs] = (w[..., None] * D).sum((1, 2)).argmax(-1)
    return res


@torch.no_grad()
def cond_final_dmax(model, u, y, bs=300):
    """d_max(top1,top2) over candidate next-block programmes from the final state, plus posterior."""
    N = u.shape[0]; dm = torch.zeros(N, dtype=torch.float64)
    for i in range(0, N, bs):
        a = u[i:i + bs].float(); yy = y[i:i + bs].float(); B = a.shape[0]
        aa = a.repeat_interleave(6, 0); yb = yy.repeat_interleave(6, 0); c = torch.arange(6).repeat(B)
        h, yp, mu, ls, nll = model.filter(aa, yb, c)
        post = torch.softmax(-nll.sum(-1).reshape(B, 6), 1)
        t2 = post.topk(2, 1).indices                                         # [B,2]
        sig = ls.reshape(B, 6, -1)[torch.arange(B), t2[:, 0]][:, -BLK:].mean(-1).exp()
        hh = h.repeat_interleave(NC, 0); yy2 = yp.repeat_interleave(NC, 0); cc = c.repeat_interleave(NC)
        acts = CAND[None].expand(B * 6, NC, BLK).reshape(-1, BLK).float()
        pred = model.rollout(hh, yy2, acts, cc).reshape(B, 6, NC, BLK)
        p1 = pred[torch.arange(B), t2[:, 0]]; p2 = pred[torch.arange(B), t2[:, 1]]
        dm[i:i + bs] = (((p1 - p2) ** 2).sum(-1) / sig[:, None] ** 2).max(-1).values.double()
    return dm


def m7_outputs(model, u, y):
    ll, gof = cond_stats(model, u, y)
    post_blocks = torch.softmax(ll, 1)                                      # [N,6,nb]
    post = post_blocks[:, :, -1]
    top = post.argmax(1)
    gof_top = gof[torch.arange(len(top)), top]
    return dict(post=post.numpy(), post_blocks=post_blocks.numpy(), gof=gof_top.numpy(), dmax=cond_final_dmax(model, u, y).numpy())


# ---------------- M1: exact-Bayes oracle with model-relative persistence test ----------------
def oracle_chooser(g):
    def f(blk, u, y, inst):
        N = u.shape[0]; ch = torch.zeros(N, dtype=torch.long)
        for fam in (0, 1):
            idx = (inst["fam"] == fam).nonzero().squeeze(-1)
            for j in range(0, len(idx), 700):
                ii = idx[j:j + 700]
                ch[ii] = agents.oracle_choose(gen.take(inst, ii), fam, u[ii], y[ii], g)
        return ch
    return f


def cond_chooser(model):
    return lambda blk, u, y, inst: cond_choose(model, u, y, inst)


def oracle_outputs(inst, u, y):
    """class posterior (epistemic grid), top-2 persistence statistic d_max over candidate next blocks between the MAP
    hypotheses of the two leading classes, and best-fit residual (goodness of fit)."""
    N, T = u.shape
    post = np.zeros((N, gen.NCLS)); dmax = np.zeros(N); gof = np.zeros(N)
    for fam in (0, 1):
        idx = (inst["fam"] == fam).nonzero().squeeze(-1)
        hy = epi.HGRID_EPI[fam]; hc = torch.tensor([c for c, _ in hy]); hp = torch.tensor([p for _, p in hy], dtype=torch.float64)
        prior = torch.zeros(len(hy), dtype=torch.float64)
        for c in hc.unique(): prior[hc == c] = 1.0 / (3 * (hc == c).sum())
        for j in range(0, len(idx), 400):
            ii = idx[j:j + 400]; sub = gen.take(inst, ii); n = len(ii)
            U = torch.cat([u[ii][:, None].expand(n, NC, T), CAND[None].expand(n, NC, BLK)], -1)
            m = agents._hyp_sim(sub, hc, hp, U)                              # [n,H,NC,T+8]
            ll = -((y[ii][:, None] - m[:, :, 0, :T]) ** 2).sum(-1) / (2 * sub["sigma"][:, None] ** 2)   # [n,H]
            lp = torch.softmax(prior.log()[None] + ll, 1)
            cp = torch.zeros(n, gen.NCLS, dtype=torch.float64)
            for c in hc.unique(): cp[:, int(c)] = lp[:, hc == c].sum(1)
            post[ii.numpy()] = cp.numpy()
            gof[ii.numpy()] = ((-2 * ll.max(1).values) / T).numpy()           # mean z^2 of best-fitting hypothesis
            t2 = cp.topk(2, 1).indices
            d = torch.zeros(n, dtype=torch.float64)
            ar = torch.arange(n)
            best = []
            for r in range(2):
                llc = torch.where((hc[None] == t2[:, r:r + 1]), ll, torch.full_like(ll, -1e30))
                best.append(llc.argmax(1))                                    # MAP hypothesis of class r
            m1 = m[ar, best[0]][..., T:]; m2 = m[ar, best[1]][..., T:]        # [n,NC,8]
            d = (((m1 - m2) ** 2).sum(-1) / sub["sigma"][:, None] ** 2).max(1).values
            dmax[ii.numpy()] = d.numpy()
    return dict(post=post, dmax=dmax, gof=gof)
