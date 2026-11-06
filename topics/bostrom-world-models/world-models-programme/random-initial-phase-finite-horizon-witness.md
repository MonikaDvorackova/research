# Truly random initial phase: exact n=2 comparison and a recovered stochastic witness

Date: 2026-11-06. Verified with independent SymPy exact-rational enumeration locally. This is a *different model* from the phase-zero-start theorem. Do not conflate the two.

## New model

Let phase Z be uniform on {0,1}, sampled once at the beginning and independent of hypothesis h, and **unknown to the memory automaton**. If Z=0, the four observations have transition kernels A_h,B,A_h,B; if Z=1, B,A_h,B,A_h. Start memory uniformly u=(1/3,1/3,1/3), use time-homogeneous T0,T1 and K=2, n=2.

Two readout conventions:

(A) Fixed terminal readout after four observations:

\[
\nu_h=u[(A_h B)^2+(B A_h)^2]/2.
\]

(B) Average over the two possible readout phases after the four observations (one extra step with the correct phase-dependent kernel):

\[
\bar\nu_h=u[(A_h B)^2(I+A_h)+(B A_h)^2(I+B)]/4.
\]

Both are distinct from the **original** fixed-phase-zero readout \(\mu_h=u(A_hB)^2(I+A_h)/2\).

## Exact 729-rule enumeration at c=1/5

| Criterion | Deterministic global optimum | Stochastic epsilon=7/10 | Difference |
|---|---:|---:|---:|
| (A) terminal | 1/4 | 12249/50000 | -251/50000 |
| (B) phase-averaged | 1529/6000 | 305402233/1200000000 | -132589/400000000 |
| original fixed-phase-zero | 779/3000 | 161177383/600000000 | 1792461/200000000 |

Six deterministic reflecting-walk relabelings maximize both (A) and (B) at c=1/5.

**Crucial discovery:** epsilon=7/10 fails, but this is NOT a counterexample to stochastic advantage. Varying epsilon in the same stochastic family recovers strict advantages under both conventions:

- For (A), epsilon=9/10, signed law difference is \((9403c/7500,0,-9403c/7500)\). At c=1/5 its TV is **9403/37500**, which exceeds the exact deterministic maximum 1/4 by **7/9375**.
- For (B), epsilon=17/20, signed law difference is
\[
\left(\frac{c(394517545+22626388c^2)}{307200000},0,-\frac{c(394517545+22626388c^2)}{307200000}\right).
\]
At c=1/5 its TV is **9885565013/38400000000**, which exceeds 1529/6000 by **33321671/12800000000**.

Therefore a *genuine random-initial-phase finite-horizon stochastic advantage exists at least at c=1/5* under both readout conventions, with **different witnesses** from the original epsilon=7/10 construction.

## Reproducer

\`\`\`python
import sympy as s,itertools
c=s.Rational(1,5);u=s.ones(1,3)/3
def law(T0,T1,h,kind):
 B=(T0+T1)/2
 A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
 if kind=="terminal":return u*((A*B)**2+(B*A)**2)/2
 return u*((A*B)**2*(s.eye(3)+A)+(B*A)**2*(s.eye(3)+B))/4
def tv(T0,T1,kind):
 p=law(T0,T1,1,kind);q=law(T0,T1,-1,kind)
 return sum(abs(p[i]-q[i]) for i in range(3))/2
for kind in ("terminal","phase_avg"):
 best=0; winners=[]
 for f in itertools.product(range(3),repeat=6):
  a=s.zeros(3);b=s.zeros(3)
  for i in range(3):a[i,f[i]]=1;b[i,f[i+3]]=1
  score=tv(a,b,kind)
  if score>best:best=score;winners=[f]
  elif score==best:winners.append(f)
 print(kind,best,len(winners))
e=s.Rational(9,10)
a=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
b=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
assert tv(a,b,"terminal")==s.Rational(9403,37500)>s.Rational(1,4)
e=s.Rational(17,20)
a=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
b=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
assert tv(a,b,"phase_avg")==s.Rational(9885565013,38400000000)>s.Rational(1529,6000)
print("PASS")
\`\`\`

## Next task

Find the all-bias deterministic envelope for truly random phase via the same exact polynomial endpoint technique and compare fixed epsilon=9/10 or 17/20. Because the terminal mixture uses two A factors, its signed difference is linear in c. The averaged mixture uses three A factors and its signed difference has c and c³ terms. The finite-horizon deterministic envelopes can therefore be certified by exact endpoint inequalities if the reflecting walk remains optimal. Do not claim all-bias random-phase theorem until verified.

## Literature

Related finite-state testing work (iid, different model): Berg, Ordentlich, Shayevitz (2020), 'Binary Hypothesis Testing with Deterministic Finite-Memory Decision Rules', IEEE ISIT, https://arxiv.org/abs/2005.07445. Classical Flower–Hellman (1972) likewise studies finite-time iid testing. These sources do not themselves establish novelty of the random-phase periodic variant.
