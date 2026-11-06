# All-bias symbolic separation from the reflecting-walk benchmark at n=2

Date: 2026-11-06. Exact algebra; limited scope explicitly stated.

Model: m=3, K=2, common uniform phase-zero initialization u=(1/3,1/3,1/3), phase-averaged readout after n=2 complete periods, Bernoulli bias 0<c<1/2. For a pair of transition matrices define B=(T0+T1)/2, A_h=(1/2-hc)T0+(1/2+hc)T1 and mu_h=u(A_h B)^2(I+A_h)/2.

Consider the fixed stochastic rule T0=[[3/10,7/10,0],[0,0,1],[0,0,1]], T1=[[1,0,0],[1,0,0],[0,7/10,3/10]]. Exact symbolic calculation gives mu_+-mu_-=(d_s,0,-d_s) with

d_s = c*(563108*c^2+6424571)/4800000.

The reflecting deterministic rule f0=(0,0,1), f1=(1,2,2) has mu_+-mu_-=(-d_d,0,d_d) where

d_d=c*(4*c^2+31)/24.

Thus the **exact strict separation from this particular deterministic rule** is

d_s-d_d = c*(74857-78964*c^2)/1600000 > 0

for every 0<c<1/2, since 78964*c^2<19741<74857.

At c=1/5, d_s=161177383/600000000, d_d=779/3000; the earlier exhaustive exact 729-rule certificate shows d_d is the **global deterministic maximum at that one c**.

IMPORTANT: This calculation **does not yet establish** that the reflecting rule is the global finite-horizon deterministic maximizer for all c. Hence it does not by itself extend the global randomization-advantage theorem to every c. That extension requires an all-bias envelope/certificate over 729 deterministic rules.

Reproducer:
```python
import sympy as s
c=s.symbols('c',positive=True); e=s.Rational(7,10);u=s.ones(1,3)/3
def diff(T0,T1):
 B=(T0+T1)/2
 laws=[]
 for h in (1,-1):
  A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
  laws.append(u*(A*B)**2*(s.eye(3)+A)/2)
 return [s.factor(laws[0][i]-laws[1][i]) for i in range(3)]
T0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
T1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
M0=s.Matrix([[1,0,0],[1,0,0],[0,1,0]])
M1=s.Matrix([[0,1,0],[0,0,1],[0,0,1]])
assert diff(T0,T1)==[c*(563108*c*c+6424571)/4800000,0,-c*(563108*c*c+6424571)/4800000]
assert diff(M0,M1)==[-c*(4*c*c+31)/24,0,c*(4*c*c+31)/24]
assert s.factor(diff(T0,T1)[0]+diff(M0,M1)[0])==c*(74857-78964*c*c)/1600000
print('PASS')
```

Research priorities before submission: (1) certify deterministic all-c finite-horizon envelope; (2) audit previous symbolic formulas and numerical tables; (3) establish literature differentiation from Hellman-Cover and hidden-periodic finite-state testing; (4) write a coherent theorem/proof/limitations manuscript. No simulation-hypothesis claims follow from these theorems.