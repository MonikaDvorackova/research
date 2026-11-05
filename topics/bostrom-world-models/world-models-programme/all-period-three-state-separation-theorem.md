# General all-period three-state separation theorem (exact)

**2026-11-05. Status:** Analytically derived theorem for every integer K≥2, with an explicit proof via spectral projectors and elementary inequalities. Not externally reviewed. **Novelty NOT established.** Supersedes the earlier finite-K conjecture in `parametric-three-state-separation.md`.

## Model

Hypotheses h=± with p_h=1/2±c, 0<c<1/2. A hidden deterministic phase of period K has one informative step (Y~Bernoulli(p_h)) and K−1 uninformative steps (Y~Bernoulli(1/2)); the observer does not know the phase or possess a clock. It always probes and has memory i∈{0,1,2}; after Y=1 it moves to min(i+1,2), after Y=0 to max(i−1,0). It guesses h from the current memory. Evaluate total variation of the Cesàro phase-averaged stationary memory laws. Write T(p) for the transition matrix with rows (1−p,p,0), (1−p,0,p), (0,1−p,p). Let A_h=T(p_h), B=T(1/2).

## Theorem (strict memory separation for all periods)

For every integer K≥2 and 0<c<1/2, the described three-state, time-homogeneous, clockless observer achieves
[
\boxed{\operatorname{TV}_3(K,c)=\frac{8c(2-x)(2+y)}{3K[4+(4c^2-1)xy-2x+2y]}}
]
where x=2^{-(K−1)} and y=(−1/2)^{K−1}. In particular,
[
\boxed{\operatorname{TV}_3(K,c)>\frac{2c}{K}=\operatorname{TV}_{2,\mathrm{opt}}(K,c).}
]
The second equality invokes Theorem 3 of `proof-note-two-state-hidden-phase.md`, whose assumptions are the same for the two-state comparator. Thus for **every** nontrivial hidden period, three memory states strictly outperform *all* admissible two-state clockless time-homogeneous observers under the specified phase-averaged Bayes criterion.

This is an **achievability separation**. It does NOT characterize the optimum among all three-state observers or the minimum memory required for a given risk.

## Proof

**Step 1 (spectral representation).** The fair-signal transition B has eigenvalues 1, 1/2, −1/2 and spectral projectors
[
P_1=\frac13\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix},\quad
P_+=\begin{pmatrix}1/2&0&-1/2\\0&0&0\\-1/2&0&1/2\end{pmatrix},\quad
P_-=\begin{pmatrix}1/6&-1/3&1/6\\-1/3&2/3&-1/3\\1/6&-1/3&1/6\end{pmatrix}.
]
Direct multiplication checks B=P_1+(1/2)P_+−(1/2)P_- and P_iP_j=δ_ijP_i. Therefore
[
B^{K-1}=P_1+xP_++yP_-,
quad
\sum_{j=0}^{K-2}B^j=(K-1)P_1+2(1-x)P_++\tfrac23(1-y)P_-.
]

**Step 2 (stationary phase average).** For h=+, let v be the stationary row distribution immediately before the informative step: v=vA_+B^{K-1}, v1=1. The phase-averaged row law is
[
\bar v_+=\frac1K\left[v+vA_+\sum_{j=0}^{K-2}B^j\right].
]
Solving the three linear equations for v and substituting the projectors gives the **exact identity**
[
\bar v_+(2)-\bar v_+(0)
=\frac{8c(2-x)(2+y)}{3K[4+(4c^2-1)xy-2x+2y]}.
]
This is rational matrix algebra; a short reproducibility script is provided below. The h=− law is the reflection of the h=+ law under state swap 0↔2 (the phase and initial stationary construction are symmetric), so the two phase-averaged distributions have equal middle component and swapped extremes. Hence their total variation equals the displayed end-state difference.

**Step 3 (strict inequality).** All factors in the formula are positive for K≥2, 0<c<1/2. To prove TV_3>2c/K it suffices to show
[
4(2-x)(2+y)>3[4+(4c^2-1)xy-2x+2y].
]
If K is even, y=−x and 0<x≤1/2. Subtracting the right-hand side from the left gives
[
4-4x+(1+12c^2)x^2>0
]
because 4−4x≥2. If K is odd, y=x and 0<x≤1/4 (since K≥3), and the difference is
[
4-(1+12c^2)x^2>0
]
since 1+12c²<4 and x²≤1/16. This proves strict separation. ∎

## Reproducibility and examples

Use exact rational/symbolic matrix operations to verify the spectral projectors and the stationary expression. The general identity can be checked with independent symbolic variables x,y representing the two nontrivial eigenvalue powers:

```python
import sympy as s
c,x,y,K=s.symbols('c x y K', real=True)
def T(p):
    return s.Matrix([[1-p,p,0],[1-p,0,p],[0,1-p,p]])
B=T(s.Rational(1,2))
values=[s.Integer(1),s.Rational(1,2),-s.Rational(1,2)]
proj={}
for lam in values:
    P=s.eye(3)
    for mu in values:
        if mu!=lam: P=P*(B-mu*s.eye(3))/(lam-mu)
    proj[lam]=P
P1,Pp,Pm=[proj[z] for z in values]
BK=P1+x*Pp+y*Pm
S=(K-1)*P1+2*(1-x)*Pp+s.Rational(2,3)*(1-y)*Pm
A=T(s.Rational(1,2)+c)
z=s.symbols('z0:3')
v=s.Matrix(1,3,z)
sol=s.solve(list(v*A*BK-v)+[sum(z)-1],z)
v=s.Matrix(1,3,[sol[t] for t in z])
avg=s.simplify((v+v*A*S)/K)
lhs=s.factor(avg[2]-avg[0])
rhs=8*c*(2-x)*(2+y)/(3*K*(4+(4*c**2-1)*x*y-2*x+2*y))
assert s.simplify(lhs-rhs)==0
print(s.factor(lhs))
```

Substitution yields K=2: 12c/(9−4c²); K=3: 56c/(63+4c²); K=4: 150c/(225−4c²); K=5: 2728c/[5(1023+4c²)], agreeing with earlier finite-period calculations.

## Research significance and caveats

This closes the mathematical question whether the *specific* three-state reflecting-walk observer strictly beats the optimal two-state observer for **every** hidden period K≥2. The answer is yes, with an explicit formula and proof.

The result is **not** evidence that an embedded observer can identify the physical substrate of a universe, and is **not yet established as novel** relative to finite-state hypothesis-testing theory. The model is intentionally narrow: fixed periodic schedule, phase-averaged stationary decision, symmetric binary signals, no observer clock.

**Next genuinely open task:** seek a nontrivial upper bound or exact m=3 optimum; examine scaling with m and K; verify the closest prior literature (especially original Hellman–Cover and finite-state testing with periodic observation channels). Do not write a paper asserting novelty until that gate is passed.
