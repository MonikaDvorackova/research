# Noncommuting long-time and small-noise limits

Date: 2026-11-06. Independently verified by exact symbolic matrix multiplication. Scope: the explicit three-state randomized family, K=2, common uniform phase-zero initialization.

For 0<c<1/2, let

T0(e) = [[1-e,e,0],[0,0,1],[0,0,1]],
T1(e) = [[1,0,0],[1,0,0],[0,e,1-e]].

Set B=(T0+T1)/2, A_h=(1/2-h*c)T0+(1/2+h*c)T1, P_h=A_h B. Let u=(1/3,1/3,1/3), v_h^(n,e)=u P_h(e)^n, and the period-phase averaged law mu_h^(n,e)=v_h^(n,e)(I+A_h(e))/2. Define TV_(n,e)=TV(mu_+^(n,e),mu_-^(n,e)).

**Theorem: the limits do not commute.**

For each e>0 the period chain is irreducible and aperiodic; its unique stationary phase-averaged TV is

F(c,e)=4*c*(4-e)/(8+2*e-e^2-8*c^2*e+4*c^2*e^2).

Therefore lim_(e→0+) lim_(n→infinity) TV_(n,e)=2c.

At e=0, direct exact multiplication yields

P_h(0) = [[1,0,0],[1/2+h*c,0,1/2-h*c],[0,0,1]].

Thus u P_h(0)^n = (1/2+h*c/3, 0, 1/2-h*c/3) for **every n≥1**. Because T0(0) and T1(0) leave both absorbing states 0 and 2 fixed, phase averaging does not alter this distribution. Hence TV_(n,0)=2c/3 for every n≥1.

For each fixed n, P_h(e)^n and A_h(e) are polynomial functions of e, so TV_(n,e)→TV_(n,0) as e→0+. Consequently

lim_(n→infinity) lim_(e→0+) TV_(n,e)=2c/3.

The discrepancy is 4c/3, nonzero for every c>0. For c=1/5 the two limits are 2/5 and 2/15.

**Interpretation.** The stationary advantage 2c of this near-reducible family requires the observation horizon to grow with 1/e. The previous spectral calculation found lambda_2=1-e+O(e^2), consistent with this mechanism. The present result establishes the noncommuting limits exactly; it does not establish a universal finite-time minimax lower bound.

**Reproducer:**
```python
import sympy as s
c=s.symbols('c',positive=True)
u=s.ones(1,3)/3
T0=s.Matrix([[1,0,0],[0,0,1],[0,0,1]])
T1=s.Matrix([[1,0,0],[1,0,0],[0,0,1]])
B=(T0+T1)/2
for h in (1,-1):
    A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
    P=A*B
    target=s.Matrix([[s.Rational(1,2)+h*c/3,0,s.Rational(1,2)-h*c/3]])
    assert u*P==target
    assert target*P==target
    assert target*(s.eye(3)+A)/2==target
```

Next: calculate finite-n crossover on the scaling n*e→t, which could produce a quantitative observation-horizon/performance curve. Do not infer a sharp global stochastic upper bound from this family.