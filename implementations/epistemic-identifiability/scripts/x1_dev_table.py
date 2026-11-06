import json, sys, collections, numpy as np
rows=[json.loads(l) for l in open(sys.argv[1]+"/runs.jsonl")]
N=json.load(open(sys.argv[1]+"/meta.json"))["config"]["N"]
g=collections.defaultdict(list)
for r in rows: g[(r["truth"],r["policy"])].append(r["reject_episode"])
P=("P0","P1","P2","P3","P4","P5")
print(f"{'truth':6s}"+"".join(f"{p:>20s}" for p in P))
for t in ("E0","split","n10","n20","t05","t10","pc0","pc1","pc2","shift"):
    s=f"{t:6s}"
    for p in P:
        x=np.array(g[(t,p)]); s+=f"  rej={(x<=N).mean():.3f} med={np.median(np.minimum(x,N+1)):6.0f}"
    print(s)
print("total run-seconds", round(sum(r["seconds"] for r in rows)))
