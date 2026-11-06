# Exact finite-horizon randomization advantage: rational certificate

Date: 2026-11-06. Verified with exact SymPy rational arithmetic.

## Theorem (specific model and horizon)

Take m=3 memory states, K=2 observations per period, Bernoulli informative bias c=1/5, uniform phase-zero initialization u=(1/3,1/3,1/3), and phase-averaged readout after n=2 full periods. For each pair T0,T1 of deterministic three-state transition matrices, let

B=(T0+T1)/2,
A_h=(1/2-hc)T0+(1/2+hc)T1,
mu_h=u(A_h B)^2(I+A_h)/2,
TV_2=(1/2)sum_i |mu_+(i)-mu_-(i)|.

There are 3^6=729 ordered deterministic rule pairs. Exhaustive enumeration in exact rational arithmetic gives

\[
\boxed{\max_{\rm deterministic} TV_2=779/3000=0.259666666\ldots}
\]

with exactly six maximizers:

\`\`\`
(0,0,1,1,2,2)
(0,2,0,2,1,1)
(1,1,0,2,0,2)
(1,2,2,0,0,1)
(2,0,2,1,1,0)
(2,1,1,0,2,0)
\`\`\`

Each tuple encodes the destination states for input 0 (first three entries) and input 1 (last three entries). The six rules are relabelings of one reflecting-walk machine.

Now consider the stochastic family

T0=[[1-e,e,0],[0,0,1],[0,0,1]],
T1=[[1,0,0],[1,0,0],[0,e,1-e]],

with exact rational e=7/10. Exact multiplication gives

\[
\boxed{TV_2=161177383/600000000=0.268628971666\ldots}
\]

Therefore the advantage is the strictly positive rational number

\[
\boxed{TV_2^{\rm stochastic}-\max_{\rm deterministic}TV_2
=1792461/200000000=0.008962305.}
\]

This is an **exact certificate of finite-horizon randomization advantage** within the specified model. It is not a proof of global stochastic optimality, nor a universal result for every bias c or horizon n.

## Fully reproducible exact certificate

\`\`\`python
import itertools
import sympy as s

c=s.Rational(1,5)
u=s.ones(1,3)/3

def tv2(T0,T1):
    B=(T0+T1)/2
    laws=[]
    for h in (1,-1):
        A=(s.Rational(1,2)-h*c)*T0+(s.Rational(1,2)+h*c)*T1
        laws.append(u*(A*B)**2*(s.eye(3)+A)/2)
    return sum(abs(laws[0][i]-laws[1][i]) for i in range(3))/2

best=s.S.Zero
winners=[]
for rule in itertools.product(range(3),repeat=6):
    T0=s.zeros(3)
    T1=s.zeros(3)
    for i in range(3):
        T0[i,rule[i]]=1
        T1[i,rule[i+3]]=1
    score=tv2(T0,T1)
    if score>best:
        best=score
        winners=[rule]
    elif score==best:
        winners.append(rule)

assert best==s.Rational(779,3000)
assert len(winners)==6

e=s.Rational(7,10)
T0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
T1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
stochastic=tv2(T0,T1)
assert stochastic==s.Rational(161177383,600000000)
assert stochastic-best==s.Rational(1792461,200000000)
print("EXACT CERTIFICATE PASS",best,stochastic,stochastic-best)
\`\`\`

## Verification and scope

The exhaustive loop checks each of the 729 deterministic rules, including reducible transition kernels, with **the same uniform initialization and finite horizon**. No irreducibility, Cesaro projection, floating-point optimizer, or stationary assumption is needed. The stochastic rule uses rational probabilities and exact arithmetic. The certificate proves a strict gap at n=2, c=1/5. Claims of novelty relative to classical finite-memory hypothesis testing (Hellman and Cover 1970/1971) require separate prior-art review.

Next questions: characterize the range of c for which this fixed rational e=7/10 yields an advantage; derive an all-c exact finite-horizon certificate; or prove a general stochastic upper bound.
