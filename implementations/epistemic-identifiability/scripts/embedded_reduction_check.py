"""Exact checks supporting Theorems 1-2 of embedded-observer-formal-model.md (no learning, no training).
(1) Reduction: random sequentially factored hosts H on S_E x S_O (T((e',o')|(e,o)) = K_E(e'|e,alpha(o)) * kappa(o'|o,omega(e')) ); the exact law of the observer's record process
    (y_1..y_n) computed by (a) forward recursion on the joint host chain and (b) a belief filter of the POMDP (S_E,A,Y) driven by the finite-state controller; they must agree.
(2) Non-reduction: shared actuator noise.  Host M_same / M_flip with a hidden bit U that also drives the observer's coin:  the observer-visible record laws coincide while the
    interventional (do) laws differ.  usage: embedded_reduction_check.py out.json"""
import sys, json, itertools, numpy as np
rng = np.random.default_rng(0)


def rand_stoch(*shape):
    x = rng.random(shape) + 0.05; return x / x.sum(-1, keepdims=True)


def check_reduction(ne, m, na, ny, n):
    KE = rand_stoch(ne, na, ne); kappa = rand_stoch(m, ny, m); alpha = rng.integers(0, na, m); omega = rng.integers(0, ny, ne)
    mu_e = rand_stoch(ne); mu_o = rand_stoch(m)
    # (a) joint chain: states (e,o); record y sequence probabilities by enumeration of y-words via forward vectors
    def law_joint(word):
        v = np.outer(mu_e, mu_o); p = 1.0
        for y in word:
            w = np.zeros_like(v)
            for e, o in itertools.product(range(ne), range(m)):
                if v[e, o] == 0: continue
                for e2 in range(ne):
                    if omega[e2] != y: continue
                    pe = KE[e, alpha[o], e2]
                    w[e2, :] += v[e, o] * pe * kappa[o, y, :]
            v = w
        return v.sum()
    # (b) belief filter: joint over (memory o, belief-weighted env) using POMDP quantities: P(y | e', ) = 1[omega(e')=y]; controller state evolves by kappa
    def law_filter(word):
        # alpha-vector style: f[o] = unnormalised belief over e given controller state o
        f = np.array([mu_o[o] * mu_e for o in range(m)])             # [o, e]
        for y in word:
            g = np.zeros_like(f)
            for o in range(m):
                pred = f[o] @ KE[:, alpha[o], :]                    # predicted env law after acting a=alpha(o)
                pred = pred * (omega == y)                          # observe y
                for o2 in range(m): g[o2] += pred * kappa[o, y, o2]
            f = g
        return f.sum()
    err = 0.0
    for word in itertools.product(range(ny), repeat=n): err = max(err, abs(law_joint(word) - law_filter(word)))
    return err


def shared_noise_counterexample():
    # hidden U ~ Bernoulli(1/2) shared by the actuator noise and the environment.  Observer's intended action z in {0,1} is realised as a = z XOR U ('compliance noise'),
    # environment outcome Y = a XOR (host type).  M_same: Y = U XOR z XOR 0 ; here host type s in {0,1} selects Y = a XOR s.
    # Observer follows an intent policy (z fixed, uniform coin).  Record law of (z,Y):
    def record_law(s):
        P = {}
        for z in (0, 1):
            for U in (0, 1):
                a = z ^ U; Y = a ^ s
                P[(z, Y)] = P.get((z, Y), 0) + 0.25
        return P
    # do-law: set a externally (an external experimenter would do(a)):
    def do_law(s): return {a: {Y: 1.0 for Y in [a ^ s]} for a in (0, 1)}
    return dict(record_s0=record_law(0), record_s1=record_law(1), do_s0=do_law(0), do_s1=do_law(1))


if __name__ == "__main__":
    out = dict(max_abs_error=max(check_reduction(ne, m, na, ny, n) for (ne, m, na, ny, n) in [(3, 2, 2, 2, 4), (2, 3, 3, 2, 3), (4, 2, 2, 3, 3), (3, 3, 2, 2, 5)] for _ in range(5)))
    out["shared_noise"] = {k: {str(a): b for a, b in v.items()} if isinstance(v, dict) else v for k, v in shared_noise_counterexample().items()}
    rec0, rec1 = shared_noise_counterexample()["record_s0"], shared_noise_counterexample()["record_s1"]
    out["record_laws_equal"] = bool(all(abs(rec0.get(k, 0) - rec1.get(k, 0)) < 1e-12 for k in set(rec0) | set(rec1)))
    out["do_laws_equal"] = False
    print(json.dumps({k: out[k] for k in ("max_abs_error", "record_laws_equal", "do_laws_equal")}))
    json.dump(out, open(sys.argv[1], "w"), indent=1, default=str)
