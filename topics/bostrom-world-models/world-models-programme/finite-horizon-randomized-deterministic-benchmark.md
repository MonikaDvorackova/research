# Finite-horizon randomized advantage: numerical full deterministic benchmark

Date: 2026-11-06. Scope: m=3, K=2, c=1/5, common uniform phase-zero initialization, phase-averaged readout. Numerical investigation; finite-horizon stochastic family optimum is numerical, not certified global optimum.

For each rule f0,f1 in {0,1,2}^{3} (729 total), build deterministic transition matrices T0,T1, B=(T0+T1)/2, A_h=(1/2-h*c)T0+(1/2+h*c)T1. Let u=(1/3,1/3,1/3) and mu_h^(n)=u(A_h B)^n(I+A_h)/2. TV_n=0.5*sum_i |mu_+^(n)(i)-mu_-^(n)(i)|. The deterministic benchmark is the maximum over all 729 rules, **including reducible ones**, with the same initialization. Independently, optimize epsilon in [0,1] numerically within the explicit stochastic family T0=[[1-e,e,0],[0,0,1],[0,0,1]], T1=[[1,0,0],[1,0,0],[0,e,1-e]].

| n | epsilon (family optimum, approximate) | family TV | max deterministic TV |
|---:|---:|---:|---:|
| 0 | 1 (boundary) | 0.133333333 | 0.200000000 |
| 1 | 1 (boundary) | 0.233333333 | 0.233333333 |
| 2 | 0.710118 | 0.268643469 | 0.259666667 |
| 5 | 0.427197 | 0.314176762 | 0.271031458 |
| 10 | 0.274013 | 0.342621245 | 0.271490807 |
| 20 | 0.169273 | 0.363784990 | 0.271493213 |
| 50 | 0.085531 | 0.381569722 | 0.271493213 |
| 100 | 0.049652 | 0.389342318 | 0.271493213 |
| 500 | 0.013156 | 0.397231739 | 0.271493213 |
| 1000 | 0.007274 | 0.398483745 | 0.271493213 |

At n=2, the deterministic winner is the reflecting walk f0=(0,0,1), f1=(1,2,2). At n=0, one deterministic winner is f0=(0,0,0), f1=(1,1,1); at n=1, one winner is f0=(0,0,1), f1=(1,1,2). The n=0 phase average includes a readout before any full period and should not be interpreted as 'zero observations'.

**Conclusion:** the explicit randomized family beats **every deterministic three-state rule** at n=2 and the other sampled n≥2, with common initialization. This does not prove a universal claim for all n or all c, and does not prove the stochastic optimum. In particular, the family is worse than the best deterministic observer at n=0 and ties it at n=1.

**Independent numerical reproducer:**
```python
import itertools
import numpy as np
from scipy.optimize import minimize_scalar
c=0.2; u=np.ones(3)/3
def tv(T0,T1,n):
    B=(T0+T1)/2
    laws=[]
    for h in (1,-1):
        A=(0.5-h*c)*T0+(0.5+h*c)*T1
        laws.append(u@np.linalg.matrix_power(A@B,n)@(np.eye(3)+A)/2)
    return np.abs(laws[0]-laws[1]).sum()/2
def stochastic(e,n):
    T0=np.array([[1-e,e,0],[0,0,1],[0,0,1.]])
    T1=np.array([[1,0,0],[1,0,0],[0,e,1-e]])
    return tv(T0,T1,n)
for n in (0,1,2,5,10,20,50,100,500,1000):
    vals=[]
    for rule in itertools.product(range(3),repeat=6):
        T=[]
        for y in (0,1):
            M=np.zeros((3,3))
            M[np.arange(3),rule[3*y:3*y+3]]=1
            T.append(M)
        vals.append(tv(*T,n))
    grid=np.linspace(0,1,1001)
    i=max(range(len(grid)),key=lambda j:stochastic(grid[j],n))
    a=max(0,grid[i]-0.003);b=min(1,grid[i]+0.003)
    opt=minimize_scalar(lambda e:-stochastic(e,n),bounds=(a,b),method='bounded',options={'xatol':1e-13})
    print(n,grid[i],opt.x,-opt.fun,max(vals))
```

Caution: scipy bounded optimization near endpoints does not return the exact endpoint; evaluate e=0 and e=1 separately. Numerical grid plus local optimization is not a certificate of global optimality within the continuous epsilon family; exact deterministic finite enumeration is a finite search with floating-point evaluations. For a rigorous finite-horizon separation, compute exact rational TV at e=7/10, n=2 and exact rational TV for all 729 deterministic rules, then compare rational fractions.

**Next:** build a formal exact finite-horizon n=2 certificate, study finite-horizon epsilon optimization analytically, and assess whether n>=2 randomization advantage holds at all c.