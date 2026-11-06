# All-bias theorem for truly random initial phase (two readout conventions)

Date: 2026-11-06. Exact symbolic endpoint enumeration performed independently with SymPy on all 729 deterministic rules. This note extends the previous single-bias random-phase witness.

## Setting

Let h∈{−1,+1}, 0<c<1/2, memory size m=3, uniform memory initialization u=(1/3,1/3,1/3). Initial source phase Z is independently uniform on {0,1} and unobserved by the time-homogeneous memory automaton. At the informative phase the Bernoulli parameter is 1/2+h c; at the other phase it is 1/2. Let T0,T1 be 3x3 row-stochastic memory update matrices, A_h=(1/2−h c)T0+(1/2+h c)T1, B=(T0+T1)/2.

After four observations (two complete periods) define:

**Terminal:** ν_h = u[(A_h B)^2+(B A_h)^2]/2.

**Phase-averaged:** \barν_h = u[(A_h B)^2(I+A_h)+(B A_h)^2(I+B)]/4.

For either convention D=TV(law_+,law_-).

## Theorem (exact all-bias global deterministic envelope)

For every 0<c<1/2, the maximum over all 729 deterministic 3-state transition pairs is

\[
D_{\rm det,terminal}^*(c)=5c/4,
\qquad
D_{\rm det,phaseavg}^*(c)=c(61+4c^2)/48.
\]

Both maxima are attained by the reflecting deterministic maps f0=(0,0,1), f1=(1,2,2), and their relabelings.

**Proof/certificate:** For each rule, each signed coordinate difference is odd in c, of degree at most 1 in the terminal convention (two informative A factors) and at most 3 in the phase-averaged convention (three informative A factors). For each of the six nonempty proper state subsets S, g_S(x)=sum_{i∈S}(law_+(i)−law_-(i))/c is affine in x=c². The difference between the claimed deterministic envelope divided by c and g_S(x) is affine on x∈[0,1/4]. Thus it suffices to check its values at x=0 and x=1/4. Exact enumeration of 729 transition pairs × 6 subsets × 2 endpoints yields 8,748 nonnegative rational inequalities in each convention. In a fresh SymPy enumeration, endpoint maxima were:

- Terminal: max_S g_S(0)=5/4, max_S g_S(1/4)=5/4.
- Phase-averaged: max_S g_S(0)=61/48, max_S g_S(1/4)=31/24.

The reflecting pair attains the interpolating envelope identically, proving equality for every c.

## Strict randomized advantage for all biases

Consider the same randomized family as earlier:

\[
T_0(\varepsilon)=
\begin{pmatrix}1-\varepsilon&\varepsilon&0\\0&0&1\\0&0&1\end{pmatrix},\quad
T_1(\varepsilon)=
\begin{pmatrix}1&0&0\\1&0&0\\0&\varepsilon&1-\varepsilon\end{pmatrix}.
\]

**Terminal:** choose ε=9/10. Exact signed difference:

\[
\nu_+-\nu_-=(9403c/7500,0,-9403c/7500).
\]

Hence D_rand=9403c/7500 and

\[
\boxed{D_{\rm rand}-D_{\rm det}^*=7c/1875>0.}
\]

**Phase-averaged:** choose ε=17/20. Exact signed difference:

\[
\bar\nu_+-\bar\nu_-=
\frac{c(394517545+22626388c^2)}{307200000}(1,0,-1).
\]

Hence

\[
\boxed{D_{\rm rand}-D_{\rm det}^*
=\frac{c(1372515-991204c^2)}{102400000}>0}
\]

for every 0<c<1/2. In particular, the bracket is >1372515−991204/4=1124714>0.

These are two separate fixed randomized witnesses. **Do not** claim they are globally optimal stochastic observers.

## Independent audit script

\`\`\`python
import sympy as s,itertools
u=s.ones(1,3)/3
c=s.symbols('c')
maps=[]
for f in itertools.product(range(3),repeat=3):
 M=s.zeros(3)
 for i,j in enumerate(f): M[i,j]=1
 maps.append(M)
def signed(a,b,z,kind):
 B=(a+b)/2;out=[]
 for h in (1,-1):
  A=(s.Rational(1,2)-h*z)*a+(s.Rational(1,2)+h*z)*b
  v=(u*((A*B)**2+(B*A)**2)/2 if kind=='terminal'
    else u*((A*B)**2*(s.eye(3)+A)+(B*A)**2*(s.eye(3)+B))/4)
  out.append(v)
 return [out[0][i]-out[1][i] for i in range(3)]
for kind,endpoint_bound in [
 ('terminal',(s.Rational(5,4),s.Rational(5,4))),
 ('phase_avg',(s.Rational(61,48),s.Rational(31,24)))
]:
 checks=0
 for a,b in itertools.product(maps,repeat=2):
  d1=signed(a,b,s.Rational(1,4),kind)
  d2=signed(a,b,s.Rational(1,2),kind)
  for mask in range(1,7):
   g1=4*sum(d1[i] for i in range(3) if mask>>i&1)
   g2=2*sum(d2[i] for i in range(3) if mask>>i&1)
   g0=(4*g1-g2)/3
   assert g0<=endpoint_bound[0]
   assert g2<=endpoint_bound[1]
   checks+=2
 assert checks==8748
 print('PASS',kind,checks)
e=s.Rational(9,10)
a=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
b=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
assert [s.factor(v) for v in signed(a,b,c,'terminal')]==[9403*c/7500,0,-9403*c/7500]
e=s.Rational(17,20)
a=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
b=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
q=c*(394517545+22626388*c*c)/307200000
assert [s.factor(v) for v in signed(a,b,c,'phase_avg')]==[q,0,-q]
assert s.factor(q-c*(61+4*c*c)/48)==c*(1372515-991204*c*c)/102400000
print('ALL PASS')
\`\`\`

## Novelty and limits

This result strengthens the previous theorem by allowing a genuinely unknown random initial source phase. It remains specific to m=3, K=2, two periods, uniform initial memory, and either of the two stated readout conventions. It does not prove stochastic global optimality or imply anything empirical about a simulation hypothesis.

Finite-time randomized finite-memory testing is classical (Flower and Hellman, 1972, https://ee.stanford.edu/~hellman/publications/10.pdf). The precise periodic random-phase exact-envelope result needs targeted novelty review before submission.
