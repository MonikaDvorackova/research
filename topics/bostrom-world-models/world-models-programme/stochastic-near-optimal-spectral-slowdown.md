# Exact spectral slowdown of the three-state stochastic observer

Date: 2026-11-06. Corrected 2026-11-06 after a fresh exact SymPy audit: the characteristic polynomial previously contained an incorrect (1-epsilon)^2 factor; the correct factor is (2-epsilon)^2. Reproduction assertion now passes. This is a result for the explicit family, not a global mixing-time theorem.

For 0<c<1/2 and 0<epsilon<1, let T0=[[1-epsilon,epsilon,0],[0,0,1],[0,0,1]] and T1=[[1,0,0],[1,0,0],[0,epsilon,1-epsilon]]. Put B=(T0+T1)/2, A_h=(1/2-h*c)*T0+(1/2+h*c)*T1 and P_h=A_h*B.

**Exact theorem.** For either h=+1 or -1, the characteristic polynomial is

    det(xI-P_h)=(x-1)*(x^2-x+epsilon*x-epsilon^2*x/2+epsilon^2*(2-epsilon)^2*(1-4*c^2)/16).

The nontrivial eigenvalue approaching 1 as epsilon decreases is lambda_2=1-epsilon+O_c(epsilon^2). Thus the spectral relaxation gap is epsilon+O_c(epsilon^2) and the characteristic relaxation scale is asymptotically 1/epsilon periods, i.e. 2/epsilon observations. This is not a sharp mixing-time bound with uniform constants.

The previously verified stationary TV is

    F(c,epsilon)=4*c*(4-epsilon)/(8+2*epsilon-epsilon^2-8*c^2*epsilon+4*c^2*epsilon^2).

An exact subtraction gives

    2*c-F=2*c*epsilon*(4-8*c^2-epsilon+4*c^2*epsilon)/(8+2*epsilon-epsilon^2-8*c^2*epsilon+4*c^2*epsilon^2)
         =c*(1-2*c^2)*epsilon+O_c(epsilon^2).

Therefore (2*c-F)/(1-lambda_2) tends to c*(1-2*c^2). This is a within-family performance/spectral-relaxation tradeoff, not a universal lower bound on observation complexity.

Independent exact checkpoint at c=1/5, epsilon=1/1000: TV=79980000/200041979.

**Reproducer (SymPy):**
```python
import sympy as s
c,e,x=s.symbols('c e x',positive=True)
T0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
T1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
B=(T0+T1)/2
q=x*x-x+e*x-e*e*x/2+e*e*(2-e)**2*(1-4*c*c)/16
for h in (1,-1):
 A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
 assert s.factor((A*B).charpoly(x).as_expr()-(x-1)*q)==0
D=8+2*e-e**2-8*c*c*e+4*c*c*e**2
F=4*c*(4-e)/D
assert s.simplify(2*c-F-2*c*e*(4-8*c*c-e+4*c*c*e)/D)==0
assert s.limit((2*c-F)/e,e,0,dir='+')==c*(1-2*c*c)
```

Prior art: Hellman and Cover (1970), Learning with Finite Memory, DOI 10.1214/aoms/1177696958; Hellman and Cover (1971), On Memory Saved by Randomization, https://www-ee.stanford.edu/~hellman/publications/09.pdf. Neither the novelty nor global stochastic optimum is established.