import sys, json; sys.path.insert(0,'scripts')
import numpy as np, warnings; warnings.filterwarnings("ignore")
import embedded_finite_memory_search as F
rng=np.random.default_rng(7); out={}
for K,m,R in [(2,2,80),(2,3,80),(3,2,80),(3,3,80),(1,2,40),(1,3,60)]:
    vals=[F.search(m,K,R//2,np.random.default_rng(s)) for s in (1,2)]
    out[f"K{K}_m{m}"]=vals; print(K,m,[round(v,4) for v in vals],flush=True)
json.dump(out,open('results/embedded/finite_memory_search_repeat.json','w'),indent=1)
