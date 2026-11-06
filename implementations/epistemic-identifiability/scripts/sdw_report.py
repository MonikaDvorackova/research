"""Analysis of the SDW development evaluation: pre-fixed metrics and decision rules of doc 19.  usage: sdw_report.py main.pkl out.md"""
import sys, os, pickle, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import numpy as np
from eid.sdw import env, agent as A

d = pickle.load(open(sys.argv[1], "rb")); res = sorted(d["res"], key=lambda r: r["k"]); N = len(res)
fam = np.array([r["fam"] for r in res]); rng = np.random.default_rng(0); NB = 10000
BS = (3, 5, 8)
GROUPS = dict(known=env.KNOWN, unfamiliar=env.UNFAMILIAR, inlang=env.INLANG)
gmask = {g: np.isin(fam, f) for g, f in GROUPS.items()}; gmask.update({f: fam == f for f in env.ALL_FAMS})
boot_idx = {g: rng.integers(0, m.sum(), (NB, m.sum())) for g, m in gmask.items()}


def ci(x, g):
    x = np.asarray(x, float)[gmask[g]]; b = x[boot_idx[g]].mean(1); return x.mean(), np.percentile(b, 2.5), np.percentile(b, 97.5)


def fmt(t, p=2): return f"{t[0]:.{p}f} [{t[1]:.{p}f},{t[2]:.{p}f}]"


def get(kind, name, B, field, sched="B"):
    out = []
    for r in res:
        rec = r["agents"][name][B] if kind == "ag" else r["base"][sched][name][B]
        out.append(rec[field])
    return np.array(out)


def outcomes(name, B, mode): return np.array([A.outcome(r["agents"][name][B], mode) for r in res])


lines = []; P = lines.append; J = {}
P(f"# SDW development evaluation (ns 25000): {N} instances ({N//len(env.ALL_FAMS)} per family), paired; 95% bootstrap CIs over instances ({NB} resamples)\n")
P("Primary outcome: functional recovery = RMSE of predicted x3 on 24 fresh admissible programmes <= tau=0.05. Agent rows use the agent's best hypothesis irrespective of abstention (that is the *nocrit* claim); abstention outcomes are in section 3.\n")

# ---------------------------------------------------------- 1 recovery rates
AG = ["falsify", "sweepA", "sweepB", "random", "ens", "eig", "declared_eig", "falsify_nou2"]
BSL = ["bayes_declared", "grammar_sweep", "narx", "hammerstein", "sindyc_raw", "sindyc_embed", "sindyc_learned", "sindyc_oracle", "sindyc_dict_raw", "sindyc_dict_learned", "sindyc_dict_oracle"]
P("## 1. Functional recovery rate (ok)  — groups: known / unfamiliar-in-language / osc / unreach\n")
for B in BS:
    P(f"### B={B}\n\n| method | known | unfamiliar | all in-language | osc | unreach |\n|---|---|---|---|---|---|")
    for n in AG:
        ok = get("ag", n, B, "ok").astype(float); P(f"| agent[{n}] | " + " | ".join(fmt(ci(ok, g)) for g in ("known", "unfamiliar", "inlang", "osc", "unreach")) + " |")
    for n in BSL:
        try: ok = get("bs", n, B, "ok").astype(float)
        except KeyError: continue
        tag = " (ORACLE state, privileged)" if "oracle" in n else ""
        P(f"| baseline[{n}]{tag} | " + " | ".join(fmt(ci(ok, g)) for g in ("known", "unfamiliar", "inlang", "osc", "unreach")) + " |")
    P("")
P("### Per-family recovery, B=5 (agent[falsify] | agent[sweepB] | grammar | bayes_declared | narx | hammerstein | sindyc_dict_raw | sindyc_raw)\n\n| family | " + " | ".join(["falsify", "sweepB", "grammar", "bayes", "narx", "hammer", "dict_raw", "raw"]) + " |\n|---|---|---|---|---|---|---|---|")
for f in env.ALL_FAMS:
    cells = []
    for kind, n in [("ag", "falsify"), ("ag", "sweepB"), ("bs", "grammar_sweep"), ("bs", "bayes_declared"), ("bs", "narx"), ("bs", "hammerstein"), ("bs", "sindyc_dict_raw"), ("bs", "sindyc_raw")]:
        cells.append(f"{ci(get(kind, n, 5, 'ok').astype(float), f)[0]:.2f}")
    P(f"| {f} | " + " | ".join(cells) + " |")
P("\nMedian test RMSE (B=5) in-language: " + ", ".join(f"{n}={np.median(get('bs', n, 5, 'rmse')[gmask['inlang']]):.3f}" for n in BSL if n in res[0]["base"]["B"]) + ", agent[falsify]=" + f"{np.median(get('ag','falsify',5,'rmse')[gmask['inlang']]):.3f}\n")

# ---------------------------------------------------------- 2 paired rules
def pdiff(a, b, g):
    x = (np.asarray(a, float) - np.asarray(b, float))[gmask[g]]; bb = x[boot_idx[g]].mean(1); return x.mean(), np.percentile(bb, 2.5), np.percentile(bb, 97.5)


P("## 2. Pre-fixed decision rules (paired risk differences in recovery rate)\n")
P("**H1** (grammar search vs best baseline; agent[falsify] without criticism minus each baseline; unfamiliar in-language families)\n\n| B | baseline | difference |\n|---|---|---|")
H1 = {}
for B in (5, 8):
    ag = get("ag", "falsify", B, "ok").astype(float)
    rows = []
    for n in BSL:
        if n == "grammar_sweep": continue                                  # ablation of the agent itself, not a protocol baseline (addendum B)
        try: b = get("bs", n, B, "ok").astype(float)
        except KeyError: continue
        rows.append((n, pdiff(ag, b, "unfamiliar"), b[gmask["unfamiliar"]].mean()))
    best = max(rows, key=lambda r: r[2]); H1[B] = (best[0], best[1])
    for n, t, _ in rows: P(f"| {B} | {n}{' (oracle)' if 'oracle' in n else ''} | {fmt(t)} |")
P("\nBest baseline (by point estimate): " + "; ".join(f"B={B}: {H1[B][0]} diff {fmt(H1[B][1])}" for B in H1))
nonorc = lambda B: max([(n, pdiff(get('ag','falsify',B,'ok'), get('bs',n,B,'ok'), 'unfamiliar')) for n in BSL if 'oracle' not in n and n != 'grammar_sweep' and n in res[0]['base']['B']], key=lambda r: get('bs', r[0], B, 'ok')[gmask['unfamiliar']].mean())
h1 = all(nonorc(B)[1][1] > 0 for B in (5, 8)); J["H1_supported_vs_best_nonoracle"] = bool(h1)
P(f"\n**H1 {'SUPPORTED' if h1 else 'NOT SUPPORTED'}** against the best non-oracle baseline at both budgets: " + "; ".join(f"B={B}: {nonorc(B)[0]} {fmt(nonorc(B)[1])}" for B in (5, 8)) + "\n")

P("**H2** (falsification design vs alternatives; risk difference in recovery rate, agent[falsify] minus X; groups unfamiliar / in-language)\n\n| B | X | unfamiliar | all in-language |\n|---|---|---|---|")
J["H2"] = {}
for B in BS:
    f = get("ag", "falsify", B, "ok").astype(float)
    for X in ("sweepA", "sweepB", "random", "ens", "eig", "falsify_nou2"):
        x = get("ag", X, B, "ok").astype(float); P(f"| {B} | {X} | {fmt(pdiff(f, x, 'unfamiliar'))} | {fmt(pdiff(f, x, 'inlang'))} |")
        J["H2"][f"{B}/{X}"] = pdiff(f, x, "inlang")[1] > 0
# decisive: vs the better of the two fixed sweeps
dec = []
for B in BS:
    f = get("ag", "falsify", B, "ok").astype(float); sa, sb = get("ag", "sweepA", B, "ok").astype(float), get("ag", "sweepB", B, "ok").astype(float)
    better = sa if sa[gmask["inlang"]].mean() >= sb[gmask["inlang"]].mean() else sb; dec.append((B, pdiff(f, better, "inlang")))
P("\nDecisive comparison (vs the better fixed sweep, all in-language): " + "; ".join(f"B={B}: {fmt(t)}" for B, t in dec))
h2 = sum(t[1] > 0 for _, t in dec) >= 2; J["H2_supported"] = bool(h2)
P(f"\n**H2 {'SUPPORTED' if h2 else 'NOT SUPPORTED'}** (CI>0 against the better fixed sweep at {sum(t[1] > 0 for _, t in dec)} of 3 budgets; rule: >=2 budgets and CI>0 against every alternative listed in the protocol).\n")
P("Median RMSE by design (all in-language, B=3 / 5 / 8): " + "; ".join(f"{X}: " + " / ".join(f"{np.median(get('ag', X, B, 'rmse')[gmask['inlang']]):.3f}" for B in BS) for X in ("falsify", "sweepA", "sweepB", "random", "ens", "eig")) + "\n")

# ------------------------------------------------------- 3 epistemic
P("## 3. Criticism and abstention (agent[falsify]; modes: full = in-sample + out-of-sample chi-square + ambiguity; crit_in = in-sample + ambiguity; nocrit)\n")
P("| B | mode | coverage (in-lang) | precision P(ok given claim) | in-lang false rejection (abstain_ool) | in-lang abstain_amb | osc claim rate | osc claim with RMSE>tau | unreach claim&ok | decision accuracy (all 9 families) |\n|---|---|---|---|---|---|---|---|---|---|")
J["H3"] = {}
for B in BS:
    ok = get("ag", "falsify", B, "ok").astype(float)
    for mode in ("full", "crit_in", "nocrit"):
        o = outcomes("falsify", B, mode); claim = (o == "claim").astype(float)
        prec = (claim * ok); gm = gmask["inlang"]; precv = prec[gm].sum() / max(claim[gm].sum(), 1)
        right = np.where(fam == "osc", 1 - claim, claim * ok)
        row = dict(cov=ci(claim, "inlang"), fr=ci((o == "abstain_ool").astype(float), "inlang"), am=ci((o == "abstain_amb").astype(float), "inlang"),
                   osc=ci(claim, "osc"), oscbad=ci(claim * (1 - ok), "osc"), unr=ci(claim * ok, "unreach"), acc=ci(right, "inlang")[0])
        accall = float(right.mean())
        P(f"| {B} | {mode} | {fmt(row['cov'])} | {precv:.2f} | {fmt(row['fr'])} | {fmt(row['am'])} | {fmt(row['osc'])} | {fmt(row['oscbad'])} | {fmt(row['unr'])} | {accall:.2f} |")
        J["H3"][f"{B}/{mode}"] = dict(osc_claim=row["osc"][0], in_false_rej=row["fr"][0], unreach_ok=row["unr"][0], coverage=row["cov"][0], precision=float(precv), acc=accall)
P("\n**Per-family outcome shares, B=8, mode full** (claim / abstain_ool / abstain_amb):\n\n| family | claim | abstain_ool | abstain_amb |\n|---|---|---|---|")
o = outcomes("falsify", 8, "full")
for f in env.ALL_FAMS: m = fam == f; P(f"| {f} | {(o[m]=='claim').mean():.2f} | {(o[m]=='abstain_ool').mean():.2f} | {(o[m]=='abstain_amb').mean():.2f} |")

# AUROC osc vs in-language
def auroc(pos, neg):
    s = np.concatenate([pos, neg]); y = np.concatenate([np.ones(len(pos)), np.zeros(len(neg))]); r = s.argsort().argsort() + 1
    return (r[y == 1].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg))
P("\n**AUROC of the in-sample misfit statistic (-log10 min p) for osc vs in-language truth** (higher = better flag)\n\n| B | agent[falsify] | agent[sweepB] | grammar_sweep | bayes_declared (GOF, declared class) |\n|---|---|---|---|---|")
J["auroc"] = {}
for B in BS:
    cells = []
    for kind, n in [("ag", "falsify"), ("ag", "sweepB"), ("bs", "grammar_sweep"), ("bs", "bayes_declared")]:
        s = -np.log10(np.clip(get(kind, n, B, "p_in").astype(float), 1e-300, 1)); a = auroc(s[fam == "osc"], s[gmask["inlang"]]); cells.append(f"{a:.2f}")
        J["auroc"][f"{B}/{n}"] = a
    P(f"| {B} | " + " | ".join(cells) + " |")
P("\n**epsilon sensitivity (analysis only; primary eps=0.5 sigma-hat)**, agent[falsify], B=8, mode full: coverage / precision / decision accuracy\n")
for eps in (0.25, 0.5, 1.0, 2.0):
    sav = A.EPS; A.EPS = eps; o = outcomes("falsify", 8, "full"); claim = (o == "claim").astype(float); ok = get("ag", "falsify", 8, "ok").astype(float)
    right = np.where(fam == "osc", 1 - claim, claim * ok); gm = gmask["inlang"]; A.EPS = sav
    P(f"* eps={eps}: coverage {claim[gm].mean():.2f}, precision {(claim*ok)[gm].sum()/max(claim[gm].sum(),1):.2f}, accuracy {right.mean():.2f}")

# ---------------------------------------------------------- 4 representation
P("\n## 4. Representation role (H4)\n")
P("**Proposal recall@3** (true primitive among the 3 best-scoring primitives by BIC-penalised equation-error regression on the reconstructed hidden state; sweep-B data, 6 episodes; in-language families):\n\n| state | known | unfamiliar | all in-language |\n|---|---|---|---|")
rec = {}
for w in ("oracle", "analytic", "learned"):
    hit = np.array([float(any(e in r["proposal"][w][:3] for e in A.EXPECT[r["fam"]])) if r["fam"] in A.EXPECT else np.nan for r in res]); rec[w] = np.nan_to_num(hit)
    P(f"| {w}{' (privileged)' if w=='oracle' else ''} | {fmt(ci(rec[w], 'known'))} | {fmt(ci(rec[w], 'unfamiliar'))} | {fmt(ci(rec[w], 'inlang'))} |")
dl = pdiff(rec["learned"], rec["analytic"], "inlang"); dlu = pdiff(rec["learned"], rec["analytic"], "unfamiliar")
P(f"\nlearned minus analytic recall@3: in-language {fmt(dl)}, unfamiliar {fmt(dlu)}; oracle minus analytic: {fmt(pdiff(rec['oracle'], rec['analytic'], 'inlang'))}")
P("\n**SINDYc recovery by state set (B=8, in-language, library degree-1 tuned / dictionary):**\n\n| state set | linear library | dictionary library |\n|---|---|---|")
for m in ("raw", "embed", "learned", "oracle"):
    a = get("bs", "sindyc_" + m, 8, "ok").astype(float); b = get("bs", "sindyc_dict_" + m, 8, "ok").astype(float) if "sindyc_dict_" + m in res[0]["base"]["B"] else None
    P(f"| {m}{' (ORACLE)' if m=='oracle' else ''} | {fmt(ci(a, 'inlang'))} | {fmt(ci(b, 'inlang')) if b is not None else '–'} |")
dsl = pdiff(get("bs", "sindyc_learned", 8, "ok"), get("bs", "sindyc_embed", 8, "ok"), "inlang"); dsr = pdiff(get("bs", "sindyc_learned", 8, "ok"), get("bs", "sindyc_raw", 8, "ok"), "inlang")
P(f"\nSINDYc learned minus embed (B=8): {fmt(dsl)}; learned minus raw: {fmt(dsr)}.")
J["H4"] = dict(recall_learned_minus_analytic=dl, sindyc_learned_minus_embed=dsl)
mse = []
P("")

# ---------------------------------------------------------- 5 synergy
P("## 5. Decision accuracy (synergy and ablations, all 9 families; right = correct claim for in-language/unreach, abstention for osc)\n\n| variant | B=3 | B=5 | B=8 |\n|---|---|---|---|")
variants = [("full agent (falsify, criticism full)", "falsify", "full"), ("no criticism", "falsify", "nocrit"), ("in-sample criticism only", "falsify", "crit_in"), ("no active design: sweep B", "sweepB", "full"),
            ("no active design: sweep A", "sweepA", "full"), ("random design", "random", "full"), ("generic ensemble-variance design", "ens", "full"), ("declared-class EIG design (structure search kept)", "eig", "full"),
            ("no structure generation (declared class + EIG)", "declared_eig", "full"), ("no u2 interventions in pool", "falsify_nou2", "full")]
acc = {}
for lab, n, mode in variants:
    cells = []
    for B in BS:
        o = outcomes(n, B, mode); ok = get("ag", n, B, "ok").astype(float); claim = (o == "claim").astype(float); right = np.where(fam == "osc", 1 - claim, claim * ok); acc[(lab, B)] = right
        cells.append(fmt(ci(right, "inlang" if False else "inlang"), 2) if False else f"{right.mean():.2f}")
    P(f"| {lab} | " + " | ".join(cells) + " |")
P("\nPaired decision-accuracy difference, full agent minus variant (all 9 families pooled; CI over instances):\n")
full = {B: acc[(variants[0][0], B)] for B in BS}; allmask = np.ones(N, bool); gmask["all"] = allmask; boot_idx["all"] = rng.integers(0, N, (NB, N))
J["H5"] = {}
for lab, n, mode in variants[1:]:
    cells = []
    for B in BS:
        t = pdiff(full[B], acc[(lab, B)], "all"); cells.append(fmt(t)); J["H5"][f"{lab}/{B}"] = t[1] > 0
    P(f"* {lab}: " + " | ".join(f"B={B} {c}" for B, c in zip(BS, cells)))

json.dump(J, open(sys.argv[2].replace(".md", ".json"), "w"), indent=1, default=float)
open(sys.argv[2], "w").write("\n".join(lines)); print("\n".join(lines[:60]))
