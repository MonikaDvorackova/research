"""Exact structured baselines over GF(2): Berlekamp-Massey (linear class) and degree-<=2 polynomial recurrence fit (nonlinear class)."""
from __future__ import annotations
import itertools
import numpy as np


def berlekamp_massey(s):
    """Linear complexity and connection polynomial of a bit sequence (list/array of 0/1)."""
    n = len(s); c = [1] + [0] * n; b = [1] + [0] * n; L, m = 0, -1
    for i in range(n):
        d = s[i]
        for j in range(1, L + 1): d ^= c[j] & s[i - j]
        if d:
            t = c[:]
            for j in range(0, n - i + m if n - i + m > 0 else 0):
                if i - m + j <= n: c[i - m + j] ^= b[j]
            if 2 * L <= i: L, m, b = i + 1 - L, i, t
    return L, c[:L + 1]


def predict_lfsr(s, L, c):
    """Next bit predicted by connection polynomial c (length L+1): s[t] = XOR_{j=1..L} c[j] s[t-j]."""
    x = 0
    for j in range(1, L + 1): x ^= c[j] & s[len(s) - j]
    return x


def _monomials(L, degree):
    mons = [()]
    for d in range(1, degree + 1): mons += list(itertools.combinations(range(L), d))
    return mons


def _design(history, mons):
    """history [M,L] of previous bits (column j = lag j+1) -> [M,len(mons)] monomial values."""
    X = np.ones((history.shape[0], len(mons)), dtype=np.uint8)
    for k, m in enumerate(mons):
        for j in m: X[:, k] &= history[:, j]
    return X


def gf2_solve(A, y):
    """Solve A x = y over GF(2); returns one solution or None if inconsistent."""
    A = A.copy().astype(np.uint8); y = y.copy().astype(np.uint8); M, N = A.shape
    Ab = np.concatenate([A, y[:, None]], 1); row = 0; piv = []
    for col in range(N):
        sel = np.nonzero(Ab[row:, col])[0]
        if len(sel) == 0: continue
        r = row + sel[0]; Ab[[row, r]] = Ab[[r, row]]
        mask = Ab[:, col].astype(bool); mask[row] = False
        Ab[mask] ^= Ab[row]; piv.append(col); row += 1
        if row == M: break
    if np.any(Ab[row:, N]): return None
    x = np.zeros(N, dtype=np.uint8)
    for i, col in enumerate(piv): x[col] = Ab[i, N]
    return x


def fit_recurrence(bits, L, degree, n_eq=None):
    """Fit s[t] = poly_deg(s[t-1..t-L]) over GF(2) from a long bit sequence (or list of sequences). Returns (mons, coef) or None."""
    seqs = bits if isinstance(bits, list) else [bits]
    H, Y = [], []
    for s in seqs:
        s = np.asarray(s, dtype=np.uint8)
        for t in range(L, len(s)):
            H.append(s[t - L:t][::-1]); Y.append(s[t])
    H = np.array(H, dtype=np.uint8); Y = np.array(Y, dtype=np.uint8)
    mons = _monomials(L, degree)
    X = _design(H, mons)
    if n_eq is not None: X, Y = X[:n_eq], Y[:n_eq]
    coef = gf2_solve(X, Y)
    return None if coef is None else (mons, coef)


def predict_recurrence(fit, hist):
    """hist [M,L] previous bits (col j = lag j+1) -> predicted bits."""
    mons, coef = fit
    return (_design(np.asarray(hist, dtype=np.uint8), mons).astype(np.int64) @ coef.astype(np.int64)) % 2
