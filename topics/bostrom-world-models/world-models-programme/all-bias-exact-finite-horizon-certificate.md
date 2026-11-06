# All-bias exact finite-horizon randomization advantage

Date: 2026-11-06. New exact exhaustive symbolic certificate, independently evaluated locally with SymPy. This supersedes the limited-scope all-bias comparison against a single reflecting rule.

## Model

Three memory states m=3, hidden period K=2, informative Bernoulli parameter P_h(Y=1)=1/2+h*c with 0<c<1/2, and fair Bernoulli at the other phase. A memory update is a pair of row-stochastic 3x3 matrices T0,T1, time homogeneous and without access to the phase. Let

B=(T0+T1)/2,
A_h=(1/2-h*c)*T0+(1/2+h*c)*T1,
u=(1/3,1/3,1/3).

After n=2 complete periods, the phase-averaged readout is

mu_h=u*(A_h*B)^2*(I+A_h)/2.

Distinguishability is TV_2=(1/2)*sum_i |mu_+(i)-mu_-(i)|.

## Theorem

For every 0<c<1/2,

\[
\boxed{\max_{\text{all 729 deterministic rules}}\mathrm{TV}_2(c)=\frac{c(31+4c^2)}{24}.}
\]

The reflecting-walk deterministic rule f0=(0,0,1), f1=(1,2,2) attains this value for all c.

The explicit stochastic rule

T0=[[3/10,7/10,0],[0,0,1],[0,0,1]],
T1=[[1,0,0],[1,0,0],[0,7/10,3/10]]

has exact performance

\[
\mathrm{TV}^{\rm rand}_2(c)=\frac{c(6424571+563108c^2)}{4800000}.
\]

The difference is

\[
\boxed{\mathrm{TV}^{\rm rand}_2(c)-\max_{\rm det}\mathrm{TV}_2(c)
=\frac{c(74857-78964c^2)}{1600000}>0.}
\]

Since 0<c²<1/4, the bracket exceeds 74857−78964/4=55116>0. Thus randomization strictly beats **every deterministic three-state rule for every admissible c**, at this finite horizon and with this initialization/readout.

## Rigorous exhaustive polynomial certificate

There are exactly 3^3=27 deterministic transition maps per input and 27²=729 pairs. For each rule, the signed coordinate differences d_i(c)=mu_+(i)−mu_−(i) are odd polynomials of degree at most 5 in c, because mu_h is a product of three affine A_h factors and two c-independent B factors (in fact degree at most 3 here; allowing 5 is harmless). Thus d_i(c)/c is a polynomial of degree at most 2 in x=c².

Because the three signed differences sum to zero,

\[
\mathrm{TV}(\mu_+,\mu_-)=\max_{S\subseteq\{0,1,2\}}\sum_{i\in S}d_i(c).
\]

For every nonempty proper subset S and both signs, certify the polynomial inequality

\[
\frac{31+4x}{24}\mp\frac{\sum_{i\in S}d_i(\sqrt{x})}{\sqrt{x}}\ge0,\qquad x\in[0,1/4].
\]

The extra ± sign is redundant but strengthens the check. Each quadratic q(x)=a+bx+dx² is nonnegative on [0,1/4] if its degree-2 Bernstein coefficients under x=t/4 are nonnegative:

\[
\beta_0=a,\quad \beta_1=a+b/8,\quad\beta_2=a+b/4+d/16.
\]

A complete exact rational audit of all 729 rules, all six nonempty proper subsets and both signs (8748 quadratic inequalities, each with three Bernstein coefficients) found **no negative Bernstein coefficients**; the minimum is exactly zero (72 zero coefficients). This is a finite exact certificate with a short independent reproducer below. It proves the global deterministic envelope for every c in the interval. The reflecting rule supplies equality.

## Reproducer (SymPy, no floating point)

\`\`\`python
import itertools
import sympy as s

c,x=s.symbols('c x', real=True)
u=s.ones(1,3)/3
maps=[]
for f in itertools.product(range(3),repeat=3):
    T=s.zeros(3)
    for i,j in enumerate(f):
        T[i,j]=1
    maps.append(T)

points=[s.Rational(1,10),s.Rational(1,4),s.Rational(2,5)]
basis=[]
for j,z in enumerate(points):
    basis.append(s.expand(s.prod((x-w*w)/(z*z-w*w)
        for k,w in enumerate(points) if k!=j)))

checks=0
for T0 in maps:
    for T1 in maps:
        B=(T0+T1)/2
        samples=[]
        for z in points:
            mus=[]
            for h in (1,-1):
                A=(s.Rational(1,2)-h*z)*T0+(s.Rational(1,2)+h*z)*T1
                mus.append(u*(A*B)**2*(s.eye(3)+A)/2)
            samples.append([s.factor(mus[0][i]-mus[1][i]) for i in range(3)])
        for mask in range(1,7):
            ys=[sum(v[i] for i in range(3) if mask>>i&1)/z
                for v,z in zip(samples,points)]
            p=s.Poly(s.expand(sum(y*L for y,L in zip(ys,basis))),x)
            for sign in (-1,1):
                q=s.Poly((31+4*x)/24-sign*p.as_expr(),x)
                a,b,d=(q.nth(k) for k in range(3))
                bern=(a,a+b/8,a+b/4+d/16)
                assert all(v>=0 for v in bern), (mask,sign,bern)
                checks+=1
assert checks==729*6*2

# Verify equality by the reflecting walk and strict randomized gap:
def signed(T0,T1):
    B=(T0+T1)/2
    out=[]
    for h in (1,-1):
        A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
        out.append(u*(A*B)**2*(s.eye(3)+A)/2)
    return [s.factor(out[0][i]-out[1][i]) for i in range(3)]

D0=s.Matrix([[1,0,0],[1,0,0],[0,1,0]])
D1=s.Matrix([[0,1,0],[0,0,1],[0,0,1]])
assert signed(D0,D1)==[-c*(31+4*c*c)/24,0,c*(31+4*c*c)/24]
e=s.Rational(7,10)
R0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
R1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
assert signed(R0,R1)==[
    c*(6424571+563108*c*c)/4800000,0,
    -c*(6424571+563108*c*c)/4800000]
print('PASS',checks)
\`\`\`

## Scope and caveats

This proves finite-horizon strict separation at n=2 for every 0<c<1/2 under uniform initialization and phase-averaged readout. It does **not** establish that this randomized rule is optimal among all stochastic rules, that randomization wins under every initialization, that the result holds for all K/m/n, or that the result is novel relative to classical finite-memory hypothesis testing. A careful prior-art review is required before external publication.

Earlier note \`all-bias-finite-horizon-reflecting-separation.md\` proved only comparison against the reflecting rule; the present exhaustive Bernstein certificate closes the deterministic-envelope gap.
