# Exact finite-horizon recurrence for the three-state stochastic observer

Date: 2026-11-06. Independently derived and verified using SymPy exact arithmetic. This note also documents a correction to the characteristic polynomial in \`stochastic-near-optimal-spectral-slowdown.md\` (corrected in commit 96c2f894).

## Model and symmetry

Let 0<c<1/2, 0<e<1 and

\[
T_0=\begin{pmatrix}1-e&e&0\\0&0&1\\0&0&1\end{pmatrix},
\quad
T_1=\begin{pmatrix}1&0&0\\1&0&0\\0&e&1-e\end{pmatrix}.
\]

Set B=(T0+T1)/2, A_h=(1/2−hc)T0+(1/2+hc)T1, P_h=A_hB, u=(1/3,1/3,1/3). For n≥0 define the phase-averaged readout

\[
\mu_h^{(n)}=uP_h^n(I+A_h)/2.
\]

The reflection matrix R exchanging states 0 and 2 satisfies T1=RT0R, hence A_−=RA_+R, P_−=RP_+R, uR=u and μ_−^(n)=μ_+^(n)R. Consequently

\[
\mu_+^{(n)}-\mu_-^{(n)}=(d_n,0,-d_n),\quad
\mathrm{TV}_n=|d_n|.
\]

## Exact finite-time theorem

Define

\[
S=1-e+e^2/2,\quad Q=e^2(2-e)^2(1-4c^2)/16,
\]
\[
F=\frac{4c(4-e)}{8+2e-e^2-8c^2e+4c^2e^2}.
\]

Then d_n satisfies the **exact affine order-two recurrence**

\[
\boxed{d_{n+2}=S d_{n+1}-Qd_n+(1-S+Q)F,\qquad n\ge0,}
\]

with initial values

\[
\boxed{d_0=\frac{c(1+e)}3,\qquad
d_1=\frac{c(e^3-5e^2+7e+4)}6.}
\]

This gives TV after any finite number of periods by exact arithmetic, without multiplying P_h to a large power.

**Proof.** Direct exact determinant expansion gives the corrected characteristic polynomial, the same for both hypotheses,

\[
\det(xI-P_h)=(x-1)(x^2-Sx+Q).
\]

Because μ_−^(n)=μ_+^(n)R, the scalar d_n is a linear functional of uP_+^n and has the form F+aλ_+^n+bλ_-^n, where λ_± are roots of x²−Sx+Q. Cayley–Hamilton yields the recurrence. F is the independently verified stationary TV and d_0,d_1 follow by direct multiplication. Exact substitution checks n=0,1 and the characteristic polynomial.

The roots are

\[
\lambda_{\pm}=\frac{S\pm\sqrt{S^2-4Q}}2.
\]

For the parameter domain, the discriminant is positive and the eigenvalues satisfy 0<λ_-<λ_+<1. Hence an explicit formula is

\[
d_n=F+\frac{(d_1-F)-\lambda_-(d_0-F)}{\lambda_+-\lambda_-}\lambda_+^n
+\frac{\lambda_+(d_0-F)-(d_1-F)}{\lambda_+-\lambda_-}\lambda_-^n.
\]

The absolute value in TV_n is retained to avoid relying on an unproved global positivity assertion for every n and every parameter.

## Independent numerical checkpoints

At c=1/5:

| e | n | TV_n |
|---|---:|---:|
| 1/100 | 0 | 0.067333333 |
| 1/100 | 1 | 0.135650033 |
| 1/100 | 100 | 0.300825975 |
| 1/100 | 1000 | 0.398156240 |
| 1/1000 | 0 | 0.066733333 |
| 1/1000 | 1 | 0.133566500 |
| 1/1000 | 100 | 0.158667492 |
| 1/1000 | 1000 | 0.301790913 |
| 1/1000 | 5000 | 0.398022195 |

These were calculated independently by direct exact matrix powers and converted to decimals. The finite-n recurrence agrees with direct multiplication for n=0,1,2,3 by exact symbolic simplification.

## Reproducer

\`\`\`python
import sympy as s
c,e,x=s.symbols("c e x",positive=True)
T0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
T1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
B=(T0+T1)/2
u=s.ones(1,3)/3
As=[(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1 for h in (1,-1)]
S=1-e+e**2/2
Q=e**2*(2-e)**2*(1-4*c**2)/16
F=4*c*(4-e)/(8+2*e-e**2-8*c**2*e+4*c**2*e**2)
ds=[]
for n in range(4):
    mus=[u*(A*B)**n*(s.eye(3)+A)/2 for A in As]
    assert s.simplify(mus[0][1]-mus[1][1])==0
    assert s.simplify((mus[0][0]-mus[1][0])+(mus[0][2]-mus[1][2]))==0
    ds.append(s.factor(mus[0][0]-mus[1][0]))
for A in As:
    assert s.factor((A*B).charpoly(x).as_expr()-(x-1)*(x*x-S*x+Q))==0
assert s.simplify(ds[0]-c*(1+e)/3)==0
assert s.simplify(ds[1]-c*(e**3-5*e**2+7*e+4)/6)==0
for n in (0,1):
    assert s.simplify(ds[n+2]-S*ds[n+1]+Q*ds[n]-(1-S+Q)*F)==0
print("PASS")
\`\`\`

## Research significance and scope

This is a complete finite-horizon calculation for one explicit stochastic observer and common uniform initialization. It permits quantitative tests of horizon-dependent observer performance, and gives a reproducible check on the previously derived metastable scaling curve. It does not prove the conjectured global stochastic upper bound TV≤2c, and does not establish that this observer is finite-horizon optimal. The earlier characteristic-polynomial error is now explicitly corrected in its original file.
