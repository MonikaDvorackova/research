"""Independent, dependency-free rational certificate for the random-phase theorem.
Run: python random-phase-independent-audit.py (Python >=3.9).
"""
from fractions import Fraction as F
from itertools import product
n=3
I=[[F(i==j) for j in range(n)] for i in range(n)]
def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def add(a,b,wa=1,wb=1):
    return [[wa*a[i][j]+wb*b[i][j] for j in range(n)] for i in range(n)]
def row(a):
    return [sum(a[i][j] for i in range(n))/3 for j in range(n)]
def signed(a,b,c,kind):
    B=add(a,b,F(1,2),F(1,2));v=[]
    for h in (1,-1):
        A=add(a,b,F(1,2)-h*c,F(1,2)+h*c)
        AB=mul(A,B);BA=mul(B,A)
        if kind=='terminal':
            M=add(mul(AB,AB),mul(BA,BA),F(1,2),F(1,2))
        else:
            M=add(mul(mul(AB,AB),add(I,A)),mul(mul(BA,BA),add(I,B)),F(1,4),F(1,4))
        v.append(row(M))
    return [v[0][i]-v[1][i] for i in range(3)]
def mat(f):
    return [[F(j==f[i]) for j in range(3)] for i in range(3)]
maps=[mat(f) for f in product(range(3),repeat=3)]
for kind,ends in [('terminal',(F(5,4),F(5,4))),('phase',(F(61,48),F(31,24)))]:
    checks=0;max0=F(0);max1=F(0)
    for a in maps:
        for b in maps:
            d1=signed(a,b,F(1,4),kind);d2=signed(a,b,F(1,2),kind)
            for mask in range(1,7):
                g1=4*sum(d1[i] for i in range(3) if mask>>i&1)
                g2=2*sum(d2[i] for i in range(3) if mask>>i&1)
                g0=(4*g1-g2)/3
                assert g0<=ends[0] and g2<=ends[1],(kind,mask,g0,g2)
                max0=max(max0,g0);max1=max(max1,g2);checks+=2
    assert checks==8748 and (max0,max1)==ends
    print('PASS',kind,checks,'max endpoints',max0,max1)
# Exact rational witness checks at c=1/5.
def stochastic(e):
    return ([[1-e,e,F(0)],[F(0),F(0),F(1)],[F(0),F(0),F(1)]],
            [[F(1),F(0),F(0)],[F(1),F(0),F(0)],[F(0),e,1-e]])
for kind,e,bound in [('terminal',F(9,10),F(1,4)),('phase',F(17,20),F(1529,6000))]:
    a,b=stochastic(e)
    d=signed(a,b,F(1,5),kind)
    score=sum(abs(x) for x in d)/2
    assert score>bound,(kind,score,bound)
    print('PASS witness',kind,score,'gap',score-bound)

# Polynomial identity checks: signed differences are odd degree <=3,
# so equality at two distinct nonzero squared biases proves all-bias identity.
def assert_signed_identity(a,b,kind,formula):
    for c in (F(1,5),F(2,5)):
        d=signed(a,b,c,kind)
        z=formula(c)
        assert sorted(d)==[-z,F(0),z],(kind,c,d,z)
    print('PASS symbolic-degree identity',kind)
a=mat((0,0,1));b=mat((1,2,2))
assert_signed_identity(a,b,'terminal',lambda c:5*c/4)
assert_signed_identity(a,b,'phase',lambda c:c*(61+4*c*c)/48)
a,b=stochastic(F(9,10))
assert_signed_identity(a,b,'terminal',lambda c:9403*c/7500)
a,b=stochastic(F(17,20))
assert_signed_identity(a,b,'phase',lambda c:c*(394517545+22626388*c*c)/307200000)
for c in (F(1,5),F(2,5)):
    terminal=9403*c/7500-5*c/4
    phase=c*(394517545+22626388*c*c)/307200000-c*(61+4*c*c)/48
    assert terminal==7*c/1875 and terminal>0
    assert phase==c*(1372515-991204*c*c)/102400000 and phase>0
print('PASS exact gap polynomial identities')
