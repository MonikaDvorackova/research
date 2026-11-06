"""Exact quantities for X1: KL rates under open-loop iid policies, nearest-member distances, positive-control selection."""
import itertools
import numpy as np
from eid.pomdp import exact_obs_law, A

T_EXACT = 4


def _kl(p, r):
    m = p > 0
    return float(np.sum(p[m] * np.log(p[m] / r[m])))


def policy_kl(truth, member, q, T=T_EXACT):
    pr = np.array([(1 - q) / 2, (1 - q) / 2, q])
    tot = 0.0
    for acts in itertools.product(range(A), repeat=T):
        w = np.prod(pr[list(acts)])
        if w > 0:
            tot += w * _kl(exact_obs_law(truth, acts), exact_obs_law(member, acts))
    return tot


def nearest_member(truth, comps, q, T=T_EXACT):
    ks = [policy_kl(truth, m, q, T) for m in comps]
    i = int(np.argmin(ks))
    return i, ks[i]


def pc_member_index(e0, M, W, q=1 / 3, T=T_EXACT):
    """Positive control: the W member whose distance (KL under the wide policy) to its nearest M member is the median over W."""
    d = [nearest_member(w, [m for _, m in M], q, T)[1] for w in W]
    order = np.argsort(d)
    return int(order[len(order) // 2])
