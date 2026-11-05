# Seven- and eight-state exact formulas at K=2

**2026-11-05.** Exact symbolic calculation and elementary positivity proofs for the reflecting-walk observer. Not a claim of optimality or novelty.

## Model

Use the binary hidden K=2 periodic observation model from \`arbitrary-memory-k2-cofactor-formula.md\`. For 0<c<1/2, informative signal probabilities are 1/2±c; the other phase is fair. The m-state memory is a reflecting nearest-neighbor random walk, with no phase clock. Performance is TV of phase-averaged stationary memory laws.

## Theorem

Set
\[
F(c)=(8c^3-20c^2+6c-7)(8c^3+20c^2+6c+7).
\]
For every 0<c<1/2,
\[
\boxed{\mathrm{TV}_7(2,c)=\frac{8c(16c^4-48c^2-21)}{F(c)},}
\qquad
\boxed{\mathrm{TV}_8(2,c)=\frac{4c}{1+4c^2}.}
\]
The function F(c)<0 throughout the interval: the first factor is negative (8c³+6c<7 for c<1/2, and −20c²≤0; more directly 8c³+6c≤4, hence first≤−3), while the second factor is positive. The numerator for TV_7 is negative, so both TV expressions are positive.

Furthermore, with TV_6=c(9−4c²)/(3+4c²),
\[
\boxed{\mathrm{TV}_8(2,c)>\mathrm{TV}_7(2,c)>\mathrm{TV}_6(2,c).}
\]

### Proof of strict inequalities

Direct symbolic subtraction and factorization yield
\[
\mathrm{TV}_7-\mathrm{TV}_6=
\frac{c(4c^2-1)(64c^6-304c^4+76c^2+63)}
{(4c^2+3)F(c)}.
\]
Let t=c²∈(0,1/4). The polynomial in parentheses is strictly positive: 64t³+76t≥0, −304t²≥−19, and 63−19=44>0. Since 4c²−1<0 and F<0, the quotient is positive.

Likewise
\[
\mathrm{TV}_8-\mathrm{TV}_7=
-\frac{4c(4c^2-1)(16c^4-8c^2-7)}
{(4c^2+1)F(c)}.
\]
The factor 16t²−8t−7 is negative on 0<t<1/4 (16t²≤4 and −8t≤0, so ≤−3). Therefore the numerator is positive or negative? Here (4c²−1)<0 and (16c⁴−8c²−7)<0, their product is positive; the leading minus makes the numerator negative; F<0 makes the whole expression positive. This proves the strict inequalities. ∎

### Derivation of the rational functions

Let B=T(1/2), D=∂T(p)/∂p, A_±=B±cD, P_±=A_±B. For each m=7,8 solve the linear stationary equations v_±P_±=v_±, v_±1=1. Compute μ_±=v_±(I+A_±)/2, then TV=(1/2)||μ_+−μ_-||_1. Reflection symmetry gives μ_−=μ_+J. Exact symbolic factorization of the resulting rational functions yields the two formulas.

The signed differences μ_+−μ_- have negative entries below the midpoint and positive entries above it for m=7 and m=8; this can be checked from the factored expressions below, so the absolute values are resolved exactly rather than guessed numerically.

For m=7, the signed difference entries are the antisymmetric vector (−a,−b,−d,0,d,b,a), where
\[
a=-\frac{4c(4c^2+3)(20c^2+7)}{F(c)},\quad
b=\frac{8c(16c^4-8c^2-7)}{F(c)},\quad
d=\frac{4c(1-4c^2)(20c^2+7)}{-F(c)}.
\]
All a,b,d>0 in the admissible interval.

For m=8, the signed difference vector is (−a,−b,−d,−e,e,d,b,a), with
\[
a=\frac{c(20c^2+7)}{4(4c^2+1)},\quad
b=\frac{c(5-4c^2)}{4(4c^2+1)},\quad
d=\frac{3c(1-4c^2)}{4(4c^2+1)},\quad
e=\frac{c(1-4c^2)}{4(4c^2+1)}.
\]
The sum a+b+d+e simplifies to 4c/(1+4c²).

## Reproducible exact computation

~~~python
import sympy as s
c=s.symbols("c", real=True)
def exact_tv(m):
    B,D=s.zeros(m),s.zeros(m)
    for i in range(m):
        B[i,max(0,i-1)]+=s.Rational(1,2)
        B[i,min(m-1,i+1)]+=s.Rational(1,2)
        D[i,max(0,i-1)]-=1
        D[i,min(m-1,i+1)]+=1
    A=B+c*D
    P=A*B
    M=P.T-s.eye(m)
    M[m-1,:]=s.ones(1,m)
    rhs=s.zeros(m,1)
    rhs[m-1]=1
    v=M.inv()*rhs
    mu=v.T*(s.eye(m)+A)/2
    delta=[s.factor(mu[0,i]-mu[0,m-1-i]) for i in range(m)]
    tv=s.factor(sum(delta[i] for i in range((m+1)//2,m)))
    return tv,delta
tv6,_=exact_tv(6)
tv7,d7=exact_tv(7)
tv8,d8=exact_tv(8)
print("m7",tv7)
print("m8",tv8)
print("7-6",s.factor(tv7-tv6))
print("8-7",s.factor(tv8-tv7))
~~~

## Research status

These are exact constructive results for m=7,8 and a strict hierarchy m=6,7,8 at K=2. Together with prior notes they establish m=4<5<6<7<8 in this specific setting. They do **not** prove a general monotonicity theorem for all m or optimality of the reflecting-walk rule. A general single-crossing proof and a tractable all-m recurrence remain open. The rational formulas may follow from classical finite Markov-chain theory; novelty has not been established.
