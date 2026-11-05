"""PySR baselines (eid-pysr venv).  Reads the prepared datasets written by ool_run.py ('prep'), fits PySR with a fixed and an expanded operator library on the coupling drive
recovered from a reconstructed hidden state (tuned Kalman | learned GRU | privileged oracle), plus role A (raw observations, no latent), and scores each on the fresh programmes.
usage (eid-pysr python): ool_pysr.py in.pkl out.pkl [--workers 5] [--niter 40]"""
import sys, os, argparse, pickle, time, warnings
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src")); warnings.filterwarnings("ignore")
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from multiprocessing import Pool
from eid.ool import base, evals

TAU = 0.05


def score(fn, tr, fam, m):
    t0 = time.time()
    try: p, div = fn(); r = float(np.sqrt(np.mean((p - tr) ** 2))); r = r if np.isfinite(r) else 99.0
    except Exception as e: r, div = 99.0, True
    eq = str(m.get_best()["equation"]) if m is not None else ""
    return dict(rmse=r, ok=bool(r <= TAU), diverged=bool(div), eq=eq, struct=evals.sr_signature(fam, eq), wall=time.time() - t0)


def work(args):
    r, niter = args; out = dict(fam=r["fam"], k=r["k"], iseed=r["iseed"], pysr={})
    for B, d in r["prep"].items():
        U, Y, st, tr, Ut = d["U"], d["Y"], d["st"], d["truth"], d["Ut"]
        for src in ("kalman", "learned", "oracle"):
            sk = dict(st, **d["true_skel"]) if src == "oracle" else st
            V, D = base.eq_data(U, Y, d["x2"][src], sk)
            for lib in (("fixed", "expanded") if src != "oracle" else ("expanded",)):
                t0 = time.time()
                try: m = base.pysr_fit(V, D, lib, int(r["iseed"]) % 10000, niter=niter, timeout=60)
                except Exception as e: out["pysr"][(B, src, lib)] = dict(rmse=99.0, ok=False, eq=f"FAIL {e!r}"[:80], struct=None, diverged=True, wall=time.time() - t0, fit_wall=time.time() - t0); continue
                rec = score(lambda: base.simulate(lambda Vq, u2: m.predict(Vq), sk, Ut), tr, r["fam"], m); rec["fit_wall"] = time.time() - t0 - rec["wall"]; out["pysr"][(B, src, lib)] = rec
        t0 = time.time()
        try:
            V, D = base.raw_data(U, Y, st); m = base.pysr_fit_raw(V, D, int(r["iseed"]) % 10000, niter=niter, timeout=60)
            rec = score(lambda: base.simulate_raw(lambda Vq: m.predict(Vq), st, Ut), tr, r["fam"], m); rec["fit_wall"] = time.time() - t0 - rec["wall"]; out["pysr"][(B, "raw", "expanded")] = rec
        except Exception as e: out["pysr"][(B, "raw", "expanded")] = dict(rmse=99.0, ok=False, eq=f"FAIL {e!r}"[:80], struct=None, diverged=True, wall=0.0, fit_wall=time.time() - t0)
    return out


if __name__ == "__main__":
    from concurrent.futures import ProcessPoolExecutor, as_completed
    ap = argparse.ArgumentParser(); ap.add_argument("inp"); ap.add_argument("out"); ap.add_argument("--workers", type=int, default=5); ap.add_argument("--niter", type=int, default=40); a = ap.parse_args()
    res = pickle.load(open(a.inp, "rb"))["res"]; t0 = time.time(); out = []; failed = []
    with ProcessPoolExecutor(a.workers) as P:                 # a crashed Julia worker raises instead of hanging; results are saved incrementally
        futs = {P.submit(work, (r, a.niter)): r for r in res}
        for f in as_completed(futs):
            try: out.append(f.result())
            except Exception as e: failed.append((futs[f]["fam"], futs[f]["k"], repr(e)[:100]))
            print(f"{len(out)+len(failed)}/{len(res)} {time.time()-t0:.0f}s failed={len(failed)}", flush=True)
            pickle.dump(dict(args=vars(a), res=out, failed=failed), open(a.out + ".partial", "wb"))
    pickle.dump(dict(args=vars(a), res=out, failed=failed), open(a.out, "wb")); print("done", time.time() - t0, "failed", failed)
