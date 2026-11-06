"""Grid check of the vertex inequality of proof-note-two-state-hidden-phase.md: min over (u,v,K,c) of s^2 - F at the box vertices; expected minimum margin 0 (never negative)."""
import numpy as np, itertools
worst=1e9; arg=None
g=np.linspace(0,1,201)
for K in list(range(1,12))+[20,40]:
    for c in (0.1,0.3,0.4999):
        for u in g:
            for v in g:
                s=u+v
                if s<1e-9: continue
                sig=1-s; gam=sig**(K-1); den=1-gam*sig
                if abs(den)<1e-12: continue
                eps=gam*c/den
                r0m=2*min(v,1-v); r1m=2*min(u,1-u)
                for a,b in itertools.product((r0m,-r0m),(r1m,-r1m)):
                    F=abs(a*u+b*v)+(s*eps*(b-a))**2
                    m=s*s-F
                    if m<worst: worst=m; arg=(K,c,u,v,a,b)
print("minimum margin s^2 - F over vertices:",worst,arg)
