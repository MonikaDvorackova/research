# Exact five- and six-state separation at hidden period K=2

**Status (2026-11-05):** Exact symbolic derivation for the specified reflecting-walk automata. Not an optimality theorem, not externally reviewed, and novelty is unverified.

## Model

Let the hidden period be K=2. At the informative phase the signal is Bernoulli(1/2±c), 0<c<1/2, and at the other phase Bernoulli(1/2). The time-homogeneous clockless observer has m states {0,…,m−1}; after signal 1 it increments with reflection at the top, and after signal 0 decrements with reflection at zero. The decision is based only on current memory. Performance is total variation of the phase-averaged periodic stationary memory laws.

Let B=T(1/2), D=∂T/∂p, π=(1/m,…,1/m), Π=1π, Z=(I−B+Π)^{-1}. For h∈{+1,−1}, solve v_h=v_h(B+h c D)B with v_h1=1. The exact phase-average response identity gives

μ_+−μ_−=(c/2)(v_++v_−)DZ.

All calculations below use exact rational functions in c.

## Theorem: strict m=4,5,6 hierarchy for K=2

For every 0<c<1/2,

\[
\boxed{\mathrm{TV}_4(2,c)=2c,}
\]

\[
\boxed{\mathrm{TV}_5(2,c)=\frac{4c(4c^2+15)}{16c^4+24c^2+25},}
\]

\[
\boxed{\mathrm{TV}_6(2,c)=\frac{c(9-4c^2)}{3+4c^2}.}
\]

Furthermore,

\[
\boxed{\mathrm{TV}_6(2,c)>\mathrm{TV}_5(2,c)>\mathrm{TV}_4(2,c)}
\]

throughout the open bias interval.

### Proof

Solving the finite linear systems symbolically and using reflection symmetry gives for m=5 the signed phase-averaged difference vector

\[
\mu_+-\mu_-=\frac{1}{(4c^2-4c+5)(4c^2+4c+5)}
(-8c(4c^2+5),\,4c(4c^2-5),\,0,\,4c(5-4c^2),\,8c(4c^2+5)).
\]

For m=6 the difference vector is

\[
\mu_+-\mu_-=\frac{c}{4c^2+3}
(-(4c^2+5),\,4c^2-3,\,4c^2-1,\,1-4c^2,\,3-4c^2,\,4c^2+5).
\]

The signs are fixed on 0<c<1/2: negative on the lower states, positive on the upper states. Total variation is therefore the sum of the positive entries, yielding the displayed rational expressions.

For the first strict comparison, direct subtraction and factorization gives

\[
\mathrm{TV}_5-\mathrm{TV}_4=
\frac{2c(1-4c^2)(4c^2+5)}
{(4c^2-4c+5)(4c^2+4c+5)}>0.
\]

For the second,

\[
\mathrm{TV}_6-\mathrm{TV}_5=
\frac{c(1-4c^2)(16c^4+8c^2+45)}
{(4c^2+3)(4c^2-4c+5)(4c^2+4c+5)}>0.
\]

Every denominator is strictly positive, as are c, 1−4c² and the remaining factors. This completes the proof. ∎

## Reproducibility

The following SymPy code derives the signed vectors and checks both strict-difference factorizations:

~~~python
import sympy as s
c = s.symbols("c", positive=True)

def matrices(m):
    B, D = s.zeros(m), s.zeros(m)
    for i in range(m):
        B[i, max(i-1, 0)] += s.Rational(1, 2)
        B[i, min(i+1, m-1)] += s.Rational(1, 2)
        D[i, max(i-1, 0)] -= 1
        D[i, min(i+1, m-1)] += 1
    return B, D

def exact_tv(m):
    B, D = matrices(m)
    Z = (s.eye(m) - B + s.ones(m)/m).inv()
    vs = []
    for h in (1, -1):
        P = (B + h*c*D)*B
        M = P.T - s.eye(m)
        M[m-1, :] = s.ones(1, m)
        rhs = s.zeros(m, 1)
        rhs[m-1] = 1
        vs.append(M.inv()*rhs)
    delta = s.simplify((vs[0]+vs[1]).T*D*Z*c/2)
    tv = s.factor(sum(delta[0, j] for j in range(m//2, m)))
    return tv, [s.factor(delta[0, j]) for j in range(m)]

tv4, _ = exact_tv(4)
tv5, d5 = exact_tv(5)
tv6, d6 = exact_tv(6)
assert s.simplify(tv4-2*c) == 0
assert s.simplify(tv5-4*c*(4*c**2+15)/(16*c**4+24*c**2+25)) == 0
assert s.simplify(tv6-c*(9-4*c**2)/(3+4*c**2)) == 0
print("TV5-TV4 =", s.factor(tv5-tv4))
print("TV6-TV5 =", s.factor(tv6-tv5))
print("delta5 =", d5)
print("delta6 =", d6)
~~~

## Interpretation and caveats

This establishes a strict hierarchy of **achievable** discrimination for one fixed update rule, K=2, across m=4,5,6. It does not establish monotonicity for every m, every K, or the optimal discrimination among all m-state automata. At the boundary c→1/2 the differences approach zero, so the strict inequalities correctly exclude c=1/2.

The formulas follow from finite-state stationary Markov-chain algebra and may be known consequences of prior theory. A primary-literature novelty review remains essential before any publication claim.

**Next:** derive a general K=2 expression in m, or investigate the joint K/m→α regime; independently audit earlier two-state optimality assumptions.
