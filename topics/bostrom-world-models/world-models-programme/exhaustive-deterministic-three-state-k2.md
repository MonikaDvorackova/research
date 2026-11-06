# Exhaustive deterministic three-state observers at K=2, c=1/5

**2026-11-06. Status: exact exhaustive computational certificate within the irreducible deterministic observer class.** This result is parameter-specific; it does not prove deterministic optimality for arbitrary c, K, or m. The earlier sticky-observer counterexample uses stochastic transitions and remains valid.

## Setup

Memory state set {0,1,2}; binary input y∈{0,1}. A deterministic clockless, always-probing observer is a pair of maps f_0,f_1:{0,1,2}→{0,1,2}. There are 3^6=729 labeled automata. Their transition matrices T_y have exactly one 1 per row. Set c=1/5, K=2, B=(T_0+T_1)/2, A_h=(1/2−hc)T_0+(1/2+hc)T_1. For h=±1, let v_h be the stationary row distribution of P_h=A_h B and μ_h=v_h(I+A_h)/2. Score TV=(1/2)∑_i|μ_+(i)−μ_−(i)|.

To avoid ambiguity from multiple stationary distributions, restrict to observers whose two-step chain P_h is irreducible (equivalently, the support of (T_0+T_1)^2 is strongly connected). Because 0<c<1/2, support does not depend on h.

## Exact enumeration result

Of 729 deterministic labeled rules, exactly **290** have irreducible two-step kernels. For every one of these 290, stationary distributions and TV were calculated with exact SymPy rational arithmetic. The maximum is

\[
\boxed{\max_{\text{deterministic, irreducible, }m=3}\operatorname{TV}(\mu_+,\mu_-)=60/221\approx0.271493212669683.}
\]

Exactly **six** labeled rules attain the maximum, all isomorphic to the reflecting walk (permuting memory labels, possibly exchanging input symbols):

\`\`\`
(f0(0),f0(1),f0(2); f1(0),f1(1),f1(2))
(0,0,1; 1,2,2)
(0,2,0; 2,1,1)
(1,1,0; 2,0,2)
(1,2,2; 0,0,1)
(2,0,2; 1,1,0)
(2,1,1; 0,2,0)
\`\`\`

There are exactly 19 distinct rational TV scores among the 290 rules. The second largest is 140/621≈0.225442834138486. Hence the maximum has a strictly positive gap.

The earlier certified stochastic sticky-decision observer achieves

\[
\operatorname{TV}_{\rm sticky}
=\frac{56152526035739308}{144699267323882167}
\approx0.388064
>60/221.
\]

Thus **stochastic update rules strictly outperform every irreducible deterministic three-state rule** at this parameter point.

## Reproducible exact enumeration (Python / SymPy)

\`\`\`python
from itertools import product
from sympy import Matrix, Rational, eye, zeros, ones

c=Rational(1,5)

def strongly_connected(P):
    n=P.rows
    for start in range(n):
        reached={start}
        todo=[start]
        while todo:
            i=todo.pop()
            for j in range(n):
                if P[i,j]!=0 and j not in reached:
                    reached.add(j)
                    todo.append(j)
        if len(reached)!=n:
            return False
    return True

def stationary(P):
    n=P.rows
    M=P.T-eye(n)
    M[n-1,:]=ones(1,n)
    b=zeros(n,1)
    b[n-1]=1
    return (M.inv()*b).T

def score(rule):
    T=[]
    for y in range(2):
        mat=zeros(3,3)
        for i in range(3):
            mat[i,rule[3*y+i]]=1
        T.append(mat)
    B=(T[0]+T[1])/2
    if not strongly_connected((T[0]+T[1])**2):
        return None
    mu=[]
    for h in (1,-1):
        A=(Rational(1,2)-h*c)*T[0]+(Rational(1,2)+h*c)*T[1]
        v=stationary(A*B)
        mu.append(v*(eye(3)+A)/2)
    return sum(abs(mu[0][i]-mu[1][i]) for i in range(3))/2

scores=[(score(rule),rule) for rule in product(range(3),repeat=6)]
scores=[x for x in scores if x[0] is not None]
best=max(x[0] for x in scores)
winners=[rule for value,rule in scores if value==best]
assert len(scores)==290
assert best==Rational(60,221)
assert len(winners)==6
assert len(set(value for value,_ in scores))==19
assert max(value for value,_ in scores if value<best)==Rational(140,621)
print(best,winners)
\`\`\`

## Scope and interpretation

This is a **finite exhaustive proof by exact computation** for irreducible deterministic 3-state observers at K=2, c=1/5. It is not a proof about reducible observers: those may have multiple invariant laws and require a separate convention about initialization, limiting distributions, and admissibility. It does not cover deterministic automata with an additional clock, or stochastic update rules. It demonstrates a concrete randomization advantage relative to the irreducible deterministic class under phase-averaged stationary TV, but does not determine the global stochastic optimum.

**Next:** check reducible deterministic rules under a specified initialization convention, and derive a symbolic-in-c classification of the 290 irreducible rules to test whether the reflecting walk is optimal for all 0<c<1/2 at K=2.
