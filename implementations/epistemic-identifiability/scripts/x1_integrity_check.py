"""Integrity checks on a finished X1 run, performed BEFORE any outcome is analysed. Reads structure only (keys, counts, finiteness)."""
import collections, hashlib, itertools, json, sys
d = sys.argv[1]
cfg = json.load(open(d + "/meta.json"))["config"]
meta = json.load(open(d + "/meta.json"))
rows, bad = [], 0
for i, l in enumerate(open(d + "/runs.jsonl")):
    try: rows.append(json.loads(l))
    except Exception: bad += 1
exp = {(s, t, p, r) for s in cfg["seeds"] for t in cfg["truths"] for p in cfg["policies"] for r in range(cfg["R"])}
got = collections.Counter((r["seed"], r["truth"], r["policy"], r["rep"]) for r in rows)
dup = [k for k, v in got.items() if v > 1]
missing = exp - set(got); extra = set(got) - exp
fields = {"seed", "truth", "policy", "rep", "role", "reject_episode", "reject_step", "max_logE", "seconds"}
import math
nonfinite = sum(1 for r in rows if not math.isfinite(r["max_logE"]))
rng_ok = all(1 <= r["reject_episode"] <= cfg["N"] + 1 for r in rows)
fields_ok = all(set(r) == fields for r in rows)
dev_seeds = {500, 501, 502, 503, 504, 505}
print(f"expected runs {len(exp)}; read {len(rows)}; unparsable lines {bad}; duplicates {len(dup)}; missing {len(missing)}; unexpected {len(extra)}")
print(f"non-finite max_logE {nonfinite}; reject_episode within [1,N+1] {rng_ok}; field set exact {fields_ok}")
print(f"confirmatory seeds {min(cfg['seeds'])}..{max(cfg['seeds'])} n={len(cfg['seeds'])}; overlap with development seeds {sorted(dev_seeds & set(cfg['seeds']))}")
print(f"config in meta.json: {json.dumps(cfg)}")
print(f"execution metadata: python {meta['python'].split()[0]}, numpy {meta['numpy']}, {meta['platform']}, wall {meta['wall_seconds']:.0f}s")
for f in ("runs.jsonl", "meta.json"):
    print(hashlib.sha256(open(f"{d}/{f}", "rb").read()).hexdigest(), f)
ok = len(rows) == len(exp) and not bad and not dup and not missing and not extra and not nonfinite and rng_ok and fields_ok and not (dev_seeds & set(cfg["seeds"]))
print("INTEGRITY:", "PASS" if ok else "FAIL")
