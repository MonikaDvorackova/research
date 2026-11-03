"""Phase 11: upper bounds U(D) >= L*(D) = sup_{theta in Theta_0} p_theta(D) for small controlled HMMs.

(A/B) interval branch-and-bound (S = 2): certified up to the stated floating-point inflation; any partition of the parameter box yields a VALID bound, and the
      bound converges to the supremum as boxes shrink (this class of algorithm exists in the literature: Montanher; Gormley-Eisner).
(C)   type-class relaxation (any S, O, A): group latent paths by their complete-data sufficient statistics c = (s_0, transition counts N, emission counts M).
      p_theta(D) = sum_c W(c) f_c(theta), f_c(theta) = b0(s_0) prod T^N prod Z^M >= 0.  Then
          L*(D) <= U_C(D) := sum_c W(c) sup_theta f_c(theta)   (sup of a sum of nonnegative terms <= sum of sups; each sup is a closed-form complete-data MLE)
      and  L*(D) >= max_c W(c) sup f_c(theta) >= U_C(D)/K,  K = number of classes with W > 0, hence 0 <= log U_C - log L* <= log K.
(D)   confidence-set-restricted supremum: boxes whose certified upper bound on the TRAINING likelihood lies below the confidence level are discarded."""
from __future__ import annotations

import itertools
import math
import time
from fractions import Fraction

import numpy as np

U_ROUND = 2.0 ** -53


def fp_inflation(n):
    """Relative inflation making a computed product-sum of n+1 nonnegative factors an upper bound in IEEE-754 double (round-to-nearest, no under/overflow):
    each multiplication/addition contributes a relative error <= u, and fewer than 16 (n + 2) operations enter any term."""
    return 1.0 + 16.0 * (n + 2) * U_ROUND * 1.01


# ---------------------------------------------------------------- (C) type-class relaxation
def type_classes(acts, obs, S, O, A, max_states=4_000_000):
    """Dictionary {(s0, N flat (A*S*S), M flat (S*O)) : W} of latent-path type classes consistent with the data; W = number of latent paths (exact Python int).
    Raises MemoryError when the DP exceeds max_states."""
    nN, nM = A * S * S, S * O
    states = {}
    for s0 in range(S):
        states[(s0, s0) + (0,) * (nN + nM)] = 1
    peak = len(states)
    for a, o in zip(acts, obs):
        new = {}
        for key, w in states.items():
            s0, st = key[0], key[1]
            cnt = key[2:]
            for s2 in range(S):
                lst = list(cnt)
                lst[a * S * S + st * S + s2] += 1
                lst[nN + s2 * O + o] += 1
                k2 = (s0, s2) + tuple(lst)
                new[k2] = new.get(k2, 0) + w
        states = new
        peak = max(peak, len(states))
        if len(states) > max_states:
            raise MemoryError(f"type-class DP exceeded {max_states} states")
    out = {}
    for key, w in states.items():
        k = (key[0],) + key[2:]
        out[k] = out.get(k, 0) + w
    return out, peak


def class_log_sup(key, S, O, A):
    """log sup_theta f_c(theta) = sum N log(N / N_row) + sum M log(M / M_row)   (b0 can be a point mass at s_0)."""
    nN = A * S * S
    cnt = key[1:]
    val = 0.0
    for a in range(A):
        for s in range(S):
            row = [cnt[a * S * S + s * S + s2] for s2 in range(S)]
            r = sum(row)
            for x in row:
                if x > 0:
                    val += x * math.log(x / r)
    for s in range(S):
        row = [cnt[nN + s * O + o] for o in range(O)]
        r = sum(row)
        for x in row:
            if x > 0:
                val += x * math.log(x / r)
    return val


def log_U_C(classes, S, O, A):
    terms = [math.log(w) + class_log_sup(k, S, O, A) for k, w in classes.items()]
    m = max(terms)
    return m + math.log(sum(math.exp(t - m) for t in terms)), m, len(classes)


def exact_U_C(classes, S, O, A):
    """Exact rational U_C (small n): sum_c W(c) prod (N/N_row)^N prod (M/M_row)^M."""
    nN = A * S * S
    tot = Fraction(0)
    for key, w in classes.items():
        cnt = key[1:]
        v = Fraction(w)
        for a in range(A):
            for s in range(S):
                row = [cnt[a * S * S + s * S + s2] for s2 in range(S)]
                r = sum(row)
                for x in row:
                    if x > 0:
                        v *= Fraction(x, r) ** x
        for s in range(S):
            row = [cnt[nN + s * O + o] for o in range(O)]
            r = sum(row)
            for x in row:
                if x > 0:
                    v *= Fraction(x, r) ** x
        tot += v
    return tot


def class_likelihood(classes, T, Z, b0, S, O, A):
    """sum_c W(c) f_c(theta): equals the forward-algorithm likelihood (identity used as a correctness check of the DP)."""
    nN = A * S * S
    tot = 0.0
    for key, w in classes.items():
        cnt = key[1:]
        v = b0[key[0]]
        for a in range(A):
            for s in range(S):
                for s2 in range(S):
                    v *= T[a, s, s2] ** cnt[a * S * S + s * S + s2]
        for s in range(S):
            for o in range(O):
                v *= Z[s, o] ** cnt[nN + s * O + o]
        tot += w * v
    return tot


# ---------------------------------------------------------------- (A/B/D) interval branch and bound, S = 2
def _unpack(lo, hi, A):
    """Parameter box (rows = boxes) for S = 2: tau[a, s] = T[a, s, 1], z[s] = Z[s, 1] (O = 2), beta = b0[1].  Columns: tau (2A), z (2), beta (1)."""
    return lo, hi


def box_upper(lo, hi, acts, obs, A):
    """Vectorised interval upper bound of p_theta(D) over boxes (S = 2, O = 2).  Entries are nonnegative and the likelihood is a product-sum of them, hence monotone."""
    B = lo.shape[0]
    tau_hi = hi[:, :2 * A].reshape(B, A, 2); tau_lo = lo[:, :2 * A].reshape(B, A, 2)
    z_hi, z_lo = hi[:, 2 * A:2 * A + 2], lo[:, 2 * A:2 * A + 2]
    be_hi, be_lo = hi[:, -1], lo[:, -1]
    b = np.stack([1.0 - be_lo, be_hi], 1)                                  # upper bounds of b0 = (1 - beta, beta)
    for a, o in zip(acts, obs):
        T01, T00 = tau_hi[:, a, :], 1.0 - tau_lo[:, a, :]                  # upper bounds of T[a, s, 1] and T[a, s, 0]
        zo = z_hi if o == 1 else 1.0 - z_lo                                # upper bound of Z[s', o]
        nb0 = (b[:, 0] * T00[:, 0] + b[:, 1] * T00[:, 1]) * zo[:, 0]
        nb1 = (b[:, 0] * T01[:, 0] + b[:, 1] * T01[:, 1]) * zo[:, 1]
        b = np.stack([nb0, nb1], 1)
    return b.sum(1) * fp_inflation(len(obs))


def box_point(theta, acts, obs, A):
    """Likelihood of a point theta (rows) computed in floating point and DEFLATED so that it is a lower bound of the true likelihood."""
    B = theta.shape[0]
    tau = theta[:, :2 * A].reshape(B, A, 2); z = theta[:, 2 * A:2 * A + 2]; be = theta[:, -1]
    b = np.stack([1.0 - be, be], 1)
    for a, o in zip(acts, obs):
        T01, T00 = tau[:, a, :], 1.0 - tau[:, a, :]
        zo = z if o == 1 else 1.0 - z
        b = np.stack([(b[:, 0] * T00[:, 0] + b[:, 1] * T00[:, 1]) * zo[:, 0], (b[:, 0] * T01[:, 0] + b[:, 1] * T01[:, 1]) * zo[:, 1]], 1)
    return b.sum(1) / fp_inflation(len(obs))


def theta_from_hmm(T, Z, b0, A):
    """Pack an S = 2, O = 2 HMM into the box coordinates (tau[a, s] = T[a, s, 1], z[s] = Z[s, 1], beta = b0[1])."""
    return np.concatenate([np.array([[T[a, s, 1] for s in range(2)] for a in range(A)]).ravel(), [Z[0, 1], Z[1, 1]], [b0[1]]])[None, :]


def branch_and_bound(acts, obs, A, log_tol=0.1, max_boxes=400_000, train=None, time_limit=60.0, warm=None):
    """Certified bracket [L_lo, U] for sup_theta p_theta(D) (S = 2, O = 2) by level-synchronous interval branch and bound; stops when log U - log L_lo <= log_tol or the
    budget is exhausted (the returned U is VALID either way).  `train = (acts_tr, obs_tr, gamma)` restricts to the confidence set {theta: p_theta(D_tr) >= exp(gamma)}:
    boxes whose certified training upper bound is below exp(gamma) are discarded (valid for the restricted supremum, with the confidence level accounted separately).
    Returns dict(L_lo, U, boxes_evaluated, rounds, seconds, certified_gap, converged)."""
    d = 2 * A + 3
    lo = np.zeros((1, d)); hi = np.ones((1, d))
    L_best = 0.0; evaluated = 0; rounds = 0; t0 = time.perf_counter()
    if warm is not None:                                                    # local-optimiser warm start: a deflated (hence valid) lower bound
        th = theta_from_hmm(*warm, A)
        if train is None or box_point(th, train[0], train[1], A)[0] >= math.exp(train[2]):
            L_best = float(box_point(th, acts, obs, A)[0])
    done_U = 0.0                                                            # max certified upper bound over terminal boxes
    while True:
        rounds += 1
        U = box_upper(lo, hi, acts, obs, A); evaluated += len(U)
        centre = 0.5 * (lo + hi)
        if train is None:
            Lc = box_point(centre, acts, obs, A)
        else:
            ok = box_point(centre, train[0], train[1], A) >= math.exp(train[2])           # centre certified inside the confidence set
            Lc = np.where(ok, box_point(centre, acts, obs, A), 0.0)
        L_best = max(L_best, float(Lc.max()))
        keep = U >= L_best
        if train is not None:
            Utr = box_upper(lo, hi, train[0], train[1], A); keep &= Utr >= math.exp(train[2])
        lo, hi, U = lo[keep], hi[keep], U[keep]
        if len(U) == 0:
            break
        Umax = max(float(U.max()), done_U)
        if L_best > 0 and math.log(Umax) - math.log(L_best) <= log_tol:
            done_U = Umax; lo = hi = lo[:0]; break
        if evaluated >= max_boxes or time.perf_counter() - t0 > time_limit:
            done_U = Umax; break
        w = hi - lo; dim = w.argmax(1); idx = np.arange(len(lo))
        mid = 0.5 * (lo[idx, dim] + hi[idx, dim])
        lo2, hi2 = lo.copy(), hi.copy(); hi[idx, dim] = mid; lo2[idx, dim] = mid
        lo = np.concatenate([lo, lo2]); hi = np.concatenate([hi, hi2])
    Ufinal = max(done_U, float(box_upper(lo, hi, acts, obs, A).max()) if len(lo) else done_U)
    conv = L_best > 0 and math.log(Ufinal) - math.log(L_best) <= log_tol + 1e-12
    return dict(L_lo=L_best, U=Ufinal, boxes=evaluated, rounds=rounds, seconds=time.perf_counter() - t0,
                gap=(math.log(Ufinal) - math.log(L_best)) if L_best > 0 else float("inf"), converged=bool(conv))
