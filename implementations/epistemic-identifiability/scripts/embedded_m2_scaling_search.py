import sys, json; sys.path.insert(0,'scripts')
import numpy as np, warnings; warnings.filterwarnings("ignore")
import embedded_finite_memory_search as F
out={}
for p,lam in [((1/3,2/3),2.0),((0.25,0.75),3.0),((0.4,0.6),1.5)]:
    F.stationary_error.__defaults__=(p,)
    for K in (1,2,4,5):
        e=min(F.search(2,K,30,np.random.default_rng(s)) for s in (1,2))
        pred=0.5-(0.5-1/(1+lam))/K; out[f"lam{lam}_K{K}"]=dict(found=float(e),conj=pred)
        print(f"lam={lam} K={K}: found {e:.4f}  conjecture {pred:.4f}",flush=True)
json.dump(out,open('results/embedded/m2_scaling_check.json','w'),indent=1)
