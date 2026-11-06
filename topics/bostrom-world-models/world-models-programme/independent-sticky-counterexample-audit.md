# Independent exact audit: sticky observer defeats the reflecting walk

**Date:** 2026-11-06. **Status:** Independently reconstructed and verified in exact rational arithmetic, using SymPy, the m=3, K=2, c=1/5 counterexample stated in \`memory-hierarchy-and-walk-nonoptimality.md\`. This is a constructive disproof of reflecting-walk optimality **within the class of time-homogeneous stochastic three-state observers with independent transition randomness**. It does not establish the optimum, nor disprove optimality in a restricted class of deterministic update maps.

## Model and admissibility

Let memory states be 0,1,2. An observer always probes a binary signal and updates memory with a row-stochastic kernel T_y depending only on its current memory and the observed y∈{0,1}. The kernels are time homogeneous and have no access to the informative phase. The observer may use internal randomness. The signal is informative at one of K=2 phases, with P_+(Y=1)=1/2+c and P_−(Y=1)=1/2−c, and fair at the other phase. The decision uses the phase-averaged stationary memory law. We take c=1/5.

For ε=1/10000 and ℓ=1/30, define

\[
T_0=\begin{pmatrix}
\varepsilon&1-2\varepsilon&\varepsilon\\
\varepsilon&1-2\varepsilon&\varepsilon\\
\ell&\varepsilon&1-\ell-\varepsilon
\end{pmatrix},
\quad
T_1=\begin{pmatrix}
\varepsilon&\varepsilon&1-2\varepsilon\\
\ell&1-\ell-\varepsilon&\varepsilon\\
\varepsilon&\varepsilon&1-2\varepsilon
\end{pmatrix}.
\]

All entries are strictly positive, and each row sums to one, so these define admissible irreducible aperiodic stochastic update kernels.

Set B=(T_0+T_1)/2 and A_±=(1/2∓c)T_0+(1/2±c)T_1. Let v_± be the unique normalized stationary row of P_±=A_±B. The phase averages are μ_±=v_±(I+A_±)/2. Direct exact rational linear algebra gives

\[
\boxed{
\mathrm{TV}_{\rm sticky}(3,2,1/5)
=\frac{56152526035739308}{144699267323882167}
\approx0.38806365142162336.
}
\]

For the deterministic reflecting walk with T_0 moving down and T_1 moving up, using exactly the same phase averaging,

\[
\boxed{
\mathrm{TV}_{\rm walk}(3,2,1/5)=\frac{60}{221}
\approx0.27149321266968324.
}
\]

The difference is

\[
\boxed{
\mathrm{TV}_{\rm sticky}-\mathrm{TV}_{\rm walk}
=\frac{286750170343496696}{2459887544505996839}
>0.
}
\]

This is an **exact rational certificate**. The advantage is approximately 42.94% relative to the walk.

## Independently executed verification

The verification reconstructed T_0 and T_1 from the rows specified in the previous note, built the informative and fair kernels, solved each stationary system by replacing one row of P^T−I with the normalization constraint, and calculated TV of the two phase averages using exact SymPy rationals. A separate reflecting-walk construction returned 60/221. The exact difference was factored and shown positive. This did not reuse a stored result file or floating-point stationary solver.

Minimal reproduction:

~~~python
import sympy as s

eps, ell, c = s.Rational(1,10000), s.Rational(1,30), s.Rational(1,5)
T0 = s.Matrix([[eps,1-2*eps,eps],
               [eps,1-2*eps,eps],
               [ell,eps,1-ell-eps]])
T1 = s.Matrix([[eps,eps,1-2*eps],
               [ell,1-ell-eps,eps],
               [eps,eps,1-2*eps]])

def stationary(P):
    M = P.T-s.eye(P.rows)
    M[P.rows-1,:] = s.ones(1,P.rows)
    rhs = s.zeros(P.rows,1)
    rhs[P.rows-1] = 1
    return (M.inv()*rhs).T

def phase_average(T0,T1,c):
    B=(T0+T1)/2
    return [
        (lambda A: (lambda v: v*(s.eye(B.rows)+A)/2)(
            stationary(A*B)))(
            (s.Rational(1,2)+h*c)*T1+(s.Rational(1,2)-h*c)*T0)
        for h in (1,-1)
    ]

def tv(laws):
    return s.factor(sum(abs(x) for x in laws[0]-laws[1])/2)

sticky = tv(phase_average(T0,T1,c))
W0=s.Matrix([[1,0,0],[1,0,0],[0,1,0]])
W1=s.Matrix([[0,1,0],[0,0,1],[0,0,1]])
walk=tv(phase_average(W0,W1,c))
assert sticky==s.Rational(56152526035739308,144699267323882167)
assert walk==s.Rational(60,221)
assert sticky>walk
print("sticky",sticky,"walk",walk,"advantage",s.factor(sticky-walk))
~~~

## Consequences and restrictions

1. The reflecting walk is **not optimal** among all stochastic time-homogeneous three-state observers, even when the hidden informative phase has period two.
2. The construction uses nontrivial randomization in T_0 and T_1. It does **not** show that the walk is suboptimal within the narrower class of deterministic three-state update maps.
3. The result does not identify the global optimum over stochastic automata; it only provides a certified lower bound for that optimum.
4. It does not invalidate the reflecting-walk crossover theorem, which is explicitly a result for one observer construction.
5. The next rigorous question is whether deterministic automata can outperform the reflecting walk under the same hidden-phase model, and how the true stochastic-automaton optimum depends on (m,K,c).
6. Novelty relative to Hellman–Cover-style finite-memory hypothesis testing is not established.
