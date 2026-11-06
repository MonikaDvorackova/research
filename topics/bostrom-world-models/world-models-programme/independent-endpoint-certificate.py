"""Independent exact all-bias finite-horizon deterministic envelope audit.

Run: python independent-endpoint-certificate.py
Requires: sympy. No floats or numerical optimizers.
"""
import itertools
import sympy as s

u=s.ones(1,3)/3
c=s.symbols("c")
maps=[]
for f in itertools.product(range(3),repeat=3):
    M=s.zeros(3)
    for i,j in enumerate(f):
        M[i,j]=1
    maps.append(M)

def signed(T0,T1,z):
    B=(T0+T1)/2
    out=[]
    for h in (1,-1):
        A=(s.Rational(1,2)-h*z)*T0+(s.Rational(1,2)+h*z)*T1
        out.append(u*(A*B)**2*(s.eye(3)+A)/2)
    return [out[0][i]-out[1][i] for i in range(3)]

checks=0
equalities_at_zero=0
equalities_at_quarter=0
for T0 in maps:
    for T1 in maps:
        d1=signed(T0,T1,s.Rational(1,4))
        d2=signed(T0,T1,s.Rational(1,2))
        for mask in range(1,7):
            # g(x)=sum_{i in S} d_i(sqrt(x))/sqrt(x) is affine in x.
            # This follows from the three affine A_h factors and oddness in c.
            g1=4*sum(d1[i] for i in range(3) if (mask>>i)&1)
            g2=2*sum(d2[i] for i in range(3) if (mask>>i)&1)
            g0=(4*g1-g2)/3  # extrapolation from x=1/16,1/4 to x=0
            gap0=s.Rational(31,24)-g0
            gap1=s.Rational(4,3)-g2
            assert gap0>=0 and gap1>=0,(mask,gap0,gap1)
            equalities_at_zero+=int(gap0==0)
            equalities_at_quarter+=int(gap1==0)
            checks+=2
assert checks==8748

D0=s.Matrix([[1,0,0],[1,0,0],[0,1,0]])
D1=s.Matrix([[0,1,0],[0,0,1],[0,0,1]])
assert [s.factor(v) for v in signed(D0,D1,c)]==[
    -c*(31+4*c*c)/24,0,c*(31+4*c*c)/24]

e=s.Rational(7,10)
R0=s.Matrix([[1-e,e,0],[0,0,1],[0,0,1]])
R1=s.Matrix([[1,0,0],[1,0,0],[0,e,1-e]])
assert [s.factor(v) for v in signed(R0,R1,c)]==[
    c*(6424571+563108*c*c)/4800000,0,
    -c*(6424571+563108*c*c)/4800000]
assert s.factor(c*(6424571+563108*c*c)/4800000-c*(31+4*c*c)/24)==c*(74857-78964*c*c)/1600000
print("PASS: 729 rules; 8748 exact endpoint inequalities; equality counts:",
      equalities_at_zero,equalities_at_quarter)
