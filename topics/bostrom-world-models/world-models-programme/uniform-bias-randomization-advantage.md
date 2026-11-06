# Uniform-in-bias randomization advantage for three-state hidden-phase testing

**Date:** 2026-11-06. **Status:** independently derived exact rational formulas using symbolic linear algebra. The sticky-observer part and positivity are self-contained; the comparison to the *global deterministic optimum* invokes the earlier exhaustive symbolic classification of 729 deterministic rules (including the uniform-initialization convention for reducible rules). Not peer reviewed; novelty unverified.

## Model

Three memory states, hidden period K=2, one informative Bernoulli step per period, with bias ±c (0<c<1/2), and one fair step. The observer is time homogeneous, always probes, and may use stochastic state transitions T_0,T_1. Let B=(T_0+T_1)/2, A_h=(1/2−hc)T_0+(1/2+hc)T_1, v_h the unique stationary row of A_h B, and μ_h=v_h(I+A_h)/2. Distinguish hypotheses by TV(μ_+,μ_−).

## Fixed randomized observer

Use ε=1/10000 and ℓ=1/30:

\[
T_0=\begin{pmatrix}
\varepsilon&1-2\varepsilon&\varepsilon\\
\varepsilon&1-2\varepsilon&\varepsilon\\
\ell&\varepsilon&1-\ell-\varepsilon
\end{pmatrix},\qquad
T_1=\begin{pmatrix}
\varepsilon&\varepsilon&1-2\varepsilon\\
\ell&1-\ell-\varepsilon&\varepsilon\\
\varepsilon&\varepsilon&1-2\varepsilon
\end{pmatrix}.
\]

Every entry is strictly positive, so A_hB is irreducible and aperiodic for all 0<c<1/2. There is no dependence of these matrices on c: **one fixed observer works for the entire bias interval**.

## Theorem 1: exact TV formula

Define constants

\[
N=168457578107217924,\quad
C=17386045750268881,\quad
D=553341785075524.
\]

Direct solution of the two stationary linear systems over Q(c) gives

\[
\mu_+(0)-\mu_-(0)=0,\qquad
\mu_+(1)-\mu_-(1)=-\frac{Nc}{5(C-Dc^2)},\qquad
\mu_+(2)-\mu_-(2)=+\frac{Nc}{5(C-Dc^2)}.
\]

Thus, because C−Dc²>0 throughout 0<c<1/2,

\[
\boxed{\operatorname{TV}_{\rm sticky}(c)=\frac{Nc}{5(C-Dc^2)}.}
\]

At c=1/5 this reproduces the independently certified exact fraction 56152526035739308/144699267323882167.

## Theorem 2: strict improvement over the deterministic optimum for every c

The earlier symbolic enumeration over all 729 deterministic update pairs, with common uniform initialization and Cesàro stationary projection for reducible chains, gives

\[
W(c)=\operatorname{TV}^{*}_{\rm det}(3,2,c)=\frac{12c}{9-4c^2}.
\]

Subtracting exactly and factoring yields

\[
\boxed{
\operatorname{TV}_{\rm sticky}(c)-W(c)
=\frac{24c(19706477414534519-26692908555180844c^2)}
{5(9-4c^2)(17386045750268881-553341785075524c^2)}>0
}
\]

for every 0<c<1/2. Indeed, c>0, 9−4c²>8, C−Dc²>C−D/4>0, and

\[
19706477414534519-\frac{26692908555180844}{4}
=13033250275739308>0.
\]

Therefore the numerator is positive throughout the interval. This proves a **uniform-in-bias randomization advantage** within the stated model, without tuning the observer to c.

**Logical scope:** The strict inequality between the fixed sticky observer and W(c) is independently proved by exact algebra. Interpreting W(c) as the optimum over *all* deterministic three-state rules depends on the separate finite exhaustive theorem and its initialization convention.

## Exact reproduction (SymPy)

\`\`\`python
import sympy as s
c=s.symbols("c",real=True)
e=s.Rational(1,10000); l=s.Rational(1,30)
T0=s.Matrix([[e,1-2*e,e],[e,1-2*e,e],[l,e,1-l-e]])
T1=s.Matrix([[e,e,1-2*e],[l,1-l-e,e],[e,e,1-2*e]])
B=(T0+T1)/2
def stationary(P):
    M=P.T-s.eye(3)
    M[2,:]=s.ones(1,3)
    rhs=s.zeros(3,1);rhs[2]=1
    return (M.inv()*rhs).T
mu=[]
for h in (1,-1):
    A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
    mu.append(stationary(A*B)*(s.eye(3)+A)/2)
delta=[s.factor(mu[0][i]-mu[1][i]) for i in range(3)]
assert delta[0]==0 and s.simplify(delta[1]+delta[2])==0
sticky=s.factor(delta[2])
walk=12*c/(9-4*c**2)
gap=s.factor(sticky-walk)
assert s.simplify(sticky-s.Rational(168457578107217924)*c/
  (5*(s.Integer(17386045750268881)-s.Integer(553341785075524)*c**2)))==0
print(sticky,gap)
\`\`\`

## Research consequences

1. The separation between randomized and deterministic three-state observers holds for **all** 0<c<1/2 with one fixed randomized observer, not merely at c=1/5.
2. The result does **not** identify the globally optimal randomized observer.
3. It does not cover other periods K, more memory states, observers with a clock, or arbitrary observation policies.
4. The deterministic optimum relies on a finite exact symbolic classification, not an analytic classification-free proof.
5. Potential relationship to classical finite-memory hypothesis testing and randomized finite automata must be assessed before claiming novelty.

**Next:** derive a general stochastic upper bound or a tractable restricted-family optimum; independently rerun the 729-rule symbolic certificate and inspect related literature.
