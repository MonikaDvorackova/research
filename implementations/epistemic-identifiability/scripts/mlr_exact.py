"""Exact rational computation of the reflecting-walk observer's periodic stationary laws (Fractions; no floating point).
phase_laws(m,K,c) -> {'+': [nu_{+,0..K-1}], '-': [...]} with nu_{h,j} = law at the start of phase j (phase 0 informative).  c is a Fraction."""
from fractions import Fraction as Fr
import sympy as sp

def kernel(m, p):
    P = [[Fr(0)] * m for _ in range(m)]
    for i in range(m):
        P[i][min(i + 1, m - 1)] += p; P[i][max(i - 1, 0)] += 1 - p
    return P

def vecmat(v, M): return [sum(v[i] * M[i][j] for i in range(len(v))) for j in range(len(M[0]))]
def matmul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def stationary(M):
    n = len(M); S = sp.Matrix(n, n, lambda i, j: sp.Rational(M[i][j].numerator, M[i][j].denominator))
    A = (S.T - sp.eye(n)); A = A.row_insert(n, sp.ones(1, n)); b = sp.zeros(n, 1).row_insert(n, sp.Matrix([1]))
    sol = A.gauss_jordan_solve(b)[0]
    return [Fr(int(sp.numer(x)), int(sp.denom(x))) for x in sol]

def phase_laws(m, K, c):
    out = {}; B = kernel(m, Fr(1, 2))
    for h, ch in (("+", c), ("-", -c)):
        A = kernel(m, Fr(1, 2) + ch); Per = A
        for _ in range(K - 1): Per = matmul(Per, B)
        v = stationary(Per); ph = [v]; x = vecmat(v, A); ph.append(x)
        for _ in range(K - 2): x = vecmat(x, B); ph.append(x)
        out[h] = ph[:K]
    return out
