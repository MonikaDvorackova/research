# Complete exact enumeration including reducible deterministic observers

**2026-11-06. Status: independently executed exact rational enumeration for m=3, K=2, c=1/5 under an explicitly specified initialization convention.** This note extends \`exhaustive-deterministic-three-state-k2.md\`. It does not assert the all-c result for reducible automata.

## Why reducibility matters

For a deterministic clockless three-state observer, two update maps f_0,f_1 map {0,1,2} to itself. There are 3^6=729 labeled pairs. The one-period kernel P_h=A_hB may be reducible; in that case a generic stationary solution is not uniquely determined. Merely selecting an arbitrary stationary vector would make the optimization ill-defined.

We impose a **common phase-zero uniform initialization** u=(1/3,1/3,1/3), independent of the hypothesis. For each h, define

\[
v_h=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}uP_h^n.
\]

This Cesàro limit exists for every finite Markov chain, including reducible and periodic chains. The phase-average memory law for K=2 is μ_h=v_h(I+A_h)/2.

## Exact projection without matrix-power approximations

Let H be any matrix whose columns form a basis for the right nullspace of P−I (harmonic vectors). The Cesàro limit v is the **unique** row vector satisfying

\[
v(P-I)=0,\qquad vH=uH.
\]

The first condition is stationarity; the second preserves every harmonic observable, since P H=H implies uP^nH=uH for all n. These conditions characterize the stationary projection even for multiple recurrent classes. Thus we can calculate v by an exact rational linear solve, with no floating-point convergence tolerance or arbitrary choice of stationary law.

## Theorem: all 729 deterministic rules at one parameter point

Take m=3, K=2, c=1/5, and uniform phase-zero initialization. Enumerating all 729 pairs (f_0,f_1) with exact rational matrices gives

\[
\boxed{\max_{f_0,f_1\text{ deterministic}}\operatorname{TV}(\mu_+,\mu_-)=\frac{60}{221}.}
\]

The maximum is attained by exactly six labeled rules, all relabelings of the reflecting walk:

\`\`\`
(0,0,1; 1,2,2)
(0,2,0; 2,1,1)
(1,1,0; 2,0,2)
(1,2,2; 0,0,1)
(2,0,2; 1,1,0)
(2,1,1; 0,2,0)
\`\`\`

Of the 729 rules, 290 have irreducible two-step support. Exactly 82 have a stationary right-eigenspace of dimension greater than one (more than one recurrent class). The remaining reducible rules have a unique stationary distribution supported on their recurrent class(es), and transient states do not prevent uniqueness. Across all 729 rules, exactly 22 distinct rational TV scores occur under this convention. The next highest score is 140/621.

**Comparison with randomized updates:** the earlier sticky-decision observer has TV≈0.388064 > 60/221≈0.271493. Therefore stochastic update randomness gives a strict improvement over **every deterministic three-state observer** at K=2, c=1/5 under this common initialization convention.

## Reproducible exact code

\`\`\`python
import itertools
import sympy as s

c=s.Rational(1,5)
I=s.eye(3)
u=s.ones(1,3)/3

def stationary_cesaro(P,u):
    H=s.Matrix.hstack(*(P-I).nullspace())
    M=(P.T-I).col_join(H.T)
    rhs=s.zeros(3,1).col_join(H.T*u.T)
    sol=s.linsolve((M,rhs))
    assert len(sol)==1
    return s.Matrix(list(next(iter(sol)))).T

scores=[]
for rule in itertools.product(range(3),repeat=6):
    T=[]
    for y in range(2):
        mat=s.zeros(3)
        for i in range(3):
            mat[i,rule[3*y+i]]=1
        T.append(mat)
    B=(T[0]+T[1])/2
    laws=[]
    for h in (1,-1):
        A=(s.Rational(1,2)-h*c)*T[0]+(s.Rational(1,2)+h*c)*T[1]
        v=stationary_cesaro(A*B,u)
        laws.append(v*(I+A)/2)
    tv=s.factor(sum(abs(laws[0][i]-laws[1][i]) for i in range(3))/2)
    scores.append((tv,rule))

best=max(tv for tv,_ in scores)
winners=[rule for tv,rule in scores if tv==best]
assert len(scores)==729
assert best==s.Rational(60,221)
assert len(winners)==6
assert len(set(tv for tv,_ in scores))==22
assert max(tv for tv,_ in scores if tv<best)==s.Rational(140,621)
print(best,winners)
\`\`\`

This exact computation was independently executed locally, not inferred from prior notes. A separate numerical power-iteration calculation with lazy kernels (I+P)/2 returned the same maximum and six maximizers.

## Scope

- This is a **complete finite computer-assisted result** for one parameter point and the uniform phase-zero initialization convention.
- The prior all-c theorem applies only to **irreducible** deterministic automata; this note does not extend its symbolic certificate to all c for reducible automata.
- Allowing an observer-specific or hypothesis-dependent initialization would change the problem and is not permitted here.
- Stochastic transitions can outperform the deterministic optimum; their global optimum remains unknown.
- Novelty versus finite-memory testing literature has not been established.

## Next concrete task

Symbolically classify the 439 reducible deterministic rules for all 0<c<1/2 using the exact Cesàro projector. Compare their rational TV functions to W(c)=12c/(9−4c²), and combine with the previously certified 290-rule irreducible theorem to obtain an all-c theorem for all 729 deterministic rules.
