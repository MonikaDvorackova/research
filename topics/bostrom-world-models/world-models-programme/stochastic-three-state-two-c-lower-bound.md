# A three-state stochastic family approaching TV = 2c

Date: 2026-11-06. **Status:** exact symbolic stationary-law calculation, independently checked in SymPy. Stronger lower bound than the earlier sticky observer. This is a supremum statement, not an attained maximum or a global optimality proof.

## Model

Period K=2 with one informative Bernoulli observation of bias ±c, 0<c<1/2, followed by a fair observation; observer has m=3 states, no clock. Set B=(T0+T1)/2, A_h=(1/2−hc)T0+(1/2+hc)T1, P_h=A_hB, v_hP_h=v_h, and μ_h=v_h(I+A_h)/2. TV=1/2∑|μ_+−μ_-|.

## Explicit stochastic family

For 0<ε<1 define

\[
T_0=\begin{pmatrix}
1-\varepsilon&\varepsilon&0\\
0&0&1\\
0&0&1
\end{pmatrix},
\quad
T_1=\begin{pmatrix}
1&0&0\\
1&0&0\\
0&\varepsilon&1-\varepsilon
\end{pmatrix}.
\]

Both P_h are irreducible for every ε>0 and 0<c<1/2: the positive transition graph contains paths 0→1→2→0, and all support probabilities are positive on those paths. Consequently each stationary law is unique.

Exact symbolic solution of the two stationary linear systems gives

\[
\mu_+-\mu_-=
\left(
\frac{4c(4-\varepsilon)}{D(c,\varepsilon)},
0,
-\frac{4c(4-\varepsilon)}{D(c,\varepsilon)}
\right),
\]
where
\[
D(c,\varepsilon)=8+2\varepsilon-\varepsilon^2-8c^2\varepsilon+4c^2\varepsilon^2.
\]
The denominator is positive throughout the domain (it is the denominator arising from positive stationary probabilities; directly D≥8−2ε−ε²>5 for 0<ε<1 and c²<1/4). Therefore

\[
\boxed{\operatorname{TV}(c,\varepsilon)=\frac{4c(4-\varepsilon)}{D(c,\varepsilon)}}.
\]

Taking ε→0+ yields
\[
\boxed{\lim_{\varepsilon\to0^+}\operatorname{TV}(c,\varepsilon)=2c.}
\]

Thus \(\sup_{T_0,T_1}\mathrm{TV}\ge 2c\) for m=3, K=2, all 0<c<1/2. This family improves upon the previous fixed sticky construction for sufficiently small ε. At c=1/5 and ε=1/1000 the exact expression is approximately 0.39981608060376167.

**Important discontinuity:** At ε=0 the transition kernels are reducible and the stationary law depends on initialization. The limiting score 2c is approached as ε→0+, and must not be presented as necessarily attained by the ε=0 automaton.

## Exact SymPy reproducer

\`\`\`python
import sympy as s
c,e=s.symbols("c e",positive=True)
T0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
T1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
B=(T0+T1)/2
mu=[]
for h in (1,-1):
    A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
    M=(A*B).T-s.eye(3)
    M[2,:]=s.ones(1,3)
    v=(M.inv()*s.Matrix([0,0,1])).T
    mu.append(v*(s.eye(3)+A)/2)
d=[s.factor(mu[0][i]-mu[1][i]) for i in range(3)]
D=8+2*e-e**2-8*c**2*e+4*c**2*e**2
assert all(s.simplify(d[i]-t)==0 for i,t in enumerate(
    [4*c*(4-e)/D,0,-4*c*(4-e)/D]))
assert s.limit(d[0],e,0,dir="+")==2*c
print(d)
\`\`\`

## What this does and does not establish

- A **new explicit lower bound** 2c for the supremum of three-state randomized observer TV at K=2. No claim of novelty relative to prior art.
- The previously proved full deterministic optimum is 12c/(9−4c²), which is strictly less than 2c throughout 0<c<1/2 because 2c−12c/(9−4c²)=2c(3−4c²)/(9−4c²)>0.
- This improves the quantitative randomization separation for every bias.
- The earlier universal upper bound tanh(3 atanh(2c)) remains much larger than 2c. Equality of the stochastic supremum with 2c is **not proved**.
- A numerical differential-evolution search with 12 unconstrained stick-breaking parameters found TV≈0.39906 at c=1/5, consistent with but not proving the conjecture sup=2c. The exact family, not the optimizer, is the rigorous result.

## Research next steps

Seek a sharp m=3,K=2 upper bound, ideally TV≤2c for all stochastic T0,T1, including sparse irreducible matrices. Analyze near-reducible metastability and mixing time: ε→0 causes long transients, so asymptotic discrimination and finite-time utility may differ sharply. Compare the resulting tradeoff to Hellman–Cover finite-memory testing.
