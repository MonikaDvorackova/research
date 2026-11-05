"""Evaluation-only helpers (the agent never imports this module): structural equivalence (L2) and mechanistic identification (L3) against the frozen manifest,
and a coarse token-signature check for symbolic-regression equations."""
from __future__ import annotations
import re
from . import bench

# (term name, field in {'op','ip'} or 'gamma', truth value fn(inst), kind, tol)
PARAM = dict(
    sat=[("tanh(id)", "op", lambda i: i["P"]["p"], "abs", 0.15)],
    gate=[("gate(id)", "op", lambda i: i["P"]["p"], "abs", 0.10)],
    delay=[("id(delay)", "ip", lambda i: i["k"], "abs", 1.0)],
    sin=[("sin(id)", "op", lambda i: i["P"]["q"], "rel", 0.20)],
    rectsq=[("relu(sq)", "op", lambda i: i["P"]["p"], "abs", 0.07)],
    leak=[("id(lp)", "ip", lambda i: i["tau"], "rel", 0.25)],
    bilin=[("XINT", "gamma", lambda i: i["c"] * i["P"]["g"], "rel", 0.35)],
    bump=[("bump(id)", "op", lambda i: i["P"]["p"], "rel", 0.25)],
    gdelay=[("gate(delay)", "ip", lambda i: i["k"], "abs", 1.0), ("gate(delay)", "op", lambda i: i["P"]["p"], "abs", 0.10)],
    quadlag=[("sq(lp)", "ip", lambda i: i["tau"], "rel", 0.30)],
)


def tname(t): return f"{t[0]}({t[2]})"


def level2(fam, desc):
    sigs = bench.FAM[fam]["sig"]
    return any(set(desc) == set(s) for s in sigs)


def level3(fam, inst, terms, gamma, desc):
    if not level2(fam, desc): return False
    for (name, field, truth, kind, tol) in PARAM.get(fam, []):
        v = None
        if field == "gamma": v = gamma
        else:
            for t in terms:
                if tname(t) == name: v = t[1] if field == "op" else t[3]
        if v is None: return False
        tv = truth(inst); err = abs(v - tv) / (abs(tv) + 1e-9) if kind == "rel" else abs(v - tv)
        if err > tol: return False
    return True


def sr_signature(fam, eq):
    """Coarse structural check of a PySR equation string; None when not definable for the family."""
    lags = set(re.findall(r"\bl(\d)\b", eq)); has = lambda s: s in eq; var = bool(re.search(r"\b(x|l\d|x2h)\b", eq))
    if fam in ("lin", "sat", "quad", "gate", "delay", "leak", "quadlag", "saw"): return None
    if fam == "sin": return has("sin(")
    if fam == "rectsq": return has("max(") and has("square(")
    if fam == "bilin": return has("x2h")
    if fam == "bump": return has("exp(")
    if fam == "sqrtabs": return has("sqrt_abs") or has("sqrt(")
    if fam == "rate": return "1" in lags and bool(re.search(r"\bx\b", eq))
    if fam == "gdelay": return bool(lags & set("3456789")) and (has("max(") or has("sign("))
    if fam in ("thresh", "bumpfar"): return not var
    return None
